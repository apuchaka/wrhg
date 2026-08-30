# 1 Project Rules — Grind Time Intern Exam Notes

## 1.1 What this project is
Intern-level medical exam notes for Australian AMC-standard exams (MCQ 27 Sept 2026, OSCE 1 Nov, second MCQ 8 Nov). 148 content .md files, checklist.csv (872-row master topic checklist, 24 categories), and MASTER_VERIFICATION_WORKFLOW.md (the 26-step method and work queue).

Read MASTER_VERIFICATION_WORKFLOW.md before any work. Read checklist.csv with `encoding='utf-8-sig'` — plain utf-8 breaks the first column header.

## 1.2 Target standard
Intern/RMO level. The test for any content: would a newly-graduated intern need this to recognise, explain, or act on something clinically? Not subspecialist depth. The workflow document's "Target standard" section has the full definition — follow it.

## 1.3 Non-negotiable working rules

1. **Verify before writing any cross-reference.** Check the target file's exact header text first. Never write a plausible-sounding section name and assume it exists.

2. **Zero grep hits is not proof of absence.** Check case-sensitivity, Unicode characters (α, β, ₂ subscripts), hyphenation variants, **markdown emphasis inside a word**, and alternate medical terminology before concluding content is missing. Historically most "missing" results have been search artifacts.
   - **The markdown case specifically:** this corpus bolds acronym expansions letter by letter — `**H**aemolysis, **E**levated **L**iver enzymes, **L**ow **P**latelets`. A search for `Haemolysis` finds nothing, because the literal text is `**H**aemolysis`. **Whenever a search for an acronym expansion returns zero hits, search again for a distinctive letter-run from the middle of the word** (`aemolysis`) before concluding the expansion is absent. The construction most likely to be searched for is the one least likely to be found.
   - Also never conclude absence from **truncated** output: a hit that was returned and cut off by a `cut`/`head` limit looks identical to no hit at all. View the full line.
   - **Rule 9 is this rule's inverse** — it covers the search that finds the *wrong* thing
     rather than nothing, and the file silently skipped before any search ran. A zero
     result can mean the term was absent, the spelling differed (this rule), or the file
     was never examined (rule 9).

3. **Every automated scan produces false positives.** Verify each hit manually against actual file content before treating it as a gap. Report dismissed artifacts alongside confirmed gaps — the ratio is the main signal of whether the run was careful.

4. **Scans also produce false negatives.** A template-completeness scan keyed on the presence of an S/Smx line cannot detect entries that lack one entirely. Build scans defensively and assume blind spots exist. If you find one, fix the scan and re-run affected items before continuing.

5. **In any paediatric entry, treat every absolute quantity as suspect.** Confirmed four times (2026-08-29): DKA maintenance fluid, DKA dextrose rate, paediatric nephrotic proteinuria, and the adrenaline band that stopped at 7.5kg. For any `g`, `mg`, `mL`, `mL/h` or `g/24h` figure in a paediatric file, **ask what it does at 10kg and at 50kg.** The correct paediatric forms are per-kg, per-m², per-age-band, or per-kg with an absolute cap — the corpus does this well where it does it at all (`40mg/kg (≤2g)`, `60mg/m²/day (max 80mg)`, the ASCIA and ANZCOR bands). **The defect is always an absolute figure standing alone**, because a number that is right for an adult survives being copied — nothing about it looks wrong in isolation. This applies to every round, not only paediatric ones: adult files carry paediatric content too.

6. **One fix at a time, one commit each.** After each fix: confirm no duplicate headers introduced, confirm all cross-references resolve. Commit with a descriptive message before moving on. Never batch unverified edits.

7. **Stop and report if you discover a limitation in your own method mid-run.** Do not continue applying a scan you've realised is flawed. This is more important than completing the phase.

8. **Report honestly.** "Clean against everything currently known to check for" — never "verified complete." This project's history is that every completeness claim was later disproven by a new technique.

