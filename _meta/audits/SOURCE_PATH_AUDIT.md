---
name: Source-path audit
description: Which directory every merged section was actually read from, resolved against the filesystem.
built: 2026-09-01
---

# Source-path audit — which directory each merged section came from

Asked for because the run order's "73 files in `Corpus B-new/`" is a figure carried
across several hours from a decision made before the run started — the same shape as the
CLAUDE.md §1.10 row that was true of one directory and became false by being quoted as a
fact about the project.

**Nothing here is read from the run order or from a placement record.** Every path is
resolved live, through the same call the driver makes.

## How the driver resolves a B file

```python
def bsection(bfile, sec):
    cands = glob.glob(f"Corpus B/{bfile}*.md") + glob.glob(f"Corpus B-new/{bfile}*.md")
    lines = open(cands[0], encoding='utf-8').read().split('\n')
```

`Corpus B/` is searched first, so it wins wherever both hold a file with that prefix.
**Where only `Corpus B-new/` has one, it is read from there silently** — there is no
warning and no record in the block.

## THE ANSWER: every section merge came from `Corpus B/`

| | n |
|---|---:|
| section-merge commits, B file re-resolved against the tree | **74** |
| …resolving to `Corpus B/` | **74** |
| …resolving to `Corpus B-new/` | **0** |

Eleven B files: C1–C7, D1–D4. **Each also exists in `Corpus B-new/`**, so `cands[0]` was
choosing on every one of them rather than being uncontested.

`D4 §0.3`, opened live at the time of asking:

```
resolution candidates: ['Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md',
                        'Corpus B-new/D4_Weakness__Neuropathy_and_Radiculopathy.md']
OPENED: /home/user/wrhg/Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md
first line: ## 0.3 Radiculopathy
```

## 47 SRC tokens IN THE VAULT do come from `Corpus B-new/` — all from the fragment phase

Counted independently, by asking git which commit first wrote each token:

```
source dir       phase      count
Corpus B         SECTION    45
Corpus B         fragment   93
Corpus B-new     fragment   45
B-new sections merged by the SECTION merge: 0
```

45 distinct file+section pairs, 47 token occurrences — `K2 §0.4` and `L5 §0.3` each have
fragments in **two** destinations.

25 B files, every one of them in a wave this run **has not reached**: AN1, AU1, CV-X,
I1–I5, K1–K4, L1–L8, O4–O7, RESP-X. Those files exist **only** in `Corpus B-new/`, so the
fragment phase had no `Corpus B/` alternative. Spot-checked against the introducing commit:

```
SRC:K1_Fever_Workup §0.1                        ff23b47 2026-08-31 K1 §0.1/0.5/0.6 -> 08_09
SRC:L3_Muscle_Symptoms_and_Widespread_Pain §0.4 de8f92a 2026-08-31 L3 -> 04_Neurology and 12_02
SRC:I2_Diabetes_and_Glucose_Disorders §0.2      5296d07 2026-08-31 I2 -> 06_Metabolic
SRC:CV-X_Chronic_Heart_Failure §0.4             8da08a0 2026-08-31 CV-X -> 01_Cardiovascular
SRC:AN1_Perioperative_Care §0.1                 a680277 2026-08-31 AN1 -> 03a_Anaesthetics_Primer
```

**Read the 45/93 split carefully — it is not "45 of 74 section merges".** It counts which
commit first wrote each token *string*. Where a section already had a fragment, the string
`SRC:C1_Acute_Abdomen §0.6` was first written by the fragment commit, so the later section
merge that superseded it is attributed to `fragment`. The 74/74 figure above is the direct
answer; this one is about token authorship.

## The "73 new files" arithmetic — measured

```
Corpus B:     39 files, 38 distinct prefixes    collision '00': 00_BUILD_QUEUE.md, 00_BUILD_QUEUE_v2.md
Corpus B-new: 112 files, 111 distinct prefixes  collision '00': same two
B prefixes with NO twin in B-new: []
B prefixes WITH a twin: 38
B-new prefixes with no Corpus B/ counterpart: 73
same prefix but DIFFERENT filename: none
```

**73 is right, and the reason is not the one the arithmetic suggests.** It is not
112 − 39. `Corpus B/` holds 39 files across **38** prefixes, because `00_BUILD_QUEUE.md`
and `00_BUILD_QUEUE_v2.md` share one; `Corpus B-new/` holds 112 across **111** for the
same reason. 111 − 38 = 73. The two errors cancel.

> [!warning] **There is NO twinless `Corpus B/` file. I claimed there was, in a message,
> before measuring it.**
> Seeing `39 files, 38 distinct prefixes` I inferred a missing twin. The gap is the `00`
> collision — and `Corpus B-new/` has the same two files and the same collision, which is
> why both directories lose exactly one and `111 − 38 = 73` comes out right.
> Measured by filename, not by prefix:
> ```
> By FILENAME — in Corpus B/ but not in Corpus B-new/: none
> Every Corpus B/ file has an identically-named twin: True
> Corpus B/ files with no twin: 0
> ```
> **All 39 have a twin, none renamed.** The table above was already correct
> (`B prefixes with NO twin in B-new: []`); the error was in reading a fact off an
> adjacent count instead of running the check — rule 11, one message after writing this
> audit about that exact habit.

**No section-merge prefix globs to more than one file** — checked for C1–C7, D1–D7,
GER1–2, A6–A8, F0-1…F0-5. The only collision in either directory is `00`, which is a build
queue, not a content file, and no merge references it. So `cands[0]` is unambiguous for
every file this run will touch.

## What to carry into the `Corpus B-new/` wave

- **38 of the 112 are re-exports of files already merged from `Corpus B/`.** Same prefix,
  and in every case the same filename — no renames to reconcile.
- **They are not known to be identical.** This audit establishes *which file was opened*,
  not whether the two copies agree. Nothing here licenses skipping a re-export on the
  grounds that its `Corpus B/` twin was merged.
- **The 45 pairs already merged from `Corpus B-new/` were merged as fragments, not as whole
  sections.** When their wave arrives they are section-merge candidates with a fragment
  already present, i.e. the ordinary supersede-and-inherit case — and two of them have
  fragments in **two** destinations.
