---
name: Week 1 vault-wide claim audit — C4
description: Every claim in C4_Gastrointestinal_Bleeding tested against all of Corpus A and Corpus C. Report only.
built: 2026-08-31
status: REPORT ONLY — nothing merged
---

# C4_Gastrointestinal_Bleeding — vault-wide claim audit

**Extraction rule, verbatim:** one claim = one assertion that could independently be true or
false, and that a reader could act on differently.

```
claims extracted    81
PRESENT             61
WEAKER              10
ABSENT              10
```

## Claim density per section

| § | Topic | Claims |
|---|---|---:|
| 0.1 | Framework and resuscitation | 17 |
| 0.2 | Upper GI — non-variceal | 18 |
| 0.3 | Variceal bleeding | 15 |
| 0.4 | Lower GI bleeding | 12 |
| 0.5 | Occult, obscure, and iron deficiency | 19 |

## Merged blocks — clean, and one of them handled correctly in a way worth copying

Two blocks: `03_Gastrointestinal:272` (§0.6.7, variceal) and `:1365` (§0.33.4, ulcer stigmata
and the aspirin decision).

- `Forrest` **0 in base-A** — genuinely new.
- The **aspirin restart decision** is genuinely new: base-A contains **no** discussion of
  restarting aspirin or resuming it after a bleed.
- `Heyde` **0 in base-A** — but it was **not merged either**, so it stays absent (below).

**The §0.33.4 block is the model for how to handle an overlap.** Glasgow-Blatchford and
Rockall were *already* in base-A at `03_Gastrointestinal` §0.33.2 and at
`NEW_Gastroenterology_and_Hepatology:69`. Instead of restating them, the block writes:

> *"**AIMS65** is a further pre-endoscopy risk score alongside the Glasgow-Blatchford and
> Rockall scores **already at §0.33.2**."*

**That is the Barrett failure avoided.** It adds one score, names where the others live, and
does not reproduce them. Contrast the Barrett block, which asserted the destination "stops
before management" when the destination carried the management.

## The 10 ABSENT

| # | Claim | Weight |
|---:|---|---|
| 21 | **lesser curve gastric ulcers erode into the left gastric artery** | anatomy explaining why these bleed briskly. The *posterior duodenal → gastroduodenal artery* half is present |
| 28 | after endoscopic therapy for a high-risk ulcer, **PPI does reduce rebleeding** — that is where the benefit sits | the counterpart to the pre-endoscopy PPI claim, and the one that changes practice |
| 42 | **tissue glue for gastric varices, which do not band well** | a management step for a specific site |
| 50 | **a substantial proportion of bleeds in cirrhotic patients are from ulcers, not varices** — the source cannot be assumed | **anchoring trap**, and the reason endoscopy is diagnostic as well as therapeutic |
| 53 | **post-polypectomy bleeding** as a cause of lower GI haemorrhage | an iatrogenic cause, increasingly common |
| 60 | **Meckel's diverticulum bleeds from ectopic gastric mucosa ulcerating adjacent ileum** | Meckel's is present; the bleeding mechanism is not |
| 72 | **repeating the first gastroscopy and colonoscopy is often more productive than small bowel imaging** — a meaningful proportion of "obscure" bleeds were missed first time | a workup decision that saves an invasive test |
| 73 | **NSAID enteropathy** as a small bowel source | all `enteropathy` hits are coeliac, gluten or protein-losing |
| 74 | **Heyde syndrome** — aortic stenosis + angiodysplasia + acquired von Willebrand deficiency | 0 in base-A **and** not merged. **The bleeding resolves after valve replacement**, which is the actionable half |
| 75/76 | high shear cleaving von Willebrand multimers, and resolution after aortic valve replacement | as above |

## The 10 WEAKER (selected)

| # | Claim | Where, and what is lost |
|---:|---|---|
| 2 | **"coffee grounds" is over-called** — a single small one in a well patient is often not significant bleeding | the term is everywhere; the calibration is nowhere |
| 5/6 | **fresh red PR in a shocked patient is an upper GI bleed until proven otherwise, so scope upward first** | upper and lower bleeding both covered; the crossover rule that decides which scope goes first is not stated as a rule |
| 8 | **black stool from iron or bismuth is not tarry, not offensive, and not associated with anaemia** | iron appears as a cause of black stool; the three discriminating features do not |
| 9 | the first haemoglobin is not a measure of blood loss | present for **trauma** (`A9`-derived, `11_09b`); not tied to GI bleeding |
| 17 | review the causative drug with a **named responsible clinician** | drug review present; the accountability step is the part that fails in practice |
| 39 | prophylactic antibiotics apply **whether or not the bleed proves variceal and whether or not there are signs of infection** | the intervention is present; its unconditional scope is not |
| 62 | **surgery for lower GI bleeding is far better if the site is localised first** — blind colectomy has poor outcomes | localisation tests present; the reason to spend time on them is not |
| 66 | do not attribute iron deficiency to diet, aspirin or piles in this group | the mandate to scope both ends is present; the named excuses it exists to override are not |

## Strongly present — the heavy ones

- **FIT is for asymptomatic people and does not defer colonoscopy in a symptomatic patient** —
  `19_General_Practice:46`, stated as *"the distinction that gets tested and gets missed
  clinically"*. Fully covers claims 77 and 78.
- **Restarting aspirin after an ulcer bleed** — `03_Gastrointestinal:1372`, merged from C4,
  including that stopping it for secondary prevention increases mortality.
- Glasgow-Blatchford, Rockall, Dieulafoy, aortoenteric fistula, balloon tamponade — all in
  base-A already.
