---
block: Infectious Disease
source: quackquackmed 08.09 Miscellaneous infections
trust: inherited
population: mixed
conflicts_open: 1
conflicts_r1: 0
no_baseline: 9
---

## Animal & human bites

- **A/P:**
  - Animal bites — *Pasteurella multocida*.
  - Human bites — aerobic and anaerobic bacteria: Strep, Staph, *Eikenella*, *Fusobacterium*, *Prevotella*. Consider risk of HIV, hepatitis C.
- **Mx:** clean wound, do not suture closed unless thorough washout performed. Antibiotics: amoxicillin+clavulanate, or doxycycline + metronidazole. `UNVERIFIED — AU regimen; Therapeutic Guidelines (login). Look up at point of use.`

### Added from unverified layer — two bite exposures the organism list does not carry
`SRC:K2_Skin_and_Soft_Tissue_Infection §0.5` `UNVERIFIED — model knowledge, not source-checked.`

> [!danger] ***Capnocytophaga canimorsus* — a dog bite that kills the asplenic patient** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> An oral commensal of dogs and cats that causes **fulminant sepsis with purpura fulminans, disseminated intravascular coagulation and multi-organ failure** — overwhelmingly in people who are **asplenic or hyposplenic, have chronic liver disease or harmful alcohol use, or are immunosuppressed.**
> **The bite itself can look trivial**, and the patient presents days later profoundly unwell out of proportion to the wound.
> This is the organism behind the standing instruction at Post-splenectomy sepsis below: an asplenic patient with **any** animal bite needs antibiotics, not observation. `UNVERIFIED — the agent and duration for bite prophylaxis in asplenia, per Therapeutic Guidelines: Antibiotic.`

