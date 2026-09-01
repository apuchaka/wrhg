---
name: C6 placement record
description: Where each section of C6 was placed under the section-level merge rule. This is the file whose audit motivated the rule change.
bfile: Corpus B/C6_Dyspepsia__Oesophageal_and_Anorectal_Disease.md
rule: section-level merge
built: 2026-08-31
---

# C6 — placement record

**This is the calibration file.** Under the topic rule it produced 4 discards; the
claim-level re-audit found 49 ABSENT and 26 WEAKER against the 14 the row rule named. Under
the section rule all six sections merge whole.

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Dyspepsia, Reflux and Heartburn | `03_Gastrointestinal` §0.28.1 | under **§0.28 GORD** — and B's heading is kept, which is the entire point: the retrieval failure was searching "dyspepsia" and getting nothing while the content sat under "0.28 GORD" |
| 0.2 | Peptic Ulcer Disease and *H. pylori* | `03_Gastrointestinal` §0.27.1 | under **§0.27 Peptic Ulcer Disease** |
| 0.3 | Oesophageal Disease | `13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology` §0.3.1 | superseded the Barrett fragment; **CF-039 carried onto the new heading** |
| 0.4 | Anorectal Pain | `03_Gastrointestinal` §0.25.1 | superseded the anorectal fragment, under §0.25 Haemorrhoids |
| 0.5 | Anal Lump | `03_Gastrointestinal` §0.25.4 | with the anorectal material |
| 0.6 | Pruritus Ani | `03_Gastrointestinal` §0.25.5 | as above |

## The two failures that motivated the rule are closed

**Achalasia.** Previously two hits in `13_06b`, both one word in a list. Now:
`13_06b:75` `> [!tip] Achalasia` with the definition and the myenteric-plexus mechanism ·
`:77` **the discriminating feature is dysphagia to solids AND liquids from the outset** ·
`:79` **pseudoachalasia** · plus pneumatic dilatation, POEM and Heller myotomy.

**Dyspepsia.** §0.28.1 now carries B's section whole — the inferior-MI cardiac exclusion with
the point that antacid or GTN relief does not distinguish them, transient LOS relaxations,
the drug-cause list with the bisphosphonate instruction, functional dyspepsia as a positive
diagnosis, coeliac serology, and the fuller red-flag list. §0.28 GORD is untouched beside it.

## Cross-references retargeted

`[[B1_Chest_Pain…]]` → `[[01_Cardiovascular]]` ACS · `[[A4_Dyspnoea…]]` → `[[02_Respiratory]]` ·
`[[GER1…]]` → `[[18_Geriatrics…]]` Polypharmacy and Deprescribing · `[[C1…]] 0.4` → §0.41.11
Epigastric Pain · `[[C4…]] 0.4` → §0.34.1 · `[[C2…]] 0.7` → §0.41.20. All verified.

**Left as TODO:** I5 weight and lipids · F3 throat and voice · K2 skin and soft tissue ·
O6 sexual and reproductive health.

## Connective tissue inherited

- §0.3 → **`CF-039`**, the Barrett surveillance-interval conflict. Its `[!fail]` block sits
  above the fragment and survived; the **inline marker on the heading** would have been lost
  and the driver refused the merge until it was carried.
- §0.4 → §0.16.1 Crohn on the atypical fissure, §0.23 for the ischaemic mechanism, §0.24 for
  the fistula, §0.25 for the haemorrhoids themselves.

## A tool defect found here

The annotation refusal compared **whole lines**, so an inline `CF-` marker attached to a
heading could never survive — the new block necessarily rewrites that heading. Inline markers
are now compared as **tokens**; callout blocks are still compared as whole lines. Both
directions re-tested.

## Report

```
sections merged      6
destinations         03_Gastrointestinal × 5, 13_06b_ENT × 1
new-file proposals   0
conflicts raised     0  (CF-039 already raised; carried, not re-raised)
cross-refs           6 retargeted, 4 left as TODO
digit multiset       pass — no digits removed on any of the 6 sections
```
