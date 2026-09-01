---
name: Fourteen-file gate — remediation and re-run
description: The six gate failures fixed, and the eight checks re-run with a known-answer result for each.
built: 2026-09-01
---

# Gate remediation — the six failures, and the re-run

## 1 · Ten UNVERIFIED markers restored — byte-identical, per marker

Recovered from the pre-supersede blob with `git`, never retyped, then matched against the
tree:

| Section | Marker | |
|---|---|---|
| C1 §0.9 | empirical antibiotic choice … **Therapeutic Guidelines (login)** | BYTE-IDENTICAL |
| C1 §0.10 | **tranexamic acid dose and time window** … National Blood Authority | BYTE-IDENTICAL |
| C1 §0.2 | contrast protocols … check local radiology guidance | BYTE-IDENTICAL |
| C2 §0.5 | whether a specific QT threshold should gate the second agent | BYTE-IDENTICAL |
| C3 §0.6 | desaturation threshold that defines orthodeoxia … | BYTE-IDENTICAL |
| C4 §0.2 | the grade labels (Ia/Ib/IIa/IIb/IIc/III) … RACGP | BYTE-IDENTICAL |
| C4 §0.2 | the recommended timing of restarting; RACGP … | BYTE-IDENTICAL |
| C4 §0.2 | its components and thresholds … Glasgow-Blatchford in Australian practice | BYTE-IDENTICAL |
| C4 §0.3 | the maximum inflation time and the balloon pressures … | BYTE-IDENTICAL |
| C5 §0.1 | caecal diameter … neostigmine or colonoscopic decompression | BYTE-IDENTICAL |

**10 of 10.** C1 §0.9 and §0.10 first, in their own commit (`ff06221`) — the §1.14
login-marker violation and the R1 dose marker whose replacement carried none.

**The Atlanta marker stays reworded and was NOT restored verbatim.** Its closing clause
read *"…and neither is the 48-hour CRP cut-off"*, and the section that replaced the
fragment **states** that figure. Verbatim restoration would put a marker on the page
contradicting the line above it.

**Three were placed by replacing B's shorter equivalent, not stacked beside it** — caecal
diameter, Forrest grades, restart timing. In each, B asks the same question and names no
source, which §1.7 forbids.

**A content loss found while restoring.** C4 §0.2's supersede removed the **AIMS65
sentence**, not only its marker — §1.10's own worked example of correct placement.
`AIMS65` had dropped to zero occurrences outside a note claiming its pointer was carried.
Restored verbatim.

## 2 · The SRC-in-conflict-block boundary bug

A conflict block names B's provenance inside its argument, and the boundary read that as
a new block. Now: a block header **starts** with the SRC token; one mid-sentence is prose.

```
SRC quoted inside a CF block, fragment continues past it
   KNOWN ANSWER 13   superseded 13   orphan left: False   CF-999 carried: True   PASS
a REAL foreign block header after the fragment
   KNOWN ANSWER 5    superseded 5    foreign survived: True                      PASS
```

The second case is what keeps the fix from being a revert. **My first run of this test
asserted 11 and failed on a correct result** — the expected value is now computed, not
guessed.

## 3 · Both relation losses

**Dubin-Johnson / Rotor** — the in-place record of a deliberate absence, restored verbatim.
**And KNOWN_ABSENCES §1 was broken by the same deletion**: its "Verified absent" row cited
`03_Gastrointestinal.md:1805` and its Status row said *"Already recorded in place. This
file cross-references that note rather than duplicating it."* Both false from the moment
of the supersede — so the absence had **no record anywhere**. Line reference repointed and
the episode written into the row.

**ILAE old-to-new pairing** — restored earlier in `09adca1`, confirmed present.

## 4 · The figure comparison now runs

`scripts/figcheck.py`. Each destination is reconstructed from git **at the parent of the
commit that merged the section** — comparing against the current tree would compare B
against itself.

```
SECTIONS 93 | B figures 28 | destination figures 20340
COMPARISONS MADE 3 | CANDIDATE MISMATCHES 0
```

**Three comparisons is the honest answer, not a vacuous check.** Of 1276 classifiable
numbers in those 93 B sections:

