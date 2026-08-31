---
name: L3 destination table
description: Where every section of Corpus B-new/L3_Muscle_Symptoms_and_Widespread_Pain.md goes, including the sections that were discarded.
bfile: Corpus B-new/L3_Muscle_Symptoms_and_Widespread_Pain.md
built: 2026-08-31
---

# L3_Muscle_Symptoms_and_Widespread_Pain — destination table

**26 concepts tested · 24 present · 2 absent.**
**Additive/discard ratio: 2 additive / 24 discard = 8% additive.**

## Two more substring traps, both three-figure

| Pattern | Hits | Matched | Real |
|---|---:|---|---:|
| `halo` | 148 | `encephalopathy` ×86, `haloperidol` ×16, `haloes` ×11, `cephalosporin(s)` ×18 | 3 |
| `PET` | 370 | `appetite`, `competent`, `petechiae` and the rest | few |

The GCA **halo sign** is genuinely present — found only by running the phrase with
`--allow-phrase` after the bare word returned unreadable noise, which is rule 10's
narrow-the-pattern instruction rather than a workaround.

## Destination table

| L3 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | "Weak" means four different things; the pattern narrows it | — | **DISCARD** — `04_Neurology` weakness entries, `Examination` |
| 0.1 | What a CK does and does not tell you; red flags | — | **DISCARD** — `04_Neurology:1403` and the myositis profile at `NEW_Investigations_Rheumatology:101` |
| 0.1 | **Steroid myopathy has a normal CK** | — | **DISCARD** — `04_Neurology:1403–1405`, an earlier D4 merge, with the metabolic-atrophy mechanism |
| 0.2 | PMR: the clinical picture, inflammatory markers, the steroid response, the mimics | — | **DISCARD** — `12_02:0.5` |
| 0.2 | Every PMR patient counselled about GCA | — | **DISCARD** — `12_02:73–74` and `12_04_Rheum_-_Vasculitis` |
| 0.3 | GCA: treat before you investigate; jaw claudication; large-vessel disease | — | **DISCARD** — `12_04:74`; 34 `claudication`, 2 `aortitis`, 6 `subclavian` hits |
| 0.3 | **Temporal artery ultrasound and the halo sign**; steroid-sparing therapy | — | **DISCARD** — `NEW_Investigations_Rheumatology:211` describes the halo as circumferential; 3 `tocilizumab` hits |
| 0.4 | The pattern that separates the myopathies | — | **DISCARD** — 87 `myopathy` hits, 6 `anti-Jo-1` |
| 0.4 | **Investigating asymptomatic hyperCKaemia** | `Corpus A/04_Neurology.md` | **ADDITIVE** — `hyperCKaemia` 0, base-A 0. The **auto-retry reported INCONCLUSIVE** (`Kaemia` matched 64 `-kaemia` words), and the narrowed search it demanded — all 10 `creatine kinase` hits read — confirmed the absence. The corpus says a normal CK does not exclude myopathy and says nothing about the commoner opposite problem |
| 0.5 | Fibromyalgia is central pain processing, not imaginary; the clinical picture | — | **DISCARD** — `12_02:0.6`, 19 `sensitisation` hits |
| 0.5 | Investigate once, appropriately, then stop | — | **DISCARD** — `12_02:0.6` |
| 0.5 | **Opioids are contraindicated in fibromyalgia and cause harm** | `Corpus A/12_02_Rheum…` | **ADDITIVE** — **173 `opioid` hits and not one is in a fibromyalgia line.** A contraindication missing from a file that already covers the condition thoroughly |
| 0.6 | Chronic fatigue; ME/CFS; post-exertional malaise; long COVID | — | **DISCARD** — `12_02:0.7`, 3 `post-exertional` and 25 `COVID` hits |

## NO-BASELINE

Both blocks. `hyperCKaemia` 0 in Corpus A and C at base-A; the opioid claim is absent as a
claim despite the word being everywhere.

## New files

**None.**
