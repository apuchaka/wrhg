---
bfile: Corpus B/B5_Murmurs__Endocarditis_and_Vascular_Disease.md
sections: 6 (0.1–0.6), 24 headings
date: 2026-08-31
prestep: _meta/merges/B_BLOCK_PRESTEP.md
tooling: first file gap-checked with scripts/gapcheck.py
---

# B5 — destination table

**First file checked with `gapcheck.py`**, and the tool found a defect in itself on this
file — see *A false PRESENT the tool caught in itself*.

Gap check across `Corpus A` and `Corpus C`, destination included (rule 10), **no truncation
on any verdict** (rule 10 hard prohibition), zero results re-searched by component (rule 2).

## A false PRESENT the tool caught in itself — six gaps nearly lost

`gapcheck.py` defaults to **all three corpora**, correctly, because rule 10 requires the gap
search to run against every corpus. But in a merge **the source file is in one of them**, so
a search for content being merged *from* Corpus B matches **the B file itself**.

Six B5 claims returned 1–9 hits each and **every single hit was a self-match**:

| Claim | hits (all corpora) | hits in destination |
|---|---|---|
| peripartum cardiomyopathy | 3 | **0** |
| pseudoaneurysm | 9 | **0** |
| reperfusion injury | 1 | **0** |
| free wall rupture | 2 | **0** |
| shopping trolley sign | 1 | **0** |
| thrombin injection | 3 | **0** |

**All six are real gaps, and all six would have been silently dropped from the merge.** That
is a **false PRESENT** — the direction rule 9 singles out as the dangerous one, because a
false ABSENT is caught downstream when someone looks for the content, while a false PRESENT
drops the item and no report mentions it again.

The tool now groups hits by corpus, prints self-matches separately, and warns loudly when
**every** hit is a self-match. Found by running it (rule 11) on the first file it was used
for.

## Superseded

