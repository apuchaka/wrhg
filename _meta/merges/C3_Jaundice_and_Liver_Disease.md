---
name: C3 destination table
description: Where every section of Corpus B/C3_Jaundice_and_Liver_Disease.md goes, including the sections that were discarded.
bfile: Corpus B/C3_Jaundice_and_Liver_Disease.md
built: 2026-08-30
---

# C3_Jaundice_and_Liver_Disease — destination table

Committed **before** any content was written. 4 595 words, 7 sections.
**3 placements · 5 discards.**

Liver disease is the most heavily built area of Corpus A (`03_Gastrointestinal` §0.1–§0.11
and §0.38 are almost entirely hepatology) and Corpus C owns the test interpretation. C3
is therefore mostly duplicative.

## Two findings that changed the placement

### 1. The LFT block is superseded on provenance, entirely

`Corpus C/NEW_Investigations_Gastroenterology.md` §0.1 is `trust: snippet` and already
states, in its own words: *"'Liver function tests' is a misnomer — ALT, AST, ALP and GGT
are markers of hepatocyte injury or cholestasis, not of function. True synthetic function
is albumin, INR/prothrombin time and bilirubin."* It also has the AST:ALT > 2 ratio with
its mechanism, GGT confirming a raised ALP is hepatic rather than bony, and ALP
physiologically raised in pregnancy and childhood.

C3's LFT block says the same things with no source. **Discarded on provenance**
(`snippet` over `unverified`), except one item: the **pathological** differential for a
raised ALP with a normal GGT — Paget disease, metastases, osteomalacia, healing fracture.
Corpus C names the bone/liver distinction but not what bony causes to think of.

### 2. A search that said ABSENT was wrong — rule 2

`hepatic encephalopathy grading` was searched as `West Haven` and
`grade[sd]? of hepatic enceph` and returned **nothing**. Reading the file shows
`03_Gastrointestinal` §0.6.3 **already carries the full four-grade scale**, under the
heading `> [!info] Grading`. The scale is there; only the eponym is not.

Zero grep hits was not proof of absence, exactly as rule 2 says. The grading block is
therefore **not** merged, and naming it West Haven is left as a note for review rather
than an edit, since renaming an existing clinical block is not an additive merge.

### 3. A gap that was not C3's to fill

`Dubin-Johnson` and `Rotor` are absent from the whole vault — but they are **also absent
from C3**. The gap is real and C3 does not close it. Recorded here so the gap is not
lost, and so nobody later assumes the merge covered it.

## Vault-wide searches (Corpus A **and** C, after C2's false-gap lesson)

| Concept | Verdict |
|---|---|
| prehepatic / hepatic / posthepatic classification | **absent** |
| the urine-and-stool discriminator for conjugated vs unconjugated | **absent** |
| bone differential for raised ALP with normal GGT | **absent** (C names bone vs liver, not the causes) |
| hepatopulmonary syndrome, portopulmonary hypertension | **absent** |
| platypnoea-orthodeoxia | **absent** |
| Dubin-Johnson, Rotor | absent from the vault **and** from C3 — not closed by this merge |
| hepatic hydrothorax | absent from the vault; C3 does not cover it either |
| Gilbert, Crigler-Najjar, kernicterus, Courvoisier, pale stool/dark urine, King's College criteria, asterixis, SAAG, hepatorenal, Child-Pugh, MELD, caput medusae, spider naevi, Dupuytren, leuconychia, N-acetylcysteine, Budd-Chiari, cholestatic pruritus | **present** |
| hepatic encephalopathy grading | **present** — found by reading, not by grep (see above) |

## Destination table

| C3 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Bilirubin metabolism, the urine/stool discriminator, three-way classification | `03_Gastrointestinal.md` **new §0.41.8** | **ADDITIVE** |
| 0.1 | LFT pattern reading, injury vs function | — | **DISCARD on provenance** — `NEW_Investigations_Gastroenterology` §0.1 is `snippet` and says all of it |
| 0.1 | Bone differential for raised ALP with normal GGT | `Corpus C/NEW_Investigations_Gastroenterology.md` §0.1 | **PARTIAL** — the one item C does not carry |
| 0.2 | Unconjugated hyperbilirubinaemia | — | **DISCARD** — Gilbert and Crigler-Najjar are present; C3 adds no Dubin-Johnson or Rotor to fill the real gap |
| 0.3 | Conjugated and obstructive jaundice | — | **DISCARD** — `03_Gastrointestinal` §0.1–§0.5 (PSC, PBC, cholecystitis, cholangitis, liver cancers) covers it in far more depth, and Courvoisier is already there |
| 0.4 | Acute liver failure | — | **DISCARD** — King's College criteria at §0.10.1, paracetamol at §0.10, and `NEW_Investigations` §0.1 gives the transaminase-plus-INR rule |
| 0.5 | Chronic liver disease and cirrhosis | — | **DISCARD** — §0.38 is a purpose-built standalone cirrhosis entry with every stigma C3 lists |
| 0.6 | Portopulmonary hypertension, hepatopulmonary syndrome, platypnoea-orthodeoxia | `03_Gastrointestinal.md` §0.38 | **ADDITIVE** |
| 0.6 | Ascites, SBP, varices, encephalopathy, hepatorenal, coagulopathy | — | **DISCARD** — §0.6.2–§0.6.6 and §0.33 each cover these, and §0.6.6 owns the SBP threshold |
| 0.7 | Hepatomegaly, splenomegaly, hepatic pain | — | **DISCARD** — `Examination.md` owns organomegaly technique; `03_Gastrointestinal` §0.41 owns the regional DDx |

No new file required. No `CONFLICT` raised — C3 contradicts nothing.