9. **Substring matches create both false hits and silent false skips.** `child` matches
   `Child-Pugh`; `ALL` matches the English word "all" under a case-insensitive search;
   `paed` matches ortho**paed**ics; `ASCIA` matches f**ascia**; `epinephrine` matches
   nor**epinephrine**. **Rule 2 covers searches that find nothing; this covers searches
   that find the wrong thing** — and skip logic that excludes files with no error at all.
   Anchor on word boundaries or full paths.
   - **The two failure directions are not equally visible.** A false hit lands in a report
     and gets dismissed. A false skip produces nothing, and **a file missing from a scan
     looks identical to a file that came back clean.** Never write skip logic on a
     substring.
   - **Not every unanchored match is a defect.** `child`, `infant`, `gestation` and
     `pubert` fire inside *children*, *infants*, *gestational* and *puberty* — the same
     concept, and anchoring them would break them. The test is whether the longer word is
     a **different** concept.
   - Found three times in one week (2026-08-30). Treat it as a class: when one turns up,
     audit every containment test and unanchored alternative in the same tool, against the
     real corpus rather than by eye. That audit found two further instances nobody had
     noticed — `ASCIA` inside `fascia` on 33 lines, mis-routing verification items into
     the actionable queue, and `epinephrine` inside `norepinephrine`.

## 1.4 Reporting format
For each queue item: what was checked · scan hits produced · genuine gaps vs dismissed artifacts (with reasons) · fixes made with commit hashes · any limitation noticed in the method itself.

## 1.5 Content builds (Phase 2 of the queue) work differently
One topic per unit of work, not one category. Require a cited Australian source per topic (RACGP, Therapeutic Guidelines, state health guidelines, relevant college). Depth should match the existing notes, not be uniformly shallow.

---

## 1.6 Corpus merge — scope of the added material

Rules 1.1–1.5 above are unchanged and take precedence. **Rule numbering in §1.3 is
load-bearing** — Corpus C files cite "CLAUDE.md rule 8" by number. Never renumber them.

The project now holds three corpora, not one:

| Corpus | Files | Frontmatter `trust:` | What it is |
|---|---|---|---|
| **A** | ~148 | `inherited` | The original notes. Plausible, in use, never systematically checked. |
| **B** | 37 | `unverified` | Built from model knowledge. Every figure marked or omitted. |
| **C** | 53 | `snippet` | AMH/guideline-derived via snippets. **Inconsistent on figures — see below.** |

`verified` is reserved for content checked against a named Australian source, with its scope
recorded (§1.9).

> [!danger] **Corpus C is NOT reliably figure-free. Never assume it.**
> This table previously read "States no doses or reference ranges", generalised from five
> sample files. **It is wrong.** Checking all 22 Corpus C drug files, **8 state a dose or
> a dose-adjacent quantity** — among them the full ASCIA adrenaline table in
> `NEW_Drugs_01` (`0.01 mL/kg`, max `0.5 mg`, injector bands from **7.5 kg**),
> `hydrocortisone 100 mg IV` in `NEW_Drugs_10`, loperamide maxima, anti-D `500 IU`,
> pyridoxine thresholds, Hb transfusion triggers and vancomycin `AUC/MIC 400–600 mg·h/L`.
>
> **Most of C abstains; some of it does not.** `figures: none` is therefore a **per-file
> finding, established by reading that file** — never a corpus-wide assumption, and never
> inferred from C's provenance. Only 3 of the 22 drug files currently carry the key.
>
> **Where a C file states a dose, the fix is the `NEW_Drugs_10` pattern, not deletion:**
> ```
> > - **SURGERY:** hydrocortisone 100 mg IV at induction, then 200 mg per 24 hours…
> >   - **THESE TWO FIGURES ARE ADULT DOSES. DO NOT USE THEM IN A CHILD.** Paediatric
> >     cover is dosed by body weight or body surface area, not as a fixed adult quantity.
> ```
> That is rule 5 in its correct form, and it is the model for every dose already sitting
> in C.

