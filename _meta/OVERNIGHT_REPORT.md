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

## Step 11 — AU drug naming · branch `phase/11-au-drug-naming` · 🛑 **HALTED**

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

### Next step

Step 28 is next in the queue and was explicitly deferred pending review of these two
reports. **Stopping here.**
