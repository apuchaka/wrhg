---
name: 28b/28c merge conflict — resolution of record
description: The one non-mechanical conflict between the Step 28 branches. Written before merge, in the repo, so the decision is not held only in a PR comment.
---

# 28b × 28c — `Corpus C/NEW_Investigations_Gastroenterology.md`

## The overlap

`phase/28b-corpus-c-refile` replaced sections **0.32 CSF Studies**, **0.33 Coombs / DAT**
and **0.34 G-CSF** with pointer stubs: 0.32 and 0.35 were refiled to their correct system
files, and 0.33 and 0.34 were found to be **duplicates that already existed at the
destination**, so they were stubbed rather than moved.

`phase/28c-wikilinks` branched from `claude/next-6gvrdi` **before 28b existed**, so it
still saw the full original sections — and converted backticked references to wikilinks
*inside them*.

Both branches therefore edit the same region for unrelated reasons. Git cannot tell that
one side deleted the text the other side was editing.

## Resolution — 28b's side, in sections 0.32–0.34 only

| Region | Take | Why |
|---|---|---|
| §0.32, §0.33, §0.34 | **28b's stubs.** Drop 28c's changes here. | 28c's edits in this region are wikilink conversions **of text 28b deleted as duplicated content**. Keeping them resurrects the duplicates 28b removed. |
| Everything else in the file | **28c's conversions apply.** | No overlap with 28b. |
| Every other file in 28c | **applies unchanged.** | 28b touched only this file plus the two refile destinations, which 28c does not conflict with. |

## What taking both sides produces — observed, not hypothetical

During the 2026-08-30 integration check this conflict was resolved by `git add -A` after
fixing a *different* conflicted file, without re-reading `git status`. The result was
committed: **three literal conflict markers in clinical content**, and sections 0.32–0.34
present **twice** — once as 28b's stubs, once as the full original sections 28b had
deliberately removed.

The file still rendered. It still opened in Obsidian. The corrupted region read as two
competing versions of the same guidance with nothing indicating which was current.

**That commit was local-only and was discarded. No pushed branch carried it.** The guard
that would have caught it is now `python3 scripts/merge_tools.py precommit --dir .`,
required before every commit (§1.1.9.1).

## Merge order

`#7` → `#3` → `#4` → `#5` → `#6`. `phase/28c-wikilinks` has been **rebased onto
`phase/28b-corpus-c-refile`** with this resolution applied on the branch, so `#6` merges
clean and no markdown conflict is resolved in the GitHub UI.
