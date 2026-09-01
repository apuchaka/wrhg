---
name: Removing the 137 blocks — feasibility and consequences
description: Tests the fragment argument by sampling ten blocks against their B source sections. Report only; nothing removed, modified or regenerated.
built: 2026-08-31
status: REPORT ONLY
---

# Feasibility and consequences of removing the 137 merged blocks

**Nothing was removed, modified or regenerated.** Two dry runs were performed on scratch
copies under `/tmp`.

---

# 0. THE FRAGMENT ARGUMENT — TESTED, AND IT DOES NOT HOLD

**The claim:** each block is a filtered subset of its B section, stripped of surrounding
argument. Under the section rule the whole section merges, so the destination would carry both
and the merge would have to judge supersession.

**Ten blocks sampled across ten different B files and all three weeks, each compared against
its own B source section. The claim is half right, and the half that is wrong is the
expensive half.**

| # | Block | Source | Verdict |
|---|---|---|---|
| 1 | `01_Cardiovascular:48` RV infarction / V4R | B1 §0.1 | **ASSEMBLY** |
| 2 | `01_Cardiovascular:410` acute AF precipitants | B3 §0.4 | **ASSEMBLY** |
| 3 | `03_Gastrointestinal:1085` rectal foreign body | A8 §0.7 | TRANSFER |
| 4 | `03_Gastrointestinal:847` appendicitis sequence | C1 §0.6 | TRANSFER + merge-written cross-refs |
| 5 | `04_Neurology:1392` two discriminators in a weak patient | **D4 §0.4 + D4 §0.6 + L3 §0.4** | **ASSEMBLY across two B files** |
| 6 | `07_Renal:793` DIAPPERS | GER2 §0.1 | TRANSFER + merge-written framing |
| 7 | `08_09:18` two bite exposures | K2 §0.5 | **ASSEMBLY** |
| 8 | `01_Cardiovascular:1908` statin muscle symptoms | I5 §0.3 | TRANSFER + ownership pointer |
| 9 | `11_02:147` lateral epicondylalgia | L5 §0.3 | TRANSFER + merge-written framing |
| 10 | `19_General_Practice:151` ATSI | **AU1 §0.2 + §0.5** | **ASSEMBLY + deliberate narrowing** |

**4 assembly · 1 assembly with deliberate narrowing · 5 transfer — and ZERO pure transfers.
Every one of the ten carries at least one merge-authored element the section merge cannot
reproduce.** Worked examples:

- **#1** quotes **the destination's own territory table** ("the territory table above sends an
  inferior pattern to the RCA"), quotes `NEW_Drugs_06_Cardiovascular` **verbatim**, and points
  at `§0.1.2`'s "GTN 1 spray (caution hypotension)" as *"the specific reason for that
  caution"*. Three of its four moves reference material that is not in B1 §0.1.
- **#2** exists only as a delta: *"the **acute** precipitants **SMITH** does not cover"*.
  SMITH is Corpus A's own mnemonic. B3 §0.4 is about anticoagulation and rate-versus-rhythm.
  Merging B3 §0.4 whole produces the AF section, not this.
- **#5** pairs foot-drop inversion testing (D4) with steroid myopathy (L3) as *"two
  discriminators in a weak patient"*, and adds *"the anatomy is already tabulated in
  [[11_07a_Ortho_-_Dermatomes_and_Myotomes]]"*. Section-merging D4 §0.4 puts foot drop in one
  place and L3 §0.4 somewhere else. **The pairing is the content.**
- **#7** selects two of five items from K2 §0.5 and adds two corpus-state observations the
  merge made: *"This is the organism behind the standing instruction at Post-splenectomy
  sepsis below"*, and that bat lyssavirus is *"named in this corpus only inside the NNDSS
  quarantinable category at [[08_01-03]] as 'rabies/lyssaviruses'"*.
- **#10** opens with an explicit scope note — *"This block is deliberately narrow. It covers
  what an intern does, not the history, the policy or the epidemiology"* — and then maps where
  the rest already lives (`12_01_Rheum:105`, `Clinical-Process…`). **Section-merging AU1 §0.2
  whole brings back exactly the material the merge deliberately excluded, and does not bring
  back the map.**
- Even the transfers carry it: **#4** *replaced* B's Alvarado sentence with a pointer to
  `§0.41.3`; **#9** opens *"The management above is correct and is missing the thing patients
  most often ask for"*; **#8** hands ownership to `[[04_Neurology]]` for rhabdomyolysis.

