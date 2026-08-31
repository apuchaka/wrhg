---
name: K1 destination table
description: Where every section of Corpus B-new/K1_Fever_Workup.md goes, including the sections that were discarded.
bfile: Corpus B-new/K1_Fever_Workup.md
built: 2026-08-31
---

# K1_Fever_Workup — destination table

Committed **before** any content was written. 267 lines, 6 sections.
**55 concepts tested · 39 present · 15 absent · 1 conflict.**
**Additive/discard ratio: 15 additive / 39 discard = 28% additive.**

## Acronym collisions reported up front

`inventory.py` over `08_09_Infectious_Disease_-_Miscellaneous`,
`10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies` and
`NEW_Infectious_Diseases` returned **72 candidates**. Read, per rule 3:

| Collision | Why it is not an instrument |
|---|---|
| `ASK` `KILLS` `LATE` `ONLY` `TIER` `RECOGNISE` `REFER` `RESUSCITATE` `CHIMPANZEES` `III` | all-caps prose and mnemonics — `SEPSIS KILLS` is the AU sepsis branding, `CHIMPANZEES` the hypercalcaemia differential |
| `CSV` | the project's own `checklist.csv`, cited in two gap-fill notes |
| `MAP` | mean arterial pressure at `08_09:207`, not the English word |
| `SBP` | **systolic blood pressure** at `08_09:193` — the same acronym is **spontaneous bacterial peritonitis** in `03_Gastrointestinal`. A real collision, and the one to watch on any future ascites/sepsis search |
| `EBM-Consent-Capacity` `NSW` `RACGP` `RCH` `SESLHD` `NNDSS` `ACI` `CDC` | filenames and organisations |
| `HLH` | **the trap of this file.** Three hits, all **hypoplastic left heart** in `15_05_Paeds`. Haemophagocytic lymphohistiocytosis is absent. Rule 9 exactly |

Genuine instruments present: **Duke criteria · Durack-Street criteria · Petersdorf ·
Eron classification · LRINEC · SIRS · SOFA · Katayama syndrome · Lemierre's syndrome ·
Pemberton's sign · HACEK**.

## Destination table

