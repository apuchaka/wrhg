---
title: Merge Specification — Corpus A / B / C consolidation
status: DRAFT FOR APPROVAL — do not execute
date: 2026-08-30
---

# Merge Specification

## 0. Premises, corrected by inspection of the samples

Four things found in your files change the starting assumptions.

**Trust is not binary.** `03_Gastrointestinal` §0.18 recommends `co-amoxiclav + metronidazole` as appendicectomy prophylaxis. That is UK naming and a UK regimen, unflagged, in the layer you called trusted, and no verification box covers the Mx block. `furosemide` appears twice, `co-amoxiclav` twice. Corpus A contains unreviewed UK-inherited content that has simply never been looked at. A two-value scheme (verified / unverified) would silently promote this to "verified" on merge.

**Your existing verification boxes record the fact of verification but not its scope.** `15_01a` demonstrates the failure in its own words: the top box confirms ANZCOR doses match, then a correction below records that the adrenaline *timing* was UK/ERC and wrong, noting "a reader has no way to tell that the box covers one dimension of the table and not the other." Scope is the missing field, and it is the single highest-value change in this spec.

**Paediatric content is mixed into adult files.** 34 paediatric signals in `03_Gastrointestinal` alone — the paracetamol nomogram branches at <40kg, autoimmune hepatitis type II is children-only, appendicitis imaging carries a radiation caveat. A file-level population field would be worse than none.

**B's cross-references are all broken.** 167 wikilinks to placeholder codes (`[[C4]]`, `[[F0.2]]`, `[[A9]]`, `[[O6]]`, `[[GER1]]`) with no counterpart in your vault. Both corpora also number sections `## 0.x` — A's GI file runs 0.1–0.42, C1 runs 0.1–0.10 — so any file-level merge collides immediately.

> [!danger] **CORRECTED 2026-08-30 — this paragraph was wrong, and it is where the error started.** It read "Corpus C is figure-free by design… **Zero doses across all five drug files**". There are **22** Corpus C drug files, not five, and **8 of them state a dose or dose-adjacent quantity** — the full ASCIA adrenaline table in `NEW_Drugs_01` (including the 7.5 kg injector floor that is B50), `hydrocortisone 100 mg IV` in `NEW_Drugs_10`, loperamide maxima, anti-D `500 IU`, pyridoxine thresholds, Hb transfusion triggers, vancomycin `AUC/MIC 400–600 mg·h/L`. The claim was a generalisation from a five-file sample and it propagated into CLAUDE.md §1.6 and the Step 26/28 tables, all now corrected. **Most of C abstains; some of it does not. `figures: none` is a per-file finding, never a corpus-wide assumption.**

**C is not purely reference material.** `NEW_ENT_and_Oral.md` is a clinical topic file (`block: NEW build — Presentations & Symptoms`, TIER 2). C is three things — drug classes by AMH section, investigations by system, and some clinical topics — and only the first two are what you described.

**C's structure has three defects to handle at merge.** The entry schema (`D / Ind / Role / Normal / Abnormal / Alt`) is inconsistently applied: `D`, `Ind`, `Role` and `Alt` appear 64–65 times each, but `Normal` and `Abnormal` only 11 times. Content is misfiled across files — CSF studies, Coombs testing, G-CSF and rubella/varicella serology all sit in the *Gastroenterology* investigations file, and §0.36 is self-labelled "OUT OF SCOPE, built in error". And at least one threshold set carries a US source attribution — the R-ratio "(ACG definition)" — unflagged in an AU corpus.

**A third linking convention.** `[CORRECTED 2026-08-30 — the counts below were generalised from a five-file sample; measured across all 53, C holds **195** wikilinks (all resolving) and **276** backticked file references, not 42 and 65. Same sampling error as the figure-free claim at line 21.]` A uses wikilinks to filenames. B uses wikilinks to placeholder codes. C uses both: 42 wikilinks that correctly resolve to real A filenames, plus 65 backticked file references (`` `NEW_Drugs_03_Analgesics.md` 0.3.4 ``) that Obsidian will not link. C integrates far more cleanly than B on this axis.

---

## 1. Provenance convention

### Options

**(a) Frontmatter only.** One `source:` field per file, as now. Cheap, survives everything, invisible while reading. Fails the stated requirement outright — a single section will contain both trust levels.

**(b) Callout types only.** Matches your existing style. But Obsidian callouts are block-level: they cannot mark a claim inside a table cell, mid-sentence, or inside a list item, which is exactly where doses live. Your ALS table is the proof — the wrong adrenaline timing was inside a table cell that no callout could have marked. Also `[!info]` is already used 40 times across six files for ordinary explanatory content, so it greps as noise.

**(c) Inline tokens only.** Works anywhere including table cells, survives any edit that doesn't delete the line, greps perfectly. Corpus B already uses one: `` `UNVERIFIED — what to check.` ``, written 75 times across the seven files, rendering as inline code — visually distinct without being loud. Weakness: no file-level orientation, and marking every verified claim individually would be exhausting to write and to read.

**(d) Tags.** `#unverified` gives you a free index in Obsidian's tag pane with no scripting. But tags mid-sentence render awkwardly, pollute the global tag pane, and can't carry a scope description without becoming unwieldy.

