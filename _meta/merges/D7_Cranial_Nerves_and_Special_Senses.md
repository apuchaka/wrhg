---
name: D7 destination table
description: Where every section of Corpus B/D7_Cranial_Nerves_and_Special_Senses.md goes, including the sections that were discarded.
bfile: Corpus B/D7_Cranial_Nerves_and_Special_Senses.md
built: 2026-08-31
---

# D7_Cranial_Nerves_and_Special_Senses — destination table

Committed **before** any content was written. 4 321 words, 6 sections.
**1 placement · 5 discards.** **20 of 22 concepts tested were already present**, both trees
agreeing on every one.

D7 was the second file flagged in advance as a likely collision, with `04_Neurology`
§Cranial Nerve Disorders. **The collision again ran in the corpus's favour**: forehead
sparing, Bell's palsy and steroid timing, Ramsay Hunt, eye protection, the third-nerve pupil
rule, fourth-nerve head tilt, sixth-nerve false localisation, INO and the MLF, Horner's
triad, fatigable ptosis, cavernous sinus, cerebellopontine angle, jugular foramen, RAPD and
the light-reflex pathway are all present already.

## Rule 10 method

Pre-merge tree `245c1e5` **and** current tree · Corpus A **and** C · 201 files each ·
**nothing excluded** · digit folding · instrument-specific components.

## Results

| Concept | Verdict |
|---|---|
| the twenty listed above | **present on both trees** |
| **bulbar versus pseudobulbar palsy, as a discriminating pair** | **absent on both trees** |
| glossopharyngeal neuralgia | absent from the vault — **and absent from D7**, so this merge cannot close it |

### The pieces exist; the discrimination does not

Checked separately, and this is why the placement is framed as it is:

- `jaw jerk` — **present** in `04_Neurology`
- `ask the patient to write`, separating dysphasia from dysarthria — **present** in
  `History-Taking`
- `emotional lability` — **present**, but in `15_20b_Paeds_-_Imprinting_Disorders`, a
  different context entirely
- `bulbar palsy` — **present** only as *"Progressive bulbar palsy: worst prognosis"*, an
  MND subtype at `04_Neurology` L456

So the components are scattered across three files and one of them is paediatric genetics.
**What is absent is the pair being set against each other** — flaccid fasciculating tongue
and absent gag versus small spastic tongue, brisk jaw jerk and emotional lability. The
block adds the discrimination and points at the owners for the parts that already exist.

## Destination table

| D7 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Cranial nerve localisation | — | **DISCARD** — §Brain Lesion Localisation, §Cranial Nerve Disorders, `Examination` |
| 0.2 | Facial palsy — UMN/LMN, Bell's, Ramsay Hunt, eye protection | — | **DISCARD** — §Bell's Palsy carries all of it |
| 0.3 | Diplopia and eye movement | — | **DISCARD** — third, fourth and sixth nerve palsies, INO and myasthenia are present across `04_Neurology` and `05_Ophthalmology` |
| 0.4 | **Bulbar versus pseudobulbar palsy** | `Corpus A/04_Neurology.md` §Cranial Nerve Disorders | **ADDITIVE** |
| 0.4 | Dysphagia, dysarthria vs dysphasia, swallow screening | — | **DISCARD** — `History-Taking`, `13_06b_ENT`, and the write-test is already in `History-Taking` |
| 0.5 | Smell and taste | — | **DISCARD** — anosmia is present |
| 0.6 | Other cranial nerve syndromes | — | **DISCARD** — cavernous sinus, CPA and jugular foramen all present |

No new file required. **No `CONFLICT` raised.**
