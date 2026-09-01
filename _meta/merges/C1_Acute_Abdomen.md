---
name: C1 placement record
description: Where each section of C1_Acute_Abdomen was placed under the section-level merge rule, and why. Replaces the superseded disposition table.
bfile: Corpus B/C1_Acute_Abdomen.md
rule: section-level merge
built: 2026-08-31
---

# C1_Acute_Abdomen — placement record

**Every section merged whole.** No gap check, no discard, no split. This file records a
**choice of destination**, not a verdict on coverage. The former disposition table is
superseded and is not evidence of anything.

## Placements

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | The Acute Abdomen — Framework | `03_Gastrointestinal` §0.41.3 | §0.41 is the presentation-led section; C1 is presentation-organised. Superseded the §0.1 fragment |
| 0.2 | Assessment, Peritonism, Core Ix | `03_Gastrointestinal` §0.41.4 | as above; superseded the §0.2 fragment |
| 0.3 | Right Upper Quadrant Pain | `03_Gastrointestinal` §0.41.10 | regional presentation belongs with the regional section, not with the biliary disease entries |
| 0.4 | Epigastric Pain | `03_Gastrointestinal` §0.41.11 | as above |
| 0.5 | Left Upper Quadrant Pain | `03_Gastrointestinal` §0.41.12 | as above |
| 0.6 | Right Iliac Fossa Pain | `03_Gastrointestinal` §0.41.13 | the appendicitis fragment at §0.18.1 is **left in place**; that duplication is marked and accepted |
| 0.7 | Left Iliac Fossa Pain | `03_Gastrointestinal` §0.41.14 | as above |
| 0.8 | Suprapubic Pain | `03_Gastrointestinal` §0.41.15 | as above |
| 0.9 | Generalised Pain and the Catastrophes | `03_Gastrointestinal` §0.41.5 | superseded the §0.9 fragment |
| 0.10 | Abdominal Trauma | `11_09b_Ortho_-_Trauma` | **the one section not placed in 03_GI.** The reader arrives from the mechanism, and that file already owns splenic, liver and abdominal trauma. Superseded the blunt-versus-penetrating fragment |
| 0.11 | The Acute Abdomen in Special Groups | `03_Gastrointestinal` §0.41.6 | superseded the §0.11 fragment |

## Cross-references retargeted

| B link | Retargeted to | Verified |
|---|---|---|
| `[[F0-3_Shock…]]` ascending cholangitis | §0.4 Ascending Cholangitis | header exists |
| `[[C7_Pancreatobiliary_Disease]]` | §0.11 Acute Pancreatitis | header exists |
| `[[C5_Bowel_Habit…]]` | §0.19 / §0.20 Bowel Obstruction | both exist |
| `[[C3_Jaundice…]]` | §0.38 Cirrhosis | header exists |
| `[[C4_Gastrointestinal_Bleeding]]` | §0.33 Upper GI Bleed | header exists |
| `[[F0-2…]] 0.3` DKA | `[[06_Metabolic_Medicine_and_Endocrinology]]` DKA | §0.16 exists |
| `[[F0-2…]] 0.5` **lactic acidosis** | **`TODO:link — F0-2 §0.5 (unmerged)`** | no built home — **corrected from an initial mis-retarget to DKA** |
| `[[A9_Transfusion…]]` | `[[10_08_Haemonc_-_Blood_Products_and_Transfusion]]` MTP | header exists |

**Left as TODO:** O1 early pregnancy · O2 later pregnancy · O5 pelvic and vulval ·
O6 sexual and reproductive health · H2 LUTS and retention · H4 scrotum, groin and loin ·
M5 paediatric GI · F0-5 renal colic. All unbuilt clusters.

## Connective tissue inherited from superseded fragments

- §0.1 → `(§0.37)`, `(§0.19, §0.20)`, `(§0.11)` on the must-not-miss list
- §0.2 → `(§0.3)` Murphy, `(§0.18)` Rovsing, `See §0.21 Hernias`, **and `CF-038`**
- §0.9 → `See §0.37 Ischaemic Bowel Disease`, `§0.6.6` owns the SBP neutrophil count
- §0.10 → `see Splenic trauma above`, `[[08_09…]]` post-splenectomy sepsis, **NO-BASELINE**
- §0.11 → **five obstetric/paediatric ownership pointers**: 17_04, 17_03, 16_14-15,
  16_08-09, 17_05, plus `[[NEW_Obstetrics]]` and 15_07 / 15_08

**Three of §0.11's five were nearly lost, and §0.2's CF-038 was lost and recovered.** Both
were caught by the per-section digit multiset, not by any content check.

## Conflicts

**None raised for C1.** The figure comparison at placement found no numeric disagreement
between any C1 section and its destination — C1 states very few figures, and the ones it
does (Alvarado, Hinchey) are named without values.

## Report

```
sections merged      11
destinations         03_Gastrointestinal × 10, 11_09b_Ortho_-_Trauma × 1
new-file proposals   0
conflicts raised     0
cross-refs           8 retargeted, 8 left as TODO (unbuilt clusters)
digit multiset       pass — no digits removed on any of the 11 sections
```
