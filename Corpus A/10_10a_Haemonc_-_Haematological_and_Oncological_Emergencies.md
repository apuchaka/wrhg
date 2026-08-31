---
block: Haematology and Oncology
source: quackquackmed 10.10 Emergencies - Neutropenic sepsis, Tumour lysis syndrome, SVC obstruction
trust: inherited
population: mixed
conflicts_open: 0
conflicts_r1: 0
no_baseline: 0
---

> [!warning] **This file is named for oncological emergencies and covers three of them — neutropenic sepsis, tumour lysis syndrome, and SVC obstruction. Two more are owned elsewhere and were not pointed at from here at all** (added in the G9 round, 2026-08-29):
> - **Malignant spinal cord compression** — [[04_Neurology]] Malignant Spinal Cord Compression (MSCC), which owns it in full, including the UMN-pattern distinction from cauda equina syndrome. (A separate, broader entry on non-malignant cord compression from trauma, disc or infection sits in [[11_01_Ortho_-_Orthopaedic_Emergencies]] Spinal cord compression.)
> - **Hypercalcaemia of malignancy** — [[06_Metabolic_Medicine_and_Endocrinology]] Hypercalcaemia, which owns the CHIMPANZEES differential, the PTH-dependent/independent split that separates malignancy from hyperparathyroidism, and the fluid and zoledronic acid figures.
>
> Neither is repeated here: **one owner for the numbers, pointers from everywhere else.** The point of this note is that a reader revising "oncological emergencies" from the file of that name was getting three of five, with nothing indicating the other two existed.

## Neutropenic sepsis

- **D:** medical emergency — presence of fever in a neutropenic patient (aka febrile neutropaenia).
- **A:** infection, most often Gram-positive (*S. aureus*, *S. epidermidis*); also Gram-negative (*E. coli*, *Klebsiella*, *Pseudomonas aeruginosa*).
- **P:** chemotherapy-induced immunosuppression; mucosal breaches, lines, catheters, etc. as routes of entry.
- **S/Smx:** mainly fever, but any other symptoms/signs of sepsis.

> [!danger] ASK "when was your last chemotherapy?" — neutropenic sepsis is most likely to occur ~10 days post-chemotherapy, but can occur at any time within 6 weeks.

- **Ix:** FBC (neutrophils <0.5), blood cultures, lactate, LDH, etc.

> [!info] Verified against current Australian Therapeutic Guidelines: Antibiotic practice, Aug 2026 — **piperacillin-tazobactam is confirmed as genuine, current first-line Australian empirical therapy** for sepsis of unknown origin including neutropenic sepsis, not a UK-specific choice as originally flagged — this is a case where checking confirmed the note was already correct rather than needing replacement. The general escalation logic (add vancomycin for suspected line-related sepsis or septic shock; switch to meropenem if risk factors for multidrug-resistant Gram-negative organisms) also matches current Australian guidance. As with the [[08_09_Infectious_Disease_-_Miscellaneous]] Sepsis entry, Australian sepsis pathways use the "SEPSIS KILLS" branding rather than "Sepsis 6" — see that entry for the fuller AU-specific detail on the underlying clinical actions, not repeated here; the substance of "Sepsis 6" below (oxygen, cultures, fluids, antibiotics, lactate, urine output) remains clinically appropriate regardless of naming.

- **Mx:**
  - SEPSIS KILLS / Sepsis 6 principles — see [[08_09_Infectious_Disease_-_Miscellaneous]] Sepsis for the full AU-specific framework, not repeated here.
  - Antibiotics: piperacillin-tazobactam to cover — only 30% of cultures come back positive, so go broad spectrum.
  - If the patient is still febrile and unwell after 48h, add meropenem ± vancomycin (vancomycin specifically for suspected line-related sepsis or septic shock, per current AU guidance).
  - If not responding in 4–6 days, order investigations for fungal infection (e.g. HRCT).
  - ± G-CSF if appropriate.

### Added from unverified layer — what the neutropenic patient does not show you
`SRC:K1_Fever_Workup §0.5` `UNVERIFIED — model knowledge, not source-checked.`

