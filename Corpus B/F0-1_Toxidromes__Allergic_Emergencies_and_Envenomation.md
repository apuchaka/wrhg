---
block: Toxicology & Envenomation
source: built in chat, model knowledge, NOT source-verified
trust: unverified
population: mixed
conflicts_open: 0
conflicts_r1: 0
---

> [!warning] Sourcing
> Written from model knowledge, not retrieved from guidelines. Mechanism, discriminators and investigation reasoning are reliable at intern level. **Every dose, threshold, reference range and timing figure carries an `UNVERIFIED` marker naming what to check, or has been omitted with the omission stated in place.** For this file specifically: all antidote dosing, all anaphylaxis adrenaline figures, and all antivenom vial numbers must come from the Australian Poisons Information Centre (13 11 26), eTG Toxicology and Toxinology, and ASCIA. A calcium channel blocker class fact was previously inverted in this corpus — 0.7 restates the selectivity explicitly for that reason.

---

## 0.1 Toxidrome Recognition — Framework

**D:** A toxidrome is a cluster of vital signs, pupil size, skin findings and mental state that identifies a class of poisoning before any drug level returns.

**A/P:** Agent binds its receptor class → predictable autonomic output → the pattern of pupils, skin, bowel sounds and temperature reveals the receptor class → class determines antidote and supportive priority, independent of which specific drug was taken.

**S/Smx:** The examination that discriminates is narrow and quick: pupil size, skin moisture, bowel sounds, temperature, reflexes and tone. Skin moisture and bowel sounds do most of the work.

> [!tip] Toxidrome comparison
> | | Pupils | Skin | Bowel sounds | Temp | Mental state | Distinctive |
> |---|---|---|---|---|---|---|
> | Anticholinergic | Dilated | **Dry, flushed** | **Absent** | Raised | Agitated delirium, mumbling | Urinary retention |
> | Cholinergic | Constricted | **Wet** | **Hyperactive** | Normal/low | Confused, then depressed | Bronchorrhoea, fasciculations |
> | Sympathomimetic | Dilated | **Wet** | Normal/increased | Raised | Agitated, alert | Normal reflexes, hypertension |
> | Opioid | **Pinpoint** | Normal | Reduced | Normal/low | Depressed | **Low respiratory rate** |
> | Sedative-hypnotic | Normal/small | Normal | Reduced | Normal/low | Depressed | Reflexes preserved early |
> | Serotonin toxicity | Dilated | Wet | Increased | Raised | Agitated | **Clonus, hyperreflexia, lower-limb predominant** |

> [!warning] The two pairs that get confused
> **Anticholinergic vs sympathomimetic** — both have dilated pupils, tachycardia, hyperthermia and agitation. The skin separates them: anticholinergic is **dry**, sympathomimetic is **soaked**. Bowel sounds confirm it — absent versus present.
> **Serotonin toxicity vs neuroleptic malignant syndrome** — see 0.4. Onset speed and the character of the tone abnormality separate them.

**Ix:** Bedside glucose (*why:* hypoglycaemia mimics every toxidrome and reverses in seconds; *what:* low value). ECG (*why:* the single highest-yield test in undifferentiated poisoning — QRS and QT tell you about sodium and potassium channel blockade regardless of the history given; *what:* QRS widening, QT prolongation, terminal R wave in aVR, arrhythmia). Paracetamol level in every deliberate self-poisoning (*why:* it is common, co-ingested, silent for the first day, and lethal if the treatable window is missed; *what:* level plotted against time since ingestion). VBG with lactate and electrolytes (*why:* identifies anion gap acidosis and gives potassium quickly; *what:* HAGMA, hyperlactataemia, potassium derangement). UEC, LFT, coagulation profile (*why:* baseline organ function and the derangements that direct antidote decisions; *what:* renal impairment, transaminitis, coagulopathy). Osmolality where toxic alcohol is plausible (*why:* the osmolar gap is elevated early when the anion gap is still normal; *what:* raised gap — see 0.8).

### 0.1.1 Mx – Immediate
Resuscitation before identification. A–E, oxygen, IV access, bedside glucose, continuous cardiac monitoring. **Call the Poisons Information Centre on 13 11 26** — this is the expected step in Australian practice, not a fallback, and it is the correct answer in both the exam and the resus bay.

### 0.1.2 Mx – Definitive
Decontamination, antidote and enhanced elimination decisions are agent-specific and time-dependent. `UNVERIFIED — activated charcoal indications, the time window in which it retains benefit, and all contraindications require verification against eTG Toxicology; no window is stated here.`

### 0.1.3 Mx – Chronic/long-term
Every deliberate self-poisoning requires mental health assessment before discharge, regardless of how medically trivial the ingestion proved to be. Cross-refer `TODO:link — N1 Risk assessment & suicidality (unbuilt)` Risk Assessment & Suicidality.

---

## 0.2 Anticholinergic Toxidrome

**D:** Poisoning by muscarinic receptor antagonism, producing central delirium with peripheral parasympathetic blockade.

**R/Causes:** Tricyclic antidepressants, sedating antihistamines (promethazine, diphenhydramine), antipsychotics, benztropine, oxybutynin, atropine, *Datura* and other plant alkaloids. Cumulative anticholinergic burden in the elderly on polypharmacy — cross-refer [[18_Geriatrics_and_Older_Persons_Health]] Anticholinergic burden.

**A/P:** Muscarinic blockade peripherally → loss of sweating, pupillary constriction, gut motility and bladder emptying → dry flushed skin, mydriasis, ileus, retention; loss of sweating removes the main heat-loss route → hyperthermia. Central muscarinic blockade → agitated delirium with visual hallucinations and characteristic mumbling incoherent speech.

