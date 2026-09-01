---
block: Older Persons Health / Geriatrics
source: built from scratch — CSV category "Older Persons Health / Geriatrics (NEW)"; no equivalent existed in the source notes, which is why this whole category was absent until now
trust: inherited
population: mixed
conflicts_open: 0
conflicts_r1: 0
no_baseline: 1
---

> [!note] Why this file exists. The CSV category "Older Persons Health / Geriatrics (NEW)" had **no corresponding file at all** — the single largest gap found in this project (Step 21). An audit of its 11 rows before building found that three were already adequately covered elsewhere and are deliberately **not** duplicated here: capacity assessment (see [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework), the cognitive screening tools themselves (see [[Investigation-Interpretation]] Cognitive Screening Tools (MMSE, MoCA, AMTS)), and osteoporosis management (see [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis, which is verified against the 2024 RACGP/Healthy Bones Australia guideline). Two further rows were built into [[04_Neurology]] rather than here, because their structural anchors already live there.
>
> This file holds the topics that no organ system owns — which is precisely why they had no home before.

## Falls in Older People

> [!note] Gap-filled from CSV ("Fall (recurrent falls)," High yield, and the falls-prevention half of "Osteopenia/osteoporosis management & falls-related fracture prevention"). Genuinely absent as clinical content: falls appeared only as a history-taking checklist bullet in [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls), which is an OSCE communication framework rather than an assessment or management approach. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Part A "Falls", the Australian Commission on Safety and Quality in Health Care falls guidelines for community care, the Cochrane review of exercise for preventing falls (Sherrington et al.), and the Exercise & Sports Science Australia position statement on exercise for falls prevention, Aug 2026.

**D:** an event resulting in a person unintentionally coming to rest on the ground or a lower level. **Roughly one third of community-dwelling people aged over 65 fall each year**, and the proportion rises with age and in residential aged care.

> [!danger] The single most important framing: a fall is a **symptom, not a diagnosis**. "Mechanical fall" is not a diagnosis either, and writing it in the notes closes an assessment that should be opening one. The cause is **multifactorial in most older fallers** — typically several modest contributors acting together rather than one dramatic cause — which is why single-intervention approaches underperform and why a multidisciplinary response is the standard.

### Distinguishing a fall from a collapse — do this first

The first branch point is whether consciousness was lost, because it splits the work-up entirely:

- **Transient loss of consciousness** → this is a *collapse*, and the differential is syncope vs seizure vs hypoglycaemia. Take that pathway instead: see [[History-Taking]] Collapse (Conscious and Unconscious) for the structured before/during/after history and [[04_Neurology]] Syncope for the differential, not repeated here.
- **No loss of consciousness** → this is a fall, and the multifactorial assessment below applies.

**In practice the distinction is often genuinely unclear**, because amnesia for the event is common in older people and there may be no witness. Where you cannot confidently exclude loss of consciousness, screen for the dangerous syncopal causes (postural blood pressure, cardiac examination, ECG) *as well as* running the falls assessment — do not simply pick one branch on the balance of probabilities.

### Risk factors — the ones worth actually asking about

**Intrinsic:**
- **Previous falls** — the strongest single predictor. A fall in the past year should trigger the full assessment.
- **Impaired balance and gait**, and **reduced lower-limb muscle strength** (sarcopenia) — the two most consistently identified modifiable contributors.
- **Visual impairment** — cataract, uncorrected refractive error, and specifically **multifocal/bifocal spectacles**, which blur the lower visual field exactly where the ground and steps are (see [[05_Ophthalmology]] Cataracts).
- **Cognitive impairment and delirium** — impaired judgement of hazards and, in delirium, fluctuating attention (see [[04_Neurology]] Dementias and [[04_Neurology]] Delirium).
- **Postural (orthostatic) hypotension** — common, frequently drug-related, and readily missed if the blood pressure is only ever taken sitting.
- **Peripheral neuropathy** — loss of proprioceptive input (see [[04_Neurology]] Diabetic Neuropathy for the commonest cause and its glove-and-stocking distribution, not repeated here).
- **Continence problems** — urgency and nocturia drive hurried, poorly-lit trips to the toilet.
- **Foot problems and inappropriate footwear** — pain, deformity, and loose or backless shoes.
- **Fear of falling** — a genuine risk factor in its own right, not merely a consequence: it drives activity avoidance, which causes deconditioning and further weakness, which raises fall risk again. Ask about it explicitly, because patients rarely volunteer it.

**Extrinsic (environmental):** loose rugs and trailing cords, poor lighting (particularly on stairs and the route to the toilet at night), absent grab rails in the bathroom, cluttered walkways, unfamiliar surroundings, pets.

> [!warning] Fall-risk-increasing drugs (FRIDs) — review these specifically, by name, rather than glancing at the list
> **Psychotropics are the highest-yield target**: benzodiazepines and Z-drugs, antipsychotics, antidepressants (including SSRIs), and anticonvulsants. Also **cardiovascular agents**: antihypertensives of all classes, diuretics, nitrates, alpha-blockers, digoxin and antiarrhythmics. Also **opioids**, **anticholinergics** (including bladder antimuscarinics, sedating antihistamines, and tricyclics), and **hypoglycaemic agents** (insulin, sulfonylureas).
>
> This matters more than it first appears: **withdrawal of psychotropic medication produced the largest effect of any single falls-prevention intervention in randomised trials** — but the same trial evidence shows sustained withdrawal is genuinely hard to achieve in practice, so this is a deprescribing project with follow-up, not a one-off stop order. See Polypharmacy and Deprescribing below.

> [!warning] Added from unverified layer — **fitting a walking stick: three things that are commonly wrong**
> `SRC:L6_Soft_Tissue_Injury_and_Mobility §0.5` `UNVERIFIED — model knowledge, not source-checked.` `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees with it.`
> A stick that has never been fitted is a fall risk rather than a fall prevention, and all three errors are visible in seconds.
> **· WRONG HAND.** The stick is held in the hand **OPPOSITE** the affected leg, and moves forward **with** that leg — it widens the base and unloads the bad side. Held on the same side it does neither, and most people pick the same side by instinct.
> **· WRONG HEIGHT.** With the person standing upright in their usual shoes, arms relaxed at their sides, **the handle should reach the wrist crease**, giving a slight bend at the elbow. Too tall pushes the shoulder up and is tiring; too short pitches them forward.
> **· WORN OR MISSING FERRULE.** The rubber tip is the only thing between the stick and the floor. **A worn, split or missing ferrule is a slip waiting to happen**, and it is a consumable that nobody thinks to replace. Look at it.
> **Also worth checking:** that the stick belongs to this person and was not inherited from a taller relative, and that they have been shown stairs — **up with the good leg, down with the bad**.
> Referral to physiotherapy or occupational therapy for assessment and prescription is the definitive answer; this is what to check in the meantime.

### Assessment — the multifactorial falls risk assessment

**Screening:** ask every older patient about falls in the past 12 months, and about unsteadiness or fear of falling. Two or more falls in a year, one fall with injury, or reported gait/balance difficulty all warrant the full multifactorial assessment.

**History:** the circumstances of each fall (what they were doing, indoors/outdoors, time of day, footwear, any prodrome), whether consciousness was lost, whether they could get up unaided and how long they were down, injuries sustained, and **fear of falling and consequent activity restriction**. Collateral history where cognition is impaired.

> [!tip] "Have you had any falls?" under-detects, because many older people do not classify a stumble or a slide to the floor as a fall, and some minimise it for fear of losing independence. Ask instead: *"Have you had any slips, trips or falls, including ones where you didn't hurt yourself?"* — and follow up with *"Have you been more unsteady on your feet?"*

**Examination:**
- **Lying and standing blood pressure** — measured supine after 5 minutes, then at 1 **and** 3 minutes standing. A sustained drop of **≥20 mmHg systolic or ≥10 mmHg diastolic** defines orthostatic hypotension. This is the highest-yield bedside test in a faller and is very commonly omitted. **Both timings matter, and the reason is derivable rather than arbitrary:** the immediate drop on standing is normally corrected within seconds by the baroreflex, so a reading at 1 minute captures failure of that reflex — while **delayed orthostatic hypotension**, where compensation succeeds initially and then fails, is missed entirely by a single early reading. Measuring from *sitting* rather than lying under-detects both, because the postural change is smaller and the venous pooling less.
- **Gait and balance**, observed directly. The **Timed Up and Go (TUG)** is the standard bedside tool: time the patient rising from a standard chair, walking 3 metres, turning, returning and sitting down. **Longer than about 10–12 seconds identifies community-dwelling older adults more likely to fall** and should prompt physiotherapy referral. Watch *how* they do it, not just the clock — hesitancy, a wide base, multiple steps to turn, or reaching for furniture are all informative.
- **Cardiovascular:** heart rate and rhythm, murmurs (aortic stenosis as a syncopal cause).
- **Neurological:** lower-limb power and tone, proprioception and vibration sense, cerebellar signs, and features of parkinsonism.
- **Vision** — acuity, and specifically ask whether they wear multifocals when walking outdoors or on stairs.
- **Feet and footwear** — inspect both, including the shoes they actually walk in at home.
- **Cognitive screen** where not already known (see [[Investigation-Interpretation]] Cognitive Screening Tools (MMSE, MoCA, AMTS)).

**Ix:** directed by the assessment rather than a reflex panel. FBC (*why:* anaemia contributes to postural symptoms and fatigue; *what:* low Hb), U&Es (*why:* dehydration and electrolyte disturbance both cause postural hypotension and confusion, and diuretics are a common contributor; *what:* raised urea/creatinine, hyponatraemia), blood glucose (*why:* hypoglycaemia is a reversible cause of falls and of apparent confusion in patients on insulin or sulfonylureas; *what:* low BGL), **vitamin D and calcium** (*why:* deficiency contributes to myopathy and to fracture risk, and identifies who benefits from supplementation; *what:* low 25-OH vitamin D), and **ECG** (*why:* screens for bradyarrhythmia, heart block, and prolonged QT as syncopal causes that a purely "mechanical" framing would miss; *what:* conduction abnormality, arrhythmia). **Imaging only where injury is suspected clinically** — a CT head is indicated for a head strike with anticoagulation, reduced consciousness, or focal neurology, not routinely after every fall.

### Mx — what actually works

- **Immediate/acute:** treat injuries (a high index of suspicion for occult hip fracture — see [[11_04_Ortho_-_Hip]] Hip / neck of femur (NOF) fractures — and for subdural haematoma in an anticoagulated patient with a head strike, where presentation can be delayed by days to weeks); assess for and treat the acute precipitant (infection, delirium, dehydration, new medication); and check for a **long lie**, which carries genuine risk of rhabdomyolysis, pressure injury, hypothermia and AKI, and which independently signals that the person cannot summon help.
- **Definitive — the interventions with real evidence:**
  - **Exercise is the single most effective intervention.** The dose and type matter and are frequently prescribed too vaguely: it must **challenge balance**, and the evidence favours a total of **3 or more hours per week, sustained**. Programmes meeting those criteria reduce falls substantially more than the ~25% average effect seen across community exercise programmes generally. Refer to physiotherapy or an accredited exercise physiologist rather than advising "keep active".
  - **Medication review and deprescribing**, targeting the FRIDs above and psychotropics first — see Polypharmacy and Deprescribing below.
  - **Home hazard assessment and modification by an occupational therapist** — most effective in those at higher risk, and more effective when the OT visits the home rather than working from a checklist in clinic.
  - **Vision** — cataract surgery where indicated, updating refraction, and advising **single-vision distance glasses for walking outdoors and on stairs** in multifocal wearers.
  - **Vitamin D** — supplement where deficient. Note the evidence is dose- and setting-dependent: higher-dose supplementation (≥700 IU/day) shows benefit while low-dose does not, and the case is stronger in residential aged care than in vitamin-D-replete community dwellers. **Do not give it routinely to everyone regardless of status.**
  - **Footwear** — well-fitting, low-heeled, thin firm soles, and fastened; treat foot pain and refer to podiatry.
  - **Postural hypotension** — reduce or withdraw the contributing drug first, ensure adequate hydration, advise rising slowly in stages, and consider compression stockings; drug treatment (e.g. fludrocortisone, midodrine) is specialist-initiated and a later step.
- **Chronic/long-term:**
  - **Fracture prevention runs alongside falls prevention, and neither substitutes for the other** — a faller with osteoporosis needs both. Assess bone health and treat per [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis (not repeated here), which carries the AU-specific DXA and treatment-initiation thresholds.
  - Address **fear of falling** directly — it responds to supervised exercise and graded activity, and is a common reason a technically excellent plan achieves nothing.
  - **A personal alarm or similar means of summoning help**, which changes the consequence of a fall even when it cannot prevent one.
  - Referral pathways: falls clinic, geriatrician, community physiotherapy/OT, and an **Aged Care Assessment Team (ACAT)** assessment where support needs have changed — see Discharge Planning and Home Safety Assessment below.

> [!danger] **Aboriginal and Torres Strait Islander people — the age threshold is the actionable point, and getting it wrong delays care by 15 years.** Falls, dementia, pain and urinary incontinence all occur at **younger ages** than in the non-Indigenous population, and the health and aged care systems reflect this: **Aboriginal and Torres Strait Islander people are eligible for aged care assessment and services from age 50, not 65.** Practically, this means a 55-year-old Aboriginal patient presenting with recurrent falls warrants the **full multifactorial assessment and an ACAT referral** — not the reassurance that they are "too young" for a falls work-up, which is the error this threshold exists to prevent. Aboriginal and Torres Strait Islander Aged Care Assessment Organisations exist specifically to provide this assessment in a culturally safe way. Verified against the Australian Government's Aboriginal and Torres Strait Islander aged care eligibility criteria and the RACGP Silver Book chapter on older Aboriginal and Torres Strait Islander people, Aug 2026.

> [!danger] **The same age-50 threshold applies to a second, separate population: people who are homeless or at risk of homelessness.** Aged care eligibility is **65 by default, and 50 both for Aboriginal and Torres Strait Islander people and for people who are homeless or at risk of homelessness** — two distinct groups reaching the same threshold, and worth holding separately rather than merging, since the reasons and the clinical picture differ. What they share is the reason the rule exists: **age-related conditions occur earlier relative to chronological age**, so a threshold set at 65 systematically excludes people who already have the problems it was written for.
> Practically, a **55-year-old who is sleeping rough or in insecure housing and presenting with falls, cognitive change or functional decline is within scope for an aged care assessment** — and the reflex that they are decades too young is the same error as in the box above, in a different guise. This population is also disproportionately likely to present through the emergency department rather than general practice, so the hospital admission may be the only opportunity anyone gets to make the referral. Verified against My Aged Care (Australian Government), Aug 2026.

> [!info] The intervention hierarchy, if you remember nothing else: **balance-challenging exercise at adequate dose, deprescribe the FRIDs, and fix the home and the glasses.** Those three carry most of the evidence. Vitamin D matters where the patient is deficient, and much less where they are not.

---

### Falls — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.5` `UNVERIFIED — model knowledge, not source-checked.`

> [!danger] Falls are the leading cause of injury hospitalisation and injury death in older Australians
> And **a previous fall is the single strongest predictor of a future fall.** Asking "have you had a fall in the last year?" is a one-question screening tool that identifies the highest-risk group.

> [!tip] Risk factors — nearly all of them modifiable
> **· Previous falls · gait and balance impairment · muscle weakness · impaired vision · cognitive impairment and delirium · MEDICATIONS · postural hypotension · foot problems and inappropriate footwear · urinary urgency and nocturia (rushing to the toilet at night) · environmental hazards · vitamin D deficiency · alcohol · fear of falling, which reduces activity and worsens deconditioning.**
> **"Fall-risk-increasing drugs" (FRIDs)** — psychotropics in particular: **benzodiazepines, Z-drugs, antipsychotics, antidepressants, opioids, anticholinergics, antihypertensives and diuretics.** **Withdrawal of psychotropic medication is one of the few single interventions with good evidence for reducing falls.**

> [!danger] Assess WHY they fell — "mechanical fall" is a diagnosis of exclusion
> **Was it a fall or was it syncope?** If unwitnessed, or if the patient does not clearly recall hitting the ground, **assume syncope and investigate accordingly** — cross-refer [[04_Neurology]] Syncope.
> **Ask how long they were on the floor.** A long lie causes **rhabdomyolysis, acute kidney injury, hypothermia, dehydration, pressure injury and pneumonia** — cross-refer [[11_09b_Ortho_-_Trauma]] Hypothermia and [[11_01_Ortho_-_Orthopaedic_Emergencies]] Rhabdomyolysis. It is also a marker of social vulnerability that should trigger a conversation about alarms and living arrangements.
> **Post-fall injury assessment: low threshold for CT head in anyone anticoagulated, even after apparently trivial trauma** — cross-refer [[04_Neurology]] CT Head, Head Injury, and Intracranial Pressure. And **an impacted or undisplaced neck of femur fracture may still allow weight-bearing and may be missed on plain films**, so persistent hip or groin pain warrants further imaging.

> [!tip] Interventions with evidence
> **· Exercise — the single most effective intervention.** It must include a **balance challenge**, be of **sufficient dose and duration**, and be **ongoing** — benefit is lost when it stops. Programs such as Otago and tai chi have good evidence. A generic "keep active" instruction does not work.
> **· Medication review with withdrawal of psychotropics.**
> **· Home hazard assessment by an occupational therapist**, which is most effective in those at highest risk and after a fall.
> **· Vision** — **expedited cataract surgery reduces falls. But NEW multifocal or bifocal glasses INCREASE falls**, particularly outdoors and on stairs, by distorting the lower visual field. Advise single-vision distance glasses for walking outside.
> **· Vitamin D where deficient** — the evidence for supplementation in replete individuals is weak, and **high intermittent bolus dosing has been associated with increased falls**, so this is not a blanket recommendation. `UNVERIFIED — dosing and who should receive it.`
> **· Podiatry and footwear** — well-fitting, low-heeled, firm-soled shoes with good grip. **Walking in socks or loose slippers indoors is a genuine and easily fixed hazard.**
> **· Cardiac pacing** for falls due to cardioinhibitory carotid sinus hypersensitivity.
> **· Treating urinary urgency and providing a night-time toileting plan.**

> [!warning] In hospital, restraints and bed rails cause harm
> **Bed rails and physical restraints increase the severity of injury when a patient does climb over them, cause agitation and delirium, and are associated with worse outcomes.** They are not a falls prevention strategy.
> What helps: **delirium prevention, low-low beds, non-slip footwear, accessible call bells, adequate lighting, proximity to the nurses' station, purposeful hourly rounding including toileting, sensory aids in place, and early mobilisation.**

**S/Smx:** Circumstances, prodrome, whether consciousness was lost, time on the floor, injuries, and the fear and activity restriction that follow.

**Ix:** **Postural blood pressure** (*why:* orthostatic hypotension is common, frequently drug-induced, and easily missed because nobody stands the patient up; *what:* postural drop measured at intervals). **Timed Up and Go and gait observation** (*why:* objective, repeatable, and identifies the gait pattern; *what:* prolonged time, gait abnormality — cross-refer [[04_Neurology]] Gait Disorders). ECG (*why:* arrhythmia as a cause of syncope presenting as a fall; *what:* rhythm, conduction disease). FBC, UEC, calcium, glucose, vitamin D, B12, TFTs (*why:* anaemia, electrolyte disturbance, hypoglycaemia and deficiency all contribute; *what:* derangement). **CK and renal function after a long lie** (*why:* rhabdomyolysis; *what:* raised CK, rising creatinine). Cognitive assessment (*why:* cognitive impairment is a major independent risk factor; *what:* impairment). **Visual acuity and review of glasses** (*why:* correctable, and multifocals are a specific hazard; *what:* uncorrected refractive error, cataract, multifocal use). **Medication review** (*why:* the most modifiable single factor; *what:* FRIDs). **Bone density assessment** (*why:* the fall and the fracture are separate problems and both need addressing — see 0.6; *what:* osteoporosis).

#### Mx – Immediate — GER1 §0.5.1
Injury assessment, analgesia, treatment of the consequences of a long lie, and identification of the precipitant.

#### Mx – Definitive — GER1 §0.5.2
**Multifactorial intervention addressing every identified risk factor** — this is what works; single interventions in isolation generally do not.

#### Mx – Chronic/long-term — GER1 §0.5.3
Ongoing exercise, review of the home, and **address fear of falling directly**, since it drives activity restriction, deconditioning and social isolation, and responds to graded exposure and confidence-building.

### Osteoporosis and Fracture Prevention — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.6` `UNVERIFIED — model knowledge, not source-checked.`

**D:** A skeletal disorder of reduced bone strength predisposing to fracture. Diagnosed by **bone mineral density on DXA** below a defined threshold, **or — regardless of density — by the occurrence of a minimal trauma (fragility) fracture.**

> [!danger] A minimal trauma fracture IS osteoporosis, and most of these patients are never treated
> **A fracture from a fall from standing height or less, in an adult over 50, is a fragility fracture** and identifies a person at high risk of the next one — with the highest risk in the immediately following period.
> **The "treatment gap" is one of the clearest quality failures in Australian practice: the large majority of people who sustain a minimal trauma fracture are never investigated or treated for osteoporosis.** They have their fracture fixed and are discharged.
> **Fracture liaison services exist to close this gap.** As an intern, **the practical action is to identify the fragility fracture, arrange bone density assessment and calcium and vitamin D, and explicitly flag osteoporosis management in the discharge summary with a named responsible clinician.**

> [!tip] Risk factors and secondary causes
> **Non-modifiable:** age, female sex, previous minimal trauma fracture, **parental hip fracture**, early menopause.
> **Modifiable:** **glucocorticoids** (the commonest drug cause, and risk begins early and at modest doses), smoking, excess alcohol, low body weight, immobility, falls, low calcium and vitamin D.
> **Secondary causes to exclude — and they are found in a meaningful proportion, particularly in men and in premenopausal women: hyperparathyroidism · hyperthyroidism (including over-replacement with thyroxine) · coeliac disease · myeloma · hypogonadism · chronic kidney disease · chronic liver disease · Cushing syndrome · rheumatoid arthritis · and drugs including aromatase inhibitors, androgen deprivation therapy, anticonvulsants and long-term PPIs.**
> **Osteoporosis in a man, or in a premenopausal woman, is secondary until proven otherwise.**

> [!danger] Do not stop denosumab without a plan
> **Denosumab discontinuation causes a rapid rebound increase in bone turnover with a risk of MULTIPLE VERTEBRAL FRACTURES**, occurring within months of a missed dose.
> **It must be given on schedule, and it must never simply be stopped** — if it is to be ceased, it requires transition to an alternative agent, usually a bisphosphonate, under specialist guidance.
> **This is a genuine and under-recognised hazard**, and it matters in hospital: a patient admitted for an unrelated reason who misses their scheduled dose is at risk. **Check whether an admitted patient is on denosumab and when their next dose is due.** `UNVERIFIED — dosing interval and the recommended transition regimen.`

> [!warning] Bisphosphonate safety — real risks, kept in proportion
> **Osteonecrosis of the jaw** and **atypical femoral fracture** are both **rare**, and the absolute risk is far outweighed by fracture prevention in patients who meet treatment criteria — but they justify **dental assessment and completion of invasive dental work before starting**, and attention to **new thigh or groin pain in a patient on long-term therapy**, which may herald an atypical fracture.
> **"Drug holidays"** after a period of bisphosphonate therapy are considered in lower-risk patients, and this is a specialist-informed decision. `UNVERIFIED — duration of therapy before a holiday, and who is eligible.`

> [!tip] The whole package, not just a tablet
> **· Calcium — preferably dietary — and vitamin D sufficiency.**
> **· Weight-bearing and resistance exercise.**
> **· Falls prevention (0.5) — because most fractures require both a weak bone AND a fall. Treating osteoporosis while ignoring falls addresses half the problem.**
> **· Smoking and alcohol reduction.**
> **· Antiresorptive or anabolic pharmacotherapy** — bisphosphonates (oral or intravenous), denosumab, and for very high risk teriparatide or romosozumab. Menopausal hormone therapy has a role in selected younger postmenopausal women.
> **· Glucocorticoid-induced osteoporosis prophylaxis** should be considered at the time of prescribing prolonged steroids, not years later.
> `UNVERIFIED — all agents, doses, and the PBS authority criteria that determine what is actually prescribable in Australia.`

**S/Smx:** Usually asymptomatic until fracture. **Vertebral fractures are frequently silent** and present as height loss, kyphosis, or as an incidental finding on imaging done for another reason — **and an incidental vertebral fracture on a chest radiograph or CT is a diagnosis of osteoporosis that is routinely not acted upon.**

**Ix:** **DXA bone mineral density** (*why:* diagnoses osteoporosis, quantifies risk and provides a baseline for monitoring; *what:* T-score at hip and spine). **Absolute fracture risk calculation** (*why:* combines density with clinical risk factors and guides treatment decisions — **the Garvan calculator is Australian and includes falls history**, alongside FRAX; *what:* 5- and 10-year fracture probability). **Calcium, phosphate, ALP, UEC, vitamin D, and TFTs** (*why:* excludes osteomalacia, hyperparathyroidism and thyroid disease before attributing low density to primary osteoporosis; *what:* the metabolic pattern). **Serum protein electrophoresis** (*why:* myeloma presents with fractures, bone pain, anaemia, renal impairment and hypercalcaemia and is missed if not sought; *what:* paraprotein — cross-refer `TODO:link — J4 Paraproteins & lymphoproliferative (unbuilt)`). **Coeliac serology, testosterone in men, and cortisol assessment where indicated** (*why:* secondary causes, particularly in men and younger women; *what:* the underlying condition). **Lateral spine imaging** (*why:* detects the silent vertebral fractures that change risk category and treatment decisions; *what:* vertebral height loss).

#### Mx – Immediate — GER1 §0.6.1
Fracture management. **Analgesia adequate to allow mobilisation** — under-treated pain after a fragility fracture causes immobility, delirium and further decline.

#### Mx – Definitive — GER1 §0.6.2
Investigation for secondary causes, and commencement of appropriate pharmacotherapy alongside calcium, vitamin D and exercise.

#### Mx – Chronic/long-term — GER1 §0.6.3
**Adherence support — persistence with oral bisphosphonates is poor**, and intravenous or six-monthly options may suit better. Monitoring, dental review, and combined falls and bone health management. **Explicit handover to the GP with a named plan.**

### Pressure Injury — from unverified layer
`SRC:GER2_Geriatric_Syndromes_and_End_of_Life_Care §0.2` `UNVERIFIED — model knowledge, not source-checked.`

**A/P:** **Sustained pressure exceeding capillary closing pressure occludes perfusion**, causing tissue ischaemia. **Shear** (sliding down the bed, dragging rather than lifting during transfers) deforms and tears tissue at deeper levels, **friction** damages the epidermis, and **moisture** from incontinence or sweat macerates skin and lowers its tolerance.
**It is a function of pressure AND time** — high pressure for a short period, or modest pressure for a long one, both cause injury. **Deep tissue over a bony prominence dies before the skin does**, which is why a small area of discolouration can overlie extensive underlying necrosis.

> [!danger] Device-related pressure injuries are the ones that get missed
> **Oxygen tubing behind the ears, nasal prongs, CPAP and NIV mask edges, nasogastric tube tape, urinary catheters, plaster casts, splints, cervical collars, compression stockings, and pulse oximeter probes.**
> **These account for a substantial proportion of hospital-acquired pressure injuries and are entirely preventable** by inspecting under and around every device, padding, and rotating sites.
> **Look under the mask and behind the ears on every ward round in a patient on oxygen.**

> [!tip] Sites and the one that is forgotten
> Sacrum, ischial tuberosities, greater trochanters, **heels**, occiput, ears, elbows, and the malleoli.
> **Heels are the second commonest site and the most neglected. Offload them — a pillow lengthwise under the calves so the heels float free of the bed.** This costs nothing and prevents a wound that can take months to heal.

> [!warning] Staging, and the two categories people forget
> Staged from **non-blanchable erythema of intact skin** through partial-thickness loss, full-thickness loss with visible fat, to full-thickness loss with exposed bone, tendon or muscle.
> Plus two additional categories:
> **· Unstageable** — the base is obscured by slough or eschar, so depth cannot be determined until it is debrided.
> **· Deep tissue pressure injury** — persistent non-blanchable deep red, maroon or purple discolouration, or a blood-filled blister, over intact skin. **This can evolve rapidly to a full-thickness wound and looks deceptively minor.**
> `UNVERIFIED — the full staging definitions and terminology.`

> [!danger] Do not massage a reddened pressure area
> It was traditional advice and it is wrong — **massage over a bony prominence causes further tissue damage in already compromised tissue.** Offload, do not rub.

> [!tip] Prevention — what actually works
> **· Formal risk assessment on admission and with any change in condition** (Braden, Waterlow or equivalent).
> **· Repositioning at appropriate intervals**, and — more importantly — **mobilisation.**
> **· Pressure-redistributing mattresses and cushions** for at-risk patients.
> **· Skin inspection at least daily, including heels, sacrum and under every device.**
> **· Moisture management** — prompt continence care and barrier products.
> **· Nutrition and hydration** — see 0.3.
> **· Lift, do not drag** — using slide sheets and hoists to avoid shear.
> **A hospital-acquired pressure injury is a reportable clinical indicator in Australian hospitals**, and it is regarded as a marker of nursing and system quality precisely because it is largely preventable.

**S/Smx:** Non-blanching erythema, pain over a pressure point, blistering, skin loss, slough, eschar, exudate, odour, and surrounding cellulitis. **Pain over a bony prominence in an immobile patient warrants inspection**, and patients with sensory impairment may report nothing at all.

**Ix:** **Regular full skin inspection including under devices** (*why:* the diagnosis is entirely visual, and injuries are missed by not looking; *what:* stage, site, extent). Wound swab **only where clinical infection is suspected** (*why:* all chronic wounds are colonised, so routine swabbing produces misleading results and drives unnecessary antibiotics; *what:* organism in the context of clinical infection). FBC, CRP, albumin (*why:* systemic infection and the nutritional status that determines healing; *what:* infection markers, hypoalbuminaemia). **Probe-to-bone assessment and imaging where osteomyelitis is suspected** (*why:* underlying osteomyelitis changes the treatment duration and may require surgery, and it is common in deep sacral and heel wounds; *what:* bone involvement on MRI). Nutritional assessment (*why:* healing requires protein and energy, and malnourished wounds do not close; *what:* intake, weight, albumin). Vascular assessment for heel and lower limb wounds (*why:* an ischaemic limb will not heal, and compression is contraindicated; *what:* pulses, ABI — cross-refer [[01_Cardiovascular]] §0.36.1 Peripheral Arterial Disease (PAD)).

#### Mx – Immediate — GER2 §0.2.1
**Offload the area completely.** Analgesia — pressure injuries are painful and this is under-treated.

#### Mx – Definitive — GER2 §0.2.2
Stage-appropriate wound care with specialist wound nursing input, debridement of devitalised tissue where appropriate, management of infection, and optimisation of nutrition and perfusion.

#### Mx – Chronic/long-term — GER2 §0.2.3
Ongoing pressure redistribution, equipment provision for home or residential care, and **carer education**, since most pressure injuries develop outside hospital.




## Frailty

> [!note] Gap-filled from CSV ("Frailty phenotype / frailty assessment," High yield). Genuinely absent: the word appeared three times in the whole corpus, each time as a passing modifier on some other topic (an ECOG caveat in oncology, a relaxed HbA1c target in diabetes, a bladder-drug caution) — never as a concept with a definition, an assessment method, or management. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Part A "Frailty", the Australian Consensus Statement on the Prevention and Management of Frailty Among Community-Dwelling Older Adults (MJA, modified Delphi), and the AJGP review of sarcopenia in general practice, Aug 2026.

**D:** a state of **reduced physiological reserve across multiple organ systems**, producing disproportionate vulnerability to decompensation after a stressor that a non-frail person of the same age would absorb without consequence.

> [!info] The clinical signature, which is what makes frailty a useful concept rather than a synonym for "old": **the response is out of proportion to the insult.** The same urinary tract infection produces mild dysuria in a fit 80-year-old and, in a frail one, a fall, delirium, incontinence, immobility and an admission — with function often not returning to baseline afterwards. That non-linear response, and the incomplete recovery, is frailty. It is the reason a frail patient's presenting complaint is so often one of the geriatric syndromes (falls, delirium, immobility, incontinence) rather than the organ-specific symptom of the actual illness.

**Frailty is not the same as any of the things it is routinely confused with:**
- **Not age.** Many 90-year-olds are not frail; some 65-year-olds are.
- **Not multimorbidity.** They overlap and each raises the risk of the other, but a patient can carry several well-controlled chronic diseases with intact reserve, and a patient with few diagnoses can be profoundly frail.
- **Not disability.** Disability is established loss of function; frailty is the vulnerability that predicts *future* loss. A frail person may currently be fully independent — which is exactly when intervention has the most to offer.

### Assessment — two different models, used for different jobs

**1. The frailty phenotype (Fried) — a physical, criteria-based definition.** Five components:
1. Unintentional weight loss
2. Self-reported exhaustion
3. Low physical activity
4. Slow walking speed
5. Weak grip strength

**Three or more = frail; one or two = pre-frail; none = robust.** The *pre-frail* category is the practically important one — it identifies the patient in whom the trajectory is still readily modifiable.

**2. The Clinical Frailty Scale (Rockwood) — a judgement-based 9-point scale**, running from *very fit* through to *terminally ill*, and derived from the accumulated-deficits model, which counts deficits across physical, cognitive and psychosocial domains rather than physical criteria alone. Fast enough to apply at the bedside or on admission, which is why it is the one most often seen in hospital practice and in escalation and perioperative decisions.

Both are validated and both predict mortality; they are not interchangeable, and they answer different questions. The phenotype asks *"is this patient physically frail, and can I target the components?"*; the CFS asks *"how much reserve does this patient have, and what does that mean for the decision in front of me?"*

**Australian guidance is to assess frailty annually in older patients using a validated tool** — the specific tool matters less than doing it systematically rather than by impression.

**Sarcopenia** — the age-related loss of skeletal muscle mass, strength and function — is the muscle-specific core of physical frailty, and is what the exercise and protein interventions below are actually targeting.

### Why it changes management, not just prognosis

Frailty should alter clinical decisions rather than merely describe the patient:
- **Treatment targets loosen.** Tighter is not better in frailty — see the relaxed HbA1c targets in frail older patients in [[06_Metabolic_Medicine_and_Endocrinology]], and weigh the falls and postural-hypotension cost of intensive blood-pressure lowering against its benefit.
- **Fitness for intervention.** Frailty predicts postoperative complications and chemotherapy toxicity better than age or performance status alone — note the explicit acknowledgement in [[10_11a_Oncology_-_Common_Cancers__Carcinogens__Tumour_Markers]] ECOG Performance Status that ECOG is a broad functional snapshot rather than a frailty assessment.
- **Falls and fracture risk rise together** — see Falls in Older People above and [[11_08b_Ortho_-_Paget_s_Disease_and_Osteoporosis]] Osteoporosis.
- **Delirium risk rises sharply**, which is why reduced physiological reserve appears as the first half of the delirium equation in [[04_Neurology]] Delirium.
- **Goals of care conversations become timely**, not premature — see [[Communication]] Discussing "Do Not Attempt Cardiopulmonary Resuscitation" (DNACPR / Not-for-Resuscitation) for that conversation, and [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework for the capacity question that underlies it.

### Mx — the central message is that frailty is modifiable

> [!danger] **Frailty is not an inevitable consequence of ageing, and identifying it is not a reason for therapeutic nihilism.** Its main drivers — sarcopenia, undernutrition, physical inactivity, uncontrolled chronic disease and polypharmacy — are all modifiable, and pre-frailty in particular can be reversed. Recording "frail" and doing nothing is a clinical failure, not a diagnosis.

- **Immediate/acute:** in an acute presentation, expect an atypical one, hunt for the geriatric syndrome masking the illness, and avoid the iatrogenic harms that frail inpatients are most susceptible to — deconditioning from bed rest, delirium, pressure injury, and new medications.
- **Definitive — the interventions with evidence:**
  - **Exercise, progressive and individualised, combining resistance, aerobic, and balance/functional training**, tailored to frailty level and professionally supervised. **The resistance component is essential** and is the part most often left out when a patient is simply told to "stay active".
  - **Nutrition — an individualised, protein-rich diet**, with active identification and treatment of protein–energy malnutrition and specific deficiencies. Early dietitian involvement.
  - **Deprescribing** — see Polypharmacy and Deprescribing below.
  - **Optimise contributing chronic disease**, and correct sensory impairment (vision, hearing), which drives inactivity and social withdrawal.
  - **Early physiotherapist and dietitian involvement** is specifically recommended rather than reserved for failure of advice alone.
> [!danger] **Aboriginal and Torres Strait Islander people — frailty presents earlier, and the assessment age must move with it.** Age-related conditions occur at younger ages, and aged care eligibility begins at **50 rather than 65** — as it does for people who are homeless or at risk of homelessness, in whom frailty likewise presents early (see the equity boxes under Falls in Older People above, not repeated here). The practical consequence for this entry specifically: **do not use 65 as the trigger for frailty assessment**, and do not read a frailty phenotype or Clinical Frailty Scale score in a 55-year-old Aboriginal patient as implausible for their age. Applying an unadjusted age threshold is the mechanism by which this disparity is perpetuated in individual consultations.

- **Chronic/long-term:** **Comprehensive Geriatric Assessment** — the multidimensional, multidisciplinary assessment (medical, functional, cognitive, psychological, social, environmental) with a coordinated plan, which is the structure that ties together everything in this file. Address social isolation, arrange appropriate community supports, and reassess frailty status annually to track the trajectory rather than assuming it only goes one way.

---

### Comprehensive Geriatric Assessment — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.1` `UNVERIFIED — model knowledge, not source-checked.`

**D:** A **multidimensional, interdisciplinary** diagnostic process that identifies medical, psychological, functional and social capabilities and problems, in order to develop a coordinated plan for treatment and long-term follow-up.

> [!tip] The five domains
> **1. Medical** — comorbidities, medications, nutrition, continence, pain, sensory impairment, dentition.
> **2. Functional** — activities of daily living, mobility, gait and balance.
> **3. Cognitive and psychological** — cognition, mood, delirium, capacity.
> **4. Social** — living situation, carer, supports, finances, elder abuse risk.
> **5. Environmental** — home safety, access, equipment, transport.
> **CGA delivered in hospital increases the likelihood that a patient is alive and living in their own home afterwards.** It is one of the better-evidenced interventions in the specialty, and it is a process rather than a test.

> [!info] The physiology that makes older people different
> **Reduced homeostatic reserve** — every organ system has less capacity to buffer a stressor, so a small insult produces a large decompensation. This is why a urinary tract infection precipitates a fall, delirium and functional decline in one patient and nothing in another.
> **Altered pharmacokinetics and pharmacodynamics** — reduced renal clearance, reduced hepatic first-pass metabolism, **increased body fat and reduced total body water (so lipophilic drugs such as benzodiazepines accumulate and water-soluble drugs reach higher concentrations)**, reduced serum albumin, and **increased CNS sensitivity to sedatives, opioids and anticholinergics.**
> **Blunted physiological responses** — reduced fever response, reduced tachycardic response (compounded by beta-blockers), reduced thirst.

> [!danger] Illness presents atypically — and this is where diagnoses are missed
> **· Myocardial infarction without chest pain** — presenting as dyspnoea, confusion, a fall or simply "not right".
> **· Pneumonia without fever or cough** — presenting as delirium, tachypnoea or a fall.
> **· Sepsis with confusion and hypothermia rather than fever.**
> **· Hyperthyroidism as apathy, weight loss and atrial fibrillation** ("apathetic thyrotoxicosis") rather than agitation.
> **· Depression as physical complaints and cognitive impairment.**
> **· Abdominal catastrophe with minimal pain and a soft abdomen** — cross-refer [[03_Gastrointestinal]] §0.41.6 The Acute Abdomen in Special Groups.
> **The corollary: a non-specific presentation in an older person — a fall, confusion, reduced mobility, "off legs" — is a symptom requiring a diagnosis, not a diagnosis in itself.**

> [!tip] The "geriatric giants"
> **Immobility · Instability (falls) · Incontinence · Impaired cognition · Iatrogenesis.**
> These five presentations account for a large share of geriatric medicine, each is multifactorial, and each is a **final common pathway** for many underlying diseases rather than a diagnosis.

> [!warning] Collateral history is not optional
> The patient may not recall, may minimise, may have cognitive impairment, or may fear losing independence. **The family, carer, residential facility staff, GP and community pharmacist each hold part of the picture** — particularly regarding baseline function, medication adherence, and the timeline of decline.
> **Ask specifically: what could they do six months ago that they cannot do now?** That single question establishes both the baseline and the trajectory.

**S/Smx:** As above, elicited systematically across the five domains.

**Ix:** **Baseline bloods — FBC, UEC, LFT, calcium, TFTs, glucose, B12 and folate, vitamin D, CRP** (*why:* covers the correctable metabolic, endocrine and nutritional contributors to almost every geriatric presentation; *what:* anaemia, renal impairment, hypercalcaemia, thyroid disease, deficiency). Urinalysis interpreted cautiously (*why:* **asymptomatic bacteriuria is extremely common in older people and a positive urine does not diagnose the cause of a fall or delirium** — treating it while missing the real cause is a recurring error; *what:* infection in clinical context). ECG (*why:* silent ischaemia and arrhythmia; *what:* the trace). **Cognitive screening with a tool appropriate to language and education** (*why:* baseline and detection — cross-refer [[04_Neurology]] Dementias; *what:* impairment). **Functional assessment** (*why:* determines care needs and prognosis more than any diagnosis; *what:* ADL and IADL dependence). **Medication reconciliation** (*why:* see 0.4; *what:* the true list, including over-the-counter and complementary products). Postural blood pressure, vision, hearing, weight and nutritional screening (*why:* all are common, contributory and correctable; *what:* deficits).

#### Mx – Immediate — GER1 §0.1.1
Treat the acute problem, and simultaneously begin the functional and social assessment — **discharge planning starts on admission, not on the day of discharge.**

#### Mx – Definitive — GER1 §0.1.2
Interdisciplinary team management — medical, nursing, physiotherapy, occupational therapy, speech pathology, dietitian, pharmacist, social work.

#### Mx – Chronic/long-term — GER1 §0.1.3
Coordinated follow-up with the GP, community supports, and a documented plan. **Advance care planning** — cross-refer [[Clinical-Process-EBM-Consent-Capacity]] Right to refuse treatment.

### Frailty — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.2` `UNVERIFIED — model knowledge, not source-checked.`

**D:** A state of **increased vulnerability to stressors**, resulting from cumulative decline across multiple physiological systems, such that a minor insult produces a disproportionate and often lasting deterioration.

> [!tip] Frailty is not the same as age, comorbidity or disability
> They overlap but are distinct. **A 90-year-old may be robust; a 65-year-old with multiple conditions may be severely frail.**
> **Frailty predicts outcomes better than age or diagnosis**, which is why it has become central to decision-making about surgery, chemotherapy, intensive care, dialysis, anticoagulation and screening.

> [!info] The two models
> **Phenotype model (Fried)** — frailty as a syndrome defined by **unintentional weight loss, self-reported exhaustion, weakness (grip strength), slow gait speed, and low physical activity.** Meeting a threshold number of criteria defines frailty, with an intermediate "pre-frail" state.
> **Deficit accumulation model** — frailty as the proportion of accumulated deficits across many domains. Operationalised most usefully as the **Clinical Frailty Scale**, a nine-point judgement-based scale developed at **Dalhousie University**, running from very fit through to terminally ill.
> **The Clinical Frailty Scale is widely used in Australian hospitals**, including for intensive care triage and perioperative decision-making, and **it is scored on the patient's baseline two weeks before the acute illness, not on how they look in the bed today.** Scoring an acutely delirious pneumonia patient as severely frail because they cannot currently mobilise is a common and consequential error. `UNVERIFIED — the scale descriptors and scoring rules.`

> [!warning] Sarcopenia
> **Loss of skeletal muscle mass, strength and function** — the physical substrate of much of frailty.
> Driven by ageing, inactivity, inadequate protein intake, inflammation and illness. **Hospitalisation accelerates it dramatically — bed rest causes measurable muscle loss within days**, which is the argument for early mobilisation.
> **The intervention with the best evidence is resistance exercise combined with adequate protein intake.** Both are under-prescribed, and older people are frequently advised to rest when they should be moving.

> [!danger] Frailty is partly reversible — treat it as modifiable, not as a verdict
> **Interventions with evidence: resistance and balance exercise · adequate protein and energy intake · deprescribing · correction of vision and hearing · treatment of depression · social engagement · management of pain.**
> **Using a frailty score purely to withhold treatment is a misuse of the concept.** It is intended to individualise decisions and to identify people who need *more* support, not to ration by proxy. Where it does justify a different approach — avoiding a burdensome intervention unlikely to benefit — that should be an explicit shared decision, not an unspoken one.

**S/Smx:** Fatigue, weight loss, slow gait, weakness, reduced activity, falls, delirium with minor illness, and prolonged recovery from stressors.

**Ix:** **Clinical Frailty Scale or an equivalent, scored at baseline** (*why:* it predicts outcome and guides decisions across specialties; *what:* frailty grade). **Gait speed and grip strength** (*why:* simple, objective, and among the best single predictors of adverse outcomes; *what:* slow gait, weak grip). **Timed Up and Go** (*why:* combines strength, balance and gait in one repeatable measure; *what:* prolonged time). Nutritional screening and weight trajectory (*why:* malnutrition and sarcopenia are common and treatable; *what:* weight loss, poor intake). FBC, albumin, vitamin D, B12, TFTs (*why:* correctable contributors; *what:* anaemia, deficiency). Assessment for depression (*why:* it mimics and worsens frailty and is treatable; *what:* depressive symptoms).

#### Mx – Immediate — GER1 §0.2.1
Recognise it, and adjust the acute plan — lower thresholds for delirium prevention, earlier mobilisation, more cautious prescribing.

#### Mx – Definitive — GER1 §0.2.2
Multicomponent intervention: exercise, nutrition, deprescribing, sensory correction, treatment of contributing conditions.

#### Mx – Chronic/long-term — GER1 §0.2.3
Ongoing exercise programs, community supports, and **use of the frailty assessment to inform advance care planning and to guide goals-of-care conversations** — cross-refer [[18_Geriatrics_and_Older_Persons_Health]].

### Malnutrition and Nutrition — from unverified layer
`SRC:GER2_Geriatric_Syndromes_and_End_of_Life_Care §0.3` `UNVERIFIED — model knowledge, not source-checked.`

> [!danger] Malnutrition is common, consequential and under-diagnosed
> A large proportion of older hospital inpatients and residential care residents are malnourished or at risk, and **it is documented in a small fraction of them.**
> **Consequences: impaired wound healing, infection, sarcopenia and falls, delirium, longer length of stay, readmission, and increased mortality.**
> **Screen everyone** — a validated tool such as the Malnutrition Screening Tool takes a minute and asks essentially two things: **have you lost weight without trying, and have you been eating poorly?** `UNVERIFIED — the tools, thresholds and scoring.`

> [!tip] Why older people eat less — and most of it is fixable
> **· Poor dentition, ill-fitting dentures, and dentures left at home during admission.**
> **· Dysphagia** — cross-refer [[04_Neurology]] Speech, Voice and Swallowing.
> **· Reduced smell and taste** — cross-refer [[04_Neurology]] Smell and Taste.
> **· Medications** — nausea, dry mouth, altered taste, anorexia, and polypharmacy generally.
> **· Depression** — a leading and treatable cause of weight loss in older people.
> **· Dementia** — apraxia of feeding, distraction, forgetting to eat, refusal.
> **· Social** — isolation, bereavement, poverty, inability to shop or cook.
> **· Pain, constipation, and nausea.**

> [!danger] The hospital-specific barriers, which are our fault and are fixable
> **· Repeated nil by mouth orders for tests that are then delayed or cancelled.**
> **· Meals delivered and removed without anyone helping the patient eat.**
> **· Packaging that an older person with arthritis or weakness cannot open.**
> **· Poor positioning** — trying to eat lying flat or slumped.
> **· The tray placed out of reach.**
> **· Ward rounds and procedures during mealtimes.**
> **Protected mealtimes, mealtime assistance, red tray systems and simply opening the packaging are effective interventions**, and noticing that a patient's tray has gone back untouched is a genuinely useful thing to do on a ward round.

> [!warning] Refeeding syndrome
> In a patient who has had prolonged inadequate intake, **reintroduction of nutrition drives insulin release and a rapid intracellular shift of phosphate, potassium and magnesium**, with potentially fatal cardiac, respiratory and neurological consequences.
> **Identify at-risk patients before starting feeding, replace electrolytes, give thiamine, and reintroduce calories slowly with monitoring.** Cross-refer [[03_Gastrointestinal]] §0.41.20 Complications of Vomiting. `UNVERIFIED — risk criteria, electrolyte thresholds and the rate of caloric reintroduction.`

> [!danger] PEG feeding in advanced dementia does not achieve what people expect
> **The evidence indicates that gastrostomy feeding in advanced dementia does not prolong survival, does not prevent aspiration pneumonia, does not heal or prevent pressure injuries, and does not improve function or quality of life.**
> **Careful hand feeding, with attention to positioning, texture, food preferences, unhurried assistance and mouth care, is the recommended alternative** and is what families are frequently not offered as an option.
> This conversation is difficult because families experience "not feeding" as abandonment. **The framing that helps is that the goal is comfort and pleasure in eating rather than a nutritional target**, and that hand feeding continues rather than stopping. Cross-refer 0.5 and [[Clinical-Process-EBM-Consent-Capacity]] Right to refuse treatment.

> [!tip] Practical nutrition management
> **Food first** — fortified meals, high-energy high-protein options, frequent small meals, nourishing fluids. Then oral nutrition supplements. Then enteral feeding where appropriate to the goals of care.
> **Texture-modified diets and thickened fluids** are described using the **IDDSI framework** in Australian practice. Note that **thickened fluids reduce coughing but reduce fluid intake and are unpleasant**, so they are not universally beneficial and should be a considered decision with speech pathology rather than a reflex. `UNVERIFIED — the IDDSI levels and descriptors.`
> **Dietitian referral**, which is under-used.

**Ix:** **Weight and weight trajectory** (*why:* the single most useful nutritional measure, and weighing patients is routinely omitted; *what:* percentage weight loss over time). **Validated malnutrition screening tool** (*why:* identifies risk quickly and triggers dietitian referral; *what:* screening score). Albumin, interpreted with caution (*why:* it is a **negative acute phase reactant and reflects inflammation more than nutrition**, so a low albumin in an unwell patient does not by itself indicate malnutrition; *what:* level in context). **Phosphate, potassium, magnesium and thiamine status before and during refeeding** (*why:* refeeding syndrome; *what:* falling electrolytes). FBC, iron studies, B12, folate, vitamin D, zinc (*why:* specific deficiencies; *what:* deficiency). **Dental and oral examination** (*why:* an entirely mechanical and correctable cause; *what:* dentition, candidiasis, ulceration, denture fit). Swallow assessment (*why:* dysphagia; *what:* aspiration risk).

#### Mx – Immediate — GER2 §0.3.1
Ensure the patient can actually eat what is in front of them — position, assistance, packaging, dentures, and reversal of unnecessary fasting.

#### Mx – Definitive — GER2 §0.3.2
Dietitian-led nutrition plan, treatment of contributing causes, and speech pathology for dysphagia.

#### Mx – Chronic/long-term — GER2 §0.3.3
Meals services, shopping and cooking support, social eating, and **carer education.** Ongoing weight monitoring.




## Polypharmacy and Deprescribing

> [!note] Gap-filled from CSV ("Polypharmacy review / deprescribing in the elderly," High yield). Genuinely absent as content: polypharmacy appeared only as checklist bullets inside [[Communication]] Management of Patients with Multiple Chronic Medical Problems and [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls) — "review for sedating, anticholinergic, and hypotension-causing medications" — with no method for actually doing it, and no mention of Beers, STOPP/START, the prescribing cascade, or tapering anywhere in the corpus. Verified against the RACGP aged care clinical guide (Silver Book, 5th edition) Parts A "Polypharmacy" and "Deprescribing", and the *Deprescribing in Older People: A Clinical Practice Guideline* summary (MJA, 2026), Aug 2026.

**D:** **polypharmacy** is conventionally defined as the regular use of **five or more medicines**, though the number matters far less than whether each medicine still has a valid indication and a favourable benefit-to-harm balance for *this* patient now. **Deprescribing** is the planned, supervised withdrawal of a medicine that is no longer appropriate, done as a positive clinical act rather than as an omission.

> [!info] The framing that makes this a clinical skill rather than an administrative tidy-up: **deprescribing is part of the prescribing continuum, not the opposite of prescribing.** Most treatment guidelines say when to start a medicine and are silent on when to stop it, so medicines accumulate by default — each one started for a good reason at the time, none ever formally reviewed for whether that reason still holds. This is the 2026 Australian guideline's central point, and it explains why polypharmacy develops in patients whose every individual prescribing decision was defensible.

**Why it matters:** each additional medicine raises the risk of adverse drug events, drug–drug and drug–disease interactions, falls (see Falls in Older People above), delirium (see [[04_Neurology]] Delirium), cognitive impairment, non-adherence, and hospital admission. In an older person with reduced renal and hepatic clearance and reduced physiological reserve (see Frailty above), the dose–harm relationship is shifted relative to a younger patient on the same regimen.

> [!danger] **The prescribing cascade** — the single most important pattern to recognise, because it is invisible unless you look for it. An adverse effect of one drug is misinterpreted as a new medical condition, and a second drug is prescribed to treat it. Classic examples:
> - **Metoclopramide or an antipsychotic → drug-induced parkinsonism → levodopa** (see [[04_Neurology]] Parkinson's Disease (PD), where drug-induced parkinsonism is already noted as a differential).
> - **Calcium channel blocker → ankle oedema → a diuretic** (which then causes postural hypotension and falls).
> - **Anticholinergic → confusion or urinary retention → a cholinesterase inhibitor or a catheter.**
> - **NSAID → hypertension or dyspepsia → an antihypertensive or a PPI** (see [[03_Gastrointestinal]] Peptic Ulcer Disease).
>
> The diagnostic question that breaks the cascade: **"could this new symptom be a side effect of an existing medicine?"** — asked *before* reaching for a new prescription.

### Anticholinergic burden — specifically worth knowing in Australia

Anticholinergic effects are **cumulative across drugs**, so a patient can carry a substantial burden from several individually-innocuous medicines with no single obvious culprit. Contributors include bladder antimuscarinics, sedating antihistamines, tricyclic antidepressants, some antipsychotics, antispasmodics and antiemetics. The consequences in an older person are precisely the ones easily attributed to ageing or dementia instead: confusion, memory impairment, falls, constipation, urinary retention, dry mouth, blurred vision.

This is not a marginal issue in Australian practice — **roughly 20–34% of older Australians use at least one medicine with anticholinergic effects**, and these drugs remain widely prescribed despite being flagged as potentially inappropriate by both the criteria sets below.

### Tools for identifying potentially inappropriate medicines

- **Beers Criteria** (American Geriatrics Society) — a list of medicines generally to be avoided in older people, or avoided in specific conditions.
- **STOPP** (Screening Tool of Older People's Prescriptions) — medicines to consider stopping.
- **START** (Screening Tool to Alert to Right Treatment) — the complement, and the half that is routinely forgotten: **older people are also *under*-prescribed** medicines with clear benefit (osteoporosis treatment after a minimal-trauma fracture, anticoagulation in AF, statins where indicated). Deprescribing is about appropriateness in both directions, not simply about reducing the count.

**Australian services that exist to do this properly** and that an intern should know to arrange rather than attempt in a ward round: a **Home Medicines Review (HMR)** for community-dwelling patients and a **Residential Medication Management Review (RMMR)** for those in residential aged care — both accredited-pharmacist-conducted, both government-funded, and both underused.

### Mx — how to actually deprescribe

- **Immediate/acute:** on any admission, take a complete and accurate medication history including over-the-counter medicines, supplements and PRN use, and reconcile it against what the patient is actually taking. Admission is the highest-yield opportunity for review, and also the point at which unintended changes most often occur.
- **Definitive — a workable sequence:**
  1. **List every medicine with its indication.** A medicine whose indication nobody can state is the first candidate.
  2. **Assess benefit versus harm for this patient now** — including the *time to benefit*. A preventive medicine whose benefit accrues over 5–10 years offers little to a patient whose life expectancy is shorter than that, while its harms are immediate.
  3. **Establish the patient's own priorities** — symptom control and independence often matter more to them than a long-term risk-reduction target (see [[Communication]] Management of Patients with Multiple Chronic Medical Problems).
  4. **Prioritise** the medicines with the worst harm profile in older people: benzodiazepines and Z-drugs, anticholinergics, antipsychotics, opioids, and the fall-risk-increasing drugs listed under Falls in Older People above.
  5. **Stop one medicine at a time**, so that any benefit or deterioration is attributable.
  6. **Taper where withdrawal or rebound is a genuine risk** — benzodiazepines and Z-drugs, opioids, antidepressants, beta-blockers, corticosteroids, antipsychotics, and PPIs (rebound acid hypersecretion). Do **not** stop these abruptly. For benzodiazepines specifically, a workable approach is an initial reduction of around 20–25%, held for 2–4 weeks, then smaller reductions of roughly 5–12.5%, going slower if withdrawal symptoms emerge (see [[14_06a_Psych_-_Drugs_Used_in_Psychiatry]] Benzodiazepines).
  7. **Monitor and follow up** — document what was stopped and why, tell the patient what to expect and what would warrant restarting, and arrange review. Deprescribing without follow-up is not safer than not deprescribing.
- **Chronic/long-term:** schedule medication review as a recurring event rather than an incidental one, and record a stop date or review date at the time of *starting* any new medicine — the intervention that prevents the problem rather than correcting it later.

> [!tip] Deprescribing is a shared decision, and forced or abrupt withdrawal is both unsafe and counterproductive. The evidence on what makes it succeed is unglamorous: the patient's trust in the prescriber, a gradual taper, and an explicit agreement that a medicine can be restarted if stopping it turns out to be the wrong call. Framing matters — "let's see whether you still need this" is heard very differently from "I'm taking you off this."

---

### Polypharmacy and Deprescribing — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.4` `UNVERIFIED — model knowledge, not source-checked.`

**D:** **Polypharmacy** is commonly defined as the concurrent use of five or more regular medicines — but **the number matters less than the appropriateness.** A patient on eight medicines all clearly indicated is in a better position than one on four that are not.

> [!danger] The prescribing cascade
> **A drug side effect is mistaken for a new medical condition, and a second drug is prescribed to treat it.**
> **Recognisable examples:**
> **· Calcium channel blocker → ankle oedema → furosemide** (and then hyponatraemia and falls). Cross-refer [[01_Cardiovascular]] §0.36 Vascular Disease.
> **· Metoclopramide or prochlorperazine → drug-induced parkinsonism → levodopa.** Cross-refer [[04_Neurology]] Parkinsonism.
> **· Anticholinergic → dry mouth, constipation, urinary retention → laxatives and further drugs.**
> **· NSAID → hypertension → antihypertensive.**
> **· Cholinesterase inhibitor → urinary urgency → oxybutynin** (which then opposes the cholinesterase inhibitor and worsens cognition).
> **The question that breaks the cascade: "could this new symptom be caused by a medicine they are already taking?"** Ask it before every new prescription in an older person.

> [!warning] The high-risk classes in older people
> **· Benzodiazepines and Z-drugs** — falls, fractures, delirium, cognitive impairment, dependence. **Among the highest-yield deprescribing targets.**
> **· Anticholinergics** — see the box below.
> **· Antipsychotics** — increased stroke and mortality in dementia. Cross-refer [[04_Neurology]] Delirium–0.3.
> **· Opioids** — falls, constipation, delirium, respiratory depression.
> **· NSAIDs** — acute kidney injury, GI bleeding, heart failure, hypertension. **Rarely appropriate long-term in an older person.**
> **· Sulfonylureas** — hypoglycaemia, which in an older person causes falls, confusion and death.
> **· Digoxin** — narrow therapeutic index with reduced renal clearance.
> **· Proton pump inhibitors** — frequently continued indefinitely without indication. Cross-refer [[03_Gastrointestinal]] §0.28.1 Dyspepsia, Reflux and Heartburn.
> **· Tricyclics and first-generation antihistamines** — anticholinergic and sedating.

> [!danger] Anticholinergic burden is cumulative and is measured across the whole list
> **Many drugs have modest anticholinergic activity, and the effect is additive.** A patient on an antihistamine, an antidepressant, a bladder antimuscarinic and a tricyclic for pain may have a substantial total burden without any single "anticholinergic" drug.
> **Consequences: delirium, cognitive decline, falls, dry mouth and dental disease, constipation, urinary retention, blurred vision, and impaired heat regulation.**
> **Calculate or at least consider the total anticholinergic burden** rather than assessing drugs one at a time — cross-refer the existing corpus entry [[18_Geriatrics_and_Older_Persons_Health]] on anticholinergic burden.

> [!tip] Tools that structure the review
> **· STOPP/START criteria** — explicit lists of potentially inappropriate prescriptions (STOPP) and of indicated treatments that are being omitted (START). **The START half matters: under-prescribing is as real a problem as over-prescribing**, and older people are frequently denied anticoagulation, statins, osteoporosis treatment and analgesia on the basis of age alone.
> **· Beers criteria** — American, widely cited, useful with the caveat that some agents differ from Australian practice.
> **· Drug Burden Index** — quantifies cumulative anticholinergic and sedative exposure.
> `UNVERIFIED — the criteria themselves.`

> [!info] The Australian medication review services
> **· Home Medicines Review (HMR)** — a GP-initiated, Medicare-funded review conducted by an accredited pharmacist **in the patient's home**, which is where the actual medication practices are visible: the expired boxes, the duplicated brands, the doses not being taken.
> **· Residential Medication Management Review (RMMR)** — the equivalent for residential aged care.
> **These are under-utilised, and referring for one is a concrete, fundable action** you can recommend. `UNVERIFIED — current eligibility and referral requirements.`

> [!warning] How to deprescribe
> **1. Get an accurate list** — including over-the-counter, complementary and "as needed" medicines, and what they are **actually taking** rather than what is on the chart.
> **2. For each: what is the indication, is it still valid, is it working, and do the benefits still outweigh the harms given the patient's remaining life expectancy and goals?** A statin started for primary prevention at 60 may not serve an 88-year-old with limited life expectancy; the same statin after a myocardial infarction may.
> **3. Prioritise** — start with the highest-risk, lowest-benefit agents.
> **4. Taper where necessary** — **benzodiazepines, opioids, antidepressants, corticosteroids, beta-blockers, gabapentinoids and PPIs all have withdrawal or rebound effects**, and abrupt cessation causes harm and convinces the patient they need the drug.
> **5. Change one thing at a time, and monitor.**
> **6. Involve the patient and carer** — deprescribing without explanation feels like the withdrawal of care, and it fails.

> [!danger] Renal function is overestimated in older people
> **Creatinine is produced by muscle. An older person with low muscle mass can have a "normal" creatinine and substantially impaired renal function.**
> **eGFR equations are less reliable at the extremes of body habitus and age**, and many drug dose adjustments are based on creatinine clearance rather than eGFR.
> **The practical consequence: renally cleared drugs — including DOACs, metformin, gabapentinoids and many antibiotics — are routinely overdosed in frail older people with a normal-looking creatinine.**

**Ix:** **A complete medication reconciliation from multiple sources** (*why:* the hospital list, the GP list, the pharmacy dispensing record and what is actually in the patient's bag routinely disagree, and the discrepancies are where the harm sits; *what:* the true regimen). **UEC with eGFR, interpreted with the caveat above** (*why:* dose adjustment; *what:* renal function). Drug levels where relevant — digoxin, phenytoin, lithium (*why:* narrow therapeutic index with reduced clearance; *what:* toxicity). Postural blood pressure (*why:* identifies drug-induced orthostatic hypotension causing falls; *what:* postural drop). Cognitive and functional assessment (*why:* both are affected by drug burden and both improve with deprescribing; *what:* impairment). **Anticholinergic burden calculation** (*why:* the cumulative effect is invisible if drugs are assessed individually; *what:* total burden).

#### Mx – Immediate — GER1 §0.4.1
Withhold contributing drugs in an acute presentation — falls, delirium, hypotension, acute kidney injury.

#### Mx – Definitive — GER1 §0.4.2
Structured deprescribing as above, with a Home Medicines Review where appropriate.

#### Mx – Chronic/long-term — GER1 §0.4.3
**Document the deprescribing rationale clearly**, so the next clinician does not simply restart it — this is the commonest reason deprescribing fails. Communicate with the GP and community pharmacist. Use dose administration aids where adherence is the issue, and address cost, which is a genuine and under-asked barrier.


## Abuse of Older People (Elder Abuse) and Carer Stress

> [!note] Gap-filled from CSV ("Elder abuse / carer stress recognition," High yield). The only genuinely absent row in the whole Geriatrics category on a corpus-wide search — the sole related content was one carer-wellbeing bullet in [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls). Deliberately structured to mirror [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] Non-accidental injury (NAI) — risk factors, features suggestive of abuse, differential, then response — so the two safeguarding entries read the same way despite living in different files. Verified against the RACGP aged care clinical guide (Silver Book) Part B "Abuse of older people", the AIFS National Elder Abuse Prevalence Study, and the Aged Care Quality and Safety Commission's Serious Incident Response Scheme guidance, Aug 2026.

**D:** a single or repeated act, or lack of appropriate action, occurring within a relationship where there is an **expectation of trust**, which causes harm or distress to an older person. The trust relationship is the defining element — it is what distinguishes elder abuse from crime committed by a stranger, and it is also why disclosure is so difficult.

**The five recognised subtypes**, with Australian 12-month prevalence among community-dwelling people aged 65+ from the National Elder Abuse Prevalence Study (**15% experienced at least one subtype**):
- **Psychological/emotional (12%)** — by far the commonest, and the one least likely to be looked for: intimidation, humiliation, threats (including threats of residential care placement), social isolation, withholding contact with family.
- **Neglect (3%)** — failure to provide necessities of life: food, hygiene, medication, medical care, warmth, supervision. May be intentional or arise from carer incapacity.
- **Financial (2%)** — misuse of funds or assets, coercion over a will or power of attorney, unpaid "borrowing", pressure to transfer property. The subtype most often uncovered incidentally.
- **Physical (2%)** — including inappropriate use of restraint or over-sedation.
- **Sexual (1%)**.

**R:** older person factors — cognitive impairment (particularly dementia), functional dependence, social isolation, communication difficulty, and previous family violence. Perpetrator factors, which matter at least as much and are commonly the adult child rather than a paid carer — financial dependence on the older person, substance misuse, mental illness, and **carer stress with inadequate support**.

> [!warning] Features suggestive of abuse of an older person
> **From the history/interaction:** delayed presentation, or an explanation inconsistent with the injury; repeated presentations to different services; a carer who answers for the patient, refuses to leave the room, or is dismissive or hostile toward them; a patient who appears fearful, withdrawn or watchful in the carer's presence; the patient's own disclosure — which may be tentative, minimised, or later retracted.
> **Physical:** bruising in unusual sites or of varying ages, pressure injuries, poor hygiene, unexplained weight loss or dehydration, over- or under-medication, untreated injuries.
> **Financial:** unexplained inability to pay for care or medicines, sudden changes to a will or power of attorney, a relative with unusual control over finances, unpaid bills despite adequate income.
> **Service-related:** missed appointments, non-collection of prescriptions, refusal of services on the patient's behalf by someone else.

> [!note] Differential — none of the features above is specific, and each has innocent explanations that must be genuinely considered rather than dismissed: bruising from anticoagulants, thrombocytopenia or repeated falls (see Falls in Older People above); weight loss from malignancy, depression or dysphagia; pressure injury from immobility despite adequate care; confusion from delirium, dementia or polypharmacy (see [[04_Neurology]] Delirium vs Dementia vs Depression); and self-neglect, which is genuinely different from neglect by another and calls for a different response.

**Assessment:**
- **Interview the older person alone.** This is the single most important step and the one most often skipped. A carer's insistence on remaining present is itself a red flag; a neutral reason to separate them ("I always examine people privately") is usually enough.
- Ask directly but non-accusatorially — *"Does anyone at home make you feel afraid?"*, *"Is anyone taking or using your money without your permission?"*, *"Do you get the help you need with washing, dressing and meals?"*
- **Assess capacity** for the specific decisions in question (see [[Clinical-Process-EBM-Consent-Capacity]] Capacity assessment — the general framework), since it determines whether the person can decline intervention. **A person with capacity may choose to remain in an abusive situation**, and that choice must be respected while support and information are still offered — a genuinely difficult but legally clear point.
- Assess the **carer** as well: burden, mental health, substance use, and whether they have adequate support. Carer stress is a contributing factor to be addressed, not an excuse that discharges the concern.
- Examine and **document thoroughly and objectively** — describe and measure injuries, distinguish fact from opinion, and record the patient's own words verbatim, exactly as the NAI entry requires.

> [!danger] The Australian reporting position — and it is genuinely different from child abuse, which is where most people's intuition comes from
> **There is no general statutory mandatory reporting obligation for elder abuse in Australia.** This is a real and important contrast with mandatory reporting of child abuse (see [[15_24a_Paeds_-_Non-Accidental_Injury_and_Sexual_Abuse]] Sexual abuse for the SA mandatory-reporting duty that does apply to children). Assuming the same duty applies to older people is a common error in both directions — some clinicians report without consent believing they must, others do nothing believing that without a mandatory duty there is no pathway.
> - **Limited exception:** Commonwealth-funded aged care providers have specific reporting obligations under the *Aged Care Act 1997* (Cth), and the **Serious Incident Response Scheme (SIRS)** — in residential aged care since April 2021 and extended to in-home aged care services from December 2022 — requires providers to report serious incidents including abuse and neglect to the **Aged Care Quality and Safety Commission**. This is a *provider* obligation, not a treating-clinician one.
> - **Call the police** where there is a suspected crime or immediate danger.
> - **1800ELDERHelp (1800 353 374)** is the national number that redirects to the relevant state or territory service.
> - Other pathways: the **Office of the Public Advocate** and the relevant state tribunal (**SACAT** in South Australia) where guardianship or financial administration is in question — the same bodies already named in [[Clinical-Process-EBM-Consent-Capacity]] Consent to Medical Treatment and Palliative Care Act 1995 (SA) for capacity disputes.
> The national policy framework is the **National Plan to Respond to the Abuse of Older Australians**.

> [!info] **Two Australian-specific points.** First, **who counts as an "older person" is not 65 for everyone** — Aboriginal and Torres Strait Islander people, and people who are homeless or at risk of homelessness, are eligible for aged care from age 50, so an abuse concern in a 55-year-old from either group should be considered within this framework rather than dismissed on age (see Falls in Older People above). Second, and stated as a limitation rather than a finding: **reliable Australian prevalence data on abuse of older Aboriginal and Torres Strait Islander people specifically is limited**, and the National Elder Abuse Prevalence Study's community-dwelling sample should not be assumed to represent it. Do not extrapolate the subtype percentages above to this population — the honest position is that the data is thin, not that the rates are the same.

**Mx:**
- **Immediate/acute:** treat injuries and address any immediate safety risk. Admission is a legitimate tool where it is the only way to create a safe space while a plan is made.
- **Definitive:** raise the concern through the appropriate pathway above; involve social work early; separate the older person's needs from the carer's; and where the person has capacity and declines intervention, **keep the door open** — document the discussion, provide the contact numbers, treat what they will let you treat, and arrange follow-up. Disclosure often takes several contacts.
- **Chronic/long-term:** address the modifiable drivers — carer support and respite, home care packages via an **Aged Care Assessment Team (ACAT)** assessment, treatment of carer mental illness or substance misuse, and reducing the older person's social isolation. Reassess, because circumstances change and a refusal today is not a refusal forever.

---

## Discharge Planning and Home Safety Assessment

> [!note] Gap-filled from CSV ("Discharge planning / home safety assessment," High yield). Partially present before this: [[Communication]] Caring for the Elderly in the Community (Dementia, Mobility, Parkinson's, Recurrent Falls) carries home-environment and referral bullets within an OSCE communication framework, and [[15_01b_Paeds_-_Anaphylaxis]] Discharge planning covers a single-condition paediatric discharge — but the discharge *process* for an older inpatient existed nowhere. Verified against the Australian Commission on Safety and Quality in Health Care's Medication Management at Transitions of Care Stewardship Framework and medication reconciliation guidance, the NSW ACI Care of Confused Hospitalised Older Persons (CHOPs) transfer-of-care principles, and the RACGP aged care clinical guide (Silver Book, 5th edition), Aug 2026.

**Why this is a clinical task rather than an administrative one:** the transition out of hospital is a **recognised high-risk period**, and older people are particularly vulnerable to re-presentation after it. The failure modes are predictable and therefore preventable — the medication list is wrong, the GP does not know what happened, nobody checked whether the person can actually manage at home, and the follow-up that the plan depends on was never arranged.

> [!danger] **Discharge planning starts on admission, not on the day of discharge.** An older person's discharge destination and support needs should be an explicit question from day one, because the assessments and services it depends on — occupational therapy home visit, ACAT assessment, package activation, equipment supply — all take days to arrange. Beginning on the morning of discharge guarantees either a delayed discharge or an unsafe one.

### Functional readiness — the question that actually decides discharge

Medical stability is necessary but not sufficient. The operative question is whether this person can manage in **their** home, which requires knowing what that home is like and what they could do before:
- **Baseline versus current function.** Compare current ADLs (washing, dressing, toileting, transferring, feeding) and IADLs (shopping, cooking, finances, medications, transport) against their **premorbid** level, not against normal. A patient discharged at a function below their baseline without new support will fail.
- **Mobility and transfers**, assessed by physiotherapy — including stairs if there are stairs, and specifically whether they can get off a low chair and off the toilet.
- **Cognition**, which determines whether they can follow the plan at all (see [[04_Neurology]] Delirium vs Dementia vs Depression — and note that delirium frequently has *not* fully resolved at discharge, so the cognitive assessment made on admission may no longer apply).
- **Continence, nutrition and swallowing.**
- **Who is at home**, what they can realistically provide, and whether that arrangement is sustainable for them (see Abuse of Older People (Elder Abuse) and Carer Stress above — carer breakdown is both a discharge failure and a safeguarding risk).

### Home safety assessment

An **occupational therapist home visit** is the substantive version of this, and is more informative than any checklist completed in the ward, because it sees the actual environment. It covers access and entry (steps, rails), the bathroom (shower access, grab rails, toilet height), the kitchen, trip hazards and lighting, bed height and transfers, and the ability to summon help. It prescribes equipment and home modifications and — importantly — checks the person can use them. OT-led discharge planning of this kind is associated with reduced readmission.

Overlaps directly with falls prevention: the same assessment addresses both, so do not commission it twice (see Falls in Older People above).

### Medication reconciliation — the highest-yield single step

**Medication reconciliation should occur at every transition of care**, and the patient and carer should leave with an accurate, updated medication list they understand.

The scale of the problem is Australian and specific: **more than half of medication errors occur at transitions of care**, and **a patient with one or more medicines missing from their discharge information is around 2.3 times more likely to be readmitted** than one whose discharge information is correct. Practically, that means:
- Reconcile the discharge list against the pre-admission list, and account for every difference — stopped, started, or changed dose — with the reason.
- **Say what was deliberately stopped and why**, or the GP or a community pharmacist will helpfully restart it. This is the point at which good deprescribing work done during the admission is most often undone (see Polypharmacy and Deprescribing above).
- Consider a dose administration aid, and whether the person can physically open the packaging and read the label.

### Communication and follow-up

- **Discharge summary to the GP, promptly**, stating the diagnosis, what changed, what was stopped and why, what is outstanding, and what the GP is being asked to do and by when. A summary that arrives after the patient does is of limited use.
- **Explicit follow-up**: GP appointment, outpatient reviews, and who is responsible for chasing any pending results.
- **The patient and carer must understand the plan** — teach-back rather than a handed-over sheet, particularly where cognition is impaired.
- **Safety-netting**: what would warrant re-presentation, and who to call.

### Australian services worth knowing by name

- **Aged Care Assessment Team (ACAT)** — the assessment gateway to Commonwealth-funded aged care, including home care packages, residential care, and transition care. Refer early; it is a common cause of discharge delay.
- **Transition Care Programme** — time-limited therapy and support after a hospital stay for people who need longer to recover; requires the acute episode to be complete, medical stability, and ACAT assessment.
- **My Aged Care** as the entry point patients and families are directed to.
- **Home Medicines Review** for the medication side (see Polypharmacy and Deprescribing above).

> [!danger] **Discharge to a remote community is a different problem, not a harder version of the same one.** Where a patient is returning to a remote or very remote community, the standard plan can fail for reasons that have nothing to do with the medical assessment: the **medicines may not be locally available** and supply arrangements need confirming before discharge rather than after; **follow-up may be through an Aboriginal Community Controlled Health Organisation (ACCHO) or a visiting service** rather than a GP clinic, so the discharge summary must reach the right service; **transport home may take days** and may itself need arranging; and **equipment and home modifications** assume an environment and a supply chain that may not exist. Aboriginal and Torres Strait Islander people are also eligible for aged care assessment from age 50 (see Falls in Older People above), so the ACAT referral threshold is younger than the default.
>
> **Discharge to no fixed address is the other version of this problem**, and it fails for overlapping reasons: there is nowhere to deliver equipment or a home modification to, no address for follow-up correspondence, no safe storage for medicines, and often no phone number that will still work next week. People who are homeless or at risk of homelessness are **also eligible for aged care assessment from age 50** (see Falls in Older People above) — which is frequently the most useful referral available and is routinely not made, because the patient does not look like the person the service is imagined to be for. Involve social work early, and ask about housing explicitly rather than inferring it from the address on the chart, which may be historical. Ask **where the patient is going and who will actually see them**, early — this is the discharge planning that most often fails silently because everyone assumes someone else arranged it.

> [!tip] The commonest avoidable discharge failures, in the order they occur: planning started too late for the services to be arranged; discharge to a function level below baseline with no new support; a medication list that does not say what changed or why; and a follow-up plan that depends on an appointment nobody actually booked.

### Functional Assessment and the Australian Aged Care System — from unverified layer
`SRC:GER1_Comprehensive_Geriatric_Assessment §0.3` `UNVERIFIED — model knowledge, not source-checked.`
*Supersedes the former two-funding-pathways fragment; its eligibility marker is carried onto the NDIS line it belongs to.*

> [!tip] ADLs and IADLs — and why the distinction matters
> **Basic activities of daily living (ADLs)** — **D**ressing, **E**ating, **A**mbulating, **T**oileting, **H**ygiene.
> **Instrumental activities of daily living (IADLs)** — **S**hopping, **H**ousekeeping, **A**ccounting (managing money), **F**ood preparation, **T**ransport (and telephone, and medication management).
> **IADLs require more complex cognition and decline FIRST.** So **the earliest functional sign of cognitive decline is usually difficulty with finances, medications, transport or shopping — not with dressing or eating.**
> Ask about these specifically. "Are you managing at home?" gets a yes from almost everyone.

> [!warning] The Australian aged care pathway — and a caveat
> **`My Aged Care` is the single national entry point** — by phone or online — for assessment and services.
> Assessment has historically been through two streams: a **lower-intensity assessment** for basic entry-level supports, and a **comprehensive assessment (traditionally by an Aged Care Assessment Team, ACAT)** for higher-level home care packages, residential aged care and respite.
> **The system is currently mid-reform**, with the **Support at Home** program replacing previous home care arrangements, and assessment structures and program names changing accordingly.
> `UNVERIFIED — program names, assessment pathways, eligibility, funding levels and waiting times have all changed and continue to change. Verify against My Aged Care and the Department of Health and Aged Care before advising a patient or family. Do not quote package levels or waiting times from memory.`

> [!tip] Practical supports worth knowing exist
> **· Home support services** — domestic assistance, personal care, meals, transport, social support, allied health, home modifications, nursing.
> **· Home care packages** at graded levels of funding for more complex needs.
> **· Residential aged care** — permanent and respite.
> **· Transition care** after hospital, providing time-limited therapy and support to maximise recovery before a permanent decision is made — **valuable, and under-used, because it prevents premature placement decisions made from a hospital bed.**
> **· Carer supports** — Carer Payment and Carer Allowance through Centrelink, carer respite, and Carer Gateway.
> **· Continence support schemes** and equipment funding.
> **· For younger people with disability, the NDIS rather than aged care.**
> `UNVERIFIED — current eligibility criteria and the age boundary between NDIS and aged care, and what DVA covers; both are open government sources.`
> **· Veterans may access DVA-funded services**, which are separate and often quicker — **always ask about veteran status**, because it opens a different and frequently better-resourced pathway that families do not know about.

> [!danger] Do not make permanent placement decisions from an acute hospital bed
> **A patient assessed during or immediately after an acute illness will function far below their baseline**, and decisions made at that point systematically over-estimate the level of care needed.
> **Rehabilitation, transition care, and a period at home with supports should generally precede any permanent residential decision.** Families under pressure in a hospital corridor make decisions they later regret, and the hospital's need for the bed should not drive it.

> [!warning] Elder abuse — ask about it
> Physical, psychological, financial, sexual, and neglect. **Financial abuse is the commonest and the least recognised** — misuse of a power of attorney, pressure to transfer assets or sign documents, "inheritance impatience".
> **Warning signs: unexplained injuries, a carer who answers all questions and will not leave the room, unexplained financial difficulty, missed appointments, poor adherence, malnutrition, poor hygiene, fear or deference toward a family member.**
> **Speak to the person alone.** Cross-refer `TODO:link — GER4 Safeguarding & forensic (unbuilt; was P3 in build queue v1)`. `UNVERIFIED — reporting obligations for elder abuse in South Australia, and the relevant services and hotlines.`

**Ix:** **Structured ADL and IADL assessment** (*why:* determines care needs and is the basis of any aged care referral; *what:* dependence in each domain). **Occupational therapy home assessment** (*why:* function in a clinic bears limited relationship to function at home, and the home visit identifies hazards and equipment needs that no other assessment will; *what:* hazards, equipment, actual performance). Physiotherapy mobility assessment (*why:* determines aids, transfers and falls risk; *what:* gait, transfers, aid requirement). Cognitive assessment (*why:* determines capacity for self-care and for decision-making; *what:* impairment). **Social work assessment** (*why:* identifies carer strain, financial issues, housing and abuse; *what:* social supports and risks). Nutritional assessment (*why:* malnutrition is common and predicts poor outcome; *what:* weight loss, intake).

#### Mx – Immediate — GER1 §0.3.1
Ensure safety at discharge — supports in place before, not after, the patient goes home.

#### Mx – Definitive — GER1 §0.3.2
Referral to My Aged Care for assessment, with allied health input and equipment provision.

#### Mx – Chronic/long-term — GER1 §0.3.3
Review as needs change. **Support the carer explicitly — ask how they are, and offer respite before they are in crisis**, because carer breakdown is a leading reason for unplanned residential placement.


## Added from unverified layer — two things done on admission
`SRC:GER2_Geriatric_Syndromes_and_End_of_Life_Care §0.2` `SRC:GER2 §0.4` `UNVERIFIED — model knowledge, not source-checked.`

- **Pressure injury risk is scored, not eyeballed.** The **Waterlow** and **Braden** scales are the instruments in use; the staging and the repositioning regimen are covered elsewhere in this file, but neither happens unless someone scores the risk on admission and it drives a plan. `UNVERIFIED — which scale is used in your health network, and its action thresholds.`
- **Delirium prevention is a bundle, and it is more effective than treatment.** Reorientation, sleep protection, early mobilisation, hearing and visual aids in place, hydration, and avoiding precipitant drugs — delivered together, from admission, to every at-risk patient rather than started after delirium appears. See [[04_Neurology]] §Delirium for the syndrome itself, which this does not repeat. `UNVERIFIED — whether an Australian bundle is specified by name, and its components; NSW ACI or your health network.`

