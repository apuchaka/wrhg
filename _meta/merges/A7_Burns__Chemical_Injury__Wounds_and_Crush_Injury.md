---
name: A7 destination table
description: Where every section of Corpus B/A7_Burns__Chemical_Injury__Wounds_and_Crush_Injury.md goes, including the sections that were discarded.
bfile: Corpus B/A7_Burns__Chemical_Injury__Wounds_and_Crush_Injury.md
built: 2026-08-31
---

# A7_Burns__Chemical_Injury__Wounds_and_Crush_Injury — destination table

Committed **before** any content was written. 4 417 words, 6 sections.
**1 placement · 5 discards. 19 of 20 concepts tested were already present** — the most
completely superseded file of the run.

The contrast with A6 is the point: **A6 and A7 sit in the same B-block and the same
destination file, and one filled a missing domain while the other adds a single sentence.**
Corpus A's `11_09b_Ortho_-_Trauma` §Burns and Scalds is thorough — Parkland, rule of nines,
Lund and Browder, burn depth, referral criteria, escharotomy, inhalation injury, urine
output targets — and the wound, crush and compartment material is spread across `11_09b`,
`07_Renal` and `12_04_Rheum`.

## Instrument comparison run first

`inventory.py --compare` against `11_09b` returned **10 candidates in A7 and not in it** —
`Compartment syndrome`, `DIC`, `MCP`, `PPE`, `QRS`, `SDS`, plus prose noise (`BEFORE`,
`INJURY`) and two unbuilt B-file codes (`GER3`, `GER4`). Every one was checked; all the
clinical ones are present elsewhere in the vault.

## Results

| Concept | Verdict |
|---|---|
| **acids cause coagulative necrosis, alkalis cause liquefactive necrosis — so alkali burns are worse** | **absent, both trees** |
| Parkland, TBSA, rule of nines, Lund and Browder, burn depth, burns unit referral, escharotomy, inhalation injury, urine output target, chemical irrigation, hydrofluoric acid and calcium gluconate, chemical eye injury and pH, tetanus prophylaxis, primary vs delayed closure, bite wounds, retained foreign body, crush syndrome, reperfusion, myoglobin and AKI, hyperkalaemia, compartment syndrome, fasciotomy | **present, both trees** |

**The `alkali` search returned four hits and none were burns** — calcium phosphate and
struvite renal stones in `07_Renal`, urinary alkalinisation, and alkali replacement in
renal tubular acidosis. Four hits, one word, an entirely different organ system.

## Destination table

| A7 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Burns assessment | — | **DISCARD** — `11_09b` §Burns and Scalds |
| 0.2 | Burns resuscitation | — | **DISCARD** — same |
| 0.3 | Chemical burns | `Corpus A/11_09b_Ortho_-_Trauma.md` §Burns and Scalds | **PARTIAL** — the acid/alkali mechanism only; irrigation and hydrofluoric acid are present |
| 0.4 | Chemical eye injury | — | **DISCARD** — `05_Ophthalmology` owns it, with pH checking |
| 0.5 | Minor traumatic wound | — | **DISCARD** — tetanus, closure timing, bite wounds and retained foreign body all present |
| 0.6 | Crush injury and rhabdomyolysis | — | **DISCARD** — crush syndrome, reperfusion, myoglobin, hyperkalaemia, compartment syndrome and fasciotomy all present |

No new file required. **No `CONFLICT` raised.**