```
621  section number         ## 0.1 The Acute Abdomen — Framework
346  bare number, no unit   "> **1. The hernial orifices"
281  inside a wikilink      [[F0-3_Shock_Phenotypes_and_Sepsis_Syndromes]] 0.11
 28  NUMBER+UNIT            "pancreatic necrosis takes 48 to 72 hours"
```

Corpus B states 28 figures across 93 sections, by design (§1.6). Only 3 share both a unit
and an anchor with a destination figure.

**Two false positives were found and eliminated rather than waved through** — both matched
on the anchor `lasting`, pairing cluster-headache duration with status epilepticus. The
count went 2 → 0 for that reason, not because the corpus changed.

**Known answer:** a planted `amiodarone 300 mg` against a destination `150 mg`, with a
matching `24 hours` alongside → `COMPARISONS 2 | MISMATCHES 1`, hit
`('amiodarone','300','mg',['150'])`. The tool can fail.

## 5 · Counters regenerated

14 destination files were stale. The diff is **frontmatter only** — every changed line
matches `^[-+](conflicts_open|conflicts_r1|no_baseline):`, and every file's **body digit
multiset is unchanged**.

**My gate audit overcounted: 17, not 14.** Three — `09_01_Dermatology`, `15_01b_Paeds`,
`NEW_Drugs_01` — carry a **resolved** conflict, which the scan correctly does not count as
open. That was my conflation of "`[!fail]` block" with "open conflict".

The scan also offered to stamp 112 `Corpus B-new/` files; reverted, they are merge inputs.

## 6 · Twelve nested blocks queued, none moved

`_meta/MISPLACEMENT_QUEUE.md` — **8 mine, 4 base-A.** Re-parenting breaks `§n.n` pointers
and renumbers siblings, so it belongs with the other post-merge moves.

---

# The re-run

| Check | Result | Known answer |
|---|---|---|
| **2** additive-only | 1 historical, **0 outstanding** | fa7aba5's line, restored in `4eedf73` |
| **4** annotations | 41 markers in removed lines, **13 absent — all explained** | Atlanta (deliberate) + 6 replaced by fuller originals + CF-039 R2→R3 + 5 earlier-phase deliberate removals |
| **5** placement | **12 queued, 0 moved** | 8 mine / 4 base-A |
| **10** figures | **3 comparisons, 0 mismatches** | planted mismatch → 1 hit; tool can fail |
| **11** counters | **0 mismatches** across 201 files | 14 stale, fixed; 3 were my miscount |
| **15** trailing prose | **0** in the current tree | **1** at `fa7aba5` — audit still fails when it should |
| **16** relations | Dubin-Johnson 1 · ILAE pairing 1 · KNOWN_ABSENCES ref 1 | all three restored |
| **17** combined-source | **3** multi-section SRC lines, **0 in C1–D7** | GER2, A6 ×5, F0-4 — fragment phase, unmerged waves |

**Regression after all six fixes:** 93 of 93 sections still placed; across 49 destinations,
**0 digit removals and 0 new duplicate headings** against base-A.

## Check 4's thirteen, itemised

Every one accounted for; none is an outstanding loss.

| Commit | Marker | Why it is absent |
|---|---|---|
| `21ba198` | Atlanta / modified Marshall | **deliberately reworded** (would contradict its own line) |
| `1a7852c` ×2, `3050204`, `23bad52` ×3 | six short markers | **replaced by the fuller originals** in the restoration commits |
| `d53c696` | `CF-039 … **R2**` | re-weighted to **R3** as directed |
| `e251bcd` | under-7.5 kg band | **resolved** — ASCIA 2026 p6 covers that band |
| `1175373` | pulled-elbow reduction | removed with a **false NO-BASELINE** it depended on |
| `9c4a94f` | HLA-B*5801 testing | duplicate content removed, marker with it |
| `aee1148`, `30b2f18` | `→MED:GTN`, `→MED:sodium nitroprusside` | **marker misuse** — both lines state no dose |

## What this still does not establish

Clinical correctness of anything merged. And the figure comparison's reach is bounded by
what Corpus B states: **28 figures**. It cannot check a destination figure that B is silent
about, which is most of them.
