---
block: Paediatrics
source: quackquackmed 15.01 Anaphylaxis in children
trust: inherited
population: paed
conflicts_open: 0
conflicts_r1: 0
---

## Anaphylaxis

> [!note] See [[09_01_Dermatology_-_Dermatological_Emergencies]] Anaphylaxis for the full adult-context entry (definition, pathophysiology, atypical infant presentation signs, and the point that persistent tachycardia is the first sign of cardiovascular compromise in children specifically), not repeated here — this entry covers the paediatric-specific practical details.

- **Dx:** sudden onset, life-threatening problem involving airway, breathing, or circulation, and in ~80% skin changes.
> [!fail] CONFLICT CF-001 — ASCIA IM adrenaline: same dose stated in two different units, across three owners **R1**
> **`09_01_Dermatology_-_Dermatological_Emergencies` (`inherited`):** "IM adrenaline dose (ASCIA) — 1:1000, outer mid-thigh, **0.01 mg/kg** up to a maximum of **0.5 mg**", with a weight-and-age band table.
> **`NEW_Drugs_01_Allergy_and_Anaphylaxis` (`snippet`):** "Ampoule (adrenaline 1:1000), all ages: **0.01 mL/kg**, to a maximum of **0.5 mL (0.5 mg)** per dose, intramuscular", plus injector bands from 7.5 kg.
> **`15_01b_Paeds_-_Anaphylaxis` (`inherited`):** asserts ASCIA verification and "1:1000 … weight-based", and **states no figure at all**.
> **Why it matters:** **`0.01 mg/kg` and `0.01 mL/kg` are not the same quantity.** They coincide only at **1:1000**, where 1 mL = 1 mg, and diverge at any other concentration — at 1:10,000 (the arrest presentation) `0.01 mL/kg` delivers **one tenth** of `0.01 mg/kg`. The mg form is concentration-independent; the mL form is correct only because "1:1000" happens to sit beside it. **One of the two is wrong as written.** A reader who carries the mL form to a differently-concentrated ampoule under-doses a child in anaphylaxis.
> **Resolve against:** **ASCIA** Acute Management of Anaphylaxis (open, no login) and the Australian **Acute Anaphylaxis Clinical Care Standard**. Tracked as `PENDING_GUIDELINE_CHECKS.md` **B72**; see also **B50** (the 7.5 kg floor) and **B71** (duplicate owners).
> **RESOLVED 2026-08-30 NEITHER-WRONG — ASCIA Guidelines: Acute Management of Anaphylaxis, 2026 v2.**
> **Both unit forms are ASCIA's own, and both are correctly qualified.** The initial-management
> flowchart (p4) footnotes *"Adrenaline injector OR 1:1000 IM adrenaline - 0.01mL/kg up to
> 0.5 mL/dose"*; the pregnancy section (p8) states *"1:1,000 IM adrenaline 0.01mg per kg up to
> 0.5mg per dose"*. They are equivalent **because both state 1:1000**.
> **The defect is any mL figure WITHOUT the concentration — and a corpus-wide sweep found none:**
> every adrenaline mL value in all 240 files carries `1:1000` on its line or in its block.
> No number changed and no concentration needed adding.

> [!check] VERIFIED — ASCIA Guidelines: Acute Management of Anaphylaxis, 2026 v2 (accessed 2026-08-30)
> **Checked:** that both `0.01 mg/kg` and `0.01 mL/kg` are ASCIA's own wordings; that each is
> stated with the `1:1000` concentration; and that this entry states the concentration.
> **NOT checked:** the intranasal route and neffy devices; refractory infusion protocols;
> fluid-bolus volume; observation periods; and every non-adrenaline drug in this entry.
> **The weight-band table is now present below and separately verified.**

- Once suspected, the chief priority is IM adrenaline — strength 1:1000. Best site is the anterolateral aspect of the middle third of the thigh.

> [!danger] **IM adrenaline 1:1000 — ASCIA 2026 weight/age bands** `→MED:adrenaline`
> **Owner: [[09_01_Dermatology_-_Dermatological_Emergencies]] Anaphylaxis.** Marked mirror, not
> an independent copy — correct it there first, then here.
>
> | Age (years) | Weight (kg) | Volume of 1:1,000 ampoule | Injector device |
> |---|---|---|---|
> | **~<1** | **<7.5** | **0.1 mL** | **Not available — draw it up** |
> | ~1–2 | 7.5 | 0.1 mL | 7.5–20 kg: **150 microgram** |
> | ~2–3 | 15 | 0.15 mL | as above |
> | ~4–6 | 20 | 0.2 mL | 20 kg and over: **300 microgram** |
> | ~7–10 | 30 | 0.3 mL | as above |
> | ~10–12 | 40 | 0.4 mL | as above |
> | **>12 and adults** | **>50** | **0.5 mL** | 50 kg and over: 300 or **500 microgram** |
>
> Overall rule: **0.01 mg/kg (= 0.01 mL/kg of 1:1000) up to a maximum of 0.5 mg (0.5 mL)**.
> **7.5 kg is a DEVICE limit, not a dose limit** — below it the ampoule dose exists and no
> injector does. A 150 microgram device may be prescribed for an infant of **7.5–10 kg** on
> considered assessment. **Repeat every 5 minutes** if no or inadequate response.
>
> **This table was added 2026-08-30.** This entry previously asserted ASCIA verification and
> stated **no figure at all**, while `01_Cardiovascular` pointed here for paediatric specifics —
> so a reader following that pointer for a child's dose reached an assurance and no dose. **An
> assurance without a figure is worse than nothing.**

