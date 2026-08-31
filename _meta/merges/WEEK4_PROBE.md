---
name: Week 4 probe
description: Verdict counts only for one M file and one J file. NO MERGING was done and no content was written from either.
built: 2026-08-31
---

# Week 4 probe — M4 and J3, verdict counts only

**No merging.** No destination sections were written, no `SRC:` block was created, and
neither file was consumed. This exists to price Week 4 before committing 25 files to it.

## Which two, and why those two

Chosen by a **neutral rule, not by judgement**: the numeric middle of each series.
M1–M7 → **M4**. J1–J5 → **J3**. Picking "a representative file" by eye would have let me
choose the answer.

## Results

| File | Tested | Absent | Present | Additive rate |
|---|---:|---:|---:|---:|
| **M4** Growth and Development | 32 | 5 | 27 | **16%** |
| **J3** Bleeding and Thrombosis | 34 | 3 | 31 | **9%** |

**Both are in or below the Week 2 band (15% overall). Neither is much higher.**

### M4 — what is absent
**M-CHAT** (0 hits) · **bone age** (0, with `--allow-phrase`) · **creatine kinase in a boy
with motor delay** (no hit pairs the test with the presentation) · **regression as a rule**
(the word appears in brain tumours and growth red flags, not as the developmental
principle) · the **height-tells-you-whether-obesity-is-endocrine** discriminator.

### M4 — what supersedes it
`15_19a_Paeds_-_Developmental_Milestones_and_Delay` carries a **full milestone table with
per-age red flags**; `Investigation-Interpretation` §1.19 owns growth charts, centiles and
**mid-parental height**; `History-Taking` §1.26 owns faltering growth;
`15_19b` owns cerebral palsy and the muscular dystrophies **including Gower's sign**;
`15_18a` owns precocious and delayed puberty; Turner and karyotype are present 18 and 17
times.

### J3 — what is absent
**PFA / platelet function analyser** (0) · **May-Hegglin** (0) · one interpretive framing
point. That is all.

### J3 — what supersedes it
Twelve `10_*` Corpus A files plus two Corpus C haematology investigation files. von
Willebrand 29 hits, mixing study 6, Wells 16, D-dimer 35, thrombophilia 21,
antiphospholipid 30, DOACs 33, **idarucizumab 6 and andexanet 9**, 4Ts 10, Budd-Chiari 3,
splanchnic 2, desmopressin 14, tranexamic 19, `rebalanced` haemostasis in liver disease 1.
**Bernard-Soulier and Glanzmann are both present.** Haematology is the densest area met
in this project so far.

## Projection for Week 4 — extrapolated from 2 of 25, and labelled as such

| Sub-block | Files | Assumed rate | Additive |
|---|---:|---:|---:|
| M paediatrics | 7 | 16% (measured) | ~35 |
| J haematology | 5 | 9% (measured) | ~15 |
| N psychiatry | 8 | ~15% (assumed) | ~35 |
| H renal | 4 | ~12% (assumed) | ~15 |
| PH1 | 1 | unknown | ~4 |
| **Total** | **25** | | **~100** |

**~100 additive blocks for 25 files — which matches the user's own estimate**, so the
decision to take Week 4 after Week 3 stands on measured ground rather than on the file
count that was wrong about endocrine.

**The caveat that matters:** the two sub-blocks differ by nearly a factor of two, and the
low one is haematology. If Week 4 is ever cut short, **run M before J.**

## A ninth and tenth substring trap, found while probing

| Pattern | Hits | Matched |
|---|---:|---|
| `PERC` | 253 | `hypercalcaemia` ×73, `percentage` ×23, `hypercholesterolaemia` ×17, `percussion` ×16 |
| `HIT` | 206 | `white`, `within`, and every other word containing the letters |

`PERC` **was** on the known-collisions list this run started from — and it still returned
253 hits, because knowing a pattern is bad does not stop the count being produced. Rule 9's
new clause covers it: read what the matches are before reading any of them as a verdict.
