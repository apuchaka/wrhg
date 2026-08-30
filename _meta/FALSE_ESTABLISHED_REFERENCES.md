---
name: false-established references
description: A recurring failure class — a reference that reads as established because it is repeated, cross-referenced or discussed in prose, while nothing on disk backs it.
---

# References that read as established and are not

## The class

**A claim acquires the appearance of verification from repetition, cross-reference or
confident prose — never from a source.** Every instance below looked settled at the point
of use. None was.

The reason it recurs is structural: this project's documents cite each other. A number,
an ID or a filename that appears in three documents *looks* corroborated, and CLAUDE.md
already warns that **two corpora agreeing is not corroboration**. This is the same
failure one level up — **two documents agreeing is not corroboration either**, when both
are downstream of the same unchecked original.

## Instances

| # | Instance | How it acquired authority | How it was caught | Whose |
|---|---|---|---|---|
| 1 | **The inherited `0.7`** | A reference value copied forward from commit `39be13e`; being inherited made it feel sourced | Traced to origin; no source was ever attached | corpus |
| 2 | **`A5` in prose with no queue row** | Discussed as a build target in prose, so it read as queued | Coverage check re-run against the queue itself, not against the prose | corpus |
| 3 | **`F0.4` in no v2 queue reference** | `F0-4_Resuscitation_Algorithms` exists on disk and every sibling is referenced, so its absence read as an oversight rather than a fact | Enumerated from disk instead of from the index | corpus |
| 4 | **`GER1`/`GER2` as a rename of `P2`** | Stated as history, twice, in opposite directions | Measured against the filesystem | corpus |
| 5 | **`CONFLICT CF-012`** | Appeared in **three** documents (`MERGE_SPEC.md`, `CLAUDE.md`, `MASTER_VERIFICATION_WORKFLOW.md`) as a formatting example **using real appendicitis wording**, then `MERGE_SPEC.md` L524 discussed it in prose as a live conflict that had "surfaced a probable error in the `inherited` layer" | Whole-vault grep before writing the cross-reference the merge instruction called for — rule 1 | **the human's**, propagated for days |

## What instance 5 adds that the others did not

The first four were defects in the corpus or its index. **`CF-012` was a defect in the
project's own governing documents**, and it was believed by the person who wrote them.

Two specifics made it durable:

1. **The example used real content.** `MERGE_SPEC.md`'s R2 template was not
   `<claim>`/`<claim>` — it was the actual appendicitis ultrasound wording. An example
   indistinguishable from a real entry will eventually be read as one.
2. **Prose then referred back to the example as evidence.** L524 cited CF-012 as proof
   that overlap between corpora surfaces real errors. The argument is sound; the example
   supporting it did not exist.

**The correction, 2026-08-31:** the disagreement is real and is now **`CF-032`** in
`03_Gastrointestinal` §0.18.1, R2, in the conflict index. `CF-012` has been annotated as
an example ID in all three documents, and L524 rewritten.

## The check this class implies

Before writing any cross-reference — to a section, a file, a conflict ID, a queue row or
a figure — **confirm it against the filesystem or the file's actual text, not against
another document that mentions it.** Rule 1 already says this for section headers. The
same applies to every identifier this project uses.

Corollary, from instance 5: **when writing an example, make it obviously an example.**
Placeholder claims, or an explicit "EXAMPLE ID" annotation. An illustration built from
real content is a future false reference.
