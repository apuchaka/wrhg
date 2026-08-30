---
name: prefix-map
description: Corpus B's code scheme — which prefixes exist on disk, which are queue phases, the P2 -> GER rename, and the cluster name every unbuilt code resolves to. Authoritative source for Step 31's TODO markers and Step 29's retargeting.
---

# Corpus B prefix and cluster map

Measured 2026-08-30 against `00_BUILD_QUEUE.md` (v1), `00_BUILD_QUEUE_v2.md` (v2) and the files on disk.

## The rename went P2 → GER, not GER → P2

> [!danger] **Corrected finding.** The working assumption was that `GER` is the *old* geriatrics
> prefix superseded by `P2`. **It is the other way round.**
>
> - `P2. Geriatric assessment & frailty` appears **only in v1** (`00_BUILD_QUEUE.md` line 127).
> - `GER1. Comprehensive geriatric assessment` and `GER2. Geriatric syndromes` appear **only in v2**, and both have files on disk.
> - **`P2` appears nowhere in v2, and in no wikilink anywhere in the corpus.**
>
> So **`GER` is current and `P2` is superseded.** The hazard the rename creates is real but
> points the other way: a session reading **v1** would look for `P2`, find no file, and rebuild
> geriatrics content that already exists as `GER1`/`GER2`. **v2 is the authoritative queue.**

## Three authorities, and what each is authoritative for

| Source | Authoritative for |
|---|---|
| `00_BUILD_QUEUE_v2.md` | **planning** — cluster codes, names, parts, week ordering |
| filenames on disk | **what exists** — 37 clinical files |
| `00_BUILD_QUEUE.md` (v1) | **superseded.** Retained for the P2→GER history and its totals line only |

## Prefixes on disk vs queue phases

| Prefix | Files | In v2 as |
|---|---|---|
| `A` | 10 | referenced as **BUILT** (`[[A1]]`…`[[A10]]`), not as cluster definitions |
| `B` | 6 | referenced as **BUILT** (`[[B1]]`…`[[B6]]`) |
| `C` | 7 | cluster definitions `C1.`–`C7.` (parts still to build) |
| `D` | 7 | cluster definitions `D1.`–`D7.` |
| `F0` | 5 | referenced as BUILT — **except `F0.4`, which appears in no v2 reference** |
| `GER` | 2 | cluster definitions `GER1.`, `GER2.` |

**No prefix on disk is missing from v2**, once BUILT-references are counted as well as cluster
definitions. The earlier appearance that `A`, `B` and `F0` were absent was an artefact of
matching only `**Code. Name**` definitions — the queue lists built clusters differently from
unbuilt ones.

## The 191 unbuilt-target links → their queue clusters

**47 of 50 codes resolve to a named v2 cluster (188 links).** Use the cluster name verbatim in
the Step 31 marker — never a topic inferred from surrounding prose:

```
`TODO:link — J4 Paraproteins & hyperviscosity (unbuilt)`
```

| Code | Links | Cluster name (v2, authoritative) |
|---|---|---|
| `P1` | 14 | Preventive & occupational health |
| `P3` | 13 | Safeguarding & forensic |
| `O6` | 11 | Sexual & reproductive health |
| `L4` | 9 | Back & neck pain |
| `N6` | 9 | Dissociation & somatic |
| `E1` | 7 | Red & painful eye |
| `H4` | 7 | Scrotum, groin & loin |
| `M5` | 7 | Paediatric GI, GU & limb |
| `O2` | 7 | Later pregnancy & fetal |
| `N1` | 6 | Risk assessment & suicidality |
| `F3` | 5 | Throat, voice & oral |
| `J2` | 5 | Haemoglobinopathy & haemolysis |
| `J3` | 5 | Bleeding & thrombosis |
| `J5` | 5 | Oncology & palliative |
| `N8` | 5 | Eating & body image |
| `O1` | 5 | Early pregnancy |
| `J4` | 4 | Paraproteins & lymphoproliferative |
| `O5` | 4 | Pelvic & vulval |
| `F1` | 3 | Ear |
| `F4` | 3 | Neck lumps & facial pain |
| `H2` | 3 | LUTS, retention & incontinence |
| `I1` | 3 | Thyroid |
| `I2` | 3 | Glucose |
| `I5` | 3 | Weight, lipids & fluid balance |
| `J1` | 3 | Cytopenias & marrow failure |
| `L3` | 3 | Muscle symptoms & widespread pain |
| `M3` | 3 | Neonatal problems |
| `N4` | 3 | Mood |
| `AU1` | 2 | Australian health context |
| `COM1` | 2 | Communication & consultation skills |
| `G5` | 2 | Lumps, ulcers & nails |
| `H3` | 2 | Urine output & renal injury |
| `K2` | 2 | Skin & soft tissue infection |
| `L6` | 2 | Soft tissue injury & mobility |
| `L8` | 2 | Facial, head & torso trauma |
| `M2` | 2 | Fever in children |
| `N3` | 2 | Psychosis |
| `O7` | 2 | Breast |
| `P6` | 2 | Procedure addendum |
| `H1` | 1 | Haematuria & proteinuria |
| `I3` | 1 | Calcium, bone & parathyroid |
| `K3` | 1 | Exposure & immunodeficiency |
| `L5` | 1 | Regional limb pain |
| `M1` | 1 | The seriously unwell child |
| `M7` | 1 | Adolescent & behavioural |
| `O4` | 1 | Abnormal & menstrual bleeding |
| `P4` | 1 | Drug-class addendum |

### 3 codes are NOT in the queue — these are the real malformed links

| Link | Links | What it looks like |
|---|---|---|
| `[[13_ENT]]` | 1 | a truncated filename, not a cluster code |
| `[[15_Paeds]]` | 1 | a truncated filename, not a cluster code |
| `[[Shock_Phenotypes]]` | 1 | a truncated filename, not a cluster code |

These are **not** `TODO:link` candidates. They are broken wikilinks to files that exist and
should be repaired to the full filename during Step 31, and each must be read in context first.
