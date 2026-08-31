---
name: RESP-X destination table
description: Where every section of Corpus B-new/RESP-X_Occupational_and_Chronic_Lung_Disease.md goes, including the sections that were discarded.
bfile: Corpus B-new/RESP-X_Occupational_and_Chronic_Lung_Disease.md
built: 2026-08-31
---

# RESP-X_Occupational_and_Chronic_Lung_Disease — destination table

**26 concepts tested · 25 present · 1 absent.**
**Additive/discard ratio: 1 additive / 25 discard = 4% additive.**

`02_Respiratory` is one of the strongest files in the vault on exactly this material, and
several of the "Australian" points RESP-X leads with are already there in more detail.

> [!danger] **A truncation near-miss, the third of this run.**
> Checking whether the venous-bicarbonate screen for obesity hypoventilation was present, I
> piped the gapcheck output through `cut -c1-190`. **The sentence that answers the question
> is the last one on the line:** `NEW_Investigations_Respiratory:106` ends *"Look for a
> raised bicarbonate on daytime bloods as the clue."* The cut removed it and I nearly
> recorded a duplicate.
> With `RICE` cut off by `head -4` in L6, that is **two truncations in one week-3 block**,
> both in *filter* greps run over gapcheck's own untruncated output — which is precisely
> the hole rule 10's hard prohibition is meant to close. `gapcheck.py` cannot truncate; a
> `cut` downstream of it can, and does.

## Destination table

| RESP-X § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | ILD clinical signature and classification | — | **DISCARD** — `02_Respiratory`, 33 `pneumonitis` hits |
| 0.1 | **IPF — steroids are the wrong reflex** | — | **DISCARD** — 2 `nintedanib` and 2 `pirfenidone` hits; the antifibrotic-not-immunosuppressant point is carried |
| 0.1 | Hypersensitivity pneumonitis; the drugs that cause ILD; CTD-ILD and sarcoidosis | — | **DISCARD** — `02_Respiratory:328` lists hypersensitivity pneumonitis in the upper-zone differential; `12_03_Rheum` and `NEW_Drugs_19` own the drug and CTD causes |
| 0.2 | Ask the occupational history — systematically not taken | — | **DISCARD** — `02_Respiratory:809`: *"occupational history is central to diagnosis"*; `History-Taking:520` |
| 0.2 | **Accelerated silicosis from engineered stone — an Australian public health failure** | — | **DISCARD** — `02_Respiratory:805` names *"crystalline silica dust (mining, stonework, engineered stone/benchtop cutting — a recognised and increasing cause of severe disease)"*, and `:813` adds the TB reactivation surveillance |
| 0.2 | Occupational asthma; the other occupational lung diseases; the obligations that follow | — | **DISCARD** — `02_Respiratory:0.20` Pneumoconioses |
| 0.3 | Asbestos: the benign-to-malignant spectrum; mesothelioma; Australia's exposure history | — | **DISCARD** — 16 `asbestos` and 7 `mesothelioma` hits |
| 0.4 | Bronchiectasis: look for a cause; airway clearance | — | **DISCARD** — 29 `bronchiectasis` hits, `02_Respiratory` Bronchiectasis |
| 0.4 | **Bronchiectasis in Aboriginal and Torres Strait Islander communities** | — | **DISCARD** — `02_Respiratory:281–285` is a fuller treatment than RESP-X's, with the **20-year mortality gap** and the **weekly azithromycin** evidence base |
| 0.5 | OSA; STOP-BANG; the consequences; **driving obligations** | — | **DISCARD** — `02_Respiratory:0.18`, 2 `STOP-BANG` hits, 30 `Austroads` hits, and `NEW_Investigations_Respiratory:104` carries the statutory reporting point |
| 0.5 | **Obesity hypoventilation — check a venous bicarbonate** | — | **DISCARD** — `NEW_Investigations_Respiratory:106`, which also gives the bilevel-not-CPAP distinction. See the truncation note above |
| 0.6 | **Long-term oxygen therapy — narrow criteria, not a treatment for breathlessness** | — | **DISCARD in part** — the criteria are covered; the not-for-breathlessness half is folded into the additive block below rather than merged twice |
| 0.6 | Home non-invasive ventilation | — | **DISCARD** — `NEW_Investigations_Respiratory`, `02_Respiratory` |
| 0.6 | **Pulmonary rehabilitation is under-referred and works** | — | **DISCARD** — 36 `rehabilitation` hits including `02_Respiratory:813` |
| 0.6 | **Refractory breathlessness — what actually helps** | `Corpus A/02_Respiratory.md` | **ADDITIVE** — 31 `breathlessness` hits and **not one** pairs it with opioid, morphine, fan or refractory. `handheld fan` and `refractory breathlessness` both 0 in base-A |
| 0.6 | Advance care planning in chronic lung disease | — | **DISCARD** — folded into the same block as a cross-reference rather than merged separately |

## NO-BASELINE

The refractory-breathlessness block. Both search terms return 0 in Corpus A and C at base-A.

## New files

**None.**
