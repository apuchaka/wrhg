---
bfile: Corpus B/A1_Emergency_-_Deteriorating_Patient__Sepsis__Cardiac_Arrest.md
date: 2026-08-31
prestep: _meta/merges/A_BLOCK_PRESTEP.md
tooling: scripts/gapcheck.py
---

# A1 — destination table

All verdicts via `gapcheck.py` — untruncated, destination corpora only, zeros re-searched by
component (rule 2).

## Superseded

| A1 claim | Where it already is |
|---|---|
| Sepsis definition — life-threatening organ dysfunction from a dysregulated host response | `08_09_Infectious_Disease_-_Miscellaneous.md:157` |
| The Australian sepsis pathway | `08_09:164` — **"SEPSIS KILLS"**, with a `[!info] Verified` box noting it is distinct from the UK "Sepsis 6" branding |
| Necrotising soft tissue infection; **pain out of proportion** | `08_09:74` and 25 further hits — including the Type 1/Type 2 split |
| **4 Hs and 4 Ts** | `01_Cardiovascular.md` §0.5 ALS |
| Shockable versus non-shockable; **PEA** | `01_Cardiovascular.md` §0.5–§0.6 |
| Naloxone — shorter duration than most opioids, re-sedation follows | 25 hits incl. `NEW_Drugs_03_Analgesics.md` |
| Flumazenil precipitates seizures | 4 hits incl. `14a-2_Psych_-_Overdose_and_Poisoning_Management.md` |
| Check glucose in any altered conscious state | 8 hits |
| Track-and-trigger and MET escalation | 4 hits |
| **Oxygen saturation is a late sign** | `NEW_Respiratory.md:48` (*"Three traps… saturation is a late sign in several of these diagnoses"*), `NEW_Neurology.md:141` |

## CONFLICT

| ID | Topic | Risk |
|---|---|---|
| **CF-034** | **Is qSOFA a screening tool or a prognostic flag?** | **R2** |

`08_09_Infectious_Disease_-_Miscellaneous.md:159` heads its box *"**qSOFA — quick screening
tool** to identify patients at increased risk of sepsis"* and lists the three components.

A1: *"**qSOFA is a prognostic flag, not a screening tool.** … It is **insensitive as a bedside
screen**, and a **negative qSOFA does not exclude sepsis**."*

**These cannot both be acted on.** A clinician who reads the existing box as licence to screen
with qSOFA, and gets a negative, may not escalate a septic patient. **R2 — it drives
disposition**, and the failure mode is silent: the score performs exactly as designed while
being used for the wrong purpose.

**Not adjudicated** (§1.12). Both claims retained; block above the existing box.

## Additive

| A1 claim | Destination |
|---|---|
| **Why SIRS was retired as a sepsis definition** — it describes a generic inflammatory response and fires in pancreatitis, trauma, burns and post-operative states with no infection | `08_09` sepsis entry |
| **Tachycardia with hypotension in the first 24 hours post-operatively is bleeding until excluded** — not pain, not anxiety, not anaesthetic effect | `11_09b_Ortho_-_Trauma.md` / post-operative care |
| **Anastomotic leak presents around days 3–7** as tachycardia, low-grade fever, ileus and a patient "not progressing" — not as obvious peritonitis; **new post-operative AF is a recognised early sign** | same |

## A third kind of rule 9 artifact — an acronym collision across specialties

`SIRS` returned **2 hits, both real words, neither the right concept**:

- `18_Geriatrics_and_Older_Persons_Health.md:235` and `Clinical-Process-EBM-Consent-Capacity.md:107` — **SIRS = the Serious Incident Response Scheme**, the aged-care reporting obligation under the *Aged Care Act 1997*.

This is not a substring inside a longer word (rule 9's usual form) and not a paraphrase. It is
**the same acronym meaning something else in a different specialty**, and it produces hits that
survive word-boundary anchoring, survive reading the line, and are only caught by reading the
*meaning*. **Anchoring does not help here; comprehension does.**

## Summary

| | n |
|---|---|
| Superseded | 10 |
| **Additive** | **3** |
| **Conflicts raised** | **1 (CF-034, R2)** |

The pre-step predicted the shape of this: no named-instrument additive, and the yield in
mechanism and framing instead.
