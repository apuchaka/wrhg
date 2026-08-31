---
name: K4 destination table
description: Where every section of Corpus B-new/K4_Allergy_and_Clinical_Immunology.md goes, including the sections that were discarded.
bfile: Corpus B-new/K4_Allergy_and_Clinical_Immunology.md
built: 2026-08-31
---

# K4_Allergy_and_Clinical_Immunology — destination table

**38 concepts tested · 25 present · 10 absent · 3 partial.**
**Additive/discard ratio: 10 additive / 25 discard = 29% additive.**

## A fifth substring trap

`Gell` (for the Gell and Coombs classification) returned **9 hits** — `flagellin`,
`flagellated`, `Shigella` ×3, `Salmonella` ×2, `trichomonads … flagellated`, and the
HACEK note. **Zero real.** Fifth of the night, after `felon`→`lifelong`,
`IGRA`→`migraine`, `PrEP`→`preparation`, `IRIS`→`iris`.

The user's own warning list for this run named `ASCIA` inside `fascia`. **Every one of
tonight's five is the same shape and none was on that list**, which is the argument for
treating a short unanchored pattern as suspect by default rather than keeping a list of
known-bad ones.

## Destination table

| K4 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | **Gell and Coombs types I–IV** | `Corpus A/09_01_Dermatology_-_Dermatological_Emergencies.md` | **ADDITIVE** — see above. 0 real hits |
| 0.1 | IgE-mediated vs non-IgE; anaphylaxis definition and management | — | **DISCARD** — `09_01:11` Anaphylaxis, `15_01b` paediatric, `NEW_Drugs_01` owns the ASCIA adrenaline table |
| 0.2 | Skin prick testing, specific IgE, component-resolved diagnostics | — | **DISCARD** — `NEW_Investigations_Rheumatology:213` and `:234` own both, including that specific IgE is unaffected by antihistamines |
| 0.2 | Serum tryptase timing | — | **DISCARD** — `15_01b:85` and `NEW_Drugs_01:195` |
| 0.3 | Penicillin allergy de-labelling; ~10% carry a label, most are not allergic | — | **DISCARD** — `NEW_Drugs_05:22` states it, Corpus C provenance beats B (§1.10) |
| 0.3 | Graded challenge and desensitisation | — | **PARTIAL** — 17 `challenge` and 3 `desensitis` hits exist; K4's protocol detail is not merged without a source |
| 0.4 | **Early introduction of allergenic solids to PREVENT food allergy** | `Corpus A/15_01b_Paeds_-_Anaphylaxis.md` | **ADDITIVE** — `solids` 0, `LEAP` 0, both `peanut` hits irrelevant (one is dimercaprol in peanut oil). An Australian preventive recommendation absent from an Australian corpus |
| 0.4 | **The atopic march as a sequence** | `Corpus A/15_01b` | **ADDITIVE** — `15_04b:82` says food allergy *"commonly emerges after or alongside eczema in infancy"*, which is two of the four steps and not named as a march |
| 0.4 | **FPIES** | `Corpus A/15_01b` | **ADDITIVE** — 0 hits. Non-IgE, so tests are negative, which is exactly why it is mislabelled sepsis |
| 0.4 | **Pollen-food (oral) allergy syndrome** | `Corpus A/15_01b` | **ADDITIVE** — 0 hits for `pollen-food`; the phrase search was refused and the single-word retry run |
| 0.5 | Allergic rhinitis | — | **DISCARD** — `13_04_ENT:59` |
| 0.6 | Acute urticaria and angioedema | — | **DISCARD** — `09_01:90` |
| 0.6 | Hereditary angioedema, C1 inhibitor, bradykinin | — | **DISCARD** — `10_09b:11–13` |
| 0.6 | ACE inhibitor angioedema, may start up to a year in | — | **DISCARD** — `01_Cardiovascular:1509` |
| 0.6 | **Bradykinin-mediated angioedema does not respond to adrenaline or antihistamine** | `Corpus A/09_01` | **ADDITIVE** — both mechanisms are present in separate files and **nothing states the treatment consequence**, which is the only part that changes what you do at 3am |
| 0.6 | **Chronic spontaneous urticaria — the >6-week definition, up-dosing, omalizumab** | `Corpus A/09_01` | **PARTIAL→ADDITIVE** — 1 `chronic urticaria` hit, inside a dermatology DDx list; 3 `omalizumab` hits, none for urticaria |
| 0.6 | Mastocytosis | — | **PARTIAL** — named at `15_01b:96` as an anaphylaxis risk co-factor only. Left as is; the entity belongs to haematology, not here |
| 0.7 | **Alpha-gal / tick-induced mammalian meat allergy** | `Corpus A/09_01` | **ADDITIVE** — 0 hits. Australian, and the delayed reaction is what makes it invisible |
| 0.7 | **Jack jumper ant venom immunotherapy** | `Corpus A/09_01` | **ADDITIVE** — `jumper` and `Myrmecia` both 0. A distinctly Australian anaphylaxis cause with an Australian-developed treatment |
| 0.7 | Immunotherapy generally, sublingual and subcutaneous | — | **DISCARD** — 15 `immunotherapy`, 11 `sublingual` hits |

## NO-BASELINE — Corpus A and C at base-A only

**All seven tested return 0:** alpha-gal · FPIES · jack jumper · *Myrmecia* · LEAP ·
Gell and Coombs · oral allergy syndrome.

## New files

**None.**

## Rule 5 note

`15_01b` is a **paediatric** file. The blocks merged into it state **no absolute quantity
of any kind** — no age in months, no gram weights, no dose. The ASCIA infant feeding
timing is left as an `UNVERIFIED` marker naming ASCIA, which is an open Australian source.
