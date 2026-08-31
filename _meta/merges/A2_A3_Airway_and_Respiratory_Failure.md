---
bfiles:
  - Corpus B/A2_Airway_Compromise__Stridor_and_Tracheostomy_Emergencies.md
  - Corpus B/A3_Respiratory_Failure__Bronchospasm_and_Hypoxia.md
date: 2026-08-31
prestep: _meta/merges/A_BLOCK_PRESTEP.md
tooling: scripts/gapcheck.py
---

# A2 + A3 — destination table

Merged together because their gap checks overlap almost entirely (airway → wheeze →
hypoxaemia is one continuum in the corpus, spread across `13_05b_ENT`, `02_Respiratory` and
`03a_Anaesthetics_Primer`).

## The headline finding — tracheostomy emergencies are absent

**`tracheostomy` returns ONE hit in the whole of Corpus A and Corpus C**:
`03a_Anaesthetics_Primer.md:114`, a one-line definition of the surgical procedure.

There is **no** emergency content at all — no green/red algorithm, no
**tracheostomy-versus-laryngectomy** distinction, no displaced-tube management, no
tracheo-innominate fistula. `NTSP`, `tracheo-innominate` and `false passage` are all **0**.

This is a **ward emergency an intern is called to**, and it is the single largest absence
found in the A block.

## Superseded

| Claim | Where it already is |
|---|---|
| Croup versus epiglottitis; no throat examination; do not distress the child | `13_05b_ENT_-_Stridor__Croup__Epiglottitis__Laryngomalacia__OSA.md` — a whole file, 28 `croup` hits |
| Laryngomalacia — positional, improves prone, normal cry | `13_05b:79` |
| Inhaled foreign body in a child | 5 hits incl. `13_06b_ENT` (button battery, from the A8 merge) |
| ACE-inhibitor angioedema is bradykinin-mediated | `01_Cardiovascular.md:1228`; `10_09b_Haemonc.md:12` |
| Inhalation injury — carbonaceous sputum, singed nasal hair | `11_09b_Ortho_-_Trauma.md` burns |
| **Expanding post-operative neck haematoma obstructing the airway** | `NEW_Exam_Manoeuvres_and_Procedures.md:434` — named as a carotid endarterectomy complication *"which can rapidly obstruct the airway"* |
| Vocal cord palsy — weak breathy voice, find the cause | `13_06a_ENT_-_Dysphonia_and_HNSCC.md:18`; `NEW_ENT_and_Oral.md:62`, `:68` (with the CXR/CT workup) |
| Five mechanisms of hypoxaemia; V/Q mismatch, shunt | 38 hits incl. `Investigation-Interpretation.md` |
| Paradoxical abdominal movement | 30 hits |
| **Pulse oximetry lies in CO poisoning and methaemoglobinaemia** | 4 + 13 hits — `10_06b_Haemonc` has a **whole methaemoglobinaemia section** |
| Long-term oxygen therapy criteria | 2 hits |
| Bradypnoea / opioid-induced respiratory depression | 35 hits |
| Silent chest; falling respiratory rate as exhaustion | 9 hits |
| **Ophthalmic beta-blocker drops are systemically absorbed** | 9 `timolol` hits incl. `NEW_Drugs_11_Eye.md` |
| Respiratory rate is the most sensitive and most omitted observation | `NEW_Respiratory.md:31` |
| Compensation never fully corrects the pH | `NEW_Investigations_Orthopaedics_Neurology_and_Other.md:31` |

## Additive

| From | Claim | Destination |
|---|---|---|
| **A2 §0.4** | **Tracheostomy and laryngectomy emergencies** — the patent-upper-airway question first, the emergency sequence, the **displaced tube in a stoma less than a week old** (blind reinsertion creates a false passage), and **sentinel bleeding heralding a tracheo-innominate fistula** | `03a_Anaesthetics_Primer.md` §Airway Adjuncts |
| A2 §0.1 | **The timing of the noise localises the level** — inspiratory = supraglottic/glottic; expiratory = intrathoracic; **biphasic = subglottic or tracheal, the fixed lesion** | `13_05b_ENT` |
| A2 §0.2 | **Tracheal stenosis after prolonged intubation or tracheostomy** — treated repeatedly as "asthma" that does not respond to bronchodilators | `13_05b_ENT` |
| A2 §0.2 | **Bilateral vocal cord palsy gives a NEAR-NORMAL VOICE with stridor** — because the cords sit in the midline, which is exactly why it is missed | `13_06a_ENT` |
| **A3 §0.1** | **Type 1 becomes Type 2 when the patient tires** — the classification is not a fixed category, and **a rising CO₂ in a previously hypocapnic patient is exhaustion, not improvement** | `Investigation-Interpretation.md` ABG section |
| A3 §0.3 | **Wheeze is a sign, not a diagnosis** — in a patient with no airways history, exclude **anaphylaxis, pulmonary oedema ("cardiac asthma") and foreign body** before calling it asthma | `02_Respiratory.md` asthma entry |

## Summary

| | n |
|---|---|
| Superseded | 15 |
| **Additive** | **6** |
| Conflicts | 0 |

## Figures

Both files state **no figure** — all thresholds, saturations and the NTSP algorithm itself
carry `UNVERIFIED` markers naming their sources. **No figure enters the vault.** The
tracheostomy block explicitly directs the reader to the current **National Tracheostomy
Safety Project** algorithms rather than reproducing them.
