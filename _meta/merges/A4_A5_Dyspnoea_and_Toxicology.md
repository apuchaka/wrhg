---
bfiles:
  - Corpus B/A4_Dyspnoea__Cough_and_the_Solitary_Pulmonary_Nodule.md
  - Corpus B/A5_Toxicology_II_-_Poisoned_Patient__ADRs_and_Immunotherapy.md
date: 2026-08-31
prestep: _meta/merges/A_BLOCK_PRESTEP.md
tooling: scripts/gapcheck.py
---

# A4 + A5 — destination table

## Superseded

| Claim | Where it already is |
|---|---|
| Dyspnoea by speed of onset; the cardiac-vs-respiratory discriminator table | `NEW_Respiratory.md` §Dyspnoea; `History-Taking.md` |
| Orthopnoea — **ask how many pillows and whether the number has changed** | 8 `pillow` hits |
| MRC / mMRC dyspnoea scale | 3 hits, in the COPD assessment |
| Pertussis — paroxysms, post-tussive vomiting, whoop often absent in adults | 32 hits, incl. a full entry |
| Upper airway cough syndrome / post-nasal drip | 8 hits |
| **ACE-inhibitor cough**, and that it can begin late | `01_Cardiovascular.md:1228` — *"may occur up to a year after starting"* |
| Haemoptysis vs haematemesis; causes of haemoptysis | 38 hits |
| Bronchiectasis — chronic sputum, positional, recurrent infection | 29 hits, a full entry |
| **Risk assessment: resuscitate first, then identify**; activated charcoal limits | `14a-2_Psych_-_Overdose_and_Poisoning_Management.md` |
| **Poisons Information Centre is the expected step** | 12 hits |
| Take a paracetamol level regardless of the stated history | 7 hits |
| **TCA overdose — QRS widening, sodium bicarbonate is the treatment** | `NEW_Drugs_17_Psychotropic.md:57` — verbatim |
| Do not give flumazenil in mixed overdose | 4 hits |
| **CO poisoning — the oximeter reads falsely normal, needs co-oximetry** | **THREE** places: `11_09b_Ortho_-_Trauma.md:100`, `NEW_Drugs_04_Antidotes_and_Antivenoms.md:53`, `NEW_Investigations_Respiratory.md:79` |
| CO — household/occupational exposure history, several people affected | `History-Taking.md:802` |
| Penicillin allergy de-labelling | 16 hits |
| SJS / TEN / DRESS, and the culprit drug classes | 197 hits incl. `09_01_Dermatology_-_Dermatological_Emergencies.md` |
| Immune-related adverse events on checkpoint inhibitors | 9 hits incl. `NEW_Drugs_14_Immunomodulators_and_Antineoplastics.md` |

## Additive

| From | Claim | Destination |
|---|---|---|
| **A4 §0.4** | **The solitary pulmonary nodule** — benign versus malignant features, the **benign calcification patterns** including "popcorn", and that **a nodule unchanged on adequate prior films is almost certainly benign, so finding the old films can end the workup**. **Fleischner Society** named as the follow-up framework, criteria not reproduced | `02_Respiratory.md` |
| A4 §0.2 | **Post-viral cough** — a dry cough for weeks after a viral illness resolves, from transient airway hyperresponsiveness; benign, self-limiting, and needs explanation rather than investigation | `02_Respiratory.md` |
| **A5 §0.3** | **Type A versus Type B adverse drug reactions** — augmented and predictable versus bizarre and idiosyncratic | `14a-2_Psych_-_Overdose_and_Poisoning_Management.md` |
| A5 §0.3 | **TGA reporting — the Database of Adverse Event Notifications, and the Black Triangle** marking newly registered medicines under additional monitoring | same |
| A5 §0.2 | **Benzodiazepine withdrawal causes seizures and delirium and can kill** — unlike opioid withdrawal, which is deeply unpleasant and rarely lethal | same |
| A5 §0.2 | **CO poisoning — delayed neuropsychiatric sequelae** days to weeks after apparent recovery, and **fetal haemoglobin binds CO more avidly**, so the fetus is at greater risk than the maternal level suggests | same |
| A5 §0.1 | **A terminal R wave in aVR** as the TCA-overdose ECG sign, alongside QRS widening | `14a-2` §0.4 |

## Rule 9 — a second acronym collision, in the same shape as A1's `SIRS`

`Type A.*Type B` returned **3 hits, all real, none about drug reactions**:
- `01_Cardiovascular.md:553`, `:561` — **WPW Type A / Type B** (left- vs right-sided accessory pathway)
- `01_Cardiovascular.md:1386` — **Stanford Type A / Type B** aortic dissection

Like `SIRS` in A1, these survive anchoring and survive reading the line. **"Type A/Type B" is a
naming pattern the corpus uses for at least three unrelated classifications**, and only reading
the meaning separates them.

## Summary

| | n |
|---|---|
| Superseded | 18 |
| **Additive** | **7** |
| Conflicts | 0 |

The pre-step held again: **no named-instrument additive** (Fleischner is named but its criteria
deliberately omitted), with the yield in discriminators and Australian-specific process.

## Figures

Both files state **no figure** — nodule size thresholds, Fleischner intervals, CO
carboxyhaemoglobin levels and all doses carry `UNVERIFIED` markers or are omitted. **No figure
enters the vault.**
