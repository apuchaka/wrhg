---
name: overnight-report
description: Per-step record of unattended overnight runs. Written as the run proceeds, by what was examined rather than by what was changed.
---

# Overnight report

## Night of 2026-08-30

Branch per step, PR per step. Steps run in queue order (§1.1.9): 17, then 11.
Stopped before Step 28 by instruction.

---

## Step 17 — UK-localisation sweep · branch `phase/17-uk-localisation` · ✅ no halt

### What was examined

**All 240 corpus files — Corpus A 148, B 39, C 53 — every line, against 33 terms.**

This is **the first time Steps 17 has ever run over Corpus B and C.** The 2026-08-28
re-run covered the 148 Corpus A files only; B and C did not exist in the vault then.

Term list: the 9 from §1.23 (`NICE`, `NHS`, `BNF`, `A&E`, `GP surgery`,
`casualty department`, `Royal College of`, `British Society`,
`British National Formulary`) plus 24 added this run — `SIGN`, `DVLA`, `MHRA`, `GMC`,
`CQC`, `CCG`, `QOF`, `AMHP`, `NPSA`, `RCOG`, `RCGP`, `RCPCH`, `CG<n>`, `999`,
`111 service`, `health visitor`, `district nurse`, `GP practice`, `Green Book`,
`NHS/hospital trust`, UK Mental Health Act section numbers, `Mental Capacity Act`,
`EarCalm|Otosporin|Debendox`, `NICE guidance`.

### Raw hits: 71 · genuine: 3 · consistency fix: 1 · dismissed: 67

**Fixed (4 commits, one per fix):**

| File | What | Commit |
|---|---|---|
| `15_24a` | "Contact GP, **health visitor**, school" → child and family health nurse, service name varies by state | `be697f6` |
| `History-Taking` | "parent, **health visitor**/nurse" → child and family health nurse | `4ccd148` |
| `17_06` | RCOG OHSS severity grading — the **only** UK-college attribution in the corpus with no adjacent Australian adjudication. Flagged inline, `UNVERIFIED` naming **RANZCOG** as the open source. Not deleted, and no Australian equivalent invented | `6485509` |
| `16_01-05` | bare "**NICE recommendations**" heading above the Australian timetable → labelled "UK schedule, retained for reference only", matching the convention the same file already uses at L122 | `ecc45bc` |

**Dismissed, with reasons (67):**

- **NICE 29 — all legitimate.** Every one either sits inside a verification box naming an
  Australian source that supersedes it (Australian Asthma Handbook, AMH/Heart Foundation,
  eTG/GESA, RACGP, RANZCOG, RANZCP, Australian Prescriber/RCH), or is **already flagged**
  as unconfirmed with a `PENDING_GUIDELINE_CHECKS.md` **B32** pointer (`14_05a`,
  `16_01-05` L443, `16_10-13` L103), or is **a record of a correction already made** —
  `12_01` L70 reads "corrected — the original note's 'not recommended by NICE' was
  UK-specific guidance left uncorrected".
- **NHS 9 — all legitimate.** Deliberate AU-vs-UK contrasts inside verified boxes (no
  Australian AAA call-recall programme; no Medicare cap equivalent to the UK's 1–3 NHS
  cycles), plus `GMAWS` (an instrument name, not a UK-system reference) and the
  `03_Gastrointestinal` box that is itself the record of the "2-week-wait" fix.
- **DVLA 5 — all legitimate.** Every one an Austroads *Assessing Fitness to Drive*
  verification box naming the DVLA as the UK contrast.
- **RCOG 3 of 4 legitimate** — `16_06-07` ×2 sit inside a box recording that **RANZCOG
  hosts and directly adopts RCOG Green-top Guideline No. 13**; `16_10-13` already carries
  a warning that the attribution is unconfirmed.
- **GP practice 4 — all false positives.** Matched inside "Australian GP practice" and
  "Australian general practice" — Australian usage, not a UK-ism.
- **UK products 2 — both legitimate.** `13_01` is the box recording that EarCalm and
  Otosporin were wrong and giving Kenacomb/Otocomb Otic; `16_01-05` discusses Debendox as
  withdrawn in Australia in 1983.