| K1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Fever mechanism — endogenous pyrogens, PGE2, hypothalamic set point | `Corpus A/08_09_Infectious_Disease_-_Miscellaneous.md` | **ADDITIVE** — the only `pyrogen` hit in the vault is malaria's synchronous-rupture cycle at `08_07:71`, a different mechanism |
| 0.1 | Fever vs hyperthermia — antipyretics do not work | — | **DISCARD** — `11_09b_Ortho_-_Trauma.md:250`: *"**Cool actively and early; antipyretics do not work**, because the thermostat is not reset — this is not fever."* Found only because rule 2's backstop was run on a search that looked clean |
| 0.1 | Blunted/absent febrile response; hypothermia as a poor prognostic sign | `Corpus A/08_09` | **ADDITIVE** — near-misses at `03_Gastrointestinal:1741` (surgical abdomen in the old), `NEW_Investigations_General:33` (normal CRP), `NEW_Drugs_19:50` (fever on a biologic). None carries the list or the hypothermia claim |
| 0.1 | Fever patterns over-taught; Pel-Ebstein; relative bradycardia | `Corpus A/08_09` | **ADDITIVE** — tertian/quartan are at `08_07:71`; **`Pel-Ebstein` is 0 hits, and all 5 `Ebstein` hits are Ebstein's anomaly** |
| 0.1 | Not all fever is infection — malignancy, inflammatory, VTE, drug, endocrine | — | **DISCARD** — `08_09:124–127` carries the same four categories under FUO |
| 0.2 | Systematic head-to-toe source search | — | **DISCARD** — `History-Taking.md:519–520` owns the exposure and travel screen; `08_09:136` owns "confirm true fever" |
| 0.2 | Do not reflexively start antibiotics without a source | — | **DISCARD** — `08_09` Mx: *"stable patients do not automatically need empirical antibiotics"*, with the culture-sterilisation reasoning |
| 0.2 | Asymptomatic bacteriuria does not prove the source | — | **DISCARD** — `Investigation-Interpretation:358` and `NEW_Investigations_Renal_and_Urology:33` |
| 0.2 | Very high ESR with modest CRP | — | **DISCARD** — `Investigation-Interpretation:518–520` carries a fuller CRP/ESR discordance block (SLE, myeloma rouleaux, pregnancy, anaemia) |
| 0.2 | Discitis and epidural abscess on spine percussion | — | **DISCARD** — `11_06_Ortho_-_Spinal_Orthopaedics.md:111` owns Discitis; `08_09:216` and `11_01:170` own epidural abscess |
| 0.3 | FUO definition, Durack-Street categories, four cause groups, approach | — | **DISCARD** — `08_09:116–142`, ACI-verified, and more complete than K1 |
| 0.3 | Repeat the history and examination; stop non-essential drugs | — | **DISCARD** — `08_09:137` step 2 |
| 0.3 | **PET-CT in FUO** | `Corpus A/08_09` | **ADDITIVE** — 6 `PET-CT` hits, all oncological staging (oesophageal, colorectal, myeloma, renal). None is FUO |
| 0.3 | Adult-onset Still — quotidian fever, very high ferritin | `Corpus A/08_09` | **ADDITIVE** — the entity is named at `08_09:126`; **`quotidian` is 0 hits**, and the one `salmon-pink` hit is **systemic-onset JIA** at `11_10_Ortho:18`, the paediatric disease |
| 0.3 | Haemophagocytic lymphohistiocytosis | `Corpus A/08_09` | **ADDITIVE** — `lymphohistiocytos` 0 hits; `HLH` 3 hits, all hypoplastic left heart |
| 0.3 | Fastidious organisms, HACEK, culture-negative endocarditis | — | **DISCARD** — `01_Cardiovascular:1374–1376` names HACEK in full and the fastidious-organism category |
| 0.3 | Familial Mediterranean fever | — | **DISCARD** — `03_Gastrointestinal:1654` |
| 0.4 | Malaria until proven otherwise; prophylaxis does not exclude | — | **DISCARD** — `08_09:148` and `08_09:164`, stated more strongly |
| 0.4 | Incubation-period bands, short/medium/long | — | **DISCARD** — `08_09:153–159`, the same three bands with the same organisms |
| 0.4 | Primaquine radical cure; G6PD first | — | **DISCARD** — `08_07:75` *"**Check G6PD status before giving primaquine**"*, and `NEW_Drugs_05:280` states it as a hard requirement plus tafenoquine |
| 0.4 | Dengue warning signs | — | **DISCARD** — `08_05-06:25` carries abdominal pain, hepatomegaly, persistent vomiting and fluid accumulation |
| 0.4 | Typhoid, leptospirosis, Katayama, amoebic abscess, chikungunya, HIV seroconversion | — | **DISCARD** — each has its own entry; `suffusion` resolves to `08_01-03:205` |
| 0.4 | **Rickettsial eschar at the bite site** | `Corpus A/08_09` | **ADDITIVE** — **4 `eschar` hits: anthrax ×2, burns escharotomy, acid coagulative necrosis. Not one is the rickettsial bite-site eschar.** Rule 9 |
| 0.4 | **Melioidosis as an entity** | `Corpus A/08_09` | **ADDITIVE** — 1 hit, `NEW_Drugs_05:146`, inside a doxycycline indication list. No entity, no northern-Australia/wet-season epidemiology, no risk groups |
| 0.4 | **Murray Valley and Japanese encephalitis as clinical entities** | `Corpus A/08_09` | **ADDITIVE** — both appear **only as names inside the NNDSS notifiable list** at `08_01-03:335`. Named in a sentence, so the topic reads as covered |
| 0.4 | **Zika** | `Corpus A/08_09` | **ADDITIVE** — 0 hits vault-wide |
| 0.4 | Ross River and Barmah Forest | — | **DISCARD** — `NEW_Rheumatology_and_Immunology:25` and `:33`, as alphavirus arthritis with serology |
| 0.4 | Q fever, abattoir exposure | — | **DISCARD** — `08_01-03:198` |
| 0.5 | Febrile neutropenia is an emergency; empirical broad-spectrum | — | **DISCARD** — `10_10a` Neutropenic sepsis, **verified against Therapeutic Guidelines Aug 2026** with pip-taz. B cannot win against a verified box (§1.10) |
| 0.5 | Escalation, antifungals for persistent fever | — | **DISCARD** — `10_10a`: *"If not responding in 4–6 days, order investigations for fungal infection"*; `02_Respiratory:417` owns the halo sign; `NEW_Infectious_Diseases:49` owns galactomannan and beta-D-glucan |
| 0.5 | **No localising signs, because the signs require neutrophils** | `Corpus A/10_10a` | **ADDITIVE** — `10_10a` S/Smx is *"mainly fever, but any other symptoms/signs of sepsis"*, which is the opposite emphasis |
| 0.5 | **Avoid digital rectal examination and rectal thermometers** | `Corpus A/10_10a` | **ADDITIVE** — `thermometer` 0 hits in either destination; 8 `translocation` hits, none about neutropenia |
| 0.5 | **MASCC score and the low-risk group** | `Corpus A/10_10a` | **ADDITIVE** — 0 hits, and reading the whole `10_10a` section confirms there is no risk stratification in it at all. Threshold stays `UNVERIFIED` |
| 0.5 | **Paired peripheral and line cultures; differential time to positivity** | `Corpus A/10_10a` | **ADDITIVE** — `Investigation-Interpretation:455` has time-to-positivity **as a contamination discriminator**, not as line-source identification. Correct-looking hit, different clinical question |
| 0.5 | **Post-transplant infection timeline** | `Corpus A/08_09` | **ADDITIVE** — `07_Renal:146–162` owns transplant immunosuppression and complications, but not the month-by-month infection timeline |
| 0.5 | Eculizumab → meningococcal; rituximab → hepatitis B; TNF inhibitors → latent TB | — | **DISCARD** — `NEW_Drugs_07:122`, `NEW_Drugs_20:32` (vaccinate before starting), `NEW_Investigations_Gastroenterology:157` |
| 0.5 | HIV differential stratified by CD4 | — | **DISCARD** — `04_Neurology` CNS Infections Associated with Immunosuppression, pointed at from `08_09:127` |
| 0.5 | Asplenia, OPSI, immediate antibiotics | — | **DISCARD** — `08_09:108` Post-splenectomy sepsis |
| 0.5 | Immune reconstitution inflammatory syndrome | — | **DISCARD** — `04_Neurology:711` names IRIS and the ART-timing problem |
| 0.5 | Neutropenia from clozapine, carbimazole, methotrexate, co-trimoxazole | — | **DISCARD** — `10_07_Haemonc` owns neutropaenia; 16 `carbimazole` hits |
| 0.6 | Post-operative timeline and the five Ws | — | **DISCARD** — `03a_Anaesthetics_Primer:348` carries the mnemonic with the same day bands |
| 0.6 | **Atelectasis as a cause of post-operative fever** | `Corpus A/03a_Anaesthetics_Primer.md` | **CONFLICT `CF-035` R2** — A says *"Wind (atelectasis/pneumonia — most common cause in the first 24–48h)"*; B says the teaching is poorly supported and delays finding the real source |
| 0.6 | Anastomotic leak; the patient who is not progressing | — | **DISCARD** — `03a_Anaesthetics_Primer:354` already holds this as an earlier additive block |
| 0.6 | **Drug fever — culprits, "looks better than the temperature", diagnosis by cessation** | `Corpus A/08_09` | **ADDITIVE** — named as an FUO cause at `08_09:127` with no features; `defervescence` 0 hits |
| 0.6 | Gout and pseudogout mimicking sepsis; VTE; withdrawal; thyroid storm | — | **DISCARD** — 27 `pseudogout` hits; `NEW_Investigations_Rheumatology:169` states crystals do not exclude infection |

## NO-BASELINE — tested against base-A (`0db4034`), not against the destination

Five subjects return **zero hits across all 246 base-A files**, so no inherited layer
disagrees with them: **MASCC · haemophagocytic lymphohistiocytosis · Zika ·
Pel-Ebstein · quotidian fever**.

`thermometer` (2), `melioidosis` (3), `eschar` (11), `Murray Valley encephalitis` (1) and
`PET-CT` (7) all have base-A hits and are **not** marked — the hits are the wrong sense in
each case, which makes them gaps but not absences.

## New files

**None.** Every destination is an existing section in an existing file.