**S/Smx:** Hot, dry, flushed skin. Dilated poorly reactive pupils. Absent bowel sounds, palpable bladder. Agitated delirium, picking at bedclothes, visual hallucinations of small figures or insects, mumbling speech. Tachycardia.

> [!tip] The classical mnemonic
> Blind as a bat (mydriasis, blurred vision) · Dry as a bone (anhidrosis) · Red as a beet (flushing) · Hot as a hare (hyperthermia) · Mad as a hatter (delirium) · Full as a flask (urinary retention).

> [!danger] The real risk is the co-ingestant, not the anticholinergic effect
> Tricyclic antidepressants produce this picture and also block fast sodium channels — the death is from QRS widening, seizures and arrhythmia, not from the dry skin. Any anticholinergic presentation demands an ECG looking specifically for QRS widening and a terminal R wave in aVR. Cross-refer [[A5_Toxicology_II_-_Poisoned_Patient__ADRs_and_Immunotherapy]] TCA Overdose.

**Ix:** ECG (*why:* separates a benign antihistamine ingestion from a sodium-channel-blocking TCA, which is the entire prognostic question; *what:* QRS widening, terminal R wave in aVR, QT prolongation). Bedside glucose and core temperature (*why:* hyperthermia here is a failure of heat dissipation and rises without warning; *what:* core temperature trend). Bladder scan (*why:* retention is uncomfortable, causes further agitation, and is easily missed in a delirious patient; *what:* retained volume). Paracetamol level (*why:* combination analgesic and cold-and-flu preparations pair antihistamines with paracetamol; *what:* level against time). CK where prolonged agitation or restraint (*why:* rhabdomyolysis follows sustained agitation; *what:* elevation).

### 0.2.1 Mx – Immediate
Supportive care is the treatment. Cooling for hyperthermia, benzodiazepines for agitation, IV fluids, catheterisation for retention. **Avoid physical restraint where possible** — it worsens hyperthermia and rhabdomyolysis. Continuous cardiac monitoring.

### 0.2.2 Mx – Definitive
Sodium bicarbonate is the intervention for QRS widening in sodium channel blockade, not for the anticholinergic features. `UNVERIFIED — the QRS threshold at which bicarbonate is indicated, and its dosing, require verification against eTG Toxicology and the Poisons Information Centre.` Physostigmine has a narrow and contested role and is not an intern decision.

### 0.2.3 Mx – Chronic/long-term
Medication review and deprescribing where the cause was cumulative burden. Mental health assessment where deliberate.

---

## 0.3 Cholinergic Toxidrome (Organophosphates)

**D:** Acetylcholinesterase inhibition producing acetylcholine excess at muscarinic, nicotinic and central receptors.

**R/Causes:** Organophosphate and carbamate insecticides — agricultural and domestic exposure, deliberate ingestion. Nerve agents. Some mushrooms.

**A/P:** Cholinesterase inhibited → acetylcholine accumulates at the synapse → muscarinic overstimulation gives secretions, bronchoconstriction, bradycardia and gut hyperactivity; nicotinic overstimulation gives fasciculations, weakness and ultimately paralysis; central overstimulation gives confusion, seizures and respiratory depression. Organophosphates then undergo "ageing" — an irreversible covalent change to the enzyme after which pralidoxime cannot reactivate it, which is why antidote timing matters.

**S/Smx:** Wet everywhere. Miosis, salivation, lacrimation, sweating, vomiting, diarrhoea, bronchorrhoea, bronchospasm, bradycardia, fasciculations, weakness. A garlic or solvent odour may be present.

> [!tip] Two mnemonics, and which one matters
> **DUMBELS** — Diarrhoea, Urination, Miosis, Bronchorrhoea/Bronchospasm/Bradycardia, Emesis, Lacrimation, Salivation.
> **The killer B's — bronchorrhoea, bronchospasm, bradycardia.** These are what kill. The patient drowns in their own secretions. Everything else on the list is uncomfortable rather than lethal.

> [!danger] Staff contamination
> Organophosphates are absorbed through skin and through vomit and clothing. **Decontaminate before, or while, treating** — remove clothing, wash the patient, and use appropriate PPE. Secondary contamination of the resus team is a described and preventable event.

**Ix:** The diagnosis is clinical and treatment must not wait for confirmatory tests. Red cell or plasma cholinesterase activity (*why:* confirms exposure and gives some prognostic information, but turnaround is far too slow to guide management; *what:* depressed activity). ABG or VBG (*why:* quantifies the ventilatory failure that bronchorrhoea and weakness produce; *what:* hypoxia, rising CO₂). ECG (*why:* bradyarrhythmia and QT prolongation occur; *what:* bradycardia, prolonged QT). UEC and glucose (*why:* baseline and hypoglycaemia exclusion; *what:* electrolyte derangement). CXR (*why:* aspiration and pulmonary oedema from secretions; *what:* infiltrates).

### 0.3.1 Mx – Immediate
Decontamination with PPE. Airway management with aggressive suctioning — secretions, not hypoxia from lung disease, are the primary airway problem. Atropine is the muscarinic antidote and is titrated to **drying of bronchial secretions**, not to heart rate or pupil size. `UNVERIFIED — atropine initial dose, doubling regimen and titration endpoint require verification against eTG Toxicology and the Poisons Information Centre; the doses used are far larger than in any other indication and must not be estimated.`

### 0.3.2 Mx – Definitive
Pralidoxime reactivates cholinesterase and addresses the nicotinic features that atropine does not touch, but only before ageing. `UNVERIFIED — pralidoxime dosing and the time window before ageing require verification.` Benzodiazepines for seizures. Intubation and ventilation for the intermediate syndrome — delayed proximal and respiratory muscle weakness developing after the acute cholinergic phase resolves, which catches teams who have relaxed.

