---
name: D6 destination table
description: Where every section of Corpus B/D6_Seizures_and_Movement_Disorders.md goes, including the sections that were discarded.
bfile: Corpus B/D6_Seizures_and_Movement_Disorders.md
built: 2026-08-31
---

# D6_Seizures_and_Movement_Disorders — destination table

Committed **before** any content was written. 5 182 words, 7 sections.
**1 placement · 6 discards.** **20 of 22 concepts tested were already present**, and both
trees agreed on every one.

## Rule 10 method

Pre-merge tree `245c1e5` **and** current tree · Corpus A **and** C · 201 files each ·
**nothing excluded** · digit folding · instrument-specific components.

## Results

| Concept | Verdict |
|---|---|
| status epilepticus (definition and the 5-minute rule), Austroads driving advice, seizure-vs-syncope discriminators, PNES, Todd's paresis, absence with 3 Hz spike-and-wave, juvenile myoclonic epilepsy, valproate teratogenicity, enzyme-inducing interactions with contraception, parkinsonism and TRAP, drug-induced parkinsonism, essential tremor, tardive dyskinesia, acute dystonia and oculogyric crisis, chorea, myoclonus, restless legs, Tourette, functional movement disorder, NMS vs serotonin syndrome | **present on both trees** |
| **SUDEP** | **absent on both trees** |
| **ILAE terminology — *focal aware*, *focal with impaired awareness*, *focal to bilateral tonic-clonic*** | **absent on both trees** |
| **drug-resistant epilepsy, defined as failure of two appropriately chosen and tolerated medications** | **absent on both trees** |
| epilepsy surgery referral | present — `NEW_Drugs_15_Neurological` |

### The terminology finding is a partial, not a gap

`04_Neurology` §Focal Seizures says focal seizures are *"further divided by awareness and by
motor vs non-motor features"* — **the concept is present, the current terms are not**, and
neither are the superseded ones (*simple partial*, *complex partial*). So this is not a
missing idea; it is an unnamed one. That matters for an exam sat under current ILAE
terminology, which is why it is merged as a naming addition and says so.

## Destination table

| D6 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Seizure classification, first seizure, driving | `Corpus A/04_Neurology.md` §Focal Seizures | **PARTIAL** — the ILAE terms only; the lobe-by-lobe detail, Jacksonian march and Todd's paresis are already there, and Austroads driving advice is present |
| 0.2 | Status epilepticus | — | **DISCARD** — `04_Neurology` §Status Epilepticus |
| 0.3 | Epilepsy management | `Corpus A/04_Neurology.md` §Focal Seizures | **PARTIAL** — SUDEP and the drug-resistant definition only; adherence, triggers, valproate and the interaction with contraception are all present |
| 0.4 | Tremor | — | **DISCARD** — essential tremor and the PD tremor contrast are present |
| 0.5 | Parkinsonism | — | **DISCARD** — §Parkinson's Disease, §PD drug classes, §Parkinson-Plus Syndromes |
| 0.6 | Chorea, dystonia, tics, myoclonus | — | **DISCARD** — all four present across `04_Neurology`, `14_03_Psych` and `NEW_Drugs_12` |
| 0.7 | Rigidity differential | — | **DISCARD** — NMS, serotonin syndrome and lead-pipe rigidity are in `04_Neurology` §Serotonin Syndrome and NMS |

No new file required. **No `CONFLICT` raised.**
