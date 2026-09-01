"""Section-level merge driver. Additive except where superseding a named fragment."""
import re, sys, json, collections, glob
dig = lambda s: collections.Counter(re.findall(r'\d', s))

def bsection(bfile, sec):
    cands = glob.glob(f"Corpus B/{bfile}*.md") + glob.glob(f"Corpus B-new/{bfile}*.md")
    lines = open(cands[0], encoding='utf-8').read().split('\n')
    s = next(i for i, l in enumerate(lines) if re.match(rf'^##\s+{re.escape(sec)}\s', l))
    e = len(lines)
    for j in range(s+1, len(lines)):
        if re.match(r'^##\s+\d', lines[j]): e = j; break
        if 'Cross-references' in lines[j] and lines[j].lstrip().startswith('>'): e = j; break
    out = lines[s:e]
    while out and out[-1].strip() in ('', '---'): out.pop()
    return cands[0], out

def run(cfg):
    bpath, sec_lines = bsection(cfg['bfile'], cfg['sec'])
    text = '\n'.join(sec_lines)
    for pat, rep in cfg.get('linkmap', []):
        text = re.sub(pat, rep, text)
    for old, new in cfg.get('retarget', []):
        if text.count(old) != 1:
            raise SystemExit(f"RETARGET NOT UNIQUE ({text.count(old)}x): {old[:60]!r}")
        text = text.replace(old, new)
    title = re.sub(r'^##\s*[\d.]+\s*', '', sec_lines[0])
    body = '\n'.join(text.split('\n')[1:]).strip('\n')
    # B's internal subheadings carry ITS numbering (### 0.1.1 Mx - Immediate). Left as-is
    # they collide with the destination's scheme and make a section number ambiguous:
    # base-A 03_Gastrointestinal had 0 duplicate section numbers, and merging C1-C3 with
    # B's numbers intact produced 26. Rescope them under the block's own number instead,
    # which keeps B's structure and stays unique.
    num_for_sub = cfg.get('number', '')
    def _resub(m):
        lvl, tail = m.group(1), m.group(3)
        lvl = '#' * min(6, len(lvl) + 1)
        if num_for_sub:
            return f"{lvl} {num_for_sub}.{m.group(2).split('.')[-1]} {tail}"
        # UNNUMBERED DESTINATION. Dropping B's number leaves bare `#### Mx - Immediate`,
        # which every B section emits, so n sections merged into one unnumbered file give
        # an n-way duplicate heading. base-A 04_Neurology had 0 duplicate headings and the
        # first six D1 blocks produced 18 headings collapsing to 3 names. There is no
        # destination number to scope under, so scope under the block's own provenance
        # coordinates instead - unique by construction, since bfile+section is.
        return f"{lvl} {tail} \u2014 {cfg['bfile'].split('_')[0]} \u00a7{cfg['sec']}.{m.group(2).split('.')[-1]}"
    body = re.sub(r'(?m)^(#{3,6})\s+(\d+\.[\d.]+)\s+(.*)$', _resub, body)
    nb = ("\n`NO-BASELINE — absent from the corpus before this merge; no inherited layer "
          "disagrees with it.`") if cfg.get('no_baseline') else ""
    note = f"\n*{cfg['note']}*" if cfg.get('note') else ""
    num = cfg.get('number', '')
    mk = f" {cfg['marker']}" if cfg.get('marker') else ''
    block = (f"### {num}{' ' if num else ''}{title} — from unverified layer{mk}\n"
             f"`SRC:{cfg['bfile']} §{cfg['sec']}` "
             f"`UNVERIFIED — model knowledge, not source-checked.`{nb}{note}\n\n{body}")

    p = cfg['dest']; src = open(p, encoding='utf-8').read(); lines = src.split('\n')
    before = dig(src); nlines_before = len(lines)
    if cfg.get('supersede'):
        s = next(i for i, l in enumerate(lines) if l.startswith(cfg['supersede']))
        e = next(i for i, l in enumerate(lines) if i > s and re.match(r'^#{1,3} ', l))
        # THE END BOUNDARY IS NOT ONLY THE NEXT HEADING. A merged block written as a
        # callout (`> [!info] Added from unverified layer — …`) carries no heading at all,
        # so a second block sitting between this fragment and the next heading falls
        # INSIDE the deletion range. Found on D4 §0.6, where an L3 block with its own
        # SRC: token and a NO-BASELINE marker sat between the D4 fragment and
        # `### Diabetic Neuropathy`. Stop at the next foreign SRC: token instead, backing
        # up over its own callout so the block is not cut in half.
        # A SRC: token QUOTED INSIDE A CONFLICT BLOCK is provenance in an argument, not
        # the header of a different merged block. CF-038 writes
        #   > **B (`unverified`, `SRC:C1_Acute_Abdomen §0.2`, the callout above):** …
        # and reading that as a block boundary truncated the fragment, leaving an orphan.
        # A real block header is a line that STARTS with the SRC token (optionally after
        # a callout marker) - never one where it appears mid-sentence.
        def _is_block_header(l):
            t = l.lstrip()
            while t.startswith('>'):
                t = t[1:].lstrip()
            return t.startswith('`SRC:')
        for j in range(s + 2, e):
            if 'SRC:' in lines[j] and _is_block_header(lines[j]):
                k = j
                # Walk back over the CONTIGUOUS callout only. Including blank lines lets
                # the walk cross block boundaries and swallow backwards: on D4 §0.6 it
                # ran from the L3 callout all the way to the fragment's own SRC line,
                # superseding 2 lines instead of 16 and leaving the fragment's callouts
                # behind. Caught by the superseded-line count, not by the write failing.
                while k > s + 1 and lines[k - 1].lstrip().startswith('>'):
                    k -= 1
                while k > s + 1 and lines[k - 1].strip() == '':
                    k -= 1
                e = k
                break
        # A supersede must consume the FRAGMENT, not everything up to the next heading.
        # Destination prose can follow the fragment with no heading, no SRC: token, no
        # marker and no digit - invisible to every other check. D5 §0.4 deleted
        # `**P (vertigo generally):** …`, the vertigo entry's own prognosis line, and
        # printed OK. A blank-line RUN (two or more) ends the fragment: the block format
        # separates its own parts by exactly one.
        for j in range(s + 2, e - 1):
            if lines[j].strip() == '' and lines[j + 1].strip() == '':
                e = j
                break
        while e > s + 1 and lines[e - 1].strip() == '':
            e -= 1
        removed = e - s
        # NEVER delete a CONFLICT block when superseding a fragment. Lift it out and
        # re-attach it below the merged section. 1.12: no agent edits a conflict block.
        frag = lines[s:e]; carried = []
        i = 0
        while i < len(frag):
            if re.match(r'^>\s*\[!fail\]', frag[i]):
                j = i
                while j < len(frag) and frag[j].startswith('>'): j += 1
                carried += frag[i:j] + ['']
                i = j
            else:
                i += 1
        if carried:
            block = block + '\n\n' + '\n'.join(carried).rstrip('\n')
        # HARD REFUSAL. A supersede replaces the fragment's PROSE. It must never delete an
        # annotation ON the destination: a CONFLICT block, a VERIFIED box, or an
        # UNVERIFIED/VERIFIED marker. Digit checks cannot see an annotation with no digits
        # in it, so this is checked structurally and refuses rather than warns.
        PROT = [(r'^>\s*\[!fail\]', 'CONFLICT block'),
                (r'^>\s*\[!check\]', 'VERIFIED [!check] box'),
                (r'`VERIFIED [^`]*`', 'VERIFIED marker'),
                # UNVERIFIED was named in the instruction and omitted from this list. Seven
                # were destroyed by supersedes before it was noticed. A fragment's body
                # UNVERIFIED marker names the specific source that would settle a specific
                # question (§1.7); the replacement section's own marker asks something else.
                (r'`UNVERIFIED[^`]*`', 'UNVERIFIED marker'),
                (r'`CF-\d{3}`', 'inline CF marker'),
                (r'`NO-BASELINE[^`]*`', 'NO-BASELINE marker'),
                # AUDITED against §1.7's full marker inventory rather than extended one
                # item at a time as each gets destroyed. §1.7 defines seven marker types:
                #   UNVERIFIED  VERIFIED  CF-###  [paed]/[adult]  →MED:  TODO:link  SRC:
                # The first three were covered; the next three were not, and are added
                # here. SRC: is deliberately NOT protected - it is the fragment's own
                # provenance and the new block writes its own.
                # Callouts other than [!fail]/[!check] ([!danger], [!warning], [!tip])
                # are CONTENT, not annotations on the destination - B's sections carry
                # them too - so they stay out on purpose.
                (r'`\[(?:paed|adult)\]`', 'population-scope marker'),
                (r'`→MED:[^`]*`', 'dose-mirror marker'),
                (r'`TODO:link[^`]*`', 'TODO:link marker')]
        lost = []
        for pat, name in PROT:
            # A line carrying the fragment's own SRC: token IS the fragment's marker line,
            # not an annotation on the destination — the new block writes its own.
            was = [l for l in frag if re.search(pat, l) and 'SRC:' not in l]
            for l in was:
                if pat.startswith('^>'):
                    # a callout block: the whole line must survive verbatim
                    if l not in block:
                        lost.append(f"{name}: {l.strip()[:90]}")
                else:
                    # an inline marker: what must survive is the MARKER, not its host line,
                    # because the new block rewrites the heading it was attached to
                    for tok in re.findall(pat, l):
                        if tok not in block:
                            lost.append(f"{name}: {tok}")
        # The rule says a supersede INHERITS the fragment's cross-references. Every
        # supersede so far has silently dropped some, caught only by reading the digit
        # multiset by hand. Check it structurally instead.
        # \d.]+ greedily eats a sentence-ending period, so §0.17 and §0.17. compare
        # unequal and the refusal fires on a reference that IS carried.
        refs = lambda t: set(x.rstrip('.') for x in
                             re.findall(r'\[\[([^\]]+)\]\]|(§[\d.]+)', t)
                             for x in x if x)
        # A `SRC:<file> §n.n` token is PROVENANCE, not a pointer, and a fragment built from
        # two B sections carries two of them. Counting those as cross-references makes the
        # refusal fire on the section number the merge is replacing. Exclude SRC lines from
        # the fragment side, exactly as the PROT loop above already does.
        lost_refs = refs('\n'.join(l for l in frag if 'SRC:' not in l)) - refs(block)
        # A fragment assembled from TWO B sections legitimately splits its pointers
        # between the two blocks that replace it. `carry_refs` declares a pointer as
        # relocated - but the driver VERIFIES it is actually in the destination before
        # accepting the claim, so a declaration cannot excuse a loss.
        for r in cfg.get('carry_refs', []):
            if r in lost_refs:
                # ...against the destination WITHOUT the fragment. Checking the whole file
                # finds the pointer in the fragment that is about to be deleted, so the
                # guard passes on exactly the case it exists to catch. Caught by the
                # known-answer test, not by reading this code.
                if r in '\n'.join(lines[:s] + lines[e:]):
                    lost_refs.discard(r)
                else:
                    lost.append(f"carry_refs declared {r!r} relocated, but it is NOT in {p}")
        for r in sorted(lost_refs):
            lost.append(f"cross-reference: {r}")
        if lost:
            raise SystemExit("*** SUPERSEDE REFUSED — would delete destination annotation(s):\n    "
                             + "\n    ".join(lost)
                             + "\n    Carry them into the block, or place without superseding.")
        out = lines[:s] + block.split('\n') + [''] + lines[e:]
    else:
        h = cfg['heading']; s = next(i for i, l in enumerate(lines) if l.strip() == h.strip())
        lvl = len(re.match(r'^(#+)', lines[s]).group(1)); e = len(lines)
        for j in range(s+1, len(lines)):
            m = re.match(r'^(#{1,6}) ', lines[j])
            if m and len(m.group(1)) <= lvl: e = j; break
        while e > s+1 and lines[e-1].strip() == '': e -= 1
        removed = 0
        out = lines[:e] + [''] + block.split('\n') + [''] + lines[e:]
    new = '\n'.join(out); open(p, 'w', encoding='utf-8').write(new)
    after = dig(new)
    probes = [l for l in block.split('\n') if len(l.strip()) > 60][:3]
    miss = [x for x in probes if x not in new]
    dupset = lambda ls: {h for h, c in collections.Counter(
        [l for l in ls if re.match(r'^#{2,6} ', l)]).items() if c > 1}
    dup = sorted(dupset(out) - dupset(lines))
    print(f"  {cfg['bfile']} §{cfg['sec']} -> {p}")
    print(f"    block {len(block.split(chr(10)))} lines | superseded {removed} lines")
    print(f"    digits added {dict(after-before) or '{}'} | REMOVED {dict(before-after) or '{}'}")
    print(f"    probes missing {len(miss)} | NEW duplicate headers {len(dup)}"
          + (" " + repr(dup) if dup else ""))
    ok = not miss and not dup and (cfg.get('supersede') or not (before-after))
    print(f"    {'OK' if ok else '*** CHECK ***'}")
    return ok

if __name__ == '__main__':
    for cfg in json.load(open(sys.argv[1])): run(cfg)
