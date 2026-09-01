"""Figure comparison: B section against the destination AS IT STOOD BEFORE the merge.

Comparing against the CURRENT tree compares B against itself - the merged block is in
there - and reports clean for the wrong reason. Every destination here is reconstructed
from git at the parent of the commit that merged the section.

A "figure" is a number with a unit. Two figures CONFLICT when they share a unit and an
anchor term but differ in value. The anchor is the nearest preceding clinical word, which
is crude - so this reports CANDIDATES for reading, never verdicts.
"""
import re, sys, json, subprocess, collections, glob

UNIT = (r'(?:mg/kg/h|mg/kg|mcg/kg/min|mcg/kg|micrograms?|mmol/L|mmol|mg/dL|g/L|g/dL|IU/L|U/L|'
        r'mL/kg/h|mL/kg|mL/h|mL|L/min|mg|mcg|µg|kg|cm|mm|hours?|hrs?|h\b|days?|weeks?|months?|'
        r'years?|minutes?|mins?|%|bpm|mmHg|units?)')
RE_FIG = re.compile(r'(\d+(?:\.\d+)?)\s*(' + UNIT + r')', re.I)
# The anchor must be a CLINICAL word. Without a full stop-list it lands on "takes",
# "about", "within" - which match everything and make the comparison meaningless.
STOP = set('''the a an of in for with and or to is are be at on by from that this it as if
 not no all any per over under more less than which where when who whom whose then than
 takes take taken about within beyond after before during through across around near
 first second third last next only just even also still yet once twice more most least
 usually often sometimes rarely never always typically generally commonly frequently
 significant significantly approximately roughly nearly almost around under over above
 below into onto upon while whilst whereas because since although though however
 including includes include such same other others another each every both either
 neither some many much few little several various numerous multiple single
 patient patients case cases time times point points level levels value values
 give given gives giving use used using make made makes making been being have has had
 will would should could must may might can cannot does did done doing
 measured rising falling raised elevated normal abnormal high low
 lasting lasts last duration persisting persists continuing occurring occurs
 hours hour days day weeks week months month years year minutes minute'''.split())

def figures(text):
    """(anchor, value, unit, sentence) for every number+unit in the text."""
    out=[]
    for para in re.split(r'\n', text):
        if para.strip().startswith('`SRC:'): continue
        for m in RE_FIG.finditer(para):
            before = re.sub(r'[^a-zA-Z ]',' ', para[:m.start()]).split()
            anchor = next((w.lower() for w in reversed(before)
                           if len(w) > 3 and w.lower() not in STOP), '')
            out.append((anchor, m.group(1), m.group(2).lower().rstrip('.'), para.strip()[:200]))
    return out

def bsection(bfile, sec):
    cands = glob.glob(f"Corpus B/{bfile}*.md") + glob.glob(f"Corpus B-new/{bfile}*.md")
    lines = open(cands[0], encoding='utf-8').read().split('\n')
    s = next(i for i,l in enumerate(lines) if re.match(rf'^##\s+{re.escape(sec)}\s', l))
    e = len(lines)
    for j in range(s+1, len(lines)):
        if re.match(r'^##\s+\d', lines[j]): e=j; break
        if 'Cross-references' in lines[j] and lines[j].lstrip().startswith('>'): e=j; break
    return '\n'.join(lines[s:e])

def compare(bfile, sec, commit, dest):
    """dest AS IT STOOD at commit^ - never the current tree."""
    before = subprocess.run(['git','show',f'{commit}^:{dest}'],
                            capture_output=True, text=True).stdout
    if not before: return None
    B = figures(bsection(bfile, sec))
    D = figures(before)
    dmap = collections.defaultdict(set)
    dsent = {}
    for a,v,u,s in D:
        if a: dmap[(a,u)].add(v); dsent.setdefault((a,u,v), s)
    hits=[]
    for a,v,u,s in B:
        if not a: continue
        vals = dmap.get((a,u))
        if vals and v not in vals:
            hits.append(dict(anchor=a, unit=u, b_value=v, dest_values=sorted(vals),
                             b_sentence=s, dest_sentence=dsent.get((a,u,sorted(vals)[0]),'')))
    return dict(bfile=bfile, sec=sec, b_figures=len(B), dest_figures=len(D),
                comparable=len([1 for a,v,u,_ in B if (a,u) in dmap]), conflicts=hits)

if __name__ == '__main__':
    plan = json.load(open(sys.argv[1]))
    tot=collections.Counter(); allhits=[]
    for row in plan:
        r = compare(row['bfile'], row['sec'], row['commit'], row['dest'])
        if r is None:
            print(f"  {row['bfile'][:22]:<22} §{row['sec']:<5} dest not in tree at {row['commit'][:7]}^"); continue
        tot['sections']+=1; tot['bfig']+=r['b_figures']; tot['dfig']+=r['dest_figures']
        tot['cmp']+=r['comparable']; tot['conf']+=len(r['conflicts'])
        allhits += [(row['bfile'], row['sec'], h) for h in r['conflicts']]
        print(f"  {row['bfile'][:22]:<22} §{row['sec']:<5} B figs {r['b_figures']:>3}  dest figs {r['dest_figures']:>4}  "
              f"comparable {r['comparable']:>3}  candidates {len(r['conflicts'])}")
    print(f"\n  SECTIONS {tot['sections']} | B figures {tot['bfig']} | destination figures {tot['dfig']} | "
          f"COMPARISONS MADE {tot['cmp']} | CANDIDATE MISMATCHES {tot['conf']}")
    json.dump([{'bfile':b,'sec':s,**h} for b,s,h in allhits],
              open('/tmp/figcheck_hits.json','w'), indent=1)
