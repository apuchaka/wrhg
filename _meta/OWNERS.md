---
name: owners
description: Which file owns each drug's dose figures, for which population, and — critically — the RANGE that owner's table actually covers. A pointer to an incomplete owner is worse than a local figure, because nothing signals the failure.
---

# `_meta/OWNERS.md` — dose ownership registry

Generated 2026-08-30 by measurement (Step 28d): every line in all 240 corpus files matching
the dose pattern, grouped by drug. **Range is recorded, not just location** — B50 is the case
where two files pointed at an ASCIA table that stopped at 7.5 kg, so a reader following the
pointer for an infant reached a table that did not cover them.

> [!danger] **Adrenaline for anaphylaxis has THREE locations, not two.**
> `PENDING_GUIDELINE_CHECKS.md` **B71** records two owners. Measured, there are three:
> `09_01_Dermatology` (`0.01 mg/kg`, max `0.5 mg`), `NEW_Drugs_01` (`0.01 mL/kg`, max
> `0.5 mL`, injector bands **from 7.5 kg**) and `15_01b_Paeds_-_Anaphylaxis` (an ASCIA
> verified box). **The two that state a figure express the same dose in different units** —
> mg in one, mL in the other — which is exactly how two owners drift without either looking
> wrong. B71 should be updated to three.

> [!warning] **Cardiac-arrest adrenaline is a SEPARATE fact and is correctly separate.**
> `01_Cardiovascular` `1 mg` (adult) and `15_01a_Paeds` `10 mcg/kg` (paediatric) are a
> different indication from anaphylaxis. Do not consolidate them with the ASCIA table.

## Drugs whose dose figures appear in more than one file

**31 of 43 drugs.** Step 12 governs the same-fact-in-3+-files consistency pass;
this table makes the candidates mechanical.

