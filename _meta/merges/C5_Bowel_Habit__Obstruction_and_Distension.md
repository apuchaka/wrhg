---
name: C5 destination table
description: Where every section of Corpus B/C5_Bowel_Habit__Obstruction_and_Distension.md goes, including the sections that were discarded.
bfile: Corpus B/C5_Bowel_Habit__Obstruction_and_Distension.md
built: 2026-08-31
---

# C5_Bowel_Habit__Obstruction_and_Distension — destination table

Committed **before** any content was written. 4 352 words, 6 sections.
**2 placements · 5 discards.** The most heavily superseded file in Block 1 so far —
**23 of 25 concepts tested were already present.**

## Searches that returned ABSENT and were wrong

| Search | Reality |
|---|---|
| `hernia.{0,40}obstruct` | **Present three times**, and word order defeated it every time: §0.21.1 (*"Richter — herniation of only part of the bowel wall… can strangulate without causing obstruction"*), §0.41.2 (*"strangulated hernia"* under Intestinal), and §0.41.4 (*"Palpate both groins in every patient with abdominal pain or obstruction"*). Rule 2 |

Six false negatives across C4 and C5 now share one cause: **a regex requiring two terms in
a fixed order.** The corpus writes *prophylactic antibiotics* not *antibiotic prophylaxis*,
*strangulated hernia* not *hernia… obstruction*. Where a concept is two words that can
appear in either order, search for the **rarer word alone** and read the hits.

## Step 17 check

C5 was searched for UK-localisation leftovers before merging — `two-week wait`, `2ww`,
`NICE`, `NHS`, `GMC`, `A&E`, `co-amoxiclav`. **No hits.** The `rectal bleeding urgent
referral` gap is real in Corpus A but C5 does not state a pathway either, so nothing was
imported and no UK referral route entered the corpus.

## Confirmed genuine gaps, against Corpus A **and** Corpus C

| Concept | Verdict |
|---|---|
| **acute colonic pseudo-obstruction (Ogilvie syndrome)** | **absent** — §0.39 covers *paralytic* ileus thoroughly but not this |
| **the CT transition point** as the discriminator between mechanical and non-mechanical | **absent** |
| **the six Fs** of a distended abdomen | **absent** |
| **new "IBS" in a woman over 50 is ovarian cancer until excluded** | **absent** — `17_10` has early satiety as an ovarian symptom, but not the IBS-misattribution trap |
| closed-loop obstruction, strangulation, adhesions, drip-and-suck, Gastrografin, hernia-as-cause, faecal impaction with overflow, opioid constipation, bowel-habit red flags, Bristol chart, *C. difficile*, traveller's diarrhoea, notifiable disease, food-handler exclusion, HUS, avoiding antibiotics in STEC, coeliac serology, faecal calprotectin, bile acid malabsorption, microscopic colitis, tenesmus, volvulus coffee-bean sign | **present** |

## Destination table

| C5 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Bowel obstruction — level, cardinal features, causes, management | — | **DISCARD** — §0.19 SBO, §0.20 LBO, §0.20.1 volvulus and §0.21 hernias cover it, and §0.41.5 (merged from C1) adds the simple-vs-strangulated distinction |
| 0.1 | Ileus vs pseudo-obstruction vs mechanical; Ogilvie; the transition point | `03_Gastrointestinal.md` **new §0.39.1** | **PARTIAL** — the ileus half is discarded to §0.39, which is more detailed |
| 0.2 | Constipation | — | **DISCARD** — §0.42 faecal incontinence, `NEW_Drugs_12` §0.5 laxatives, and the paediatric files |
| 0.3 | Acute diarrhoea and gastroenteritis | — | **DISCARD** — `08_10_Infectious_Disease_-_Diarrhoea_DDx_and_Gastroenteritis` is a purpose-built file, and STEC/HUS is in `08_01-03` and `07_Renal` |
| 0.4 | Chronic diarrhoea and change in bowel habit | — | **DISCARD** — §0.35 IBS, §0.40 malabsorption, §0.17 coeliac, §0.16 IBD, §0.26 colorectal cancer |
| 0.5 | Distension — the six Fs, and the ovarian cancer trap | `03_Gastrointestinal.md` **new §0.41.9** | **ADDITIVE** |
| 0.5 | Ascites, functional bloating, SIBO, mass | — | **DISCARD** — §0.6.2 ascites with SAAG, §0.13 SIBO, §0.35 IBS |
| 0.6 | Tenesmus and rectal symptoms | — | **DISCARD** — §0.23 fissures, §0.24 fistulae, §0.25 haemorrhoids, §0.26 colorectal cancer |

No new file required. No `CONFLICT` raised.
