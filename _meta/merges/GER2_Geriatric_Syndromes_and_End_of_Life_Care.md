---
name: GER2 destination table
description: Where every section of Corpus B/GER2_Geriatric_Syndromes_and_End_of_Life_Care.md goes, including the sections that were discarded.
bfile: Corpus B/GER2_Geriatric_Syndromes_and_End_of_Life_Care.md
built: 2026-08-31
---

# GER2_Geriatric_Syndromes_and_End_of_Life_Care — destination table

Committed **before** any content was written. 4 876 words, 6 sections.
**3 placements · 3 discards.** **The largest genuine gap of any file since C1** — 15 of 21
concepts present, but the six absent ones cluster in one area the corpus barely covers.

## The finding: Corpus A has palliative PRESCRIBING and no dying-phase framework

`Corpus A/10_11c_Oncology_-_Palliative_Care_Prescribing.md` has exactly three sections —
*General principles*, *Conversion between opioids*, *Symptom management in palliative care*.
It is a **prescribing** file, and its only use of "anticipatory" is
*"Cortical (e.g. anticipatory): lorazepam, cyclizine"* — anticipatory **nausea**, not
anticipatory prescribing.

A whole-vault search for `last days of life`, `terminal phase`, `recognising dying` and
`anticipatory prescribing` returns **nothing, in either corpus, on either tree**.

So the corpus can tell an intern which opioid to convert to, and cannot tell them **that
the patient is dying**. That is the gap.

## Instrument inventory, digit-folded

`DIAPPERS · IDDSI · PEG · ABI · ACD · NFR · CPAP · NIV · CPR` — checked by name **and**
components. `Refeeding syndrome` also detected and confirmed present.

## Results

| Concept | Verdict |
|---|---|
| **recognising dying / the terminal phase** | **absent, both trees** |
| **anticipatory prescribing** | **absent, both trees** |
| **voluntary assisted dying** | **absent, both trees** |
| **DIAPPERS** (transient causes of incontinence) | **absent, both trees** |
| **Waterlow / Braden** pressure-injury risk tools | **absent, both trees** |
| **delirium prevention bundles** | **absent, both trees** |
| incontinence types, post-void residual, pressure injury staging and repositioning, malnutrition screening, refeeding, IDDSI, PEG in dementia, deconditioning, syringe driver, death rattle, Advance Care Directive, NFR, bereavement, ABI | **present, both trees** |

## Destination table

| GER2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Continence | `Corpus A/07_Renal_Medicine_and_Urology.md` | **PARTIAL** — DIAPPERS only; types, post-void residual and bladder scanning are present |
| 0.2 | Pressure injury | `Corpus A/18_Geriatrics_and_Older_Persons_Health.md` | **PARTIAL** — the risk tools only; staging and repositioning are present |
| 0.3 | Malnutrition and nutrition | — | **DISCARD** — screening, refeeding, IDDSI and PEG-in-dementia all present |
| 0.4 | Immobility and deconditioning | `Corpus A/18_Geriatrics_and_Older_Persons_Health.md` | **PARTIAL** — delirium prevention bundle only |
| 0.5 | **End-of-life care and recognising dying** | `Corpus A/10_11c_Oncology_-_Palliative_Care_Prescribing.md` | **ADDITIVE** — the largest placement of the run |
| 0.6 | Advance care planning | — | **DISCARD** — Advance Care Directive, substitute decision-maker and NFR are in `Communication` and `Clinical-Process-EBM-Consent-Capacity`, with the SA framework already verified there |

## Figures and law — what is deliberately not written

- **GER2's own frontmatter omits every anticipatory prescribing dose**, directing them to
  eTG Palliative Care. eTG is login-gated (§1.8), so they are **permanently noted** and no
  dose crosses.
- **Voluntary assisted dying is state-based law.** Eligibility criteria, timeframes and the
  practitioner requirements are **not stated** — an `UNVERIFIED` marker names SA Health and
  the state legislation instead. Writing legal criteria from model knowledge is exactly
  what §1.14 forbids, and the consequence of being wrong is not academic.

No new file required. **No `CONFLICT` raised.**