| Drug | Files | Population(s) | Range the figures state | Owner status |
|---|---|---|---|---|
| `prednisolone` | 9 | mixed, paed | 2 weeks · 3 months · 4 weeks | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `04_Neurology` · `11_08b_Ortho_-_Paget_s_Disease_and_Osteoporo` · `12_02_Rheum_-_Ankylosing_Spondylitis__Gout__` · `12_04_Rheum_-_Vasculitis` · `13_03_ENT_-_Deafness_and_Vertigo_Conditions` … |
| `ceftriaxone` | 8 | adult, mixed, paed | 1 year · children · infants | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `04_Neurology` · `07_Renal_Medicine_and_Urology` · `08_08_Infectious_Disease_-_Genitourinary_Inf` · `15_02_Paeds_-_Ill_and_Feverish_Child__Mening` · `16_06-07_Ante-Perinatal_Infections` … |
| `dexamethasone` | 7 | mixed, paed | 3 months · children | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `03a_Anaesthetics_Primer` · `04_Neurology` · `11_01_Ortho_-_Orthopaedic_Emergencies` · `13_05b_ENT_-_Stridor__Croup__Epiglottitis__L` · `15_02_Paeds_-_Ill_and_Feverish_Child__Mening` … |
| `adrenaline` | 6 | mixed, paed | all ages · children · paediatric | **3+ files — Step 12 pass required** |
| | | | | `01_Cardiovascular` · `09_01_Dermatology_-_Dermatological_Emergenci` · `15_01a_Paeds_-_Paediatric_and_Newborn_Life_S` · `15_01b_Paeds_-_Anaphylaxis` · `15_04a_Paeds_-_URTI_and_LRTI` · `NEW_Drugs_01_Allergy_and_Anaphylaxis` |
| `amoxicillin` | 6 | adult, mixed | 2 weeks | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `03_Gastrointestinal` · `07_Renal_Medicine_and_Urology` · `08_09_Infectious_Disease_-_Miscellaneous` · `13_01_ENT_-_Otalgia__Otitis_Externa__Otitis_` · `13_07c_ENT_-_Dental_and_Teeth_Problems` |
| `doxycycline` | 6 | adult, mixed | 2 weeks | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `07_Renal_Medicine_and_Urology` · `08_08_Infectious_Disease_-_Genitourinary_Inf` · `08_09_Infectious_Disease_-_Miscellaneous` · `17_05_PID__Endometriosis__Fibroids` · `17_08_Vaginal_Discharge__Urinary_Incontinenc` |
| `metronidazole` | 6 | adult, mixed | 3 months | **3+ files — Step 12 pass required** |
| | | | | `03_Gastrointestinal` · `08_08_Infectious_Disease_-_Genitourinary_Inf` · `08_09_Infectious_Disease_-_Miscellaneous` · `13_07c_ENT_-_Dental_and_Teeth_Problems` · `17_05_PID__Endometriosis__Fibroids` · `17_08_Vaginal_Discharge__Urinary_Incontinenc` |
| `glucose` | 6 | adult, mixed, paed | adult · children · paediatric | **3+ files — Step 12 pass required** |
| | | | | `03a_Anaesthetics_Primer` · `06_Metabolic_Medicine_and_Endocrinology` · `10_03b_Haemonc_-_Acute_Intermittent_Porphyri` · `15_12a_Paeds_-_Epilepsy_Syndromes_and_Status` · `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA` · `NEW_Investigations_Endocrine` |
| `aciclovir` | 5 | mixed, paed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `04_Neurology` · `08_05-06_Infectious_Disease_-_Viral_Infectio` · `09_01_Dermatology_-_Dermatological_Emergenci` · `15_02_Paeds_-_Ill_and_Feverish_Child__Mening` · `16_06-07_Ante-Perinatal_Infections` |
| `azithromycin` | 5 | adult, mixed | 3 weeks · paediatric | **3+ files — Step 12 pass required** |
| | | | | `07_Renal_Medicine_and_Urology` · `08_08_Infectious_Disease_-_Genitourinary_Inf` · `16_06-07_Ante-Perinatal_Infections` · `17_05_PID__Endometriosis__Fibroids` · `17_08_Vaginal_Discharge__Urinary_Incontinenc` |
| `diazepam` | 4 | mixed, paed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `03_Gastrointestinal` · `04_Neurology` · `15_12a_Paeds_-_Epilepsy_Syndromes_and_Status` · `16_14-15_Obstetric_Emergencies` |
| `dextrose` | 4 | adult, mixed, paed | adult · paediatric | **3+ files — Step 12 pass required** |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `10_03b_Haemonc_-_Acute_Intermittent_Porphyri` · `15_08_Paeds_-_Surgical_Abdomen__Appendicitis` · `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA` |
| `potassium` | 4 | mixed | adult | **3+ files — Step 12 pass required** |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `17_03_Termination_of_Pregnancy_and_Miscarria` · `NEW_Drugs_07_Blood_and_Electrolytes` · `NEW_Drugs_12_Gastrointestinal` |
| `magnesium` | 4 | mixed, paed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `15_04b_Paeds_-_Asthma_in_Children` · `16_08-09_Antenatal_and_Perinatal_Problems` · `16_14-15_Obstetric_Emergencies` · `NEW_Drugs_07_Blood_and_Electrolytes` |
| `anti-d` | 4 | mixed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `16_01-05_Antenatal_Care` · `17_03_Termination_of_Pregnancy_and_Miscarria` · `17_04_Ectopic_Pregnancy_and_GTD` · `NEW_Drugs_16_Obstetric_and_Gynaecological` |
| `paracetamol` | 3 | mixed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `01_Cardiovascular` · `03_Gastrointestinal` · `07_Renal_Medicine_and_Urology` |
| `morphine` | 3 | adult, mixed, paed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `01_Cardiovascular` · `10_11c_Oncology_-_Palliative_Care_Prescribin` · `15_08_Paeds_-_Surgical_Abdomen__Appendicitis` |
| `warfarin` | 3 | mixed | 70kg | **3+ files — Step 12 pass required** |
| | | | | `01_Cardiovascular` · `10_08_Haemonc_-_Blood_Products_and_Transfusi` · `16_01-05_Antenatal_Care` |
| `vancomycin` | 3 | mixed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `02_Respiratory` · `04_Neurology` · `08_01-03_Infectious_Disease_-_Bacterial_Infe` |
| `lorazepam` | 3 | mixed, paed | **RANGE NOT STATED** | **3+ files — Step 12 pass required** |
| | | | | `03_Gastrointestinal` · `15_12a_Paeds_-_Epilepsy_Syndromes_and_Status` · `16_01-05_Antenatal_Care` |
| `benzylpenicillin` | 3 | mixed | 10 years | **3+ files — Step 12 pass required** |
| | | | | `04_Neurology` · `08_01-03_Infectious_Disease_-_Bacterial_Infe` · `16_06-07_Ante-Perinatal_Infections` |
| `hydrocortisone` | 3 | mixed | 4 weeks | **3+ files — Step 12 pass required** |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `16_01-05_Antenatal_Care` · `NEW_Drugs_10_Endocrine` |
| `amiodarone` | 2 | mixed, paed | paediatric | two files — confirm one owner |
| | | | | `01_Cardiovascular` · `15_01a_Paeds_-_Paediatric_and_Newborn_Life_S` |
| `insulin` | 2 | mixed | **RANGE NOT STATED** | two files — confirm one owner |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `NEW_Investigations_Endocrine` |
| `glucagon` | 2 | mixed, paed | 25kg · 8 years · paediatric | two files — confirm one owner |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `15_16b_Paeds_-_Diabetes_Mellitus__MODY__DKA` |
| `calcium gluconate` | 2 | mixed | adult · paediatric | two files — confirm one owner |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `16_14-15_Obstetric_Emergencies` |
| `salbutamol` | 2 | mixed, paed | adult · paediatric | two files — confirm one owner |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `15_04b_Paeds_-_Asthma_in_Children` |
| `furosemide` | 2 | mixed | **RANGE NOT STATED** | two files — confirm one owner |
| | | | | `06_Metabolic_Medicine_and_Endocrinology` · `07_Renal_Medicine_and_Urology` |
| `vitamin k` | 2 | mixed | **RANGE NOT STATED** | two files — confirm one owner |
| | | | | `10_08_Haemonc_-_Blood_Products_and_Transfusi` · `16_01-05_Antenatal_Care` |
| `midazolam` | 2 | mixed, paed | **RANGE NOT STATED** | two files — confirm one owner |
| | | | | `15_12a_Paeds_-_Epilepsy_Syndromes_and_Status` · `16_14-15_Obstetric_Emergencies` |
| `oxytocin` | 2 | mixed | **RANGE NOT STATED** | two files — confirm one owner |
| | | | | `16_10-13_Labour_and_Delivery` · `16_14-15_Obstetric_Emergencies` |

