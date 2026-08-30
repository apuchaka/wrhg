---
name: C6 destination table
description: Where every section of Corpus B/C6_Dyspepsia__Oesophageal_and_Anorectal_Disease.md goes, including the sections that were discarded.
bfile: Corpus B/C6_Dyspepsia__Oesophageal_and_Anorectal_Disease.md
built: 2026-08-31
---

# C6_Dyspepsia__Oesophageal_and_Anorectal_Disease — destination table

Committed **before** any content was written. 4 323 words, 6 sections.
**2 placements · 4 discards.** 22 of 28 concepts tested were already present.

Searches used the **rarer word alone** this time, per the C4/C5 lesson. **No false
negatives on this file** — the change worked.

## Confirmed genuine gaps, against Corpus A **and** Corpus C

| Concept | Verdict |
|---|---|
| **Barrett's management** — PPI plus endoscopic surveillance, and that **dysplastic** Barrett is treated endoscopically (RFA, EMR) rather than watched | **absent** — `13_06b` §0.3 gives D, R, S/Smx and Ix but stops before management |
| **anal fissure is posterior midline**, because that mucosa is relatively poorly perfused | **absent** — §0.23 has the ischaemic mechanism and the sphincter spasm but never the location or why |
| **thrombosed external haemorrhoid** — tense, tender, blue-purple, excision early | **absent** |
| **proctalgia fugax** | **absent** |
| **internal haemorrhoids are painless**, so pain means something else | **absent as a consequence** — §0.25 states the anatomy (*"internal haemorrhoids lie proximal to the dentate line"*) without drawing the clinical conclusion from it |
| **fundoplication** | **absent** |
| Barrett, achalasia, eosinophilic oesophagitis, oesophageal spasm, pharyngeal pouch, Plummer-Vinson, *H. pylori* eradication, urea breath test, PPI washout before testing, ALARM features, test-and-treat, levator ani syndrome, perianal abscess, GTN for fissure, anal cancer, pruritus ani, skin tags, rectal prolapse, condylomata, hidradenitis, pilonidal, GORD lifestyle measures | **present** |

### A gap C6 does not close

**Schatzki ring** is absent from the whole vault. `13_06b` §0.2 covers benign oesophageal
stricture generally, but not this specific entity. **C6 does not mention it either**, so
the merge cannot close it. Recorded here and added to the study list, not written from
memory.

## Ownership decisions

- **Barrett's belongs to `13_06b`, not `03_Gastrointestinal`.** §0.30 says so explicitly:
  *"Oesophageal carcinoma and Barrett's oesophagus are covered under the ENT/Dysphagia
  section of this source, not here."* The management block goes to the owner.
- ***H. pylori* eradication regimens were not touched.** C6's own frontmatter warning says
  they must come from **eTG Antibiotic**, which is login-gated, and
  `NEW_Investigations_Gastroenterology` already owns the testing. Permanently noted.
- **GTN for anal fissure** is already in `NEW_Drugs_12` and `NEW_Drugs_06`. The drug stays
  with the drug files; only the anatomy goes to the condition file.

## Destination table

| C6 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Dyspepsia, reflux, heartburn; ALARM features; PPI trial | — | **DISCARD** — §0.28 GORD and §0.29 gastritis, plus `NEW_Drugs_12` §0.1 for the drug classes |
| 0.1 | Fundoplication | `03_Gastrointestinal.md` §0.28 → folded into the §0.30.5 block | **PARTIAL** |
| 0.2 | Peptic ulcer disease and *H. pylori* | — | **DISCARD** — §0.27, and eradication regimens are login-gated |
| 0.3 | Oesophageal disease | — | **DISCARD** — `13_06b` and §0.30 own it |
| 0.3 | Barrett's surveillance and dysplasia management | `Corpus A/13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology.md` §0.3 | **ADDITIVE** |
| 0.4 | Anorectal pain — fissure location, thrombosed pile, proctalgia fugax | `03_Gastrointestinal.md` **new §0.30.5** *(see note)* | **ADDITIVE** |
| 0.5 | Anal lump | — | **DISCARD** — §0.22 pilonidal, §0.23 fissures, §0.24 fistulae, §0.25 haemorrhoids, and `08_08`/`17_07` for condylomata |
| 0.5 | Internal haemorrhoids are painless | folded into the anorectal block | **ADDITIVE** |
| 0.6 | Pruritus ani | — | **DISCARD** — `09_08_Dermatology` and `NEW_Drugs_12` |

> **Note on numbering:** the anorectal block is placed as **§0.25.1**, under Haemorrhoids,
> not §0.30.5 — §0.30 is Oesophageal Conditions and would have been the wrong parent. The
> row above records the first intention so the correction is visible.

No new file required. No `CONFLICT` raised.