- **MHRA 1, AMHP 1, British Society 1, health visitor 1 of 3** — each an explicit
  historical or cross-jurisdictional reference (the MHRA PREVENT programme named as
  international; the AMHP inside the SA localisation box; "British Society for
  Haematology-**style**" named as the superseded advice; `15_24b` contrasting Australian
  child health checks with the UK health visitor schedule).
- **Zero hits:** `BNF`, `A&E`, `GP surgery`, `casualty department`, `Royal College of`,
  `British National Formulary`, `999`, `111 service`, `district nurse`, `Green Book`,
  `hospital trust`, `Mental Capacity Act`, `GMC`, `CQC`, `CCG`, `QOF`, `NPSA`, `RCGP`,
  `RCPCH`, `CG<n>`. **`A&E` at zero and `BNF` at zero confirms the 2026-08-28 fixes held**
  — those were 6 and 1 genuine leftovers then.

### Finding — Corpus B and C are clean on this term list

Their first ever exposure to Step 17 produced **5 hits, every one a false positive**
(`SIGN` ×2, the sectioning regex ×4 — see below, `MHRA` ×1 legitimate). No UK-ism was
found in either corpus. Expected in hindsight: B was built from model knowledge with an
Australian brief, and C from Australian-guideline snippets.

> [!warning] **Two defects in this sweep's own regexes — CLAUDE.md rule 9, found while
> running the step it was written for.**
> - **UK Mental Health Act section numbers**: `section(ed|ing)? (2|3|5\(2\)|136|135)`
>   matched **"AMH section 2 Anaesthetics"** and "AMH section 3 Analgesics" — 6 hits, all
>   false, all document-structure references to the Australian Medicines Handbook's own
>   section numbering. A term list aimed at UK statute matched an Australian source's
>   table of contents.
> - **Case-sensitivity is not a reliable anchor in this corpus.** `\bSIGN\b` was made
>   case-sensitive precisely to avoid matching the word "sign" — and then matched
>   **"CARDIOVASCULAR WARNING SIGN"** and **"it is a CLINICAL SIGN"**, because this corpus
>   uses ALL-CAPS for emphasis inside danger callouts. The anchor that works for `NICE`
>   fails for any acronym that is also a common word.
>
> Neither defect changed a label or an edit — both hit sets were read and dismissed. They
> are recorded because the term list is reused, and per rule 7 they are **reported, not
> silently patched**.

**Honest status: clean against this 33-term list.** Not "clean of UK-isms" — the term
list is still a guess at which UK-isms exist, which is exactly what §1.23 already says
about itself.

---

## Step 11 — AU drug naming · branch `phase/11-au-drug-naming` · 🛑 halted, then ✅ **CLEARED**

### What was examined

All 240 corpus files against `merge_tools.py`'s `DRUG_NAMING` map (15 entries), plus a
brand-product check. **44 hits across 5 terms**, 30 in Corpus A and 14 in Corpus C.

### Done: 2 of 44

`norepinephrine` → `noradrenaline`, in `01_Cardiovascular` L975 and `14a-1` L64 (`8a631e9`).
Unambiguous — Australia uses noradrenaline universally, including for the neurotransmitter
in a mechanism description, and the rest of the corpus already does.

**Digit-invariance verified before committing**, per the Step 11 automation constraint: the
multiset of digits in both files is identical before and after. No dose figure moved.

### 🛑 HALT — the rename map is not an Australian naming authority, and 4 of its 5 triggered entries are unsafe to apply

Branch left **unmerged**. Nothing else was changed.

