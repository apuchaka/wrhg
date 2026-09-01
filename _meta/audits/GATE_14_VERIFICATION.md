---
name: Fourteen-file gate — verification report
description: The 20-point gate check run against C1–C7 and D1–D7. Findings, not fixes.
built: 2026-09-01
---

# Fourteen-file gate — verification

**Nothing in this report was fixed.** Six checks failed.

## Per-file

| B file | 1 complete | 2 additive | 7 digits | 8 double | 13 headings | 6 links | verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| C1 | 11/11 | pass | pass | doc'd | pass | pass | **markers lost (4,17)** |
| C2 | 7/7 | pass | pass | doc'd | pass | pass | **markers lost (4,17)** |
| C3 | 7/7 | pass | pass | pass | pass | pass | **marker + relation lost (4,16)** |
| C4 | 5/5 | pass | pass | pass | pass | pass | **3 markers lost (4)** |
| C5 | 6/6 | pass | pass | pass | pass | pass | **marker lost (4)** |
| C6 | 6/6 | pass | pass | pass | pass | pass | **placement (5), 17** |
| C7 | 6/6 | pass | 1 ok | pass | pass | pass | pass |
| D1 | 6/6 | pass | pass | pass | pass | pass | pass |
| D2 | 6/6 | pass | pass | doc'd | pass | pass | pass |
| D3 | 7/7 | pass | 1 ok | pass | pass | pass | pass |
| D4 | 7/7 | pass | 1 ok | pass | pass | pass | pass |
| D5 | 6/6 | **FAIL** | pass | pass | pass | pass | **destination line deleted** |
| D6 | 7/7 | pass | pass | pass | pass | pass | **relation lost (16)** |
| D7 | 6/6 | pass | pass | pass | pass | pass | pass |

## FAILURES

### 4 — TEN UNVERIFIED markers destroyed, not seven. One breaks §1.14.

The earlier audit scoped its grep to `--grep="supersede" -i` — **66 of 93 commits.**
Re-run over all 93:

```
markers examined in deleted lines: 21 | now absent from the vault: 11
```

One is the Atlanta marker restored in reworded form on purpose. **The other ten are gone**,
and each named a source:

| Section | Marker | Replacing block |
|---|---|---|
| C1 §0.9 | empirical antibiotic for perforation/ischaemia; **Therapeutic Guidelines (login)** | no equivalent |
| C1 §0.10 | **TXA dose and time window in trauma, and the MTP ratio; National Blood Authority** | **no marker at all** |
| C1 §0.2 | CT contrast protocols; check local radiology guidance | no equivalent |
| C2 §0.5 | whether a QT threshold gates the second antiemetic | no equivalent |
| C3 §0.6 | orthodeoxia threshold, portopulmonary pressures | no equivalent |
| C4 §0.2 | Forrest grade labels + rebleeding percentages; RACGP | source dropped |
| C4 §0.2 | timing of restarting; RACGP or health-network guidance | source dropped |
| C4 §0.2 | AIMS65 components vs Glasgow-Blatchford in AU practice | no equivalent |
| C4 §0.3 | balloon max inflation time and pressures; gastro/ICU protocol | no equivalent |
| C5 §0.1 | caecal diameter + indications for neostigmine/decompression | source dropped |

**C1 §0.9 violates §1.14 — "Never delete a login-required marker."**
**C1 §0.10 is R1** (dose, time window, transfusion ratio) and its block now carries no marker.

### 5 — Twelve blocks nested under a narrower or unrelated parent

All are `###` under a base-A `##`:

| Block | sits under |
|---|---|
| **Oesophageal Disease** (cancer, EoE, achalasia, strictures, spasm, varices) | `## 0.3 Barrett's oesophagus` |
| **Anorectal Pain**, Tenesmus, Anal Lump, Pruritus Ani | `## 0.25 Haemorrhoids` |
| **Acute Liver Failure** | `## 0.38 Cirrhosis` — ALF is not a complication of cirrhosis |
| **Bowel Obstruction** | `## 0.39 Ileus` — inverted |
| **Constipation** | `## 0.42 Faecal Incontinence (Adult)` |
| **Radiculopathy** | `## Scoliosis` |
| **Reduced Consciousness**, Amnesia | `## CNS Infections Associated with Immunosuppression` |
| Tremor, Chorea, Mononeuropathies | `## Other Neurology Topics` while `## Movement Disorders` exists |

The last two are base-A's own structure (GCS lives in that H2). The first six are placements
I chose.

### 11 — Frontmatter counters never re-run

**17 files** where a script-maintained counter disagrees with the file, including four of this
run's destinations:

```
03_Gastrointestinal   conflicts_open 1  actual 2   no_baseline 3  actual 1
04_Neurology          conflicts_open 1  actual 1   no_baseline 1  actual 2
13_06b                conflicts_open 0  actual 1   (CF-039 is in the file)
11_06                 no_baseline    0  actual 1
```

### 10 — The figure comparison did not run. Zero comparisons.

