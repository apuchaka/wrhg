---
name: K2 destination table
description: Where every section of Corpus B-new/K2_Skin_and_Soft_Tissue_Infection.md goes, including the sections that were discarded.
bfile: Corpus B-new/K2_Skin_and_Soft_Tissue_Infection.md
built: 2026-08-31
---

# K2_Skin_and_Soft_Tissue_Infection — destination table

Committed **before** any content was written. 267 lines, 6 sections.
**42 concepts tested · 28 present · 13 absent · 1 partial.**
**Additive/discard ratio: 13 additive / 28 discard = 32% additive.**

## Acronym collisions reported up front

`inventory.py` over `08_09` and `09_05`. Beyond K1's collisions, three are **my own K1
merge coming back**: `ESCHAR`, `LOOK` and `BASELINE` are now returned as acronyms because
I wrote *"LOOK FOR THE ESCHAR"* in capitals and placed `NO-BASELINE` markers. Dismissed
per rule 3 — but worth recording, because merging into a file makes the next inventory of
that file report your own prose back at you.

Genuine instruments present: **Eron classification (in both destinations) · LRINEC ·
Kanavel's cardinal signs (`11_01_Ortho_-_Orthopaedic_Emergencies:175`) · HACEK · GAS/ARF**.

> [!danger] **`felon` matched `lifelong` — 66 times out of 66.**
> `l-i-**f-e-l-o-n**-g`. The gapcheck reported **62 hits in Corpus A and C** for a term
> that is **completely absent from the corpus**, and every one of them was the word
> *lifelong* inside prophylaxis-duration and immunosuppression sentences. A count-only
> reading calls felon present with high confidence. This is rule 9's cleanest instance
> yet found in this project and belongs with `ASCIA` inside `fascia`.

## Destination table