**So the fragment argument is correct that the clinical claims come back. It is wrong that
nothing is lost: what does not come back is the connective tissue — the cross-references, the
delta-framings against destination content, the ownership assignments and the scope notes.
That material was written by the merge, exists nowhere in Corpus B, and is the part that makes
a block reachable from where a reader actually is.**

---

# 1. FEASIBILITY

## Not a git revert
393 commits base-A → HEAD, with Step 11, the Step 26/28 infrastructure, the ASCIA correction
and the frontmatter pass interleaved between merge commits. No contiguous range exists.

## Scripted removal — structurally clean
```
137 blocks · 2136 lines · 105 headings · 4 orphaned '>' continuation lines
```

## What else breaks — measured, and it is almost nothing

| Checked | Result |
|---|---|
| **§-references from outside a block into a block-created section** | **0** |
| §-references block → block | 3 (die together) |
| `_meta/OWNERS.md` rows pointing into a block | **0** of 78 |
| `_meta/DOSE_MIRRORS.md` rows pointing into a block | **0** |
| `→MED:` mirrors inside blocks | **0** |
| `trust:` / `population:` frontmatter | 201 → **201** |
| ASCIA band table, `→MED:adrenaline`, `[!check]` box | **intact** |
| Step 11 renames | 14 → 13 (one mention was inside a block) |
| Corpus C conversions, refiling, KNOWN_ABSENCES, Step 17 | **untouched** |
| `STUDY_CHECKS.md` | 1295 entries, **derived** — regenerates |
| `no_baseline:` frontmatter counters | 201 files, script-maintained — all → 0, regenerates |
| `NO-BASELINE` markers | 74 → **0** (each is an assertion *about a block*, so moot rather than lost) |

**Nothing outside the blocks points into them.** That is the strongest feasibility finding.

---

# 2. CONSEQUENCES — what the section merge will NOT bring back

1. **The connective tissue, on all ten sampled blocks** (§0 above). Roughly: internal
   `§x.y.z` cross-references, `[[file]]` pointers written to place a claim against existing
   content, delta-framings ("what SMITH does not cover", "the management above is missing…"),
   ownership assignments, and scope notes.
2. **Assembly blocks specifically** — 5 of 10 sampled. #5 combines two B files; #10 combines
   two sections and narrows deliberately; #1, #2 and #7 are built against destination content.
   **These do not reappear by merging any single section.**
3. **The two worked examples of correct placement** — `01_Cardiovascular:48` and
   `03_Gastrointestinal` §0.33.4 (AIMS65). Both would have to be rewritten.
4. **The `NO-BASELINE` audit trail in place.** The findings survive in `_meta/audits/` and
   `STUDY_CHECKS.md`, but the in-file assertion goes.

**Extrapolating the sample:** if 5 of 10 are assembly, roughly **65–70 of the 137 blocks**
contain material no section merge reproduces. That is the honest number, and it is a sample
of ten — not a census.

---

# 3. THE CONFLICTS — and the naive script was wrong about them

**Re-run preserving `[!fail]` callouts: ALL NINE CF ids survive.** The entanglement reported
earlier was a property of my removal script, not of the corpus.

| ID | Sides | Fate under a `[!fail]`-preserving removal |
|---|---|---|
| **CF-032** | both quoted inside one `[!fail]` block | **SURVIVES UNTOUCHED** |
| **CF-039** | both quoted inside one `[!fail]` block | **SURVIVES UNTOUCHED** |
| **CF-038** | **R3 inline markers, one on each side** | **BREAKS** — the A-side marker survives at `NEW_Gastroenterology_and_Hepatology:36`; the B-side claim is deleted with the C1 block, leaving an orphan |
| CF-001, CF-012, CF-033, CF-034, CF-035, CF-036 | outside blocks | survive |

**The rule this exposes:** an **R3 inline marker cannot survive removal of one side, because
it does not quote the claim. An R1/R2 block can, because it does.** CF-032 and CF-039 are
already in that form. **CF-038 is the only one needing hand work, and the work is to rewrite
it as a block quoting both sides.**

