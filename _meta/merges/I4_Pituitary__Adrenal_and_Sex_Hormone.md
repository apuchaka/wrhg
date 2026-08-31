---
name: I4 destination table
description: Where every section of Corpus B-new/I4_Pituitary__Adrenal_and_Sex_Hormone.md goes, including the sections that were discarded.
bfile: Corpus B-new/I4_Pituitary__Adrenal_and_Sex_Hormone.md
built: 2026-08-31
---

# I4_Pituitary__Adrenal_and_Sex_Hormone — destination table

**30 concepts tested · 29 present · 1 absent.**
**Additive/discard ratio: 1 additive / 29 discard = 3% additive — the lowest of the run.**

## An eighth substring trap

`Conn` (for Conn syndrome) returned **123 hits**: `connective` ×39, `connects` ×22,
`connected` ×18, `connecting` ×13, `Connective` ×13, `connection` ×7. **Zero real** — and
it did not matter, because `aldosteronism` returned 14 real hits and the topic is present.
**The eponym search would have produced a false ABSENT on a topic the corpus covers well.**

## Destination table

| I4 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Order of hormone loss; causes of hypopituitarism; mass effect | — | **DISCARD** — `06_Metabolic:0.14`, 9 `hypopituitarism` hits |
| 0.1 | **Give hydrocortisone before thyroxine** | — | **DISCARD** — present **three times**: `06_Metabolic:435` (*"glucocorticoid replacement must be started before or alongside levothyroxine"*), `NEW_Drugs_10:206`, `NEW_Drugs_13:148` |
| 0.1 | Pituitary apoplexy; diabetes insipidus | — | **DISCARD** — 8 `apoplexy` hits; `06_Metabolic:0.19` |
| 0.2 | Prolactinoma — check the simple things first; treated medically | — | **DISCARD** — 12 `cabergoline` hits; `NEW_Investigations_Endocrine:125` lists the drug and pregnancy causes to exclude before imaging |
| 0.2 | Acromegaly; the other tumours | — | **DISCARD** — 13 `acromegaly` hits |
| 0.3 | Adrenal insufficiency — commonest cause is exogenous steroid; primary vs secondary; Synacthen; sick day rules | — | **DISCARD** — `06_Metabolic:0.13` Addison's, 7 `Synacthen` hits, and `NEW_Drugs_10_Endocrine`'s steroid-withdrawal danger callout |
| 0.4 | Cushing — endogenous causes by ACTH; discriminating features; pseudo-Cushing | — | **DISCARD** — `06_Metabolic` Cushing's, 1 `pseudo-Cushing` hit |
| 0.4 | Primary aldosteronism, commoner than taught | — | **DISCARD** — `06_Metabolic:261` with the aldosterone-renin ratio, CT and **adrenal vein sampling**; `NEW_Investigations_Endocrine:131` |
| 0.4 | Phaeochromocytoma and paraganglioma | — | **DISCARD on provenance** — 24 `phaeochromocytoma` and 2 `paraganglioma` hits. `_meta/KNOWN_ABSENCES.md` **entry 7** records that there is **no entity section** and that the three parts sit scattered across Corpus C — **and states the consolidation question is open and for a later round.** Not consolidated here |
| 0.5 | Hirsutism, virilisation, PCOS, male hypogonadism | — | **DISCARD** — 14 `hirsutism`, 6 `virilis`, 12 `hypogonadism` hits; `17_01_FGM__Amenorrhoea__PCOS` owns PCOS |
| 0.6 | **Adrenal incidentaloma — the two questions, the mandatory functional workup, never biopsy before excluding phaeo, imaging phenotype** | `Corpus A/06_Metabolic_Medicine_and_Endocrinology.md` | **ADDITIVE** — `Hounsfield` 0 hits; `adrenal` + `biopsy` on the same line 0 hits. The three `incidentaloma` hits are all **indications for a screening test**, not a workup |
| 0.6 | Pituitary incidentaloma | — | **PARTIAL, not merged** — narrower, and the same reasoning applies |

## NO-BASELINE — and a marker I wrote and then removed

I stamped this block `NO-BASELINE` and then tested it properly. **`adrenal incidentaloma`
returns 2 hits in Corpus A and C at base-A** — both in Corpus C, naming it as an
*indication* for aldosterone-renin and metanephrine screening. **An inherited layer does
exist on the subject**, so the marker was wrong by my own criterion and was removed before
the commit. `Hounsfield` is 0, but the marker attaches to the block, not to one sentence.

## New files

**None.**
