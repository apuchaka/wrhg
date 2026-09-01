---
name: Can the 137 merged blocks be removed cleanly?
description: Measured assessment, not an estimate. Dry-run removal performed on a scratch copy; nothing in the repository was changed.
built: 2026-08-31
status: ASSESSMENT ONLY — no blocks removed
---

# Reverting the merged blocks — the plain answer

**It is not a clean git revert. It IS a clean scripted removal, mechanically — and it is
entangled at exactly three points, all of them enumerable and two of them fixable by hand
first.**

## Why not a git revert

**393 commits from base-A (`0db4034`) to HEAD**, and the merge work is interleaved throughout
with the work you want to keep. Step 11's renames, the Step 26/28 infrastructure, the ASCIA
band-table correction and the frontmatter pass all sit *between* merge commits, not before
them. There is no contiguous range to revert.

## The scripted removal, dry-run on a scratch copy

137 blocks removed from 48 files:

```
2136 lines removed
 105 headings removed
   4 orphaned '>' continuation lines   ← the entire structural damage
```

**Four broken lines across the whole corpus.** The blocks are delimited well enough that
removal is a solved problem.

## What SURVIVES — measured, live tree vs dry tree

| Kept item | live | after removal |
|---|---:|---:|
| `trust:` frontmatter | 201 files | **201** |
| `population:` frontmatter | 201 files | **201** |
| Step 11 renames (`furosemide`) | 14 | 13 *(one mention was inside a block)* |
| **ASCIA band table + its VERIFIED box** | intact | **intact** — table, `→MED:adrenaline` mirror and the `[!check]` box all survive |
| Corpus C link conversions and refiling | — | **untouched** (whole-file operations) |
| `KNOWN_ABSENCES.md` | — | **untouched** (separate file) |
| `STUDY_CHECKS.md` | — | **derived** — regenerates from whatever markers remain |
| Step 17 UK-localisation sweep | — | **untouched** (word-level edits throughout) |

The three lost ASCIA mentions are `UNVERIFIED` markers *inside* blocks naming ASCIA as the
source to check. They die with their blocks, which is correct.

## What is LOST — the three entanglement points

### 1. All 74 NO-BASELINE markers — but this is not really a loss

`NO-BASELINE` goes from **74 to 0**, because every one of them lives inside a merged block.
That is what the marker *is*: an assertion that a **particular block** has nothing in the
inherited layer disagreeing with it. **Remove the block and the assertion is moot, not
destroyed.** The audit record of what they said is in `_meta/audits/` and `STUDY_CHECKS.md`.

### 2. Conflicts — TWO LOST ENTIRELY, ONE ORPHANED. This is the real loss.

| ID | Topic | Fate |
|---|---|---|
| **CF-032** | appendicitis imaging pathway | **LOST — both sides sit inside a merged block** (`03_Gastrointestinal:880` and `:885`) |
| **CF-039** | Barrett surveillance interval | **LOST — both markers inside the Barrett block**, raised an hour ago |
| **CF-038** | rebound tenderness | **ORPHANED** — the B side is inside the C1 block (`03_GI:1671`); the A-side marker survives at `NEW_Gastroenterology_and_Hepatology:36` pointing at nothing |
| CF-033, CF-034, CF-035, CF-036, CF-001 | | survive intact |

**Fixable, and it must happen before removal, by hand.** CLAUDE.md §1.12 forbids an agent
writing or editing conflict blocks beyond raising them; lifting these three out into
standalone `[!fail]` blocks that do not depend on B's text is a person's job. It is three
items.

### 3. ~2136 lines of merged content, including the blocks that were placed WELL

This is the judgement call, and it is yours. The audits so far say the merges are mostly
sound:

- **C2, C3 and C4 tested completely clean against base-A.**
- Two blocks are **worked examples of correct placement** and would have to be recreated:
  `01_Cardiovascular:48` (RV infarction — quotes `NEW_Drugs_06` and says *"what that entry
  does not give is how you know"*), and `03_Gastrointestinal` §0.33.4 (*"AIMS65 … alongside
  the Glasgow-Blatchford and Rockall scores already at §0.33.2"*).
- Confirmed bad placements so far: **two** — C6's Barrett block and C1's §0.2 block.

**So the removal discards roughly 2136 lines to fix two known duplicates.**

## The recommendation, plainly

**The removal is clean enough to do, and I do not think it is worth doing on the current
evidence.**

Reverting is the right call when the old rule produced systematically bad placement. Five
files audited claim-by-claim say it did not: three were clean, one was the model to copy, and
the two failures have a **specific, known and already-fixed cause** — the gap check searched
Corpus A alone, so the duplicates were in Corpus C. That cause is closed by rule 12 and by
the plain-name clause in rule 2.

**If you disagree and want the clean base anyway**, the sequence is:
1. **You** lift CF-032, CF-038 and CF-039 into standalone conflict blocks that do not depend
   on B's text.
2. Script the removal (2136 lines, 4 lines to repair by hand afterwards).
3. Regenerate `STUDY_CHECKS.md`.
4. Re-merge under the section rule, accepting that the two well-placed blocks above must be
   rewritten.

**What you lose either way:** keeping them means reconciling 137 blocks against the new rule,
two of which are known duplicates. Removing them means re-doing 2136 lines of placement that
the audit says was mostly right, and rebuilding three conflicts by hand first.
