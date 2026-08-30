---
name: D2 destination table
description: Where every section of Corpus B/D2_Altered_Consciousness_and_Cognition.md goes, including the sections that were discarded.
bfile: Corpus B/D2_Altered_Consciousness_and_Cognition.md
built: 2026-08-31
---

# D2_Altered_Consciousness_and_Cognition — destination table

Committed **before** any content was written. 4 379 words, 6 sections.
**2 placements · 5 discards.** 15 of 19 concepts tested were already present.

## The rule 9 instance of the run — `TGA` means three different things here

`transient global amnesia` was searched as `\bTGA\b` and returned **14 files**. **Every
one was a false positive**, and they were not even all the same false positive:

| What `TGA` meant | Where |
|---|---|
| **Transposition of the Great Arteries** | `01_Cardiovascular`, the paediatric cardiology files — *"TGA, Ebstein's anomaly, Kawasaki disease"* |
| **Therapeutic Goods Administration** | *"TGA safety guidance and Epilepsy Action Australia"* |
| Transient global amnesia | **nowhere** |

A three-way acronym collision inside one corpus, spanning a congenital heart lesion, a
national regulator and a neurological syndrome. The literal phrase `transient global
amnesia` returns **zero files**. The gap is real; the search that found it was wrong three
times over.

## The mnemonic trap — the eponym check working in the other direction

`PINCH ME` returned **ABSENT**, and the merge would have added it as a gap. Reading
`04_Neurology` §Delirium shows its `A/P` line already lists **drugs and withdrawal,
infection, hypoxia, dehydration, fever, constipation, metabolic abnormality, surgery,
pain, sleep deprivation and environmental factors** — the PINCH ME content in full, without
the mnemonic.

**Not merged.** This is the West Haven decision again: the content is present, only the
memory aid is missing, and adding a mnemonic over existing prose is not an additive merge.
Recorded so the absence is not re-found and re-merged later.

## Component-search results

| Instrument | Name | Components | Verdict |
|---|---|---|---|
| AEIOU TIPS | found | — | present |
| PINCH ME | **absent** | **present** — see above | mnemonic only |
| GCS by component (E/V/M) | found | `E_V_M` pattern found | present |
| herniation syndromes, uncal, tonsillar | found | blown pupil found | present |
| MMSE, MoCA, AMTS, KICA | found | — | present, with the derivation-population principle |
| **RUDAS** | **absent** | **absent** | **genuinely absent** |
| **4AT / CAM** | **absent** | **absent** | **genuinely absent** |
| Wernicke-Korsakoff | found ×10 | triad + thiamine found ×11 | present |
| pseudodementia, BPSD, DLB antipsychotic sensitivity, hypoactive delirium, inattention | found | found | present |

## Confirmed genuine gaps

| Concept | Verdict |
|---|---|
| **transient global amnesia** | **absent** — see the `TGA` collision above |
| **transient epileptic amnesia** | **absent** |
| **RUDAS** (Rowland Universal Dementia Assessment Scale) | **absent** — Australian-developed, and `Investigation-Interpretation` already carries the argument RUDAS answers |
| **4AT and CAM** as delirium-specific instruments | **absent** — the corpus has AMTS for a rapid screen but no delirium-specific tool |
| **structural versus metabolic** as the pattern separating causes of reduced consciousness | **absent** |

## Destination table

| D2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Reduced consciousness — first four things, AEIOU TIPS, pupils, GCS components, herniation, non-convulsive status | — | **DISCARD** — `04_Neurology` §GCS, §Seizures (status), §Brain Lesion Localisation; herniation is in eight files |
| 0.1 | **Structural versus metabolic** | `Corpus A/04_Neurology.md` §GCS | **ADDITIVE** |
| 0.2 | Delirium — inattention, hypoactive, precipitants, drugs, non-pharmacological management | — | **DISCARD** — `04_Neurology` §Delirium and §"3 Ds", which carry AU-specific antipsychotic dosing D2 lacks |
| 0.2 | **4AT / CAM** | `Corpus A/Investigation-Interpretation.md` Cognitive tools | **ADDITIVE** |
| 0.3 | Dementia syndromes, DLB, BPSD, treatable contributors | — | **DISCARD** — §Dementias covers MCI, vascular, AD, LBD, FTLD, NPH and cognitive-enhancing drugs |
| 0.3 | **RUDAS** | `Corpus A/Investigation-Interpretation.md` Cognitive tools | **ADDITIVE** |
| 0.4 | Delirium / dementia / depression | — | **DISCARD** — §"3 Ds in Older People" is a purpose-built comparison |
| 0.5 | Amnesia | `Corpus A/04_Neurology.md` after §Dementias | **PARTIAL** — TGA and TEA only; Wernicke-Korsakoff is present ten times over |
| 0.6 | MCI and the "worried about my memory" consultation | — | **DISCARD** — §Mild Cognitive Impairment, including the point that dementia should not be diagnosed during an acute illness |

No new file required. **No `CONFLICT` raised.**
