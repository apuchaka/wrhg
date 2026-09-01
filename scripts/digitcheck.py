#!/usr/bin/env python3
"""Per-section digit multiset, split into STRUCTURAL and PROSE.

The raw multiset always differs between a B section and its merged block, for reasons
that are never clinical:

  * B's `## 0.n` heading carries its number; an unnumbered destination's block does not
  * the awk/section range overruns into the NEXT `## 0.n` heading
  * the subheading rescope writes provenance tokens - `### Mx - Immediate - A6 §0.1.1`
  * the block writes its own `SRC:<bfile> §<sec>` line
  * a wikilink or TODO:link marker contains digits from a FILENAME

So the raw comparison produces a difference on every single section, and a difference
that is always present is a difference nobody reads. That is the vacuous-check shape:
it cannot fail informatively.

This splits the count. STRUCTURAL digits are allowed to differ and are reported for
information. PROSE digits are the clinical figures, and they must match EXACTLY - a
single missing digit there is a lost dose, threshold, ratio or duration.

Usage: digitcheck.py <bfile> <sec> <destfile> <block-heading-substring>
"""
import re, sys, glob, collections

LINK  = re.compile(r'\[\[[^\]]*\]\]|`TODO:link[^`]*`')
SRCL  = re.compile(r'`SRC:[^`]*`')
HEAD  = re.compile(r'^#{2,6}\s')
BNUM  = re.compile(r'^(#{2,6})\s+\d+\.[\d.]*\s')
RESC  = re.compile(r'\s+—\s+[A-Za-z0-9\-]+ §[\d.]+\s*$')

UNIT = re.compile(r'\s*(?:mg|mcg|g|kg|mL|ml|L|%|h|hr|hrs|hours?|min|mins|minutes?|days?|'
                  r'weeks?|months?|years?|°C|C|mmHg|mmol|mol|IU|units?|/)')

def split(text, secnums=()):
    """-> (structural Counter, prose Counter). Links, SRC lines, headings are structural.

    A bare `0.2` in prose is a POINTER at a B section, not a figure, and a retarget that
    swaps it for a heading name therefore removes prose digits without losing anything
    clinical. Found on A6 §0.1, where `See 0.2 for heat stroke` became `See Heat Stroke
    and Severe Hyperthermia below` and the check reported two prose digits lost.
    Such a token counts as structural ONLY when it is a real section number of the B file
    being merged AND is not followed by a unit - so `0.5` the section is structural and
    `0.5 mg` the dose stays prose.
    """
    st, pr = collections.Counter(), collections.Counter()
    secre = re.compile(r'§?\b(' + '|'.join(re.escape(s) for s in sorted(secnums, key=len,
                       reverse=True)) + r')\b') if secnums else None
    for line in text.split('\n'):
        rest = line
        for m in LINK.finditer(line): st.update(re.findall(r'\d', m.group(0)))
        rest = LINK.sub('', rest)
        for m in SRCL.finditer(rest):  st.update(re.findall(r'\d', m.group(0)))
        rest = SRCL.sub('', rest)
        if secre and not HEAD.match(rest):
            def _sec(m):
                tail = rest[m.end():]
                if UNIT.match(tail): return m.group(0)      # a figure with a unit: keep in prose
                st.update(re.findall(r'\d', m.group(0))); return ''
            rest = secre.sub(_sec, rest)
        if HEAD.match(rest):
            # a heading contributes only structure: B's own number, or the rescope token
            st.update(re.findall(r'\d', rest)); continue
        pr.update(re.findall(r'\d', rest))
    return st, pr

def secnums(bfile):
    c = glob.glob(f"Corpus B/{bfile}*.md") + glob.glob(f"Corpus B-new/{bfile}*.md")
    txt = open(c[0], encoding='utf-8').read()
    return set(re.findall(r'^#{2,6}\s+(\d+\.[\d.]*\d)\s', txt, re.M))

def bsection(bfile, sec):
    c = glob.glob(f"Corpus B/{bfile}*.md") + glob.glob(f"Corpus B-new/{bfile}*.md")
    ls = open(c[0], encoding='utf-8').read().split('\n')
    s = next(i for i, l in enumerate(ls) if re.match(rf'^##\s+{re.escape(sec)}\s', l))
    e = len(ls)
    for j in range(s + 1, len(ls)):
        if re.match(r'^##\s+\d', ls[j]): e = j; break
        if 'Cross-references' in ls[j] and ls[j].lstrip().startswith('>'): e = j; break
    out = ls[s:e]
    while out and out[-1].strip() in ('', '---'): out.pop()
    return '\n'.join(out)

def block(dest, headsub):
    ls = open(dest, encoding='utf-8').read().split('\n')
    s = next(i for i, l in enumerate(ls) if headsub in l and HEAD.match(l))
    lvl = len(re.match(r'^(#+)', ls[s]).group(1)); e = len(ls)
    for j in range(s + 1, len(ls)):
        m = re.match(r'^(#{1,6})\s', ls[j])
        if m and len(m.group(1)) <= lvl: e = j; break
    return '\n'.join(ls[s:e])

if __name__ == '__main__':
    bf, sec, dest, headsub = sys.argv[1:5]
    S = secnums(bf)
    bs, bp = split(bsection(bf, sec), S)
    ds, dp = split(block(dest, headsub), S)
    print(f"  STRUCTURAL  B {dict(sorted(bs.items()))}")
    print(f"              block {dict(sorted(ds.items()))}   (allowed to differ)")
    print(f"  PROSE       B {dict(sorted(bp.items()))}")
    print(f"              block {dict(sorted(dp.items()))}")
    lost, gained = bp - dp, dp - bp
    if not lost and not gained:
        print("  PROSE DIGITS IDENTICAL — no clinical figure lost or invented")
        sys.exit(0)
    if lost:   print(f"  *** PROSE DIGITS LOST:    {dict(sorted(lost.items()))}")
    if gained: print(f"  *** PROSE DIGITS GAINED:  {dict(sorted(gained.items()))}")
    print("  Read the digit-bearing prose lines on both sides before committing.")
    sys.exit(1)
