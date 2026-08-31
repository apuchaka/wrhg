---
name: F0-2 to F0-5 destination table
description: Destination table for the four remaining F0 files. Three are fully superseded; F0-4 contributes two ANZCOR points.
bfiles: F0-2, F0-3, F0-4, F0-5
built: 2026-08-31
---

# F0-2 … F0-5 — destination table

Committed **before** any content was written. **1 placement across four files · 41 sections
discarded.** Combined with F0-1, **the entire F0 block yields one placement from five files
and roughly 27 000 words.**

## Why the F0 block is superseded

F0 is Corpus B's *emergency foundations* layer — resuscitation, shock, sepsis, acid-base,
DKA, asthma, head injury. **These are the most heavily built areas of any set of medical
notes**, and Corpus A and C own them several times over: `06_Metabolic_Medicine`,
`Investigation-Interpretation`, `15_16b_Paeds_DKA`, `15_01a_Paeds_Life_Support`,
`02_Respiratory`, `04_Neurology`, `11_09b_Trauma`, `08_09_Infectious_Disease`,
`NEW_Infectious_Diseases`, `NEW_Drugs_02/03/06/17`.

## Coverage tested in two rounds — and the second round mattered

**Round 1: 42 concepts across F0-2…F0-5. All 42 present.** On that evidence the block was
fully superseded.

**Round 2 sampled the unusual items instead of the headline ones, and found three
absences.** Had the merge stopped at round one it would have concluded "fully superseded"
and been wrong.

**Recorded as a method point: a first sampling round that returns 100% present is a reason
to sample differently, not a reason to stop.** The headline concepts of an emergency file
are exactly the ones any corpus already has.

| Round 2 absence | Verdict on reading |
|---|---|
| time-critical antibiotics in sepsis | **PRESENT** — `NEW_Infectious_Diseases` L53: *"Empirical broad-spectrum intravenous antibiotics must be given within 60 minutes of presentation"*, plus the Australian sepsis pathway at `08_09` L164. My pattern was too narrow |
| **newborn resuscitation commences in AIR, not oxygen** | **absent** — the only `room air` hit in the vault is ABG interpretation at `Investigation-Interpretation` L121, and `21` matched *cotrimoxazole 21 days* |
| **paediatric arrest is hypoxic/respiratory in origin** | **absent** — `15_01a` L49 lists Hypoxia among the 4Hs as a *reversible cause*, which is a different statement. The only other hit was codeine respiratory depression |

## Destination table

| File | Sections | Disposition |
|---|---|---|
| **F0-2** Acid-Base, DKA and Fluid States | 10 | **ALL DISCARDED** — 20 of 20 present. `06_Metabolic_Medicine` and `Investigation-Interpretation` own acid-base; `15_16b` owns paediatric DKA including cerebral oedema; `07_Renal` owns hyponatraemia and osmotic demyelination |
| **F0-3** Shock Phenotypes and Sepsis Syndromes | 11 | **ALL DISCARDED** — Beck's triad, pulsus paradoxus, massive PE thrombolysis, Addisonian crisis, qSOFA, meningococcal rash, Charcot's and Reynolds' all present |
| **F0-4** Resuscitation Algorithms and Emergency Procedures | 11 | **1 PLACEMENT** into `Corpus A/15_01a_Paeds_-_Paediatric_and_Newborn_Life_Support.md`; the other 10 discarded — ALS, 4Hs/4Ts, RSI, cricothyroidotomy, IO access, lung-protective ventilation, ketamine, nitrous oxide and the fascia iliaca block are all present |
| **F0-5** Acute Respiratory, Headache and Head Injury | 10 | **ALL DISCARDED** — asthma severity, NIV, CPAP in pulmonary oedema, CURB-65, FVC monitoring, CT head rules, Cushing's reflex, skull base signs, CT KUB, tamsulosin and quinsy aspiration all present |

**No new file. No `CONFLICT` raised across any of the four.**
