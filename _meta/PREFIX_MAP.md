---
name: prefix-map
description: Corpus B's code scheme — which prefixes exist on disk, which are queue phases, the P2 -> GER rename, and the cluster name every unbuilt code resolves to. Authoritative source for Step 31's TODO markers and Step 29's retargeting.
---

# Corpus B prefix and cluster map

Measured 2026-08-30 against `00_BUILD_QUEUE.md` (v1), `00_BUILD_QUEUE_v2.md` (v2) and the files on disk.

## Two DISTINCT relationships — do not conflate them

Build queue v2 (2026-08-30) creates Phase `GER` through **two different mechanisms**. They
look alike in a code list and are not the same thing.

### 1. RENAME — six clusters moved from Phase P / COM into Phase GER

Same content, new code. **A marker naming the old code must be updated to the new one.**

| v1 code | v2 code | Cluster |
|---|---|---|
| `P1` | **`GER3`** | Preventive & occupational health |
| `P3` | **`GER4`** | Safeguarding & forensic |
| `COM1` | **`GER5`** | Communication & consultation skills |
| `P4` | **`GER6`** | Drug-class addendum |
| `P5` | **`GER7`** | Investigation & lab addendum |
| `P6` | **`GER8`** | Procedure addendum |

### 2. EXPANSION — `GER1` and `GER2` are NEW, not renamed from anything

v2 marks §3.3 **"(EXPANDED — beyond `bl.md`)"** and both clusters **BUILT**. Geriatrics went
from *2 items in `bl.md`* to a proper block. **`GER1`/`GER2` have no v1 predecessor.**

> [!danger] **`P2` is not the predecessor of `GER1`/`GER2`.** `P2. Geriatric assessment &
> frailty` existed in v1 and is simply **gone** in v2 — absorbed into the expansion, not
> renamed into it. An earlier instruction to this project asserted "GER is the old prefix,
> superseded by P2", which is **backwards on both counts**: `GER` is current, and `P2` was
> never its successor. Recorded as measured so a later session does not re-invert it.
>
> **Why conflating the two matters:** a rename means *update the reference*; an expansion
> means *there was no earlier reference to update*. Treating `GER1` as a renamed `P2` would
> send a session looking for v1 content that was never there.

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
| `F0` | 5 | referenced as BUILT — **except `F0.4`, which appears in no v2 reference at all** |

> [!note] The full class — `A5`, `F0.4`, the inherited `0.7`, the `GER` rename and
> `CF-012` — is consolidated in `_meta/FALSE_ESTABLISHED_REFERENCES.md`.

> [!warning] **`F0.4` is a missing-from-the-index defect, same class as `A5`'s missing queue
> row.** `F0-4_Resuscitation_Algorithms_and_Emergency_Procedures` exists on disk and every
> other `F0` file is referenced in v2. The queue reads as complete because nothing is missing
> *from view* — only enumerating the filesystem and subtracting the index reveals it.
> Recorded in §1.1.9.2's failure-class table. **Not fixed:** the build queues are Corpus B
> content and are edited by the author, not by a session.
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