### 0.3.3 Mx – Chronic/long-term
Prolonged ICU stay is common. Delayed peripheral neuropathy is described. Occupational exposure requires workplace notification — cross-refer `TODO:link — P1 Preventive & occupational health (unbuilt)` Occupational Exposure.

---

## 0.4 Sympathomimetic Toxidrome vs Serotonin Toxicity

**D:** Two hyperadrenergic hyperthermic states with overlapping presentations and different mechanisms — catecholamine excess versus excess serotonergic neurotransmission.

**R/Causes:**
*Sympathomimetic:* Amphetamines, methamphetamine, cocaine, MDMA, synthetic cathinones, salbutamol and theophylline in overdose.
*Serotonin toxicity:* Almost always a combination — SSRI or SNRI plus tramadol, MAOI, linezolid, triptan, St John's wort, MDMA, or an SSRI dose increase.

**A/P:**
*Sympathomimetic:* Increased synaptic catecholamine → α and β stimulation → vasoconstriction, tachycardia, hypertension, mydriasis, diaphoresis, agitation; sustained agitation and vasoconstriction → hyperthermia, rhabdomyolysis, and in cocaine specifically coronary vasospasm and aortic dissection.
*Serotonin toxicity:* Excess 5-HT2A stimulation → autonomic instability plus a distinctive neuromuscular excitation — **clonus and hyperreflexia, greater in the legs than the arms** — with hyperthermia driven by muscular activity.

**S/Smx:** Both give agitation, mydriasis, diaphoresis, tachycardia, hypertension and hyperthermia. The neuromuscular examination separates them.

> [!tip] Serotonin toxicity vs NMS vs sympathomimetic
> | | Onset | Tone | Reflexes | Pupils | Discriminator |
> |---|---|---|---|---|---|
> | Serotonin toxicity | Hours | Rigidity, **lower limbs > upper** | **Hyperreflexia, clonus** | Dilated | Inducible or spontaneous clonus |
> | NMS | Days to weeks | **Lead-pipe rigidity, generalised** | Reduced or normal | Normal | Slow onset after antipsychotic |
> | Sympathomimetic | Minutes to hours | Normal | Normal | Dilated | Normal reflexes, clear drug history |

> [!warning] Ask about the combination, not the drug
> Serotonin toxicity is a drug–drug interaction far more often than a single-agent overdose. Tramadol added to an SSRI is the classic Australian ward and GP scenario. A patient on a stable SSRI who has just been started on something new is the history to elicit.

**Ix:** Core temperature (*why:* hyperthermia is the proximate cause of death in both and determines the aggressiveness of cooling; *what:* trend, with severe elevation demanding active cooling and paralysis). CK (*why:* rhabdomyolysis from sustained muscular hyperactivity causes the renal failure that follows; *what:* marked elevation). UEC and potassium (*why:* rhabdomyolysis produces hyperkalaemia and acute kidney injury; *what:* rising creatinine, hyperkalaemia). ECG and troponin where cocaine is involved (*why:* cocaine causes coronary vasospasm and infarction in young patients with normal arteries; *what:* ischaemic change, troponin rise). Coagulation profile (*why:* DIC complicates severe hyperthermia; *what:* deranged INR, low fibrinogen). CT brain where headache, focal deficit or sustained severe hypertension (*why:* sympathomimetics cause intracranial haemorrhage; *what:* bleed).

### 0.4.1 Mx – Immediate
**Benzodiazepines are the first-line treatment for both**, addressing agitation, hypertension, tachycardia and muscular hyperactivity in one intervention. Active cooling for hyperthermia. IV fluids. Continuous monitoring. `UNVERIFIED — benzodiazepine dosing and the core temperature threshold defining severe hyperthermia require verification against eTG.`

> [!danger] Two agent-specific traps
> **Avoid beta-blockers in cocaine toxicity** — unopposed alpha stimulation may worsen hypertension and coronary vasospasm. **Avoid antipsychotics for agitation in either syndrome** — they lower the seizure threshold, impair heat dissipation, and in serotonin toxicity may worsen the picture. Benzodiazepines, not droperidol, are the answer here.

### 0.4.2 Mx – Definitive
Cease all serotonergic agents. Severe serotonin toxicity with hyperthermia requires intubation, paralysis and cooling — muscular activity is generating the heat, so paralysis stops it. Cyproheptadine has a role. `UNVERIFIED — cyproheptadine dosing and route require verification.`

### 0.4.3 Mx – Chronic/long-term
Medication reconciliation with explicit documentation of the interacting pair. Drug and alcohol referral where recreational. Mental health assessment where deliberate.

---

## 0.5 Opioid-Induced Respiratory Depression

**D:** Reduced respiratory drive from mu opioid receptor agonism, whether iatrogenic, recreational or deliberate.

**R:**
*Unmodifiable:* Age, renal impairment altering clearance, obstructive sleep apnoea.
*Modifiable:* Dose escalation, opioid-naive status, co-prescribed benzodiazepines or gabapentinoids, recent abstinence with lost tolerance (post-release from custody, post-detoxification), switching between opioid formulations without correct equianalgesic conversion.

**A/P:** Mu receptor agonism in the brainstem respiratory centres → reduced CO₂ chemosensitivity → falling respiratory rate rather than falling tidal volume → hypercapnia → CO₂ narcosis deepens sedation → further hypoventilation → hypoxia → arrest.

