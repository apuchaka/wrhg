---
name: A8 destination table
description: Where every section of Corpus B/A8_Foreign_Bodies_by_Site.md goes, including the sections that were discarded.
bfile: Corpus B/A8_Foreign_Bodies_by_Site.md
built: 2026-08-31
---

# A8_Foreign_Bodies_by_Site — destination table

Committed **before** any content was written. 4 410 words, 8 sections.
**4 placements · 4 discards.** **The second A6-shaped finding: a domain the checklist never
asked for and the corpus never built.**

## The finding: button battery ingestion is absent from all 240 files

`batter` returns six hits across both corpora. **Not one is a button battery:**

| Hit | What it is |
|---|---|
| `04_Neurology` L350 | "a **battery** of tests" |
| `08_09_Infectious_Disease` L120 | "a reflexive **battery** of tests" |
| `15_18a_Paeds` L21 | unrelated |
| `NEW_Drugs_15` L72 | unrelated |
| `NEW_Exam_Manoeuvres` L411 | **pacemaker battery** |
| `NEW_Investigations_Orthopaedics` L537 | **Short Physical Performance Battery** |

A button battery lodged in the oesophagus causes **liquefactive necrosis within hours** and
is one of the highest-stakes paediatric presentations there is. **It appears nowhere.**

**And the XR sign search was a rule 9 false positive**: `halo sign` returned three files, all
of them **aspergillosis** (`02_Respiratory`) and **temporal artery ultrasound** (`12_04`,
`NEW_Investigations_Rheumatology`). Neither the entity nor its radiographic sign exists.

## Confirmed absent, verified individually

| Concept | Verdict |
|---|---|
| **button battery ingestion**, and the halo/double-ring sign | **absent, both trees** |
| **rust ring** after a corneal foreign body | **absent** |
| **mother's kiss** technique for a nasal foreign body | **absent** |
| **live insect in the ear canal** | **absent** |
| **rectal foreign body** | **absent** |
| **vaginal foreign body** | **absent** as an entity (`retained tampon` is present in the gynaecology files) |
| coin ingestion, sharp/long object rules | **absent** — `coin` returned 12 files, all *coincide*/*coincidental* |
| magnets, body packing, inhaled FB and unilateral wheeze, back blows, intraocular FB, soft-tissue FB and ultrasound for radiolucent wood, food bolus, Poisons Information Centre | **present** |

## Destination table

| A8 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | General principles | — | **DISCARD** — safeguarding, radiolucent FB and ultrasound already present |
| 0.2 | Aural foreign body | `Corpus A/13_02_ENT_-_Hearing_Loss__Tinnitus__Vertigo__DDx_Charts_.md` | **ADDITIVE** |
| 0.3 | Nasal foreign body | `Corpus A/13_04_ENT_-_Nose…` | **ADDITIVE** |
| 0.4 | Corneal and ocular foreign body | `Corpus A/05_Ophthalmology.md` | **PARTIAL** — rust ring only; intraocular FB and the hammering-metal history are present |
| 0.5 | Oropharyngeal foreign body | — | **DISCARD** — `13_05b_ENT` and the airway files |
| 0.6 | **Swallowed foreign body — button battery, magnets, coins, sharps** | `Corpus A/13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology.md` | **ADDITIVE — the important one** |
| 0.7 | Rectal foreign body | `Corpus A/03_Gastrointestinal.md` §0.25.1 | **ADDITIVE** |
| 0.8 | Vaginal foreign body | — | **DISCARD** — `17_08_Vaginal_Discharge…` owns retained tampon and the safeguarding framing |

No new file required. **No `CONFLICT` raised.**

## Checklist implication, recorded for the 872-row audit

Neither `Injury, Poisoning, Envenomation & Environmental` nor `ENT` has a foreign-body row.
**This is the third domain found missing from checklist and corpus together** — after
environmental injury and recognising dying. All three were found by the merge, and only
because a Corpus B file happened to cover them.