### Recommendation — three layers, each doing one job

**Layer 1, frontmatter — sets the file's default trust.** Three values, because trust is not binary:

```yaml
trust: verified        # every clinical claim checked against a named AU source
trust: inherited       # Corpus A default — plausible, in use, never systematically checked
trust: unverified      # Corpus B default — model knowledge
trust: snippet         # Corpus C default — AMH/guideline-derived via snippets, figures deliberately omitted
population: adult      # adult | paed | mixed
figures: none          # optional — set ONLY after reading that file and finding no figure
```

`snippet` sits between `inherited` and `unverified`: the prose derives from named Australian sources but was not read in full, and the file abstains from figures rather than guessing them. The `figures: none` flag is what tells the drift script it can skip the file entirely, and what tells future-you not to "helpfully" add a dose.

Every current Corpus A file is `inherited` until audited, **not** `verified`. This is the change that stops the co-amoxiclav problem propagating. Files earn `verified` only when a scoped check has covered them.

**Layer 2, inline token — marks claims that deviate from the file default.** Keep B's existing syntax and add its converse:

```
`UNVERIFIED — the scope of what needs checking.`
`VERIFIED eTG 2026-08 — dose and frequency.`
`CONFLICT CF-012`
`[paed]` `[adult]`
`→MED:adrenaline`
```

All backtick-delimited, all greppable with one pattern, all legal inside table cells and mid-sentence. You only write these where the claim differs from the file default, so a `trust: verified` file carries few or no `VERIFIED` tokens and an `unverified` file carries few or no `UNVERIFIED` tokens — the markers stay rare enough to keep meaning something.

**Layer 3, verification record callout — one per file or per major section, with mandatory scope.** Use `> [!check]`, a real Obsidian callout type currently unused in your corpus, so it greps clean unlike `[!info]`:

```markdown
> [!check] VERIFIED — ANZCOR Guideline 12.2, Aug 2026
> **Checked:** adrenaline dose, amiodarone dose, defibrillation energy.
> **NOT checked:** drug timing relative to shock number, sequencing, 4Hs/4Ts wording.
```

The `NOT checked` line is mandatory and may not be omitted or left empty. If you genuinely checked everything, write `NOT checked: nil`. This single field is what would have caught the adrenaline error.

**Default rule:** an unmarked claim inherits its file's frontmatter `trust`. Absence of a marker never means verified.

Costs: you are adding a discipline that must be maintained by hand, and the `NOT checked` field is the one people skip when tired. Mitigation is in §6 — a linter that fails any `[!check]` callout missing the field.

---

## 2. Conflict handling

### Options

**(a) Inline only.** Flag where the claims disagree. Maximally visible at point of reading, invisible as a worklist.

**(b) Central log only.** `CONFLICTS.md` with entries. Reviewable as a queue, but the conflict is invisible when you read the topic — you can be misled by a claim whose contested status is recorded in a file you aren't looking at.

**(c) Inline authoritative, central index generated.** Both properties, one source of truth.

### Recommendation — (c), with graduated weight for study-time resolution

The inline marker is the record. The central file is generated from it and never hand-edited.

#### Three weights, by risk tier

Conflicts appear at the point of disagreement, but not all at the same visual cost. A `[!fail]` block on every discrepancy would make the corpus unreadable, which is the failure mode you named at the outset.

**R1 — expanded, above the claim.** You must not read the claim unwarned.

```markdown
> [!fail] CONFLICT CF-004 — adrenaline dose, adult vs paed **R1**
> **A (`inherited`):** ...
> **B (`unverified`):** ...
> **Resolve against:** ANZCOR 12.2.
```

**R2 — collapsed, above the claim.** One line until you open it. The `-` suffix is Obsidian's default-collapsed syntax.

```markdown
> [!fail]- CONFLICT CF-012 — imaging pathway **R2**
> **A (`inherited`):** ultrasound not useful for visualising the appendix...
> **B (`unverified`):** ultrasound first-line in children, young women, pregnancy...
> **Resolve against:** TG Acute appendicitis; RCH imaging guidance.
```

**R3 — inline token only, detail in the generated index.**

```markdown
...recurrence risk 12–24% `CF-031` ...
```

#### Resolution stamps — designed to be written in fifteen seconds, on a phone

Closing a conflict properly (rewriting the block into a `[!check]` with a scope line) takes a couple of minutes and will not happen mid-study. So separate the **verdict** from the **cleanup**.

Append one line inside the conflict block. Four forms, all greppable:

```
> **RESOLVED 2026-09-14 A — TG Acute appendicitis.** B's US claim correct; A's line to be deleted.
> **RESOLVED 2026-09-14 B — RCH CPG Appendicitis.**
> **RESOLVED 2026-09-14 NEITHER — TG.** Both wrong; correct answer is X.
> **DEFERRED 2026-09-14 — TG silent, needs surgical reg.**
```

Grammar: `RESOLVED|DEFERRED`, ISO date, verdict (`A`/`B`/`NEITHER`), source, optional note. The verdict is what the script reads; the note is for you.

**The stamp does not require you to edit the claim text.** That is deliberate. The stamp sits adjacent to the claim, so a later reading gets the right answer from the stamp even before the text is fixed. Text cleanup batches into a separate pass when you have a laptop and twenty minutes. This is what makes partial progress genuinely useful rather than half-done.

