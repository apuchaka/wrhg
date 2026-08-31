---
name: AN1 destination table
description: Where every section of Corpus B-new/AN1_Perioperative_Care.md goes, including the sections that were discarded.
bfile: Corpus B-new/AN1_Perioperative_Care.md
built: 2026-08-31
---

# AN1_Perioperative_Care — destination table

**30 concepts tested · 26 present · 4 absent.**
**Additive/discard ratio: 4 additive / 26 discard = 13% additive.**

## An eighteenth substring trap

`ERAS` returned **48 hits** — `cholinesterase` ×10, `topoisomerase` ×6,
`phosphodiesterase` ×6, `acetylcholinesterase` ×4, `polymerase` ×3. **Zero real.** A search
note is written into the merged block so the next reader is not misled the same way.

## Destination table

| AN1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | The four purposes of preoperative assessment; risk stratification tools | — | **DISCARD** — `03a_Anaesthetics_Primer:17` Pre-op checks |
| 0.1 | **Do not stop DAPT after a recent coronary stent** | — | **DISCARD** — 5 `dual antiplatelet` hits; `01_Cardiovascular` and `NEW_Drugs_06` |
| 0.1 | **Preoperative anaemia should be found and treated weeks in advance** | `Corpus A/03a_Anaesthetics_Primer.md` | **ADDITIVE** — 0 hits, base-A 0. The 2 `iron infusion` hits are not perioperative. The most modifiable preoperative risk factor, routinely found the day before when nothing can be done |
| 0.1 | **Prehabilitation and ERAS** | `Corpus A/03a_Anaesthetics_Primer.md` | **ADDITIVE** — `prehabilitation` 0, `carbohydrate drink` 0, both base-A 0, and `ERAS` is unusable as a pattern (see above) |
| 0.1 | Do not order routine preoperative investigations in well patients | — | **DISCARD** — `03a:17` |
| 0.2 | Predictors of a difficult airway | — | **DISCARD** — `Examination:300`, `03a` Airway Adjuncts |
| 0.2 | Regional anaesthesia; **new back pain with deficit after neuraxial is an emergency**; post-dural puncture headache | — | **DISCARD** — 1 `epidural haematoma` and 2 `post-dural puncture` hits |
| 0.2 | **Local anaesthetic systemic toxicity — lipid emulsion** | — | **DISCARD** — 8 `lipid emulsion` hits; `NEW_Drugs_02_Anaesthetics:77` names the LAST protocol and says the doses come from the poster, not from memory |
| 0.3 | Drugs to continue and to withhold; **SGLT2 and GLP-1 are the two newest** | — | **DISCARD** — 27 `SGLT2` and 20 `GLP-1` hits; `06_Metabolic:0.15.7` Perioperative Diabetes Management, which also carries the AU-specific BGL targets |
| 0.3 | Diabetes management around surgery | — | **DISCARD** — `06_Metabolic:0.15.7` and `:562` |
| 0.3 | **Patients are fasted far longer than necessary** | — | **DISCARD in part** — `03a:43` Pre-op instructions covers fasting; the carbohydrate-drink and shortened-fasting element is folded into the prehabilitation block rather than merged twice |
| 0.3 | Perioperative fluids — the two errors | — | **DISCARD** — `03a`, `NEW_Drugs_07_Blood_and_Electrolytes` |
| 0.4 | Post-operative complications by timing; the deteriorating patient | — | **DISCARD** — `03a:348–356`, including the 5 Ws and the anastomotic leak block from an earlier merge, and CF-035 written this run |
| 0.4 | **Perioperative myocardial infarction is frequently SILENT** | `Corpus A/03a_Anaesthetics_Primer.md` | **ADDITIVE** — 34 `silent` hits and **none** pairs it with perioperative or post-operative. The post-op fever timeline handles the febrile patient; this is the differential for the one who is not febrile and not right |
| 0.4 | Postoperative hypoxia; the common treatable problems | — | **DISCARD** — `03a`, `02_Respiratory` |
| 0.5 | Multimodal analgesia; PCA and the sedation score | — | **DISCARD** — 2 `sedation score` hits |
| 0.5 | **Discharge opioid prescribing drives persistent opioid use**, and the opposite error in patients on opioid agonist therapy | `Corpus A/03a_Anaesthetics_Primer.md` | **ADDITIVE** — `persistent opioid` 0 and base-A 0; `opioid agonist therapy` 0. 14 `buprenorphine` and 17 `methadone` hits exist but only 2 touch surgery at all |
| 0.6 | **The steroid-dependent patient** | — | **DISCARD** — `NEW_Drugs_10_Endocrine` and the hydrocortisone cover pattern quoted in CLAUDE.md §1.6 |
| 0.6 | **The frail older patient — "can we" versus "should we"** | — | **DISCARD** — `18_Geriatrics`, `GER2`-derived goals-of-care content |

## NO-BASELINE

All four blocks. `preoperative anaemia`, `prehabilitation`, `carbohydrate drink` and
`persistent opioid` all return 0 in Corpus A and C at base-A.

## Figure discipline

**No dose or threshold is stated.** The haemoglobin and ferritin triggers carry an
`UNVERIFIED` marker naming the **National Blood Authority** Patient Blood Management
guidelines. The single number in the block is "the first 48 hours", which is a timing
statement about when perioperative infarction occurs, not a dose.

## New files

**None.**
