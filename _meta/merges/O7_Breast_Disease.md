---
name: O7 destination table
description: Where every section of Corpus B-new/O7_Breast_Disease.md goes, including the sections that were discarded.
bfile: Corpus B-new/O7_Breast_Disease.md
built: 2026-08-31
---

# O7_Breast_Disease — destination table

**24 concepts tested · 23 present · 1 absent.**
**Additive/discard ratio: 1 additive / 23 discard = 4% additive.** Breast disease is covered
by `10_12_Oncology_-_Breast`, `Corpus C/NEW_Breast`, `08_09` for mastitis and abscess, and
`Examination:416` for the inspection sequence.

## Destination table

| O7 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Triple assessment, and it must be **concordant** | — | **DISCARD** — 8 `triple assessment` and 4 `concordan` hits |
| 0.1 | Imaging chosen by age because density changes; family history; risk factors | — | **DISCARD** — `10_12_Oncology_-_Breast`, `NEW_Breast` |
| 0.2 | Every discrete new lump needs triple assessment; the common causes and how they feel | — | **DISCARD** — `NEW_Breast:23–24` gives the malignant and benign differentials with the discriminating features |
| 0.2 | **Male breast lump — gynaecomastia versus carcinoma**; look for a cause | — | **DISCARD** — 19 `gynaecomastia` hits; `NEW_Breast:48` lists the drug causes and calls them the commonest outside infancy |
| 0.3 | Cyclical vs non-cyclical pain; **breast pain alone is rarely cancer**; chest wall pain mislabelled; management is non-pharmacological | — | **DISCARD** — 3 `cyclical mastalgia` and 2 `chest wall pain` hits |
| 0.4 | Concerning features of discharge; the causes | — | **DISCARD** — `NEW_Breast`, which names intraductal papilloma with blood-stained discharge |
| 0.4 | **Paget disease of the nipple — biopsy persistent nipple eczema** | — | **DISCARD** — `10_12:26`, `NEW_Breast:23` and `Examination:416`, which points at it from the inspection sequence. The full phrase returns 0 because the corpus writes **"Paget's"**; the eponym search found it |
| 0.5 | Cancer types and treatment principles; complications an intern meets; metastatic spread | — | **DISCARD** — `10_12_Oncology_-_Breast` |
| 0.5 | **BreastScreen Australia and the screening/diagnostic distinction** | — | **DISCARD** — 4 `BreastScreen` hits |
| 0.6 | **Continue breastfeeding through mastitis** | — | **DISCARD** — `08_09:57` and `:98` |
| 0.6 | **Breast abscess — aspirate rather than incise** | — | **DISCARD** — `08_09:98` states it with the reasons (comparable efficacy, less scarring, less disruption to breastfeeding) and when surgery is still needed |
| 0.6 | **Inflammatory breast cancer masquerades as mastitis** | — | **DISCARD** — `NEW_Breast:23` calls it *"the classic trap"* and says a non-resolving mastitis needs re-evaluation rather than a second antibiotic course. Reinforced, not restated, in the new block |
| 0.6 | **Non-lactational and periductal mastitis** | `Corpus A/08_09_Infectious_Disease_-_Miscellaneous.md` | **ADDITIVE** — `periductal` 0 hits, base-A 0. The auto-retry derived `ductal` (21 hits) and found duct ectasia but not this. Different organisms, different antibiotic, the **smoking** association, and the mammary duct fistula |
| 0.7 | Lactation problems — most nipple pain is attachment | — | **DISCARD** — 16 `attachment` hits; `16_10-13_Labour_and_Delivery` and `08_09:89` |

## NO-BASELINE

The periductal mastitis block. `periductal` returns 0 in Corpus A and C at base-A.

## New files

**None.**
