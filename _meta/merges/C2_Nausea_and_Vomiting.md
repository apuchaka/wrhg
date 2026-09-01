---
name: C2 placement record
description: Where each section of C2_Nausea_and_Vomiting was placed under the section-level merge rule, and why.
bfile: Corpus B/C2_Nausea_and_Vomiting.md
rule: section-level merge
built: 2026-08-31
---

# C2_Nausea_and_Vomiting — placement record

Every section merged whole. Records a **choice of destination**, not a verdict on coverage.

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Mechanism | `03_Gastrointestinal` §0.41.16 | §0.41 is the presentation section and already hosts the vomiting material |
| 0.2 | Acute Vomiting — Differential and Red Flags | `03_Gastrointestinal` §0.41.17 | as above |
| 0.3 | Bilious versus Non-Bilious | `03_Gastrointestinal` §0.41.7 | superseded the §0.3 fragment; the pyloric-stenosis fragment in `15_08` is **left in place** |
| 0.4 | Chronic and Refractory | `03_Gastrointestinal` §0.41.18 | as above |
| 0.5 | **Antiemetic Selection by Mechanism** | **`NEW_Drugs_12_Gastrointestinal` §0.2.5** | **the one section not placed in 03_GI.** A drug-class selection table — which agent for which receptor — which §1.11 assigns to the drug file. That file already says *"Choose the antiemetic by the MECHANISM of the vomiting, not by habit"*; this is the fuller version of it. Superseded the §0.5 fragment |
| 0.6 | Appetite Change, Early Satiety, Anorexia | `03_Gastrointestinal` §0.41.19 | a GI presentation; the reader arrives from the symptom |
| 0.7 | Complications of Vomiting | `03_Gastrointestinal` §0.41.20 | the dental-erosion fragment in `14_05a` is **left in place** |

## Cross-references retargeted

| B link | Retargeted to | Verified |
|---|---|---|
| `[[C4_Gastrointestinal_Bleeding]]` | §0.33 Upper GI Bleed | exists |
| `[[C5_Bowel_Habit…]]` | §0.19 / §0.20 Bowel Obstruction | exists |
| `[[C1_Acute_Abdomen]] 0.11` | §0.41.6 — **the section merged from C1 earlier today** | exists |
| `[[D1_Headache_and_Meningism]]` | `[[04_Neurology]]` Other Headache Causes | exists |
| `[[F0-5…]] 0.6` | `[[04_Neurology]]` CT Head, Head Injury, and Intracranial Pressure | exists |
| `[[F0-2…]] 0.3` DKA | `[[06_Metabolic…]]` Diabetic Ketoacidosis (DKA) | exists |
| `[[F0-2…]] 0.7` alkalosis | `[[06_Metabolic…]]` Acid-Base Balance | exists |
| `[[B3_Arrhythmia…]] 0.3` | `[[01_Cardiovascular]]` Long QT Syndrome | exists |
| `[[B1_Chest_Pain…]] 0.1` | `[[01_Cardiovascular]]` Acute Coronary Syndrome (ACS) | exists — corrected from "Syndromes" |
| `[[B6_Oedema…]] 0.5` | `TODO:link — B6 §0.5 (unmerged)` | no built home |

**Left as TODO:** O1 early pregnancy · N8 eating and body image · N6 dissociation and
somatic · J5 oncology and palliative · I5 weight and lipids · F0-2 §0.5 lactic acidosis.

## Connective tissue inherited

§0.3's superseded fragment carried three pointers, **all three initially lost and recovered**:
`§0.20` Large Bowel Obstruction on faeculent vomiting, `(§0.27)` on gastric outlet
obstruction, and `[[13_06b_ENT…]]` on undigested food. The fragment also held C2 §0.4's
cannabinoid hyperemesis, which now merges whole at §0.41.18.

## Report

```
sections merged      7
destinations         03_Gastrointestinal × 6, NEW_Drugs_12_Gastrointestinal × 1
new-file proposals   0
conflicts raised     0
cross-refs           10 retargeted, 6 left as TODO
digit multiset       pass — no digits removed on any of the 7 sections
```

**No conflict raised.** The placement figure comparison found no numeric disagreement:
C2's figures are the pyloric-stenosis biochemistry and the QT agents, and the destination
sections state neither differently.
