---
name: GER1 destination table
description: Where every section of Corpus B/GER1_Comprehensive_Geriatric_Assessment.md goes, including the sections that were discarded.
bfile: Corpus B/GER1_Comprehensive_Geriatric_Assessment.md
built: 2026-08-31
---

# GER1_Comprehensive_Geriatric_Assessment — destination table

Committed **before** any content was written. 5 067 words, 6 sections.
**1 placement · 5 discards.** **21 of 22 concepts tested were already present.**

`Corpus A/18_Geriatrics_and_Older_Persons_Health.md` is a purpose-built geriatrics file
and absorbs almost all of GER1: CGA, frailty and the Clinical Frailty Scale, ADL/IADL,
ACAT and My Aged Care, home care packages, Beers, STOPP/START, Home Medicines Review,
anticholinergic burden, deprescribing, multifactorial falls assessment with Timed Up and
Go, postural blood pressure, vitamin D, FRAX, DXA and T-scores, bisphosphonates and
denosumab, secondary osteoporosis, vertebral fracture, osteonecrosis of the jaw, atypical
femoral fracture and the bisphosphonate drug holiday.

## Instrument inventory run first

Every named instrument in GER1 was enumerated with digit folding before searching, per the
required check: **ACAT · ADL · IADL · Beers criteria · CGA · DXA · FRAX · HMR · RMMR ·
STOPP · START · NDIS · DVA**. Each was then checked by name **and** by components.
All but NDIS and DVA are present.

*(The inventory also returned all-caps prose — `FIRST`, `WHY`, `MULTIPLE`, `VERTEBRAL`,
`MEDICATIONS` — dismissed on reading, per rule 3. The tool informs; it does not decide.)*

## One search artifact, and it is the word-order trap again

`vitamin D and falls` was searched as `vitamin D.{0,50}fall` and returned **ABSENT**.
`18_Geriatrics` L78 has it: *"**Vitamin D** — supplement where deficient. Note the evidence
is dose- and setting-dependent…"* — the corpus puts the caveat before the falls context, so
a pattern requiring the two within 50 characters in that order missed it. **Rule 10's
word-order corollary, on the first file after the rule was written.**

## Confirmed genuine gap

| Concept | Verdict |
|---|---|
| **NDIS and DVA as alternative funding pathways** | **absent on both trees** |
| everything else listed above | **present on both trees** |

## Destination table

| GER1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Comprehensive geriatric assessment | — | **DISCARD** — `18_Geriatrics` |
| 0.2 | Frailty, Clinical Frailty Scale, gait speed, grip strength | — | **DISCARD** — `18_Geriatrics` |
| 0.3 | Functional assessment and the aged care system | `Corpus A/18_Geriatrics_and_Older_Persons_Health.md` | **PARTIAL** — NDIS and DVA only; ACAT, My Aged Care and home care packages are present |
| 0.4 | Polypharmacy and deprescribing | — | **DISCARD** — Beers, STOPP/START, HMR, anticholinergic burden and deprescribing are all present |
| 0.5 | Falls | — | **DISCARD** — multifactorial assessment, Timed Up and Go, postural BP and vitamin D all present |
| 0.6 | Osteoporosis and fracture prevention | — | **DISCARD** — `18_Geriatrics` and `11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis` |

No new file required. **No `CONFLICT` raised.**
