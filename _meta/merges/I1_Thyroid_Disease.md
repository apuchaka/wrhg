---
name: I1 destination table
description: Where every section of Corpus B-new/I1_Thyroid_Disease.md goes, including the sections that were discarded.
bfile: Corpus B-new/I1_Thyroid_Disease.md
built: 2026-08-31
---

# I1_Thyroid_Disease — destination table

**32 concepts tested · 30 present · 2 absent.**
**Additive/discard ratio: 2 additive / 30 discard = 6% additive — the lowest of the run.**

> [!danger] **This file refutes the yield indicator I gave the user.**
> I predicted endocrine would be the richest week-2 seam on the grounds that Corpus A has
> **one** file with the `06_` prefix against five new `I` files. **The prediction was wrong,
> and the reason is a scope error in the indicator itself: it counted Corpus A filenames
> only.** Thyroid content is spread across `06_Metabolic_Medicine_and_Endocrinology`,
> `05_Ophthalmology` (thyroid eye disease, its own section), `15_16a_Paeds` (congenital
> hypothyroidism), `15_17a_Paeds` (paediatric hyperthyroidism), `16_08-09` (pregnancy),
> `13_06a_ENT` — **and above all `Corpus C/NEW_Investigations_Endocrine.md`, a dedicated
> file carrying the TFT pattern table, TIRADS, Bethesda FNA and the uptake-scan logic.**
> A file-count over one corpus is not a coverage measure.

## A sixth substring trap

`TRAb` returned **32 hits**: `trabecular` ×11, `strabismus`/`Strabismus` ×11,
`demonstrably` ×3. **4 real.**

Also worth recording as a different shape — **an eponym that is two diseases.** `Quervain`
returned 6 hits across **subacute thyroiditis** (`06_Metabolic:17`) and **de Quervain
tenosynovitis of the wrist** (`11_03_Ortho:26`, `NEW_Exam_Manoeuvres:135`). Both correct,
neither a false hit, and a reader who searched the eponym for one would land in the other.

## Destination table

| I1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | TSH as the sensitive first test; the TFT patterns | — | **DISCARD** — `NEW_Investigations_Endocrine:35` carries the full pattern table, secondary/pituitary row included |
| 0.1 | TSH unreliable in central hypothyroidism | — | **DISCARD** — `06_Metabolic:395`: *"TSH itself may be normal or even mildly [raised]"* in TSH deficiency |
| 0.1 | Do not test in an acutely unwell inpatient; sick euthyroid | — | **DISCARD** — `NEW_Investigations_Endocrine:41` and `06_Metabolic:0.1.2` |
| 0.1 | **Biotin interference produces spurious TFTs** | `Corpus A/06_Metabolic_Medicine_and_Endocrinology.md` | **ADDITIVE** — 1 `biotin` hit vault-wide, and it is **pyridoxine or biotin supplements for intractable neonatal seizures** at `15_22a:50` |
| 0.2 | Hypothyroidism, causes, Ix, levothyroxine, absorption interactions | — | **DISCARD** — `06_Metabolic:0.1`, 20 `levothyroxine` hits, `NEW_Drugs_10_Endocrine:197` |
| 0.2 | Subclinical hypothyroidism; do not over-treat | — | **DISCARD** — `06_Metabolic:0.1.1`; `NEW_Investigations_Endocrine:233` explicitly records the treatment threshold as a stated omission |
| 0.3 | Thyroiditis vs true hyperthyroidism, by uptake | — | **DISCARD** — `NEW_Investigations_Endocrine:79`: *"Low or absent uptake with thyrotoxicosis → the thyroid is leaking stored hormone, not making it"* |
| 0.3 | **Apathetic thyrotoxicosis in the elderly** | `Corpus A/06_Metabolic_Medicine_and_Endocrinology.md` | **ADDITIVE** — 0 hits. `06_Metabolic:88`'s S/Smx list is the classic sympathetic picture only; *"palpitations ± AF"* is not the apathetic presentation, it is the same disease seen the usual way |
| 0.3 | Graves, TRAb, ophthalmopathy as a separate process | — | **DISCARD** — `06_Metabolic:0.2.1`, and `05_Ophthalmology` owns Thyroid Eye Disease in a section of its own |
| 0.3 | Antithyroid drugs; agranulocytosis counselling | — | **DISCARD** — 20 `agranulocytosis` hits including the carbimazole warning |
| 0.4 | Thyroid storm; myxoedema coma; hydrocortisone with thyroid hormone | — | **DISCARD** — `06_Metabolic:0.2.3` and `0.1.3`, plus `NEW_Drugs_10:231` and `NEW_Investigations_Endocrine:42` |
| 0.5 | Nodules mostly benign; TFT first; sonographic features; TIRADS; FNA and Bethesda; the cancer FNA cannot diagnose | — | **DISCARD** — `NEW_Investigations_Endocrine:51–66`, which additionally records that **TIRADS-based omission of FNA misses a proportion of follicular cancers** |
| 0.5 | Goitre and compressive symptoms | — | **DISCARD** — `06_Metabolic:0.3`, `13_06a_ENT` |
| 0.6 | Pregnancy physiology, ranges, dose change; hyperthyroidism in pregnancy; postpartum thyroiditis | — | **DISCARD** — `16_08-09`, `06_Metabolic:0.2`, 58 `trimester` hits |
| 0.6 | Amiodarone-induced dysfunction, two types, opposite treatments | — | **DISCARD** — `06_Metabolic:45` and `NEW_Drugs_06:247` |

## NO-BASELINE — Corpus A and C at base-A only

**apathetic** 0 · **biotin** — has base-A hits (the neonatal seizure line), so **not marked**.

## New files

**None.**
