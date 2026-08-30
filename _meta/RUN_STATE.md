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

## Study-list additions — real absences no merge can close

Gaps confirmed absent from **all 240 corpus files** and **not supplied by the Corpus B
material that covered the surrounding topic**. They are recorded rather than written,
because the only available filling material is model knowledge.

| Topic | Absent from | Why it matters | Would be settled by |
|---|---|---|---|
| **Dubin-Johnson syndrome** | whole vault; C3 does not cover it | Conjugated hyperbilirubinaemia with an otherwise normal liver — the benign cause that must not be worked up as obstruction | RACGP, or a hepatology reference |
| **Rotor syndrome** | whole vault; C3 does not cover it | The same, and it is the standard exam pairing with Dubin-Johnson | as above |
| **Schatzki ring** | whole vault; C6 does not cover it | A specific lower-oesophageal ring causing intermittent solid dysphagia; `13_06b` §0.2 covers benign stricture generally but not this entity | RACGP, or a gastroenterology reference |

Both are hereditary conjugated hyperbilirubinaemias. The vault has Gilbert and
Crigler-Najjar (the **unconjugated** pair) but neither conjugated one, so the
classification at `03_Gastrointestinal` §0.41.8 is currently half-populated — which is
stated in that section rather than quietly filled.

