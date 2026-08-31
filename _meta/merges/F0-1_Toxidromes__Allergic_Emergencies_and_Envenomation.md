---
name: F0-1 destination table
description: Where every section of Corpus B/F0-1 goes. Every section was discarded — the file is fully superseded.
bfile: Corpus B/F0-1_Toxidromes__Allergic_Emergencies_and_Envenomation.md
built: 2026-08-31
---

# F0-1_Toxidromes__Allergic_Emergencies_and_Envenomation — destination table

Committed **before** any content was written. 6 157 words, 11 sections.
**0 placements · 11 discards. The first fully superseded file of the entire merge.**

**19 of 19 concepts tested were already present**, on both trees. Nothing was merged and
nothing needed to be.

## Why this file has no gaps

Its territory is owned four times over, and each owner is more specific than F0-1:

| Topic | Owner | Corpus |
|---|---|---|
| Toxidromes, activated charcoal, enhanced elimination, paracetamol nomogram, toxic alcohols and the osmolar gap, TCA toxicity | `14a-2_Psych_-_Overdose_and_Poisoning_Management` | A |
| Serotonin syndrome and NMS, with the reflex/tone discriminator | `04_Neurology` | A |
| Anaphylaxis, ASCIA adrenaline, biphasic reactions, tryptase | `09_01_Dermatology`, `15_01b_Paeds`, `NEW_Drugs_01` | A + C |
| **Envenomation — pressure immobilisation, antivenoms, SVDK, VICC** | **`NEW_Drugs_04_Antidotes_and_Antivenoms`** | **C** |
| Per-drug overdose detail, QRS widening and bicarbonate | `NEW_Drugs_17_Psychotropic`, `NEW_Drugs_06_Cardiovascular` | C |

**This is the file that settled the envenomation question.** The category audit implied a
corpus gap; F0-1 and `NEW_Drugs_04` between them show there was never one.

## The one apparent absence, and it was a search artifact

`sodium bicarbonate for TCA` returned **ABSENT**. It is present **twice**:

- `14a-2` **L28** — a table row: *"**Tricyclic antidepressants** | IV bicarbonate — ↓risk of
  seizures and arrhythmias."*
- `NEW_Drugs_17` **L57** — *"Overdose causes **QRS widening**, arrhythmia, seizures,
  hypotension and coma — **sodium bicarbonate is the key treatment for QRS widening**"*

The pattern required `sodium bicarbonate` within 40 characters of `TCA|tricyclic`. The
corpus writes **`IV bicarbonate`** in one place and puts the drug name on the other side of
the sentence in the other. **Word order and abbreviation, both at once** — the failure
recorded in rule 10's corollary, and the reason every "absent" verdict in this project gets
read before it is acted on.

## Destination table — all eleven discarded

| F0-1 § | Topic | Disposition |
|---|---|---|
| 0.1 | Toxidrome recognition framework | **DISCARD** — `14a-2` §0.1 |
| 0.2 | Anticholinergic | **DISCARD** — `14a-2`, `NEW_Drugs_12` |
| 0.3 | Cholinergic / organophosphates | **DISCARD** — SLUDGE present |
| 0.4 | Sympathomimetic vs serotonin toxicity | **DISCARD** — `04_Neurology` is a purpose-built contrasting-pair entry |
| 0.5 | Opioid respiratory depression | **DISCARD** — `04_Neurology` §Opioid Toxicity |
| 0.6 | Paracetamol overdose | **DISCARD** — `03_Gastrointestinal` §0.10 with King's College criteria, plus the nomogram |
| 0.7 | Beta-blocker and calcium channel blocker overdose | **DISCARD** — `NEW_Drugs_06` |
| 0.8 | Toxic alcohols | **DISCARD** — osmolar gap present |
| 0.9 | Anaphylaxis and acute allergic reaction | **DISCARD** — three owners, one with the verified ASCIA 2026 band table |
| 0.10 | Australian elapid snakebite | **DISCARD** — `NEW_Drugs_04` §0.2.1 is more detailed |
| 0.11 | Redback vs funnel-web | **DISCARD** — `NEW_Drugs_04` §0.2.2 |

**A fully superseded file is a legitimate and useful result**, not a failed merge. It says
the corpus was already complete in this domain — which, given the domain includes
anaphylaxis and snakebite, is worth knowing.
