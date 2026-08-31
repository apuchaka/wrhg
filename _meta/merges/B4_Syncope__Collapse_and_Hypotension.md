---
bfile: Corpus B/B4_Syncope__Collapse_and_Hypotension.md
sections: 5 (0.1–0.5), 20 headings
date: 2026-08-31
prestep: _meta/merges/B_BLOCK_PRESTEP.md
---

# B4 — destination table

**B4 is the most superseded file in the block.** The pre-step already predicted it: B4
introduced **no named instrument** absent from `01_Cardiovascular` — the only three
candidates were `DURING`, `LOC` and `Pregnancy`, all noise. That was an accurate early
signal, and the full check bore it out.

Gap check across `Corpus A` and `Corpus C`, destination included (rule 10), every non-zero
set read **to its last hit and untruncated**.

## Superseded

| B4 § | Claim | Where it already is |
|---|---|---|
| 0.1 | TLoC splits into syncope, seizure, other | `History-Taking.md:73` — same split, with PNES and hypoglycaemia named |
| 0.1 | The collateral history is the investigation | `History-Taking.md:57–58` — the structured before/during/after collateral |
| 0.1 | Syncope versus seizure discriminators | `04_Neurology.md:891` — its own **Seizures vs Syncope** table. **See the CONFLICT below on one row of it** |
| 0.1 | **Lateral tongue bite suggests seizure** | `History-Taking.md:57` — *"tongue-biting (lateral suggests seizure)"*. **See Dropped** |
| 0.1 | **Convulsive syncope** — brief myoclonic jerks occur in ordinary syncope | `History-Taking.md:57` — *"brief myoclonic jerks can occur in simple syncope too, not just seizure"*, **with the timing-relative-to-the-fall point B4 makes** |
| 0.1 | Rapid recovery vs prolonged postictal confusion | `History-Taking.md:58`; `04_Neurology.md:893` table |
| 0.2 | Reflex / orthostatic / cardiac | `NEW_Cardiology_and_Vascular.md:104–106` — all three, with autonomic failure named |
| 0.2 | **Situational syncope** — micturition, defaecation, cough, swallow | `NEW_Cardiology_and_Vascular.md:105`. **See Dropped** |
| 0.2 | Carotid sinus hypersensitivity | `NEW_Cardiology_and_Vascular.md:105` |
| 0.2 | Red flags — exertion, supine, no prodrome, palpitations, structural disease, abnormal ECG | `NEW_Cardiology_and_Vascular.md:111` — **the same list, as a `[!danger]` box** |
| 0.2 | The ECG hunt list — long/short QT, Brugada, pre-excitation, ARVC | `NEW_Cardiology_and_Vascular.md:110`; `01_Cardiovascular.md` §0.25 carries the **epsilon wave** |
| 0.2 | Orthostatic hypotension; drugs are the commonest cause | `NEW_Cardiology_and_Vascular.md:104` — the drug list is **longer than B4's** |
| 0.2 | Lying and standing BP measured over several minutes | `NEW_Cardiology_and_Vascular.md:109` — *"after lying for several minutes, then at intervals after standing"* |
| 0.3 | Presyncope has the same causes and significance as syncope | `04_Neurology.md:984` |
| 0.3 | "Dizzy" means four different things | `History-Taking.md:686` and the vertigo/presyncope/disequilibrium split cross-referenced to `13_02` |
| 0.4 | **"Mechanical fall" is not a diagnosis** | `18_Geriatrics_and_Older_Persons_Health.md:20` — **fuller than B4**: *"a fall is a symptom, not a diagnosis… writing it in the notes closes an assessment that should be opening one"*, with the multifactorial point |
| 0.4 | The long lie — rhabdomyolysis, AKI, hypothermia, pressure injury | `18_Geriatrics`, `07_Renal_Medicine_and_Urology.md:24`, `11_01_Ortho.md:67` — three files, including that it *"independently signals that the person cannot summon help"* |
| 0.4 | Multifactorial falls assessment | `18_Geriatrics`; `Communication.md:595` falls-history checklist |
| 0.5 | **Hypotension is relative to the patient's own baseline** | `NEW_Cardiology_and_Vascular.md:114` — *"a blood pressure low **for that patient**… A systolic of 95 mmHg is normal in a young woman and shock in a chronic hypertensive."* **See Dropped** |
| 0.5 | The four shock phenotypes | `NEW_Cardiology_and_Vascular.md:115–118` — **fuller than B4**, adding dynamic hyperinflation and drug toxicity |
| 0.5 | Occult haemorrhage — retroperitoneal | `NEW_Cardiology_and_Vascular.md:115` — *"retroperitoneal bleed on anticoagulation"* |
| 0.5 | **Acidosis impairs catecholamine responsiveness** | Present in the fluids entry — *"hyperchloraemic metabolic acidosis, which can itself impair cardiac contractility, adrenoceptor function"* |
| 0.5 | Tamponade and tension pneumothorax are not fluid-responsive | `NEW_Cardiology_and_Vascular.md:118` obstructive phenotype |

