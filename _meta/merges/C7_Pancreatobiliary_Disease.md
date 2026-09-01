---
name: C7 placement record
description: Where each section of C7 was placed under the section-level merge rule, and why.
bfile: Corpus B/C7_Pancreatobiliary_Disease.md
rule: section-level merge
built: 2026-08-31
---

# C7_Pancreatobiliary_Disease — placement record

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Acute Pancreatitis — Diagnosis and Severity | `03_Gastrointestinal` §0.11.1 | under **§0.11 Acute Pancreatitis** |
| 0.2 | Acute Pancreatitis — Management and Complications | `03_Gastrointestinal` §0.11.2 | superseded the §0.1+§0.2 fragment |
| 0.3 | Chronic Pancreatitis | `03_Gastrointestinal` §0.12.1 | superseded the §0.3 fragment, under §0.12 |
| 0.4 | Pancreatic Pseudocyst and Fluid Collections | `03_Gastrointestinal` §0.11.3 | a complication of acute pancreatitis; the reader arrives from there |
| 0.5 | Intra-abdominal Abscess | `03_Gastrointestinal` §0.11.4 | as above — it follows pancreatitis and perforation in this file |
| 0.6 | Pancreatic Malignancy | `03_Gastrointestinal` §0.14.1 | under **§0.14 Pancreatic Cancer** |

## An ordering finding

§0.2's supersede **legitimately removed a clinical figure** — the Atlanta **48-hour**
severity thresholds — because the fragment carried them and B's §0.2 does not.

They are not lost: **B's §0.1 carries them and more** (necrosis visible at 48–72 hours, CRP
at 48 hours), so the sections were merged **§0.1 first**, and the figure exists before the
supersede removes the fragment's copy. Verified after the run: 5 mentions survive.

**This is the first case where the per-section digit report showed a removal that was
correct.** It is not a false alarm and it is not a loss — it is a supersede whose replacement
lives in a sibling section, and the only thing that makes it safe is merge order.

## Cross-references retargeted

`[[F0-3_Shock…]]` → §0.4 Ascending Cholangitis · `[[A1_Emergency…]]` →
`[[08_09_Infectious_Disease_-_Miscellaneous]]` Sepsis · `[[C3_Jaundice…]]` → §0.41.22
Conjugated and Obstructive Jaundice. All verified.

**Left as TODO:** GER3 preventive and occupational. Unbuilt.

## Connective tissue inherited

- §0.2 → the enzyme-height ownership statement pointing at
  `[[NEW_Investigations_Gastroenterology]]`, the Glasgow score at §0.11, and the §0.1
  diagnosis-and-severity pointer.
- §0.3 → diabetes owned by `[[06_Metabolic_Medicine_and_Endocrinology]]`, and the isolated
  gastric varices of sinistral portal hypertension at §0.6.7.

## Report

```
sections merged      6
destinations         03_Gastrointestinal × 6
new-file proposals   0
conflicts raised     0
cross-refs           3 retargeted, 1 left as TODO
digit multiset       5 sections no removal; §0.2 removed the Atlanta 48h figure,
                     correctly — B §0.1 supplies it, and merge order guarantees it
```