| Term | Hits | Why it was not applied |
|---|---|---|
| **`furosemide` → `frusemide`** | 14 | **The map is plausibly backwards.** The TGA's ingredient-name harmonisation moved Australian Approved Names toward the INN — the same programme that gave `lignocaine`→`lidocaine`, which this map itself encodes in that direction. If `frusemide`→`furosemide` went the same way, applying this entry would **regress 14 correct names**. Settling it needs the TGA ingredient-name list, which is an open AU source but cannot be fetched from a session (§1.8). |
| **`co-trimoxazole` → `trimethoprim+sulfamethoxazole`** | 15 | **The map's own value says "AU naming varies; confirm."** It is not a UK-only term. Renaming 15 instances on an entry that flags its own uncertainty is exactly the resolve-without-a-source failure the automation constraint forbids. |
| **`co-amoxiclav` → `amoxicillin+clavulanate`** | 12 | **A blanket rename would destroy provenance.** `02_Respiratory` L356 reads "**UK figures (unverified for AU use):** co-amoxiclav 500/125mg tds x 5 days" — a deliberately labelled UK reference block, the same convention as the NICE visit schedule. Renaming inside it would make UK figures read as Australian. Other hits are already-corrected records (`08_09` L37 already says "Amoxicillin+clavulanate is specifically reserved…"). These need per-hit judgement, not a map. |
| **`epinephrine` → `adrenaline`** | 1 | **False positive.** `NEW_Drugs_01` L117 reads "**adrenaline (epinephrine)**" — the correct dual-naming form, adrenaline primary. Nothing to fix. |

### Why this is a rule 7 halt rather than a judgement call

The instruction was that renaming is safe because a name change is not a regimen change.
That premise holds. **What does not hold is that `DRUG_NAMING` is a reliable source for
which name Australia uses.** It is a hand-written map with hedges inside its own values
("AU convention; confirm local usage", "AU naming varies; confirm"), and the one entry
checkable from internal evidence — `furosemide` — points the opposite way to the
`lignocaine`→`lidocaine` entry sitting four lines below it in the same map.

Applying it would have made **41 name changes on no source**, in the step whose entire
constraint is that nothing may be resolved without one.

### What would clear the halt

1. The **TGA ingredient-name list** settles `furosemide`/`frusemide` and `co-trimoxazole`
   in one lookup. It is an open Australian source — it needs a human with a browser, not a
   session.
2. `co-amoxiclav` needs the 12 hits judged individually against the labelled-UK-block
   convention. That is an hour of reading, not automation.
3. `DRUG_NAMING` should then be rewritten to carry a **source per entry**, so a future
   automated run has an authority behind each rename instead of a hedge.

**Brand products:** no new UK-market brand names found. `EarCalm` and `Otosporin` appear
only inside the `13_01` box recording that they were wrong and naming Kenacomb/Otocomb
Otic; `Debendox` only in the `16_01-05` box recording its 1983 Australian withdrawal.

---

## Step 11 — RE-RUN, halt cleared 2026-08-30

The halt was resolved by the user against the **TGA "Updating medicine ingredient names —
list of affected ingredients"** (Ingredient Harmonisation programme), an open Australian
source. **The map was wrong in the direction the halt suspected**: harmonisation moved
Australian Approved Names *toward* the INN, so `frusemide` → `furosemide`, not the reverse.

### The map now carries a source per entry, and an entry without one is not applied

| Action | Entries | Source |
|---|---|---|
| **Reversed** | `frusemide`→`furosemide` | TGA IHIN |
| **Added** | `amoxycillin`→`amoxicillin` | TGA IHIN |
| **Kept** | `lignocaine`→`lidocaine`, `rifampin`→`rifampicin`, `cyclosporine`→`ciclosporin` | TGA IHIN |
| **Kept, explicitly not reversed** | `epinephrine`→`adrenaline`, `norepinephrine`→`noradrenaline` | TGA IHIN **retains** adrenaline/noradrenaline as the AU approved names; the *-ephrine* forms are not adopted |
| **Kept** | `acetaminophen`→`paracetamol`, `glyburide`→`glibenclamide`, `albuterol`→`salbutamol` | already INN in AU, never changed |
| **Removed** | `co-trimoxazole` | its own value was a hedge, and a hedge is not a rename |
| **Removed** | `salbutamol sulfate`, `hydroxychloroquine sulfate` (mapped to themselves), `lignocaine hydrochloride` (redundant) | — |
| **Removed** | `amphetamine sulfate`→`dexamfetamine` | **a drug-identity error, not a naming one** — they are not the same substance. Found while auditing the map for sources |

### Two skip rules, both derived from hits read this run

