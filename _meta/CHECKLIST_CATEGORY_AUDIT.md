---
name: checklist category audit
description: The 24 checklist.csv categories audited at category level, 2026-08-31. The corpus is complete against its specification and the specification has holes.
---

# Checklist category audit — the specification has holes

## Why this was run

The merge found two entirely missing clinical domains: **environmental heat illness** and
**recognising dying**. Both were absent from all 240 corpus files. The question that
followed was whether a coverage audit against `checklist.csv` would find others.

**It would not have found these two, because the checklist does not contain them either.**

| Searched in `checklist.csv` | Rows |
|---|---|
| `hypotherm` | **0** |
| `dying`, `end of life` | **0** |
| `drown` | **0** |
| `heat` | 1 — and it is **`Flexor sheath tenosynovitis`**, matching inside *s-**heat**-h* |
| `palliat` | 1, Medium yield |

**The corpus is complete against its own specification. The specification is incomplete.**

Every gap the merge has found was found because a Corpus B file happened to cover that
topic. **That is luck, not method.** Nothing in the merge, and nothing in a checklist audit,
can find what the checklist and the corpus both lack.

## Finding 1 — the five `(NEW)` categories are stubs

| | categories | rows | mean |
|---|---|---|---|
| Original | 19 | 839 | **44.2** |
| Marked `(NEW)` | 5 | 33 | **6.6** |

**A 6.7× difference.** The five:

| rows | category |
|---|---|
| 2 | Clinical Process / EBM / Consent & Capacity `(NEW)` |
| 4 | Australian Context of Health / Aboriginal & TSI Health `(NEW)` |
| 6 | Public Health, Epidemiology, Statistics, Research `(NEW)` |
| 10 | Injury, Poisoning, Envenomation & Environmental `(NEW)` |
| 11 | Older Persons Health / Geriatrics `(NEW)` |

These were added later and never populated. **Geriatrics is the exception that proves it** —
11 rows but **10 of them High yield**, so it was added *and* weighted, while the other four
were added and left.

## Finding 2 — a category named for content it does not contain

**`Injury, Poisoning, Envenomation & Environmental` has 10 rows and contains no envenomation
row and no environmental row.**

> Adult choking · Adult, paediatric and neonatal resuscitation · Burns · Burns and scalds ·
> Lacerations and abrasions · Major trauma · Overdoses · Shock · Trauma · Traumatic head injury

**In Australia.** No snakebite, no spider bite, no marine envenomation, no heat, no cold, no
drowning, no electrical injury. The category title promises four things and delivers two.

This is exactly where the merge found its largest gap, and the two facts are the same fact:
**the notes are missing environmental injury because the checklist never asked for it.**

## Finding 3 — five rows are misfiled under ENT, and appear nowhere else

| Row filed under ENT | Where it belongs |
|---|---|
| `Biceps femoris (Hamstring) TEARS` | Musculoskeletal |
| `meniscal tear` | Musculoskeletal |
| `Sick Sinus Syndrome` | Cardiology |
| `ECG (start early — it takes repeated exposure to get fluent)` | Cardiology |
| `FBC, UEC, LFTs — the "core bloods"…` | Investigations |

**Checked: none of the five appears in its correct category as well.** They exist in the
checklist *only* under ENT.

Two consequences. **ENT is 15 rows, not 20** — thinner than the table suggests, and with
**0 High-yield rows**. And **anyone studying Cardiology from this checklist will never
be prompted on the ECG**, because the ECG row is filed under ENT.

## Finding 4 — a weighting worth questioning

**`Aboriginal and Torres Strait Islander health issues` is one row, marked `Low` yield.**

An entire domain, one row, lowest weight. Whether that matches the AMC's own weighting is
**not something this audit can settle** — it needs the AMC curriculum or blueprint, which is
outside the vault. Flagged as a question, not asserted as an error.

## What this audit cannot do, and what would

This was the **cheap** audit: 24 categories against row counts and titles. It found four
things in minutes.

**The 872-row audit is still worth running** — it finds rows the corpus does not cover. It
needs the same discipline as the merge: read every hit, because a word appearing somewhere
proves nothing. A naive version of it returned *"0 of 60 sampled rows uncovered"* and was
reassuring and wrong — it would have missed all three known-missing domains, because `heat`,
`stroke`, `dying`, `terminal`, `palliative` and `hypothermia` all appear somewhere in the
vault in unrelated contexts. **Rule 9's generic-component trap, at audit scale.**

**Neither audit closes the real gap.** Finding what the checklist and the corpus both lack
requires an **external reference** — the AMC curriculum, an Australian intern syllabus, or a
published exam blueprint. That is **outstanding work, and it is not addressed by the merge,
by this audit, or by the 872-row audit.** It is recorded here so it is not mistaken for
done.
