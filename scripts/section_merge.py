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
        return f"{lvl} {tail}"
    body = re.sub(r'(?m)^(#{3,6})\s+(\d+\.[\d.]+)\s+(.*)$', _resub, body)
    nb = ("\n`NO-BASELINE — absent from the corpus before this merge; no inherited layer "
          "disagrees with it.`") if cfg.get('no_baseline') else ""
    note = f"\n*{cfg['note']}*" if cfg.get('note') else ""
    num = cfg.get('number', '')
    block = (f"### {num}{' ' if num else ''}{title} — from unverified layer\n"
             f"`SRC:{cfg['bfile']} §{cfg['sec']}` "
             f"`UNVERIFIED — model knowledge, not source-checked.`{nb}{note}\n\n{body}")

    p = cfg['dest']; src = open(p, encoding='utf-8').read(); lines = src.split('\n')
    before = dig(src); nlines_before = len(lines)
    if cfg.get('supersede'):
        s = next(i for i, l in enumerate(lines) if l.startswith(cfg['supersede']))
        e = next(i for i, l in enumerate(lines) if i > s and re.match(r'^#{1,3} ', l))
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
                (r'`CF-\d{3}`', 'inline CF marker'),
                (r'`NO-BASELINE[^`]*`', 'NO-BASELINE marker')]
        lost = []
        for pat, name in PROT:
            # A line carrying the fragment's own SRC: token IS the fragment's marker line,
            # not an annotation on the destination — the new block writes its own.
            was = [l for l in frag if re.search(pat, l) and 'SRC:' not in l]
            for l in was:
                if l not in block:
                    lost.append(f"{name}: {l.strip()[:90]}")
        # The rule says a supersede INHERITS the fragment's cross-references. Every
        # supersede so far has silently dropped some, caught only by reading the digit
        # multiset by hand. Check it structurally instead.
        # \d.]+ greedily eats a sentence-ending period, so §0.17 and §0.17. compare
        # unequal and the refusal fires on a reference that IS carried.
        refs = lambda t: set(x.rstrip('.') for x in
                             re.findall(r'\[\[([^\]]+)\]\]|(§[\d.]+)', t)
                             for x in x if x)
        lost_refs = refs('\n'.join(frag)) - refs(block)
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
    hdrs = [l for l in out if re.match(r'^#{2,6} ', l)]
    dup = [h for h, c in collections.Counter(hdrs).items() if c > 1]
    print(f"  {cfg['bfile']} §{cfg['sec']} -> {p}")
    print(f"    block {len(block.split(chr(10)))} lines | superseded {removed} lines")
    print(f"    digits added {dict(after-before) or '{}'} | REMOVED {dict(before-after) or '{}'}")
    print(f"    probes missing {len(miss)} | duplicate headers {len(dup)}")
    ok = not miss and not dup and (cfg.get('supersede') or not (before-after))
    print(f"    {'OK' if ok else '*** CHECK ***'}")
    return ok

if __name__ == '__main__':
    for cfg in json.load(open(sys.argv[1])): run(cfg)
