---
name: run-state
description: Cross-session memory for the corpus merge. Session context does not carry over — this file and the Queue markers in MASTER_VERIFICATION_WORKFLOW.md are the only memory.
---

# RUN_STATE

> [!danger] **BASELINE — run this first, every session, before any content-touching step.**
> ```bash
> git tag -f base-A 0db4034753b00573f379f273778eba01691d1c49
> git rev-parse base-A
> ```
> Local only, idempotent, no push. The tag **cannot** be pushed from a web session (proxy
> refuses tag pushes, 403) and GitHub has no UI for tagging an arbitrary commit, so it must
> be re-created in each clone.
>
> **If that SHA is absent from history, STOP — the clone is wrong, not the tag.**
>
> `base-A` **did not exist for the first six steps of this work** (26, 17, 11, 28a, 28b,
> 28c). Every "revert cleanly" and "diff against baseline" guarantee in the design assumed
> it did. Verified correct: last commit before session work · corpus 148 / 39 / 53 · corpus
> trees byte-identical to `39be13e`, the final content upload · no corpus file ever
> *modified* during the upload sequence · no `trust:` / `figures:` / `conflicts_*` /
> `CF-###` / `SRC:` anywhere in it.

## Night of 2026-08-30 — COMPLETE. All items done, 12 PRs merged to `main`.

| Item | PR | Outcome |
|---|---|---|
| `RE_OPEN_SOURCE` extension | #8 | 18 added, `ADA` rejected (American Diabetes Association) |
| `--dry-run` genuinely dry | #9 | 4 dry runs leave the tree clean |
| Corpus B link count + Step 31 split | #10 | expand, never strip |
| Merge lessons | #11 | recorded in §1.1.9.1 |
| Step 29 week mapping + W4 freeze | #12 | 37 files mapped |
| **28d** `_meta/OWNERS.md` | #13 | 43 drugs, 31 multi-file, 24 `RANGE NOT STATED` |
| `actionability()` MIXED | #14 | bug was 11 markers, not 4 |
| Prefix map + 191 clusters + coverage | #15 | **P2 → GER**, not GER → P2 |
| **Step 31** expansion | #16 | 573 expanded, 188 marked, 1 repaired |
| Step 29 conditional blocks | #17 | W1 restructured by study return |
| **Step 27** proposals | #18 | 290 boxes, 97 P1, **no box edited** |
| Follow-ups | #19 | Corpus B now **0 dangling** |

### `main` verified after the last merge

Corpus A 148 · B 39 · C 53 · **0 conflict markers**
Wikilinks: A **1257 / 0 dangling** · B **608 / 0** · C **396 / 0**
scan 360 (47 open · 11 mixed · 245 triage · 57 login) · lint 178 · drugs 0 actionable

### Not started, by instruction

**Step 29 Block 1** — needs approval on the first destination table.


## Step 26 — Provenance and population labelling · ✅ COMPLETE 2026-08-30

**→ NEXT: Step 11** (AU drug dosing and product names), then Step 17. See queue §1.1.9 —
the run order is 26, 11, 17, 28, 27, 29, **not** numeric order.

**Sessions 1–2: 2026-08-30, branch `claude/next-6gvrdi`.**

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

### `population:` — now classified, not placeholder

| Label | Files | Basis |
|---|---|---|
| `adult` | 32 | each file **read in full**; content is adult by nature and carries no paediatric entry |
| `paed` | 41 | the 40 `Corpus A/15_*_Paeds_*` files + `11_10_Ortho_-_Paediatric_Orthopaedics` |
| `mixed` | 167 | everything else, plus 7 files that scored zero but earned `mixed` on reading |

`Medications_Reference.md` (vault root, outside the 240) is `mixed`: drug-class
pharmacology, age-agnostic.

**The detector informed, it never decided.** Labels are on what each file *is*. The count
was used only to choose which 39 files to read.

**Seven files were labelled `mixed` against a zero detector score** — see the table below.

**`figures: none` is set on `Medications_Reference.md` only.** Not attempted elsewhere.

**No `conflicts_open` / `conflicts_r1` counters have been written** — `scan` has not been
run.

### The 39 zero-signal files: 32 `adult`, 7 `mixed`

All 39 were read. The seven that earned `mixed` despite scoring zero:

| File | Why `mixed` |
|---|---|
| `08_04_Infectious_Disease_-_Antibiogram` | organism→drug table, **0 doses, 0 age references**. Age-agnostic — `adult` would be a false assertion |
| `14a-2_Psych_-_Overdose_and_Poisoning_Management` | antidote table, **0 doses, 0 age references**. Same shape |
| `10_06a_Haemonc_-_Macrocytic_Anaemia` | **Fanconi anaemia** — autosomal recessive marrow failure with short stature, thumb/radius anomalies, café-au-lait spots. A childhood-presenting disease with its own entry |
| `10_06b_Haemonc_-_Thrombophilia__APS...` | **congenital methaemoglobinaemia** (HbM, NADH met-Hb reductase deficiency) — presents in infancy |
| `11_08c_Ortho_-_Fracture_Types_and_Pathological_Fractures` | **osteogenesis imperfecta** (four types, II lethal in the neonatal period) and **osteopetrosis** |
| `13_06c_ENT_-_Bell_s_Palsy` | an 11-line pointer stub with no clinical content and no figures. `adult` would assert something about content that is not there |
| `NEW_Drugs_19_Rheumatological` | baclofen indications name **cerebral palsy**, and intrathecal pumps are largely paediatric practice |

**Three files were suspected paediatric on their names and turned out adult on reading:**
`13_07c_ENT_-_Dental_and_Teeth_Problems` covers tooth pain, trismus, dental abscess and
Vincent's angina — no eruption or primary dentition content, so its zero score was
correct, and `adult` is what correctly scopes its `amoxicillin 500mg/8h + metronidazole
400mg/8h`. `14a-2` and `08_04` proved to be dose-free tables (above), so the suspected
paediatric-dosing risk did not exist.

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

### `figures:` and the conflict counters