`DEFERRED` matters as much as `RESOLVED` — it stops you re-opening the same unresolvable conflict every time you revise the topic. Deferred items move to a separate section of the index rather than disappearing.

#### Knowing before you read

Script-maintained frontmatter, so opening a file tells you its state:

```yaml
conflicts_open: 3
conflicts_r1: 1
```

If `conflicts_r1` is non-zero, that file is not safe to revise from until you have dealt with it. This is the single most useful line in the frontmatter for exam purposes.

#### The generated index

`_meta/CONFLICTS.md`, regenerated from the inline blocks, grouped by file and sorted R1 first, with resolved and deferred items in separate sections. Because it is derived, it cannot drift. Because conflicts are also inline, you never depend on opening it.

**Never auto-resolve.** Both claims survive in the merged text, both attributed, until you stamp a verdict. Deleting a claim without a resolution note is prohibited — the deletion is unreviewable in six weeks.

ID scheme: `CF-###`, sequential, never reused. Your existing `PENDING_GUIDELINE_CHECKS.md` uses `B##` IDs (B37, B39, B42, B45, B56); leave those untouched and keep `CF-` distinct so nothing collides with "Corpus B".

---

## 3. Overlap and duplication

### Options

**(a) B supersedes A where B is broader.** Wrong direction. Trades verified content for unverified content on the grounds of length.

**(b) Interleave into continuous prose.** Reads best. Worst possible reviewability: the diff is unreadable, provenance blurs at every sentence boundary, and you cannot later separate the layers if B turns out to be wrong about something systematic.

**(c) Keep both files, cross-link.** Zero merge cost, and gives you two files per topic that drift apart immediately. This is the state you already have and want to leave.

**(d) A supersedes on any claim A covers; B contributes only what A lacks.**

### Recommendation — (d), with structural separation

**One owner per fact.** Where A and B state the same fact, A's version stays and B's is discarded — not appended, not footnoted. Where B is genuinely richer on a claim A also covers (B's atypical appendix positions versus A's single psoas-sign line), A's claim stays and B's additional material is added as new content, not as a competing statement of the same claim.

**B's unique material enters as marked blocks, not woven prose.** Under the receiving A section, appended with a subheading and the file default overridden inline:

```markdown
### Added from unverified layer — atypical presentations
`UNVERIFIED — model knowledge, not source-checked.`
...content...
```

This keeps the git diff reviewable, keeps the boundary greppable, and means a later decision to strip the unverified layer entirely is a mechanical operation rather than a rewrite.

**Anti-drift mechanism — the owner registry.** A single generated file, `_meta/OWNERS.md`, mapping fact classes to their canonical location: adrenaline dosing → `Medications_Reference.md`; Alvarado score → `03_Gastrointestinal §0.18`; paediatric anaphylaxis observation thresholds → `15_01b`. Any second appearance of an owned fact must carry a mirror token (§5). Facts appear twice at most: once at the owner, once as a marked mirror. Three appearances is a spec violation the linter reports.

---

## 4. Investigations — where they live

*Finalised against the Corpus C samples.*

### The problem restated

Three layers already write about investigations, in three different registers:

- **A and B, inline at the condition** — `(*why:* ...; *what:* ...)` per test, condition-specific reasoning. "Order LFTs in PSC because the disproportionate ALP/GGT rise is the hallmark cholestatic picture."
- **C's investigation files** — a fixed schema per test: `D` (what it is), `Ind` (generic indications), `Role` (first-line or adjunct), `Normal` / `Abnormal` (pattern interpretation), `Alt` (what else to consider).
- **The laboratory** — actual reference intervals, which C deliberately declines to state and which are correctly absent from all three corpora.

The overlap that looked threatening is C's `Ind:` field against A/B's inline `*why:*`. On inspection they are different granularities, not duplicates. C's `Ind:` for LFTs is a generic list — suspected liver disease, jaundice, abdominal pain, monitoring hepatotoxic drugs. A's `*why:*` for LFTs in PSC is disease-specific reasoning. Neither substitutes for the other, and neither contains a figure that can drift.

### Options

**(a) Collapse into C, condition files carry pointers only.** Destroys the condition-specific reasoning, which is the most exam-useful content you have, and forces navigation on every read. Reject.

**(b) Duplicate freely.** Unnecessary — the two registers are not duplicates in the first place. Reject.

**(c) Split by register, no numeric duplication.**

### Recommendation — (c)

**Condition files own "which test, and why, in this disease."** Keep the inline `(*why:*; *what:*)` form exactly as A and B already write it. It is compact, reasoning-bearing, and works in both your reading modes without navigation.

**C's investigation files own "what this test is and how to read it."** The schema stays. This is the layer you consult when you have a result and don't know what it means, which is a different moment from choosing a test.

**Nobody owns reference intervals.** C's abstention is correct and should be adopted corpus-wide as policy, not treated as a gap. Where a range is genuinely needed for exam recall, it goes in C's `Normal:` field with an explicit lab-variability note, and nowhere else.

Because the layers hold different content types, there is no mirror obligation and no drift script needed for investigations. The `→IX:` token from §1 is therefore **withdrawn** — it would be marking a duplication that doesn't exist.

