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

**B is 39 files / 37 clinical.** `Corpus B/00_BUILD_QUEUE.md` and
`Corpus B/00_BUILD_QUEUE_v2.md` are B's own build queues — infrastructure, not clinical
content. They are labelled so `lint` passes. **Every downstream tally should expect 39
files and 37 clinical entries**, and should exclude those two by name rather than
treating the 39 as a discrepancy to investigate again.

**`Medications_Reference.md` sits at vault root, in no corpus directory**, so no `init`
run reaches it. Labelled `snippet` by hand: its own header records that it was built from
cross-verified search snippets on three-source agreement, which is C's provenance
definition, not A's. It states **zero dose figures** (checked with the tool's own
`RE_DOSE`: no hits), consistent with CLAUDE.md §1.11, and carries `figures: none`. That
key was set after reading all 16 of its lines containing a digit: every one is a receptor
subscript (β1, β2, α1), a cross-reference file number, or the phrase "roughly a quarter of
β2 receptors". No dose, no reference range, no threshold.

### What is NOT done — read this before trusting any `population:` value

**Every `population:` value in the vault is the script's placeholder `mixed`. None of them
is a classification.** `merge_tools.py init` writes `mixed` unconditionally and prints
"Population is set to a placeholder. Correct it per file — do not trust the default."
Nothing has corrected it yet.

**No `figures:` key has been set on any file.**

**No `conflicts_open` / `conflicts_r1` counters have been written** — `scan` has not been
run.

### The detector: withdrawn, rebuilt, validated (CLAUDE.md rules 2, 4, 7)

**First attempt, withdrawn.** 41 files returned zero hits from the shipped
`RE_PAED_SIGNAL`. Rule 2 forbids reading that as absence, so a wider cross-check was
written. It reported paediatric content in 28 of the 41 — and was withdrawn on
inspection: **37 of ~65 sampled hits fired on `\bALL\b` matched case-insensitively**,
i.e. the English word "all", in lines like "covers all the reversible causes". That is
the `Child-Pugh` defect reproduced. A guard comment now sits in `merge_tools.py` so
nobody adds a bare `\bALL\b` for acute lymphoblastic leukaemia again.

**Rebuild.** The residue was folded into `RE_PAED_SIGNAL` itself rather than kept as a
second detector. Added: prematurity/preterm/premature birth·baby·infant·neonate, growth
centile compounds, birth weight, Apgar, fontanelle, teething, nappy, weaning, puberty,
juvenile, trisomy, Down syndrome, perinatal, rubella, BCG vaccination, mumps, measles,
varicella, pertussis, whooping cough, Hib, MMR, immunisation/vaccination schedule,
milestone, SIDS, PICU, non-accidental, NAI, Gillick.

**Four terms tried and rejected**, each by reading every line it flagged — `congenital`
(aetiology class in adult files, 5 files flagged, 0 true positives), `breast-?feed`
(maternal scope, 4 flagged, 0 true), `centile` (matches inside "99th percentile", caught
troponin assay statistics), `\bBCG\b` (3 of 17 corpus lines are intravesical BCG for
bladder cancer). **22 of the 24 lines the first widening flagged were false positives** —
that ratio is the evidence the pass was careful, per rule 3. The rejections are recorded
in `merge_tools.py` so they are not re-added.

**Validation, run before any use of the detector:**

| Check | Requirement | Result |
|---|---|---|
| `Corpus A/15_*_Paeds_*`, 40 files | must score high | min 2 · median 9.5 · max 32 · **none scoring 0** |
| `11_10_Ortho_-_Paediatric_Orthopaedics` | must score high | 28 |
| `14_05d_Psych_-_Electroconvulsive_Therapy` | must score 0 | 0 |
| `13_06c_ENT_-_Bell_s_Palsy` | must score 0 | 0 |
| `14_05b_Psych_-_Insomnia` | must score 0 | 0 |

**Known weakness the calibration exposed:** two genuinely paediatric files score only 2 —
`15_18b_Genetic_Disorders_Inheritance_Summary` and `15_20b_Imprinting_Disorders`. The
detector is weak on genetics content. It must not be used as a *threshold* classifier;
those two are labelled `paed` on what the file is, not on a count.

**Net effect of the rebuild:** raw signal lines 1570 → 1872, confirmed 1557 → 1859,
dismissed 13 → 13, zero-signal files **41 → 39**. Only two files left the adult-candidate
set: `13_02_ENT_Hearing_Loss` (rubella in the TORCH list under *congenital* causes of
hearing loss — a true positive) and `C7_Pancreatobiliary` (mumps in GET SMASHED —
marginal). **So the false-negative problem the withdrawn cross-check predicted was almost
entirely the `\bALL\b` artifact.** The shipped detector was closer to right than the
cross-check suggested.

### What session 2 must do

1. **The 39 zero-signal files are the adult candidates, and they are the only files where
   manual verification is owed.** A missed paediatric figure in a file labelled `adult` is
   the dangerous error; a `mixed` or `paed` file already warns its reader. Read each of
   the 39 — headings and any absolute quantity — before granting the label.
   Flagged as suspicious on their names alone: `13_07c_ENT_Dental_and_Teeth_Problems`
   (dental eruption is paediatric, yet it scores 0 even with `teething` in the pattern),
   `14a-2_Psych_Overdose_and_Poisoning_Management` (paediatric ingestion), and
   `08_04_Infectious_Disease_Antibiogram` (antibiotic choice carries paediatric dosing).
2. **`paed` candidates:** the 40 `Corpus A/15_*_Paeds_*` files and
   `11_10_Ortho_-_Paediatric_Orthopaedics`. Note `merge_tools.py paed` skips any path
   containing "paed", so its sweep never examines these — they need a separate check.
3. **Everything not in (1) or (2) is `mixed`**, which is where the placeholder already
   sits — so the write is only to the adult and paed sets.
4. `figures: none` beyond `Medications_Reference.md` — needs an operational definition
   first. CLAUDE.md says "where the file states no numbers", which is broader than
   `RE_DOSE` (doses only) and broader than what `lint` enforces. Do not set the key from
   `RE_DOSE` alone: a file carrying a threshold or reference range but no dose would pass,
   be wrongly flagged figure-free, and §1.14 then forbids ever adding a figure to it.
5. Run `scan` to write the `conflicts_open` / `conflicts_r1` counters and the `_meta/`
   artefacts.

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

**Anchored to the vault root**, defined as the nearest ancestor directory holding
CLAUDE.md, so it resolves identically whether `--dir` is the vault or one corpus. An
earlier version matched by bare basename, which would have dropped a clinical file sharing
one of those names from every scan with no error and nothing downstream detecting the loss.
Verified after anchoring: walking from the vault root yields exactly one top-level file,
`Medications_Reference.md`.