### CF-032 — verbatim, survives as-is
> **A (`inherited`, §0.18 above):** imaging "generally not indicated unless diagnostic uncertainty"; CT reserved for Alvarado 4–6; **"US not useful for visualising the appendix"**, useful only for gynaecological mimics.
> **B (`unverified`, `SRC:C1_Acute_Abdomen §0.6`):** **CT abdomen and pelvis is the most accurate test in adults**; **ultrasound first in children, young women and pregnancy**, looking for a **non-compressible appendix** — i.e. ultrasound *can* visualise it, though a non-visualised appendix does not exclude appendicitis. MRI in pregnancy where ultrasound is non-diagnostic.
> **Why it matters:** the two cannot both be right about whether ultrasound images the appendix, and the answer decides **first-line imaging in exactly the groups where radiation matters most** — children, young women, and pregnancy. Following A in a pregnant patient sends her to CT; following B sends her to ultrasound first.

### CF-038 — verbatim, **needs lifting by hand**
> **A (`snippet`, base-A, `NEW_Gastroenterology_and_Hepatology:36`):** "**Palpate** gently and away from the pain first: guarding, rigidity, **rebound** and percussion tenderness; **localised versus generalised peritonism**; organomegaly; **a pulsatile expansile mass**; Murphy's sign; Rovsing's sign."
> **B (`unverified`, `SRC:C1_Acute_Abdomen §0.2`, `03_Gastrointestinal:1671`):** "**Percussion tenderness rather than rebound.** Gentle percussion elicits the same information as releasing deep palpation, is far kinder, and is more reproducible. **Rebound testing is unpleasant, poorly reproducible and should largely be abandoned.**"
> **Why it matters:** A instructs the examiner to elicit a sign B says to stop eliciting.

### CF-039 — verbatim, survives as-is
> **A (`inherited`):** endoscopic surveillance with biopsies **every 3–5 years** where metaplasia is confirmed — a fixed interval.
> **B (`unverified`):** the interval is **determined by segment length and dysplasia grade** — not fixed.
> **Why it matters:** different recall dates for the same patient; the interval is what goes into the recall system and the discharge summary.

---

# 4. THE ALTERNATIVE — what section-merging onto the current base costs

| | |
|---|---:|
| Total `##` sections across Corpus B + B-new | **970** |
| Distinct (B file, section) pairs already holding a merged fragment | **138** |
| B files affected | 58 |
| Sections whose fragment landed in more than one destination | **7** |

**14% of section merges would land on a destination already holding a fragment of that same
section. 86% land on clean ground.**

For each of the 138, the merge must decide one of: the new section supersedes the fragment
(delete the fragment, keep its cross-references); the fragment is assembly the section does
not contain (keep both, and the fragment's framing needs rewording to point at the new
section); or they disagree (raise a conflict). **The seven multi-destination sections are the
awkward ones** — one section, two fragments, two destinations.

---

# 5. RECOMMENDATION — **do not remove. The fragment argument strengthens that, it does not weaken it.**

I recommended against removal on the duplicate argument: five files audited claim-by-claim
showed C2, C3 and C4 clean, C4 the model to copy, and the two known bad placements sharing one
already-closed cause.

**The fragment argument points the same way, for a different reason.** It assumed the blocks
are subsets that the section merge regenerates. **The sample says they are not: zero of ten
are pure subsets, and five of ten are assembly.** Removing them deletes ~2136 lines of which
roughly half contains material that no section merge reproduces — the cross-references, the
delta-framings, the ownership calls, the scope notes — and the reason to remove them was
precisely that the section merge *would* regenerate them.

**The judgement the fragment argument wants to avoid does not disappear either way.** Removing
the blocks trades 138 supersession judgements for **~65–70 reconstruction judgements** about
material that has no source to merge from. Reconstruction is the harder of the two: a
supersession decision has both texts in front of it; a reconstruction has only what someone
remembers the block was doing.

**And 86% of section merges never meet a fragment at all.** The collision is confined to 138
of 970, in 58 files, with only 7 genuinely awkward.

**What I would do instead**, if the reconciliation burden is the concern:
1. Before merging a section, grep the destination for `SRC:<that B file> §<that section>`. One
   command; it tells you whether a fragment is there, deterministically. **No search failure
   is possible — the token is exact.**
2. Where a fragment exists, the section merge supersedes it and **inherits its cross-references
   rather than discarding them.**
3. Rewrite **CF-038** as a two-sided block now, regardless of what is decided — an R3 inline
   marker is fragile against any future edit to either side, which is a defect independent of
   removal.

**If you still want the clean base**, the sequence is: preserve `[!fail]` callouts in the
removal script (all nine conflicts then survive; only CF-038 needs hand work first), remove,
repair 4 orphaned lines, regenerate `STUDY_CHECKS.md` and the `no_baseline:` counters, and
accept the reconstruction cost above.
