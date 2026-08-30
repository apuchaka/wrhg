---
name: run-state
description: Cross-session memory for the corpus merge. Session context does not carry over — this file and the Queue markers in MASTER_VERIFICATION_WORKFLOW.md are the only memory.
---

# RUN_STATE

## Step 26 — Provenance and population labelling · 🔶 PART 1 OF 2

**Session 1: 2026-08-30, branch `claude/next-6gvrdi`.**

### What is DONE and trustworthy

`trust:` is set on **241 files** and is correct — it is a per-corpus constant, not a
judgement:

| Corpus | Files labelled | `trust:` |
|---|---|---|
| A (`Corpus A/`) | 148 | `inherited` |
| B (`Corpus B/`) | 39 | `unverified` |
| C (`Corpus C/`) | 53 | `snippet` |
| `Medications_Reference.md` (vault root) | 1 | `snippet` |

**B is 39, not the 37 the spec states.** The extra two are `00_BUILD_QUEUE.md` and
`00_BUILD_QUEUE_v2.md` — B's own build queues, not clinical content. They are labelled
so `lint` passes, but **do not count them toward B's 37** in any downstream tally.

**`Medications_Reference.md` sits at vault root, in no corpus directory**, so no `init`
run reaches it. Labelled `snippet` by hand: its own header records that it was built from
cross-verified search snippets on three-source agreement, which is C's provenance
definition, not A's. It states **zero dose figures** (checked with the tool's own
`RE_DOSE`: no hits), consistent with CLAUDE.md §1.11.

### What is NOT done — read this before trusting any `population:` value

**Every `population:` value in the vault is the script's placeholder `mixed`. None of them
is a classification.** `merge_tools.py init` writes `mixed` unconditionally and prints
"Population is set to a placeholder. Correct it per file — do not trust the default."
Nothing has corrected it yet.

**No `figures:` key has been set on any file.**

**No `conflicts_open` / `conflicts_r1` counters have been written** — `scan` has not been
run.

### Why population stalled — the method limitation (CLAUDE.md rule 7)

41 files return **zero** hits from `RE_PAED_SIGNAL`. Rule 2 forbids reading that as proof
of absence, so a wider cross-check detector was written. It reported paediatric content in
28 of the 41.

**That result was withdrawn, not acted on.** Attributing each hit to the alternative that
fired it showed **37 of ~65 sampled hit lines fired on `\bALL\b` matched case-insensitively
— the English word "all"**, in lines like "covers all the reversible causes". The
cross-check reproduced exactly the `Child-Pugh` defect `RE_PAED_EXCLUDE` already exists to
catch.

The residue after removing that artifact is small but non-empty: `congenital` (10),
`breastfeed` (5), `prematur` (4), `centile` (2), and single hits on `birth`, `rubella`,
`BCG`. **`RE_PAED_SIGNAL` has no case for any of those terms**, so a false-negative problem
in the shipped detector probably exists. Its size is unknown. The attribution above is over
the *displayed* hits only — the report caps at 40 lines per file — so it is a sample, not a
census.

### What session 2 must do

1. **Rebuild the paediatric cross-check detector.** Fix the `\bALL\b` case (it must not
   match under `re.I`). Then **validate it against files whose answer is already known**
   before using it on anything: the 40 `Corpus A/15_*_Paeds_*` files must score high;
   `14_05d_Psych_-_Electroconvulsive_Therapy.md` and `13_06c_ENT_-_Bell_s_Palsy.md` must
   score zero. A detector that fails that calibration is not evidence.
2. **Decide the classification policy explicitly and record it here.** The asymmetry that
   matters: labelling a file `adult` when it carries paediatric content is the dangerous
   error, because a reader then trusts an absolute figure as adult-scoped. `mixed` is the
   safe direction. `adult` should require a clean widened scan **and** a read of the file's
   headings, not a clean scan alone.
3. **`paed` candidates** (not yet verified): the 40 `Corpus A/15_*_Paeds_*` files and
   `11_10_Ortho_-_Paediatric_Orthopaedics.md`. Note that `merge_tools.py paed` skips any
   path containing "paed", so its sweep never examines these — they need a separate check.
4. `figures: none` — needs an operational definition first. CLAUDE.md says "where the file
   states no numbers", which is broader than `RE_DOSE` (doses only) and broader than what
   `lint` enforces. Do not set the key from `RE_DOSE` alone; a file carrying a threshold or
   a reference range but no dose would pass and be wrongly flagged figure-free, and §1.14
   then forbids ever adding a figure to it.
5. Run `scan` to write the counters and the `_meta/` artefacts.

### Paediatric-signal audit, session 1 (recorded by what was examined, per Step 17)

Examined: all 240 corpus `.md` files, every line, against `RE_PAED_SIGNAL`.

- **raw signal lines: 1570**
- **survived `RE_PAED_EXCLUDE`: 1557**
- **dismissed by the exclusion: 13** — 12 × `Child-Pugh`
  (`03_Gastrointestinal` ×7, `C3_Jaundice` ×2, `C4_Gastrointestinal_Bleeding`,
  `NEW_Investigations_General_and_Preventive`, `NEW_Investigations_Haematology_Part2`),
  1 × `childhood cancer survivor` (`09_03a_Dermatology`).

**"Survived the exclusion" is not "verified".** Rule 3 requires each hit be checked against
file content by hand; those 1557 lines have not been read. No `adult` or `paed` label rests
on them, and none should until they are.

## Tooling change made this session

`merge_tools.py` gained `SKIP_FILES` — vault-root infrastructure documents are no longer
walked as content. `CLAUDE.md`, `MERGE_SPEC.md` and `MASTER_VERIFICATION_WORKFLOW.md`
document the marker conventions and therefore contain worked examples of every pattern the
scans match; walked as content they injected **9 phantom `UNVERIFIED` items and 4 phantom
`CONFLICT` blocks** into the generated queues.

**Known weakness in that fix:** it matches **by basename anywhere in the tree**, not
anchored to the vault root. A clinical file named `START_HERE.md` inside a corpus directory
would disappear from every scan with no error. Verified this session that no such file
exists — all five matching files are at vault root, none inside a corpus. A path-anchored
skip would be strictly safer and was not implemented.