- **Non-AU blocks.** A block flagged "UK figures (unverified for AU use)", "UK schedule,
  retained for reference only" and similar is skipped. **The foreign drug name is often
  the only thing marking that content as foreign** — renaming it makes UK figures read as
  Australian. 1 hit skipped (`02_Respiratory` L356).
- **Dual naming.** `furosemide (frusemide)`, `adrenaline (epinephrine)`,
  `lidocaine (lignocaine)` are correct as written with the AU name leading; Corpus C's
  drug files do this deliberately. **7 hits, no action.**

### Applied: 18 renames across 14 files · 0 actionable hits remaining

| Rename | Count | Marker |
|---|---|---|
| `co-amoxiclav` → `amoxicillin+clavulanate` | 6 | each carries `UNVERIFIED — AU regimen; Therapeutic Guidelines (login). Look up at point of use.` |
| `lignocaine` → `lidocaine` | 8 | none — pure TGA nomenclature |
| `frusemide` → `furosemide` | 4 | none — pure TGA nomenclature |

**Why no marker on the last two groups:** both name an open source in the commit, and two
of the `lignocaine` lines sit **inside existing WA Health verification boxes**, where an
`UNVERIFIED` marker would contradict a box that has been verified.

**Digit-invariance verified per file before committing.** The multiset of digits is
identical before and after in all 14 files. No dose figure moved.

**Note on `furosemide`:** the corpus's 14 pre-existing `furosemide` instances were already
correct. Under the old map they would all have been renamed to `frusemide`. The halt
prevented 14 regressions.

### Next step

Step 28 is next in the queue and was explicitly deferred pending review of these reports.
**Stopping here.**
## Step 28 — Corpus C remediation · ✅ 28a and 28b, one PR each

### 28a — scope every figure C already states · branch `phase/28a-corpus-c-doses`

**7 files, 9 scoping blocks, purely additive** — `git diff` shows **0 removed content
lines**, a stronger guarantee than digit-multiset invariance here, since the scoping text
itself contains digits.

`NEW_Drugs_01` was **not** given an "adult doses" warning: the ASCIA table is already
exemplary — per-kg with a cap, weight bands, and its own note saying so. What it needed was
the other defect, **the 7.5 kg floor**: the ampoule dose covers an infant below it, the
injector devices do not, and the added note says specifically not to round a child up into
the 150 microgram band because it is the smallest device available. Cross-referenced to
B71 and B50.

Scoped elsewhere: vancomycin AUC targets (neonatal regimens run on postmenstrual age, not
an adult AUC), the Hb <70 g/L trigger, pyridoxine neurotoxicity thresholds, the
hydrocortisone-equivalent HPA threshold, the metformin eGFR cut-off, probenecid CrCl, FTU
body-area counts. **Loperamide** got the sharpest wording, because it is **avoided
altogether in young children** — the adult daily maximum is not a ceiling to dose up to,
it is a figure that does not apply.

**Examined and not scoped:** `NEW_Drugs_16` anti-D `500 IU`. The population is inherently
adult — anti-D is given to the mother, the infant is not dosed.

### 28b — refile, deduplicate, flag · branch `phase/28b-corpus-c-refile`

| Entry | Action |
|---|---|
| 0.32 CSF Studies | **refiled** → `NEW_Investigations_Orthopaedics_Neurology_and_Other.md` 0.21 |
| 0.35 Rubella / Varicella Serology | **refiled** → `NEW_Investigations_Infectious_Diseases.md` 0.24 |
| 0.33 Coombs / DAT | **NOT refiled — already exists** at the destination |
| 0.34 G-CSF | **NOT refiled — already exists**, and it is a drug, not a test |

**Two of the four "misfiled" entries were duplicates, not orphans.** Grepping the
destination before moving is what found it; refiling either would have created a second
owner for the same test. Both replaced with pointer stubs, section numbers retained in
place because CLAUDE.md forbids renumbering.

> [!warning] **Rule 1 caught my own cross-reference.** I first wrote the Coombs pointer as
> `NEW_Investigations_Haematology.md` **0.7**. Verifying the target before committing
> showed **that section is unnumbered** — its header is *Immunohematology (Blood Group &
> Rh, Type & Screen, Direct Antiglobulin Test)*. The `0.7` was a plausible-sounding
> invention of exactly the kind rule 1 exists to stop, written by the same session that
> had just spent the night auditing other people's unverified claims.