> [!danger] **Australian bat lyssavirus — ANY bat contact, anywhere in Australia**
> Named in this corpus only inside the NNDSS quarantinable category at [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Notifiable Diseases (Australia), as *"rabies/lyssaviruses"*. As a clinical action:
> **Any bite, scratch or mucous-membrane exposure from any Australian bat — flying fox or microbat — is treated as a potential lyssavirus exposure.** The virus is present in bats across the country, the illness it causes is **effectively always fatal once symptomatic**, and post-exposure prophylaxis is **completely effective if given.**
> **Wash the wound immediately and thoroughly, then contact public health the same day** for rabies vaccine and immunoglobulin assessment. **Do not handle bats** — refer the public to trained wildlife handlers.
> `UNVERIFIED — the post-exposure prophylaxis schedule, immunoglobulin indication and wound-washing duration, per the Australian Immunisation Handbook and the CDNA national guidelines for Australian bat lyssavirus.`

> [!info] Verified against Australian bite-wound literature (RCH Clinical Practice Guidelines; ED and tropical Australia bite-management studies), Aug 2026 — amoxicillin-clavulanate is confirmed as the current Australian first-line choice, consistent with the "amoxicillin+clavulanate" already in the note (this is the UK name for the same amoxicillin+clavulanic acid combination — not actually a different drug). **Oral dosing: amoxicillin-clavulanate 875/125mg 12-hourly** is specifically cited as most appropriate for high-risk wounds. For penicillin allergy, Australian sources specify **ciprofloxacin 500mg 12-hourly plus clindamycin 450mg 8-hourly** — a different combination from the doxycycline+metronidazole option in the note (which isn't wrong pharmacologically, but isn't the specific Australian-cited alternative either) — worth knowing both exist as reasonable options but the ciprofloxacin+clindamycin combination is the one specifically documented in Australian clinical practice guidelines. For established moderate-severe infection requiring admission, IV piperacillin-tazobactam is the cited regimen. Minor genuine correction beyond dose specifics: routine antibiotics are **not required prophylactically for all bites** in adults — thorough washout/debridement remains the most important intervention, with prophylactic antibiotics reserved for higher-risk wounds (immunocompromise, diabetes, crush injury, wounds needing surgical repair, hand/joint involvement) rather than given to every bite universally. `UNVERIFIED — AU regimen; Therapeutic Guidelines (login). Look up at point of use.`

## Cellulitis

- **D:** infection of the dermis and deeper subcutaneous tissues. Erysipelas is a related, more superficial variant, involving only the upper dermis and superficial lymphatics — the purulent/non-purulent Mx distinction below broadly maps onto this deep/superficial and staphylococcal/streptococcal distinction respectively.
- **A:** *Strep pyogenes*, *S. aureus*.
- **R:** diabetes, venous insufficiency, eczema, oedema & lymphoedema, obesity, previous episodes of cellulitis, toe-web abnormalities (a disrupted skin barrier providing bacterial entry).

> [!danger] Added from unverified layer — **bilateral simultaneous cellulitis is rare**
> `SRC:B6_Oedema__Fatigue__Weakness_and_Undifferentiated_Presentations §0.2` `UNVERIFIED — model knowledge, not source-checked.`
> **Bilateral** red, warm, swollen lower legs are far more often **venous stasis dermatitis or
> lipodermatosclerosis** than infection. Both are **inflammatory and not infective**, both
> look convincingly like cellulitis, and **neither responds to antibiotics.**
> The risk factors above — venous insufficiency, oedema and lymphoedema — are precisely the
> patients in whom this confusion arises, and it is a common reason for repeated
> unnecessary courses. **Ask whether it is truly one leg**: cellulitis is nearly always
> unilateral, and simultaneous bilateral disease should prompt a rethink rather than a
> broader antibiotic.
> `lipodermatosclerosis` is already described at [[01_Cardiovascular]] §0.36.7 and
> [[Examination]] (*"firm, woody induration"*) — this line is the link from the infective
> differential to it.
- **S/Smx:** erythema, pain, swelling, commonly on the shins; possibly associated with systemic upset.
- **Ix:** clinical diagnosis ± bloods and blood cultures if sepsis is suspected.

### Added from unverified layer — two things to do at the bedside, and one more mimic
`SRC:K2_Skin_and_Soft_Tissue_Infection §0.1` `UNVERIFIED — model knowledge, not source-checked.`

> [!tip] **Mark the border and write the time on the skin**
> Draw around the edge of the erythema and **write the date and time beside it**. It converts an argument about whether the leg looks better into an observation, it survives handover and a change of shift, and it is the single most useful thing to do at the first review.
> **Spread beyond the mark is the objective sign of failure**, and the prompt to reconsider the diagnosis as much as the antibiotic.

> [!warning] **Calciphylaxis — the mimic to know in a dialysis patient** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> In patients with **end-stage kidney disease, particularly on dialysis**, calcific uraemic arteriolopathy produces **exquisitely painful** necrotic plaques and ulcers with surrounding violaceous, retiform erythema — most often on the thighs, abdomen and other fatty areas.
> **The pain is out of proportion and the lesions do not respond to antibiotics.** It carries a high mortality and needs renal and dermatology involvement, not a longer antibiotic course.
> Chronic kidney disease–mineral bone disorder, which is the setting it arises from, is owned by [[07_Renal_Medicine_and_Urology]] 0.2.2 Mineral Bone Disease (in CKD).

> [!info] Eron classification of cellulitis
> - **Class I:** no signs of systemic toxicity, no uncontrolled comorbidities.
> - **Class II:** systemically unwell, or has a comorbidity that may complicate/delay resolution (e.g. peripheral arterial disease).
> - **Class III:** severe systemic upset, or an unstable comorbidity that may interfere with response to treatment, or life-threatening infection due to vascular compromise.
> - **Class IV:** sepsis, or a severe life-threatening infection (e.g. necrotising fasciitis).

> [!info] Verified against Queensland Health clinical pathways and the 2025 eTG antibiotic guideline updates, Aug 2026 — flucloxacillin is confirmed as correct for Australian first-line cellulitis Mx, but current Australian practice draws a distinction not in the note below: **the specific first-line drug depends on whether the cellulitis is purulent (associated with an abscess, boil, or wound) or non-purulent (erysipelas-type, no associated wound)** — reflecting the different likely causative organism (*S. aureus* for the former, *Strep pyogenes* for the latter).
> - **Purulent (abscess/wound/furuncle-associated):** dicloxacillin or flucloxacillin 500mg PO 6-hourly for 5 days.
> - **Non-purulent (erysipelas, no associated wound):** phenoxymethylpenicillin 500mg PO 6-hourly for 5 days — genuinely narrower-spectrum than flucloxacillin, appropriate given *Strep pyogenes* remains penicillin-susceptible.
> - For penicillin hypersensitivity or known MRSA colonisation, alternative agents are used per local guidance (not detailed here).
> Amoxicillin+clavulanate is specifically reserved in current (2025) eTG guidance for more serious infections where *Enterobacterales* or *H. influenzae* involvement is suspected, rather than as a routine cellulitis first-line choice — worth knowing this is a more targeted indication than the broader "amoxicillin+clavulanate" framing below suggests. Cefazolin is a recognised IV alternative to flucloxacillin for confirmed MSSA. The general Eron-classification-based escalation logic (community oral therapy for Class I/II, IV/admission for Class III/IV) remains consistent with current Australian practice, and 2025 eTG updates specifically simplified/reduced the threshold for routine IV therapy in mild disease while increasing it for shock/ICU-level illness — a genuine recent shift toward oral-first management where appropriate. `UNVERIFIED — AU regimen; Therapeutic Guidelines (login). Look up at point of use.`

- **Mx of Eron Class I & II:** PO flucloxacillin (purulent) or phenoxymethylpenicillin (non-purulent) per the AU-specific distinction above, or clarithromycin/erythromycin (in pregnancy) or doxycycline for penicillin allergy. Class II may need IV treatment, but try to treat in the community.
- **Mx of Eron Class III/IV:** admit if rapidly deteriorating, <1 year old, immunocompromised, significant lymphoedema, or facial/periorbital involvement. Treatment: IV flucloxacillin or cefazolin first-line, escalating to IV amoxicillin+clavulanate, clindamycin, cefuroxime, or ceftriaxone for more serious/broader-spectrum indications per the notes above. `UNVERIFIED — AU regimen; Therapeutic Guidelines (login). Look up at point of use.`

## Mastitis and Breast Abscess

> [!note] Gap-filled from CSV ("Mastitis and breast abscess," High yield) — genuinely absent anywhere in this project despite being a common presentation. Verified against RACGP's "Lactational mastitis and breast abscess" clinical guidance and WA Health/SESLHD lactational mastitis protocols, Aug 2026.

- **D:** an inflammatory condition of the breast, most commonly in the lactational/postpartum context — encompassing a spectrum from simple milk stasis/engorgement (inflammation without infection) through to established infective mastitis and, if untreated or inadequately treated, breast abscess. **Lactational mastitis affects roughly 1 in 5 breastfeeding women** and is a frequent, genuinely important reason women stop breastfeeding — a point worth conveying to patients given continuing to breastfeed through mastitis is both safe and part of effective management, not something that needs to stop.
- **A/P:** most often begins as non-infective milk stasis (a blocked duct, incomplete drainage) causing localised inflammation; this can progress to infective mastitis if bacteria (typically *S. aureus*) enter via a cracked or damaged nipple — the inflammatory and infective processes exist on a spectrum rather than being two entirely separate conditions, which is why management addresses both drainage and (where infection is present) antibiotics.
- **R:** cracked/damaged nipples, poor attachment/positioning during feeding, engorgement, infrequent or incomplete feeding/expressing, rapid weaning, external pressure on the breast (tight bra, sleeping position), previous mastitis.
- **S/Smx:** localised breast pain, redness, and swelling (classically wedge/segmental-shaped, following the distribution of the affected duct system), a palpable tender lump or hardened area, ± fever and systemic symptoms (myalgia, malaise — can mimic influenza, and systemic symptoms don't necessarily mean infection is present, given severe milk stasis alone can also cause them). **Breast abscess** should be suspected when a discrete, fluctuant, persistently tender mass develops, or when symptoms fail to improve despite appropriate mastitis management — genuinely important to actively consider rather than simply escalating the same treatment, since an abscess needs drainage, not just more antibiotics.
- **Ix:** primarily a clinical diagnosis; routine bloods, cultures, and imaging are **not** required for straightforward mastitis (Australian GP practice data confirms these are rarely performed, and correctly so) — reserve breast ultrasound for suspected abscess (to confirm and guide drainage) or where the diagnosis is unclear; breast milk or nipple swab culture is occasionally useful in recurrent, severe, or treatment-resistant cases, or where MRSA is a concern.

> [!danger] Always keep the differential for inflammatory breast cancer in mind, particularly if symptoms fail to resolve as expected with appropriate treatment — a red, swollen breast that doesn't respond to standard mastitis management (rather than the acute lactational presentation described above) warrants further assessment rather than being assumed to be treatment-resistant mastitis by default.

- **Mx:**
  - **Immediate/acute:** **continue breastfeeding/effective milk removal** from the affected breast — this is a core, active part of treatment, not something to pause; feed on the affected side first, or hand-express/pump if feeding is too painful, given effective drainage is central to resolving the underlying stasis. Regular analgesia (paracetamol first-line ± NSAIDs, both safe in lactation) — genuinely important given untreated pain itself can inhibit the let-down reflex and worsen stasis. **Cold packs** between/after feeds for pain and inflammation; avoid heat, which can worsen inflammation despite feeling temporarily soothing (a genuinely counterintuitive point worth stating explicitly, since heat is a common but incorrect home remedy).
  - **Antibiotics — for confirmed or suspected infective mastitis (not required for simple milk stasis without infective features):** flucloxacillin or dicloxacillin (di/flucloxacillin is the most common Australian first-line choice in real-world GP practice), or cefalexin as a common alternative; clindamycin for penicillin allergy. Both first-line agents are safe in breastfeeding. Symptoms should meaningfully improve within 24–48 hours of appropriate treatment — if not, or if the patient is more significantly unwell, escalate assessment (consider ultrasound to exclude abscess, and reconsider the diagnosis, including inflammatory breast cancer per the danger box above).
  - **Breast abscess:** ultrasound-guided needle aspiration is now generally preferred over surgical incision and drainage where feasible, given comparable efficacy with less scarring/cosmetic impact and less disruption to breastfeeding — surgical drainage remains an option for larger or more complex abscesses, or where aspiration fails. Breastfeeding can generally continue on the affected side once an abscess is being appropriately managed, though this should be individualised with the treating clinician, particularly if drainage affects the ability to feed directly from that breast.
  - **Chronic/long-term:** address contributing factors (attachment/positioning review, feeding frequency) to prevent recurrence; lactation consultant input is genuinely valuable given how much of the underlying problem (poor drainage, positioning) is addressed through practical feeding support rather than medication alone.

### Added from unverified layer — non-lactational and periductal mastitis
`SRC:O7_Breast_Disease §0.6` `UNVERIFIED — model knowledge, not source-checked.` `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`

> [!warning] **Mastitis in a woman who is not breastfeeding is a different disease**
> The entry above is lactational mastitis. **Non-lactational mastitis has different organisms, a different natural history, and a strong and under-asked risk factor.**
> **· PERIDUCTAL MASTITIS is strongly associated with SMOKING** — the association is strong enough that smoking cessation is part of the treatment rather than general advice, and the condition recurs while smoking continues. Typically **younger women, periareolar**, and often **anaerobes and mixed flora rather than the *S. aureus* of lactational disease**, so the antibiotic choice differs. `UNVERIFIED — the antibiotic regimen for non-lactational and periductal mastitis, per Therapeutic Guidelines: Antibiotic.`
> **· It recurs, and it fistulates.** A **mammary duct fistula** — a chronic discharging periareolar sinus — is the characteristic complication, and it needs surgical rather than repeated antibiotic management.
> **· Duct ectasia** (already listed in the breast lump differential at [[NEW_Breast]]) is the related non-infective process, with thick discharge and nipple retraction in older women.

> [!danger] **AND THE RULE THAT OUTRANKS ALL OF THIS: "mastitis" that does not resolve is cancer until proven otherwise**
> **Inflammatory breast cancer presents with erythema, warmth and peau d'orange and is routinely treated as mastitis first.** [[NEW_Breast]] names it as *"the classic trap"*.
> **Any mastitis — lactational or not — that fails to settle on appropriate antibiotics needs re-examination and imaging, not a second antibiotic course.** In a non-lactating woman the threshold is lower still, because the prior probability has shifted.

## Lemierre's syndrome

- **D:** infectious thrombophlebitis of the internal jugular vein, secondary to bacterial sore throat caused by *Fusobacterium necrophorum* → peritonsillar abscess.
- **S/Smx:** neck pain, stiffness, tenderness; systemic fever and rigors; ± septic pulmonary emboli.
- **Ix:** contrast CT or Doppler ultrasound of the neck (*why:* confirms the internal jugular vein thrombosis directly, the key diagnostic finding distinguishing this from simple pharyngitis/peritonsillar abscess; *what:* thrombus within the internal jugular vein, ± the primary oropharyngeal source). Blood cultures (*why:* *F. necrophorum* bacteraemia is characteristic and confirms the diagnosis microbiologically, particularly relevant given the septic emboli risk below; *what:* often positive for *F. necrophorum*, an anaerobic Gram-negative organism). CT chest (*why:* screens for septic pulmonary emboli, a well-recognised and potentially serious complication given haematogenous spread from the infected thrombus; *what:* may show multiple peripheral nodules/cavitating lesions if emboli present).
- **Mx:**
  - **Immediate/acute:** IV antibiotics with anaerobic cover (e.g. a beta-lactam/beta-lactamase inhibitor or metronidazole-containing regimen) — genuinely urgent given the risk of ongoing septic embolisation if untreated.
  - **Definitive:** prolonged antibiotic course (often several weeks, given the difficulty of sterilising an infected thrombus); anticoagulation is used selectively (not routinely) depending on thrombus extent/progression and specialist input, rather than as an automatic component of Mx.
  - **Chronic/long-term:** source control (e.g. drainage of any peritonsillar abscess) if not already resolved; monitor for and manage any embolic complications.

## Necrotising fasciitis

> [!info] Classification
> - **Type 1:** mixed anaerobes and aerobes — often occurs post-operatively in diabetics.
> - **Type 2:** *Strep pyogenes* or MRSA (monomicrobial).
> - **Type 3:** monomicrobial, fresh-water infection (rare) — e.g. *Vibrio* species from marine/fresh-water wound exposure.
> - **Type 4:** monomicrobial fungal (mucormycosis) — rare, typically in severely immunocompromised patients.

- **R:** recent trauma, diabetes (especially if treated with SGLT-2 inhibitors), IVDU, immunosuppression, VZV infection, surgery, non-traumatic skin lesions.
- **A/P:** infection is introduced into and spreads along the fascial plane (does not typically spread into the muscle layer itself, distinguishing it from myonecrosis/gas gangrene).
- **S/Smx:** most commonly affects the perineum (= Fournier's gangrene) or limbs. Acute onset of pain, swelling, erythema, resembling rapidly worsening cellulitis — pain out of keeping with physical exam findings, or numbness, is a key red flag — do not be reassured by unremarkable-looking skin. Systemic signs from bacterial toxins (fever, tachycardia, hypotension) may be absent or late. May develop over a few days (acute) or a few hours (fulminant).

> [!danger] Skin necrosis and crepitus are LATE signs. Fever and tachycardia may be absent or late — do not rely on their absence to exclude necrotising fasciitis.

- **Ix:** this is a **clinical diagnosis, and imaging/labs should never delay surgical referral** if clinical suspicion is high, given how rapidly this progresses and how directly outcome depends on time to debridement (the same "don't wait for confirmation" principle seen elsewhere in this file, e.g. spinal epidural abscess below and elsewhere in this project, e.g. testicular torsion). The **"finger test"** can be performed at the bedside under local anaesthetic if there's genuine diagnostic uncertainty — make a 2cm incision down to deep fascia: a positive test (minimal resistance to finger dissection, absence of bleeding, presence of necrotic tissue, murky or greyish "dishwasher" fluid) supports the diagnosis, though this should not delay urgent surgical referral if suspicion is already high on clinical grounds alone. Bloods — FBC, CRP, U&Es, CK, lactate, LFTs, clotting screen, ABG (*why:* screens for the systemic inflammatory/septic response and specifically for CK elevation, which reflects muscle/fascial involvement and can support the diagnosis; *what:* often shows a markedly elevated CRP and CK disproportionate to the visible skin findings — the LRINEC score (Laboratory Risk Indicator for Necrotising Fasciitis, incorporating CRP, WCC, Hb, sodium, creatinine, glucose) can support risk stratification but should never be used to rule out the diagnosis in a clinically convincing presentation, given its imperfect sensitivity). Blood and tissue cultures, Gram stain (*why:* identifies the causative organism(s), guiding antibiotic rationalisation once source control is achieved; *what:* may be polymicrobial (Type 1) or monomicrobial (Types 2–4) per the classification above). CT or MRI (*why:* can show fascial thickening/gas/fluid tracking along fascial planes supporting the diagnosis when it's not yet clinically obvious, but again should not delay surgical exploration if clinical suspicion is high — surgical exploration is itself both diagnostic and therapeutic; *what:* fascial oedema, gas in soft tissue, or fluid collections along fascial planes).

- **Mx:**
  - **Immediate/acute:** urgent surgical debridement — the single most important intervention and the priority over any investigation, given source control is what actually halts the rapidly progressive tissue destruction; broad-spectrum IV antibiotics covering the likely organisms per the Type 1–4 classification above (typically a broad-spectrum beta-lactam/beta-lactamase inhibitor or carbapenem plus clindamycin — clindamycin specifically added for its toxin-suppressing effect on toxin-producing organisms like *Strep pyogenes*, distinct from its antibacterial action); aggressive fluid resuscitation given the septic physiology; ICU-level supportive care given the shock/organ dysfunction risk.
  - **Definitive:** repeated surgical debridement is often needed (a single operation frequently isn't sufficient, given how the disease can continue to progress along fascial planes even after initial debridement) — patients typically return to theatre for reassessment/further debridement within 24–48h; de-escalate antibiotics once culture/sensitivity results are available.
  - **Chronic/long-term:** reconstructive surgery (skin grafting, flap reconstruction) once the infection is controlled, given the often extensive tissue loss from debridement; rehabilitation given the functional impact of extensive soft tissue/muscle loss.

> [!warning] Added from unverified layer — ***Vibrio vulnificus*, and the host who gets it**
> `SRC:K2_Skin_and_Soft_Tissue_Infection §0.2` `UNVERIFIED — model knowledge, not source-checked.` `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> Type 3 above names *Vibrio* from marine or fresh-water exposure. **What makes it predictable is the host, not the water:** *V. vulnificus* causes fulminant necrotising infection and septicaemia **chiefly in people with chronic liver disease, haemochromatosis or iron overload, and the immunocompromised** — iron availability is thought to be why.
> **Exposure is seawater or estuarine water contacting a wound, or ingestion of raw shellfish** (from which it can cause primary septicaemia with haemorrhagic bullae and no wound at all).
> **A febrile patient with cirrhosis, haemorrhagic bullae and a seawater or oyster history is this diagnosis until proven otherwise**, and mortality is high and hours matter.

- **P:** average mortality 20%, worse (50–70%) if end organ damage or shock present — reinforcing why time to surgical debridement is the single most important prognostic factor.

## Added from unverified layer — terminal complement deficiency
`SRC:K3_Exposure__Tuberculosis__HIV_and_Immunodeficiency §0.5` `UNVERIFIED — model knowledge, not source-checked.` `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`

> [!danger] **A second episode of meningococcal disease is a diagnosis in itself**
> **Deficiency of the terminal complement components (C5–C9) and of properdin causes recurrent NEISSERIAL infection** — meningococcal disease above all, and disseminated gonococcal infection. The episodes are often **less severe than a first episode in a complement-sufficient person**, which is part of why the pattern is missed.
> **So: recurrent, unusually late-onset, or unusual-serogroup meningococcal disease should prompt a complement screen and immunology referral**, alongside the vaccination and prophylaxis that follow from it.
> `UNVERIFIED — the screening test (CH50/AH50 and terminal pathway assays), and Australian meningococcal vaccination recommendations for complement deficiency, per the Australian Immunisation Handbook.`
> **The acquired form is already in this vault and the inherited form was not:** [[NEW_Drugs_07_Blood_and_Electrolytes]] and [[NEW_Drugs_20_Vaccines]] record that **eculizumab and ravulizumab block C5 and mandate meningococcal vaccination before starting** — the same defect, produced deliberately by a drug.

## Post-splenectomy sepsis

> [!info] Verified against the Australian Immunisation Handbook and eTG-cited Australian guidance (Medicine Today), Aug 2026 — found genuine dose/frequency corrections and some updated vaccine coverage, not just a "check locally" caveat.
> **Vaccinations:** pneumococcal (conjugate, then polysaccharide 6–8 weeks later), Hib, **meningococcal ACWY (quadrivalent — not just type C** as in the original note) and **meningococcal B**, annual influenza — administer **2 weeks before** planned/elective splenectomy, or **2 weeks after** emergency splenectomy (vaccines given earlier than 2 weeks post-op, particularly pneumococcal, produce a weaker antibody response — though if there's a real risk the patient won't return for follow-up, vaccinating before discharge is preferred over losing the patient to follow-up entirely).
> **Antibiotic prophylaxis:** **amoxicillin 250mg PO once daily, OR phenoxymethylpenicillin (penicillin V) 250mg PO BD** — genuinely different from the original note's figures (penicillin V 500mg BD is double the correct dose; amoxicillin's frequency was also unspecified/implied differently). For confirmed penicillin allergy: roxithromycin 300mg daily or erythromycin (per local guidance).
> **Duration:** prophylaxis for a **minimum of 3 years post-splenectomy** in adults (some sources/individualised plans support lifelong prophylaxis, particularly for higher-risk patients — this is a case-by-case decision rather than a fixed endpoint for everyone); in children, prophylaxis continues until **at least 5 years of age** regardless of when splenectomy occurred, given the disproportionate infection risk in young children with asplenia.
> **Patient safety-netting:** patients should have a written action/emergency plan and keep emergency antibiotics at home and work, with instructions to take them immediately and seek urgent medical review if they develop fever, sweats, chills, or fatigue — reflecting the genuinely rapid, high-mortality course post-splenectomy sepsis can take. Infection risk is highest in the first 2 years post-splenectomy (~30% of infections occur in year 1, ~50% within 2 years) but persists lifelong, which is the rationale for the extended/individualised prophylaxis duration above.

### Added from unverified layer — fever: what produces it, and when its absence misleads
`SRC:K1_Fever_Workup §0.1, §0.5, §0.6` `UNVERIFIED — model knowledge, not source-checked.`

> [!info] **What actually raises the temperature**
> Exogenous pyrogens and tissue injury drive release of **endogenous pyrogens — interleukin-1, interleukin-6, tumour necrosis factor and the interferons** — which act on the hypothalamus via **prostaglandin E2** to **raise the thermoregulatory set point**. The body then *defends* the new higher temperature by vasoconstricting, shivering and seeking warmth.
> **This is why a patient developing a fever feels cold and shivers** — they are below their new set point — and why they feel hot and sweat as the fever breaks and the set point falls.
> The contrast with hyperthermia, where the set point is normal and **antipyretics do not work**, is owned by [[11_09b_Ortho_-_Trauma]] Heat illness and by [[03a_Anaesthetics_Primer]] — not repeated here.

> [!danger] **Absence of fever does not exclude infection**
> **Blunted or absent febrile responses occur in: the elderly · neonates · the immunosuppressed and those on corticosteroids · uraemic and dialysis patients · those taking regular paracetamol or NSAIDs · and in overwhelming sepsis.**
> **Hypothermia in a patient with infection is a marker of severity and a poor prognostic sign, not reassurance.**
> In an older person, **new confusion, a fall, reduced oral intake or functional decline may be the only sign of a serious infection.** The parallel warning for the surgical abdomen in the old is at [[03_Gastrointestinal]] 0.41.6 the acute abdomen in special groups; for inflammatory markers, [[Investigation-Interpretation]] notes that a normal CRP does not exclude serious infection.

> [!warning] **Fever patterns are over-taught and under-useful** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> Tertian and quartan patterns in malaria (owned by [[08_07_Infectious_Disease_-_Protozoan_Infections]] Malaria), **Pel-Ebstein fever in Hodgkin lymphoma**, and relative bradycardia in typhoid are classical, examinable, and **unreliable in practice** — modified by antipyretics, by the timing of observations, and by treatment already given. **Do not exclude a diagnosis because the pattern does not fit.**
> **Relative bradycardia** — a heart rate lower than expected for the temperature — retains modest usefulness, described in typhoid, legionella, brucellosis and **drug fever**, but is not diagnostic.

> [!warning] **Drug fever — a diagnosis of exclusion, but a common one, and completely reversible**
> Named as an FUO cause above; these are its features. Fever that may be high, in a patient who **looks better than their temperature suggests**; sometimes **relative bradycardia, eosinophilia or a rash**, but frequently none of these. It may begin days to weeks after the drug was started.
> **Common culprits: beta-lactams, sulfonamides including co-trimoxazole, anticonvulsants (phenytoin, carbamazepine), allopurinol, heparin, antituberculous drugs, and antipsychotics.**
> **Diagnosis is by cessation.** `UNVERIFIED — the expected time to defervescence after stopping the drug.`
> **Document it as an adverse reaction** so the agent is not re-prescribed. The more serious drug-related febrile syndromes — DRESS, neuroleptic malignant syndrome, serotonin toxicity and transfusion reactions — are owned by [[09_08_Dermatology_-_Miscellaneous]], [[11_09b_Ortho_-_Trauma]] and [[10_08_Haemonc_-_Blood_Products_and_Transfusion]].

> [!tip] **Fever after solid organ transplant follows a timeline**
> **First month** — nosocomial and surgical-site infection, and infection related to the operation itself.
> **One to six months** — **opportunistic infection**: CMV, *Pneumocystis jirovecii*, fungal disease, and reactivation of latent infection.
> **Beyond six months** — community-acquired infection, plus late opportunistic infection in those on heavier immunosuppression.
> Transplant immunosuppression regimens and the non-infective complications are owned by [[07_Renal_Medicine_and_Urology]] 0.2.6 Complications of transplant and lifelong immunosuppression, not repeated here.

## Pyrexia of unknown origin (PUO) / Fever of unknown origin (FUO)

> [!note] Expanded from CSV ("Fever of unknown origin," High yield) — the original entry was genuinely thin (a one-line definition and a bare causes list) for a High-yield topic; expanded with a systematic approach, Ix, and Mx. Verified against the NSW Agency for Clinical Innovation's FUO clinical tool, Aug 2026 — PUO and FUO are the same entity under different terminology (PUO the more traditional/British term, FUO more commonly used internationally including in current Australian resources); both are used interchangeably here.

- **D (classic definition, Petersdorf/Durack-Street criteria):** fever >38.3°C on several occasions, for >3 weeks' duration, with no cause identified despite 3 days of inpatient evaluation or ≥3 outpatient visits (the original 1961 definition required 1 week of *inpatient* evaluation specifically; this was revised in 1991 to reflect that thorough outpatient work-up is now often possible, so a lack of hospital admission doesn't preclude the diagnosis).
- **A genuinely important framing point:** FUO/PUO is most commonly an **atypical presentation of a common condition**, rather than a rare or exotic disease — this should shape the initial differential and Ix priorities, which is why the systematic approach below front-loads common causes before considering rarer possibilities.

> [!info] Classification into four categories (Durack-Street) — each with a genuinely different differential, so establishing which category applies early helps focus the work-up:
> - **Classic FUO:** the presentation above in an otherwise non-hospitalised, non-neutropenic, HIV-negative patient.
> - **Nosocomial FUO:** fever developing in a hospitalised patient, not present or incubating on admission, with no diagnosis after 3 days of appropriate investigation — differential shifts toward hospital-acquired infection (line infection, C. difficile, drug fever, post-operative complications, DVT/PE).
> - **Neutropenic FUO:** fever in a patient with a significantly low neutrophil count — a genuine emergency requiring urgent empirical broad-spectrum antibiotics rather than an unhurried diagnostic work-up (see [[10_10a_Haemonc_-_Haematological_and_Oncological_Emergencies]] Neutropenic sepsis for the AU-verified acute management approach, not repeated here) — the diagnostic-approach framework below applies once the acute emergency has been addressed, not instead of it.
> - **HIV-associated FUO:** fever of >4 weeks (outpatient) or >3 days (inpatient) in a person with confirmed HIV infection — differential shifts toward opportunistic infection (see [[04_Neurology]] CNS Infections Associated with Immunosuppression for relevant AU-verified detail, not repeated here) and HIV-associated malignancy.

**Causes — broad categories, genuinely useful as a mental checklist given the range is wide:**
- **Infection** (the single largest category in most series) — TB (including extrapulmonary), abscess (intra-abdominal, dental, or elsewhere occult), infective endocarditis, osteomyelitis, and a wide range of less common infections guided by specific risk factors/exposures.
- **Malignancy** — lymphoma classically, but also leukaemia, renal cell carcinoma (hypernephroma), atrial myxoma, and other occult malignancies.
- **Autoimmune/rheumatological/inflammatory** — connective tissue disease, vasculitis (see [[12_04_Rheum_-_Vasculitis]], not repeated here), adult-onset Still's disease, giant cell arteritis (particularly relevant in patients >50 given the genuinely serious visual-loss risk if missed — screen specifically for headache, jaw claudication, scalp tenderness, and visual symptoms in this age group).
- **Miscellaneous** — drug fever (a genuinely easy-to-miss cause, since it requires actively reviewing the medication list rather than assuming a new diagnosis), thromboembolic disease, endocrine causes, and a substantial proportion of cases that remain undiagnosed even after thorough work-up (a reasonable minority of cases resolve spontaneously without ever reaching a specific diagnosis).

**Approach — disciplined and stepwise, not a reflexive battery of tests:**
1. **Confirm true fever** — document measured temperatures (not just patient-reported subjective fever), review the pattern, duration, associated rigors/sweats, and response to antipyretics; a fever diary is genuinely useful here.
2. **Repeat a full history and examination** — specifically revisit medications (drug fever), exposures (travel, animals, insects/ticks, occupational), and repeat the physical exam given findings can evolve or be initially missed; targeted history clues matter — e.g. weight loss *without* anorexia points more toward infection, while weight loss *with* anorexia points more toward malignancy.
3. **Targeted, risk-guided investigation rather than an indiscriminate panel:** blood cultures ×3 (particularly if endocarditis, bacteraemia, an indwelling line, or prosthetic material is a possibility); FBC, inflammatory markers, LFTs, U&Es; HIV and hepatitis serology, TB testing (noting TST/IGRA cannot distinguish active from latent TB) based on risk; CT chest/abdomen/pelvis or targeted imaging for occult malignancy, abscess, lymphadenopathy, or TB; echocardiography if endocarditis risk or positive blood cultures; ferritin, ANA/ENA, ANCA, complement — only when the history/examination genuinely supports an inflammatory/rheumatological cause, not ordered by default for every case.
4. **Tissue diagnosis** where imaging or clinical suspicion points to a specific target — excisional lymph node biopsy, bone marrow biopsy, abscess drainage, or organ biopsy.
5. **Specialist referral** (infectious diseases or general/internal medicine) for persistent unexplained fever, TB or endocarditis concern, or unusual exposures — genuinely appropriate given the breadth of this differential.

**Mx:** **stable patients do not automatically need empirical antibiotics** — a genuinely important principle, given the temptation to treat empirically can obscure the underlying diagnosis (e.g. partially treating an infection without curing it, making subsequent cultures falsely negative) without addressing the actual cause; the highest-yield action is targeted, risk-guided investigation with repeated reassessment over time, not reflexive treatment. Treat the underlying cause once identified. Neutropenic FUO is the clear exception, requiring urgent empirical treatment as above, not repeated here.

### Added from unverified layer — FUO: three things the approach above does not name
`SRC:K1_Fever_Workup §0.3` `UNVERIFIED — model knowledge, not source-checked.`

> [!tip] **PET-CT has become genuinely useful in FUO**
> It identifies occult infection, inflammation and malignancy in one study and **directs biopsy**, which is the step that actually makes the diagnosis. It is one of the few broad investigations that earns its place in a workup the entry above deliberately keeps targeted.
> `UNVERIFIED — availability, funding and indications for PET-CT in FUO in Australia; Medicare Benefits Schedule and local nuclear medicine policy would settle it.`
> **Biopsy anything accessible and abnormal** — lymph node, skin lesion, temporal artery, bone marrow, liver lesion. **Histology diagnoses FUO more often than serology does.**

> [!info] **Adult-onset Still disease — the features, not just the name** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> Named in the causes list above. What identifies it: **a quotidian (once-daily spiking) fever · an evanescent salmon-pink rash that comes and goes with the fever spikes · arthralgia · and a very high ferritin.**
> The rash is the same one described in **systemic-onset juvenile idiopathic arthritis** at [[11_10_Ortho_-_Paediatric_Orthopaedics]] Juvenile idiopathic arthritis (JIA) — the paediatric counterpart of this disease, and the only place the corpus previously carried it.

> [!danger] **Haemophagocytic lymphohistiocytosis (HLH)** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> A hyperinflammatory syndrome of persistent fever, cytopenias, splenomegaly and **a strikingly high ferritin**, triggered by infection, malignancy or rheumatological disease. It is rapidly fatal untreated and is missed because it looks like sepsis that is not responding.
> **Consider it when a very high ferritin accompanies persistent fever and falling counts.** `UNVERIFIED — the diagnostic criteria, the ferritin threshold, and treatment; a haematology source would settle it.`
> **Note the acronym collision before searching for this:** every `HLH` in the corpus outside this block is **hypoplastic left heart** in [[15_05_Paeds_-_Acyanotic_Congenital_Heart_Disease]].

## Approach to Fever in the Returned Traveller

> [!note] Gap-filled from CSV ("Return traveller fever," Medium yield) — the individual travel-related diseases (Malaria, Dengue fever, Yellow fever, Enteric fever/typhoid, Leptospirosis, Schistosomiasis, Trypanosomiasis) are all built across this project's Infectious Disease files, and the history-taking approach is already established in [[History-Taking]] Fever and Suspected Infection (the travel-history block within itected Infection entry) — this entry adds the organising framework that ties the differential together, given incubation period is genuinely one of the most useful ways to narrow it. Not repeated here: the individual disease-level Ix/Mx detail, or the history-taking questions themselves.

**The single most important principle, worth stating before any framework: malaria must be actively excluded in any febrile returned traveller from an endemic area, regardless of how mild the presentation looks or how unlikely malaria seems** — falciparum malaria can deteriorate rapidly and unpredictably, and this exclusion should happen early rather than only after other causes have been worked through.

**Organising the differential by incubation period — genuinely useful given it can substantially narrow the list based on the travel timeline alone:**

> [!info] Short incubation (<10 days)
> Dengue fever (see [[08_05-06_Infectious_Disease_-_Viral_Infections]] Dengue fever, not repeated here); chikungunya; most bacterial gastroenteritis (see [[08_10_Infectious_Disease_-_Diarrhoea_DDx_and_Gastroenteritis]], not repeated here); early enteric fever/typhoid; rickettsial infections (e.g. spotted fever); yellow fever (see [[08_05-06_Infectious_Disease_-_Viral_Infections]] Yellow fever, not repeated here).

> [!info] Medium incubation (10–21 days)
> **Malaria** (see [[08_07_Infectious_Disease_-_Protozoan_Infections]] Malaria, not repeated here — genuinely the diagnosis that must never be missed regardless of which incubation band the presentation otherwise fits, given *P. falciparum* can present outside the classic timeline); enteric fever/typhoid (see [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Enteric fever (typhoid / paratyphoid), not repeated here); leptospirosis (see [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Leptospirosis, not repeated here); brucellosis.

> [!info] Long incubation (>21 days)
> Malaria (can still present this late, particularly *P. vivax*/*P. ovale* with their dormant liver-stage hypnozoites causing delayed relapse); tuberculosis; viral hepatitis; schistosomiasis (see [[08_07_Infectious_Disease_-_Protozoan_Infections]] Schistosomiasis, not repeated here — acute Katayama syndrome specifically has a longer latency after freshwater exposure); amoebic liver abscess; HIV seroconversion illness.

**Practical points beyond the incubation-period framework:**
- **Non-travel causes remain part of the differential** — a returned traveller can still have a completely unrelated, locally-acquired cause of fever, and travel history shouldn't crowd out the standard differential entirely, particularly if the timeline or exposure pattern doesn't fit a travel-related cause.
- **Specific exposures narrow the differential further than destination alone** — freshwater swimming (schistosomiasis, leptospirosis), animal contact (brucellosis, rabies exposure), insect/tick bites, sexual contact, food and water sources, and healthcare contact abroad (antimicrobial-resistant organism risk) — see [[History-Taking]] Fever and Suspected Infection for the travel-history questions that elicit these, not repeated here.
- **Malaria prophylaxis adherence doesn't exclude malaria** — no chemoprophylaxis regimen is 100% effective, and poor adherence is common; malaria should still be actively tested for (thick and thin blood films, or rapid antigen testing) in a febrile returned traveller from an endemic area regardless of reported prophylaxis use.

### Added from unverified layer — four things the incubation framework does not carry
`SRC:K1_Fever_Workup §0.4` `UNVERIFIED — model knowledge, not source-checked.`

> [!danger] **Rickettsial infection — LOOK FOR THE ESCHAR**
> **Scrub typhus, the spotted fevers (including Australian tick typhus) and murine typhus** present with fever, headache, myalgia and rash — and with **an eschar at the bite site**, a small, painless, black-crusted ulcer that **makes the diagnosis**.
> **It is missed because of where it hides: the axilla, the groin, under the breast, behind the knee, in the scalp and between the toes.** Undress and look.
> **Doxycycline is the treatment and is given empirically on suspicion**, because serology is retrospective and confirms the diagnosis after the decision has been made. Doxycycline's rickettsial indications are listed in [[NEW_Drugs_05_Anti_infectives]].
> **Search note:** every other `eschar` in this corpus is anthrax ([[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Anthrax), burns escharotomy or acid coagulative necrosis ([[11_09b_Ortho_-_Trauma]]). The word alone will not find this.

> [!danger] **Melioidosis — an Australian diagnosis, not a travel one**
> *Burkholderia pseudomallei*, in soil and surface water in **northern Australia**, with cases concentrated in **the wet season** and after flooding, storms and cyclones.
> **The risk groups are the point: diabetes, chronic kidney disease, harmful alcohol use, chronic lung disease, and Aboriginal and Torres Strait Islander people.**
> It presents as **severe community-acquired pneumonia, sepsis, or abscesses anywhere** — including prostatic, hepatic, splenic and cerebral — and it is missed when a severe pneumonia in a northern-Australian patient with diabetes is treated as ordinary CAP.
> **It requires specific and prolonged antimicrobial therapy** — an intensive intravenous phase followed by months of oral eradication. `UNVERIFIED — the agents, doses and durations of both phases, per Therapeutic Guidelines: Antibiotic and the NT/Qld melioidosis protocols.`

> [!warning] **Murray Valley and Japanese encephalitis — named on the notifiable list, but not as diagnoses**
> Both appear in this corpus only inside the NNDSS vector-borne category at [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Notifiable Diseases (Australia). As clinical entities: **mosquito-borne flaviviruses, with recent Australian activity**, to be considered in **encephalitis after inland, riverine or irrigation-area exposure**, particularly in the warmer months and after flooding.
> **Japanese encephalitis has a vaccine** and is now part of targeted Australian programmes. `UNVERIFIED — current eligibility for JE vaccination in Australia, per the Australian Immunisation Handbook and state health advice.`
> Most infections are asymptomatic; a small minority develop encephalitis, and that minority carries substantial mortality and long-term neurological sequelae. Encephalitis assessment itself is owned by [[04_Neurology]], not repeated here.

> [!info] **Zika** `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> Mosquito-borne, usually mild or asymptomatic, with fever, rash, conjunctivitis and arthralgia. **It matters almost entirely for its congenital risk** — infection in pregnancy causes fetal brain abnormalities including microcephaly. **Sexual transmission occurs**, which is why advice covers partners as well as travellers.
> **The clinically relevant action is pre-conception and pregnancy travel advice**, not the acute illness. `UNVERIFIED — current Australian advice on conception delay after travel to an area with Zika transmission, and which areas currently qualify; Smartraveller and the Australian Immunisation Handbook would settle it.`

## Sepsis

> [!note] See [[01_Cardiovascular]] Infective Endocarditis for the modified Duke criteria — the analogous structured diagnostic framework for a different specific infection, not repeated here.

> [!info] Gap-filled — "bacteraemia" and "septicaemia" are used correctly throughout this project (e.g. in Lemierre's syndrome, spinal epidural abscess) as complications of specific infections, but the terms themselves were never defined or related to "sepsis." **Bacteraemia** simply means the presence of viable bacteria in the bloodstream — it can be transient and entirely asymptomatic (e.g. briefly after tooth brushing), and does **not** by itself imply illness. **Septicaemia** is an older, less precise term for a bloodstream infection causing systemic illness — largely superseded in current clinical use by the more precisely defined **sepsis** (below), which specifically requires life-threatening organ dysfunction, not just bacteraemia or a systemic infection. The practical relationship: bacteraemia can progress to sepsis if the host response becomes dysregulated and organ dysfunction develops, but bacteraemia alone (without organ dysfunction) doesn't meet the definition of sepsis — this is precisely why blood cultures confirming bacteraemia don't automatically mean a patient has "sepsis" in the modern, clinically actionable sense of the term.

- **D:** life-threatening organ dysfunction caused by a dysregulated host response to infection.

> [!info] Added from unverified layer — **why the definition changed, and what SIRS was**
> `SRC:A1_Emergency_-_Deteriorating_Patient__Sepsis__Cardiac_Arrest §0.2` `UNVERIFIED — model knowledge, not source-checked. The formal definition history, per the Sepsis-3 papers.`
> The definition above is deliberately about **organ dysfunction**, not inflammation. It replaced
> **SIRS** — temperature, heart rate, respiratory rate and white cell count — which describes a
> **generic inflammatory response** and therefore **fires in pancreatitis, trauma, burns and the
> ordinary post-operative state with no infection at all.** SIRS was sensitive and unspecific;
> the current definition is anchored on the organ dysfunction that makes sepsis lethal.
> **Worth knowing because SIRS criteria are still in circulation** on older charts and in older
> teaching, and a patient can be SIRS-positive and not septic, or septic and SIRS-negative.
> (Note: in Australian aged-care documents `SIRS` means the **Serious Incident Response Scheme** — an unrelated acronym, see [[Clinical-Process-EBM-Consent-Capacity]].)

> [!fail]- CONFLICT CF-034 — is qSOFA a screening tool or a prognostic flag? **R2**
> **A (`inherited`):** the box below — *"qSOFA — **quick screening tool** to identify patients at increased risk of sepsis"*, with its three components.
> **B (`unverified`):** `SRC:A1_Emergency_-_Deteriorating_Patient__Sepsis__Cardiac_Arrest §0.2` — *"**qSOFA is a prognostic flag, not a screening tool.** It identifies infected patients at higher risk of poor outcome. It is **insensitive as a bedside screen**, and a **negative qSOFA does not exclude sepsis**."*
> **Why it matters:** the components are identical either way, so nothing in the box looks wrong — **the dispute is entirely about what the result licenses you to do.** A clinician using it as a screen, and getting a negative, may not escalate a septic patient. The failure is silent: the score performs exactly as designed while being used for the wrong purpose.
> **Resolve against:** the Australian Commission on Safety and Quality in Health Care sepsis materials, the NSW ACI / "SEPSIS KILLS" pathway documentation (already cited below), or the Sepsis-3 definition papers.

> [!info] qSOFA — quick screening tool to identify patients at increased risk of sepsis
> - RR >22
> - SBP <100
> - Altered mentation

> [!info] Verified — Australia has its own named sepsis pathway, distinct from the UK's "Sepsis 6" branding, though the underlying clinical actions are broadly similar in substance. **"SEPSIS KILLS"** (developed by NSW's Clinical Excellence Commission, now used in >200 health facilities and referenced by the Australian Commission on Safety and Quality in Health Care's national Sepsis Clinical Care Standard) organises the response around three actions — **RECOGNISE** (risk factors, signs/symptoms), **RESUSCITATE** (rapid IV fluids and antibiotics), **REFER** (to senior clinicians/specialty teams for source control and specialist care) — with a specific target of **IV antibiotics within 60 minutes of presentation**, rather than the "Sepsis 6" naming/framing below. The individual clinical actions in the "3 in/3 out" mnemonic below (oxygen, antibiotics, fluids; cultures, lactate, urine output) are pharmacologically/clinically sound regardless of which branded pathway a given Australian hospital uses, and most Australian EDs will have their own local sepsis pathway/order set implementing these same core actions under the SEPSIS KILLS or an equivalent local branding — check the specific hospital's own protocol/order set for the exact local process, but the underlying content below doesn't need clinical correction, only the "Sepsis 6" name/UK-attribution.
> **3 in:**
> - O2 — aim sats >94%
> - Broad spectrum antibiotics
> - IV fluids — 500mL crystalloid over 15 minutes
>
> **3 out:**
> - Blood cultures
> - Measure serum lactate
> - Measure urine output hourly

- Within ICU, a full SOFA score is used. SOFA >2 increases mortality by 10% compared to other patients. Components: PaO2, platelets, bilirubin, cardiovascular (MAP, use of vasopressors), GCS, creatinine, urine output per day.

## Spinal epidural abscess

- **D:** collection of pus superficial to the dura mater.

> [!danger] Medical emergency.

- **A:** usually *S. aureus*.
- **P:** contiguous spread from adjacent structures (e.g. discitis), haematogenous spread (e.g. bacteraemia from IVDU), or direct infection (e.g. surgery).
- **S/Smx:** fever, back pain, focal neurological deficits according to the segment of cord affected.

> [!danger] **The classic triad of back pain, fever and neurological deficit is present in only about 10% of cases** — so an incomplete picture is the *usual* picture, and its absence must not reassure. [[04_Neurology]] Spinal Epidural Abscess owns the four clinical stages this progresses through (localised pain → radicular pain → weakness and sphincter dysfunction → paralysis), which is the more useful frame than the triad. Caveat carried here by the pairs audit (2026-08-29) — this entry listed the triad with no indication of how rarely it is complete.
- **Ix:** bloods, blood cultures, infection screen (including CXR, urine cultures) (*why:* screens for the causative organism and any concurrent/source infection given the contiguous, haematogenous, or direct-inoculation spread mechanisms above; *what:* may identify *S. aureus* bacteraemia or another source). MRI whole spine (*why:* the definitive imaging test, both confirming the diagnosis and defining the extent of the abscess (given epidural abscesses can span multiple levels) — essential for surgical planning if evacuation is needed; *what:* an epidural collection, often with cord/thecal sac compression visible, directly correlating with the neurological deficit pattern).
- **Mx:**
  - **Immediate/acute:** urgent neurosurgical/spinal referral, given the risk of progressive cord compression and irreversible neurological deficit if decompression is delayed — this shares the same time-critical, "don't wait for full work-up if focal deficit is present" urgency as cauda equina syndrome and malignant spinal cord compression (see [[04_Neurology]] for both, not repeated here); empirical broad-spectrum IV antibiotics started promptly, covering *S. aureus* (including MRSA where locally relevant) given this is the most common causative organism per the A/P above.
  - **Definitive:** surgical evacuation/decompression for large abscesses, evidence of cord compression, or those not responding to antibiotics alone; long-term antibiotics (often several weeks), refined once culture/sensitivity results (from blood cultures or surgical specimens) are available.
  - **Chronic/long-term:** address any identifiable source (e.g. treat the primary discitis or bacteraemia source) to prevent recurrence; rehabilitation if a neurological deficit has occurred, given recovery depends heavily on how promptly decompression occurred relative to deficit onset.

## Added from unverified layer — suppurative lymphadenitis
`SRC:K2_Skin_and_Soft_Tissue_Infection §0.4` `UNVERIFIED — model knowledge, not source-checked.`

> [!tip] **A large, tender, fluctuant node is not always a bacterial abscess**
> **· Bacterial** — *S. aureus* and group A *Streptococcus*, acute and fluctuant, drained and treated as an abscess.
> **· Mycobacterial** — **tuberculous cervical lymphadenitis, "scrofula"**: `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.` **matted, minimally tender nodes evolving over weeks**, with overlying violaceous skin and possible **sinus formation**. **Incision produces a chronically discharging sinus rather than resolution — the diagnostic step is aspiration or excision biopsy with mycobacterial culture, not drainage.**
> **· Non-tuberculous mycobacterial lymphadenitis** — most often a **well child** with a single chronically enlarging cervical node and no systemic upset; managed surgically rather than with antibiotics.
> **· *Bartonella henselae*** — regional lymphadenopathy weeks after a cat scratch, usually self-limiting. Owned by [[08_01-03_Infectious_Disease_-_Bacterial_Infections]] Cat scratch disease.
> **· Malignancy** — **a persistent, hard, fixed or matted node is not an abscess and must not be drained as one.** Lymphoma is owned by [[10_02_Haemonc_-_Lymphomas_and_Multiple_Myeloma]].

## Nematode infections

- ***Ancylostoma braziliense*** — most common cause of cutaneous larva migrans; Central/South America.
- ***Strongyloides stercoralis*** — percutaneous entry, e.g. walking barefoot. Causes pruritus and larva currens (similar appearance to cutaneous larva migrans, but moves through the skin at a far greater rate). Abdominal pain, diarrhoea, pneumonitis. May cause Gram -ve septicaemia due to carrying of bacteria into the bloodstream. Eosinophilia sometimes seen.
  - **Mx:** thiabendazole, albendazole, ± ivermectin (especially chronic infection).
- ***Toxocara canis*** — spread by ingesting eggs from soil contaminated by dog faeces. Commonest cause of visceral larva migrans. Eye granulomas, liver/lung involvement.

## Threadworms (pinworms)

- **A/P:** *Enterobius vermicularis*. Spread by ingesting eggs. Affects children.
- **S/Smx:** asymptomatic in 90%. Perianal itching, especially at night. Girls may have vulval symptoms.
- **Dx:** usually clinical. If confirmation needed, apply tape to the perianal area ("swab") and send for microscopy to find eggs.
- **Mx:** antihelminthic for the whole household — mebendazole (single dose), with hygiene measures.

## Antimicrobial side effects

| Drug | Key side effects |
|---|---|
| Metronidazole | Disulfiram-like reaction with alcohol; ↑anticoagulant effect of warfarin |
| Rifampicin | RNA polymerase inhibitor; potent P450 inducer; red urine; hepatitis; flu-like symptoms |
| Cotrimoxazole | Hyperkalaemia; headache; rash (including Stevens-Johnson syndrome) |
| Vancomycin | Nephrotoxicity; ototoxicity; thrombophlebitis; red man syndrome |
| Aminoglycosides | Haematologic SE including agranulocytosis; ototoxicity |
| Tetracyclines (e.g. doxycycline) | Tooth discolouration — avoid in <12yo, pregnancy, breastfeeding; photosensitivity; angioedema; black hairy tongue |
| Trimethoprim | Myelosuppression; transient ↑creatinine (competitive inhibition, not true renal impairment); teratogenic risk in 1st trimester — avoid in pregnancy |

---

## Notifiable Diseases in Australia — What "Notifiable" Actually Means

> [!note] Gap-filled — "Notifiable disease" appears as a bare flag on at least 7 separate conditions scattered throughout this project (measles, mumps, pertussis, diphtheria, and others), but nowhere is the underlying system explained. This entry fills that gap. ("Notifiable diseases & public health reporting" is explicitly a High-yield CSV item, filed under a not-yet-uploaded Public Health category — but the concept is already load-bearing content throughout this project's existing disease entries, exactly analogous to how MMSE/MoCA needed explaining despite being filed under a separate Geriatrics category, addressed elsewhere in this project.) Verified against SA Health's notifiable disease reporting requirements and the Australian CDC's National Notifiable Diseases Surveillance System (NNDSS) overview, Aug 2026.

**The core system:** the **National Notifiable Diseases Surveillance System (NNDSS)** coordinates national surveillance data for a legislated list of over 70 diseases that present a risk to public health (the National Notifiable Disease List). Each state and territory runs its own notification and public health response under its own legislation — in South Australia, this is the **South Australian Public Health Act 2011** — with de-identified data supplied daily to the national system for collation and analysis. The purpose is genuinely practical, not just administrative: enabling early public health action (contact tracing, outbreak identification, targeted intervention) and informing public health policy (e.g. the National Immunisation Program).

**Who must notify, and how:** in South Australia, **both medical practitioners and laboratories** are legally required to notify each episode of a notifiable condition to the Communicable Disease Control Branch (CDCB) — notification is not solely the laboratory's responsibility, and a clinician's own suspected/clinical diagnosis can itself trigger the requirement even before laboratory confirmation.

**Timeframe — genuinely two-tiered, not a single blanket rule:**
- **Most notifiable conditions:** notify **within 3 days** of suspecting or confirming the diagnosis — this is the routine/default timeframe, typically via the online notification form.
- **Selected conditions requiring urgent public health action** (e.g. those with high transmission risk or outbreak potential — meningococcal disease is the classic example, given the time-critical need for contact prophylaxis) are **phone-notifiable**, meaning immediate telephone notification is required rather than waiting for the standard 3-day written process — this distinction matters clinically, since treating every notifiable disease as equally urgent both over- and under-responds depending on the specific condition.

**Practical relevance to this project's content:** every condition flagged "Notifiable disease" throughout the Infectious Disease, Dermatology, and Paediatrics files (e.g. measles, mumps, pertussis, diphtheria — see the individual entries for the specific flags, not repeated here) falls under this same system — the flag itself is a prompt to notify per the framework above, not a separate requirement unique to each disease. **A genuinely useful exam-relevant principle: notification is based on clinical/reasonable suspicion, not confirmed diagnosis** — waiting for definitive laboratory confirmation before notifying a condition that's already clinically apparent defeats the purpose of early public health action, particularly for conditions on the phone-notifiable/urgent list.