**S/Smx:** Pinpoint pupils, low respiratory rate, sedation. **Respiratory rate is the observation that matters — sedation score falls before saturation does, and saturation on supplemental oxygen can remain normal in a patient with a dangerously high CO₂.**

> [!danger] Oxygen masks this
> A patient on supplemental oxygen with an oximeter reading in the nineties can be profoundly hypercapnic and about to arrest. Monitor **sedation score and respiratory rate**, not saturation alone. This is the single most common serious ward prescribing harm involving opioids.

> [!warning] Naloxone has a shorter half-life than most opioids
> Re-sedation after an initial good response is expected, particularly with long-acting or slow-release preparations and with methadone. A patient who wakes with naloxone still requires prolonged observation and often an infusion. Naloxone also precipitates acute withdrawal and uncontrolled pain — titrate to adequate respiration, not to full alertness.

**Ix:** VBG or ABG (*why:* the definitive test — quantifies CO₂ retention, which oximetry cannot detect; *what:* raised pCO₂ with respiratory acidosis). Bedside glucose (*why:* reversible mimic; *what:* hypoglycaemia). Medication chart and community dispensing history (*why:* identifies cumulative dose, slow-release preparations that will outlast naloxone, and co-prescribed sedatives; *what:* total opioid load, formulation, timing). Paracetamol level where a combination preparation is possible (*why:* codeine and oxycodone are commonly co-formulated with paracetamol; *what:* level against time). CXR (*why:* aspiration and non-cardiogenic pulmonary oedema both follow; *what:* infiltrates).

### 0.5.1 Mx – Immediate
Airway positioning, oxygen and bag-mask ventilation if inadequate — **ventilate first, naloxone second.** Naloxone titrated in small increments to restore adequate respiration. `UNVERIFIED — naloxone dose, route, titration increment and infusion rate require verification against eTG and local policy; the dose appropriate for an opioid-dependent patient differs from that for an opioid-naive post-operative patient and neither is stated here.`

### 0.5.2 Mx – Definitive
Prolonged observation, and infusion where a long-acting agent was involved. Review and reduce the prescribed regimen. Cross-refer [[F0-4_Resuscitation_Algorithms_and_Emergency_Procedures]] Adult analgesia.

### 0.5.3 Mx – Chronic/long-term
Take-home naloxone provision and training for the patient and their household where dependence is present. Drug and alcohol referral. Opioid stewardship review where iatrogenic.

---

## 0.6 Paracetamol Overdose

**D:** Hepatotoxicity from saturation of normal paracetamol conjugation pathways and depletion of hepatic glutathione.

**R/Causes:** Deliberate self-poisoning; staggered supratherapeutic ingestion for pain; therapeutic-dose toxicity in the malnourished, chronic alcohol-dependent, or very low body weight. Combination cold-and-flu and analgesic preparations cause unintentional double-dosing.

**A/P:** Therapeutic doses are conjugated to glucuronide and sulfate → in overdose these pathways saturate → more paracetamol is shunted through CYP2E1 to NAPQI → NAPQI is normally detoxified by glutathione → glutathione is depleted → free NAPQI binds hepatocyte proteins → centrilobular necrosis → transaminitis at 24–48 hours, coagulopathy and encephalopathy at 72–96 hours. N-acetylcysteine works by replenishing glutathione, which is why it must be given **before** the injury occurs.

**S/Smx:** **Asymptomatic or trivially nauseated in the first day — this is the trap.** RUQ pain and vomiting at 24–48 h. Jaundice, coagulopathy, encephalopathy, hypoglycaemia and acute kidney injury from 72 h. A patient who looks well tells you nothing.

> [!danger] The window closes silently
> N-acetylcysteine is highly effective when given early and progressively less so as time passes. **Take a level in every deliberate self-poisoning regardless of the stated ingestion history**, because co-ingestion is common and the history is unreliable. The number of preventable deaths from this poisoning is entirely a function of missed early presentations.

> [!info] The treatment nomogram
> Treatment is decided by plotting the serum level against time since ingestion on a treatment nomogram, with separate handling for staggered ingestions, unknown time of ingestion, and modified-release preparations — for which the standard nomogram does not apply. `UNVERIFIED — the nomogram treatment line, the earliest time at which a level is interpretable, the modified-release protocol and all NAC dosing require verification against the current Australian and New Zealand consensus guideline for paracetamol poisoning and the Poisons Information Centre. No figures are stated here; this is the highest-consequence category of number in this file.`

**Ix:** Serum paracetamol level timed from ingestion (*why:* the single determinant of whether antidote is required, and it is uninterpretable before a defined post-ingestion interval; *what:* level plotted on the nomogram). LFT with ALT (*why:* ALT is the earliest marker of established hepatocyte injury and its trajectory determines whether NAC continues beyond the standard course; *what:* rising ALT). INR (*why:* the most useful prognostic marker in established toxicity, more so than transaminases; *what:* rising INR). UEC and creatinine (*why:* acute kidney injury occurs independently of and sometimes without liver failure; *what:* rising creatinine). VBG with lactate (*why:* metabolic acidosis and hyperlactataemia are poor prognostic markers and feature in transplant criteria; *what:* acidosis, raised lactate). Bedside glucose (*why:* hypoglycaemia signals severe hepatic failure and is easily missed; *what:* low glucose). Salicylate level and ECG (*why:* co-ingestion is common in deliberate poisoning; *what:* salicylate level, QRS and QT).

### 0.6.1 Mx – Immediate
Assess time and quantity of ingestion, whether staggered, and the preparation. Take a paracetamol level at the appropriate interval. Activated charcoal has a role in early presentation. `UNVERIFIED — charcoal timing window and dose require verification.` **Do not wait for the level before starting NAC in a late, massive, or staggered presentation** — start and stop later if the level does not support it.

