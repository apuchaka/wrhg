---
bfile: Corpus B/B1_Chest_Pain_Framework_and_Cardiac_Biomarkers.md
sections: 5 (0.1–0.5), 20 headings
date: 2026-08-31
prestep: _meta/merges/B_BLOCK_PRESTEP.md
---

# B1 — destination table

Every section, its destination, and its disposition **including discarded ones** (§1.10).
The discard rows are the point: supersession otherwise leaves no trace, so a wrong
supersede is invisible and nothing can audit it.

Supersession is on **provenance, never content** (§1.10). Corpus C is `snippet`, Corpus A
is `inherited`; B is `unverified` and **can never win automatically**.

## Gap-check scope

Every claim was searched across **`Corpus A` and `Corpus C` together**, with the
destination file **included** — rule 10. Zero results were re-searched by **components
rather than name** — rule 2. The pre-step supplied the named-instrument list.

## Dispositions

| B1 § | Claim | Destination | Disposition |
|---|---|---|---|
| 0.1 | "The six that kill" framework — ACS, PE, dissection, tension pneumothorax, Boerhaave, tamponade | `NEW_Cardiology_and_Vascular.md:20` | **SUPERSEDED** — C states the identical six, and frames it the same way ("the intern's task is not to reach the diagnosis but to exclude the lethal causes") |
| 0.1 | Atypical presentation in women, diabetes, elderly, CKD | `NEW_Cardiology_and_Vascular.md:36` | **SUPERSEDED** — *"'atypical' is a description of the pain, not evidence against the diagnosis"* |
| 0.1 | Dissection anticoagulated by mistake | `NEW_Cardiology_and_Vascular.md:36` | **SUPERSEDED** — C names it as one of the two errors that cause real harm |
| 0.1 | ECG within 10 minutes of arrival | `NEW_Cardiology_and_Vascular.md:28` | **SUPERSEDED** |
| 0.1 | D-dimer only within a risk pathway | `NEW_Cardiology_and_Vascular.md:31` | **SUPERSEDED** — C adds that the error runs in both directions |
| 0.1 | ST depression V1–V3 = posterior STEMI, posterior leads V7–V9 | `01_Cardiovascular.md:46` | **SUPERSEDED** |
| 0.1 | New LBBB is a STEMI equivalent | `01_Cardiovascular.md:33`, `:509` | **SUPERSEDED** |
| 0.1 | Bilateral blood pressures, Beck's triad, pulse deficit | `NEW_Cardiology_and_Vascular.md:27` | **SUPERSEDED** |
| 0.1 | Cardiac rehabilitation and secondary prevention | `01_Cardiovascular.md:81` §0.1.5 | **SUPERSEDED** |
| **0.1** | **Right-sided leads (V4R) for inferior STEMI; RV infarct is preload-dependent, needs fluid not nitrate** | **`01_Cardiovascular.md` §0.1, at the reciprocal-change / posterior-lead block** | **ADDITIVE** — `V4R` and `right-sided lead` are **0 vault-wide**. The *management* half exists at `NEW_Drugs_06:167` (nitrates contraindicated in RV/inferior MI, "a preload-dependent ventricle"); the **diagnostic** half does not. A reader is told what not to give and never how to recognise the patient |
| **0.1** | **Oxygen only if hypoxaemic — routine oxygen in normoxic ACS is not beneficial and may be harmful** | **`01_Cardiovascular.md` §0.1.1 Mx – Immediate** | **ADDITIVE** — 0 hits vault-wide for oxygen restraint in ACS |
| **0.1** | **A validated accelerated diagnostic protocol exists and Australian EDs use one** | **`01_Cardiovascular.md` §0.1 Ix** | **ADDITIVE** — `HEART score`, `EDACS`, `accelerated diagnostic` all 0 (pre-step). Named as a class only; **no components or cut-offs**, which are site- and assay-specific |
| **0.1** | **Why heart rate is controlled before blood pressure in dissection — reduce shear stress; a vasodilator first causes reflex tachycardia and increases shear** | **`01_Cardiovascular.md` §0.36.5 Aortic Dissection** | **ADDITIVE** — A already states the *rule* ("strict BP/HR control… IV β-blocker first-line") and **not the reason**. This is the two-sampling-round lesson exactly: the recommendation is present, the caveat inside it is not |
| 0.2 | Typical / atypical / non-anginal three-feature classification | `01_Cardiovascular.md:224` | **SUPERSEDED** |
| 0.2 | CT coronary angiography as first-line non-invasive test | `01_Cardiovascular.md:226` | **SUPERSEDED** — A's stepped pathway (CTCA → functional imaging → invasive) is **fuller than B1's**. The acronym `CTCA` is 0 vault-wide, which is why the pre-step's acronym comparison flagged it; the expansion was in the destination file all along |
| 0.2 | Demand ischaemia mechanism; crescendo pattern = unstable angina | `01_Cardiovascular.md:18`, `:81` | **SUPERSEDED** |
| 0.2 | Non-cardiac chronic chest pain — GORD, spasm, costochondritis, zoster, anxiety | `NEW_Cardiology_and_Vascular.md:23–25` | **SUPERSEDED** — including *"herpes zoster (pain precedes the rash — a recognised early misdiagnosis)"* |
| **0.2** | **Angina severity is graded by exertional threshold (Canadian Cardiovascular Society class)** | **`01_Cardiovascular.md` stable angina** | **ADDITIVE, name only** — 0 hits. **Class descriptors omitted**; B1 marks them `UNVERIFIED` and they are not reproduced from model knowledge |
| 0.3 | Pericarditis vs STEMI — positional pain, widespread concave ST, PR depression, absent reciprocal change | `01_Cardiovascular.md:1151` §0.32, `NEW_Cardiology_and_Vascular.md:57` | **SUPERSEDED** — two independent existing sources |
| 0.3 | NSAID + colchicine; colchicine reduces recurrence | `01_Cardiovascular.md` §0.32 Mx | **SUPERSEDED** — A adds PPI cover and the ~3-month course |
| 0.3 | Activity restriction after pericarditis | `01_Cardiovascular.md` §0.32 Mx – Chronic | **SUPERSEDED** |
| 0.3 | Diaphragmatic pleural irritation refers to the shoulder tip | `History-Taking.md:224` | **SUPERSEDED** — already listed with ruptured ectopic, splenic pathology, subphrenic collection |
| 0.3 | Pleuritic pain does not exclude PE | `NEW_Cardiology_and_Vascular.md:52` §Pleuritic Chest Pain | **SUPERSEDED** |
| **0.3** | **The visceral pleura has no pain fibres; the parietal pleura is richly innervated — which is why pleuritic pain is sharp and well localised** | **`NEW_Cardiology_and_Vascular.md` §Pleuritic Chest Pain** | **ADDITIVE** — `parietal pleura` and `visceral pleura` are **0 vault-wide**. The corpus states the shoulder-tip *consequence* and never the innervation that produces it |
| **0.3** | **Myopericarditis — raised troponin, impaired function or arrhythmia in apparent pericarditis reclassifies the illness, with exercise restriction** | **`01_Cardiovascular.md` §0.32 Pericarditis** | **ADDITIVE** — myocarditis has **27 mentions and no entry**: it appears only as a complication of diphtheria, clozapine, Chagas, measles and Lyme. `myocarditis.*exercise` is **0** |
| 0.4 | Cocaine chest pain — benzodiazepines, avoid beta-blockers, unopposed alpha | `01_Cardiovascular.md:103`, `14a-1:53`, `14a-1:60` | **SUPERSEDED** — three existing places |
| **0.4** | **Coronary vasospasm as an entity** — the nocturnal/rest pattern with preserved exercise tolerance, non-stimulant triggers, CCB first-line with beta-blockers avoided, and the diagnostic point that the ECG must be captured **during** pain | **`01_Cardiovascular.md` new subsection under §0.9** | **ADDITIVE — the largest block in B1.** `Prinzmetal` appears **once**, as an item in an ST-elevation causes list at `:528`. There is no entity, no pattern, no management. `PENDING_GUIDELINE_CHECKS` **P5-A30** already flags coronary vasospasm as one of "the cardiovascular four" |
| **0.4** | **MINOCA and INOCA; SCAD in younger women including peripartum** | **with the vasospasm block** | **ADDITIVE** — `MINOCA` 0; `INOCA` 0 (its 2 raw hits were **ech**INOCA**ndins**); `SCAD` and `spontaneous coronary` **0** (33 raw hits were all **ca**scad**e**). Three rule-9 artifacts on one row |
| 0.5 | Trend not single value; serial rise and/or fall | `Investigation-Interpretation.md:277` §1.12 | **SUPERSEDED** |
| 0.5 | Correlate with clinical picture and ECG, never in isolation | `Investigation-Interpretation.md` §1.12 pt 2 | **SUPERSEDED** |
| 0.5 | Non-ACS causes of a raised troponin | `Investigation-Interpretation.md` §1.12 pt 3 | **SUPERSEDED** — A's list is cross-referenced rather than bare |
| 0.5 | A single early normal troponin does not exclude ACS | `Investigation-Interpretation.md` §1.12 pt 4 | **SUPERSEDED** |
| 0.5 | BNP lowered in obesity | `NEW_Investigations_Cardiology.md:51` | **SUPERSEDED** |
| 0.5 | Age-adjusted D-dimer | `NEW_Investigations_Haematology_Part2.md:44`, `:362` | **SUPERSEDED** — recorded there as a deliberate figure omission |
| 0.5 | CK-MB useful for reinfarction | `01_Cardiovascular.md:470` | **SUPERSEDED** — A has the full marker-kinetics table |
| **0.5** | **Type 1 versus type 2 myocardial infarction** — plaque rupture with thrombus against supply-demand mismatch, and that **type 2 is treated by treating the precipitant** | **`Investigation-Interpretation.md` §1.12** | **ADDITIVE** — 0 hits for the nomenclature. A has "myocardial injury without atherothrombotic ACS" as a *category* and never the type 1 / type 2 split that decides whether the patient is anticoagulated |
| **0.5** | **Sex-specific 99th-percentile thresholds exist; a single threshold under-diagnoses in women** | **`Investigation-Interpretation.md` §1.12** | **ADDITIVE, principle only** — 0 hits. **No values**, which are assay-specific and login-gated |
| **0.5** | **Don't send a troponin without a reason; and state the classification explicitly in the discharge summary** | **`Investigation-Interpretation.md` §1.12** | **ADDITIVE** — 0 hits for either. A patient discharged with an unexplained "troponin rise" acquires a coronary-disease label that follows them for life |

