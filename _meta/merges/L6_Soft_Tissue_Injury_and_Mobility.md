---
name: L6 destination table
description: Where every section of Corpus B-new/L6_Soft_Tissue_Injury_and_Mobility.md goes, including the sections that were discarded.
bfile: Corpus B-new/L6_Soft_Tissue_Injury_and_Mobility.md
built: 2026-08-31
---

# L6_Soft_Tissue_Injury_and_Mobility — destination table

**24 concepts tested · 20 present · 3 absent · 1 conflict.**
**Additive/discard ratio: 3 additive + 1 conflict / 20 discard = 17% additive.**

> [!danger] **I TRUNCATED A VERDICT GREP AND IT HID THE ANSWER.**
> Checking whether `RICE` was in the corpus, I ran the gapcheck output through
> `grep -iE "rest.*ice|RICE\\b" | head -4`. The four lines returned were `liquorice`,
> `ocrelizumab`, `reheated rice` and `rice-water diarrhoea`, and I recorded RICE as absent —
> **which would have merged PEACE and LOVE as an addition rather than raising it as a
> conflict.**
> **`RICE` is present twice**, at `11_05:89` and `11_02:106`, further down the same result
> set. Re-run without `head`, the two lines are unmissable.
> This is **rule 10's HARD PROHIBITION** — no `head` on a grep feeding an ABSENT verdict —
> broken by me, in a run where I had already written that clause into CLAUDE.md twice. The
> clause is phrased so the *command being typed* is the violation; I typed it anyway.

## Destination table

| L6 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Load is the stimulus for healing; set the timeframe honestly; what impairs healing | — | **DISCARD** — folded into the conflict block rather than merged as a separate claim |
| 0.1 | **RICE has been superseded by PEACE and LOVE** | `Corpus A/11_05_Ortho_-_Knee_and_Ankle.md` | **CONFLICT `CF-036` R2** — A prescribes RICE at `11_05:89` and RICE + NSAIDs at `11_02:106`; B says both the rest and the anti-inflammatories are wrong. Not adjudicated |
| 0.1 | Prolonged immobilisation causes harm | — | **DISCARD** — inside CF-036; it is the same dispute |
| 0.2 | Tendinopathy is degenerative, not inflammatory; load is the treatment | — | **DISCARD** — 6 `tendinopathy` hits; `NEW_Exam_Manoeuvres:221` on gluteal tendinopathy; the epicondylalgia block merged from L5 earlier in this run carries the -itis/-osis naming point |
| 0.2 | **Fluoroquinolone-associated tendinopathy and rupture** | — | **DISCARD** — 17 `fluoroquinolone` hits, and `11_05:103` states quinolones are associated with tendon disorders |
| 0.3 | Strains and the sites that matter | — | **DISCARD** — `11_05`, `NEW_Orthopaedics_and_Trauma:86` |
| 0.3 | **Delayed onset muscle soreness versus injury** | `Corpus A/11_05_Ortho…` | **ADDITIVE** — `DOMS` returned 7 hits and **every one is the word `condoms`**. Base-A 0 |
| 0.3 | **Myositis ossificans** | `Corpus A/11_05_Ortho…` | **ADDITIVE** — `ossificans` 0 hits, base-A 0. Merged for the management point: a contusion that is losing range is a reason to stop stretching it |
| 0.3 | The two muscle emergencies | — | **DISCARD** — 25 `compartment syndrome` and 49 `rhabdomyolysis` hits; `11_01_Ortho:42` and `:70` |
| 0.4 | Return should be criteria-based, not time-based; load progression; certification | — | **DISCARD** — 3 `criteria-based` hits; `19_General_Practice` on certification |
| 0.5 | Immobility is a diagnosis with its own complications | — | **DISCARD** — 25 `immobility` and 10 `deconditioning` hits; `18_Geriatrics` and `GER2`-derived content |
| 0.5 | **Fitting a walking stick — three things commonly wrong** | `Corpus A/18_Geriatrics_and_Older_Persons_Health.md` | **ADDITIVE** — 43 `stick` hits, all "walking sticks for 6 weeks post-op" or urine dipsticks. **Nothing on which hand, what height, or the ferrule.** Base-A 0 |
| 0.5 | The other aids; weight-bearing terms | — | **DISCARD** — 8 `weight-bearing` hits, `11_08a_Ortho` |
| 0.6 | Functional assessment; Timed Up and Go; rehabilitation settings | — | **DISCARD** — 3 `Timed Up` hits; `18_Geriatrics` falls assessment |

## NO-BASELINE

All three additive blocks. `DOMS` (as the concept), `ossificans` and the stick-fitting
content return 0 in Corpus A and C at base-A.

## New files

**None.**
