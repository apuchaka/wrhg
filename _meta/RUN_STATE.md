---
name: run-state
description: Cross-session memory for the corpus merge. Session context does not carry over — this file and the Queue markers in MASTER_VERIFICATION_WORKFLOW.md are the only memory.
---

# RUN_STATE

## Night of 2026-08-30 — where things stand

| Branch | Step | Outcome |
|---|---|---|
| `claude/next-6gvrdi` | Parts 1–3: code fixes, queue reorder, Step 26/29 rewrites, CLAUDE.md rule 9 | ✅ merge first — the step branches are based on it |
| `phase/17-uk-localisation` | **Step 17** | ✅ 240 files · 33 terms · 71 hits · 3 genuine + 1 consistency fix |
| `phase/11-au-drug-naming` | **Step 11** | ✅ **halt cleared** — map rewritten with a source per entry against the TGA IHIN list; `frusemide`→`furosemide` reversed. **18 renames, 0 actionable hits remaining**, digit-invariance verified per file. The halt prevented 14 regressions. |

Full detail per step in `_meta/OVERNIGHT_REPORT.md`. **Step 28 not started** — deferred by
instruction pending review of these two reports.

**Queue order is 26, 17, 11, 28, 27, 29** (§1.1.9) — not numeric. **Items 1–3 (the whole
pre-MCQ block) are now done.** Step 28 is next and was deferred by instruction.

**Open, not resolved:** `PENDING_GUIDELINE_CHECKS.md` **B71** — the ASCIA adrenaline table
now has two owners and the 7.5 kg floor is duplicated. Resolve against ASCIA.
**Required in Step 28:** scope the 8 Corpus C files that state figures, using the
`NEW_Drugs_10` pattern (§1.34), never deletion.

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