## Round 2 — sampling the unusual items (standing method, Step 29)

Round 1 tested the headline claims and found 10 additive gaps. Round 2 sampled
**technique detail, the caveat inside a recommendation, and the reason behind a rule**
instead — 13 further probes. Most confirmed existing coverage:

| Probe | Result |
|---|---|
| Takotsubo | **Present** — `01_Cardiovascular.md:945` §0.27, its own section |
| PR elevation in aVR, exercise stress ECG, myoglobin, triptans, lung-sliding, POCUS | **Present** |
| Provocative spasm testing, magnesium as a spasm trigger | Absent, and **not merged** — specialist-centre testing and a marginal trigger, both below intern level |
| "A change in your usual angina means calling an ambulance" | **Dismissed** — `01_Cardiovascular.md:229` already carries the GTN escalation protocol ending in *"if still no relief, call emergency"*, and §0.2's crescendo point covers the clinical half |

**And it found the item round 1 missed, which is the most valuable single claim in B1:**

| **B1 §** | **Claim** | **Destination** | **Disposition** |
|---|---|---|---|
| **0.1** | **Response to treatment is not a diagnostic test in chest pain** — GTN relieves oesophageal spasm, so relief does not confirm cardiac pain; relief with antacid does not exclude it | **`01_Cardiovascular.md`, adjacent to the typical-angina triad at `:223`** | **ADDITIVE** |