`scan` was run at the vault root: **conflict counters written to all 241 files**, all
`conflicts_open: 0` / `conflicts_r1: 0`, which is correct — no `CONFLICT` block exists yet,
they are created by Step 29. `_meta/VERIFICATION_QUEUE.md`, `CONFLICTS.md`,
`DOSE_MIRRORS.md` and `PENDING_ROWS_DRAFT.md` generated.

**347 `UNVERIFIED` markers: 39 actionable against an open AU source · 254 needing triage ·
54 login-required (permanently noted).** The 254 name no source, which CLAUDE.md §1.7
forbids — that is the triage backlog, and it is large.

`lint` reports **178 problems, all one category**: a dose figure in an `inherited` or
`unverified` file with no marker or `→MED` mirror. That is Step 11/17 territory, not this
step. **Zero** missing-frontmatter problems and **zero** `figures: none` violations.

> [!danger] **Corpus C states doses. The corpus-level claim that it does not is false.**
> CLAUDE.md §1.6 and §1.11, and MERGE_SPEC, describe Corpus C as "**States no doses or
> reference ranges**". Checking all 22 Corpus C drug files against `RE_DOSE` and a
> threshold/reference-range pattern, then reading every hit:
>
> **8 of 22 state a dose or a dose-adjacent quantity**, among them:
> - `NEW_Drugs_01_Allergy_and_Anaphylaxis` — the full ASCIA adrenaline table: `0.01 mL/kg`
>   to a maximum of `0.5 mg`, and injector weight bands `150 microgram` **from 7.5 kg**,
>   `300 microgram` from 20 kg. **That 7.5 kg floor is B50** — the exact defect §1.11 cites,
>   reproduced here in a corpus documented as dose-free.
> - `NEW_Drugs_10_Endocrine` — `hydrocortisone 100 mg IV at induction` + `200 mg per 24 h`.
>   **This one is exemplary**: the next line reads "THESE TWO FIGURES ARE ADULT DOSES. DO
>   NOT USE THEM IN A CHILD", which is rule 5 in its correct form.
> - `NEW_Drugs_12` loperamide max ~`8 mg/day`, toxicity >`100 mg/day`; `NEW_Drugs_16`
>   anti-D `500 IU` at 28 and 34 weeks; `NEW_Drugs_07` pyridoxine neuropathy >`1000 mg/day`,
>   plus Hb targets `≤115 g/L` and a transfusion trigger `<70 g/L`; `NEW_Drugs_05`
>   vancomycin `AUC/MIC 400–600 mg·h/L`; `NEW_Drugs_03` and `NEW_Drugs_10` renal cut-offs.
>
> **This is a description that is wrong, not an instruction to change.** §1.11's rule — do
> not ADD doses or reference ranges to Corpus C, do not backfill its empty
> `Normal:`/`Abnormal:` fields — still stands and was followed. But the provenance table
> in §1.6 is load-bearing for the merge rules, and it currently overstates C's abstention.
> **Left for the user to decide** rather than edited from a session.

**`figures: none` set on 3 files only**, not the 22: `NEW_Drugs_11_Eye`,
`NEW_Drugs_19_Rheumatological`, `NEW_Drugs_21_Miscellaneous`. Two more passed the
automated test and were rejected on reading (rule 2 — a clean scan is not proof):
`NEW_Drugs_20_Vaccines` states "observed for at least **15 minutes**" and a cold chain of
"**2–8 °C**"; `NEW_Drugs_14` defines neutropenic sepsis by "chemotherapy in the last
**6 weeks**". Noted for the record: `NEW_Drugs_11` says "one drop is enough" and
`NEW_Drugs_19` says "ONCE WEEKLY dosing" — quantities in words, no numeral, so the key
stands.

### FINDINGS FROM THIS STEP — all now fixed

**Finding 1 — FIXED. `merge_tools.py paed` silently skipped every orthopaedics file.**
`cmd_paed` skips any path where `"paed" in r.lower()`. The word **ortho·paed·ics contains
"paed"**, so the shipped sweep never examines:
`11_01_Ortho_-_Orthopaedic_Emergencies`, `11_06_Ortho_-_Spinal_Orthopaedics`,
`11_09a_Ortho_-_Orthopaedic_and_Bone_Malignancies`,
`NEW_Investigations_Orthopaedics_Neurology_and_Other`, `NEW_Orthopaedics_and_Trauma`
(and `11_10_Ortho_-_Paediatric_Orthopaedics`, which it should skip). Five files are
excluded for a reason that has nothing to do with their content, and the sweep reports
no error. **This session's labelling did not use `cmd_paed`** — it used a direct
`RE_PAED_SIGNAL` count over every file — so the labels above are unaffected. The fix is
to match the paediatric filename marker, not a bare substring.

**Finding 2 — FIXED. A correction to this session's own earlier claim about `congenital`.**
Session 1 rejected `congenital` from `RE_PAED_SIGNAL` and recorded "5 files flagged,
**0 true positives**". **That claim was wrong.** It was made by reading the *flagged
lines*; reading the *disease entries* those lines sit in shows `congenital` caught two
genuine paediatric-scope files — `10_06b` (congenital methaemoglobinaemia) and `11_08c`
(osteogenesis imperfecta) — both of which are now labelled `mixed` on exactly that
content. Corrected score: **6 files flagged, 2 true positives.**

The asymmetry argues for restoring it: a false positive costs a `mixed` label (safe, tells
the reader to check), a false negative costs a wrong `adult` label (the B65 failure).
`congenital` has been restored and the source note corrected to 6 flagged / 2 true. The
three `adult`-labelled files it now flags were rechecked: congenital absence of the vas
deferens, congenital long QT and congenital lymphoedema are each one item in an adult
differential, not a paediatric disease entry. **Those labels stand.**

**Finding 3 — the substring defect class.** Two further instances were found by auditing
every containment test and unanchored alternative in `merge_tools.py` against all 240
files, rather than by eye: **`ASCIA` matches inside `fascia`/`fascial` on 33 corpus lines**
— so any line about fascial planes scored `OPEN` and was routed into the actionable
verification queue as though ASCIA could settle it — and **`epinephrine` is a substring of
`norepinephrine`**, so every noradrenaline line drew a second, wrong suggestion. Both
fixed; all acronyms word-anchored; `DRUG_NAMING` now matched on word boundaries. This is
now **CLAUDE.md rule 9**.