| B5 § | Claim | Where it already is |
|---|---|---|
| 0.1 | All diastolic murmurs are pathological; innocent systolic murmur criteria | `01_Cardiovascular.md` §0.21 |
| 0.1 | **RILE — right-sided on inspiration, left on expiration** | `01_Cardiovascular.md:810` — **verbatim the same mnemonic.** `RILE` returned **80 hits**, of which **79 were rule 9**: **ste**RILE, **feb**RILE, pue**RILE** |
| 0.1 | Timing, site, radiation, character, intensity, thrill | `01_Cardiovascular.md` §0.21 |
| 0.1 | The AS/MR/AR/MS/HOCM/VSD lesion table | `01_Cardiovascular.md` §0.21 — with collapsing pulse, slow-rising pulse, opening snap, malar flush |
| 0.1 | Feel the femoral pulses in every child with a murmur | `Examination.md:137`; `15_05_Paeds_-_Acyanotic_Congenital_Heart_Disease.md:60` |
| 0.2 | New murmur + fever = infective endocarditis; risk groups; IVDU right-sided | `01_Cardiovascular.md` §0.31 |
| 0.2 | **Three sets of blood cultures from separate sites before antibiotics** | `01_Cardiovascular.md:1110` — **more specific than B5**: *"3× 10 mL from different sites at 30-min intervals"* |
| 0.2 | Modified Duke criteria | `01_Cardiovascular.md:1110`, `:1114` |
| 0.2 | Osler nodes, Janeway lesions, Roth spots, splinters | `01_Cardiovascular.md` §0.31 |
| 0.2 | **New AV block suggests aortic root abscess and is a surgical indication** | `01_Cardiovascular.md:1110` — *"new conduction abnormality suggesting perivalvular/aortic root abscess extension, an indication for surgery"*; also `NEW_Cardiology_and_Vascular.md:69` |
| 0.2 | Aortic dissection involving the root → acute AR | `01_Cardiovascular.md` §0.36.5 |
| 0.5 | Claudication site indicates the level; **Leriche** | `NEW_Cardiology_and_Vascular.md:187`; `01_Cardiovascular.md:1389` §0.36.3 with the full triad |
| 0.5 | **Vascular versus neurogenic claudication** | `NEW_Cardiology_and_Vascular.md:189` — **fuller than B5**: relief by sitting or leaning forward, worse downhill, better uphill, **"leaning on a trolley"** (B5's shopping-trolley sign, unnamed), and less reproducible distance |
| 0.5 | ABI as first-line | `NEW_Cardiology_and_Vascular.md:193`; `01_Cardiovascular.md:1382` §0.36.2 — **with values B5 omits** |
| 0.5 | PAD is a marker of systemic atherosclerosis; risk-factor modification is the main treatment | `NEW_Cardiology_and_Vascular.md:195` — same framing |
| 0.5 | Supervised exercise therapy | `NEW_Cardiology_and_Vascular.md`; `01_Cardiovascular.md` §0.36.1 |
| 0.6 | Rest pain relieved by hanging the leg down | `01_Cardiovascular.md` §0.36.1 |
| 0.6 | **The six Ps of acute limb ischaemia** | `01_Cardiovascular.md:1329` — its own `[!danger]` box |
| 0.6 | The diabetic foot — neuropathy, ischaemia, infection | `06_Metabolic_Medicine_and_Endocrinology.md:492`; 17 hits across the vault |

## Additive

| B5 § | Claim | Destination |
|---|---|---|
| 0.1 | **Handgrip and the full dynamic-manoeuvre set** — squatting and handgrip increase afterload and preload, increasing MR/VSD/AR and *reducing* HOCM; Valsalva and standing reduce preload so most murmurs quieten, **with HOCM and MVP the two exceptions that get louder** | `01_Cardiovascular.md` §0.21, at the RILE line |
| 0.2 | **Mechanical complications of MI, days 3–7** — papillary muscle rupture (**murmur may be soft or absent**), ventricular septal rupture, free wall rupture | `01_Cardiovascular.md` §0.1 |
| 0.3 | **Peripartum cardiomyopathy as an entity** — missed because its symptoms *are* the symptoms of pregnancy; the features that should prompt echo rather than reassurance | `01_Cardiovascular.md` §0.27 |
| 0.4 | **Post-catheterisation vascular complications** — retroperitoneal haematoma **with no groin signs**, pseudoaneurysm, AV fistula, and why radial access is preferred | `01_Cardiovascular.md` §0.1, at the radial-access line |
| 0.6 | **Reperfusion injury after revascularising an ischaemic limb** | `01_Cardiovascular.md` §0.36 |

## Notes on two of these

**Peripartum cardiomyopathy** appears in the vault **only as the word "peripartum" in a
dilated-cardiomyopathy causes list** (`01_Cardiovascular.md:933`). `PENDING_GUIDELINE_CHECKS`
**P5-A30** already flags it as one of "the cardiovascular four" — so this is the second B-block
additive to fill a gap the project had already named for itself, after coronary vasospasm in B1.

**Handgrip is 0 vault-wide**, and this is the second time it has come up: the B1 pre-step
found the dynamic manoeuvres present **only inside the HOCM entry** (`01_Cardiovascular.md:893`)
and B1's table recorded it as partial without merging it. **B5 §0.1 is the right home** — it
carries the complete set, and the destination is the murmur section rather than one disease.

## Summary

| | n |
|---|---|
| Superseded | 19 |
| **Additive** | **5** |
| Conflicts | 0 |
| Rescued by the self-match fix | **6 of the checks**, 4 of which became additives |

## Figures

B5 states **no figure** — Levine grading descriptors, the ischaemic time window and the
Rutherford classes all carry `UNVERIFIED` markers. The ABI values and blood-culture volumes
already in `01_Cardiovascular` and `NEW_Cardiology_and_Vascular` are untouched. **No figure
enters the vault.**