**Corpus A is `inherited`, not `verified`.** Step 17's re-run found seven UK leftovers in
files an earlier sweep had already flagged, and `co-amoxiclav` still sits in
`03_Gastrointestinal` appendicectomy prophylaxis. Labelling A as verified would make that
content indistinguishable from checked content, which is the failure this whole exercise
exists to prevent.

Also set per file: `population: adult | paed | mixed`, `figures: none` where the file states
no numbers, and the script-maintained `conflicts_open` / `conflicts_r1` counters.

---

## 1.7 Inline markers

Backtick-delimited so they survive editing, work inside table cells, and grep cleanly:

```
`UNVERIFIED — what needs checking, and the source that would settle it.`
`VERIFIED <source> <YYYY-MM> — what was checked.`
`CF-012`                  conflict reference
`[paed]` `[adult]`        population scope
`→MED:adrenaline`         mirrors a figure owned elsewhere
`TODO:link — topic`       stripped placeholder link
`SRC:C1_Acute_Abdomen §0.6`  origin of an additive-merge block (§1.10)
```

Write a marker only where the claim differs from the file's frontmatter default.

**Every `UNVERIFIED` marker must name the source that would settle it.**
`` `UNVERIFIED — the dose.` `` cannot be triaged; `` `UNVERIFIED — dose, per ANZCOR 12.2.` ``
can be actioned immediately. Unsourced markers accumulate into a triage backlog.

---

## 1.8 Login-required sources — permanently noted, never queued

**Therapeutic Guidelines, AMH, AIDH and eviQ require an institutional login and will not be
consulted by anyone — agent or human.** Items only those sources could settle are
**permanently noted**. The marker stays in the file as a standing instruction to look it up
at the point of use, which is correct behaviour for dosing regardless.

Never delete a login-required marker. Never resolve one from memory, from a non-Australian
source, or on the grounds that two corpora agree.

**Open Australian sources remain usable and should be named:** ANZCOR, ASCIA, RCH,
Queensland Children's Health, NSW ACI, SA Health, the Australian Immunisation Handbook and
NIP schedule, PBS, TGA, RACGP, RANZCOG, Kidney Health Australia, APEG, CDNA, NBA, AIHW.

**No guideline is fetched from a web session** — those run network-proxied. Wanting to look
something up is a stop, not a search.

Step 11 (AU dosing and product names) and Step 17 (UK-localisation) already govern the
Australian-context sweeps. These rules do not replace them.

---

## 1.9 Verification scope — the `NOT checked:` line

Step 14 tracks whether a guideline is *current*. This tracks whether a verification box
covered *everything beneath it* — a different failure, and one this project has hit twice:
`15_01a`'s ANZCOR box confirmed the doses while the adrenaline timing beneath it was UK/ERC
and wrong, and `PENDING_GUIDELINE_CHECKS.md` **B65** is a box claiming paediatric validity
above absolute adult figures.

```markdown
> [!check] VERIFIED — ANZCOR Guideline 12.2, Aug 2026
> **Checked:** adrenaline dose, amiodarone dose, defibrillation energy.
> **NOT checked:** drug timing relative to shock number, sequencing, 4Hs/4Ts wording.
```

**`NOT checked:` is mandatory.** "nil" is permitted only when true. A box without it is a
lint failure. Rule 8 applies here directly: report honestly, never "verified complete".

---

## 1.10 Merge rules

**Supersession is on provenance, never on content.** Judging which claim is more clinically
accurate requires a source that cannot be reached from a session.

| A's claim | B's claim | Action |
|---|---|---|
| `verified` | `unverified` | A wins, B discarded |
| `inherited` | `unverified` | `CONFLICT` block, both retained |
| absent | present | additive merge, keeps `unverified` label |
| figures differ | figures | `CONFLICT`, never auto-resolved |

**Corpus B can never win automatically** — it carries no sources. Where B proves right, a
guideline established it, not B.

