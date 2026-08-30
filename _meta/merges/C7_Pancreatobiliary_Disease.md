---
name: C7 destination table
description: Where every section of Corpus B/C7_Pancreatobiliary_Disease.md goes, including the sections that were discarded.
bfile: Corpus B/C7_Pancreatobiliary_Disease.md
built: 2026-08-31
---

# C7_Pancreatobiliary_Disease — destination table

Committed **before** any content was written. 4 458 words, 6 sections.
**2 placements · 4 discards.**

## One more false negative, and it was the biggest of the run

`Glasgow-Imrie` returned **ABSENT**. `03_Gastrointestinal` §0.11 **has the Glasgow score,
with the PANCREAS mnemonic and a `CRP >200` necrosis marker.** Glasgow-Imrie *is* the
Glasgow score — the corpus uses the shorter name.

This one mattered more than the others: had it been acted on, the merge would have written
a **second severity score into the same section as the first**, under a different name,
with no indication they were the same instrument. That is worse than a duplicate — it
would have read as two independent scores to choose between.

**The eponym trap, added to the search rules:** a score with a compound name
(`Glasgow-Imrie`, `Ranson`, `West Haven`) may appear under either half, or under neither.
Search the disease plus the word *score*, then read.

## Confirmed genuine gaps, against Corpus A **and** Corpus C

| Concept | Verdict |
|---|---|
| **revised Atlanta classification** — mild / moderately severe / severe, by **transient vs persistent** organ failure | **absent**; `organ failure` appears in §0.11 but not the classification |
| **severity is judged by organ failure and trajectory, not by the lipase level** | **absent** |
| **the step-up approach** to infected necrosis — percutaneous or endoscopic drainage before surgery | **absent**; §0.11 names *infected necrosis* but not its management |
| **necrosectomy**, **percutaneous drainage** | **absent** |
| **walled-off necrosis**, and how it differs from a pseudocyst | **absent**; §0.11 has *pseudocyst* only |
| **splenic vein thrombosis** as a complication of chronic pancreatitis | **absent** |
| **type 3c (pancreatogenic) diabetes** | **absent** |
| Glasgow score, GET SMASHED, Cullen, Grey Turner, necrotising pancreatitis, pseudocyst, early enteral feeding, aggressive fluids, ERCP, same-admission cholecystectomy, PERT, faecal elastase, CA 19-9, double duct sign, Courvoisier, Whipple, subphrenic abscess, ARDS, hypocalcaemia | **present** |

## Destination table

| C7 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Acute pancreatitis diagnosis, GET SMASHED, Cullen/Grey Turner, lipase | — | **DISCARD** — §0.11 has all of it, including the Glasgow score |
| 0.1 | Revised Atlanta classification; severity is not the lipase | `03_Gastrointestinal.md` **new §0.11.2** | **ADDITIVE** |
| 0.2 | Management — fluids, enteral feeding, ERCP, cholecystectomy timing | — | **DISCARD** — §0.11 covers each |
| 0.2 | Step-up approach, walled-off necrosis, necrosectomy | `03_Gastrointestinal.md` §0.11.2 | **ADDITIVE** |
| 0.3 | Chronic pancreatitis | — | **DISCARD** — §0.12, with PERT and faecal elastase |
| 0.3 | Type 3c diabetes, splenic vein thrombosis | `03_Gastrointestinal.md` **new §0.12.1** | **ADDITIVE** |
| 0.4 | Pseudocyst and fluid collections | — | **DISCARD** — §0.11 pseudocyst; the walled-off-necrosis distinction moves to §0.11.2 |
| 0.5 | Intra-abdominal abscess | — | **DISCARD** — subphrenic abscess is in `History-Taking` and `NEW_Cardiology_and_Vascular`; §0.41.5 (merged from C1) covers the generalised-peritonitis presentation, and drainage principles belong to surgery rather than to a gastroenterology file |
| 0.6 | Pancreatic malignancy | — | **DISCARD** — §0.14, with CA 19-9, the double duct sign, Courvoisier and Whipple |

No new file required. No `CONFLICT` raised.

## Figures: what was carried and what was not

The **48-hour organ-failure threshold** in the Atlanta classification **is** carried, because
it is the definition of the categories rather than a cut-off applied to a measurement —
without it the three grades cannot be stated at all. It carries C7's `UNVERIFIED` marker
with a named source added.

**No score components were carried.** Ranson, BISAP, APACHE II and the 48-hour CRP cut-off
are named as instruments that exist, with their components and thresholds left to the
marker. §0.18's Alvarado history is the precedent: a score transcribed from memory was
wrong in two ways and took a duplicate-pair audit to catch.
