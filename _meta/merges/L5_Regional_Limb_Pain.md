---
name: L5 destination table
description: Where every section of Corpus B-new/L5_Regional_Limb_Pain.md goes, including the sections that were discarded.
bfile: Corpus B-new/L5_Regional_Limb_Pain.md
built: 2026-08-31
---

# L5_Regional_Limb_Pain — destination table

**34 concepts tested · 31 present · 3 absent.**
**Additive/discard ratio: 3 additive / 31 discard = 9% additive.**

## An A-versus-C inconsistency, noted and not merged

`11_04_Ortho:87` titles its section **"Greater trochanteric pain syndrome (trochanteric
bursitis)"**, while `NEW_Exam_Manoeuvres_and_Procedures:221` says *"Lateral hip pain with a
positive Trendelenburg in an older woman is usually **gluteal tendinopathy**, not
'trochanteric bursitis'"*. **Corpus C already carries the correction; Corpus A's heading
still carries the superseded name.** This is an A-versus-C disagreement, not an A-versus-B
one, so it is outside this merge's scope and no `CONFLICT` block was written — recorded here
so it is not rediscovered.

## Destination table

| L5 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Referred pain patterns; localise by structure; red flags; injection is not a strategy | — | **DISCARD** — `11_07a_Ortho` dermatomes, `NEW_Orthopaedics_and_Trauma` |
| 0.2 | Passive range as the discriminator; rotator cuff pain and tear; adhesive capsulitis | — | **DISCARD** — `11_02_Ortho`, 3 `capsulitis` hits, `NEW_Exam_Manoeuvres` |
| 0.2 | **Posterior shoulder dislocation is missed on the AP film** | `Corpus A/11_02_Ortho…` | **ADDITIVE** — `lightbulb` 0 hits, base-A 0. All `dislocation` hits in this region are hip or labral. The blocked-external-rotation sign and the seizure/electrocution mechanism were absent |
| 0.3 | **Corticosteroid injection is the wrong reflex in lateral epicondylalgia** | `Corpus A/11_02_Ortho…` | **ADDITIVE** — `epicondylalgia` 0 hits, base-A 0. `11_02:141–145` covers tennis elbow with *"rest, ice, physiotherapy, NSAIDs"* and does not mention injection at all — so the thing patients ask for is unaddressed, along with the reason the naming changed from -itis to -algia |
| 0.3 | **Pulled elbow in a toddler** | `Corpus A/11_10_Ortho_-_Paediatric_Orthopaedics.md` | **ADDITIVE** — `nursemaid` 0, and all 3 `pronation` hits are adult fracture mechanisms. The commonest paediatric elbow injury, absent from the paediatric orthopaedics file |
| 0.3 | The posterior fat pad sign is always pathological | — | **DISCARD** — `11_02:89` and `Investigation-Interpretation:203` both carry it |
| 0.4 | Hip OA; avascular necrosis with a normal early radiograph; occult hip fracture | — | **DISCARD** — `11_04_Ortho`, 43 `avascular` hits |
| 0.4 | **Greater trochanteric pain syndrome is gluteal tendinopathy** | — | **DISCARD** — `NEW_Exam_Manoeuvres:221`; see the A-versus-C note above |
| 0.5 | Examine the hip in every patient with knee pain | — | **DISCARD** — `11_10_Ortho` (SUFE/Perthes referred pain) and `11_05_Ortho` |
| 0.5 | Knee OA and the evidence about arthroscopy | — | **DISCARD** — 3 `arthroscopy` hits |
| 0.5 | Effusion timing after acute knee injury; the specific injuries | — | **DISCARD** — `NEW_Exam_Manoeuvres:37` (immediate haemarthrosis = ACL), `11_05_Ortho` |
| 0.5 | Extensor mechanism rupture — test the straight leg raise | — | **DISCARD** — `11_05_Ortho` |
| 0.6 | Scaphoid fracture with a normal radiograph; the other hand injuries | — | **DISCARD** — 13 `scaphoid` hits |
| 0.6 | Hand infections are surgical emergencies | — | **DISCARD** — `11_01_Ortho`, and felon and paronychia were merged there from K2 earlier in this run |
| 0.7 | **Achilles rupture — plantarflexion does not exclude it**; Thompson/Simmonds | — | **DISCARD** — 4 `Thompson` and 3 `Simmonds` hits |
| 0.7 | Always examine the proximal fibula; Maisonneuve | — | **DISCARD** — 2 `Maisonneuve` hits |
| 0.7 | Ankle sprain and the Ottawa rules; stress fracture; the diabetic foot | — | **DISCARD** — 7 `Ottawa` hits; `06_Metabolic:0.15.4` Diabetic Foot |

## NO-BASELINE

All three: `lightbulb`, `epicondylalgia` and `nursemaid` return 0 in Corpus A and C at base-A.

## Rule 5 note

`11_10_Ortho` is a paediatric destination. The pulled-elbow block states **no absolute
quantity** — the age band is written in words ("one to four years old"), and the reduction
manoeuvre and observation period are deliberately left to an `UNVERIFIED` marker naming RCH
and Queensland Children's Health.

## New files

**None.**
