---
name: NO-BASELINE audit
description: Re-test of every NO-BASELINE marker in the tree against base-A, by the block's own plain topic name.
built: 2026-08-31
---

# NO-BASELINE audit — 74 markers re-tested

## Why this ran

The week-3 close-out verification reported two terms MISSING (`hyperCKaemia`,
`nursemaid`). Both were **search terms used to establish a gap, never words written
into the merged text**, so both were false negatives of the verification — the
content was present. But checking `nursemaid` surfaced a real defect:

**`Corpus A/11_02` already contained `### Pulled elbow` in base-A.** The gap check
had searched the eponym (`nursemaid`, 0 hits) and a mechanism word (`pronation`,
3 hits, all adult fracture mechanisms) and **never searched the plain English name
of the topic.** A duplicate was merged and marked NO-BASELINE.

That is a method defect, not an incident, so all 74 markers were re-tested.

## The method

For each marker, a **distinctive term taken from the block's own title** — not from
the original gap check — was run against the base-A tree (`Corpus A` + `Corpus C`
at `0db4034`, the merge source excluded per the scope fix made at K2).

**An automated title-term extractor was written first and DISCARDED.** It derived
`ring` for the rust-ring block (1635 hits), `pain` for yellow flags (1106),
`treatment` for the window of opportunity (975). That is rule 9's too-generic
component failure exactly, and the counts were meaningless. Terms were then
chosen by hand, 74 of them.

## Result

**24 of 74 returned non-zero. Every hit was read in full.** Four were real.

| Block | Term | Hits | Verdict |
|---|---|---:|---|
| `11_10:44` pulled elbow | `pulled elbow` | 1 | **REAL — duplicate.** `11_02:149` in base-A. Fixed, `1175373` |
| `12_02:52` allopurinol / HLA-B | `allopurinol hypersensitivity` | 3 | **REAL — duplicate in 3 places**, incl. a "not repeated here" pointer at `12_02:44`. Fixed, `9c4a94f` |
| `12_01:76` window of opportunity | `treat-to-target` | 5 | **REAL in part.** `12_01:48` states treat-to-target with DAS28, 34 lines above. The early-treatment claim is genuinely absent. Scoped, `d563089` |
| `06_Metabolic:1168` weight stigma | `Weight stigma` | 1 | **REAL in part.** `14_05a:53` uses the term as a risk factor. The clinical effect is absent. Scoped, `9bd39fe` |

The remaining 20 were collisions or different senses, all read and dismissed:

| Term | Hits | What it actually matched |
|---|---:|---|
| `orf` | 7 | Peterdorf, **n**orf**loxacin**, burgd**orf**eri, perf... — **zero real.** A 3-letter pattern |
| `PPPD` | 3 | **pylorus-preserving pancreaticoduodenectomy**, not persistent postural-perceptual dizziness |
| `HLH` | 3 | **hypoplastic left heart**, not haemophagocytic lymphohistiocytosis |
| `RED-S` | 1 | `## Red-stained nappy` |
| `felon` | 60 | `lifelong` — the known trap, re-confirmed rather than assumed |
| `LADA` | 5 | `maladaptive` — likewise |
| `Whipple` | 3 | Whipple's **resection**, not Whipple's **triad** |
| `sporotrich` | 1 | an itraconazole indication in a drug file, not the lymphangitis pattern |
| `Drowning` | 2 | drowning as a cause of cerebral palsy, not its management |
| `walking stick` | 2 | duration of use after joint replacement, not how to fit one |
| `death certificate` | 1 | stillbirth registration |
| `Fever pattern` | 2 | malaria cyclical timing; drug-rash history |
| `epicondyl` · `creatine kinase` · `mycobacterial` · `substitute decision` · `Hepatitis C` · `penetrating` · `decompensated` · `aetiology` · `counselling` · `opioid` · `asymptomatic` | 7–174 | read; different conditions or contexts |

## Four new acronym collisions for the register

**`PPPD`, `HLH`, `RED-S` and `orf`.** None was on any prior list. `orf` at 7 hits
with **zero real** is another sub-six-character pattern behaving exactly as rule 9
predicts, and `PPPD` and `HLH` are the more dangerous shape: a **real acronym with a
second real medical meaning**, which reads as a genuine hit rather than as noise.

## The rule this establishes

**Search the plain English name of the topic, not only the eponym, the acronym or
the mechanism.** All four real findings were missed by gap checks that searched a
name for the thing rather than the thing. `nursemaid` and `pronation` both returned
honest, correct, useless answers about a section titled `Pulled elbow`.

This is rule 2's inverse: rule 2's eponym clause says search components rather than
the name when the name fails. It does not say the converse — that a search on an
alternate name must still be run against the corpus's own plain wording.

## Content loss check

**Zero.** All 30 week-3 additive blocks are present. An apparent 10-block shortfall
(30 claimed, 20 `SRC:` tokens found) was an artifact of counting tokens: related
claims merged under one heading carry one token spanning several sections, e.g.
`SRC:AN1_Perioperative_Care §0.1, §0.4, §0.5` covers four callouts. Verified by
reading every block.
