---
name: misplacement-queue
description: Blocks whose topic is broader than, or unrelated to, the heading they sit under. Recorded for the post-merge re-parenting job. NOT to be moved piecemeal.
built: 2026-09-01
---

# Misplacement queue — blocks under the wrong parent

**Do not move these one at a time.** Re-parenting is a move, and moves belong together
with the other moves in the post-merge job — a block relocated in isolation breaks any
`§n.n` pointer aimed at it and renumbers its siblings.

Found by the fourteen-file gate check (check 5). Every entry is a `###` block sitting
under a `##` that is **narrower than it**, or unrelated. None is a merge defect in the
sense of losing content; all are reachability defects — a reader browsing by heading will
not find them.

**`mine`** = a placement this run chose. **`base-A`** = the destination's own structure,
inherited, where the block went to the only sensible neighbour and the parent heading was
already a poor fit.

## `03_Gastrointestinal.md`

| Block | sits under | whose | why it is wrong |
|---|---|---|---|
| `0.25.1 Anorectal Pain` | `## 0.25 Haemorrhoids` | **mine** | four anorectal *presentations* under one *condition* |
| `0.25.3 Tenesmus and Rectal Symptoms` | `## 0.25 Haemorrhoids` | **mine** | as above |
| `0.25.4 Anal Lump` | `## 0.25 Haemorrhoids` | **mine** | as above |
| `0.25.5 Pruritus Ani` | `## 0.25 Haemorrhoids` | **mine** | as above |
| `0.38.2 Acute Liver Failure` | `## 0.38 Cirrhosis` | **mine** | **ALF is not a complication of cirrhosis** — it is a distinct entity, often in a previously normal liver |
| `0.39.1 Bowel Obstruction` | `## 0.39 Ileus` | **mine** | **inverted** — ileus is the functional subtype of the thing the block covers |
| `0.42.1 Constipation` | `## 0.42 Faecal Incontinence (Adult)` | **mine** | constipation is a cause of overflow incontinence, not a subtopic of it |

**Suggested parent for the four anorectal blocks:** a new `## Anorectal Presentations`
section, with `0.25 Haemorrhoids` as one entry under it. That is a structural change, not
a move, and needs a decision.

## `13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology.md`

| Block | sits under | whose | why it is wrong |
|---|---|---|---|
| `0.3.1 Oesophageal Disease` | `## 0.3 Barrett's oesophagus` | **mine** | the block covers **oesophageal cancer, eosinophilic oesophagitis, achalasia, peptic stricture, spasm, pill and infective oesophagitis and varices**. Barrett's is one paragraph of it. **This is the widest gap in the queue.** |

## `11_06_Ortho_-_Spinal_Orthopaedics.md`

| Block | sits under | whose | why it is wrong |
|---|---|---|---|
| `Radiculopathy` | `## Scoliosis` | **mine** | placed where the superseded fragment stood; the fragment was itself an `##`, so the block was demoted to `###` and inherited Scoliosis as a parent |

## `04_Neurology.md`

| Block | sits under | whose | why it is wrong |
|---|---|---|---|
| `Reduced Consciousness` | `## CNS Infections Associated with Immunosuppression` | **base-A** | the block belongs beside `### Glasgow Coma Scale (GCS)`, which is where it went — but GCS itself lives under that H2 in base-A |
| `Amnesia and Memory Impairment` | `## CNS Infections Associated with Immunosuppression` | **base-A** | same |
| `Tremor` | `## Other Neurology Topics` | **base-A** | placed after `### Abnormal Involuntary Movements`, which is in that H2 — while `## Movement Disorders` exists earlier in the file |
| `Chorea, Dystonia, Tics and Myoclonus` | `## Other Neurology Topics` | **base-A** | same |
| `Mononeuropathies and Entrapment` | `## Other Neurology Topics` | **base-A** | placed after `### Charcot-Marie-Tooth Disease`, which is in that H2 |

**The four base-A cases are a different job from the seven mine.** Moving a block out of
`## Other Neurology Topics` means first moving `### Abnormal Involuntary Movements` and
`### Charcot-Marie-Tooth Disease`, which are base-A content. That is a restructure of
`04_Neurology`, and it is not this queue's to authorise.

## Count

| | n |
|---|--:|
| **mine** | 8 |
| **base-A** | 4 |
| **total** | **12** |

## What was NOT put in this queue, and why

`0.18.1` (C1 §0.6's appendicitis fragment left in place under `## 0.18 Appendicitis`),
the `15_08` and `14_05a` fragments — those are **deliberate duplications**, recorded in
their own block notes and in the placement records, not misplacements.
