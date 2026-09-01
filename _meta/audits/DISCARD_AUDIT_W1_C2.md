---
name: Week 1 vault-wide claim audit — C2
description: Every claim in C2_Nausea_and_Vomiting tested against all of Corpus A and Corpus C. Report only.
built: 2026-08-31
status: REPORT ONLY — nothing merged
---

# C2_Nausea_and_Vomiting — vault-wide claim audit

**Extraction rule, verbatim:** one claim = one assertion that could independently be true or
false, and that a reader could act on differently.

```
claims extracted    93
PRESENT             71
WEAKER              11
ABSENT              11
```

## Claim density per section

| § | Topic | Claims |
|---|---|---:|
| 0.1 | Mechanism | 10 |
| 0.2 | Acute vomiting — differential and red flags | 16 |
| 0.3 | Bilious vs non-bilious | 14 |
| 0.4 | Chronic and refractory | 12 |
| 0.5 | Antiemetic selection by mechanism | 19 |
| 0.6 | Appetite change and early satiety | 8 |
| 0.7 | Complications | 14 |

## No base-A duplication — C2's merges are sound

Unlike C1 and the C6 Barrett block, **every C2 merged block tests clean against base-A.**
Three blocks exist: `14_05a:77`, `03_Gastrointestinal:1766`, `15_08:64`.

The cannabinoid-hyperemesis block is the one worth naming, because it **looked** like a
duplicate and is not. `hot shower` returns **3 hits in base-A** — and every one is something
else: polycythaemia pruritus after a hot bath (`10_01:104`), rosacea triggers (`09_04:144`),
and heat increasing fentanyl patch absorption (`NEW_Drugs_03:200`). **`hot bathing` returns 0
and `rumination` returns 0.** The merge was correct.

That is rule 9 in the direction that matters: a non-zero count that reads as coverage and is
not.

## The 11 ABSENT

| # | Claim | Weight |
|---:|---|---|
| 2 | **regurgitation is effortless, without nausea or abdominal contraction, and points to oesophageal pathology rather than a vomiting disorder** | **diagnostic branch point — B's own note is that getting this wrong produces an entirely wrong workup**. `effortless` 0, self-match only |
| 3 | **rumination syndrome** — effortless regurgitation, re-chewed, within minutes of eating, "frequently misdiagnosed as gastroparesis or reflux for years" | missed diagnosis |
| 4 | vomiting is coordinated by a **central pattern generator** receiving four distinct afferent inputs | mechanism — the frame the whole antiemetic logic rests on |
| 5 | the CTZ sits in the **area postrema, outside the blood-brain barrier**, so it samples blood directly | mechanism, and the reason blood-borne toxins cause vomiting |
| 8 | gut **5-HT3** afferents, and chemotherapy releasing serotonin from **enterochromaffin cells** | mechanism |
| 39 | the **"double bubble"** of duodenal atresia | classic radiological sign |
| 40 | **Ladd procedure** for malrotation | the definitive operation. `Ladd` returns **210 hits, 194 of them `bladder`, `gallbladder` or `ladder`** — see below |
| 45 | **hyperglycaemia itself slows gastric emptying**, creating a vicious cycle with gastroparesis | management rationale for glycaemic optimisation |
| 49 | topical **capsaicin** and benzodiazepines acutely in cannabinoid hyperemesis | `capsaicin` hits are topical analgesia, not this |
| 51 | **chronic mesenteric ischaemia — postprandial pain, food fear and weight loss in a vasculopath** | a diagnosis, absent as an entity. `food fear` 0 |
| 93 | **thiamine is given, not measured** — the assay is slow, treatment is safe, delay is irreversible | a decision rule, not a fact |

## The 11 WEAKER (selected)

| # | Claim | Where, and what is lost |
|---:|---|---|
| 6 | CTZ receptors **D2, 5-HT3, NK1**, triggered by opioids, uraemia, hypercalcaemia | `NEW_Drugs_12:60` matches agent to cause but does not name the receptor at the site. **Lost: why a given drug works where another does not** |
| 10 | matching the antiemetic to the mechanism is the single most useful thing here | `NEW_Drugs_12:60` says choose by mechanism "not by habit" — present as instruction, absent as the organising principle with its four-input basis |
| 15 | vomiting **preceding** the pain points away from appendicitis | the appendicitis sequence is present; the negative discriminator is not |
| 17 | in children and the elderly, **UTI and pneumonia present with vomiting and no localising symptom** | both diseases covered; this presentation is not |
| 21 | raised-ICP vomiting is **often not preceded by nausea**, because it arises centrally | ICP vomiting present; the discriminating absence of nausea is not |
| 29 | malrotation leaves the midgut on a **narrow mesenteric pedicle** that can infarct the entire midgut | malrotation is present at `15_08` via the C2 merge; the pedicle mechanism and short-bowel consequence are not |
| 30 | **the infant may initially look well** — signs and shock are late | the trap, not stated |
| 69 | **ondansetron causes constipation**, which matters on opioids and in palliative care | ondansetron present; this adverse effect not tied to it |
| 77 | thyrotoxicosis and poor diabetic control both cause **increased appetite with weight loss** | both diseases present; the pairing as a discriminator is not |
| 86 | replacement needs **chloride**, not potassium alone — the alkalosis will not correct otherwise | the alkalosis is present; the chloride point is the actionable half |

## Strongly present — worth recording, because these are the heavy ones

- **Thiamine before glucose** — `NEW_Drugs_17:191` (*"THIAMINE BEFORE GLUCOSE, AND PARENTERAL
  THIAMINE FOR ANYONE AT RISK"*) and `NEW_Neurology:57`, which names hyperemesis explicitly.
- **Do not give a prokinetic in mechanical obstruction** — `NEW_Drugs_12:79` and `:110`.
- **Cannabinoid hyperemesis with compulsive hot showering** — `03_Gastrointestinal:1777`,
  merged from C2 and genuinely new.
- Pyloric stenosis with the hungry baby, the olive, and paradoxical aciduria — `15_08`.

## A new collision for rule 9's register

| Pattern | Hits | What it matched | Real |
|---|---:|---|---:|
| **`Ladd`** | **210** | `bladder` ×152, `Bladder` ×16, `gallbladder` ×15, `ladder` ×10 | **0** |

**The one true `Ladd` in the corpus is the Corpus B self-match**, so the count is 210 and the
destination total is zero. This is the `ANA` shape at smaller scale, and `Ladd` is four
characters — inside rule 9's "treat anything under about six characters as suspect".
