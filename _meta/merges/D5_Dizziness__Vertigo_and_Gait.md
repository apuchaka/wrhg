---
name: D5 destination table
description: Where every section of Corpus B/D5_Dizziness__Vertigo_and_Gait.md goes, including the sections that were discarded.
bfile: Corpus B/D5_Dizziness__Vertigo_and_Gait.md
built: 2026-08-31
---

# D5_Dizziness__Vertigo_and_Gait — destination table

Committed **before** any content was written. 3 668 words, 6 sections.
**1 placement · 5 discards.** **18 of 20 concepts tested were already present**, and both
trees agreed on every one — so nothing merged earlier tonight contaminated the result.

D5 was flagged in advance as a likely collision point with `04_Neurology` §Vertigo. **It
is**, and the collision runs almost entirely in the corpus's favour: A's §Vertigo already
carries peripheral-versus-central, fixation suppression, BPPV with Dix-Hallpike and Epley,
vestibular neuritis, HINTS by name, and the point that vestibular sedatives impair central
compensation. `13_03_ENT_-_Deafness_and_Vertigo_Conditions` independently covers BPPV,
Ménière's, vestibular neuronitis and labyrinthitis, and `NEW_Neurology` covers vestibular
migraine and the HINTS-plus hearing-loss point.

## Rule 10 method

Pre-merge tree `245c1e5` **and** current tree · Corpus A **and** C · 201 files each ·
**nothing excluded** · digit folding · components searched separately from names and made
**instrument-specific** per the rule 9 addition.

## Results

| Concept | Verdict |
|---|---|
| dizzy disambiguation, TiTrATE timing-and-triggers, acute vestibular syndrome, HINTS and its three components, HINTS-plus, normal-head-impulse-means-central, Ménière's, vestibular migraine, orthostatic hypotension, Romberg, ataxic/parkinsonian/apraxic/waddling/high-stepping gaits, gaze-evoked and direction-changing nystagmus, fixation suppression, Dix-Hallpike, Epley, vestibular sedatives and compensation, DANISH | **present on both trees** |
| **persistent postural-perceptual dizziness (PPPD)** | **absent on both trees** |
| mal de débarquement | absent from the vault — **and absent from D5**, so this merge cannot close it |

## Destination table

| D5 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Disambiguating "dizzy"; separating presyncope | — | **DISCARD** — `History-Taking` and `01_Cardiovascular` carry the timing-and-triggers approach and the presyncope split |
| 0.2 | Acute vestibular syndrome and HINTS | — | **DISCARD** — `04_Neurology` §Vertigo, `Examination` (the manoeuvres), `NEW_Neurology` (HINTS-plus) |
| 0.3 | Episodic vertigo — BPPV, Ménière's, vestibular migraine | — | **DISCARD** — `13_03_ENT` and `NEW_Neurology` |
| 0.4 | **PPPD** | `Corpus A/04_Neurology.md` §Vertigo | **ADDITIVE** |
| 0.4 | Bilateral vestibulopathy, chronic dizziness generally | — | **DISCARD** — covered across `04_Neurology` and `13_03_ENT` |
| 0.5 | Gait disorders | — | **DISCARD** — `Examination` §gait, `04_Neurology` §Parkinson's, `11_04_Ortho_-_Hip` (waddling) |
| 0.6 | Nystagmus | — | **DISCARD** — `04_Neurology` §Vertigo and `Examination` |

**Placed in `04_Neurology` rather than `13_03_ENT`** because `13_03` is organised by ENT
*disease* — otosclerosis, schwannoma, Ménière's, neuronitis, labyrinthitis — and PPPD is
none of those. It follows *any* acute vestibular event, is a positive functional diagnosis,
and is managed with vestibular rehabilitation and SSRIs, which sits with the compensation
material already in `04_Neurology` §Vertigo.

No new file required. **No `CONFLICT` raised.**
