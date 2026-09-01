---
name: C5 placement record
description: Where each section of C5 was placed under the section-level merge rule, and why.
bfile: Corpus B/C5_Bowel_Habit__Obstruction_and_Distension.md
rule: section-level merge
built: 2026-08-31
---

# C5_Bowel_Habit__Obstruction_and_Distension — placement record

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Bowel Obstruction | `03_Gastrointestinal` §0.39.1 | superseded the §0.1 fragment, under **§0.39 Ileus** where the pseudo-obstruction material already sat |
| 0.2 | Constipation | `03_Gastrointestinal` §0.42.1 | under **§0.42 Faecal Incontinence**, the file's only bowel-habit entry |
| 0.3 | Acute Diarrhoea and Gastroenteritis | **`08_10_Infectious_Disease_-_Diarrhoea_DDx_and_Gastroenteritis`** | **the one section not placed in 03_GI.** A whole file already owns diarrhoea and gastroenteritis; the reader goes there, not to the surgical GI file |
| 0.4 | Chronic Diarrhoea and Change in Bowel Habit | `03_Gastrointestinal` §0.40.1 | under **§0.40 Malabsorption**, where the chronic-diarrhoea workup lands |
| 0.5 | Abdominal Distension, Bloating, Flatulence | `03_Gastrointestinal` §0.41.9 | superseded the §0.5 fragment |
| 0.6 | Tenesmus and Rectal Symptoms | `03_Gastrointestinal` §0.25.3 | under **§0.25 Haemorrhoids**, where the anorectal material is |

## Cross-references retargeted

All B-file links resolved to their built homes: `[[F0-2…]]` → `[[06_Metabolic…]]` Acid-Base
Balance · `[[C2…]]` → §0.41.16 · `[[C1…]]` → §0.41 · `[[C4…]]` → §0.34.2 / §0.33 ·
`[[C3…]]` → §0.38.1 / §0.38 · `[[C6…]]` → §0.25 · `[[GER2…]]` → `[[18_Geriatrics…]]`.
Each verified before writing.

**Left as TODO:** GER8 procedure addendum · M5 paediatric GI · N6 dissociation and somatic ·
O5 pelvic and vulval · H2 LUTS and retention · O6 sexual and reproductive health.

## Connective tissue inherited

- §0.1 → `[[Investigation-Interpretation]]` owns the CT transition point; §0.19 and §0.20 are
  the mechanical entities, §0.39 the non-mechanical, and **operating on a pseudo-obstruction
  is harmful** — the point the destination does not make.
- §0.5 → `[[17_10_Ovarian_Cancer…]]` for the ovarian-cancer exclusion behind a new "IBS"
  label over 50, the SAAG at §0.6.2, the tympanic differentials at §0.19/§0.20/§0.39,
  functional bloating at §0.35, organomegaly and mass at §0.13 and §0.17.

## A tool defect found here

The cross-reference refusal fired on **§0.17 when the block carried it**. The regex `§[\d.]+`
ate the sentence-ending period, so `§0.17.` and `§0.17` compared unequal. A **false positive
in a refusal** — it wastes time rather than losing content, but it also meant the check could
not be trusted to mean what it said. Fixed; both directions re-tested.

## Report

```
sections merged      6
destinations         03_Gastrointestinal × 5, 08_10_Infectious_Disease_-_Diarrhoea × 1
new-file proposals   0
conflicts raised     0
cross-refs           7 retargeted, 6 left as TODO
digit multiset       pass — no digits removed on any of the 6 sections
```
