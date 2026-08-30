---
name: C4 destination table
description: Where every section of Corpus B/C4_Gastrointestinal_Bleeding.md goes, including the sections that were discarded.
bfile: Corpus B/C4_Gastrointestinal_Bleeding.md
built: 2026-08-31
---

# C4_Gastrointestinal_Bleeding — destination table

Committed **before** any content was written. 3 665 words, 5 sections.
**2 placements · 4 discards.**

`03_Gastrointestinal` §0.33 (UGIB), §0.34 (LGIB) and §0.6.4 (varices) are among the most
worked parts of Corpus A, and `NEW_Gastroenterology_and_Hepatology` covers the rest. C4
is largely duplicative.

## Five searches returned ABSENT and were wrong — the largest artifact count of any file so far

Each of these would have produced a duplicate merge if acted on. All were caught by
reading the destination before writing.

| Search | Returned | Reality |
|---|---|---|
| `antibiotic prophylaxis` near `variceal\|cirrho`; `ceftriaxone.*variceal` | ABSENT | **Present twice.** §0.6.4: *"prophylactic antibiotics (quinolones — reduces mortality and rebleeding)"*; §0.33.3: *"terlipressin and prophylactic antibiotics at presentation (before endoscopy)"*. The corpus writes **prophylactic antibiotics**, not *antibiotic prophylaxis*. Word order defeated the search — **rule 2** |
| `PPI infusion`, `proton pump inhibitor infusion` | ABSENT | The **topic** is present and better stated than C4's: §0.33.3 says *"do NOT give PPIs before endoscopy — give after… pre-treatment PPI doesn't improve outcomes and may mask endoscopic findings"*. Only the infusion **regimen** is missing, which is a dose and therefore login-gated |
| `portal pressure`, `over-transfus` | ABSENT (first pass) | **Present in `NEW_Gastroenterology_and_Hepatology`** — Corpus C. The A-and-C rule caught it; searching A alone would have merged a duplicate |
| `second-look endoscopy` | PRESENT | **False positive.** The only hit is *second-look **ultrasound*** for breast MRI in `NEW_Investigations_Orthopaedics_Neurology_and_Other` L356. A different investigation entirely — **rule 9** |
| `precipitat.*encephalopath` | ABSENT in `03_GI` | §0.6.3 already lists *"GI bleed"* among encephalopathy precipitants. Only the **mechanism** (protein load of blood in the gut) and the lactulose rationale are missing |

## Confirmed genuine gaps, against Corpus A **and** Corpus C

| Concept | Verdict |
|---|---|
| balloon tamponade as a time-limited bridge, intubated, risk of oesophageal necrosis | **absent** — A prescribes the Sengstaken tube without any caveat |
| lactulose to clear blood from the gut after a variceal bleed | **absent** |
| portal hypertensive gastropathy, and that it is treated with beta-blockade rather than banding | **absent** |
| that a substantial proportion of bleeds in cirrhotic patients are from **ulcers**, so the source cannot be assumed variceal | **absent** |
| `AIMS65` | **absent** (A has Glasgow-Blatchford and Rockall at §0.33.2 L1268–1269) |
| `Forrest` classification of ulcer stigmata | **absent** |
| second-look endoscopy in GI bleeding | **absent** (see the false positive above) |
| NG aspirate in suspected UGIB | **absent** |
| terlipressin, octreotide, band ligation, TIPS, Sengstaken, restrictive transfusion, massive transfusion, melaena, haematochezia, coffee-ground, urea rise, angiodysplasia, Dieulafoy, aorto-enteric fistula, capsule endoscopy, FIT, iron deficiency, PCC/anticoagulant reversal | **present** |

## Destination table

| C4 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | GI bleeding framework and resuscitation | — | **DISCARD** — §0.33.3's resuscitation danger-box is more specific (platelet, FFP and PCC triggers), and `10_08_Haemonc` owns transfusion |
| 0.2 | Non-variceal UGIB — Forrest, second-look, NG aspirate, AIMS65 | `03_Gastrointestinal.md` **new §0.33.4** | **PARTIAL** — the four absent items only; the rest duplicates §0.27, §0.29, §0.33 |
| 0.3 | Variceal bleeding — the four absent points | `03_Gastrointestinal.md` **new §0.6.7** | **PARTIAL** |
| 0.3 | Management sequence, antibiotics, terlipressin, banding, TIPS, prophylaxis | — | **DISCARD** — §0.6.4 and §0.33.3 both carry it, including the antibiotics C4 calls "one of the most frequently omitted interventions" |
| 0.4 | Lower GI bleeding | — | **DISCARD** — §0.34 with its DDx-by-location and Ix, plus §0.36 diverticular and §0.25 haemorrhoids |
| 0.5 | Occult and obscure bleeding, iron deficiency anaemia | — | **DISCARD** — §0.40 malabsorption, §0.26 colorectal cancer, `NEW_Investigations_Gastroenterology` capsule endoscopy, and the haematology files own the anaemia |

No new file required. No `CONFLICT` raised — C4 contradicts nothing; where it overlaps
A it agrees, and agreement is not corroboration (§1.10), so nothing was upgraded.