`antacid.*(exclude\|diagnos)` and `GTN.*(not\|does not).*(diagnos\|confirm)` are both **0
vault-wide**, while **GTN response is used as a discriminator in four existing places** —
`History-Taking.md:29` (in SOCRATES), `01_Cardiovascular.md:26`, `:223` (the typical-angina
triad) and `:1143` (pericarditis "may mimic MI but not relieved by GTN").

### Why this was placed as additive rather than as a CONFLICT block

It was considered as one, because A is `inherited` and B is `unverified`, which is the
`CONFLICT`-and-retain-both row of §1.10. **It is a qualification, not a contradiction.**
A never claims that GTN relief *confirms* ACS — it uses relief as one of three features of
the typical-angina triad, which is standard and correct as written, and uses non-relief as
one pericarditis discriminator among several. B's point is against **over-reading** a
response, not against the triad. Nothing in A has to be withdrawn for B's caution to be
true, so there is no claim to adjudicate and no `CONFLICT` block is created.

It is placed **beside the triad at `:223`** rather than in a general warning, so a reader
meets the caution at the point where they meet the rule it qualifies.

**Recorded here so the call is auditable** — a wrong "not a conflict" decision is exactly
as invisible as a wrong supersede, and this table exists for that reason.

## Summary

| | n |
|---|---|
| Superseded | 22 |
| Round-2 probes confirming existing coverage or dismissed | 12 |
| **Additive** | **11** |
| Conflicts | 0 |

**No conflict block.** Nothing in B1 contradicts an existing figure or claim; every
difference was absence rather than disagreement.

## Figures

B1 states **no dose, threshold or reference range** — every one is either carried as an
`UNVERIFIED` marker naming its source or omitted with the omission stated in place. No
figure enters the vault from this merge, so the digit multiset of every destination file
is unchanged except where a new `V4R`, `V1–V3`, `V7–V9` or `C3–C5` lead/segment label is
introduced, and those are anatomical labels rather than quantities.
