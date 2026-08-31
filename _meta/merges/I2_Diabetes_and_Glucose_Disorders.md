---
name: I2 destination table
description: Where every section of Corpus B-new/I2_Diabetes_and_Glucose_Disorders.md goes, including the sections that were discarded.
bfile: Corpus B-new/I2_Diabetes_and_Glucose_Disorders.md
built: 2026-08-31
---

# I2_Diabetes_and_Glucose_Disorders — destination table

**34 concepts tested · 30 present · 4 absent.**
**Additive/discard ratio: 4 additive / 30 discard = 12% additive.**

Diabetes is the most heavily covered topic met this run. `06_Metabolic` alone carries
`0.15`–`0.19` (T1DM, T2DM, complications, diabetic foot, perioperative, **Austroads
driving standards**, DKA, HHS, hypoglycaemia, DI); `05_Ophthalmology` owns retinopathy,
`07_Renal` nephropathy, `04_Neurology` neuropathy, `15_16b` the paediatric and MODY
content, `16_01-05` diabetes in pregnancy, `19_General_Practice` the risk calculator, and
Corpus C owns the drug classes and the investigations.

## A seventh substring trap

`LADA` returned **6 hits: `maladaptive` ×5, `maladaptation` ×1. Zero real.**

## Destination table

| I2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Diagnostic tests and thresholds; HbA1c unreliable in haemoglobinopathy, anaemia, CKD, pregnancy | — | **DISCARD** — `NEW_Investigations_Endocrine:88–108` and `06_Metabolic:455` |
| 0.2 | Classification; the Australian context | — | **DISCARD** — `06_Metabolic:0.15.1–0.15.2` |
| 0.2 | **LADA — the adult misclassified as type 2** | `Corpus A/06_Metabolic_Medicine_and_Endocrinology.md` §0.15.2 | **ADDITIVE** — 6 hits, all `maladaptive`/`maladaptation`. MODY (the mirror-image error) is present at `15_16b:49`, which makes the asymmetry visible: the corpus warns about the young patient mislabelled type 1 and not the adult mislabelled type 2 |
| 0.3 | Individualised targets; lifestyle; remission | — | **PARTIAL, not merged** — 26 `remission` hits are too generic to resolve cheaply and the claim is soft. Recorded rather than merged |
| 0.3 | Pharmacotherapy; choose by comorbidity | — | **DISCARD** — `NEW_Drugs_10_Endocrine:0.2` owns the classes |
| 0.3 | Never omit basal insulin; sick day rules | — | **DISCARD** — `06_Metabolic:0.15.7` perioperative and `0.16` DKA |
| 0.3 | Diabetes distress | — | **PARTIAL, not merged** — 98 `distress` hits; soft claim, no distinctive pattern |
| 0.4 | Symptom sequence; causes in a person with diabetes | — | **DISCARD** — `06_Metabolic:0.18` |
| 0.4 | **Hypoglycaemia unawareness is caused by hypoglycaemia and is REVERSIBLE** | `Corpus A/06_Metabolic` §0.18 | **ADDITIVE** — 1 `unawareness` hit, and **reading the line in full** (not truncated) shows it is a criterion for a *higher perioperative BGL target* at `:562`, not the entity. The corpus has β-blockers blunting awareness and not the commoner cause |
| 0.4 | **Whipple's triad** | `Corpus A/06_Metabolic` §0.18 | **ADDITIVE** — all 3 `Whipple` hits are the **pancreatic resection** in `03_Gastrointestinal`. Base-A 0 |
| 0.4 | **C-peptide in the hypoglycaemia workup** | `Corpus A/06_Metabolic` §0.18 | **ADDITIVE** — 6 `C-peptide` hits, every one **classifying diabetes** (T1 vs T2, MODY, GAD/IA-2/ZnT8). Same test, different question, and the discriminating step — sample before the dextrose — is nowhere |
| 0.4 | Sulfonylurea hypoglycaemia is prolonged; octreotide | — | **DISCARD** — `NEW_Drugs_04:55` and `NEW_Drugs_10:101,187,191,306`, thoroughly |
| 0.5 | Retinopathy, nephropathy, neuropathy, cardiovascular | — | **DISCARD** — three dedicated files |
| 0.5 | Diabetic foot; Charcot neuroarthropathy, the hot foot that is not cellulitis | — | **DISCARD** — `06_Metabolic:507,515` (*"acute presentation is a warm, swollen…"* with total contact casting), plus `11_07b_Ortho` Charcot joint |
| 0.6 | Pregnancy, pre-existing and gestational | — | **DISCARD** — `16_01-05:0.12.2` |
| 0.7 | Inpatient errors; perioperative; driving | — | **DISCARD** — `06_Metabolic:0.15.7` and `0.15.8`, the latter Austroads-specific |

## NO-BASELINE — Corpus A and C at base-A only

**LADA** 0 (the 5 base-A hits are `maladaptive`) · **Whipple's triad** 0 ·
**hypoglycaemia unawareness** 1, so **not marked**.

## New files

**None.**
