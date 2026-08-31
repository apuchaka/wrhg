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

> [!important] **CORRECTION, 2026-08-31 — Finding 2 is half wrong, and the half that is
> wrong inverts this audit's central assumption.**
>
> Finding 2 said the `Injury, Poisoning, Envenomation & Environmental` category names four
> things and delivers two, and implied the corpus was correspondingly bare. **The
> environmental half was bare. The envenomation half was not.**
>
> `Corpus C/NEW_Drugs_04_Antidotes_and_Antivenoms.md` is **3 118 words, `trust: snippet`,
> AMH-derived**, and covers envenomation thoroughly:
>
> | Concept | Present |
> |---|---|
> | Pressure immobilisation **with the mechanism** — Australian venoms spread by lymphatics, so walking pumps them | ✅ |
> | Do not wash the bite site — **venom on the skin is what the detection kit reads** | ✅ |
> | Five monovalent antivenoms (brown, tiger, black, death adder, taipan) plus polyvalent | ✅ |
> | **Only ~5% of bites need antivenom** — the decision is evidence of envenoming, not the bite | ✅ |
> | **VICC**, neurotoxicity (ptosis → bulbar, may not reverse), myotoxicity | ✅ |
> | **The SVDK identifies WHICH antivenom, not WHETHER the patient is envenomed** | ✅ |
> | **Antivenom dose is the same in children as adults** — it neutralises venom, not body weight | ✅ |
> | Funnel-web, redback, box jellyfish and vinegar, stonefish and hot water, Irukandji, tick paralysis, blue-ringed octopus | ✅ |
>
> **So the checklist gap was real and the corpus gap was not.** That is a far smaller
> problem, and this audit originally implied the opposite.
>
> **THE PRINCIPLE THIS OVERTURNS:** *a thin checklist category does not imply thin corpus
> coverage.* Here the corpus was **ahead of its own specification**. The environmental half
> is the reverse case — checklist and corpus both empty until the A6 merge.
>
> **Consequence for the 872-row audit: it must run in BOTH directions.**
> 1. **Rows with no corpus coverage** — the obvious direction, and the only one every method
>    so far has looked in.
> 2. **Corpus content with no checklist row** — `NEW_Drugs_04` is exactly this, and **it is
>    invisible to every method used in this project to date.** Nothing has ever searched
>    from the corpus outward.
>
> The second direction is also how the corpus's real strengths get lost: content nobody is
> prompted to study.

> [!warning] **A second problem with `NEW_Drugs_04`, distinct from coverage: it is
> unreachable.**
> Its own frontmatter says `status: standalone — not yet cross-referenced into the corpus`.
>
> **Measured rather than assumed:** **five Corpus C files link to it** —
> `NEW_Drugs_06`, `07`, `10`, `12`, `18` — so it is reachable *within Corpus C*.
> **Zero Corpus A files link to it.** A reader working in the 148-file original notes —
> from `11_09b_Ortho_-_Trauma`, the anaphylaxis entries, or `09_01_Dermatology` — never
> arrives there.
>
> *(An earlier draft of this box said "nothing in the vault links to it". That was wrong,
> and the correction is the point: the file is unreachable **from Corpus A**, not
> unreachable.)*
>
> **Thorough and unreachable is close to absent in practice.** Cross-references were added
> 2026-08-31; this is a Step 28 job, not a content gap.

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

## Finding 5 — three domains missing from BOTH checklist and corpus, and what they share

Environmental injury · recognising dying · foreign bodies. **All three are
presentation-driven emergencies rather than diseases** — things a patient *arrives with*,
not things they *have*. Three is a pattern, not three coincidences.

**The hypothesis: a disease-organised specification systematically misses presentations.**

### It was tested against the categories, and it is only PARTLY supported

Every one of the 872 topics was classified as **presentation-shaped** (naming a symptom,
event or injury) or **disease-shaped** (naming a diagnosis).

| | categories | mean presentation-shaped |
|---|---|---|
| Stub (≤11 rows) | 6 | **23%** |
| Large (>11 rows) | 18 | **16%** |

The difference runs in the predicted direction but is **small**, and it is carried almost
entirely by two categories — `Injury/Poisoning` at 40% and `Older Persons Health` at 45%.
**Two of the six stubs are 0% presentation-shaped** (`Clinical Process`, `Australian
Context`), which the hypothesis does not predict.

### The refined version, which the data does support

**The checklist is overwhelmingly disease-organised everywhere — only ~17% of all 872 rows
are presentation-shaped.** So the bias is not a property of the thin categories; it is a
property of the whole specification.

**What that predicts is different, and more useful:** remaining holes will be
presentation-shaped **anywhere in the checklist**, not concentrated in the stubs. Looking
only at the thin categories for further gaps would be looking in the wrong place.

`Gastroenterology` at 102 rows and 21% presentation-shaped is the biggest category in the
file — and the merge still found a missing **acute abdomen framework**, a **neck-stiffness
differential**, and **bulbar versus pseudobulbar**, all presentation-shaped, all inside
domains the checklist covers densely. **Category size does not protect against this.**

### Why this cannot be closed from inside the vault

Testing it properly means asking *"what presentations does an Australian intern meet that
this checklist never names?"* — which is the external-reference question already recorded
below. **This finding sharpens that question; it does not answer it.** It is recorded as a
hypothesis with its supporting and non-supporting evidence, not as an established fact.

## PRIORITY ORDER for the outstanding external work

> [!important] **The ATSI weighting question comes FIRST — ahead of the 872-row audit.**
> Set 2026-08-31. The reasoning is structural, not a guess about content:
>
> **One `Low`-yield row for an entire domain that Australian curricula weight substantially
> is more likely to be a real hole than anything a row-level audit will surface.** The
> row-level audit searches for topics the checklist already names; this is a question about
> whether the checklist names the right topics at the right weight — and a weighting error
> on a whole domain costs more study time misallocated than any single missing row.
>
> It is also the **cheapest** of the outstanding checks: it needs one external document and
> answers a yes/no question, where the 872-row audit needs 872 careful reads.
>
> **What settles it:** the AMC curriculum or examination blueprint, or an Australian intern
> syllabus. **This cannot be settled from inside the vault** — the corpus has ATSI content
> (`Investigation-Interpretation` on KICA and derivation populations, `18_Geriatrics`, the
> dementia files), but its *presence* says nothing about whether the checklist's weighting
> of the domain is right.
>
> The audit does not assert the weighting is wrong. It records that **one row at the lowest
> weight, for a named domain, in a category that is itself a 4-row stub, is the shape of an
> error** — and that the check is cheap.

## What this audit cannot do, and what would

This was the **cheap** audit: 24 categories against row counts and titles. It found four
things in minutes.

**The 872-row audit is still worth running** — it finds rows the corpus does not cover. It
needs the same discipline as the merge: read every hit, because a word appearing somewhere
proves nothing. A naive version of it returned *"0 of 60 sampled rows uncovered"* and was
reassuring and wrong — it would have missed all three known-missing domains, because `heat`,
`stroke`, `dying`, `terminal`, `palliative` and `hypothermia` all appear somewhere in the
vault in unrelated contexts. **Rule 9's generic-component trap, at audit scale.**

**Neither audit closes the real gap, and the order matters.** The ATSI weighting check goes
first (above). Finding what the checklist and the corpus both lack requires an **external
reference** — the AMC curriculum, an Australian intern syllabus, or a
published exam blueprint. That is **outstanding work, and it is not addressed by the merge,
by this audit, or by the 872-row audit.** It is recorded here so it is not mistaken for
done.