**Flagged, not rewritten:** the R-ratio `(ACG definition)` → resolve against GESA; CKD
staging `(KDIGO)` → Australia follows KDIGO via Kidney Health Australia, so the marker
names KHA.

### 🛑 One instruction not carried out

**Step 28 says to delete sections self-labelled "OUT OF SCOPE, built in error". The
Gastrografin section was not deleted.** The step's premise is that such sections are build
debris; this one's own body says "**flagged rather than deleted**", a considered decision,
and the content is clinically sound and held nowhere else — the aspiration hazard, the
safe-alternative-to-barium role, the hyperosmolar caution in neonates and the frail.

The scope error is real but it is a **build-list categorisation** error. Deleting correct
clinical content to satisfy a list boundary loses information irreversibly and nothing
downstream detects the loss. Noted in place, raised for decision, not actioned. **The Step
28 wording should be narrowed before another session reads it as blanket permission to
delete.**

### Not yet done in Step 28

The **217 backticked file references** still need converting to wikilinks with each target
header verified (rule 1). Note the spec says **65**; the actual count is 217. That is a
separate PR and has not been started.
## Step 28c — backticked references → wikilinks · branch `phase/28c-wikilinks`

### Counts, measured not sampled

The spec said **65** backticked references and **42** existing wikilinks. Measured across
all 53 files: **276** references and **195** wikilinks. Both were sampling errors from the
same five-file sample that produced the figure-free claim — see the §1.34 correction.

### Classified before converting anything

| Class | n | Action |
|---|---|---|
| `sectioned-OK` | 172 | **converted** — section number verified to exist as a heading in the target file |
| `prose-bare` | 32 | **converted** — target file verified to exist |
| `table-metadata` | 72 | **left backticked** — build-status and skipped-topic tables, records of a build check rather than cross-references for a reader to follow |
| `sectioned-BAD` | 1 → 0 | see below |
| `DANGLING-FILE` | 0 | — |

**Per chunk (9 files each):**

| Chunk | examined | converted | left | flagged |
|---|---|---|---|---|
| 1 | 16 | 4 | 12 | 0 |
| 2 | 78 | 75 | 3 | 0 |
| 3 | 80 | 76 | 4 | 0 |
| 4 | 37 | 12 | 25 | 0 |
| 5 | 48 | 37 | 11 | 0 |
| 6 | 17 | 0 | 17 | 0 |
| **total** | **276** | **204** | **72** | **0** |

**Post-conversion verification: Corpus C now holds 399 wikilinks, 0 dangling.** 195 pre-
existing + 204 converted. Re-running the classifier finds only the 72 table-metadata refs
remaining, and no unresolved section number anywhere.

Nothing needed flagging in the end, because the one bad reference was found and fixed
*before* the conversion ran — which is the whole reason for classifying first.

> [!danger] **The one bad section number was inherited, and I propagated it before I caught
> it. Correcting my own earlier account.**
> I reported this as a section number *this session invented*. **That was wrong.**
>
> `` `NEW_Investigations_Haematology.md` 0.7 (Immunohaematology) `` has sat in
> `NEW_Investigations_Gastroenterology` 0.33 **since commit `39be13e`, the original Corpus C
> upload**. Writing the Step 28b pointer I copied it out of that line without checking it.
>
> It is wrong twice: that file **has no section 0.7** — the section is unnumbered — and its
> header spells it *Immuno**he**matology*, without the second `a`.
>
> **The instructive part is that it was inherited.** A wrong reference already in the corpus
> reads as established fact: it has been there since the first commit, it looks like every
> other reference, and copying it feels like *using a source* rather than *making a claim*.
> That distinction is invisible at the point of writing, which is exactly why rule 1 has to
> apply to references you did not author. **An unverified reference is a new claim no matter
> where you got it from** — and the session doing the auditing is the one that propagated it.
>
> Corpus line corrected in place, with a note recording what it used to say.