### Corpus C remediation, in priority order

1. **Refile misplaced entries.** CSF studies, Coombs, G-CSF and rubella/varicella serology move out of `NEW_Investigations_Gastroenterology.md` into their correct system files. Delete §0.36, which is self-labelled as built in error. ~30 min, mechanical, do it before any cross-referencing so links are written once.
2. **Flag the non-AU attributions.** The R-ratio "(ACG definition)" is American. Mark `` `UNVERIFIED — AU source for R-ratio cut-points; check RCPA or eTG.` `` **R2**. Sweep C for other non-AU attributions in the same pass.
3. **Do not backfill the missing `Normal:`/`Abnormal:` fields.** They are absent from 53 of 64 entries, and filling them from memory is exactly how unverified figures enter a corpus that has so far succeeded in keeping them out. Leave the schema partial and honest.

---

## 5. Medicines — where they live

*Rewritten after reading `Medications_Reference.md`. My earlier recommendation was wrong.*

### Why the original design fails

I proposed `Medications_Reference.md` as the canonical owner of every dose. It cannot be:

- It contains **two entries** (antiarrhythmics, beta-blockers). Endocrine, Neurological, Psychotropic, Analgesia, Anti-infective and Other are bare headings.
- It states **no doses at all**, on the same abstention policy as Corpus C — snippet-sourced, three agreeing sources required for any figure, disagreements recorded rather than resolved.
- Its own scope note forbids the role: *"Nothing was moved here. Drug content that already lived in organ-system files before this file existed stays where it is. This file is additive only, so no cross-reference anywhere else in the corpus was broken to create it."*

So dosing lives distributed across organ-system files, by deliberate design, to avoid breaking cross-references.

### The failure mode is already documented in your own tracker

`PENDING_GUIDELINE_CHECKS.md` **B50** records exactly the drift this section was meant to prevent, already realised: `01_Cardiovascular` and `15_01b` both point at `09_01` as *owner* of the ASCIA adrenaline table; the table stopped at 7.5 kg; the only figure for the band below it sat in `01_Cardiovascular` — the file that defers. A reader following the pointer for an infant reached a table that did not cover them. B43 is described as the same shape.

**This is evidence against pointer-only ownership**, not for it. A pointer to an owner that turns out to be incomplete is worse than a local figure, because the reader has no signal that the pointer failed.

### Revised recommendation — declared ownership, not relocated ownership

Do not move doses. Moving them would break cross-references, which is the exact thing `Medications_Reference.md` was designed to avoid.

Instead, **declare** ownership where the dose already lives:

1. **An owner registry**, `_meta/OWNERS.md`, generated and hand-corrected: drug → population → the file and section that owns that figure. `09_01` owns the ASCIA adrenaline table; `01_Cardiovascular` does not.
2. **Mirrors stay marked** with `` `→MED:name` ``, but the token names the owning *file*, not `Medications_Reference.md`.
3. **Owner completeness is checkable.** The B50 failure is detectable: an owner table whose bands do not cover the range its dependants reference. Any pointer into an owner table should state the range the table covers, so an out-of-range reader is warned rather than silently unserved.
4. **`Medications_Reference.md` keeps its actual role** — therapeutic-class pharmacology, mechanism, selectivity, class traps. It is a *class reference*, not a dose reference, and its empty section headings should be understood as scope not yet built rather than owner slots waiting to be filled.

### Do not consolidate dosing before the MCQ

Distributed dosing with a declared registry is imperfect but stable. Relocating dose figures across 150 files four weeks before an exam risks breaking cross-references that currently work, in exchange for tidiness. The drift check (§11.2) works on declared owners without anything moving.

---

## 6. The UNVERIFIED backlog

*Rewritten after reading `PENDING_GUIDELINE_CHECKS.md`. Do not build a parallel queue.*

### What already exists

`PENDING_GUIDELINE_CHECKS.md` is a mature tracker: ~57KB, 65 rows, four sections —
A (pending guideline releases), B (jurisdiction-variable), C (source-currency spot-audit),
D (content built under egress limitation) — plus a documented known-limitations section.
It has an append-never-delete protocol: *"Do not delete rows when resolved. Mark them, with
the date and what changed. A resolved row is the record that the check was actually done."*

It feeds Step 14 and Step 20 of `MASTER_VERIFICATION_WORKFLOW.md`.

**This is better than the generated queue I proposed.** It carries reasoning, not just
locations; it distinguishes "pending release" from "genuinely variable" from
"egress-blocked", which a marker scan cannot infer; and its rows record what was already
settled so it is not rechecked.

### Revised recommendation

- **The scan does not write `PENDING_GUIDELINE_CHECKS.md`.** A script that rewrote a file
  with a manual ID sequence and an append-never-delete history could destroy the record of
  which checks were actually done. `merge_tools.py scan` emits
  `_meta/PENDING_ROWS_DRAFT.md` — R1 rows in that file's table format, with IDs left blank
  for manual assignment. You paste; the script never touches the tracker.
- **`_meta/VERIFICATION_QUEUE.md` is demoted** to a working view of inline markers in the
  B and C layers only. It is scratch, not a record. The tracker remains the record.