## CONFLICT

| ID | Topic | Risk |
|---|---|---|
| **CF-033** | **Does urinary incontinence discriminate seizure from syncope?** | **R2** |

`04_Neurology.md:893` **Seizures vs Syncope** table: *"Incontinence — Seizures: More common ·
Syncope: Rare."* B4 §0.1: *"Urinary incontinence occurs in both syncope and seizure and is
**not** a useful discriminator, despite being taught as one."*

**These cannot both be acted on.** A reader using the table treats incontinence as evidence
for seizure; a reader using B4 discards it. **R2 because it drives disposition** — the
patient wrongly labelled epileptic is started on antiepileptic drugs and loses their
licence, which is the consequence B4 names explicitly for the neighbouring convulsive-syncope
trap.

**Not adjudicated** (§1.12). Both claims stay in the text; the block sits above the table.

## Additive

| B4 § | Claim | Destination |
|---|---|---|
| 0.5 | **Adrenal insufficiency causes vasoplegia that does not respond to noradrenaline** — cortisol is required for vascular responsiveness to catecholamines. Look for hyponatraemia with hyperkalaemia and hypoglycaemia | `NEW_Cardiology_and_Vascular.md` §Hypotension |
| 0.5 | **Iatrogenic hypotension is the commonest cause of an inpatient hypotension call** — antihypertensives continued in a patient now dry or septic, opioids and sedatives, neuraxial anaesthesia | `NEW_Cardiology_and_Vascular.md` §Hypotension |

## Dropped at placement — three, all mine, three different mechanisms

| Claim | Why the search said absent | Where it was |
|---|---|---|
| **Situational syncope** | Searched `situational syncope\|micturition syncope\|cough syncope` — every alternative required the word *syncope* **adjacent**. 0 hits | `NEW_Cardiology_and_Vascular.md:105` — *"situational (micturition, defaecation, cough, swallow)"*. Searching `micturition` **alone** found it instantly. This is Step 29's word-order check: **search the rarer word alone, never the phrase** |
| **Hypotension is relative to baseline** | Searched `own baseline\|relative hypotension\|usual blood pressure` — 0. The corpus writes *"low **for that patient**"* | `NEW_Cardiology_and_Vascular.md:114`, with a worked example. **A paraphrase is not a pattern** |
| **Lateral tongue bite is highly specific** | Read `History-Taking.md:57` through `cut -c1-160`, which ended at `tongue-biting (lat` | The same line continues *"(lateral suggests seizure)"* — **truncation again, on the very line I had already quoted for a different claim** |

**Three drops, three distinct causes: adjacency, paraphrase, truncation.** None was a wrong
scope and none was a wrong corpus — rule 10's original clauses would have passed all three.
The one that caught them was **rule 2's component re-search**, run on every zero result
before recording it.

## Summary

| | n |
|---|---|
| Superseded | 22 |
| **Additive merged** | **2** |
| **Conflicts raised** | **1 (CF-033, R2)** |
| Dropped at placement | 3 |

**A 2-additive result is the honest one for this file**, and the pre-step predicted it: B4
introduced no named instrument the destination lacked. **The conflict is worth more than the
two additives** — it is the first claim in the whole B block that contradicts rather than
extends the corpus.

## Figures

B4 states **no figure**. The orthostatic-drop thresholds carry an `UNVERIFIED` marker. **No
figure enters the vault.**
