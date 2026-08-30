---
name: C2 destination table
description: Where every section of Corpus B/C2_Nausea_and_Vomiting.md goes, including the sections that were discarded.
bfile: Corpus B/C2_Nausea_and_Vomiting.md
built: 2026-08-30
---

# C2_Nausea_and_Vomiting — destination table

Committed **before** any content was written.

**C2 is a mostly-discard file, and that is the finding.** 3 876 words in 7 sections;
**4 placements, 5 discards.** Nausea and vomiting is already covered across Corpus A
and — critically — across **Corpus C**, which outranks C2 on provenance.

## The provenance finding that decided most of this file

`Corpus C/NEW_Drugs_12_Gastrointestinal.md` §0.2 **Antiemetics** is `trust: snippet`,
AMH-derived. It already contains everything C2 §0.5 offers, in more detail:

| C2 §0.5 claim | Already in `NEW_Drugs_12` §0.2 |
|---|---|
| match the antiemetic to the mechanism | the section's opening `[!info]`, same mapping in prose |
| metoclopramide/prochlorperazine cause acute dystonia; treat with benztropine | §0.2.2 `[!danger]`, **plus** the 5-day and 12-week limits, tardive dyskinesia, and the Parkinson's/domperidone point C2 lacks |
| do not give a prokinetic in mechanical obstruction | §0.2.2 contraindication line, verbatim in substance |
| ondansetron, droperidol, haloperidol, domperidone prolong QT | §0.2.1 and §0.2.2, per agent |
| ondansetron causes constipation | §0.2.1, **and** names it as the cause of the abdominal pain that follows |
| aprepitant for delayed chemotherapy nausea | §0.2.3, with the CYP3A4 and contraceptive interaction C2 lacks |
| pregnancy agent choice differs | §0.2.4 names pyridoxine + doxylamine and the ondansetron cleft signal |

**C2 §0.5 is superseded on provenance, not on content** — `snippet` (guideline-derived)
over `unverified` (model knowledge). CLAUDE.md §1.10: Corpus B can never win
automatically, and it carries no source here. Two small points survive as an additive
block; everything else is discarded.

This also means "aprepitant is absent" — true of Corpus A — was **not** a gap.
It is in Corpus C. Checking only Corpus A would have produced a false gap.

## Vault-wide searches run before placement

| Concept | Verdict |
|---|---|
| ampulla of Vater as the bilious/non-bilious landmark | **absent** |
| "double bubble" of duodenal atresia | **absent** |
| palpable "olive", visible gastric peristalsis | **absent** (A has *test feeding* and the pyloric "tumour", not these) |
| correcting the alkalosis **before** theatre, and why (post-operative apnoea) | **absent** |
| cannabinoid hyperemesis syndrome | **absent** |
| dental erosion and parotid enlargement in self-induced vomiting | **absent** |
| CTZ, vomiting centre, metoclopramide, ondansetron, prochlorperazine, cyclizine, droperidol, hyoscine, gastroparesis, Mallory-Weiss, Boerhaave, hyperemesis, refeeding, QT, akathisia, malrotation, paradoxical aciduria, Wernicke, faeculent vomiting, achalasia, aspiration pneumonitis | **present** |

### Search artifact caught — rule 9, and it was my own pattern

`cannabinoid hyperemesis` was searched with `hot shower` as an alternative, since the
compulsive hot bathing is the classic feature. It returned two Corpus A files and
**both were false positives**: `04_Neurology` L1331 (a hot shower triggering
**Uhthoff's phenomenon** in multiple sclerosis) and `09_08_Dermatology` L185 (avoiding
hot showers in **pruritus**). The literal term appears nowhere. The gap is real, but
the search that found it was briefly wrong in the other direction.

`hungry` was also too loose to be evidence of anything — it matched appendicitis
anorexia and eating-disorder content. Dismissed and re-checked specifically.

## Destination table

| C2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Nausea and vomiting — mechanism, CTZ, vomiting centre | — | **DISCARD** — `03a_Anaesthetics_Primer` L184–186 already sets out the vomiting-centre pathway and its four inputs, and `NEW_Drugs_12` §0.2.1 gives the receptor detail |
| 0.2 | Acute vomiting — differential and red flags | — | **DISCARD** — the differential duplicates `03_Gastrointestinal` §0.41.2 and `History-Taking`; the red flags duplicate §0.41's danger callout |
| 0.3 | Bilious vs non-bilious — the ampulla principle, adult patterns | `Corpus A/03_Gastrointestinal.md` **new §0.41.7** | **ADDITIVE** |
| 0.3 | Paediatric signs within it | `Corpus A/15_08_Paeds_-_Surgical_Abdomen…` Pyloric stenosis | **PARTIAL** — only the three points A lacks; A's entry is otherwise more detailed and **owns** the ultrasound thresholds and fluid regimen, so C2's `UNVERIFIED — the measurement thresholds` was **not** carried across |
| 0.3 | Malrotation/midgut volvulus block | — | **DISCARD** — `15_09a_Paeds_-_Congenital_Abdominal_Wall…` and `03_Gastrointestinal` both cover it, including the duodenojejunal flexure study |
| 0.4 | Chronic and refractory nausea — cannabinoid hyperemesis | `Corpus A/03_Gastrointestinal.md` §0.41.7 | **PARTIAL** — cannabinoid hyperemesis only; gastroparesis and cyclical vomiting are already in `04_Neurology` and `15_17a` |
| 0.5 | Antiemetic selection by mechanism | — | **DISCARD on provenance** — see the table above. `NEW_Drugs_12` §0.2 is `snippet` and more complete |
| 0.5 | QT stacking check; opioid-nausea tolerance | `Corpus C/NEW_Drugs_12_Gastrointestinal.md` §0.2 | **ADDITIVE** — the two points `NEW_Drugs_12` does not make |
| 0.6 | Appetite change, early satiety, anorexia | — | **DISCARD** — early satiety is already in `03_Gastrointestinal`, `10_01_Haemonc` and `17_10_Ovarian_Cancer` as a red flag in each relevant disease, which is where it belongs |
| 0.7 | Complications — Wernicke, alkalosis, Mallory-Weiss, Boerhaave, aspiration, refeeding | — | **DISCARD** — every one is present: Wernicke and thiamine-before-glucose in `04_Neurology`, Mallory-Weiss and Boerhaave in `03_Gastrointestinal` §0.30, refeeding in `14_05a` and `15_07`, aspiration pneumonitis in `02_Respiratory` |
| 0.7 | Dental erosion and parotid enlargement | `Corpus A/14_05a_Psych_-_Eating_Disorders.md` | **ADDITIVE** — the one complication absent from the vault |

**4 placements · 5 discards · 2 partials.**

No new file was required. No `CONFLICT` was raised — C2 disagrees with nothing;
it is duplicative rather than contradictory.