- **ID sequence continues the existing one.** `B##` for tracker rows; `CF-###` for merge
  conflicts, which are a different kind of object — a disagreement between two corpora
  rather than a guideline to re-check. Where a conflict resolves into a guideline check,
  it graduates into the tracker with a new `B##` and the `CF-` block cites it.

### Risk tiering

The tracker does not tier by clinical risk. The scan's R1/R2/R3 assignment (§1) can suggest
one, but the tracker's own ordering — Section A first, because those name guidelines that
did not exist in final form — reflects a judgement a regex cannot make. **Read Section A
before the MCQ regardless of what the scan says.**

---

## 7. Naming and structure

**Filenames are the only link-breaking surface, and A's filenames are load-bearing.** Never rename a Corpus A file. Every existing `[[wikilink]]` targets a filename with no heading anchor, so heading edits and renumbering are free while renames are expensive.

**B's files.** Two dispositions, decided per file:

- *Merges into an existing A file* — content moves into A's sections under §3's rules, B's file is deleted. Preferred where A already owns the topic. C1 §0.6 appendicitis merges into `03_Gastrointestinal` §0.18.
- *Becomes a new file* — where B covers something A lacks entirely. Named to A's scheme: `NN_Block_-_Topic.md`, taking the next free number in the relevant block. `C1_Acute_Abdomen.md` is a plausible standalone as `03b_Gastrointestinal_-_Acute_Abdomen_Presentations.md`, since A is disease-organised and B is presentation-organised — genuinely complementary rather than duplicative.

**B's 167 broken wikilinks.** Do not guess targets. Strip each to plain text with a marker: `[[C4]]` → `` `TODO:link — GI bleeding` ``. Guessing produces links that look correct and go to the wrong place, which is worse than no link. Repair them opportunistically later; a stripped link costs you nothing while reading, a wrong link costs you trust in the whole system.

**Creating new files from Corpus B.** Not every B section has an A home, but far more of them do than the file names suggest — Corpus A is not purely disease-organised. It contains investigation, history-taking and examination files, and even within disease files there are presentation-type sections: `03_Gastrointestinal` §0.41 is "Abdominal Pain — Regional Anatomy and DDx", which is precisely the kind of content a naive rule would send to a new file.

The test, applied per B section, **in this order**:

1. **Search `_meta/HEADINGS.md` across the whole vault first.** If any heading anywhere plausibly owns the content, that is the destination — regardless of which file it sits in or what that file is nominally about. Creating a new file for content that already has a home is the most damaging error available here, because nothing detects it afterwards.
2. Only if the search returns nothing: **describes a disease or condition** → append into the A file that owns the adjacent material.
3. Only if the search returns nothing: **describes a presentation, approach or symptom** → new file, A's naming scheme, next free number in the relevant block.

### The heading manifest

`_meta/HEADINGS.md`, generated by one command over the vault:

```bash
for f in *.md; do echo "## $f"; grep -n '^#\{2,3\} ' "$f" | sed 's/:#\{2,3\} / · /;s/^/- L/'; echo; done > _meta/HEADINGS.md
```

Roughly 4,000 lines for ~240 files; regenerate whenever files change. It does three jobs, which is why it is built before C integration rather than alongside the merge:

- **Destination lookup** — step 1 above.
- **Generation context** — paste the relevant system's slice (~40 lines) into a session generating new B files, with the instruction to write only what is not already covered. Prevents conflicts at source.
- **Overlap reporting** — match an existing B file's headings against the manifest before merging it, to see how much is genuine new content and how much is overlap. Mechanical term-matching, no judgement required, and it tells you the size of a merge session before you start it.

For the 37 B files already generated, only the third use applies; they go through normal adjudication. Regenerating them against the manifest would cost more than the conflict resolution it saves.

This yields a deliberate two-axis corpus: disease files inherited from A, presentation files contributed by B. That is closer to how clinical exams actually work — patients present with right iliac fossa pain, not with appendicitis — and is particularly useful for OSCE preparation.

**The failure mode to watch:** a presentation file restating disease content. `C1_Acute_Abdomen` §0.6 carries a substantial appendicitis entry that overlaps `03_Gastrointestinal` §0.18. The rule is that **the presentation file owns the approach, the discriminators and the differential; the disease file owns D/R/A/P/S/Ix/Mx.** The presentation file points rather than copies. Without this, a single fact acquires three homes and the owner registry stops meaning anything.

**Corpus C's files.** Keep them as standalone files — they are a reference layer, not topic content, and merging them into condition files would destroy the property that makes them useful. Three jobs: rename to a scheme that sorts alongside A (the `NEW_` prefix is a build artefact, not a category), refile the misplaced entries per §4, and convert the 65 backticked file references to real wikilinks so navigation works. C's existing 42 wikilinks already resolve correctly and need no work — a useful contrast with B, and a reason to do C's integration before B's.

**Section numbering.** All three corpora use `## 0.x` — the `0.` is an unfilled placeholder in both, and nothing anywhere references a section number. It is therefore cosmetic and free to change. Renumber per-file at the very end, or never. Do not do it now; it produces enormous diffs that hide substantive changes.

---

## 8. Adult vs paediatric

