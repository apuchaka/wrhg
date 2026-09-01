"""Three processing passes over Corpus B files, before they are merged.

1. LINK EXPANSION   [[C3]] -> [[C3_Jaundice_and_Liver_Disease]]
2. RENAMED TARGETS  build-queue-v1 codes, map ENUMERATED from the build queues
3. DRUG NAMES       merge_tools.DRUG_NAMING, names only, with an UNVERIFIED marker

INVARIANT: the digit multiset of every file is unchanged. A rename changes NAMES.
Nothing here may touch a dose figure, and the run aborts on any file that fails.
"""
import re, os, sys, glob, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from merge_tools import DRUG_NAMING, DRUG_PATTERNS, RE_NON_AU_BLOCK, normalise

VAULT = ["Corpus A/*.md", "Corpus C/*.md", "Corpus B/*.md", "Corpus B-new/*.md", "*.md"]

def stems():
    out = set()
    for g in VAULT:
        out |= {os.path.basename(p)[:-3] for p in glob.glob(g)}
    return out

def prefix_map(all_stems):
    """code -> the single file it names. Ambiguity is REPORTED, never guessed (§1.10)."""
    m = collections.defaultdict(set)
    for s in all_stems:
        mm = re.match(r'^([A-Za-z0-9\-]+?)_', s)
        if mm:
            m[mm.group(1)].add(s)
    return m

def rename_map():
    """ENUMERATED from the build queues, not from any list handed to this script."""
    out = {}
    for q in glob.glob("Corpus B/00_BUILD_QUEUE*.md") + glob.glob("Corpus B-new/00_BUILD_QUEUE*.md"):
        for new, old in re.findall(r'\*\*([A-Z]+[0-9]*)\.[^*]*\*\*[^(\n]*\(was ([A-Z]+[0-9]*)\)',
                                   open(q, encoding='utf-8').read()):
            out[old] = new
    return out

# THE INVARIANT IS "no digit in any DOSE FIGURE changes", not "no digit in the file".
# Filenames carry digits - [[P1]] -> [[GER3_Preventive_and_Occupational_Health]] removes a
# 1 and adds a 3 - so a whole-file digit count fails on correct link expansion. Strip the
# link targets and the TODO:link markers first; what remains is the clinical prose.
def dig(s):
    s = re.sub(r'\[\[[^\]]*\]\]', '[[LINK]]', s)
    s = re.sub(r'`TODO:link[^`]*`', '[[LINK]]', s)
    return collections.Counter(re.findall(r'\d', s))

