---
name: D3 destination table
description: Where every section of Corpus B/D3_Stroke_and_Focal_Neurological_Deficit.md goes, including the sections that were discarded.
bfile: Corpus B/D3_Stroke_and_Focal_Neurological_Deficit.md
built: 2026-08-31
---

# D3_Stroke_and_Focal_Neurological_Deficit — destination table

Committed **before** any content was written. 4 483 words, 7 sections.
**1 placement · 6 discards.**

## The required eponym check earned its place twice on this file

Two scores came back **ABSENT** and are **present**, both defeated by **Unicode digits** —
CLAUDE.md rule 2's named case, which no amount of word-order care would have caught.

| Score | My search | Reality |
|---|---|---|
| `ABCD2` | ABSENT | **`04_Neurology` L1104 has `ABCD²` with a SUPERSCRIPT ²** — and every component (Age ≥60, BP ≥140/90, Clinical features, Duration, Diabetes), plus an Australian caution about using it in isolation |
| `CHA2DS2-VASc` | ABSENT on name; components flagged present | **`01_Cardiovascular` L290 has `CHA₂DS₂-VASc` with SUBSCRIPT ₂**, alongside ORBIT and the reasoning that a bleeding score does not decide whether to anticoagulate |

Had either been merged, the corpus would have carried the same score twice under two
renderings — the exact C7 `Glasgow-Imrie` failure, in a file where the duplicate would sit
in a *different* file from the original and be correspondingly harder to notice.

**Search rule added: fold sub- and superscript digits to ASCII before searching.** The
re-run with folding confirmed both, and confirmed the remaining absences were real.

**A third rule-9 artifact on the same search:** `vasc` matched **Cardio*vasc*ular** in four
files, so the first CHA₂DS₂-VASc search looked like it had hits when it had none of the
right kind.

## Component-search results

| Instrument | Verdict |
|---|---|
| NIHSS, ROSIER/FAST, Bamford-Oxford (TACS/PACS/LACS/POCS), thrombolysis window, thrombectomy, CT perfusion, lacunar syndromes, Wallenberg, Brown-Séquard, Todd's paresis, carotid endarterectomy, UMN vs LMN, Broca/Wernicke | **present** |
| ABCD², CHA₂DS₂-VASc | **present**, via Unicode folding — see above |
| **HINTS examination** | **present** — `04_Neurology`, `Examination` |
| **permissive hypertension** | **present in Corpus C** (`NEW_Cardiology_and_Vascular`) — superseded on provenance |
| **Weber syndrome / medial midbrain**, **Millard-Gubler**, **BP target in ICH**, **pronator drift**, **locked-in syndrome**, **stroke chameleons** | **absent** |

## Gaps this merge does not close

- **Weber syndrome and Millard-Gubler** — absent from the vault **and from D3**. Brainstem
  stroke syndromes are represented only by Wallenberg. Added to the study list.
- **The BP target in intracerebral haemorrhage** — a **figure**, which D3 itself marks
  `UNVERIFIED` and does not state. Not written.
- **The penumbra being pressure-dependent** — the mechanism behind permissive hypertension.
  `NEW_Cardiology_and_Vascular` owns permissive hypertension itself, so adding the
  mechanism there would extend a Corpus C section on model knowledge alone. Recorded, not
  merged.

## Destination table

| D3 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Acute stroke recognition, hyperacute management, thrombolysis, thrombectomy, BP | — | **DISCARD** — `04_Neurology` §Ischaemic Stroke and §Haemorrhagic Stroke; BP direction is in `NEW_Cardiology_and_Vascular` |
| 0.2 | Stroke syndromes and localisation | — | **DISCARD** — §Arterial Territory Syndromes and §Bamford-Oxford Classification |
| 0.3 | TIA and secondary prevention | — | **DISCARD** — §Transient Ischaemic Attack, with `ABCD²` in full and the AU caution |
| 0.4 | Intracerebral haemorrhage | — | **DISCARD** — §Haemorrhagic Stroke, §Brain Bleeds; the BP target is a figure D3 does not state |
| 0.5 | **Stroke chameleons** | `Corpus A/04_Neurology.md` §Strokes | **PARTIAL** — chameleons only; mimics are already in §Weakness — DDx and §Seizures |
| 0.6 | Paresis patterns; **locked-in syndrome** | `Corpus A/04_Neurology.md` §Strokes | **PARTIAL** — locked-in and pronator drift only; UMN/LMN and the paresis patterns are in §Weakness — DDx |
| 0.7 | Subacute and chronic focal deficit | — | **DISCARD** — §Brain Tumours, §Multiple Sclerosis, §Brain Lesion Localisation |

No new file required. **No `CONFLICT` raised.**