This is a second axis, orthogonal to provenance, and it needs its own notation. A source-verified adult eTG threshold is fully trustworthy and completely wrong for a four-year-old, so provenance markers cannot carry population and the two must stay visually and grepably distinct. If they share notation you will learn to skim past both.

**Frontmatter `population: adult | paed | mixed`** for orientation. `03_Gastrointestinal` is `mixed`, not `adult`, on the evidence of its 34 paediatric signals.

**Inline `[paed]` / `[adult]` tokens** on any dose, threshold or pathway that differs by population, wherever it appears. Only on claims that actually differ — marking universally would be noise.

**Rule for adult files carrying paed figures.** Your instinct in Corpus A is already right and inconsistently applied: `15_01b` points to `09_01_Dermatology` for the full ASCIA dose table but *also* states 150mcg/300mcg itself, which is exactly the mirror situation. Formalise it — an adult file may state a paediatric figure only as a marked mirror with the paed owner named, or may state a pointer only. Never an unmarked bare figure.

**The paediatric sweep.** Grep non-paeds files for `mg/kg`, `/kg`, `neonat`, `infant`, `child`, `adolescen`, `months old`, `years old`, plus paed-specific terms. Every hit gets a population token or a pointer. In `03_Gastrointestinal` that is 34 lines, so roughly a 45-minute pass per large file. Prioritise files where a paed figure could be acted on: toxicology, emergency, infection.

---

## 9. Order of operations

Ordered so that stopping at any point leaves you better off than when you started. Rough estimates against your ~3h/week.

| # | Step | Time | Value if you stop here |
|---|---|---|---|
| 1 | Git branch. Tag current HEAD as `pre-merge`. | 10 min | Full rollback available |
| 2 | Write `_meta/CONVENTIONS.md` — the marker vocabulary from §1, one page | 45 min | The convention exists and is citable |
| 3 | Add `trust:` and `population:` frontmatter to all ~187 files, scripted, defaults by corpus | 1 h | **Highest value per minute in the whole plan.** Every unverified file is now labelled as such, before any content moves |
| 3b | Generate `_meta/HEADINGS.md` | 10 min | Destination lookup, generation context and overlap reporting all become possible |
| 4 | Write the extract script — markers → queue, conflicts, linter | 2–3 h | Backlog becomes visible and prioritised; usable even with zero merging done |
| 5 | AU drug-naming pass across both corpora against a fixed vocabulary list | 1–2 h | Removes the highest-risk class of error, corpus-wide, cheaply |
| 6 | Paediatric sweep on the highest-risk files only (emergency, tox, infection) | 2 h | Population ambiguity gone where it could hurt |
| 7 | Merge one topic end-to-end as the pilot — appendicitis | 1 h | Proves or breaks the convention before you spend twenty hours on it |
| 8 | Merge remaining GI overlap, A-supersedes rule, B unique material as marked blocks | 4–6 h | One system fully consolidated |
| 9 | R1 verification queue items for weak systems | ongoing | Directly exam-relevant |
| 10 | Corpus C remediation across all 53 files — refile misplaced entries, delete built-in-error sections, flag non-AU attributions | 2–3 h | C becomes safe to cross-reference |
| 11 | Corpus C integration — rename, convert backticked refs to wikilinks, reciprocal pointers with `Medications_Reference.md` | 4–5 h | Reference layer navigable from condition files |
| 12 | Renumbering, link repair for B, cosmetics | — | Defer indefinitely |

**Do not do yet, deliberately:**

- Do not renumber sections. Cosmetic, enormous diffs, zero study value.
- Do not repair B's 167 links. Strip them and move on.
- Do not restructure investigations or medicines before the MCQ. Per §4 and §5 the restructure is now much smaller than feared, but it is still lower-yield than the labelling and naming passes.
- **Do not add NEW doses or reference ranges to Corpus C**, and do not treat C as figure-free: 8 of its 22 drug files already state one. Existing figures are scoped in place with the `NEW_Drugs_10` pattern, never deleted. Adding what looks like a missing figure is still the rule most likely to be broken by a well-meaning future session.
- Do not attempt to verify Corpus A's `inherited` content systematically. It is 150 files. Label it, sweep the R1 classes, and let the rest stay honestly labelled.
- Do not merge non-GI systems until the appendicitis pilot has survived a week of actual use.
- Do not delete anything from Corpus B until its content is either merged or explicitly rejected in a commit message.

---

## 10. What could go wrong

**The convention decays under time pressure.** You will be tired and you will write a dose without a mirror token. The linter catches mirrors and missing scope lines, but it cannot catch a fact you introduced with no marker at all. Partial mitigation only.

**`trust: inherited` becomes a permanent parking space.** 150 files labelled honestly and never audited. This is an acceptable failure — honest labelling is the point — but do not mistake it for progress on verification.

**The `NOT checked` field gets filled in carelessly.** "NOT checked: nil" written reflexively reintroduces the exact 15_01a failure with extra ceremony. The field only works if you are honest about the limits of what you actually looked at.

**Mirrors multiply faster than the script catches them.** The drift check depends on mirrors being marked. An unmarked duplicate is invisible to it, and unmarked duplicates are exactly what you produce when copying a line quickly.