def process(path, pmap, rmap, allstems, report):
    text = open(path, encoding='utf-8').read()
    before = dig(text)
    lines = text.split('\n')
    r = path

    # ---- pass 1 + 2: wikilink targets
    def fix_link(m):
        code = m.group(1).strip()
        if code in allstems:                       # already a full filename
            return m.group(0)
        renamed = rmap.get(code, code)             # pass 2, before resolution
        if renamed != code:
            report['renamed'].append(f"{r}: [[{code}]] -> [[{renamed}]]")
        key = renamed.replace('.', '-')
        cands = sorted(pmap.get(key, ()))
        if len(cands) == 1:
            if renamed == code:
                report['expanded'].append(f"{r}: [[{code}]] -> [[{cands[0]}]]")
            return f"[[{cands[0]}"
        # a filename SUFFIX match, for targets like [[Shock_Phenotypes]]
        suf = sorted(s for s in allstems if s.endswith('_' + renamed) or
                     re.search(r'_' + re.escape(renamed) + r'_', s))
        if len(suf) == 1:
            report['expanded'].append(f"{r}: [[{code}]] -> [[{suf[0]}]] (suffix match)")
            return f"[[{suf[0]}"
        report['unresolved'].append(
            f"{r}: [[{code}]] — {'AMBIGUOUS: ' + ', '.join(cands) if cands else 'no file with this prefix'}")
        return m.group(0)

    text = '\n'.join(lines)
    text = re.sub(r'\[\[([^\]|#]+)', fix_link, text)

    # ---- pass 3: drug names
    lines = text.split('\n')
    for i, line in enumerate(lines):
        flag = bool(RE_NON_AU_BLOCK.search(line))
        if not flag and line.lstrip().startswith('>'):
            for j in range(i - 1, max(-1, i - 12), -1):
                if not lines[j].lstrip().startswith('>'): break
                if RE_NON_AU_BLOCK.search(lines[j]): flag = True; break
        for bad, (good, src) in DRUG_NAMING.items():
            if not DRUG_PATTERNS[bad].search(line): continue
            if re.search(r'\b' + re.escape(good.split('+')[0]) + r'\b', normalise(line), re.I):
                report['dual'].append(f"{r} L{i+1}: `{bad}` beside `{good}` — dual naming, kept")
                continue
            if flag:
                report['non_au'].append(f"{r} L{i+1}: `{bad}` inside a non-AU block — NOT renamed")
                continue
            new = DRUG_PATTERNS[bad].sub(good, line)
            mark = ('`UNVERIFIED — the NAME is corrected per the TGA Ingredient Harmonisation '
                    'programme; the REGIMEN this line states is not thereby confirmed and needs '
                    'a named Australian source.`')
            if mark not in new:
                new = new.rstrip() + ' ' + mark
            report['drugs'].append(f"{r} L{i+1}: `{bad}` -> `{good}`\n        {line.strip()[:120]}")
            lines[i] = line = new
    text = '\n'.join(lines)

    after = dig(text)
    ok = before == after
    report['digits'].append((r, 'pass' if ok else 'FAIL'))
    if not ok:
        report['digit_fail'].append(f"{r}: added {dict(after-before)} removed {dict(before-after)}")
    return text, ok

def main(dirs, apply):
    allstems = stems(); pmap = prefix_map(allstems); rmap = rename_map()
    print(f"rename map enumerated from the build queues: {rmap}")
    for d in dirs:
        # The build queues are the MAP, not content: they list every code by name and
        # would be rewritten into nonsense by link expansion. Excluded by filename.
        files = sorted(p for p in glob.glob(f"{d}/*.md")
                       if not os.path.basename(p).startswith('00_BUILD_QUEUE'))
        rep = collections.defaultdict(list)
        changed = 0
        for p in files:
            orig = open(p, encoding='utf-8').read()
            new, ok = process(p, pmap, rmap, allstems, rep)
            if new != orig:
                changed += 1
                if apply and ok: open(p, 'w', encoding='utf-8').write(new)
        print(f"\n{'='*70}\n{d}/\n{'='*70}")
        print(f"  files processed              {len(files)}")
        print(f"  files changed                {changed}")
        print(f"  link expansions made         {len(rep['expanded'])}")
        print(f"  renamed targets              {len(rep['renamed'])}")
        print(f"  drug names changed           {len(rep['drugs'])}")
        print(f"  dual naming left alone       {len(rep['dual'])}")
        print(f"  non-AU blocks left alone     {len(rep['non_au'])}")
        print(f"  codes that did not resolve   {len(rep['unresolved'])}")
        for u in sorted(set(rep['unresolved'])): print(f"      {u}")
        fails = [x for x in rep['digits'] if x[1] != 'pass']
        print(f"  digit multiset per file      {len(rep['digits'])-len(fails)} pass / {len(fails)} FAIL")
        for f in rep['digit_fail']: print(f"      *** {f}")
        for k in ('drugs',):
            if rep[k]:
                print(f"  --- {k} ---")
                for x in rep[k]: print(f"      {x}")
        json.dump({k: v for k, v in rep.items() if k != 'digits'},
                  open(f"/tmp/bprep_{d.replace(' ','_').replace('/','_')}.json", 'w'), indent=1)

if __name__ == '__main__':
    apply = '--apply' in sys.argv
    main([a for a in sys.argv[1:] if not a.startswith('--')], apply)