> [!danger] **There may be no localising signs, because the signs require neutrophils**
> **Pus, erythema, consolidation on a chest radiograph and peritonism are all products of the neutrophilic inflammatory response — which this patient does not have.**
> **A neutropenic patient with pneumonia may have a normal chest radiograph.** One with a perianal abscess may have only pain. **The absence of findings is not reassurance; it is expected**, and it is why the empirical antibiotic above is given before the source is known.
> This is also why the escalation to CT above matters: it finds what plain radiography cannot.

> [!warning] **Examine carefully but gently, and there are two things not to do**
> Look at the **mouth, skin, perianal region, every line and exit site, and the chest.** The source is often visible and there is little else to find.
> **Avoid digital rectal examination and rectal thermometers in a neutropenic patient**, because of the risk of translocation and bacteraemia across a mucosal surface that cannot defend itself.

> [!tip] **Blood cultures: peripheral AND every lumen**
> **Take cultures from a peripheral vein and from each lumen of any central line, labelled by source.** Paired cultures allow **differential time to positivity** — a line culture flagging substantially earlier than the peripheral one points to the line as the source, which is what determines whether it has to come out.
> This is a different use of time-to-positivity from the one at [[Investigation-Interpretation]], where it helps separate true infection from contamination.

> [!info] **Risk stratification — the MASCC score** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> Not every febrile neutropenic patient needs the same pathway. **The MASCC score identifies a low-risk group who may be suitable for oral therapy and early discharge** rather than admission for intravenous antibiotics.
> **This is a decision made with haematology or oncology, not independently**, and it never delays the first dose — the patient is stratified after the antibiotic, not before it.
> `UNVERIFIED — the MASCC score's components, its low-risk threshold, and whether Australian practice uses it or a local equivalent, per eviQ and hospital protocol.`

## Tumour lysis syndrome

- **D:** oncological emergency caused by the rapid breakdown of cancer cells and the subsequent release of large amounts of intracellular content into the bloodstream.
- **R:** haematological cancer, large tumour burden, treatment-sensitive tumours, recent cancer treatment, pre-existing renal impairment, dehydration, volume depletion, nephrotoxic drugs.

> [!danger] Biochemical picture: ↑K, ↓Ca, ↑PO4, ↑urate, ↑LDH. LDH is a prognostic factor — indicates the rate/level of cell death.

- **S/Smx:** most often occurs in children and young adults; most often when chemotherapy starts (12–72h after). Nausea, vomiting, diarrhoea, anorexia, muscle weakness, muscle cramps, tetany, flank pain, lethargy, paraesthesia, and laryngeal spasm.
- **Ix:** U&Es, etc.
- **Mx:**
  - Fluid resuscitation.
  - Manage hyperkalaemia.
  - IV rasburicase for high-risk patients (breaks down uric acid).
  - Allopurinol for lower-risk patients.

## Superior vena cava obstruction (SVCO)

- **D:** oncological emergency caused by compression of the SVC.
- **A:** lung cancer (especially small cell lung cancer), non-Hodgkin's lymphoma, other cancers. Non-malignant causes: aortic aneurysm, mediastinal fibrosis, goitre, SVC thrombosis.
- **P:** compression of the SVC → ↓drainage of blood from the top of the body (head, neck, arms).
- **S/Smx:** dyspnoea; swelling of face, neck and arms; headache (worse in mornings); visual disturbances (possibly secondary to cerebral oedema); pulseless jugular venous distention.

> [!note] The mechanism by which SVC obstruction causes visual disturbances is not well explained in the literature.

> [!tip] Added from unverified layer — **Pemberton's sign**
> `SRC:B6_Oedema__Fatigue__Weakness_and_Undifferentiated_Presentations §0.4` `UNVERIFIED — model knowledge, not source-checked.`
> **Ask the patient to raise both arms above their head and hold them there.** In SVC
> obstruction this produces **facial plethora, cyanosis, distress and sometimes stridor**, by
> further narrowing an already compromised thoracic inlet.
> It is free, takes seconds, and is the bedside manoeuvre that converts the S/Smx list above
> from a set of symptoms into a demonstrable sign. `Pemberton` and `arms above the head` were
> both **0 vault-wide**. It is also positive in retrosternal goitre, which is worth knowing
> since that is the other mass lesion at the thoracic inlet.

- **Mx:** endovascular stenting to provide symptomatic relief; radical chemotherapy or chemo-radiotherapy in some cancers; ± glucocorticoids (weak evidence).