**A-supersedes-B is wrong in a specific class of case.** Where A is inherited UK content and B happens to be right — the appendicitis ultrasound conflict may well be an instance — the rule prefers the wrong claim. The conflict marker is the safety net, but only fires where you notice the disagreement. Silent cases will exist.

**Study time gets consumed by tooling.** Steps 1–7 are roughly 8–10 hours, which at 3h/week is three weeks of your four before the MCQ. If study is losing, stop after step 5 and read; the labelled corpus is already much safer than the current one.

**The pilot invalidates the convention.** Possible and cheap to discover, which is why the pilot is step 7 and not step 12.

**Obsidian rendering.** `[!check]` and `[!fail]` are standard, but confirm they render in your theme before committing to them. Inline backtick tokens are safe everywhere.

**Merged files get very large.** `03_Gastrointestinal` is already 158KB; C1 adds 43KB. Obsidian handles it, mobile search may get slow, and a 200KB file is unpleasant to navigate. Splitting by presentation vs disease may become necessary.

**Corpus C's abstention gets eroded — and it was never as complete as this document claimed.** Most files say "no doses stated" and mean it; 8 of the 22 drug files do state doses. A later session fills in what looks like a gap, and the corpus that could be trusted to contain no half-remembered numbers stops being that. The `figures: none` flag is a weak

**C's partial schema invites backfilling.** 53 of 64 entries lack `Normal:` and `Abnormal:`. The pull to complete a visibly incomplete table is strong, and the only available filling material is model knowledge.

**Three linking conventions persist longer than planned.** A's wikilinks, B's placeholder codes, C's backticked references. If B's stripping and C's conversion don't both happen, you end up with a corpus where "how do I follow a reference" has no single answer.

**Git and Obsidian Sync conflict.** Running both on the same vault can produce sync conflicts mid-merge. Do scripted passes with sync paused.

---

## 11. Automation: what a pipeline can and cannot decide

### 11.1 The line

Automate **detection** and **additive merge**. Keep **adjudication** human.

The tempting formulation — "compare the content and use whichever is more accurate" — is not a computable operation. Accuracy is a relation between a claim and a source, and the sources that would settle these questions are the ones an automated agent cannot reach (§11.3). An LLM asked to adjudicate without a source will fall back on model knowledge, which is the exact process that produced Corpus B. The output would be Corpus B's epistemic status wearing Corpus A's labelling, with the conflict marker deleted. That is worse than the current state, because a visible disagreement is recoverable and a confident wrong resolution is not.

This is also the requirement the original brief opened with: *flagged for manual review, never auto-resolved*. It should survive contact with the time pressure.

### 11.2 What is safely automatable

**Supersession on provenance grounds.** Trust level is a computable property; clinical correctness is not. The rule set:

| A's claim | B's claim | Action | Automated? |
|---|---|---|---|
| `verified` | `unverified` | A wins, B discarded | Yes |
| `inherited` | `unverified` | `CONFLICT` marker written, both retained | Detection only |
| absent | present | Additive merge under a marked block, retains `unverified` | Yes |
| present | absent | No action | Yes |
| numeric figures differ | numeric | `CONFLICT`, risk-tiered, never auto-resolved | Detection only |
| non-numeric, compatible, non-overlapping | — | Additive merge under a marked block | Yes |

**A corollary worth stating explicitly: Corpus B can never win an automated comparison.** It carries no sources, so there is no provenance ground on which it beats anything. Where B turns out to be right — and it will be, in cases like the appendicitis ultrasound conflict — that is established by a human checking a guideline, after which the claim is `verified` and its origin is the guideline, not B.

**Other deterministic passes**, all safe, all scriptable, none requiring judgement:

- Frontmatter injection (`trust`, `population`, `figures`)
- Marker extraction → verification queue, conflict index, owner registry
- AU/UK drug-name vocabulary check against a fixed lookup table
- Paediatric signal sweep by regex
- Link integrity: broken wikilinks, unresolved `TODO:link`, backticked refs not yet converted
- Duplicate-figure detection: same drug, same population, different number
- Linter: `[!check]` blocks missing `NOT checked:`, facts appearing three or more times, mirrors disagreeing with canonical

**Additive merge is where most of the value is**, and it is safe for a structural reason: merged-in content keeps its `unverified` label, so a wrong addition is visible rather than laundered. It also degrades gracefully — a half-finished additive merge is a corpus with some gaps filled and nothing damaged.

### 11.3 The fact-checking pass, and its access problem

**Therapeutic Guidelines (formerly eTG complete) and AMH require individual or institutional subscription.** Your Flinders login reaches them; an automated agent does not. This creates a dangerous asymmetry: automated checking will succeed on openly published guidelines and fail on general therapeutics — which is precisely where dosing errors live. Worse, an unconstrained agent that cannot reach the AU source will find a UK or US one, and mark the claim verified. The AU-divergence risk gets laundered by the process designed to catch it.

**Mitigation — a hard source whitelist.** The agent may cite only from a fixed domain list. Openly accessible and genuinely useful:

