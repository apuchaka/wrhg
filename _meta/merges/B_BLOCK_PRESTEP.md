---
kind: prestep
block: B1–B6 (cardiology)
against: Corpus A/01_Cardiovascular.md
date: 2026-08-31
---

# Cardiology pre-step — named scores and eponyms, B1–B6

Run **before** any B-block merge, per the standing instruction: enumerate every named
score and eponym in `01_Cardiovascular.md` with **digit folding**, then check each
B-block claim against that list specifically.

## Method

```
python3 scripts/inventory.py "Corpus A/01_Cardiovascular.md"          → 215 candidates
python3 scripts/inventory.py --compare "Corpus A/01_Cardiovascular.md" "Corpus B/<Bn>.md"
```

`inventory.py` folds `₀–₉` and `⁰–⁹` to ASCII, so `CHA₂DS₂-VASc` and `CHA2DS2-VASc`
collapse to one entry. That is the check the instruction exists for: **`CHA₂DS₂-VASc`
is already in `01_Cardiovascular` with subscripts**, at L277, L290 and five more, plus
the `CHA2DS2-VA` variant at L297 and `CHA2DS2-VASc-based` at L657. A plain-ASCII search
would have missed all of them and B3 would have merged a duplicate.

**Rule 10 applied throughout:** every candidate absent from `01_Cardiovascular` was then
searched across **the whole vault** — Corpus A *and* Corpus C, and against every file
type, not only `.md`. An instrument missing from the cardiology file is routinely present
in `NEW_Cardiology_and_Vascular` or `NEW_Investigations_Cardiology`. Restricting the
search to the destination's own corpus would have produced four false gaps below.

**Rule 2 applied throughout:** every zero result was re-searched by **components rather
than name** before being called absent.

## Result

63 named candidates appear in B1–B6 and not in `01_Cardiovascular`. After whole-vault
checking, **13 are genuinely absent** and 50 were present, partial, or search artifacts.

### Genuinely absent from the whole vault