```
CONFLICT blocks created by any section-merge commit: 1
new CF- ids introduced during C1-D7: CF-038, CF-039
```

Both pre-date the run — CF-038 appears only because C1 §0.2's supersede lifted and
re-attached it; CF-039 was raised before the merge began. **No destination figure was
compared against a B figure at any point in 93 sections.** The rule said "do not gap-check",
and I did not substitute a figure comparison for it. **This is a hole, not a clean result.**

### 16 — One relation destroyed beyond the ILAE pairing

C3 §0.1's fragment recorded a **named gap**:

> `Dubin-Johnson` and `Rotor` syndromes are absent from this vault and were not supplied by
> the merged material either — a real gap, recorded rather than filled from memory.

`Dubin-Johnson`: **0 hits in the vault. `Rotor`: 0.** The supersede removed the *record of
the absence*, so the gap is invisible again. **No presence check can see this** — the terms
were absent before and after; what was lost was the statement that they are missing.

34 removed lines carried a relational construction. Reading them against their replacing
blocks, the rest survive in reworded form (Sengstaken-as-bridge, sinistral portal
hypertension, the fissure perfusion→spasm→treatment chain all kept). Two exceptions besides
Dubin-Johnson: `second method` in C4 §0.2's dual-modality haemostasis, and `normal in
pregnancy` in C1 §0.11's physiological-leucocytosis delta — both partial rewordings, judged
not losses.

**This check cannot be automated.** The scan above finds candidates; every verdict here came
from reading.

### 15 / boundary — a LIVE bug, found by this check

A `SRC:` token **quoted inside a conflict block** (as CF-038 does, naming B's provenance)
is read by the foreign-SRC boundary rule as the start of a different merged block, and
truncates the fragment. Known-answer test:

```
block 4 lines | superseded 5 lines        <- should be 11
'content two' still present: True          <- orphan left behind
OK
```

It printed `OK`. **Latent, not triggered**: `aabc703` ran before that rule existed. Six
fragments in the vault now quote a `SRC:` token inside a `[!fail]` block and would hit it.

## PASSES

**1 — completeness.** 93 sections enumerated from the fourteen B files themselves;
**93 placed, 0 missing.** The enumeration pattern was itself validated: every level-2 heading
in all fourteen files is a numbered section and none has a form the pattern would miss.

**2 — additive-only.** 93 commits, 25 with deletions, all 25 supersedes. One deletion outside
a fragment: `fa7aba5`'s vertigo prognosis line, already restored.

**7 — digits per section.** 3 of 93 removed a digit, all three investigated and correct
(C7 §0.2 Atlanta figures supplied by §0.1 merged first; D3 §0.6 and D4 §0.6 removed only the
combined SRC token's own digits).

**8 / 9 — double placement and splits.** 18 tokens appear more than once; 13 are conflict-block
quotations. Three from this run have two block headers each — C1 §0.6, C2 §0.3, C2 §0.7 — and
**all three are documented decisions**, in the block's own note and in the placement record.

**12 — the seven restored markers.** All seven present; #4's reworded Atlanta marker reads
correctly against the line above it, which states the 48-hour CRP figure the original said was
*not* stated.

**13 — subheadings.** 0 new duplicate headings in any destination; 0 bare `#### Mx –`
subheadings remain; base-A's zero is restored.

**14 — the accidental pass.** With the fixed guard, **0 of 25 supersedes lose a
cross-reference.** D2 §0.5's coincidence was masking a *false positive*, not a real loss: its
`§0.1` and `§0.5` came from the SRC line, and the fragment's only true reference was `§0.6.1`,
which was carried.

**6 — links.** 138 wikilinks inside this run's blocks, **0 unresolved.** Two genuine broken
internal references: `13_06b:86` cites `§0.33 Upper GI Bleed` and `08_10:89` cites `§0.41`,
both of which live in `03_Gastrointestinal` and are unqualified. 52 `TODO:link` markers, all
already scheduled.

**17 — combined-source fragments.** Three vault fragments still carry multi-section SRC lines
(GER2, A6 ×5, F0-4). Three supersedes removed a fragment naming a not-yet-merged section —
C1 §0.1/§0.4, C2 §0.3/§0.4, C6 §0.4/§0.5 — and **all three second halves merged later in the
same run and are present now.** Only C2's was documented.

**18 — commit messages.** 74 numeric claims checked against the diffs. The 8 apparent
mismatches are a definition difference, verified: the driver counts the fragment span
(`e - s`), git pairs modified lines. `c82b3b8` claimed 21; the span is 21; git shows 11.
Prose survival claims: 5 checked, **4 pass, 1 false** — `fa7aba5`, already corrected.

**19 — deferred queue.** Three entries in RUN_STATE, each with a recorded reason: the two
cross-reference edits, the 34 `(unbuilt)` markers, and the aspirin findings.

## What this does not establish

Clinical correctness of anything merged. Rule 8: clean against everything currently known to
check for — and check 10 says one of those things was never checked at all.
