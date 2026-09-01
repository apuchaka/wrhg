---
name: Section merge — 14-file gate report
description: State of the section-level merge at the agreed stop, with the verification actually run.
built: 2026-09-01
---

# Section merge — the 14-file gate

**C1–C7 and D1–D7. 93 sections, 93 commits, one per section.** Stopped here for review, as
agreed.

## What is merged

| B file | § | Destinations |
|---|--:|---|
| C1_Acute_Abdomen | 11 | `03_Gastrointestinal` ×10, `11_09b_Ortho_-_Trauma` ×2 |
| C2_Nausea_and_Vomiting | 7 | `03_Gastrointestinal` ×6, `15_08_Paeds_-_Surgical_Abdomen…`, `NEW_Drugs_12_Gastrointestinal`, `14_05a_Psych_-_Eating_Disorders` |
| C3_Jaundice_and_Liver_Disease | 7 | `03_Gastrointestinal` ×7 |
| C4_Gastrointestinal_Bleeding | 5 | `03_Gastrointestinal` ×5 |
| C5_Bowel_Habit__Obstruction_and_Distension | 6 | `03_Gastrointestinal` ×5, `08_10_Infectious_Disease_-_Diarrhoea…` |
| C6_Dyspepsia__Oesophageal_and_Anorectal_Disease | 6 | `03_Gastrointestinal` ×5, `13_06b_ENT_-_Dysphagia…` |
| C7_Pancreatobiliary_Disease | 6 | `03_Gastrointestinal` ×6 |
| D1_Headache_and_Meningism | 6 | `04_Neurology` ×6 |
| D2_Altered_Consciousness_and_Cognition | 6 | `04_Neurology` ×6 (+ a kept fragment in `Investigation-Interpretation`) |
| D3_Stroke_and_Focal_Neurological_Deficit | 7 | `04_Neurology` ×7 |
| D4_Weakness__Neuropathy_and_Radiculopathy | 7 | `04_Neurology` ×6, `11_06_Ortho_-_Spinal_Orthopaedics` |
| D5_Dizziness__Vertigo_and_Gait | 6 | `04_Neurology` ×6 |
| D6_Seizures_and_Movement_Disorders | 7 | `04_Neurology` ×7 |
| D7_Cranial_Nerves_and_Special_Senses | 6 | `04_Neurology` ×6 |

**25 of the 93 superseded an existing fragment.** 111 `Added from unverified layer` blocks
now stand where base-A had 0.

## Verification actually run at the gate

```
sections in the 14 B files: 93 | SRC token absent from the vault: 0
49 destination files | with NEW duplicate headings vs base-A: 0
destination files with any digit removed since base-A: 0
CF-032 … CF-039 all present (CF-037 unused, as before)
[!fail] blocks: 10 across 9 files      [!check] boxes: 7
lint: 178 unmarked `inherited` dose figures | 0 inside a merged SRC block
```

**Source path, resolved live rather than assumed:** all 93 came from `Corpus B/`, 0 from
`Corpus B-new/` — `_meta/audits/SOURCE_PATH_AUDIT.md`.

## THE HONEST PART — what went wrong, and how each was found

**Nine defects. Not one was found by a check failing.** Every one was found by reading
before merging, or by reading a number the tool printed and did not flag.

| # | Defect | Found by | Fix |
|--:|---|---|---|
| 1 | Subheading rescope had no unnumbered-destination branch — 15 headings collapsed to 3 | reading the duplicate-header count | `e240184` + `38ccadd` |
| 2 | Duplicate-header check counted the whole file, so it could not fail once one existed | chasing 1 | `e240184` |
| 3 | A linkmap rule right for F0-5 §0.6–0.8 and wrong for §0.10 — real file, real heading, wrong section | reading the merged block | `c82b3b8` |
| 4 | `SRC:` token read as a cross-reference | a refusal on D3 §0.6 | `202ac36` |
| 5 | **D2 §0.5's supersede passed the cross-reference check by coincidence** — a note I wrote happened to contain the string `"§0.1 above"` | chasing 4 | `202ac36` + `a14a902` |
| 6 | **`UNVERIFIED` was never in the protected list. Seven had already been destroyed.** | reading D4 §0.3's fragment before merging | `aa6beb2`, restored `0a76b66` `1a7852c` `3050204` |
| 7 | Supersede boundary was the next *heading*, so a callout-shaped block between fragments fell inside the deletion range | reading D4 §0.6's fragment | `3f7df30` |
| 8 | …and that fix's walk-back crossed blank lines: `superseded 2 lines` instead of 16, everything printing `OK` | **reading the superseded-line count** | `e9ae615` |
| 9 | **A supersede deleted destination prose** — `**P (vertigo generally):**` — and my commit message said it survived | the grep printed 0 and I did not read it | restored `4eedf73`, cause fixed `4c26d92` |

**Two of my own commit messages stated figures I had not read** (`6e279a3`'s digit delta,
`fa7aba5`'s survival claim). Both corrected in the record rather than amended away.

**And one guard I wrote could not fail.** `carry_refs` checked the destination *including
the fragment about to be deleted*, so it always found the pointer — in the very text being
removed. The known-answer test caught it; reading the three lines did not.

## Two failure shapes worth carrying into the next block

**A fragment whose `SRC:` line names TWO sections cannot be superseded by the first of
them.** Four instances (D2, D3, D4, D6). The first section merges *without* superseding.
The test is an exact-token grep and cannot fail — count the `§` tokens on the SRC line.

**A presence check passes while a RELATION is destroyed.** D6's fragment paired each current
ILAE term with the obsolete one it replaced. B's §0.1 states both sets and never maps them.
All six terms survived — which is what I checked and reported — and the pairing did not.
Rule 12 names this at claim level for discards; it applies to supersedes, and **no
structural check in the driver can see it.**

## Findings recorded, not fixed

- **`CLAUDE.md` §1.10's "191 unbuilt targets (50 codes)" is stale.** Measured: 47 of 47
  codes and 188 of 188 markers now have a file. 34 already merged into Corpus A/C say
  `(unbuilt)` about topics that exist. Scheduled after the B-new merges (`f974630`,
  `d92d36a`).
- **Aspirin 75 mg** for secondary prevention in `01_Cardiovascular` is the UK strength, and
  the corpus gives **three different answers** for pre-eclampsia prophylaxis across two
  files. Inherited content, untouched by this merge (`fd341d1`).
- **Two cross-reference edits scheduled** — §0.28's `Ix` line has no ECG pointer, and
  `ALARM` appears once in 240 files (`eebb110`).

## What this run does NOT establish

- That the merged sections are clinically correct. They are `unverified` and labelled so.
- That B and its `Corpus B-new/` re-export agree. The source audit says which file was
  opened, not whether the copies match.
- Completeness in any sense beyond rule 8: **clean against everything currently known to
  check for.**
