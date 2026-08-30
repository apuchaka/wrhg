---
name: D4 destination table
description: Where every section of Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md goes, including the sections that were discarded.
bfile: Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md
built: 2026-08-31
---

# D4_Weakness__Neuropathy_and_Radiculopathy — destination table

Committed **before** any content was written. 4 348 words, 7 sections.
**2 placements · 6 discards.** 19 of 22 concepts tested were already present.

## Gap check run under the rule 10 method

This is the first table built after the destination-scope failure. The check was run:

- against the **pre-merge tree `245c1e5`** *and* the current tree, so nothing merged
  tonight can masquerade as pre-existing;
- across **Corpus A and Corpus C together**, 201 files at pre-merge;
- with **nothing excluded** — no `grep -v`, destinations included;
- with **digit folding** and **components searched separately from names**.

All three surviving gaps were confirmed absent on **both** trees.

## Three flags dismissed by reading, per rule 3

My component patterns were generic enough to make two real gaps look filled and one
irrelevant hit look real.

| Flag | What it actually was |
|---|---|
| `normal CK` — 9 files | **PMR** at `12_02` L76 (*"↑ESR (>40). Normal CK and EMG"*) — a different condition — plus unrelated lines. **Steroid myopathy's normal CK appears nowhere.** |
| `over-interpret` — 2 files | `Investigation-Interpretation` L339 (urine dipstick in the elderly) and L498 (CRP/ESR kinetics). **Nothing about spinal imaging.** |
| `tibialis posterior` — 1 file | `NEW_Exam_Manoeuvres` L115, about **Achilles rupture and the Thompson test** — plantarflexion, not inversion. **Not the discriminator.** |

**This is the inverse of the eponym trap: a component pattern too generic makes a real gap
look filled.** The eponym check says *search components, not just the name*; this says
*the components must be specific to the instrument*. Both failures are silent.

## Confirmed genuine gaps

| Concept | Verdict |
|---|---|
| **steroid myopathy has a NORMAL CK** | **absent, both trees** — `History-Taking` L372 lists *"steroids (myopathy)"* as a drug-history prompt and stops there |
| **do not over-image, and do not over-interpret the images, in radiculopathy** | **absent, both trees** |
| **foot drop — ankle inversion discriminates peroneal palsy from L5** | **absent, both trees**. `11_07a` carries the raw anatomy (tibial nerve does inversion) and `11_07a` L79 gives the peroneal territory, but **neither states the diagnostic use** |
| UMN vs LMN, glove-and-stocking, diabetic foot ulceration, neuropathic pain agents, cervical and lumbosacral roots, cauda equina red flags, carpal tunnel, ulnar and radial entrapment, mononeuritis multiplex, myasthenia and fatigability, drugs precipitating myasthenic crisis, Lambert-Eaton, botulism, proximal myopathy and CK, dissociated sensory loss, Brown-Séquard, positive vs negative sensory phenomena, subacute combined degeneration | **present** |

## Destination table

| D4 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Localising the lesion — the eight levels, UMN vs LMN | — | **DISCARD** — `04_Neurology` §Weakness — Differential Diagnosis and §Brain Lesion Localisation |
| 0.2 | Peripheral neuropathy, diabetic neuropathy, neuropathic pain | — | **DISCARD** — §Diabetic Neuropathy, and the agents are in `NEW_Drugs_15` and `NEW_Drugs_03` |
| 0.3 | Radiculopathy, roots, cauda equina red flags | — | **DISCARD** — `11_06_Ortho_-_Spinal_Orthopaedics`, `11_07a` dermatomes/myotomes, and cauda equina appears in 16 files |
| 0.3 | **Do not over-image or over-interpret** | `Corpus A/11_06_Ortho_-_Spinal_Orthopaedics.md` | **ADDITIVE** |
| 0.4 | Mononeuropathies and entrapment | — | **DISCARD** — carpal tunnel is in 12 files with Phalen and Tinel; the other entrapments are in `11_07a` |
| 0.4 | **Foot drop — the inversion discriminator** | `Corpus A/04_Neurology.md` §Weakness — Differential Diagnosis | **ADDITIVE** |
| 0.5 | Neuromuscular junction — myasthenia, crisis, Lambert-Eaton, botulism | — | **DISCARD** — §Myasthenia Gravis and the infectious-disease files |
| 0.6 | Myopathy | — | **DISCARD** — proximal weakness and CK are present across 31 files |
| 0.6 | **Steroid myopathy has a normal CK** | `Corpus A/04_Neurology.md` §Weakness — Differential Diagnosis | **ADDITIVE** |
| 0.7 | Sensory disturbance, dissociated loss, Brown-Séquard | — | **DISCARD** — §Weakness — DDx and the cord syndromes are present |

No new file required. **No `CONFLICT` raised.**