| Candidate | From | Component search that confirmed it |
|---|---|---|
| **HEART score / EDACS / any accelerated chest-pain pathway** | B1 | `accelerated diagnostic`, `chest pain pathway`, `rule-out pathway` — 0 |
| **MINOCA** | B1 | `non-obstructive coronar`, `nonobstructive coronar`, `unobstructed coronar` — 0 |
| **INOCA** | B1 | 2 raw hits, **both `Ech`INOCA`ndins`** — rule 9 |
| **V4R / right-sided chest leads** | B1 | `right.sided lead`, `V3R`, `RV infarct` — 0. See partial below |
| **CSANZ as a cited body** | B1, B3 | 0 in A and C; the corpus cites Heart Foundation, NHF, ESC, ACC/AHA, NICE |
| **HBPM (home BP monitoring)** | B2 | `home blood pressure` — 0. **ABPM is present** at L138/L148; the home arm is not |
| **SCAPE (sympathetic crashing acute pulmonary oedema)** | B2 | 5 raw hits, **all `e`SCAPE` rhythm / land`SCAPE`** — rule 9 |
| **HAS-BLED** | B3 | 0 in A and C — **and correctly so. NOT a gap; see the correction below.** |
| **Sgarbossa criteria** | B3 | `concordant ST` — 0; `paced rhythm.*ST` — 0. **New LBBB is present** (L33, L509 "a new LBBB is always assumed…"), so the corpus has the STEMI-equivalent rule and not the way to read ST in a *known* LBBB or paced rhythm |
| **Twiddler's syndrome** | B3 | `pacemaker.*pocket`, `manipulat.*generator` — 0. `lead displacement` **is** present as a complication at `NEW_Exam_Manoeuvres_and_Procedures.md:411` |
| **May-Thurner syndrome** | B6 | `iliac vein compress`, `left leg.*DVT` — 0. Absent by name and by mechanism |
| **Pemberton's sign** | B6 | `arm(s) above the head`, `raising both arms` — 0. **SVC obstruction itself is well covered** at `10_10a §Superior vena cava obstruction (SVCO)` — the sign is what is missing, not the entity |
| **Stemmer's sign / lymphoedema as an entity** | B6 | No heading for lymphoedema anywhere in A or C. It appears **only as a cellulitis risk factor** (`08_09:23`, `08_09:40`). The oedema differential has no lymphoedema arm |

### Partial — the concept is present, one half is missing

| Candidate | What is present | What is not |
|---|---|---|
| **Right ventricular infarction** | `NEW_Drugs_06_Cardiovascular.md:167` — *"Nitrates are contraindicated… in right ventricular / inferior myocardial infarction — a preload-dependent ventricle"*. The **management** danger is stated | The **diagnostic** half: right-sided leads, V4R, how you know the RV is involved. A reader is told what not to give and not how to recognise the patient |
| **Mitral valve prolapse** | Named at `01_Cardiovascular.md:804` as a **late systolic** murmur | `mid-systolic click` — 0 vault-wide. `myxomatous` — 0 |
| **Dynamic murmur manoeuvres** | `01_Cardiovascular.md:893` has *"ejection systolic (↑ with Valsalva, ↓ with squatting)"* — **inside the HOCM entry only** | `handgrip` — **0 vault-wide**. The manoeuvres exist as a HOCM fact, not as a general murmur-differentiating tool |

### Present — no gap, and the searches that nearly said otherwise

| Candidate | Where | Note |
|---|---|---|
| CTCA / calcium score | **`01_Cardiovascular.md:226`** — *"CT coronary angiography (first-line non-invasive anatomical test per current stepped-diagnostic pathway)"* → stress echo/perfusion → invasive angiography; plus `NEW_Investigations_Cardiology.md:84` (calcium score) | The **acronym** `CTCA` is 0 vault-wide, so the acronym comparison flagged it. The expansion is present **in the destination file itself**, with a fuller three-step pathway than B1 states. A name-only search would have merged a duplicate into the file that already had it — rule 10 |
| Tietze | costochondritis at `NEW_Cardiology_and_Vascular.md:24`, `NEW_Breast.md:36` | Eponym absent, **concept present** — not a gap |
| PRES | `NEW_Neurology.md:76` (full expansion), `NEW_Drugs_14:141` | Bare `PRES` returned **3197** hits vault-wide before word-boundary anchoring — *present*, *pressure*. Anchored: 2, both genuine |
| MAT | `NEW_Cardiology_and_Vascular.md:90` — its own section | Word-order trap: searching `MAT` alone is useless, `multifocal atrial` finds it |
| Leriche | `01_Cardiovascular.md:1346` §0.36.3, with the full triad at L1348 | |
| Rutherford | Name absent; `01_Cardiovascular.md:1329` "The P's of acute limb ischaemia" | Classification is above intern level; the recognition tool is present |
| ABI | Present as **ABPI** (7 hits) | Dual naming, §1.11 — not a gap |
| CRAB | `NEW_Investigations_Haematology_Part2.md:215`, `10_02:100` | Raw `CRAB` also matched a **COPD/asthma mnemonic** at `02_Respiratory.md:64` and the **crab louse** at `08_08:221` — rule 9, two artifacts on one four-letter string |
| CFS | `12_02 §0.7 Chronic fatigue syndrome (myalgic encephalomyelitis)` | |
| SOMANZ, HELLP, MEN2, NIV, PTH, SDH, GCA, PMR, SVC, ALP, B12, CCP, FVC, FNA, Cushing | all present, ≥3 anchored hits each | |

## CORRECTION — the HAS-BLED row was wrong. ORBIT **is** a bleeding score

**What this document originally said:** that `01_Cardiovascular` carries "three stroke/bleed
instruments, and **no bleeding-risk score paired with the stroke score**."

**That is false.** Found 2026-08-31 while merging B3, by reading every `ORBIT` hit instead of
counting them.

**ORBIT is the bleeding score.** `01_Cardiovascular.md:280` carries it in full — *"ORBIT
bleeding score — 5 components, maximum 7"* — with the component list, the risk bands, and at
`:292` a `[!danger]` box on the trap that **a high bleeding score does not decide against
anticoagulation**, because high bleeding and high stroke scores occur in the same patient.
`:296` states the pairing outright: *"use CHA₂DS₂-VASc for stroke risk and ORBIT for bleeding
risk."* The block even records its own arithmetic correction from 2026-08-29.

**HAS-BLED is therefore absent by design, not by omission.** Adding it would introduce a
competing instrument for a role already filled, which is worse than leaving it out.

**How the error happened, because the method is what needs fixing:** `inventory.py` returns
bare names. I read `ORBIT` as one more acronym in a list and never opened the block it names.
**A name in an inventory is not a description of what it does** — and since the pre-step's
entire method is a name comparison, this failure is available to it on every row.

**The guard: a name-level absence must be checked by reading the destination before it is
called a gap.** This is the same shape as the CTCA row above, which the pre-step did catch —
acronym absent, content in the destination all along. There the reading happened before the
claim landed. Here it did not, and the claim reached a PR body.

## Rule 9 artifacts caught in this pre-step

Six, on a list of 63. Recorded because the ratio is the signal (rule 3):

1. `INOCA` inside **ech**INOCA**ndins** — would have reported a real gap as filled
2. `SCAPE` inside e**scape** rhythm and land**scape** — same direction
3. `CRAB` inside a COPD mnemonic and *crab louse* — the myeloma sense was also genuinely there, so this one was harmless
4. `PRES` inside *present* and *pressure* — 3197 → 2
5. `facial plethora` matched **Cushing's syndrome** at `06:174`, not SVC obstruction — **the generic-component trap exactly**: the right words, the wrong condition, and it would have reported Pemberton's sign present
6. `ABI` vs `ABPI` — the reverse direction, a **false absent** from a naming variant

## A method defect found and corrected mid-run

Several probe commands were written as `grep -rniE -- "$pattern" --include="*.md" .`.
Because `--` ends option parsing, `--include="*.md"` was consumed as a **filename**, not a
filter, and `2>/dev/null` hid the resulting error. Those runs therefore searched **every
file type recursively**, not just `.md`.

**The error direction is safe** — a broader scope produces more hits, never fewer, so no
absence claim above was weakened by it. Every absence was nonetheless **re-run with correct
syntax** against `Corpus A` and `Corpus C` before being recorded, and the counts in the
table are from the clean run.

Recorded rather than quietly fixed, per rule 7: a suppressed stderr made a
scope error invisible, which is the same shape as the silently-voided marker.
