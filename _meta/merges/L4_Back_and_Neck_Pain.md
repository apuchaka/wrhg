---
name: L4 destination table
description: Where every section of Corpus B-new/L4_Back_and_Neck_Pain.md goes, including the sections that were discarded.
bfile: Corpus B-new/L4_Back_and_Neck_Pain.md
built: 2026-08-31
---

# L4_Back_and_Neck_Pain — destination table

**28 concepts tested · 27 present · 1 absent.**
**Additive/discard ratio: 1 additive / 27 discard = 4% additive.**

## A scope error in my own reading, caught before it became a merge

I filtered the `MSCC` gapcheck output for `whole spine|ambulat` and got nothing, and was
about to record **two** additive claims. **Both are present** — at `04_Neurology:1735` and
`:1743` — on lines that do not contain the string `MSCC`, which is what my filter was
searching. **The gapcheck result was correct; my filter over it re-created exactly the
scope error rule 10 describes.** Reading the section itself settled it.

## Destination table

| L4 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Most back pain is non-specific and self-limiting | — | **DISCARD** — `11_06_Ortho`, `NEW_Orthopaedics_and_Trauma` |
| 0.1 | Red flags grouped by what they point to | — | **DISCARD** — `11_01_Ortho`, `NEW_Orthopaedics_and_Trauma:27` |
| 0.1 | Referred visceral pain, some of it lethal | — | **DISCARD** — 58 `dissection` hits; `01_Cardiovascular` AAA and dissection |
| 0.1 | **Yellow flags predict chronicity better than any scan** | `Corpus A/11_06_Ortho_-_Spinal_Orthopaedics.md` | **ADDITIVE** — 36 `yellow` hits, **not one** about psychosocial predictors of chronic back pain. Base-A 0. The corpus covers red flags thoroughly and has no second axis at all |
| 0.1 | Do NOT image non-specific back pain without red flags | — | **DISCARD** — present; the new block supplies the *mechanism* (incidental findings confirming a fear-avoidance belief) rather than restating the rule |
| 0.2 | Cauda equina: ask directly about bladder, bowel and sexual function; bladder scan and PR; same-day MRI | — | **DISCARD** — 52 `equina` and 46 `residual` hits; `11_01_Ortho` |
| 0.3 | **MSCC: pain precedes the neurology by weeks** | — | **DISCARD** — `04_Neurology:1732` says it in those words |
| 0.3 | **MSCC: image the WHOLE spine** | — | **DISCARD** — `04_Neurology:1735`: *"urgent whole-spine MRI … whole spine imaging is needed since metastatic disease is frequently multifocal"* |
| 0.3 | **MSCC: ambulatory status at treatment predicts outcome** | — | **DISCARD** — `04_Neurology:1743`: *"neurological function at the time treatment starts is the strongest predictor"* |
| 0.4 | Discitis and vertebral osteomyelitis; the triad is present in a minority; organisms; cultures before antibiotics | — | **DISCARD** — `11_06:111` Discitis, `08_09:216` |
| 0.4 | Epidural abscess causes rapid irreversible cord injury | — | **DISCARD** — `08_09:279`, `11_01:170` |
| 0.5 | Natural history is good and saying so is treatment; language shapes the outcome | — | **DISCARD** — folded into the yellow-flag block rather than merged twice |
| 0.5 | Radiculopathy | — | **DISCARD** — `04_Neurology:1380`, `11_06` |
| 0.6 | Lumbar spinal stenosis; **neurogenic vs vascular claudication** | — | **DISCARD** — `NEW_Cardiology_and_Vascular:222` names neurogenic claudication as *"the key mimic"* with the relieved-by-sitting discriminator; `11_06:39` |
| 0.6 | Vertebral fragility fracture; vertebroplasty and kyphoplasty | — | **DISCARD** — `11_06:57`, 2 hits each |
| 0.7 | **Cervical myelopathy — insidious and attributed to ageing**; Hoffmann; Lhermitte | — | **DISCARD** — `11_06:27` Degenerative cervical myelopathy; 4 `Hoffmann`, 3 `Lhermitte` hits |
| 0.7 | Cervical spine trauma; Canadian C-spine and NEXUS | — | **DISCARD** — 7 `Canadian` and 1 `NEXUS` hits, `NEW_Investigations_Orthopaedics:188` |
| 0.7 | **Three groups whose cervical spine is different** | — | **DISCARD** — rheumatoid, Down syndrome and ankylosing spondylitis are all covered, and the atlantoaxial instability point was already discarded in L2 |
| 0.7 | Mechanical neck pain and whiplash; vascular considerations | — | **DISCARD** — 2 `whiplash` hits; `NEW_Investigations_Orthopaedics:207` covers vertebral and carotid dissection with CT angiography |

## NO-BASELINE

`yellow flag` returns 0 in Corpus A and C at base-A.

## New files

**None.**
