---
name: AU1 destination table
description: Where every section of Corpus B-new/AU1_Australian_Health_Context_and_ATSI_Health.md goes, including the sections that were discarded.
bfile: Corpus B-new/AU1_Australian_Health_Context_and_ATSI_Health.md
built: 2026-08-31
---

# AU1_Australian_Health_Context_and_ATSI_Health — destination table

**26 concepts tested · 21 present · 5 absent.**
**Additive/discard ratio: 5 additive / 21 discard = 19% additive — the highest of week 3.**

## Scope decision, made deliberately and stated here

**One block, narrow by design.** AU1 is 250 lines spanning the health system, ATSI health,
rural and remote practice, CALD patients and health literacy. **The merged block covers only
the operational layer — what an intern does** — because the corpus already carries cultural
safety as a disease-specific barrier (`12_01_Rheum:105`), the equity-of-screening argument
(`Clinical-Process-EBM-Consent-Capacity:354`), ARF and RHD across the cardiology and
infectious disease files, Medicare and the PBS, and interpreter use.

**The history, the policy and the epidemiology were not merged.** They are not intern-level
action, and a model-knowledge account of them is the kind of content that should come from
an Australian source rather than from this corpus. **This is a scope judgement and the user
should review it** — it is flagged in the morning report as well as here.

## Destination table

| AU1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Two-tier funding; Medicare and the items funding longitudinal care; **cost is a clinical variable** | — | **DISCARD** — 18 `Medicare` hits; `19_General_Practice:0.4` |
| 0.1 | The other systems you interact with | — | **DISCARD** — `19_General_Practice`, `18_Geriatrics` (ACAT, My Aged Care) |
| 0.2 | The framing determines the clinical encounter | — | **DISCARD in part** — the principle is at `12_01_Rheum:105`; the operational consequences are merged below |
| 0.2 | **Social and emotional wellbeing as a model** | `Corpus A/19_General_Practice_and_Preventive_Medicine.md` | **ADDITIVE** — 0 hits, base-A 0 |
| 0.2 | Social determinants generating clinical burden | — | **DISCARD** — `12_01_Rheum:105` states the barriers are structural and relational, not individual |
| 0.2 | **Closing the Gap and the community-controlled sector** | `Corpus A/19_General_Practice…` | **ADDITIVE (partial)** — `Closing the Gap` returns 4 hits, but **`community-controlled` returns 0** and base-A 0. ACCHOs and what their governance means were absent |
| 0.2 | **Cultural safety is defined by the PATIENT** | — | **DISCARD** — 2 hits carry the concept; the block does not restate it |
| 0.2 | **Engage Aboriginal Liaison Officers and Health Workers EARLY** | `Corpus A/19_General_Practice…` | **ADDITIVE** — `Aboriginal Liaison` 0 hits, base-A 0 |
| 0.2 | **"Discharge against medical advice" is a signal about the service** | `Corpus A/19_General_Practice…` | **ADDITIVE** — `against medical advice` 0 hits, base-A 0. Merged with the language-in-the-notes point, which is the part that persists |
| 0.2 | Distance and being far from home | — | **DISCARD in part** — folded into the discharge block as one of the concrete reasons |
| 0.3 | **Acute rheumatic fever and rheumatic heart disease** | — | **DISCARD** — 12 and 11 hits; `01_Cardiovascular`, `08_01-03`, `13_05a_ENT` |
| 0.3 | Chronic and end-stage kidney disease; the other higher-burden conditions | — | **DISCARD** — `07_Renal`, `02_Respiratory:281–285` (bronchiectasis with the 20-year mortality gap), `06_Metabolic` |
| 0.3 | Social and emotional wellbeing and suicide | — | **DISCARD in part** — cross-referenced from the merged block to `14_01_Psych` rather than duplicated |
| 0.4 | Rural and remote practice | — | **DISCARD** — `19_General_Practice`, `NEW_Investigations_Respiratory` retrieval content |
| 0.4 | **CALD patients — use professional interpreters** | — | **DISCARD** — 1 `interpreter` hit plus `GER5_Communication` (Week 5, unmerged) will own this properly |
| 0.5 | **Health literacy — teach-back** | — | **DISCARD** — 1 `teach-back` hit |
| 0.5 | **Ask the identification question — every patient, every time** | `Corpus A/19_General_Practice…` | **ADDITIVE** — `identification question` 0 hits, base-A 0. Merged with the reason it matters clinically: identification is what unlocks the health assessment, the co-payment programme and ACCHO care |
| 0.5 | **The CTG PBS Co-payment Programme** | `Corpus A/19_General_Practice…` | **ADDITIVE (within the ACCHO block)** — 2 `PBS co-payment` hits exist but not the registration-and-annotation requirement, which is what makes it work or fail at the point of prescribing |
| 0.6 | A useful social history; discharge planning that accounts for reality; reflect on your own practice | — | **DISCARD in part** — the actionable elements are inside the discharge and Liaison Officer blocks |

## NO-BASELINE

All five: `community-controlled`, `Aboriginal Liaison`, `against medical advice`,
`social and emotional wellbeing` and `identification question` return 0 in Corpus A and C at
base-A.

## Figure discipline

**No figure of any kind.** No percentage, no gap statistic, no eligibility threshold. The
co-payment eligibility and registration process carry an `UNVERIFIED` marker naming Services
Australia and the PBS — both open.

## New files

**None.** The block is a section inside an existing file, so the new-file gate did not fire.
