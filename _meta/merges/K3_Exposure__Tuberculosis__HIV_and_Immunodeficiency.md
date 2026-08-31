---
name: K3 destination table
description: Where every section of Corpus B-new/K3_Exposure__Tuberculosis__HIV_and_Immunodeficiency.md goes, including the sections that were discarded.
bfile: Corpus B-new/K3_Exposure__Tuberculosis__HIV_and_Immunodeficiency.md
built: 2026-08-31
---

# K3_Exposure__Tuberculosis__HIV_and_Immunodeficiency — destination table

**48 concepts tested · 40 present · 7 absent · 1 deferred.**
**Additive/discard ratio: 7 additive / 40 discard = 15% additive.** The most superseded
file of the three so far — Corpus A and C between them own TB, HIV and pre-immunosuppression
screening thoroughly.

## Acronym collisions — THREE new ones, all severe, all in this file's searches

| Pattern | Hits | What it actually matched |
|---|---:|---|
| `IGRA` | 125 | **`migraine` ×57, `Migraine` ×12, `migration` ×13, `migrans` ×8, `migratory` ×5, `scintigraphy` ×4, `nigra` ×3, `migrates`/`migrate` ×6.** **7 real.** |
| `PrEP` | 113 | **`preparations` ×42, `preparation` ×26, `prepared` ×7, `prepare` ×6, `prepares` ×4, `prepuce` ×3.** **~15 real.** |
| `IRIS` | 19+ | **the eye `iris` ×18.** 4 real — the syndrome is at `04_Neurology:711`. |

With `felon`→`lifelong` (66/66) from K2, that is **four unanchored-substring traps in one
night**, three of them returning three-figure hit counts for terms that are largely or
entirely absent. **A high hit count is the least reliable signal in this corpus**, because
the commonest English and clinical words are the ones most likely to contain a short
acronym.

## Destination table

| K3 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | **Sharps and splash first aid — wash, and what NOT to do** | `Corpus A/08_05-06_Infectious_Disease_-_Viral_Infections.md` | **ADDITIVE** — 17 `squeeze` hits, **not one about a wound**; the corpus goes straight from exposure to PEP with nothing in between |
| 0.1 | Risk assessment; transmission risk hierarchy | — | **DISCARD** — `08_05-06:186` and `History-Taking:519` |
| 0.1 | Hepatitis B — anti-HBs status governs immunoglobulin vs vaccination | — | **DISCARD** — 8 `anti-HBs` hits including `03_Gastrointestinal:381`'s serology block |
| 0.1 | **Hepatitis C has NO post-exposure prophylaxis — surveillance instead** | `Corpus A/08_05-06` | **ADDITIVE** — 0 hits pairing PEP with hepatitis C anywhere. The absence of a prophylaxis is itself the teaching point, and an absence cannot be found by reading around |
| 0.1 | HIV PEP within hours, 72h outer limit, 28 days | — | **DISCARD** — `08_05-06:186` states all three, and notes cabotegravir is TGA-approved but not PBS-subsidised |
| 0.2 | PrEP — tenofovir/emtricitabine | — | **DISCARD** — same block |
| 0.2 | **NPEP as a distinct non-occupational pathway** | `Corpus A/08_05-06` | **ADDITIVE** — `NPEP` 0 hits. The corpus has occupational and sexual exposure collapsed into one PEP paragraph |
| 0.2 | Adult sexual assault pathway | — | **DEFERRED to `GER4_Safeguarding_and_Forensic` (Week 5)**, not discarded. `15_24a` owns the paediatric pathway; `Corpus C/NEW_Safeguarding_and_Forensic` is a stub that states no topic matched any header. Merging K3's generic version now would duplicate what GER4 carries in depth |
| 0.3 | Latent vs active; screen before immunosuppression; isolation; sputum ×3; Xpert; CXR; tissue | — | **DISCARD** — `02_Respiratory:0.9` and `NEW_Investigations_Respiratory:0.7` own TB and its screening |
| 0.3 | Four first-line drugs and their toxicities, pyridoxine with isoniazid | — | **DISCARD** — 15 `pyridoxine`, 6 `ethambutol`, 5 `pyrazinamide`, 41 `rifampicin` |
| 0.4 | HIV testing offered widely; seroconversion illness; CD4 stratification; PJP, toxoplasmosis, cryptococcal, CMV retinitis | — | **DISCARD** — `08_05-06:166`, `04_Neurology` CNS Infections Associated with Immunosuppression |
| 0.4 | ART immediately regardless of CD4; U=U | — | **DISCARD** — both present |
| 0.5 | Categories of primary immunodeficiency; asplenia | — | **DISCARD** — `08_09:108` post-splenectomy sepsis, `10_07_Haemonc` |
| 0.5 | **Terminal complement deficiency → recurrent neisserial infection** | `Corpus A/08_09` | **ADDITIVE** — `neisserial` 0 hits in either case. The corpus has the *acquired* version (eculizumab → meningococcal, `NEW_Drugs_07:122`) and not the inherited one, so a young adult with a second meningococcal episode has nothing pointing at a complement screen |
| 0.5 | Pre-immunosuppression screening: latent TB, hep B core antibody, HIV, VZV, *Strongyloides*, live vaccines first | — | **DISCARD** — four Corpus C files carry this as a standing danger callout, including the Australian *Strongyloides*-before-steroids warning at `NEW_Drugs_05:41` |
| 0.6 | Ross River, Barmah Forest, MVE, JE, dengue, malaria | — | **DISCARD** — merged from K1 this run, plus `NEW_Rheumatology_and_Immunology:25` |
| 0.6 | **Queensland tick typhus and Flinders Island spotted fever** | `Corpus A/08_01-03_Infectious_Disease_-_Bacterial_Infections.md` | **ADDITIVE** — all 7 `Flinders` hits are the South Australian institution in localisation notes. The *Australian* rickettsioses are absent; K1's merge added the eschar sign without naming them |
| 0.6 | Lyme — not locally acquired in Australia | — | **DISCARD** — `08_01-03:173`, **verified against the Australian CDC**, and `NEW_Cardiology_and_Vascular:77` |
| 0.6 | Q fever, leptospirosis, brucellosis, melioidosis, bat lyssavirus, hydatid | — | **DISCARD** — `08_01-03` owns the first three; the last two merged from K1/K2 this run |
| 0.6 | **Hendra virus** | `Corpus A/08_01-03` | **ADDITIVE** — 0 hits. Queensland and northern NSW, horses and the people who treat them |
| 0.6 | **Psittacosis** | `Corpus A/08_01-03` | **ADDITIVE** — 0 hits. An atypical pneumonia with a bird exposure that is only found by asking |

## NO-BASELINE — Corpus A and C at base-A only

**Hendra · psittacosis · neisserial · NPEP** all return 0. The sharps first-aid block is
**not** marked (`squeeze` has base-A hits, wrong sense).

## New files

**None.**
