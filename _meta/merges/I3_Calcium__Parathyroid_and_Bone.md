---
name: I3 destination table
description: Where every section of Corpus B-new/I3_Calcium__Parathyroid_and_Bone.md goes, including the sections that were discarded.
bfile: Corpus B-new/I3_Calcium__Parathyroid_and_Bone.md
built: 2026-08-31
---

# I3_Calcium__Parathyroid_and_Bone — destination table

**26 concepts tested · 23 present · 2 absent · 1 partial.**
**Additive/discard ratio: 2 additive / 23 discard = 8% additive.**

Corpus C's electrolyte and investigation files carry most of this, and carry it better
than K3-style prose: `NEW_Drugs_07_Blood_and_Electrolytes` and
`NEW_Investigations_General_and_Preventive` own albumin correction and ionised calcium,
and `NEW_Drugs_07:153` states the magnesium point verbatim — *"hypomagnesaemia causes
hypocalcaemia that will not correct until magnesium is replaced."*

## Destination table

| I3 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Correct for albumin; ionised calcium | — | **DISCARD** — `NEW_Investigations_General_and_Preventive:59`, `NEW_Drugs_07:151` |
| 0.1 | Alkalosis causes symptomatic hypocalcaemia with a normal total calcium | — | **DISCARD** — `06_Metabolic:985`: *"Complexing of calcium from circulation: alkalosis (↑albumin binding)"* |
| 0.1 | PTH is the single most useful test; the two-branch differential | — | **DISCARD** — `06_Metabolic:0.10`'s Ix line is explicitly *"the key test distinguishing the three subtypes"* |
| 0.2 | **Familial hypocalciuric hypercalcaemia** | `Corpus A/06_Metabolic_Medicine_and_Endocrinology.md` §0.11 | **ADDITIVE** — `hypocalciuric` **and** `FHH` both 0 hits, base-A 0. The urinary-calcium discriminator, and the pointless operation it prevents |
| 0.2 | Stones, bones, groans and moans; treatment sequence, fluids first | — | **DISCARD** — `06_Metabolic:0.10` and Hypercalcaemia, which owns the CHIMPANZEES differential and the fluid and zoledronic acid figures per `10_10a`'s own pointer |
| 0.3 | Hypocalcaemia: causes, Chvostek and Trousseau, correct the magnesium first | — | **DISCARD** — 5 `Chvostek`, 6 `Trousseau`, and `NEW_Drugs_07:152–153` |
| 0.3 | Post-thyroidectomy hypocalcaemia — anticipate it | — | **PARTIAL, not merged** — `06_Metabolic:19` lists post-thyroidectomy as a cause of **hypothyroidism**, not hypocalcaemia, and §0.11 gives the biochemistry without the surgical anticipation. A narrow gap, left rather than merged because it sits inside a section a surgeon's source should write |
| 0.4 | Primary, secondary, tertiary hyperparathyroidism; who gets surgery; cinacalcet | — | **DISCARD** — `06_Metabolic:0.10.1–0.10.3`, 3 `cinacalcet` hits |
| 0.4 | **Localisation imaging is for surgical planning, not diagnosis** | `Corpus A/06_Metabolic` §0.11 | **ADDITIVE** — `sestamibi` 0 hits, base-A 0. A negative scan is not a reason to withhold surgery, and an incidental lesion is not a diagnosis |
| 0.5 | Osteomalacia and rickets; vitamin D deficiency risk groups in Australia | — | **DISCARD** — `11_08b_Ortho` and `06_Metabolic`; the risk-group list including veiling and residential aged care is at `I3`-equivalent depth already |
| 0.5 | Paget disease | — | **DISCARD** — `11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis` |
| 0.5 | CKD–mineral and bone disorder | — | **DISCARD** — `07_Renal:0.2.2` |
| 0.6 | Hypophosphataemia, hyperphosphataemia, refeeding | — | **DISCARD** — 5 `hypophosphataemia`, 10 `refeeding` hits |
| 0.6 | Hypo- and hypermagnesaemia | — | **DISCARD** — 26 `hypomagnesaemia` hits, `06_Metabolic:1006` |

## NO-BASELINE

**hypocalciuric** 0 · **sestamibi** 0, both against Corpus A and C at base-A.

## New files

**None.**
