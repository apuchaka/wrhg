---
bfiles:
  - Corpus B/A9_Transfusion__Coagulopathy_and_Anticoagulant_Emergencies.md
  - Corpus B/A10_Ethics__Capacity__Consent_and_Certification.md
date: 2026-08-31
prestep: _meta/merges/A_BLOCK_PRESTEP.md
tooling: scripts/gapcheck.py
---

# A9 + A10 — destination table

## The rule 9 artifact of the entire project

`TRALI` returned **966 hits**. **963 of them are the word "Australian".**

```
inst the Australian Heart F
kers the Australian Heart F
```

**`Aus`TRALI`a` contains `TRALI`.** In an Australian medical corpus, on a transfusion
reaction, the containing word is **the most common proper noun in the entire vault**.
Anchored, `\bTRALI\b` returns **3** — and TRALI and TACO are both **genuinely present**, with
their own boxes at `10_08_Haemonc_-_Blood_Products_and_Transfusion.md:146` and `:148`.

**This beats `TIMI`'s 203→0 on ratio and on danger.** A 966-hit result is not read as
"probably artifacts" — it is read as "obviously covered, move on". The one saving grace is
that here the unanchored answer happened to be *correct*; had TRALI been absent, nothing in
that count would have revealed it.

## Superseded

| Claim | Where it already is |
|---|---|
| **The haemoglobin lags in acute bleeding** | 4 hits |
| **The lethal triad** — hypothermia, acidosis, coagulopathy | 2 hits |
| Massive haemorrhage protocol, activate early | 6 hits |
| **Restrictive transfusion threshold** | 27 hits, incl. `10_08_Haemonc` and the NBA-aligned content |
| Acute transfusion reaction — stop, keep the line open, check identity | 5 hits |
| **TACO versus TRALI** | `10_08_Haemonc.md:146`, `:148`, each with its own box; plus `NEW_Drugs_07_Blood_and_Electrolytes.md:46`, `:51` (*"prescribe the rate"*) |
| Citrate hypocalcaemia, hyperkalaemia, hypothermia in massive transfusion | 14 hits |
| A negative haemostatic-challenge history argues against an inherited disorder | 4 hits |
| **Factor VII has the shortest half-life, so the PT prolongs first** | 26 hits |
| DIC — consumption, low fibrinogen, schistocytes, always secondary | 44 hits |
| **Reverse anticoagulation in ICH before the coagulation result returns** | 9 hits incl. `NEW_Investigations_Haematology_Part2.md` |
| DOACs — no routine level; idarucizumab and andexanet | 14 hits |
| Capacity — understand, retain, weigh, communicate | present |
| **An adult may make an unwise decision** | present |
| Decision-specific capacity | 3 hits |
| **Gillick competence** | 3 hits |
| **Material risk / patient-centred standard** | 2 hits |
| Advance care directives | 11 hits |
| Mental Health Act authorises treatment of the mental illness only | 5 hits |
| Voluntary assisted dying | present |
| Open disclosure | 7 hits |
| Ahpra notifiable conduct | 6 hits |
| **Austroads** *Assessing Fitness to Drive*, private vs commercial | 26 hits |

## Additive

| From | Claim | Destination |
|---|---|---|
| **A9 §0.2** | **Delayed haemolytic transfusion reaction** — days later, falling haemoglobin, jaundice, newly positive antibody screen in a previously sensitised patient | `10_08_Haemonc_-_Blood_Products_and_Transfusion.md` |
| **A9 §0.3** | **"Rebalanced haemostasis" in liver disease** — procoagulant *and* anticoagulant factors fall together, so **a raised INR in cirrhosis does not mean the patient is auto-anticoagulated** and does not predict bleeding | `03_Gastrointestinal.md` liver section |
| **A9 §0.4** | **Someone must actively decide when, or whether, to restart anticoagulation** after the bleed is controlled — leaving a mechanical valve or recent PE indefinitely un-anticoagulated is its own harm | `10_08_Haemonc` |
| **A10 §0.3** | **Substituted judgement** — what would *this person* have wanted, from their known values and previously expressed wishes; **not** what the substitute decision-maker would choose, and **not** what the team thinks best | `Clinical-Process-EBM-Consent-Capacity.md` |
| **A10 §0.5** | **Brain death determination** — the preconditions (a known cause sufficient to explain irreversible damage, reversible contributors excluded), **two practitioners examining independently**, and that **spinally mediated movements including the "Lazarus sign" occur after brain death and do not indicate brain function** | same |
| A10 §0.5 | **Death determination and the donation conversation are kept separate** — death determined and communicated first, family given time | same |
| A10 §0.7 | **Work capacity certificates are framed around what the person CAN do**, not what they cannot, and are **legal documents** — certify only what you assessed, and never backdate | same |

## A note on A10 and legal content

**Most of A10 is jurisdictional**, and B wrote it against South Australian legislation from
model knowledge. Per §1.14, nothing legal is asserted from an unverified layer. **Only the
clinical framing is merged** — the substituted-judgement *standard*, the brain-death
*principles*, the certificate *framing* — each with an `UNVERIFIED` marker naming the
legislation or professional standard that would settle it. **No Act, section, timeframe or
eligibility criterion is reproduced.**

## Summary

| | n |
|---|---|
| Superseded | 23 |
| **Additive** | **7** |
| Conflicts | 0 |