| K2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Cellulitis/erysipelas definition, portal of entry, toe-web, risk factors | — | **DISCARD** — `08_09:20–24` |
| 0.1 | Eron classification; purulent vs non-purulent antibiotic choice | — | **DISCARD** — `08_09:44–56`, **verified against Queensland Health and the 2025 eTG update**. B carries no source (§1.10) |
| 0.1 | Bilateral "cellulitis" is usually venous stasis / lipodermatosclerosis | — | **DISCARD** — already an additive block at `08_09:25` from `SRC:B6` |
| 0.1 | Mimics: DVT, gout/pseudogout, contact dermatitis, thrombophlebitis, erythema nodosum | — | **DISCARD** — 27 `pseudogout`, 11 `thrombophlebitis`, `09_08:61` panniculitis/erythema nodosum |
| 0.1 | **Calciphylaxis as a cellulitis mimic in dialysis** | `Corpus A/08_09` Cellulitis | **ADDITIVE** — 0 hits vault-wide |
| 0.1 | **Mark the border and write the time on the skin** | `Corpus A/08_09` Cellulitis | **ADDITIVE** — 11 `demarcat` hits: subconjunctival haemorrhage, fixed drug eruption, psoriasis, alopecia areata, lichen planus, neonatal harlequin colour change, dithranol plaques. None is tracking a cellulitis margin |
| 0.1 | Lymphoedema–cellulitis vicious cycle | — | **DISCARD** — `NEW_Investigations_Haematology_Part2:334`: *"CELLULITIS IS THE MAJOR COMPLICATION OF LYMPHOEDEMA and it is recurrent"* |
| 0.1 | Prophylactic antibiotics for recurrent cellulitis | — | **PARTIAL** — the risk factors are present, the prophylaxis decision is not; K2 marks its own regimen `UNVERIFIED` and the source is login-gated. **Not merged** rather than merging an unsourced regimen |
| 0.2 | NF types I–IV, Fournier, pain out of keeping, late signs, imaging must not delay, repeat debridement, mortality | — | **DISCARD** — `08_09:85–107` carries all of it, plus a fourth (fungal) type K2 does not have |
| 0.2 | ***Vibrio vulnificus* — seawater and raw shellfish, and the host who gets it** | `Corpus A/08_09` Necrotising fasciitis | **ADDITIVE** — `vulnificus` 0 hits. `08_09` Type 3 says *"fresh-water infection (rare) — e.g. Vibrio species"*; the **chronic liver disease and haemochromatosis** susceptibility, which is what makes it predictable, is absent |
| 0.2 | An agent that suppresses toxin production | — | **DISCARD** — 26 `clindamycin` hits; the agent is not named here without a source |
| 0.3 | Incision and drainage is the treatment; recurrent boils | — | **DISCARD** — `09_05` Folliculitis covers furuncle and carbuncle |
| 0.3 | Hidradenitis suppurativa is not an infection | — | **DISCARD** — its own section at `09_07_Dermatology…:75`, plus `NEW_Drugs_08:228` |
| 0.3 | Flexor tenosynovitis and Kanavel's signs | — | **DISCARD** — `11_01_Ortho_-_Orthopaedic_Emergencies:175` |
| 0.3 | **Felon and paronychia** | `Corpus A/11_01_Ortho_-_Orthopaedic_Emergencies.md` | **ADDITIVE** — `paronychia` 0 hits; `felon` 62 hits, **all `lifelong`** (see above) |
| 0.3 | Perianal, breast, pilonidal, dental abscess; abscess in people who inject drugs | — | **DISCARD** — `08_09:57` Mastitis and Breast Abscess, `03_Gastrointestinal:0.22` Pilonidal Disease, `C6` anorectal |
| 0.4 | **Nodular lymphangitis as a pattern** — sporotrichosis, *M. marinum*, *Nocardia*, tularaemia | `Corpus A/09_05_Dermatology…` | **ADDITIVE** — `sporotrichosis` 1 hit, inside an **antifungal indication list**; `Nocardia` 2 hits, inside a **co-trimoxazole indication list**; `marinum` and `tularaemia` 0. The pattern itself is absent, and three of the four organisms exist only as drug indications |
| 0.4 | **Suppurative lymphadenitis; tuberculous cervical lymphadenitis (scrofula)** | `Corpus A/08_09` | **ADDITIVE** — `scrofula` 0; both `lymphadenitis` hits are ENT/neurological (`04_Neurology:641`, `13_05a:17`) |
| 0.4 | Cat scratch disease; malignancy in a persistent node; melioidosis | — | **DISCARD** — `08_01-03:52` *Bartonella henselae*; melioidosis merged from K1 this run |
| 0.5 | *Pasteurella* (cat), *Eikenella* (human), fight bite, irrigation, do not close primarily, tetanus | — | **DISCARD** — `08_09:11–15` Animal & human bites |
| 0.5 | ***Capnocytophaga canimorsus* — fulminant sepsis after a dog bite in the asplenic** | `Corpus A/08_09` Animal & human bites | **ADDITIVE** — 0 hits. The asplenia link matters: `08_09:108` owns post-splenectomy sepsis and does not name this organism |
| 0.5 | **Australian bat lyssavirus — any bat contact needs assessment** | `Corpus A/08_09` Animal & human bites | **ADDITIVE** — 1 hit, inside the NNDSS quarantinable list at `08_01-03:335` as *"rabies/lyssaviruses"*. Named on a list, so it reads as covered; the clinical action is absent |
| 0.5 | ***Mycobacterium ulcerans* — Buruli / Bairnsdale ulcer** | `Corpus A/09_05_Dermatology…` | **ADDITIVE** — `Buruli`, `Bairnsdale` and `ulcerans` all 0. A Victorian and Queensland coastal disease absent from an Australian corpus |
| 0.5 | **Occupational: erysipeloid and orf** | `Corpus A/09_05_Dermatology…` | **ADDITIVE** — `erysipeloid` 0; all 7 `orf` hits are substrings, not the disease |
| 0.5 | Q fever, brucellosis, tetanus, leptospirosis, *Nocardia* by exposure | — | **DISCARD** — each owned in `08_01-03` |
| 0.6 | Scabies: treat all contacts, whole body, repeat, laundry, itch persists | — | **DISCARD** — `09_05:62` Scabies and `NEW_Drugs_08` |
| 0.6 | Crusted (Norwegian) scabies and its ATSI public health significance | — | **DISCARD** — `NEW_Drugs_08:198`, which already carries the remote-community framing |
| 0.6 | Head lice | — | **DISCARD** — `09_05:42` |

## NO-BASELINE — tested against **Corpus A and Corpus C at base-A only**

**A scope error of my own, caught and corrected before any marker was written.** My first
base-A test grepped everything `git archive 0db4034` produced — which includes **Corpus B,
the merge source**, and the repo's root documents. A base-A "hit" from Corpus B would have
suppressed a NO-BASELINE marker on the exact ground that the *source* mentions it, which is
the self-match trap one level up. Restricted to `Corpus A` + `Corpus C`:

**NO-BASELINE (0 hits):** calciphylaxis · *V. vulnificus* · *Capnocytophaga* · Buruli /
*M. ulcerans* · *M. marinum* · scrofula · erysipeloid · tularaemia · paronychia · felon.

**Not marked** — a base-A hit exists in A or C, wrong sense though it is: sporotrichosis
(1), *Nocardia* (2), lyssavirus (1).

`paronychia` is the case that shows the scope error mattered: **1 hit across the whole
base-A archive, 0 in Corpus A and C.** The hit is in a root project document, not in the
inherited clinical layer.

## New files

**None.** All four destinations are existing sections.
