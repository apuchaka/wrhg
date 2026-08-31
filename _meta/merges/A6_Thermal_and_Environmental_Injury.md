---
name: A6 destination table
description: Where every section of Corpus B/A6_Thermal_and_Environmental_Injury.md goes, including the sections that were discarded.
bfile: Corpus B/A6_Thermal_and_Environmental_Injury.md
built: 2026-08-31
---

# A6_Thermal_and_Environmental_Injury — destination table

Committed **before** any content was written. 5 497 words, 8 sections.
**2 placements · 6 discards.** **The largest genuine gap in the corpus, and the only one so
far where an entire clinical domain is missing rather than a discriminator within one.**

## The finding: the corpus has drug-induced hyperthermia and no environmental heat illness

Searching `heat stroke`, `heatstroke`, `heat exhaustion` and `hyperthermi` across both
corpora, both trees, returns **only**:

- `04_Neurology` §Serotonin Syndrome and NMS — **drug-induced** hyperthermia
- `14_03_Psych` — NMS again
- `03a_Anaesthetics_Primer` and `NEW_Drugs_02` — **malignant** hyperthermia
- `04_Neurology` L766 — hyperthermia as a "T" in the reversible causes of arrest

**Environmental heat illness — the exhaustion-to-stroke spectrum, exertional versus classic,
active cooling — appears nowhere.** In an Australian curriculum that is a conspicuous hole.

Hypothermia is the same shape: `01_Cardiovascular` **§0.12.11** covers **the ECG in
hypothermia only** — bradycardia, J wave, first-degree block, long QT — inside an
ECG-interpretation list. **No staging, no rewarming, no afterdrop, no arrest rules.**

## Four PRESENT verdicts that were false, all caught by reading

| Search | What it actually matched |
|---|---|
| `active cooling` | **malignant hyperthermia** cooling in `03a_Anaesthetics_Primer` — a different indication |
| `rewarming` | malignant hyperthermia again, and `NEW_Drugs_02` |
| `frostbite` | `14a-1_Psych_-_Substance_Misuse` — **cold injury from inhaling gas canisters**, not a frostbite entry |
| `drowning` | `15_19a_Paeds` — drowning as a **postnatal cause of cerebral palsy** — and a syncope history line in `NEW_Cardiology_and_Vascular` |

This is the generic-component trap (rule 9) at scale: four hits, four different contexts,
none of them the concept. **Reading each one is what separated them.**

## Confirmed present, and correctly owned

| Concept | Owner |
|---|---|
| electrical injury | `11_09b_Ortho_-_Trauma` |
| pressure immobilisation for envenomation | `NEW_Drugs_04_Antidotes_and_Antivenoms` |
| burns first aid, TBSA, rule of nines | `11_09b_Ortho_-_Trauma` §Burns and Scalds |
| carbon monoxide and cyanide | present |
| rhabdomyolysis | present |
| Osborn/J wave | `01_Cardiovascular` §0.12.11 — ECG only |

## Destination table

| A6 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Heat illness spectrum | `Corpus A/11_09b_Ortho_-_Trauma.md` | **ADDITIVE** |
| 0.2 | Heat stroke and severe hyperthermia | `Corpus A/11_09b_Ortho_-_Trauma.md` | **ADDITIVE** |
| 0.3 | Hyperthermia versus fever, and drug-induced hyperthermias | — | **DISCARD** — `04_Neurology` §Serotonin Syndrome and NMS is a purpose-built contrasting-pair entry, and malignant hyperthermia is in `03a` and `NEW_Drugs_02` |
| 0.4 | Heat intolerance | — | **DISCARD** — thyrotoxicosis and the endocrine causes are in `06_Metabolic_Medicine_and_Endocrinology` |
| 0.5 | Hypothermia | `Corpus A/11_09b_Ortho_-_Trauma.md` | **ADDITIVE** — the ECG stays owned by `01_Cardiovascular` §0.12.11 and is pointed at, not restated |
| 0.6 | Frostbite and non-freezing cold injury | `Corpus A/11_09b_Ortho_-_Trauma.md` | **ADDITIVE** |
| 0.7 | Drowning and submersion | `Corpus A/11_09b_Ortho_-_Trauma.md` | **ADDITIVE** |
| 0.8 | Electrical injury | — | **DISCARD** — `11_09b` already has it |

**Placed in `11_09b_Ortho_-_Trauma` and no new file created.** That file is already the
vault's injury home despite its orthopaedic filename — it holds Major Trauma, Burns and
Scalds, thoracic, splenic, liver, head and ocular trauma, electrical injury, and the
abdominal trauma merged from C1. Creating an "environmental injury" file would split the
domain. This is the §1.10 case again: Corpus A is not organised the way its filenames
suggest.

No `CONFLICT` raised.