### What the next session must do

**Run Step 11, then Step 17.** Both are existing steps (§1.17, §1.23) pulled to the front
of Phase 5 because they are cheap, corpus-wide, and fix the highest-risk error class before
the MCQ. `lint`'s 178 unmarked-dose hits are the raw material for Step 11.

Deferred from this step:
1. The Corpus C provenance description (see the danger box above) — **user's call.**
2. `figures: none` beyond `Medications_Reference.md` — needs an operational definition
   first. CLAUDE.md says "where the file states no numbers", which is broader than
   `RE_DOSE` (doses only) and broader than what `lint` enforces. Do not set the key from
   `RE_DOSE` alone: a file carrying a threshold or reference range but no dose would pass,
   be wrongly flagged figure-free, and §1.14 then forbids ever adding a figure to it.
3. Run `scan` to write the `conflicts_open` / `conflicts_r1` counters and the `_meta/`
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

---

## BLOCK 1 (C1–C7) IS COMPLETE — 2026-08-31

All seven gastroenterology files merged: PRs #30, #31, #32, #35, #36, #37, #38.
**Resume at Block 2, `D1_Headache_and_Meningism`.**

**14 additive placements, 30 discards** across the block. The discard-heavy ratio is the
finding: `03_Gastrointestinal` is 20 000 words and among the most worked files in Corpus A,
so Corpus B's gastroenterology layer was mostly duplicative. Where it added, it added
**reasoning the corpus set up and never drew** — the visceral-to-parietal transition, the
dentate line implying painless internal haemorrhoids, the CT transition point deciding
whether to operate.

### Search rules established during Block 1 — read before the next file

Nine searches returned the wrong answer across the block. Three causes, all now known:

1. **Fixed word order.** A regex needing two terms in a set order kept failing, because the
   corpus writes *prophylactic antibiotics* not *antibiotic prophylaxis*, and *strangulated
   hernia* not *hernia … obstruction*. **Search the rarer word alone and read the hits.**
   Adopted before C6, which then produced **no false negatives**.
2. **The eponym trap.** `Glasgow-Imrie` returned ABSENT while §0.11 carried the **Glasgow
   score** all along; `West Haven` returned ABSENT while §0.6.3 carried the full grading
   under a heading reading only "Grading". **A score with a compound name may appear under
   either half, or neither. Search the disease plus the word *score*, then read.**
   This was the most dangerous of the run: acting on it would have placed a second,
   differently-named copy of one score beside the first.
3. **Corpus A alone is not the vault.** `aprepitant`, the aortoenteric *herald bleed* and
   the over-transfusion/portal-pressure point are all in **Corpus C**. Now Step 29 policy.

And rule 9 fired four times on the other side — `FAST`, `obturator`, `hot shower`,
`second-look` all matched a different concept sharing a word.

---

## Overnight run, 2026-08-30 → 31 — the first half

