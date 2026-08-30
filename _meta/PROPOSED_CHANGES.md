---
name: proposed-changes
description: PROPOSALS ONLY. ASCIA 2026 v2 content the corpus lacks or states differently. NOTHING HERE HAS BEEN APPLIED to clinical content.
---

# Proposed changes — ASCIA Acute Management of Anaphylaxis, 2026 v2

**Verified against the source PDF on 2026-08-30**, page by page, including the image-only pages
(4 and 6) which carry the flowchart and the dose tables. **No clinical content has been edited.**

> [!danger] **The corpus's weight-band table is a SUPERSEDED, COARSER version. This is the
> substantive finding, and it is not additive — it changes existing figures.**

## 1. The band table differs materially — four locations affected

**ASCIA 2026 v2, p6, table header: "Volume (mL) of adrenaline 1:1,000 ampoules"**

| Age (years) | Weight (kg) | ASCIA 2026 volume |
|---|---|---|
| ~<1 | **<7.5** | **0.1 mL** |
| ~1–2 | 7.5 | **0.1 mL** |
| ~2–3 | 15 | **0.15 mL** |
| ~4–6 | 20 | **0.2 mL** |
| ~7–10 | 30 | **0.3 mL** |
| ~10–12 | 40 | **0.4 mL** |
| >12 and adults | >50 | **0.5 mL** |

**What the corpus currently says** (`09_01`, and identically in `01_Cardiovascular`):

| Corpus | ASCIA 2026 | Difference |
|---|---|---|
| `<7.5 kg / <6 months` → **0.1–0.15 mL** | `~<1 year, <7.5 kg` → **0.1 mL** | **volume is a range where ASCIA gives one figure; age band is `<6 months` where ASCIA says `~<1 year`** |
| `7.5–20 kg and ≤5 years` → **0.15 mL** | 7.5 kg → **0.1 mL**; 15 kg → 0.15 mL; 20 kg → **0.2 mL** | **the corpus band is coarse: it over-doses at 7.5 kg and under-doses at 20 kg** |
| `>20 kg and ≥5 years` → **0.3 mL** | 30 kg → 0.3 mL; 40 kg → **0.4 mL** | under-doses at 40 kg |
| `>50 kg and ≥12 years` → 0.5 mL | >50 kg → 0.5 mL | **matches** |

**Affected files:** `09_01_Dermatology` · `01_Cardiovascular` · `NEW_Drugs_01` (injector bands) ·
`15_01b_Paeds` (points at the others).

## 2. Intranasal is now a route — absent from the corpus

ASCIA 2026 writes **IM/IN** throughout: *"Give adrenaline (epinephrine) IM/IN (intramuscular or
intranasal)"*.

| Device | Band |
|---|---|
| **neffy® 1 mg** nasal spray | **15–30 kg (minimum age 4 years)** |
| **neffy® 2 mg** nasal spray | **30 kg and over** |

Both are listed as TGA/Medsafe entries in the device table. **The corpus has no intranasal route
anywhere.**

## 3. Refractory anaphylaxis — peripheral IV adrenaline infusion (p6)

| Setting | Protocol |
|---|---|
| **ED / tertiary** | Mix **1 mL of 1:1,000 in 100 mL** normal saline. Start at **0.5 mL/kg/hour** (~0.1 microgram/kg/minute). **Infusion pump only.** |
| **Non-tertiary / pre-hospital**, in consultation with a senior clinician and critical care/medical transport | Mix **1 mL of 1:1,000 in 1,000 mL** normal saline. Start at **~5 mL/kg/hour** (~0.1 microgram/kg/minute). Without a pump, a standard giving set delivers ~20 drops/mL, so **~2 drops per second for an adult**. |

Both: titrate to response; monitor continuously with ECG, pulse oximetry and frequent
non-invasive BP. ASCIA notes the protocol is **for temporary use** — indefinite continuation
risks fluid overload.

## 4. IV adrenaline boluses

*"IV boluses of adrenaline are **NOT recommended** but may be used in some specialist settings
(e.g. perioperative/theatre) and in peri-cardiac arrest scenarios with critical care/medical
transport service advice, and as indicated in cardiac arrest."*

**Note the exceptions are part of the statement** — this is not a flat prohibition.

## 5. Fluid bolus — ASCIA gives TWO figures in the same document

| Location | Figure |
|---|---|
| Initial management flowchart (p4) | *"Consider IV insertion and fluid bolus **10-20 mL/kg** NaCl 0.9%"* |
| Actions if IV infusion not available (p8) | *"fluid bolus **(20mL/kg)** NaCl 0.9%"* |

**Not a transcription error on my part — both appear verbatim.** Whichever the corpus adopts
should say which context it came from.

## 6. Infants (p8) — supports the B50 closure

- *"A 150 microgram device **may be prescribed for an infant weighing 7.5-10kg** by health
  professionals who have made a considered assessment."*
- *"Use of a 150 microgram device for treatment of infants weighing 7.5kg or more poses **less
  risk**, particularly when used without medical training, than use of an adrenaline ampoule and
  syringe."*
- Infants may **retain pallor** despite one or more doses; this can resolve without further doses.
- **More than two doses in infants may cause hypertension and tachycardia**, often misread as
  ongoing cardiovascular compromise.
- Infants should be **held flat or seated with legs outstretched — not upright, not over the
  shoulder.**

## What I could not verify

Nothing. Pages 4 and 6 are image-only and were read by page rendering after installing
`poppler-utils`; every figure above was read from the source, not from a summary.