## Single-owner drugs

These state a dose in exactly one file, so the owner is unambiguous. Listed so a future
session can tell *unambiguous* from *unexamined*.

| Drug | Owner | Population | Range |
|---|---|---|---|
| `adenosine` | `01_Cardiovascular` | mixed | **RANGE NOT STATED** |
| `enoxaparin` | `16_01-05_Antenatal_Care` | mixed | 130kg · 170kg · 171kg · 50kg · 90kg |
| `fentanyl` | `10_11c_Oncology_-_Palliative_Care_Prescribing` | adult | **RANGE NOT STATED** |
| `flucloxacillin` | `08_09_Infectious_Disease_-_Miscellaneous` | mixed | **RANGE NOT STATED** |
| `gentamicin` | `16_06-07_Ante-Perinatal_Infections` | mixed | neonatal |
| `gtn` | `01_Cardiovascular` | mixed | **RANGE NOT STATED** |
| `heparin` | `16_01-05_Antenatal_Care` | mixed | **RANGE NOT STATED** |
| `hypertonic saline` | `06_Metabolic_Medicine_and_Endocrinology` | mixed | **RANGE NOT STATED** |
| `ibuprofen` | `07_Renal_Medicine_and_Urology` | mixed | **RANGE NOT STATED** |
| `methylprednisolone` | `12_04_Rheum_-_Vasculitis` | mixed | **RANGE NOT STATED** |
| `naloxone` | `14a-1_Psych_-_Substance_Misuse__Recreational_Drug_Profiles_` | adult | **RANGE NOT STATED** |
| `phenytoin` | `15_12a_Paeds_-_Epilepsy_Syndromes_and_Status_Epilepticus` | paed | **RANGE NOT STATED** |

## How to use this

- **Before adding a dose anywhere, check this table.** If the drug already has an owner,
  cross-reference it with `→MED:` rather than restating the figure.
- **`RANGE NOT STATED` is the actionable finding**, not a formatting gap. It means the entry
  gives a figure without saying who it applies to — the B65 shape.
- **Regenerate rather than hand-edit:** this file is derived. Re-run the Step 28d scan.
