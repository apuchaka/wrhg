---
name: CV-X destination table
description: Where every section of Corpus B-new/CV-X_Chronic_Heart_Failure.md goes, including the sections that were discarded.
bfile: Corpus B-new/CV-X_Chronic_Heart_Failure.md
built: 2026-08-31
---

# CV-X_Chronic_Heart_Failure — destination table

**28 concepts tested · 26 present · 2 absent.**
**Additive/discard ratio: 2 additive / 26 discard = 7% additive.**

`01_Cardiovascular:0.28` plus `NEW_Drugs_06_Cardiovascular:0.10` and
`NEW_Investigations_Cardiology:0.2` cover this almost completely, including the four drug
classes, sacubitril/valsartan, dapagliflozin, ivabradine, vericiguat, diuretic resistance
with its causes, CRT and ICD, natriuretic peptides used to rule out, and cardiac
rehabilitation in four separate places. `01_Cardiovascular:0.28.4` even owns *explaining a
new heart failure diagnosis to a patient*.

## Destination table

| CV-X § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Classification by ejection fraction; the neurohormonal model; aetiology | — | **DISCARD** — `01_Cardiovascular:0.28`, 9 `HFrEF` and 4 `HFpEF` hits |
| 0.2 | Signs perform poorly; natriuretic peptides rule OUT; echo is essential; then investigate the cause | — | **DISCARD** — `NEW_Investigations_Cardiology:0.2` |
| 0.3 | Four drug classes started early and titrated in parallel; diuretics do not prolong life; the other agents; drugs to avoid in HFrEF | — | **DISCARD** — `NEW_Drugs_06:0.10` and `01_Cardiovascular:1249` |
| 0.3 | Cardiac rehabilitation is under-referred | — | **DISCARD** — present in four places, including `01_Cardiovascular:156`, `:1249`, `:1279` and `NEW_Drugs_06:350` |
| 0.4 | HFpEF: the typical patient; exclude the mimics; the treatment position has changed | — | **DISCARD** — 21 `amyloidosis` and 9 `constrictive` hits cover the mimics |
| 0.5 | Always look for the precipitant | — | **DISCARD** — 57 `precipitant` hits |
| 0.5 | **The wet–dry / warm–cold framework** | `Corpus A/01_Cardiovascular.md` §0.28 | **ADDITIVE** — `wet-dry` and `warm-cold` both 0, and the concept retry (`congestion`, `hypoperfusion`) returns nothing profiling the two axes together. `0.28.1`'s acute Mx assumes warm-and-wet, which is right most of the time and wrong in the group that does worst |
| 0.5 | Diuresis and diuretic resistance | — | **DISCARD** — `NEW_Drugs_06:322` lists adherence, salt and fluid, NSAIDs and renal decline |
| 0.5 | **The post-discharge period is the highest-risk time** | `Corpus A/01_Cardiovascular.md` §0.28 | **ADDITIVE** — 2 `post-discharge` hits, one the **GRACE score** for ACS and one a general-practice continuity note. Nothing about the heart failure vulnerable phase, and nothing about who owns the titration after discharge |
| 0.6 | Comorbidities; devices; recognising advanced HF | — | **DISCARD** — 4 `CRT`, 2 `resynchronisation` hits |
| 0.7 | Self-management; multidisciplinary programmes | — | **PARTIAL** — folded into the post-discharge block rather than merged separately |
| 0.7 | Prognosis is worse than many cancers; palliative care in heart failure | — | **DISCARD** — `10_11c_Oncology` and `GER2`-derived palliative content; `01_Cardiovascular:0.28.4` handles the conversation |

## NO-BASELINE

Both blocks. `wet-dry` and `warm-cold` return 0 in Corpus A and C at base-A.

## New files

**None.**