> [!check] VERIFIED — ASCIA Guidelines: Acute Management of Anaphylaxis, content updated May 2026, p6 and p8 (accessed 2026-08-30)
> **Checked:** every row of the mirrored table above; the 7.5 kg device threshold and the
> 7.5–10 kg considered-assessment statement; and the 0.01 mg/kg ≡ 0.01 mL/kg-of-1:1000 rule with
> its 0.5 mg cap.
> **NOT checked:** the intranasal route and neffy® devices, which ASCIA 2026 adds and this entry
> omits pending a dedicated pass; refractory infusion protocols; fluid-bolus volume; IV-bolus
> exceptions; the observation periods below, which are verified separately against their own box;
> ASCIA's infant-specific guidance on pallor, the effects of more than two doses, and positioning;
> and every non-adrenaline drug in this entry.


> [!info] Verified against current ASCIA (Australasian Society of Clinical Immunology and Allergy) Acute Management of Anaphylaxis guidelines, Aug 2026 — **IM adrenaline dosing is weight-based in current Australian guidance, not the simple 3-tier age-band split previously in this note**: 150mcg for approximately 7.5–20kg, 300mcg for ≥20kg, stepping up to 300mcg or 500mcg from around 12 years old/>50kg — the full ASCIA dose table (weight **and** age criteria, 0.01 mg/kg to a maximum of 0.5 mg) is set out in [[09_01_Dermatology_-_Dermatological_Emergencies]] Anaphylaxis. Repeat every 5 minutes if inadequate response, consistent with the original note.

### Refractory anaphylaxis

- Defined as ABC problems persisting despite 2 doses of IM adrenaline.
- **Mx:** IV fluids for shock; consider IV adrenaline infusion (only under expert guidance).

### Management after the patient's ABC are stabilised

- PO antihistamines and corticosteroids may be given as adjuncts once adrenaline has been given, but never as a substitute for or before it.
- **Ix:** serum tryptase levels (ideally within 1–2 hours of onset, with a comparison sample later) can retrospectively support the diagnosis, but has no role in the acute treatment decision.
- Refer to a specialist allergy/immunology clinic — genuinely important for children specifically, given ASCIA guidance recommends all children treated for anaphylaxis have their case discussed with the immunology team as soon as practical. Prescribe (and where possible dispense) an adrenaline injector, with device-specific training for the child/carer and a written ASCIA Action Plan for Anaphylaxis.

### Discharge planning

> [!info] Verified against current ASCIA guidelines and Queensland Children's Health emergency management guidance, Aug 2026 — **the observation-time thresholds below are updated to reflect current Australian practice**, which differs meaningfully from a simple fixed-hour-count approach:

- **Standard minimum observation: at least 4 hours after the last dose of adrenaline** for a patient who has responded well and is stable, given adrenaline's short duration of action means recurrence can still occur as it wears off (biphasic reactions are estimated to occur in ~3–20% of cases, within 48 hours of the initial episode) — this is the current ASCIA-recommended baseline, not the 6h/12h figures previously in this note.
- **Overnight observation is specifically recommended if the child:**
  - Required more than one/two adrenaline doses (reflecting more severe or refractory anaphylaxis), or had refractory anaphylaxis requiring IV adrenaline infusion or IV fluid resuscitation.
  - Has a history of severe, refractory, or biphasic/recurrent anaphylaxis.
  - Has a concomitant illness that increases risk (e.g. severe asthma, a history of arrhythmia, systemic mastocytosis or other mast cell disorders).
  - Presents for care late in the evening, given this limits the practical ability to complete a full observation period and safely arrange follow-up before a typical discharge time.
- A child who remains stable and asymptomatic through the appropriate observation period above, has (or is prescribed) an adrenaline injector with confirmed understanding of its use, and has adequate supervision arranged after discharge, may be discharged with the safety-netting and referral advice above.

> [!note] Anaphylaxis from a sting or bite
> Where anaphylaxis follows an insect sting or a bite, the envenomation itself is owned by [[NEW_Drugs_04_Antidotes_and_Antivenoms]] — antivenoms, pressure immobilisation, and the **tick paralysis** trap where weakness progresses after removal. **The anaphylaxis is treated as anaphylaxis regardless**; the envenomation is the separate question.
