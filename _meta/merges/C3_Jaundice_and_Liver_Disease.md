---
name: C3 placement record
description: Where each section of C3_Jaundice_and_Liver_Disease was placed under the section-level merge rule, and why.
bfile: Corpus B/C3_Jaundice_and_Liver_Disease.md
rule: section-level merge
built: 2026-08-31
---

# C3_Jaundice_and_Liver_Disease — placement record

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Jaundice — Mechanism and Classification | `03_Gastrointestinal` §0.41.8 | §0.41 presentation section; superseded the §0.1 fragment |
| 0.2 | Unconjugated Hyperbilirubinaemia | `03_Gastrointestinal` §0.41.21 | a presentation, reached from the jaundiced patient |
| 0.3 | Conjugated and Obstructive Jaundice | `03_Gastrointestinal` §0.41.22 | as above |
| 0.4 | Acute Liver Failure | `03_Gastrointestinal` §0.38.2 | placed under **§0.38 Cirrhosis**, not §0.41 — the reader arrives at liver failure from liver disease, and the destination's liver entries are there |
| 0.5 | Chronic Liver Disease and Cirrhosis | `03_Gastrointestinal` §0.38.3 | as above |
| 0.6 | Complications of Cirrhosis | `03_Gastrointestinal` §0.38.1 | superseded the §0.6 fragment, already under Cirrhosis |
| 0.7 | Hepatomegaly, Splenomegaly, Hepatic Pain | `03_Gastrointestinal` §0.41.23 | an examination finding the reader arrives at from the abdomen |

## Cross-references retargeted

| B link | Retargeted to | Verified |
|---|---|---|
| `[[F0-1_Toxidromes…]] 0.6` paracetamol | `[[14a-2_Psych_-_Overdose…]]` §0.1 Overdose / poisoning — management by agent | exists — **corrected**: my first attempt wrote a "Paracetamol" header that does not exist in that file |
| `[[F0-3_Shock…]] 0.11` | §0.4 Ascending Cholangitis | exists |
| `[[A5_Toxicology_II…]] 0.1` | `[[14a-2_Psych_-_Overdose…]]` | exists |
| `[[A9_Transfusion…]] 0.3` | `[[10_08_Haemonc…]]` Warfarin — management of high INR | exists |
| `[[A4_Dyspnoea…]] 0.2` | §0.38.1 the pulmonary complications of cirrhosis | exists |
| `[[C1_Acute_Abdomen]] 0.5` | §0.41.12 Left Upper Quadrant Pain — **the C1 section merged earlier today** | exists |

**Left as TODO:** J2 haemoglobinopathy and haemolysis · M3 neonatal problems · N1 risk
assessment and suicidality. All unbuilt.

## Connective tissue inherited

§0.1's fragment carried four pointers, **all four initially lost and recovered**: the LFT
panel owned by `[[NEW_Investigations_Gastroenterology]]` §0.1, bilirubinuria owned by
`[[NEW_Investigations_Renal_and_Urology]]`, and the section pointers on the three-way
classification — Hepatitis (§0.9), cirrhosis (§0.38), posthepatic (§0.3, §0.4, §0.5, §0.14).

The two ownership statements are **reworded** from *"not restated here"* to an owner
reference. Under the section rule B's section does now restate that material, so the pointer
still matters but the claim about non-repetition does not.

## Report

```
sections merged      7
destinations         03_Gastrointestinal × 7 (§0.41 × 5, §0.38 × 3 incl. one supersede)
new-file proposals   0
conflicts raised     0
cross-refs           6 retargeted, 3 left as TODO
digit multiset       pass — no digits removed on any of the 7 sections
```

**No conflict raised.** The placement figure comparison found no numeric disagreement.
C3's figures are largely withheld behind `UNVERIFIED` markers (King's College criteria,
Child-Pugh, MELD, SAAG cut-off, SBP neutrophil threshold), so there is nothing to compare
against the destination's numbers.