**Stopped after C3 that night; C4–C7 completed 2026-08-31.** Block 1 is C1–C7; **C1, C2 and C3 are merged** (PRs #30, #31,
#32). **C4–C7, Block 2 (D1–D7), GER1–2 and A6/A7/A8 are NOT started.** Nothing is
half-merged and no branch is left unmerged — every destination table that was written was
followed through to its placements.

Resume at **C4_Gastrointestinal_Bleeding**. The method that worked is in the three
committed destination tables; follow those.

### Corpus B files: 3 of 37 merged

| | |
|---|---|
| merged | `C1_Acute_Abdomen`, `C2_Nausea_and_Vomiting`, `C3_Jaundice_and_Liver_Disease` |
| next | `C4_Gastrointestinal_Bleeding` |
| not started | C4–C7, D1–D7, GER1–2, A6/A7/A8, and everything mapped to a later week |

**No Corpus B file has been deleted.** C1–C3 are fully merged or explicitly discarded
section by section, so they are eligible for deletion under §1.14 — but other unmerged B
files link to them, and deleting now would dangle those links. Deletion is a separate
decision once Block 1 finishes.

### Conflict state — the do-not-revise-from list is currently EMPTY

Verified two ways: every corpus file's `conflicts_open` and `conflicts_r1` counter reads
**0**, and the only `CONFLICT CF-` blocks in clinical content are the three **CF-001**
blocks, all carrying a `RESOLVED 2026-08-30 NEITHER-WRONG` stamp.

One thing would be on that list if it had an ID: the **appendicitis imaging
disagreement** at `03_Gastrointestinal` §0.18.1, deliberately left without a `CF-` number.
See `_meta/merges/C1_Acute_Abdomen.md`.

> A search for `CONFLICT CF-` in clinical files now returns a **false positive** at
> `03_Gastrointestinal` L836 — that line is prose explaining why there is no `CF-` number,
> not a conflict block. Any future conflict-counting tool needs to exclude it.

### Method lessons from this run

1. **Check gaps against Corpus A *and* Corpus C.** C2 nearly produced a false gap
   (aprepitant) because only A was searched. Corpus C is `snippet` and outranks Corpus B
   on provenance, so a topic covered in C means the B section is superseded, not additive.
2. **Rule 9 fired four times**, once inside a pattern written during this very run:
   `FAST` matching the English word and the stroke mnemonic · `obturator` matching a
   hernia, a nerve and lymph nodes · `hot shower` matching Uhthoff's phenomenon and
   pruritus · `parotid enlargement` present in an HIV file, a different cause of the same
   sign.
3. **Rule 2 fired once and would have caused a wrong merge.** `West Haven` returned zero
   hits; §0.6.3 already carries the full grading under a heading reading only "Grading".
4. **Two wikilinks written from memory were wrong** and were caught only by checking every
   link against the filesystem before commit. Do that check every time; do not trust a
   filename that looks right.

## Correction — why the two `→MED:` markers behaved differently

Both explanations given in the B1 and B2 commit messages were **wrong**, and both were
asserted from reading the code rather than running it. Tested 2026-08-31:

```
GTN                    MED match: ['GTN']      DOSE match: []
sodium nitroprusside   MED match: []           DOSE match: []
```

| What was claimed | What is true |
|---|---|
| `→MED:GTN` registered "because the filename inside its wikilink contains digits" | **`RE_DOSE` requires a unit** (`mg`, `mL`, …), so the filename never matched it. It registered because **`RE_MED_MIRROR` matched and the report listed it regardless of whether a figure was found** — the report had no figure requirement at all |
| `→MED:sodium nitroprusside` did not register "because the report only picks up lines carrying a digit" | **`RE_MED_MIRROR`'s drug pattern was `[A-Za-z0-9_\-]+`, which excludes spaces.** A two-word drug name never matched. Nothing to do with digits |

**The second is a defect in its own right, and worse than the misuse that exposed it.**
Every multi-word drug name — `sodium nitroprusside`, `magnesium sulfate`, `calcium
gluconate`, `tranexamic acid` — was **silently ignored** by the mirror machinery. No match,
no report entry, no error. That is the voided-marker failure shape, and it was found the
only way it could be: **by writing one and noticing the report did not change.**

An audit of every `→MED:` in the vault found **three, all `adrenaline`, all parsing, all
correct** — so nothing was lost. The defect was latent, waiting for the first two-word drug.

## PRIORITY study-list gaps — MISSING DOMAINS, not single facts

**Different in kind from the eponym gaps below.** Those are one named thing each. **These
were whole clinical domains absent from 240 files**, and both have now been filled — **but
filled from Corpus B, which is `unverified` model knowledge. Read them knowing that.**

| Domain | Why it matters | Now in | Read it as |
|---|---|---|---|
| **Heat illness** — heat exhaustion vs heat stroke, exertional vs classic, active cooling, hypothermia management | **Australian-specific and seasonal.** The corpus had drug-induced hyperthermia (NMS, serotonin syndrome, malignant hyperthermia) and nothing environmental. Hypothermia existed only as an ECG pattern | `11_09b_Ortho_-_Trauma` §Added from unverified layer — environmental injury | `unverified`; six `UNVERIFIED` markers inside it, and **not one temperature figure is stated** |
| **Foreign bodies** — button battery above all, plus nasal, aural, ocular and rectal | **A button battery in the oesophagus is liquefactive necrosis already in progress.** The word `batter` returned six vault hits and not one was a button battery — two were "a battery of tests", one a pacemaker battery, one the Short Physical Performance Battery | `13_06b_ENT` §0.3.2, with pointers from `13_04`, `13_02`, `05_Ophthalmology`, `03_GI` §0.25.2 | `unverified`; **no removal time window stated** — marker names Poisons Information Centre, RCH, Queensland Children's Health |
| **Recognising dying** — the terminal phase, anticipatory prescribing, voluntary assisted dying | **This is an OSCE station.** `10_11c_Oncology_-_Palliative_Care_Prescribing` could say which opioid to convert to and not that the patient was dying | `10_11c_Oncology_-_Palliative_Care_Prescribing` §Added from unverified layer | `unverified`; **all anticipatory doses omitted** (eTG, login-gated) and **no VAD law stated** (state legislation) |

**Both are worth verifying against a named source before the exam**, precisely because they
are now the only account of these domains in the vault — there is no `inherited` layer
underneath them to disagree with.

### Same tier, different shape — **MYOCARDITIS has no entity**

> [!danger] **27 mentions across the vault. Every one is somebody else's complication. No entry.**
> Found merging B1, 2026-08-31. `grep -i myocarditis` returns 27 hits and
> `grep "^#+.*[Mm]yocarditis"` returns **nothing**. It appears as a complication of
> **diphtheria** (`15_04a`), **clozapine** (`14_03`), **Chagas disease** (`08_07`),
> **measles** (`15_03a`), **Lyme disease** (`08_01-03`), and as a cause of **dilated
> cardiomyopathy** (`01_Cardiovascular:1006`) — and never as a thing a patient presents with.
>
> **This is the same tier as heat illness, recognising dying and foreign bodies**, and it is
> a different shape from all three. Those were domains absent from the specification *and*
> the corpus. **Myocarditis is densely present and structurally absent**: the word is
> everywhere, so every search for it succeeds, and no search reveals that there is nothing
> to find. A coverage audit keyed on term presence would score it as covered.
>
> **What exists now, and what it is not.** The B1 merge added a myopericarditis block to
> `01_Cardiovascular` §0.32 Pericarditis — troponin rise or impaired function reclassifies
> the illness, and exertion during active myocarditis is associated with arrhythmic death,
> so exercise restriction matters in a way it does not in uncomplicated pericarditis.
> **That block is a fragment inside another disease's entry, it is `unverified`, and it is
> explicitly not a substitute for an entry.** A reader arriving at "young person, chest
> pain, viral prodrome, raised troponin" still has nowhere to go.
>
> **A proper entry needs** aetiology (viral, drug, autoimmune, peripartum), the
> presentation, its overlap with pericarditis, the ECG and echo findings, the troponin
> pattern, when to suspect fulminant disease, and the exercise-restriction advice with a
> duration. `UNVERIFIED — the whole entry, per CSANZ or Heart Foundation.`
>
> **Read the §0.32 fragment knowing there is no inherited layer beneath it** — the same
> caveat as the three domains above.

## Study-list additions — real absences no merge can close

Gaps confirmed absent from **all 240 corpus files** and **not supplied by the Corpus B
material that covered the surrounding topic**. They are recorded rather than written,
because the only available filling material is model knowledge.

| Topic | Absent from | Why it matters | Would be settled by |
|---|---|---|---|
| **Dubin-Johnson syndrome** | whole vault; C3 does not cover it | Conjugated hyperbilirubinaemia with an otherwise normal liver — the benign cause that must not be worked up as obstruction | RACGP, or a hepatology reference |
| **Decompression sickness** | whole vault | Australian diving makes this more arguable than altitude illness, which is deliberately left alone as low priority for an intern exam. The only current mention is a nitrous-oxide gas-space aside in `NEW_Drugs_02` | SA Health / DAN Asia-Pacific, or an emergency medicine reference |
| **Rotor syndrome** | whole vault; C3 does not cover it | The same, and it is the standard exam pairing with Dubin-Johnson | as above |
| **Schatzki ring** | whole vault; C6 does not cover it | A specific lower-oesophageal ring causing intermittent solid dysphagia; `13_06b` §0.2 covers benign stricture generally but not this entity | RACGP, or a gastroenterology reference |

Both are hereditary conjugated hyperbilirubinaemias. The vault has Gilbert and
Crigler-Najjar (the **unconjugated** pair) but neither conjugated one, so the
classification at `03_Gastrointestinal` §0.41.8 is currently half-populated — which is
stated in that section rather than quietly filled.

## Scores and terms written with NON-ASCII DIGITS — search differently in Obsidian

Measured 2026-08-31 across all 240 corpus files: **382 contexts** contain sub- or
superscript digits. **An Obsidian search for the ASCII form finds none of them.**

### Named instruments — the ones that matter when revising

| Written as | An ASCII search that FAILS | Where | n |
|---|---|---|---|
| **`CHA₂DS₂-VASc`** | `CHA2DS2-VASc` | `01_Cardiovascular`, `B3_Arrhythmia` | 8 |
| **`ABCD²`** | `ABCD2` | `04_Neurology` | 5 |
| **`FEV₁`** | `FEV1` | `NEW_Investigations_Respiratory` | 8 |
| **`HbA₂`** | `HbA2` | `NEW_Investigations_Haematology` | 5 |
| `5-HT₁B`, `5-HT₁D`, `5-HT₂A`, `5-HT₂B`, `5-HT₂C` | `5-HT1B` etc. | the `NEW_Drugs` files | 6 |
| `PGE₁`, `PGE₂`, `PGF₂` | `PGE1` etc. | `NEW_Drugs_16` | 3 |

### High-frequency terms — the same problem, and `B₁₂` is the one to remember

| Written as | Fails as | n |
|---|---|---|
| **`B₁₂`** | `B12` | **23** |
| `CO₂` | `CO2` | 76 |
| `PaO₂`, `PaCO₂`, `SpO₂`, `FiO₂`, `SaO₂`, `pCO₂`, `ETCO₂` | ASCII forms | ~73 |
| `×10⁹/L` | `x10^9`, `x109` | throughout the haematology thresholds |
| `m²`, `cm²`, `cm³`, `mm³` | ASCII forms | 13 |

**Practical rule for revising in Obsidian:** search the **letters only** — `CHA`, `ABCD`,
`FEV`, `HT`, and `B` followed by a space in the case of B₁₂ — or paste the subscript
character itself. Searching the number will not work.

`scripts/merge_tools.py normalise()` now folds these to ASCII, so the project's own tools
are unaffected. **Obsidian's search is not.**

### A clinical finding that came out of this audit

`01_Cardiovascular` uses **`CHA₂DS₂-VASc`** and states the threshold as **"≥1 (male) or ≥2
(female)"**. `Corpus C/NEW_Exam_Manoeuvres_and_Procedures` writes **`CHA₂DS₂-VA/VASc`**,
naming both instruments. **`CHA₂DS₂-VA` removes sex as a criterion**, which would make the
sex-split threshold obsolete. Queued as **R1** in the verification queue against the Heart
Foundation and Stroke Foundation, both open. **Not adjudicated** — Corpus C names the newer
instrument without stating a threshold, so there is no competing claim to conflict with.

---

# STATE AS AT 2026-08-31 — READ THIS FIRST

## Resume point

**BLOCK 1 (C1–C7) AND BLOCK 2 (D1–D7) BOTH COMPLETE.**
**RESUME AT: the C2–C7 full re-audit** (below), then GER1–2 · A6, A7, A8 · F0-1…F0-5 ·
B1–B6 · A1–A5, A9, A10.

### Block 2 result — 8 placements, 34 discards, ZERO new conflicts

| File | Placements | Discards | Of concepts tested, already present |
|---|---|---|---|
| D1 Headache | 1 | 5 | 32 of 33 |
| D2 Consciousness | 2 | 5 | 15 of 19 |
| D3 Stroke | 1 | 6 | — (2 scores saved by digit folding) |
| D4 Weakness | 2 | 6 | 19 of 22 |
| D5 Dizziness | 1 | 5 | 18 of 20 |
| D6 Seizures | 1 | 6 | 20 of 22 |
| D7 Cranial nerves | 1 | 5 | 20 of 22 |

**Conflict rate: 0 across 7 files, against Block 1's 1 across 7.** Vault-wide still
**CF-032 alone**, 0 R1. Both files flagged in advance as collision risks — D5 against
§Vertigo, D7 against §Cranial Nerve Disorders — collided almost completely, and **the
corpus won both times**.

`04_Neurology` is 28 637 words and absorbed six of the eight placements. Where Corpus B
added, it added **discriminations the corpus had the parts for but never assembled**: the
neck-stiffness differential, structural versus metabolic, stroke chameleons, foot drop by
inversion, bulbar versus pseudobulbar.

### The four remaining Block-2 gaps no merge can close

Hunt and Hess · Weber syndrome · Millard-Gubler · mal de débarquement · glossopharyngeal
neuralgia. Each absent from the vault **and** from the B file covering that topic. On the
study list with Dubin-Johnson, Rotor and Schatzki ring.

---

## C2–C7 FULL RE-AUDIT — DONE 2026-08-31

**57 verdict rows re-tested under rule 10.** Two more absences were wrong; both corrected.
**Total duplicates from Block 1: seven.** All seven are now pointers.

| # | Block 1 claim | Original lives in | Shape |
|---|---|---|---|
| 1 | ALP/GGT bone differential | `NEW_Investigations_General_and_Preventive` L77–79 | different file |
| 2 | Russell's sign + dental erosion | `14_05a` L42 — **same file, 36 lines up** | same file |
| 3 | CT transition point | `Investigation-Interpretation` L159 | different file |
| 4 | appendicitis in pregnancy | `NEW_Obstetrics` L31 | different file |
| 5 | psoas abscess | `NEW_Exam_Manoeuvres` L285 | left — pointers, never a copy |
| 6 | severity is not the lipase | `NEW_Investigations_Gastroenterology` L158 | different file |
| 7 | urine-and-stool discriminator | `NEW_Investigations_Renal_and_Urology` L88 | different file, **partial** — mechanism kept |

**Six of seven originals were in Corpus C**, and five sat in a **different file** from where
the duplicate landed. That is the shape nothing else detects.

### The other direction is clean — this is the reassuring half

**22 PRESENT verdicts were re-tested**, the ones whose being wrong would mean content was
**discarded** that should have merged. **All 22 confirmed.** No discard was wrong.

**Every Block 1 error ran the same direction: a gap called where none existed, never a gap
missed.** The merges were over-eager, not careless — and over-eagerness is the recoverable
failure, because the added block is always visible and removable.

---

## MERGE QUEUE PROGRESS

**Done:** C1–C7 · D1–D7 · **GER1 · GER2 · A6**.
**RESUME AT: A7**, then A8 · F0-1…F0-5 · B1–B6 · A1–A5, A9, A10.

### GER1, GER2, A6 results

| File | Placements | Discards | Present of tested |
|---|---|---|---|
| GER1 | 1 | 5 | 21 of 22 |
| GER2 | 3 | 3 | 15 of 21 |
| A6 | 2 (large) | 6 | 13 of 17 |

**Still zero new conflicts.** Vault-wide: **CF-032 alone, 0 R1.**

### The two biggest clinical gaps found in the entire merge, both here

1. **The corpus could say which opioid to convert to, and not that the patient was dying.**
   `10_11c_Oncology_-_Palliative_Care_Prescribing` is a prescribing file with three
   sections. `last days of life`, `terminal phase`, `recognising dying` and `anticipatory
   prescribing` returned **nothing** vault-wide. Filled from GER2 §0.5.
2. **Environmental heat illness was entirely absent** — the corpus had drug-induced
   hyperthermia (NMS, serotonin syndrome, malignant hyperthermia) and nothing on heat
   exhaustion, heat stroke, or hypothermia beyond an ECG pattern. Filled from A6.

### A reusable tool was built: `inventory.py` (scratchpad, not committed)

Enumerates named scores, eponyms and acronyms in a file **with digit folding**, so a
B-block claim can be checked against the actual instrument list rather than a guessed
search string. Noisy on all-caps prose (`FIRST`, `WHY`, `MULTIPLE`) — **it informs, it does
not decide**, and every hit is read.

**It is now a committed script: `scripts/inventory.py`.** Usage:
`python3 scripts/inventory.py "Corpus A/01_Cardiovascular.md"`, `--corpus A` for a whole
corpus, or `--compare FILE_A FILE_B` for what B has that A does not.

> Its own self-test found a defect in its first version: the acronym pattern allowed
> **trailing** digits only, so after folding it saw `ABCD2` but **not `CHA2DS2-VASc`** — the
> very score it was written to catch. A tool that misses its own worked example is worse
> than no tool, because it reports a clean inventory. Fixed to allow interspersed digits;
> it now returns `CHA2DS2-VASc`, the `CHA2DS2-VA` variant at `01_Cardiovascular` L297, and
> `CHA2DS2-VASc-based`.

### BEFORE B1–B6 — a required step, not yet done

**Enumerate every named score and eponym in `01_Cardiovascular` with digit folding, and
check each B-block claim against that list specifically.** `CHA₂DS₂-VASc` is already there
**with subscripts** and `B3_Arrhythmia` links to it — the exact configuration that nearly
produced a cross-file duplicate in D3.

**Same for A1–A5, A9, A10 against the emergency files:** Wells · PERC · GRACE · TIMI ·
HAS-BLED · Ottawa · Canadian C-spine · PECARN · NEXUS.

---

## Method reminder — non-negotiable, it has now caught eleven errors

Scope: **every claim in those six destination tables**, not only the concepts previously
listed. They were built with the A-and-C rule but **before rule 10 and digit folding**, so
they sit at lower confidence than D4–D7 now do.

Method: rule 10 throughout — pre-merge tree `245c1e5` **and** current tree, Corpus A **and**
C, **nothing excluded**, digit folding, instrument-specific components.

**Order:** GER1–2 · A6, A7, A8 · F0-1…F0-5 · B1–B6 · A1–A5, A9, A10.

**Method, non-negotiable now that it has caught seven errors:** rule 10 throughout —
pre-merge tree `245c1e5` **and** current tree, Corpus A **and** C, **nothing excluded**,
digit folding, instrument-specific components. Read every hit before trusting it.

**Cardiology and emergency are as eponym-dense as neurology** — Levine, Beck, Cushing,
Kussmaul, TIMI, GRACE, Wells, PERC, CHA₂DS₂-VASc, HAS-BLED — so B1–B6 and A1–A5 will
exercise the eponym and Unicode checks hardest. Note `CHA₂DS₂-VASc` and `HAS-BLED`
specifically: the first is already in `01_Cardiovascular` **with subscripts**, and B3 links
to it.

---

`D4_Weakness__Neuropathy_and_Radiculopathy` — **nothing committed, no table written.** Its
three candidate gaps are listed below and **must be re-verified against the pre-merge tree
before landing** (see the finding below for why).

Remaining after D4: D5, D6, D7 · GER1–2 · A6, A7, A8 · F0-1…F0-5 · B1–B6 · A1–A5, A9, A10.

**Corpus B deletion remains deferred** until every B file is merged AND intra-B links are
retargeted — not per block. See CLAUDE.md §1.14.

## THE FINDING — five merged blocks duplicated content already in the vault

Discovered 2026-08-31 by re-running the C-block absence conclusions against the
**pre-merge tree `245c1e5`**. **42 of 45 absences hold. Five were wrong**, and the merges
built on them created duplicates.

> The first attempt at this audit searched the **current** corpus and reported everything
> present — because it was finding my own additions. **An audit of a merge must run against
> the tree the merge started from.** Recorded because the mistake took a second run to see.

| Merged block | Duplicates | Status |
|---|---|---|
| ALP raised + GGT normal → bone, in `NEW_Investigations_Gastroenterology` §0.1.1 | `NEW_Investigations_General_and_Preventive` **L77–79** — near-verbatim, and `snippet` rather than `unverified` | corrected |
| Russell's sign + dental erosion, in `14_05a` | `14_05a` **L42** — **the same file, 36 lines above** | corrected; parotid enlargement kept, that absence was real |
| CT transition point, in `03_Gastrointestinal` §0.39.1 | `Investigation-Interpretation` **L159** | corrected to a pointer |
| Appendicitis in pregnancy, in `03_Gastrointestinal` §0.41.6 | `NEW_Obstetrics` **L31** | corrected to a pointer |
| Psoas abscess (one-line differential mentions) | `NEW_Exam_Manoeuvres_and_Procedures` **L285** | left as pointers — they were never a second copy |

**Barrett surveillance holds as absent.** Its apparent hits were *cardiac* radiofrequency
ablation and HCC ablation — a rule 9 artifact.

### Two causes. Neither was digit folding.

1. **C1 predates the A-and-C rule by one file.** Its gap check searched Corpus A alone;
   visceral/parietal, psoas abscess and appendicitis-in-pregnancy all live in Corpus C.
2. **A search that excludes its own destination cannot detect the duplicate it is about to
   create.** The Russell's sign check ran `grep … "Corpus A" | grep -v "14_05a"`, answering
   *"does this exist elsewhere"* when the question was *"does this exist at all"*. The
   search was correct; its **scope** was wrong. Now a required check in Step 29 and
   CLAUDE.md rule 10.

## D4 candidate gaps — NOT YET VERIFIED against the pre-merge tree

1. **Steroid myopathy has a normal CK.** Checked only against the current corpus.
2. **Do not over-image or over-interpret imaging in radiculopathy.** Same.
3. **Foot drop — peroneal palsy vs L5, discriminated by ankle inversion.** Same. Note
   `11_07a` already carries the raw anatomy (tibial nerve does inversion), so the risk here
   is duplicating a discriminator that is implicit in an existing table.

Re-verify all three against `245c1e5`, **including the destination files**, and against
Corpus A **and** C, before writing D4's destination table.

## Lint sweep — clean

443 backticked marker tokens corpus-wide, **zero malformed**. The 37 non-parsing instances
are all the bare `` `UNVERIFIED` `` prose reference in Corpus B line 11 and one Corpus C
file. **No marker was silently voided in Block 1.**


---

# Week 2 run — Corpus B-new merge (2026-08-31, branch `claude/next-6gvrdi`)

## Resume point

**WEEK 2 COMPLETE** — K1 · K2 · K3 · K4 · I1 · I2 · I3 · I4 · I5 · O6 · CV-X. Eleven files.
**IN PROGRESS:** Week 3 — **L1–L8, RESP-X done.** Next O4. Remaining: L2–L8, RESP-X, O4/O5/O7, AN1, AU1. Then Week 5
ophthalmology (E1–E3). **Week 4 is approved for AFTER week 3**, priced by the probe in
`_meta/merges/WEEK4_PROBE.md` at ~100 additive blocks for 25 files; **run M before J** if
it is ever cut short.

**PR #88 covers this branch, not just week 2.** Week 3 commits extend it, because the
session is restricted to `claude/next-6gvrdi` and cannot open a second branch. If week 2
is wanted as its own reviewable unit, merge #88 before week 3 lands.
Then Week 3 (L1–L8, RESP-X, O4/O5/O7, AN1, AU1), then Week 5 ophthalmology (E1–E3).
**Do NOT start Week 4** — the user decides that after seeing this run's yield.

## Standing facts for a session picking this up

- **The 39 files in `Corpus B-new/` that duplicate a `Corpus B/` name are NOT merge
  material.** They are a pre-Step-11 re-export: byte-identical to `Corpus B` at
  `75ae3b9f^` once frontmatter and wikilink form are normalised. Leave them alone.
  Only the **73 new files** are in scope.
- **`merge_tools.py scan` re-stamps counter frontmatter on those 39 every run**, because
  they are `.md` files under the vault root. Revert them after each scan:
  `while read -r f; do git checkout -- "Corpus B-new/$f"; done < <(cd "Corpus B" && ls *.md)`

> [!danger] **THE TWO-COPIES TRAP — read this before searching or editing anything in
> `Corpus B-new/`.** Thirty-nine filenames now exist **twice in one vault**, in
> `Corpus B/` and `Corpus B-new/`, **with different content**. `A8_Foreign_Bodies_by_Site.md`
> is the clearest case: `Corpus B/` says *lidocaine* (Step 11's TGA-sourced correction) and
> `Corpus B-new/` says *lignocaine* (the pre-Step-11 export). Same filename, opposite side
> of a sourced rename.
>
> Consequences to keep in mind while both exist:
> - **A vault-wide grep returns both copies**, so a hit count over `Corpus B*` double-counts,
>   and reading only the first hit can return the reverted text.
> - **An Obsidian wikilink resolves by filename**, so `[[A8_Foreign_Bodies_by_Site]]` is
>   ambiguous and which copy opens is not something this vault decides.
> - **Any tool taking `--dir` at the vault root walks both.** That is why `scan` keeps
>   stamping them.
>
> **The 39 are being kept deliberately, pending a deletion decision.** Until then: scope
> every search to `Corpus A`, `Corpus C` and the **73 new files**, never to `Corpus B-new`
> as a whole, and never treat a `Corpus B-new` copy of a Corpus B filename as current.
- The 73 carry `trust: unverified`; `population` is corrected per file only for the week
  being merged, and stays at the tool's `mixed` placeholder otherwise.
- Step 31 has been run on the 73: 3064 links expanded, 0 unresolved.

## NO-BASELINE test — the scope that is correct

`git archive 0db4034 | tar -x` produces the **whole repository**, including **Corpus B —
the merge source** — and the root project documents. Testing a subject against all of it
suppresses a marker on the ground that the *source* mentions the subject.

**Restrict every base-A test to `Corpus A` and `Corpus C`.** `paronychia` is the proof:
1 hit across the full archive, 0 in the inherited layer.

## Yield so far

| File | Tested | Additive | Discard | Conflicts | New files |
|---|---:|---:|---:|---:|---|
| K1 Fever Workup | 55 | 15 | 39 | 1 (CF-035 R2) | none |
| K2 Skin and Soft Tissue Infection | 42 | 13 | 28 | 0 | none |
| K3 Exposure, TB, HIV, Immunodeficiency | 48 | 7 | 40 | 0 | none |
| K4 Allergy and Clinical Immunology | 38 | 10 | 25 | 0 | none |
| I1 Thyroid Disease | 32 | 2 | 30 | 0 | none |
| I2 Diabetes and Glucose Disorders | 34 | 4 | 30 | 0 | none |
| I3 Calcium, Parathyroid and Bone | 26 | 2 | 23 | 0 | none |
| I4 Pituitary, Adrenal and Sex Hormone | 30 | 1 | 29 | 0 | none |
| I5 Weight, Lipids and Fluid Balance | 30 | 3 | 27 | 0 | none |
| O6 Sexual and Reproductive Health | 34 | 2 | 32 | 0 | none |
| CV-X Chronic Heart Failure | 28 | 2 | 26 | 0 | none |
| **WEEK 2 TOTAL (11 files)** | **382** | **56** | **329** | **1 (CF-035 R2)** | **none** |
| — *week 3 below* — | | | | | |
| L1 Hot and Swollen Joint | 30 | 3 | 27 | 0 | none |
| L2 Polyarthralgia and Inflammatory Arthritis | 31 | 1 | 30 | 0 | none |
| L3 Muscle Symptoms and Widespread Pain | 26 | 2 | 24 | 0 | none |
| L4 Back and Neck Pain | 28 | 1 | 27 | 0 | none |
| L5 Regional Limb Pain | 34 | 3 | 31 | 0 | none |
| L6 Soft Tissue Injury and Mobility | 24 | 3 | 20 | 1 (CF-036 R2) | none |
| L7 Fractures and Eponyms | 26 | 1 | 25 | 0 | none |
| L8 Facial, Head and Torso Trauma | 28 | 2 | 26 | 0 | none |
| RESP-X Occupational and Chronic Lung Disease | 26 | 1 | 25 | 0 | none |

**Week 2 ran 15% additive overall** (56 of 385 dispositions), against the ~20% of blocks
1 and 2. Corpus A + Corpus C together are **denser** in week 2's topics than the
file-count indicator suggested, not thinner.

**The K block ran ~26% additive. I1 ran 6%.**

> [!danger] **The endocrine yield indicator I gave the user was WRONG, and the error is
> reusable.** I predicted endocrine would be week 2's richest seam because Corpus A has
> **one** `06_` file against five new `I` files. **That indicator counted Corpus A
> filenames only.** Thyroid content is spread over `06_Metabolic`, `05_Ophthalmology`
> (thyroid eye disease, own section), `15_16a`, `15_17a`, `16_08-09`, `13_06a` — and
> above all **`Corpus C/NEW_Investigations_Endocrine.md`**, which carries the TFT pattern
> table, TIRADS, Bethesda and the uptake-scan logic. **A file count over one corpus is
> not a coverage measure.** Expect I2–I5 to run low too, for the same reason: Corpus C
> has a dedicated investigations file per specialty.

**Eight unanchored-substring traps so far this run**, none of which was on the user's
known-collisions list: `felon`→`lifelong` (66/66) · `IGRA`→`migraine` (118/125) ·
`PrEP`→`preparation` (~98/113) · `IRIS`→the eye (18/22) · `Gell`→`Shigella`/`flagellin`
(9/9) · `TRAb`→`trabecular`/`strabismus` (28/32) · `LADA`→`maladaptive` (6/6) · `Conn`→`connective` (123/123). **Treat any short unanchored pattern as
suspect by default; a list of known-bad ones will always be behind.**

## Next free conflict ID: **CF-036.** (CF-035 is the atelectasis conflict written this run.)

## A verification defect found mid-run (rule 7) — FIXED, and the correct form

Every merge until I5 ended with this duplicate-header check:

```
grep -n "^#\+ " FILE | awk -F: '{print $3}' | sort | uniq -d      # VACUOUS - DO NOT USE
```

`grep -n` prefixes the line number, so `$2` is the header text **up to its first colon**
and `$3` is whatever follows a second one. For a colon-free header `$3` is **empty**, so
every such header maps to the empty string and `uniq -d` prints one blank line — which
reads as "no duplicates". Proven, not reasoned:

```
$ printf '10:## Alpha\n20:## Alpha\n' | awk -F: '{print $3}' | sort | uniq -d | cat -A
$
```

Two identical headers, one empty line. **Use this instead:**

```
grep -h "^#\+ " FILE | sort | uniq -d
```

Re-run correctly over all eleven Corpus A files modified this run: **all clean.** No
duplicate header was introduced; only the check was broken.

## Open for the user — a pre-existing duplicate header

`12_01_Rheum` has **`### Management` twice**, at `:37` (rheumatoid arthritis) and `:150`
(psoriatic arthritis). **Present at `f6bfb05`, before this run** — not introduced by any
merge. It is the first genuine duplicate the *corrected* duplicate-header check has caught,
which is some evidence the corrected check works.

**Not fixed:** renaming a heading is not an additive merge, it changes an anchor, and
CLAUDE.md forbids renumbering file sections. No other file currently points at either
anchor (checked). Left for a decision.

## A practice change for the rest of this run

**Stop piping `gapcheck.py` output through `cut -c` or `head`.** Three near-misses in week 3
came from exactly that — `RICE` cut off by `head -4` (L6, would have merged a conflict as an
addition) and the obesity-hypoventilation bicarbonate screen cut off by `cut -c1-190`
(RESP-X, would have merged a duplicate). **`gapcheck.py` cannot truncate; a filter
downstream of it can.** Use `grep -c` for a count, or grep for a distinctive substring and
print the whole line.