- ANZCOR (resuscitation)
- ASCIA (anaphylaxis, allergy, immunodeficiency)
- RCH Melbourne Clinical Practice Guidelines, and state paediatric emergency guidelines (Queensland Children's Health, NSW ACI)
- Australian Immunisation Handbook and the NIP schedule
- PBS and TGA
- RACGP (partly member-gated — treat gated pages as unreachable, not as absent)

Rules the agent operates under:

1. **"Not found on whitelist" is a required and acceptable output.** It never triggers a fallback to open search or model knowledge.
2. **Never mark `verified` from a non-AU source.** A UK or US source may be recorded as corroboration in a conflict note; it does not close an item.
3. **Proposals, not edits.** For any clinical claim, the agent writes to `_meta/PROPOSED_CHANGES.md` — claim, current text, proposed text, source URL, date, and confidence. You approve. Deterministic passes (frontmatter, link stripping, drug-name flagging) may edit in place, because they carry no clinical judgement.
4. **Every `[!check]` the agent writes carries the mandatory `NOT checked:` field**, and the agent fills it honestly with the dimensions it did not examine.
5. **R1 items are never batch-approved.** R3 items may be.

This yields real coverage of resuscitation, anaphylaxis, paediatrics and immunisation — a substantial share of your R1 backlog — and honest silence on general therapeutics, where you open Therapeutic Guidelines yourself.

### 11.4 Claude Code setup

Your sequencing instinct is right. Specifics:

1. **Commit Corpus A untouched, tag it `base-A`.** Never amend that commit. It is the reference against which every later automated pass can be diffed and reverted.
2. **Put the conventions in `CLAUDE.md` at the repo root** — the marker vocabulary from §1, the supersession table from §11.2, the whitelist and rules from §11.3, and the do-not-do list from §9. You already have a `CLAUDE.md` with numbered rules (Corpus C cites "rule 8"), so extend it rather than starting a new one. An agent that re-reads the rules each session is the only thing keeping the convention alive across sessions.
3. **One pass per branch, one concern per pass.** `pass/frontmatter`, `pass/drug-names`, `pass/paed-sweep`, `pass/merge-gi`. A branch that does two things produces a diff you cannot review, and an unreviewed diff on clinical content is how errors enter.
4. **Add B and C incrementally, not all at once.** Two or three files per pass, reviewed, merged, then the next batch. This also gives you an early read on whether the convention survives contact with real content.
5. **Pause Obsidian Sync during scripted passes** to avoid sync conflicts mid-write.
6. **Every script writes a run log** to `_meta/runs/` — what it changed, in which files, how many. Inspectable after the fact, per your constraints.

### 11.5 Merge cadence — per-file merging, per-week adjudication

These are separate operations and should not be coupled.

**Merging is per B file.** Distribute an entire B file into its destination A sections (and any new presentation files) in a single pass, on a single branch. One review, one merge, and the B file is deleted at the end. Do not fragment a B file across weeks — partial consumption requires tracking state inside the file and produces a corpus where no one can tell what has been used.

**Adjudication is per week, per section.** Conflicts raised in sections you are not currently studying stay unresolved. That is what the markers exist for. Resolve the conflicts in the sections you are revising, while the clinical context is already loaded — this is the cheapest adjudication will ever be, and it is the main argument for merging alongside study rather than in a separate project.

**Backpressure applies per section, not per file:** do not revise from a section whose `conflicts_r1` count is non-zero until you have stamped a verdict on those items.

**Steering new B files — and why overlap should not be suppressed wholesale.** Where B files are still to be generated, give the session the relevant **headings manifest** slice (~40 lines). But the instruction should steer toward gaps, not forbid overlap, because overlap and disagreement are not the same thing and only one of them is expensive.

- **Suppress overlap on explanatory prose** — mechanism, pathophysiology, the reasoning behind a sign. A second rendering costs adjudication time and yields little, since divergence here is hard to adjudicate and rarely clinically consequential.
- **Welcome overlap on figures** — doses, thresholds, scores, timings, observation periods. A second rendering is cheap to compare (the numbers match or they don't) and a mismatch is free signal that something needs checking. With no automated access to Therapeutic Guidelines or AMH, an independent second rendering disagreeing with A is one of the few error-detection mechanisms available. The appendicitis imaging conflict (CF-012) exists only because B covered a topic A already had, and it surfaced a probable error in the `inherited` layer.

**Critical caveat: agreement between A and B is not corroboration.** B is model knowledge; A's UK-derived layer came from broadly similar material. They share ancestry, so concordance tells you about the ancestry rather than about the fact. A model asked about appendicectomy prophylaxis would very likely reproduce A's `co-amoxiclav + metronidazole` and agree perfectly, and that agreement would feel like verification while being worth nothing. **Concordance never closes a verification item. Only disagreement is informative, and only against a named AU source does anything become `verified`.**

### 11.6 The paediatric sweep as an automation candidate

This is the best-suited pass in the whole plan, because most of it is detection rather than judgement. The regex sweep (`mg/kg`, `/kg`, `neonat`, `infant`, `child`, `adolescen`, `months old`, `years old`, plus paed-specific terms) is deterministic. Classifying each hit as adult-figure, paed-figure, or population-neutral prose is mostly mechanical and can be agent-assisted with human review of the numeric hits only. Applying `[paed]` / `[adult]` tokens is then a scripted edit.

Run it after frontmatter injection and before any merging, so B and C content arrives into a corpus where population is already marked.
