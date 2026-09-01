---
name: ger1-ger2-placement
description: Section-level placement record for GER1 and GER2. Every section, its destination, its disposition — including the discarded one.
built: 2026-09-01
---

# GER1 and GER2 — section placement record

Read from the tree, not from the run order. Every row was confirmed by locating the
`SRC:` token and reading the heading it sits under.

## GER1_Comprehensive_Geriatric_Assessment

| § | Title | Destination | Disposition | Commit |
|---|---|---|---|---|
| 0.1 | Comprehensive Geriatric Assessment | `18_Geriatrics…:305` | additive | `eed249d` |
| 0.2 | Frailty | `18_Geriatrics…:353` | additive | `64c21a2` |
| 0.3 | Functional Assessment and the Australian Aged Care System | `18_Geriatrics…:659` | **supersedes** the two-funding-pathways fragment | `12bf172` |
| 0.4 | Polypharmacy and Deprescribing | `18_Geriatrics…:493` | additive | `a1c3fa2` |
| 0.5 | Falls | `18_Geriatrics…:107` | additive | `e6bca03` |
| 0.6 | Osteoporosis and Fracture Prevention | `18_Geriatrics…:149` | additive | `9218fac` |

**GER1 ran before `carry_markers` existed.** Re-audited from the diffs: five of its six
commits **removed zero lines** — pure additive, nothing to inherit. Only §0.3 removed
anything (7 lines), and its single marker
`` `UNVERIFIED — current eligibility criteria and the age boundary between NDIS and aged care…` ``
is present in the tree now. **No GER1 section needed a carry and did not get one.**

## GER2_Geriatric_Syndromes_and_End_of_Life_Care

| § | Title | Destination | Disposition | Commit |
|---|---|---|---|---|
| 0.1 | Continence | `07_Renal_Medicine_and_Urology:794` | **supersedes** the DIAPPERS fragment | `02a23b7` |
| 0.2 | Pressure Injury | `18_Geriatrics…:196` | additive — the combined fragment is superseded on §0.4, not here | `be611cf` |
| 0.3 | Malnutrition and Nutrition | `18_Geriatrics…:389` | additive | `ba58102` |
| 0.4 | Immobility, Deconditioning and Hospital-Associated Decline | `18_Geriatrics…:707` | **supersedes** the combined `§0.2`+`§0.4` fragment | `0ef2248` |
| 0.5 | End-of-Life Care and Recognising Dying | `10_11c_Oncology…:61` | **supersedes** the recognising-dying fragment | `6d19957` |
| 0.6 | Advance Care Planning in Practice | `Communication:162` (`### 1.4.1`) | **DISCARDED to verified content; 5 of 13 claims merged as a delta** | `9328d0a` |

### §0.1 and the end-of-file crash

§0.1's fragment was the **last block in `07_Renal_Medicine_and_Urology`**, and the driver's
end-boundary `next()` had no default, so it raised `StopIteration` and died mid-run. Fixed in
`4a7af4b`. **`4a7af4b` precedes `02a23b7` in the history** — the section was retried after
the fix and landed; it was not skipped. Confirmed by `git log --reverse`.

### §0.6 and what check 1 counts

§0.6 carries a normal `SRC:GER2_… §0.6` token under a `— from unverified layer` heading, so
**check 1 counts it as placed and that is correct** — something from §0.6 did land. But the
shape is not a section merge:

- `Communication.md` §1.4 is **`verified`** against ACSQHC goals-of-care guidance and Advance
  Care Planning Australia. §1.10: verified beats unverified, so the section is discarded.
- Rule 12: a discard is made at CLAIM level. Thirteen claims were extracted and tested.
  **Eight were covered** (§1.4 ×5, §1.3 ×1, `Clinical-Process` ×2) and **five were not**.
  Only the five are in the block, in the §1.10 delta shape.

**The token therefore proves less than it does on a whole-section merge**, and check 1 cannot
see the difference. Two things follow, and they are the standing instruction for this shape:

1. **A `discard-plus-delta` block must say so in its own first line**, as this one does —
   the italic note names the verified destination, the rule, and the 8/13 split. A future
   check-1 run that finds a token should read that line before reporting the section
   reproduced.
2. **Check 1 should report three states, not two**: `SECTION` (token under a
   `— from unverified layer` heading whose block reproduces the section), `DELTA` (same, but
   the block states it carries only part), and `ABSENT`. The distinguishing text is
   machine-readable today only as prose. **If a later wave produces more than a handful of
   these, give them a token of their own** — the `SRC:` line is the right place, and a
   `` `PARTIAL — n of m claims; rest superseded by <file> §<sec>` `` token would make the
   state countable instead of readable. One instance does not justify the token; a pattern
   would.

### What each supersede inherited

| § | removed | markers in the removed lines | outcome |
|---|--:|--:|---|
| 0.1 | 4 lines | 0 | nothing to inherit |
| 0.4 | 4 lines | 2 + `[[04_Neurology]]` | both markers and the pointer carried; the Waterlow/Braden one was relocated onto §0.2's block first (`2789be9`) and verified by `carry_markers` against the destination EXCLUDING the fragment |
| 0.5 | 11 lines | 0 in the removed set | the four markers survive as **diff context**, i.e. they were reproduced verbatim by the block rather than deleted and rewritten. Confirmed separately at commit time by byte-comparing every marker in the pre-merge blob against the result: 4/4 PRESENT |

### A defect in the verification itself, found here

The first run of this audit reported `[[04_Neurology]]` **LOST** on §0.4. It was not lost — it
is in the retargeted line. The audit extracted destination filenames with
`re.findall(r'^\+\+\+ b/(.+)$')`, which **captures git's trailing tab**, so `git show
<rev>:<file>` returned an empty blob and every cross-reference read as absent.

**A false MISSING in a verification, which is the direction §1.3 rule 11 names as the more
dangerous one** — it says content was destroyed and invites a "restore" that duplicates
content already present. It was caught only because the rewritten check asserts the blob is
non-empty before testing anything against it. **Any check that reads a blob must assert it
got one.**