### 0.6.2 Mx – Definitive
N-acetylcysteine per protocol, with the course extended if ALT is rising or the level remains detectable at the end. Anaphylactoid reactions to NAC are common, usually rate-related, and are managed by slowing the infusion rather than abandoning the antidote. Discuss with a liver transplant unit where INR, lactate, pH or encephalopathy meet escalation criteria. `UNVERIFIED — transplant referral criteria require verification.`

### 0.6.3 Mx – Chronic/long-term
Mental health assessment before discharge in every deliberate case. Cross-refer `TODO:link — N1 Risk assessment & suicidality (unbuilt)` Risk Assessment & Suicidality.

---

## 0.7 Beta-Blocker and Calcium Channel Blocker Overdose

**D:** Cardiogenic shock from blockade of beta-adrenergic receptors or L-type calcium channels, characteristically resistant to conventional vasopressor support.

**R/Causes:** Deliberate ingestion; accidental paediatric ingestion, where a small number of tablets of a slow-release preparation can be lethal to a toddler.

**A/P:**
*Beta-blocker:* β1 blockade → reduced cAMP → reduced intracellular calcium → negative inotropy and chronotropy → bradycardia and hypotension. Propranolol additionally blocks fast sodium channels, adding QRS widening and seizures, and is lipophilic enough to cause direct CNS depression.
*Calcium channel blocker:* L-type channel blockade → reduced calcium entry into myocardium and vascular smooth muscle → negative inotropy and vasodilatation. Pancreatic islet L-type channel blockade also impairs insulin release → hyperglycaemia.

> [!info] Calcium channel blocker selectivity — stated explicitly
> **Dihydropyridines** (amlodipine, nifedipine, felodipine) are **vascular-selective** — they cause vasodilatation and, at therapeutic doses, reflex tachycardia. They are not primarily rate-controlling agents.
> **Non-dihydropyridines** (verapamil, diltiazem) are **cardiac-selective** — negatively inotropic and chronotropic, causing bradycardia. These are the rate-control agents.
> **In significant overdose this selectivity is lost**, and a dihydropyridine can produce bradycardia and profound myocardial depression. `UNVERIFIED — this class fact was previously recorded inverted in this corpus; confirm the selectivity direction against the Australian Medicines Handbook before relying on it.`

> [!tip] The bedside discriminator
> **Hyperglycaemia points to calcium channel blocker.** CCBs block pancreatic insulin release, so glucose rises. Beta-blockers tend toward normal or low glucose, and propranolol may cause frank hypoglycaemia. Both give bradycardia and hypotension; the glucose separates them.

> [!danger] Slow-release preparations
> Onset can be delayed by many hours, so an initially well patient is not reassuring. A paediatric exploratory ingestion of a slow-release calcium channel blocker requires admission and prolonged observation regardless of how well the child appears. `UNVERIFIED — observation duration requires verification with the Poisons Information Centre.`

**S/Smx:** Bradycardia, hypotension, reduced conscious state. Preserved mental state despite marked hypotension is described in CCB toxicity early. Seizures and QRS widening suggest propranolol. Pulmonary oedema occurs with CCBs.