**Two corpora agreeing is not corroboration.** They share ancestry. A model asked about
appendicectomy prophylaxis would likely reproduce A's `co-amoxiclav + metronidazole` and
agree perfectly. Concordance never closes an item.

**Additive merge format** — under a marked subheading, never woven into existing prose,
which produces unreviewable diffs and blurs provenance at every sentence boundary. **Every
block carries a `SRC:` token naming the origin file and section**, so `grep -rn "SRC:C1_" .`
reconstructs everything that B file contributed and where each piece landed:

```markdown
### Added from unverified layer — <topic>
`SRC:C1_Acute_Abdomen §0.6` `UNVERIFIED — model knowledge, not source-checked.`
```

**The destination table for each B file is committed to `_meta/merges/<bfile>.md`** — every
section, its destination, and its disposition **including discarded ones**. Supersession
otherwise leaves no trace at all: a superseded section simply never appears, so a wrong
supersede is invisible and nothing can audit it. The discard rows are the point.

**Before creating any file, grep the whole vault.** Corpus A is not purely
disease-organised — it holds investigation, history and examination files, and
presentation-type sections inside disease files (`03_Gastrointestinal` §0.41 is "Abdominal
Pain — Regional Anatomy and DDx"). A duplicate file is the one error nothing downstream
detects. Rule 2 applies: zero grep hits is not proof of absence.

**Corpus B's wikilinks — the count and the characterisation were both wrong.** This said
"167 wikilinks point at placeholder codes that resolve to nothing". Measured across all 39
files: **798 wikilinks, of which 764 are unresolved** — and **573 of those 764 are not dead
at all.**

| | |
|---|---|
| **573 (75%)** | resolve to **exactly one existing Corpus B file**, with **zero ambiguity**, once `.`→`-` is normalised and the code is anchored to a following `_` (so `[[A1]]` cannot match `A10_`). `[[C2]]` → `C2_Nausea_and_Vomiting`, `[[F0.5]]` → `F0-5_Acute_Respiratory…`. These are **B's internal cross-references**, not placeholders. |
| **191 (50 codes)** | have **no candidate file** — `P1`, `P3`, `O6`, `N6`, `L4`, `E1`, `M5`, `H4`, the `J` series. B's code scheme anticipated files that were never built. **These are the genuine placeholders**, and only these get `` `TODO:link — topic` ``. |

**Never guess a target** still stands, and the 573 are not guesses: the mapping is
deterministic and verified 1:1 against the filesystem. Do not resolve any of the 191.

**This is the fourth sampled count, and they share one cause.** "Corpus C states no doses"
(8 of 22 drug files do), "65 backticked references" (276), "42 wikilinks in C" (195), and
"167 placeholder links in B" (798/764) were each generalised from the same five-file sample
rather than counted. **Nobody ran the count.** Before quoting any corpus-wide figure in this
project, measure it — the habit, not the individual numbers, is the defect.

---

## 1.11 Content ownership

| Content | Owner |
|---|---|
| Dose, route, frequency, maximum | the file where it already lives — recorded in `_meta/OWNERS.md` |
| Drug mechanism, adverse effects, monitoring, class traps | `NEW_Drugs_NN_*.md` |
| Therapeutic-class pharmacology | `Medications_Reference.md` |
| Which drug in this disease, and why | condition file |
| Which test in this disease, and why | condition file, inline `(*why:*; *what:*)` |
| What a test is and how to read it | `NEW_Investigations_*.md` |
| Reference intervals | nobody — deliberately absent |

**Dual naming is correct and must never be rewritten.** `furosemide (frusemide)`,
`adrenaline (epinephrine)`, `lidocaine (lignocaine)` — Australian name leading, superseded
or international name in brackets. Corpus C does this deliberately, so a reader who learnt
the old name can find the entry. If the AU term already appears on the line, the line is
already correct; rewriting it produces `furosemide (furosemide)`.

**A rename map is a list of substance identities, not spellings.** `DRUG_NAMING` carried
`amphetamine sulfate → dexamfetamine` — **two different substances** — until the
source-per-entry audit of 2026-08-30 removed it. **The digit check cannot catch this**: no
digit moves when a substance name is swapped, so the dose survives intact attached to the
wrong drug. Every entry names a source; an entry without one is not applied.

**`Medications_Reference.md` is not the dose owner.** Its own scope note forbids the role
("Nothing was moved here"), it holds two entries, and it states no doses. Do not relocate
dosing into it — that would break cross-references it was designed to preserve.

**Owner tables must record the range they cover.** B50 is the case where two files pointed at
an ASCIA adrenaline table that stopped at 7.5 kg, so a reader following the pointer for an
infant reached a table that did not cover them. A pointer to an incomplete owner is worse
than a local figure, because nothing signals the failure.

**Do not add NEW doses or reference ranges to Corpus C, and do not backfill its empty
`Normal:`/`Abnormal:` fields.** The only available filling material is model knowledge.

**But do not treat C as figure-free** (§1.6): 8 of its 22 drug files already state doses,
so "C states no doses" must never be used as a premise — not to skip a check, not to grant
`figures: none`, and not to assume a C dose came from somewhere else. Existing figures are
**scoped in place using the `NEW_Drugs_10` pattern**, never deleted.

Step 12 already covers same-fact-in-3+-files consistency. `→MED:` mirrors exist to make that
check mechanical, not to replace it.

---

## 1.12 Conflicts

Weight by risk. **R1** — dose, route, frequency, resuscitation timing, weight-based
paediatric figures, anything legal or notifiable — expanded `> [!fail]` block above the
claim. **R2** — thresholds and scores driving disposition — collapsed `> [!fail]-`.
**R3** — inline `` `CF-###` `` only.

```markdown
> [!fail]- CONFLICT CF-012 — imaging pathway **R2**
> **A (`inherited`):** <claim>
> **B (`unverified`):** <claim>
> **Why it matters:** <clinical consequence>
> **Resolve against:** <named open AU sources>
```

Both claims stay in the text. **Never adjudicate** — resolution is done by the human during
study, when the clinical context is already loaded. IDs are `CF-###`, sequential, never
reused, kept distinct from the tracker's `B##` sequence.

**No agent edits a `CONFLICT` block or a resolution stamp.** Those are written by hand in
Obsidian, and a session editing them causes exactly the silent loss described in §1.13.

---

## 1.13 Obsidian and git both write these files

Resolution stamps are made by hand in Obsidian during study. Sessions edit on branches.
**Two independent sync systems over one folder, neither aware of the other.** A merge
conflict in clinical markdown is the worst failure available, because taking one side
silently discards either a stamp or a merge and nothing detects the loss.

- Pull `main` into Obsidian **before** every study session.
- Push Obsidian edits **before** starting a session — a session clones `main`, so anything
  unpushed is invisible to it.
- Never leave a PR open on files being revised from.
- Resolve any conflict on a computer, never on a phone, and check the `NOT checked:` lines
  survived.

**One step = one session = one branch = one PR.** Web sessions can only push to their own
working branch, and session context does not carry over — `_meta/RUN_STATE.md` and the Queue
markers are the only memory.

---

## 1.14 Never

- Resolve a clinical conflict, or mark anything `verified`, without a named Australian source.
- Treat agreement between two corpora as corroboration.
- Write a `[!check]` without a `NOT checked:` line.
- Add a figure to a file declaring `figures: none`.
- Delete a login-required marker, or resolve one from a non-AU source.
- Edit `PENDING_GUIDELINE_CHECKS.md` from a script — it has a manual ID sequence and an
  append-never-delete history.
- Create a file without grepping the whole vault first.
- Delete a Corpus B file before every section is merged or explicitly rejected in a commit
  message.
- Renumber §1.3's rules, or renumber file sections, or repair Corpus B's placeholder links.
- Claim a phase is "complete" in the sense of verified. Rule 8: "clean against everything
  currently known to check for."

