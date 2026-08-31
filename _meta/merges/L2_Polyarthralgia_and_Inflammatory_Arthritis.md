---
name: L2 destination table
description: Where every section of Corpus B-new/L2_Polyarthralgia_and_Inflammatory_Arthritis.md goes, including the sections that were discarded.
bfile: Corpus B-new/L2_Polyarthralgia_and_Inflammatory_Arthritis.md
built: 2026-08-31
---

# L2_Polyarthralgia_and_Inflammatory_Arthritis — destination table

**31 concepts tested · 30 present · 1 absent.**
**Additive/discard ratio: 1 additive / 30 discard = 3% additive.** Rheumatology is covered
by five Corpus A files (`12_01`–`12_04`, `11_*`) and three Corpus C files
(`NEW_Rheumatology_and_Immunology`, `NEW_Investigations_Rheumatology`,
`NEW_Drugs_19_Rheumatological`), and between them they carry almost all of this.

## Two findings from the searches themselves

> [!danger] **`pulmonary-renal` returned 0 — and the syndrome is present TWICE, with an
> EN-DASH.** `pulmonary–renal` is at `NEW_Investigations_Infectious_Diseases:436` and
> `NEW_Investigations_Rheumatology:49`, both as same-day-referral `[!danger]` callouts.
> **The automated retry could not find it either** — it derived `pulmonary` (233 hits) and
> `renal` (768), both too common to read. **The tool said INCONCLUSIVE rather than
> negative**, which is the only reason this was not merged as a duplicate; the narrowed
> component search it asked for (`Goodpasture` 3, `anti-GBM` 9) settled it immediately.
> That distinction was added to `gapcheck.py` an hour earlier, prompted by this same query.
> **Third en-dash false-ABSENT of this run**, after `warm-cold` in the week 2 verification.

> [!warning] **`ANA` returned 2111 hits** — `management` ×465, `anaemia` ×316, `Anaemia`
> ×168, `Anaesthetics` ×162, `Management` ×128, `analgesia` ×124. **The largest substring
> trap found in this project.** The real ANA content is at `12_02:67` and
> `NEW_Investigations_Rheumatology`.

## Destination table

| L2 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Inflammatory vs mechanical; pattern characterisation | — | **DISCARD** — `NEW_Rheumatology_and_Immunology:25–27` |
| 0.1 | Acute symmetrical polyarthritis under six weeks is often viral | — | **DISCARD** — 24 `parvovirus` hits, 65 `self-limiting`; `NEW_Rheumatology_and_Immunology:25` names parvovirus B19, hepatitis B and C, EBV and the Australian alphaviruses |
| 0.2 | RA: extra-articular disease, red flags | — | **DISCARD** — `12_01:75` Complications / extra-articular manifestations |
| 0.2 | **Atlantoaxial subluxation — flag before any anaesthetic** | — | **DISCARD** — `NEW_Investigations_Orthopaedics_Neurology_and_Other:206`: *"relevant before any airway management"*, and `04_Neurology:636` |
| 0.2 | Methotrexate weekly dosing error | — | **DISCARD** — 46 `methotrexate` hits; `NEW_Drugs_19:41` carries **ONCE WEEKLY** in capitals |
| 0.2 | **The window of opportunity — early treatment changes the ceiling** | `Corpus A/12_01_Rheum…` | **ADDITIVE** — 31 `DMARD` hits and **not one** mentions early, prompt, window or delay. The principle exists in the vault **only for psoriatic arthritis**, at `NEW_Drugs_08_Dermatological:168`, inside a dermatology drug entry |
| 0.3 | Spondyloarthropathy family; inflammatory back pain criteria; Schober | — | **DISCARD** — `12_02:0.1`, 7 `Schober` hits |
| 0.3 | **A fused spine fractures with trivial trauma and the fracture is unstable** | — | **DISCARD** — `NEW_Exam_Manoeuvres_and_Procedures:310` states it |
| 0.3 | Acute anterior uveitis needs same-day ophthalmology | — | **DISCARD** — 37 `uveitis` hits |
| 0.3 | Psoriatic arthritis patterns; the hidden psoriasis | — | **DISCARD** — `NEW_Dermatology:38` lists scalp, behind the ears, umbilicus, **natal cleft**, nails, palms and soles |
| 0.4 | SLE; Sjögren; systemic sclerosis | — | **DISCARD** — `12_03_Rheum` owns all three |
| 0.4 | **Scleroderma renal crisis** | — | **DISCARD** — `NEW_Investigations_Rheumatology:95`, as a hypertensive emergency with its treatment |
| 0.4 | **Antiphospholipid syndrome — the anticoagulant choice** | — | **DISCARD** — `NEW_Drugs_06:39`: *"DOACs are CONTRAINDICATED in mechanical heart valves and in antiphospholipid syndrome"* |
| 0.4 | Raynaud, primary vs secondary; nailfold capillaroscopy | — | **DISCARD** — 2 `nailfold` and 1 `capillaroscopy` hits |
| 0.5 | Vasculitis by vessel size; red flags; Behçet | — | **DISCARD** — `12_04_Rheum_-_Vasculitis`; `Behçet` 8 hits |
| 0.5 | **Pulmonary-renal syndrome is an emergency** | — | **DISCARD** — see the en-dash finding above |
| 0.6 | Order antibodies to CONFIRM, never to screen | — | **DISCARD** — `Investigation-Interpretation:397`: *"autoimmune markers should always be interpreted in the context of clinical suspicion, not used as a screening panel"*, and `NEW_Investigations_Rheumatology:151` |
| 0.6 | ESR and CRP are not interchangeable; discordance is informative | — | **DISCARD** — `Investigation-Interpretation:518–520`, already used to discard a K1 claim |

## NO-BASELINE

`window of opportunity` returns 0 in Corpus A and C at base-A.

## New files

**None.**
