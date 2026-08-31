---
name: Week 1 vault-wide claim audit — C3
description: Every claim in C3_Jaundice_and_Liver_Disease tested against all of Corpus A and Corpus C. Report only.
built: 2026-08-31
status: REPORT ONLY — nothing merged
---

# C3_Jaundice_and_Liver_Disease — vault-wide claim audit

**Extraction rule, verbatim:** one claim = one assertion that could independently be true or
false, and that a reader could act on differently.

```
claims extracted   118
PRESENT             89
WEAKER              16
ABSENT              13
```

## Claim density per section

| § | Topic | Claims |
|---|---|---:|
| 0.1 | Mechanism and classification | 15 |
| 0.2 | Unconjugated hyperbilirubinaemia | 12 |
| 0.3 | Conjugated and obstructive | 19 |
| 0.4 | Acute liver failure | 15 |
| 0.5 | Chronic liver disease and cirrhosis | 24 |
| 0.6 | Complications of cirrhosis | 24 |
| 0.7 | Hepatomegaly, splenomegaly, hepatic pain | 9 |

## Merged blocks — both clean against base-A

Two exist: `03_Gastrointestinal:1514` (pulmonary complications of cirrhosis) and `:1786`
(bilirubin metabolism).

- `hepatopulmonary` **0 in base-A** · `portopulmonary` **0** · `platypnoea` **0**
- `biliverdin` **0** · `reticuloendothelial` **0** · `glucuronic` **0**

**No duplication, and no buried disagreement.** C3 is the cleanest merge audited so far.

## The 13 ABSENT

| # | Claim | Weight |
|---:|---|---|
| 11 | **"liver function tests" mostly do not test liver function** — ALT, AST, ALP, GGT and bilirubin mark damage or obstruction, not function | **the framing the whole section rests on**; the components are present, the correction is not |
| 13 | **watch the INR** — it has the short half-life, so it reflects *acute* function and is the more sensitive early marker; big transaminases with a normal INR is injury without failure | **prognostic reasoning**, and the practical instruction |
| 22 | **pigment stones from chronic haemolysis** | a diagnosis linking two present topics |
| 44 | **ultrasound first, and duct dilatation is the branch point** — its absence redirects to hepatocellular or intrahepatic causes | `duct dilatation`, `biliary dilatation`, `dilated intrahepatic` all 0. **The single decision that orders the whole obstructive workup** |
| 54 | **do not routinely correct the INR** — it is the prognostic marker and a transplant listing component; FFP obscures the trajectory | **counterintuitive, examined, and a real management error.** Distinct from the *rebalanced coagulopathy* point in cirrhosis, which is present |
| 58 | in acute liver failure patients are **functionally immunosuppressed** and frequently have no fever or leucocytosis | red flag |
| 61 | **fetor hepaticus** | 0, self-match only |
| 69 | **thrombocytopenia is often the earliest laboratory clue** to compensated cirrhosis, via splenic sequestration | `thrombocytopenia` has 58 hits, none making this link. **How compensated cirrhosis is actually found** |
| 75 | **variceal screening endoscopy at diagnosis of cirrhosis** so primary prophylaxis starts before the first bleed | 0. Treatment of varices is present; the screening program is not |
| 105 | hepatorenal syndrome is a diagnosis of exclusion, and **an albumin challenge is used to exclude hypovolaemia** before making it | the diagnostic step |
| 110 | congestive hepatomegaly is smooth, tender and **pulsatile in tricuspid regurgitation** | bedside sign |
| 116 | the liver parenchyma is insensate — **pain arises from stretch of Glisson's capsule** | mechanism |
| 117 | so hepatic pain means **rapid** distension, and **a slowly enlarging liver is painless** — which is why hepatic metastases are painless until very large | the clinical corollary, and the more useful half |

## The 16 WEAKER (selected)

| # | Claim | Where, and what is lost |
|---:|---|---|
| 9 | **a raised ALP with a normal GGT points away from the liver** — bone or placenta | ALP and GGT both present; the discriminating *pairing* is not |
| 34 | painless progressive jaundice with weight loss is malignancy until proven otherwise | pancreatic cancer present; **"the absence of pain is not reassuring — it is the pattern"** is not |
| 37 | drug-induced cholestasis may appear **weeks after the course finished**, which is why it is missed | flucloxacillin present as a cause; the latency is the actionable part |
| 52 | **contact a transplant unit before the patient meets criteria** — referring too late is the commonest error | transplant referral present; the pre-emptive instruction is not |
| 74 | surveillance detects HCC **at a curable stage; symptomatic HCC is usually incurable** | surveillance present; the rationale that makes people do it is not |
| 76 | **put surveillance in the discharge summary with who is responsible** | the handover failure mode |
| 96 | **SBP frequently presents with no abdominal pain and no fever** — sometimes only worsening encephalopathy or renal impairment | SBP and the tap are present; the atypical presentation that makes the tap universal is not |
| 100 | **inoculate culture bottles at the bedside** — it substantially improves yield | technique |
| 104 | **ammonia is not required and a normal level does not exclude** encephalopathy | ammonia appears as a mechanism; the over-ordering correction does not |
| 112 | **a cirrhotic liver is typically small and shrunken**, so hepatomegaly in cirrhosis should prompt thought of malignancy or congestion | `shrunken` 1 destination hit; the inference is not drawn |
| — | **hepatic encephalopathy grading** | **PRESENT but unnamed** — `03_Gastrointestinal:230–234` gives all four grades under a heading reading only `Grading`. `West Haven` returns **0 across the whole vault.** Exactly as CLAUDE.md records. Lost: the eponym, which is how it is examined |

## Method note — the numeral fold earned its place immediately

The encephalopathy scale was found by searching `Grade 3`, which the new numeral folding also
matches as `Grade III`. Without it, a search phrased in Roman numerals — the form most
textbooks use for West Haven — would have returned a false ABSENT on a complete four-grade
scale sitting in the destination file.