**Ix:** ECG and continuous monitoring (*why:* identifies the degree of conduction block and distinguishes propranolol's sodium channel effect; *what:* bradycardia, AV block, QRS widening). Bedside and serial glucose (*why:* the discriminator above, and glucose must be tracked closely once high-dose insulin therapy begins; *what:* hyperglycaemia in CCB, hypoglycaemia in propranolol). VBG with lactate (*why:* quantifies the perfusion deficit and tracks response to therapy; *what:* rising lactate, acidosis). UEC with potassium and calcium (*why:* high-dose insulin therapy drives potassium down and calcium is given therapeutically; *what:* baseline and serial potassium). Bedside echocardiography (*why:* distinguishes a vasodilated state from a failing pump, which changes whether vasopressor or inotrope is prioritised; *what:* contractility, filling).

### 0.7.1 Mx – Immediate
A–E, IV access, continuous monitoring, early ICU and Poisons Information Centre involvement — this is a poisoning where standard resuscitation frequently fails and early escalation is the intervention that changes outcome. Atropine, calcium, fluids and vasopressors are all used, with **high-dose insulin euglycaemic therapy** as a central intervention in significant toxicity. `UNVERIFIED — atropine, calcium, glucagon, vasopressor and high-dose insulin dosing and titration are all omitted here and must come from the Poisons Information Centre and eTG. High-dose insulin regimens use doses far above diabetic practice and must never be estimated.`

### 0.7.2 Mx – Definitive
Escalation to lipid emulsion, pacing, or extracorporeal support in refractory cases — ICU decisions. Whole bowel irrigation is considered for slow-release preparations. `UNVERIFIED — indications and technique require verification.`

### 0.7.3 Mx – Chronic/long-term
Mental health assessment. Where paediatric and exploratory, medication storage counselling and safeguarding consideration — cross-refer `TODO:link — P3 Safeguarding & forensic (unbuilt)` Neglect Concern.

---

## 0.8 Toxic Alcohols — Methanol and Ethylene Glycol

**D:** Poisoning by alcohols whose metabolites, rather than the parent compound, cause organ-specific injury and severe metabolic acidosis.

**R/Causes:** Deliberate ingestion; substitution when ethanol is unavailable; accidental ingestion of automotive coolant (ethylene glycol, sweet-tasting) or industrial solvents, screen wash and illicitly distilled spirits (methanol).

**A/P:** Parent alcohol is itself relatively inert and causes intoxication → alcohol dehydrogenase metabolises it → **methanol → formaldehyde → formic acid**, which is directly toxic to the retina and optic nerve; **ethylene glycol → glycolic acid → oxalic acid**, which chelates calcium and precipitates as calcium oxalate in the renal tubules. Accumulating acid metabolites produce a severe high anion gap metabolic acidosis. Blocking alcohol dehydrogenase prevents metabolite formation, which is why the antidote works and why it must be given before metabolism is complete.

> [!tip] The gap sequence tells you the timing
> **Early:** parent alcohol present, metabolites not yet formed → **raised osmolar gap, normal anion gap.**
> **Late:** parent alcohol metabolised → **normal osmolar gap, raised anion gap with severe acidosis.**
> A patient presenting late with a normal osmolar gap has not excluded the diagnosis — they have the dangerous version of it. `UNVERIFIED — osmolar gap calculation and its normal threshold require verification; the gap is insensitive and a normal value never excludes ingestion.`

> [!danger] The organ-specific clues
> **Methanol — visual symptoms.** Blurred vision, "snowfield" whiteout, photophobia, and on examination dilated poorly reactive pupils with optic disc hyperaemia. Blindness is permanent once established.
> **Ethylene glycol — renal failure with hypocalcaemia.** Oxalate crystalluria, acute kidney injury, and tetany or a prolonged QT from calcium chelation.

**S/Smx:** Apparent intoxication **without the smell of ethanol**. Nausea and vomiting. Then, as metabolites accumulate, Kussmaul respiration, altered conscious state, and the organ-specific features above.

**Ix:** VBG or ABG with anion gap calculation (*why:* the severity of the acidosis drives both the antidote and the dialysis decision; *what:* severe HAGMA). Serum osmolality with calculated osmolar gap (*why:* detects the parent alcohol in the early window when the anion gap is still normal; *what:* raised gap early). Ethanol level (*why:* co-ingested ethanol competitively occupies alcohol dehydrogenase and is itself protective, and its presence explains an osmolar gap without toxic alcohol; *what:* level). UEC with calcium (*why:* ethylene glycol causes renal failure and hypocalcaemia; *what:* rising creatinine, low calcium). Urine microscopy (*why:* calcium oxalate crystals support ethylene glycol though their absence does not exclude it; *what:* envelope-shaped crystals). Lactate, interpreted with caution (*why:* glycolate cross-reacts on some lactate analysers producing a spuriously high value, and the discrepancy between analysers is itself a clue; *what:* lactate gap). Formal methanol and ethylene glycol levels (*why:* confirmatory, but turnaround is far too slow to guide treatment; *what:* level). Visual acuity and fundoscopy where methanol suspected (*why:* documents the injury and supports urgent treatment; *what:* reduced acuity, hyperaemic disc).

### 0.8.1 Mx – Immediate
Call the Poisons Information Centre early. Airway support, IV access. **Treat on suspicion — do not wait for confirmatory levels.** Alcohol dehydrogenase blockade with fomepizole, or ethanol where fomepizole is unavailable. `UNVERIFIED — fomepizole and ethanol dosing, and the anion gap or level thresholds triggering treatment, require verification with the Poisons Information Centre.` Sodium bicarbonate for severe acidosis. Cofactor therapy differs by agent — folinic acid for methanol, thiamine and pyridoxine for ethylene glycol.

### 0.8.2 Mx – Definitive
**Haemodialysis** removes both parent alcohol and metabolite and corrects the acidosis; it is the definitive treatment in severe poisoning. Early nephrology and ICU involvement. `UNVERIFIED — dialysis indication thresholds require verification.`

### 0.8.3 Mx – Chronic/long-term
Ophthalmology follow-up for methanol survivors. Renal follow-up for ethylene glycol. Drug and alcohol referral and mental health assessment.

---

## 0.9 Anaphylaxis and Acute Allergic Reaction

**D:** Acute, rapidly progressive, potentially fatal systemic hypersensitivity reaction involving airway, breathing or circulation, with or without skin involvement.

**R:**
*Unmodifiable:* Prior anaphylaxis, atopy, mast cell disorders.
*Modifiable:* Known allergen exposure, poorly labelled food, delayed adrenaline administration, upright or sudden posture change during a reaction, concurrent beta-blocker therapy blunting adrenaline response.

**A/P:** Allergen cross-links IgE on mast cells and basophils → massive degranulation with histamine, tryptase and leukotriene release → vasodilatation with capillary leak causing distributive shock and profound intravascular volume loss; bronchial smooth muscle constriction causing bronchospasm; mucosal oedema causing upper airway obstruction. Adrenaline reverses all three arms simultaneously — α1 vasoconstriction, β2 bronchodilatation, and mast cell stabilisation — which is why nothing else substitutes for it.

**S/Smx:** Sudden onset after exposure with **airway** (tongue or throat swelling, stridor, hoarseness), **breathing** (wheeze, dyspnoea, hypoxia) or **circulation** (hypotension, collapse, pallor) involvement. Urticaria, angioedema, flushing, vomiting and abdominal pain support the diagnosis but their absence does not exclude it.

> [!danger] Skin findings are absent in a meaningful minority
> Anaphylaxis with hypotension and no rash is a well-described presentation, particularly in perioperative and drug-induced cases. **Do not require urticaria before diagnosing anaphylaxis or before giving adrenaline.**

> [!danger] Two positioning and route errors that kill
> **Do not sit or stand the patient up**, and do not walk them to the bathroom or the ambulance — sudden upright posture in a volume-depleted vasodilated patient has caused arrest. Lie flat, or left lateral in pregnancy, and elevate the legs.
> **Adrenaline is intramuscular into the anterolateral thigh.** Subcutaneous and inhaled routes are inadequate. IV adrenaline is for refractory cases with expert supervision and carries real hazard.

> [!warning] Antihistamines and steroids are not treatment
> Neither reverses airway obstruction or shock. They are adjuncts at most, and reaching for them before adrenaline is the commonest documented error in anaphylaxis management. Delayed adrenaline is the strongest predictor of fatality.

**Ix:** The diagnosis is clinical and **no test should delay adrenaline.** Serum tryptase, ideally serially (*why:* supports the diagnosis retrospectively when the presentation was atypical, and matters for later allergy assessment and for medicolegal clarity in perioperative cases; *what:* acute rise falling toward baseline). Bedside glucose and ECG (*why:* excludes mimics and monitors for adrenaline-related ischaemia and arrhythmia in older patients; *what:* ischaemic change, arrhythmia). VBG (*why:* quantifies the perfusion deficit in shocked patients; *what:* acidosis, raised lactate). Formal allergy investigation is deferred to a specialist clinic weeks later — acute-phase specific IgE testing is unreliable.

### 0.9.1 Mx – Immediate
Remove the trigger where possible. Lie flat with legs elevated. **Intramuscular adrenaline into the anterolateral thigh immediately**, repeated as required. High-flow oxygen. Large-bore IV access and fluid resuscitation. Call for help early. `UNVERIFIED — adrenaline IM dose by age and weight, the repeat interval, IV infusion rates, and paediatric fluid bolus volumes are all deliberately omitted here. Obtain them directly from the ASCIA Acute Management of Anaphylaxis guideline and ANZCOR Guideline 9.2.7. A paediatric adrenaline timing error has already been found in this corpus and originated in exactly this section.`

### 0.9.2 Mx – Definitive
Observation for biphasic reaction, which can occur hours after apparent resolution. Refractory cases require adrenaline infusion and ICU. Patients on beta-blockers may respond poorly to adrenaline; glucagon is described as an adjunct. `UNVERIFIED — observation period duration and glucagon dosing require verification.`

### 0.9.3 Mx – Chronic/long-term
Adrenaline autoinjector prescription with **demonstrated** technique, not just a script. ASCIA action plan. Medical alert identification. Allergy or immunology referral. Documentation of the allergy in the record and on discharge summary. Cross-refer [[15_01b_Paeds_-_Anaphylaxis]].

---

## 0.10 Australian Elapid Snakebite

**D:** Envenomation by an Australian elapid — brown, tiger, black, death adder, taipan or sea snake — producing a syndrome dominated by coagulopathy, with variable neurotoxicity and myotoxicity.

**R/Causes:** Rural and outer-suburban exposure, gardening, bushwalking, attempts to handle or kill a snake. Peak in warmer months.

**A/P:** Venom is injected into subcutaneous tissue → absorbed predominantly via **lymphatics**, not blood vessels → this is the entire rationale for pressure immobilisation bandaging, which compresses lymphatic drainage and delays systemic absorption. Once systemic: procoagulant toxins activate the clotting cascade → consumption of fibrinogen and factors → **venom-induced consumptive coagulopathy**; presynaptic and postsynaptic neurotoxins → descending flaccid paralysis beginning with cranial nerves; myotoxins → rhabdomyolysis with hyperkalaemia and renal failure.

**S/Smx:** The bite site is often unimpressive or invisible. Early systemic features are non-specific and easily dismissed: headache, nausea and vomiting, abdominal pain, collapse shortly after the bite. Later: bleeding from the bite site or venepuncture sites, ptosis and ophthalmoplegia as the first neurological signs, then bulbar weakness and descending paralysis, then myalgia and dark urine.

> [!danger] Ptosis is the earliest neurological sign
> Descending paralysis starts with the cranial nerves. **Examine for ptosis and ophthalmoplegia repeatedly** — they precede limb weakness and respiratory failure by a useful interval.

> [!warning] Do not wash the bite site
> Venom on the skin is the sample used by the snake venom detection kit. Washing it destroys the specimen. Equally: no tourniquet, no incision, no suction, no ice.

> [!info] Pressure immobilisation bandage
> A broad elastic bandage applied firmly over the bite site and extended to cover the whole limb, with the limb then splinted and the patient kept still. It is left in place until the patient is at a facility able to manage envenomation. `UNVERIFIED — bandage pressure guidance, application technique and the criteria and timing for removal require verification against ANZCOR Guideline 9.4.8 and the Australian Snakebite Project consensus guideline.`

**Ix:** Coagulation profile with INR, APTT, fibrinogen and D-dimer, repeated serially (*why:* venom-induced consumptive coagulopathy is the most sensitive and earliest laboratory marker of systemic envenomation, and serial testing is how envenomation is confirmed or excluded over time; *what:* rising INR, undetectable fibrinogen, grossly raised D-dimer). FBC (*why:* thrombocytopenia and evidence of microangiopathy; *what:* falling platelets, fragments on film). CK (*why:* identifies myotoxicity, which changes fluid and renal management; *what:* marked and rising elevation). UEC with potassium (*why:* rhabdomyolysis causes hyperkalaemia and acute kidney injury; *what:* rising creatinine and potassium). ECG (*why:* hyperkalaemic changes; *what:* peaked T waves, widened QRS). Snake venom detection kit on a bite site swab (*why:* guides monovalent antivenom selection where the snake is unidentified, though it does not diagnose envenomation and a positive result in an asymptomatic patient with normal bloods does not mandate antivenom; *what:* venom group). Serial neurological examination (*why:* ptosis and ophthalmoplegia detect neurotoxicity before respiratory compromise; *what:* new ptosis, restricted eye movements, reduced vital capacity).

### 0.10.1 Mx – Immediate
Apply or check the pressure immobilisation bandage and keep the patient still. Resuscitate. IV access in the unaffected limb. **Call the Poisons Information Centre on 13 11 26 early** — antivenom decisions in Australia are made with toxinology advice. Baseline bloods and serial repeats. Any patient with a possible elapid bite is retrieved to a facility with antivenom and laboratory capability, regardless of how well they look.

### 0.10.2 Mx – Definitive
Antivenom is indicated for confirmed systemic envenomation — coagulopathy, neurotoxicity, myotoxicity or systemic symptoms — not for a bite alone. `UNVERIFIED — antivenom indications, the number of vials, dilution, administration rate and premedication practice all require verification with the Poisons Information Centre and current Australian guidance. Vial numbers in particular have changed with evidence and must not be recalled.` Anaphylaxis to antivenom is a recognised risk; give it where resuscitation is available. Coagulopathy corrects as venom is neutralised and hepatic synthesis recovers; factor replacement is not routinely first-line.

### 0.10.3 Mx – Chronic/long-term
Prolonged observation with repeat coagulation studies before discharge. Serum sickness is a delayed complication after antivenom — warn the patient explicitly. Wound care and tetanus status.

---

## 0.11 Spider Bites — Redback vs Funnel-Web

**D:** Two clinically distinct Australian spider envenomation syndromes with opposite urgency, first aid and disposition.

> [!tip] The comparison that matters
> | | Redback (*Latrodectus hasseltii*) | Funnel-web (*Atrax*, *Hadronyche*) |
> |---|---|---|
> | Distribution | All of Australia | Eastern seaboard, Sydney region and NSW/Qld |
> | Onset | Gradual, over hours | Rapid, within minutes to an hour |
> | Local | Severe increasing local pain, sweating around the bite | Immediate severe pain, visible fang marks |
> | Systemic | Regional then generalised pain, sweating, hypertension, malaise | Autonomic storm — salivation, lacrimation, sweating, muscle fasciculation, hypertension, pulmonary oedema, coma |
> | Life-threatening | Very rarely | **Yes — a genuine emergency** |
> | Pressure immobilisation | **No** | **Yes** |
> | Antivenom | Contested benefit | Effective and indicated |

**A/P:**
*Redback:* α-latrotoxin causes massive presynaptic neurotransmitter release at nerve terminals → sustained regional pain, diaphoresis characteristically localised around or proximal to the bite, and autonomic disturbance. Systemic effects develop over hours and are rarely dangerous.
*Funnel-web:* δ-atracotoxin slows sodium channel inactivation → repetitive neuronal firing → catecholamine and acetylcholine storm → severe autonomic instability, non-cardiogenic pulmonary oedema, and in untreated cases death within hours.

**S/Smx:**
*Redback:* Increasing local pain radiating proximally, patchy or regional sweating (a distinctive and useful sign), malaise, nausea, hypertension. Pain may persist for days.
*Funnel-web:* Immediate severe pain, perioral tingling, tongue fasciculation, profuse salivation and lacrimation, piloerection, hypertension and tachycardia, then hypotension, pulmonary oedema and coma.

> [!danger] The first aid differs — getting it backwards causes harm
> **Funnel-web: apply a pressure immobilisation bandage immediately** and treat as a life threat.
> **Redback: do not apply a pressure immobilisation bandage.** The venom acts locally and slowly; bandaging worsens the already severe local pain and confers no benefit. Ice pack and analgesia.

**Ix:** Largely clinical. Continuous cardiac and respiratory monitoring in suspected funnel-web (*why:* deterioration is rapid and pulmonary oedema is the mode of death; *what:* rising respiratory rate, hypoxia, arrhythmia). VBG (*why:* quantifies the metabolic disturbance in a severe autonomic storm; *what:* acidosis, raised lactate). UEC and CK (*why:* baseline in a patient with sustained muscular activity; *what:* electrolyte derangement, elevated CK). Where the bite is unidentified and the presentation is atypical, treat as the more dangerous possibility and involve the Poisons Information Centre.

### 0.11.1 Mx – Immediate
*Funnel-web:* Pressure immobilisation bandage, immobilise, resuscitate, high-dependency monitoring, urgent antivenom. Call 13 11 26.
*Redback:* Ice pack and simple analgesia. Escalating analgesia as needed. Observation. No bandage.

### 0.11.2 Mx – Definitive
Funnel-web antivenom is effective and given on clinical grounds. `UNVERIFIED — antivenom vial numbers and repeat criteria require verification with the Poisons Information Centre.` Redback antivenom benefit over placebo has been questioned by Australian randomised evidence, and its use is now a discussion with toxinology rather than a reflex. `UNVERIFIED — confirm current recommendation and the status of the redback antivenom evidence; this is an area where practice has changed.`

### 0.11.3 Mx – Chronic/long-term
Wound care and tetanus status. Warn about serum sickness after antivenom. Redback pain may persist for days to weeks and warrants GP follow-up.

---

> [!note] Cross-references
> Sepsis and shock phenotypes → [[F0-3_Shock_Phenotypes_and_Sepsis_Syndromes]] · Acid-base consequences of these poisonings → [[F0-2_Acid-Base__DKA_and_Fluid_States]] · Resuscitation algorithms and airway management → [[F0-4_Resuscitation_Algorithms_and_Emergency_Procedures]] · Deliberate self-poisoning risk assessment → `TODO:link — N1 Risk assessment & suicidality (unbuilt)` · Adverse drug reactions and TCA overdose → [[A5_Toxicology_II_-_Poisoned_Patient__ADRs_and_Immunotherapy]]
