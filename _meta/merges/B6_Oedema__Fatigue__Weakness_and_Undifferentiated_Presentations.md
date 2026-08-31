---
bfile: Corpus B/B6_Oedema__Fatigue__Weakness_and_Undifferentiated_Presentations.md
sections: 8 (0.1–0.8), 32 headings — the largest B file
date: 2026-08-31
prestep: _meta/merges/B_BLOCK_PRESTEP.md
tooling: gap-checked with scripts/gapcheck.py
---

# B6 — destination table

**324 lines, 8 sections, and 4 additives.** That is the honest yield: B6 covers general
medicine — oedema, fatigue, weakness, pain, lumps — and this is exactly the territory a
148-file general corpus already covers well. The pre-step predicted a low yield here too;
B6's 19 candidate names were almost all common acronyms (`ALP`, `B12`, `FVC`, `FNA`, `GCA`,
`PMR`, `SVC`, `CCP`) already present.

All verdicts via `gapcheck.py` — untruncated, destination corpora only, zeros re-searched by
component (rule 2).

## Superseded — the notable ones

| B6 § | Claim | Where it already is |
|---|---|---|
| 0.1 | **Look at the sacrum in a bedbound patient** | `NEW_Cardiology_and_Vascular.md:181` and `NEW_Respiratory.md:34` — *"peripheral and **sacral** oedema"* in both examination sequences |
| 0.1 | **DHP calcium channel blockers cause ankle oedema** | `01_Cardiovascular.md:196`, `:1240`; `NEW_Drug_Classes_Cardiovascular_Antihypertensives.md:47` — **fuller**: *"peripheral (ankle) oedema is the characteristic class effect"* |
| 0.2 | Systemic causes and their giveaways — HF, nephrotic, cirrhosis, CKD | `NEW_Cardiology_and_Vascular.md` §Heart Failure; `07_Renal_Medicine_and_Urology.md` |
| 0.3 | **Phlegmasia cerulea dolens** | `NEW_Orthopaedics_and_Trauma.md:53` — *"massive iliofemoral thrombosis (phlegmasia)"* |
| 0.3 | DVT until excluded; classical signs individually unreliable | `01_Cardiovascular.md` §0.29 with Wells |
| 0.3 | Cellulitis can coexist with DVT | `08_09_Infectious_Disease_-_Miscellaneous.md:23` |
| 0.4 | **Orbital versus preseptal cellulitis** | `05_Ophthalmology.md:681` — **its own section**, with the CT discriminator and the sight-loss rationale |
| 0.4 | **Angioedema — histamine versus bradykinin** | `01_Cardiovascular.md:1228` (ACE-i, *"may occur up to a year after starting"*); `10_09b_Haemonc.md:12` (**C1 inhibitor deficiency**, with the mechanism) |
| 0.4 | **SVC obstruction** | `10_10a_Haemonc.md:51` — its own section |
| 0.4 | Nephrotic periorbital oedema | 13 hits incl. `15_10_Paeds` and `07_Renal` |
| 0.5 | Iron deficiency **without** anaemia causes fatigue — check ferritin | 23 `ferritin` hits incl. the investigations entries |
| 0.5 | **ME/CFS** | `12_02_Rheum` §0.7, a full entry with a `[!info] Verified` box |
| 0.6 | **Monitor FVC, not oxygen saturation, in neuromuscular weakness** | **FIVE places** — `04_Neurology.md:1486` (a `[!danger]` box), `NEW_Drugs_15_Neurological.md:164`, `NEW_Investigations_Rheumatology.md:117`, `NEW_Neurology.md:141`, `NEW_Respiratory.md:46` |
| 0.6 | UMN versus LMN localisation | `04_Neurology.md`; `Examination.md` |
| 0.6 | **Polymyalgia rheumatica** | `12_02_Rheum` — a full entry |
| 0.7 | **Fibromyalgia is a positive diagnosis** | `12_02_Rheum` — a full entry |
| 0.8 | **Soft tissue sarcoma — do not biopsy before referral** | 19 `sarcoma` hits incl. the oncology files |
| 0.8 | Lipoma, epidermoid cyst with **central punctum**, ganglion | `09_08_Dermatology_-_Miscellaneous.md:216` |
| 0.8 | **Expansile** versus pulsatile mass | `03_Gastrointestinal.md:1704` — AAA, *"pulsatile expansile abdominal mass"* |

## Additive

| B6 § | Claim | Destination |
|---|---|---|
| 0.2 | **Bilateral simultaneous cellulitis is rare** — bilateral red, warm, swollen legs are far more often **venous stasis dermatitis or lipodermatosclerosis**, which are inflammatory and not infective | `08_09_Infectious_Disease_-_Miscellaneous.md` cellulitis entry |
| 0.3 | **May-Thurner syndrome** — left iliac vein compression as a cause of left-sided DVT in a young patient | `01_Cardiovascular.md` §0.29 DVT |
| 0.3 | **Stemmer's sign** — inability to pinch a skinfold at the base of the second toe | `NEW_Investigations_Haematology_Part2.md` lymphoedema block |
| 0.4 | **Pemberton's sign** — facial plethora and distress on raising both arms above the head | `10_10a_Haemonc.md` §SVCO |

## CORRECTION to the pre-step — lymphoedema IS covered

The B-block pre-step recorded lymphoedema as appearing *"only as a cellulitis risk factor"*
with *"no heading for lymphoedema anywhere in A or C."*

**The heading claim is true and the conclusion drawn from it is false.**
`NEW_Investigations_Haematology_Part2.md:324–339` carries a substantial lymphoedema block
inside the **lymphoscintigraphy** entry: assessment and confirmation of lymphatic
obstruction, excluding a treatable or dangerous cause, **cellulitis as the major and
recurrent complication**, **complex decongestive therapy as the mainstay rather than a
drug**, and that a rapidly progressive or painful "lymphoedema" raises malignancy.

**The search was for a heading. The content lives under someone else's heading.** That is the
paraphrase failure in a structural form — not "the corpus used different words" but "the
corpus filed it somewhere I did not think to look." A section-heading search is a *location*
assumption, and it fails exactly like an adjacency assumption.

So only **Stemmer's sign** is added, into the block that already exists — not a lymphoedema
entry, which the vault has in substance.

## Summary

| | n |
|---|---|
| Superseded | 19 |
| **Additive** | **4** |
| Conflicts | 0 |
| Pre-step claims corrected | 1 (lymphoedema) |

## Figures

B6 states **no figure** — node size thresholds, the sarcoma size cut-off and all reference
ranges carry `UNVERIFIED` markers or are omitted. **No figure enters the vault.**
