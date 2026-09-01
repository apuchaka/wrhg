---
name: Discard audit — C6 calibration
description: Claim-level re-test of every DISCARD/PARTIAL row in the C6 destination table. The calibration case for the whole discard audit.
built: 2026-08-31
status: REPORT ONLY — nothing fixed
---

# C6 — the calibration case

**The gate:** if this audit does not independently find achalasia and the dyspepsia claim
gaps, the audit method is wrong and must be fixed before continuing.

## CALIBRATION RESULT — PASSED

Both known failures were found independently, from the section text, without reference to
the brief that named them.

- **Achalasia** — `13_06b` is the named destination. Achalasia appears there **twice, both
  times as one word in a list** (`:26` a dysphagia cause, `:81` an SCC risk factor). No
  definition, no failure of LOS relaxation, no management. **AREA-LEVEL confirmed.**
- **Dyspepsia** — §0.28 GORD and §0.29 gastritis are present and good, and specific claims
  are absent from both. **CLAIM-GAPS confirmed.**

**The audit also found three failures that were not in the brief**, and disagreed with the
brief on two claims. Both directions are recorded below.

## Counts

```
C6 — Dyspepsia, Oesophageal and Anorectal Disease
  rows audited        6   (5 DISCARD + 1 PARTIAL)
  CONFIRMED           2   (§0.6 pruritus ani, largely; §0.2 in its main claims)
  DISPLACED           0   as a whole-row verdict — but see §0.1, which is
                          CLAIM-GAPS containing a DISPLACED claim
  AREA-LEVEL          1   (§0.3 oesophageal disease)
  CLAIM-GAPS          3   (§0.1 dyspepsia, §0.2 PUD, §0.5 anal lump)
  WRONG               0
  PARTIAL — LOST      1   (§0.1 fundoplication: recorded as merged, never merged)
```

## Row by row

### §0.1 Dyspepsia, reflux, heartburn → **CLAIM-GAPS**

Named destination: §0.28 GORD, §0.29 gastritis, `NEW_Drugs_12` §0.1.
**24 distinct claims extracted. `NEW_Drugs_12` §0.1 is excellent and carries more than the
table's own reason for naming it ("the drug classes") suggests.**

**Present at a named destination — CONFIRMED:**
GORD definition · red-flag/ALARM list (`NEW_Drugs_12:38`, fuller than §0.28's) · long-term
PPI harms, the whole list (`NEW_Drugs_12:32`) · **rebound acid hypersecretion and the taper
instruction** (`NEW_Drugs_12:32`) · deprescribing, with the Australian NSW TAG guide ·
pH/impedance and manometry (§0.28) · *H. pylori* testing (§0.29) · extra-oesophageal
features, partially (§0.28 S/Smx has cough, halitosis, globus, enamel erosion).

**Missing or displaced:**

| Claim | Verdict | Weight |
|---|---|---|
| **Cardiac exclusion before settling on reflux** | **DISPLACED** | **lethal misattribution** |
| **Transient LOS relaxations** as the mechanism | CLAIM-GAP | mechanism detail |
| **Functional dyspepsia** as a positive diagnosis | CLAIM-GAP | common presentation, no management |
| **Coeliac serology in a dyspepsia workup** | **DISPLACED** | missed treatable diagnosis |
| Drugs that cause or worsen reflux, as a list | CLAIM-GAP | reachability — components exist |
| Crural diaphragm, angle of His | CLAIM-GAP | detail |
| Red flags: *previous gastric surgery or gastric ulcer* | CLAIM-GAP | detail |

**The cardiac claim in detail, because it is the heaviest thing in this file.**
The claim exists in the vault, and **not at the named destination**:
- `03_Gastrointestinal:1649` — *"**Cardiac** — inferior myocardial infarction presenting as
  epigastric pain with nausea, particularly in diabetics, women and the elderly. **Get an ECG
  before settling on a gastrointestinal diagnosis for epigastric pain.**"*
- `03_Gastrointestinal:1699` — the same, as an Ix line.
- `01_Cardiovascular:328–332` — *"Relief with GTN **does not confirm** that pain is cardiac …
  Relief with an **antacid does not exclude** cardiac pain either. **Do not use response to
  treatment as a diagnostic test in chest pain.**"*
- `NEW_Gastroenterology_and_Hepatology:24` — MI presenting as epigastric pain, particularly
  inferior.

**But all four sit in acute-abdomen, chest-pain and cardiology contexts. §0.28 GORD has no
ECG in its investigations and no cardiac warning of any kind**, and `epigastric` returns
**0 hits in `01_Cardiovascular`**. A reader working through dyspepsia never meets it.
**This is the reachability problem, not a content gap — and it is the shape the brief warned
not to score as CONFIRMED.**

**Where I disagree with the brief:** the brief listed "a fuller red-flag list" as one of six
missing claims. `NEW_Drugs_12:38` carries the ALARM features including odynophagia, palpable
mass, and family history of upper GI cancer — a **named destination**. Only *previous gastric
surgery or gastric ulcer* is genuinely additional. Likewise the inferior-MI claim is
**displaced, not absent**.

### §0.1 Fundoplication → **PARTIAL, AND THE UNMERGED HALF IS LOST**

The table records **PARTIAL — "folded into the §0.30.5 block"**. It was not.

- `fundoplication` — **1 hit in the whole vault, a self-match in Corpus B.** Zero in the
  destination corpora.
- The `SRC:C6` block that exists is at `03_Gastrointestinal:1069`, and its token reads
  **`§0.4` and `§0.5`** — not §0.1.
- The only `anti-reflux surgery` mentions (`03_Gastrointestinal:1186`,
  `NEW_Investigations_Gastroenterology:378`) are *indications for manometry*, not the
  procedure.
- **The table's own gap list already said fundoplication was "absent".**

**This is failure class 2.2 found on the first table audited.** Weight: a management option
for a common condition, and the endpoint the manometry entries point toward.

### §0.2 Peptic ulcer disease and *H. pylori* → **CLAIM-GAPS**

§0.27 is strong and most claims are **CONFIRMED**: gastric-vs-duodenal pain timing *with its
mechanism*, Zollinger-Ellison, biopsy of gastric ulcers, **repeat endoscopy to confirm
healing and not for duodenal ulcers**, risk factors including SSRIs and steroids. PPI/
antibiotic withholding before testing is at §0.29.

**Missing:**

| Claim | Weight |
|---|---|
| **NSAID injury is systemic via COX-1 — enteric coating and rectal administration do not protect the stomach** (`enteric coating` 0 hits) | **prescribing error, actively believed otherwise** |
| **Gastroprotection indications**, and that NSAID + SSRI / corticosteroid / anticoagulant multiplies bleeding risk | **prescribing error** |
| **Curling and Cushing stress ulcers** | detail |
| Many NSAID ulcers are asymptomatic until they bleed or perforate | red flag |

**An unraised CONFLICT.** §0.27 teaches the gastric-vs-duodenal pain-timing rule and
elaborates its mechanism. **C6 §0.2 says the distinction "is unreliable in practice and
should not be used to decide who needs endoscopy."** A (`inherited`) versus B
(`unverified`) on a triage rule — that is a `CONFLICT` block that was never written.
**Not adjudicated here.** Suggested **CF-037, R2**.

### §0.3 Oesophageal disease → **AREA-LEVEL** *(the calibration case)*

`13_06b` and §0.30 own the area. They do not carry the topics.

**Achalasia** — 2 hits in `13_06b`, both one word in a list. Absent vault-wide:
- the definition (failure of LOS relaxation, absent peristalsis, myenteric plexus degeneration)
- **dysphagia to solids AND liquids from the outset** — the discriminator from mechanical
  obstruction. `liquids` has **1 destination hit and it is about hyperemesis**.
- **management** — `myotomy` returns 3 hits, of which the only destination hit is
  **Ramstedt pyloro*myotomy* for pyloric stenosis**, a different operation. Pneumatic
  dilatation, POEM and Heller myotomy are absent.
- **pseudoachalasia** — 0 (self-match only). A GOJ tumour mimicking achalasia.

Present but **DISPLACED** into Corpus C: bird's beak (`NEW_Investigations_Gastroenterology:288`)
and manometry (`:378`, `:384`). Neither is reachable from the condition file.

**Eosinophilic oesophagitis — a THIRD failure, and it was on the table's own PRESENT list.**
`eosinophilic` returns 24 hits; **exactly one is EoE** — `NEW_Drugs_12:26`, where it is the
last item in a list of PPI indications. Absent entirely: the young atopic male with a food
bolus, the endoscopic appearance (`furrows` **0 hits**), the fact the oesophagus may look
normal, **and the biopsy rule — multiple biopsies proximal AND distal, because disimpacting a
food bolus without biopsies loses the opportunity.**

**Weight: the achalasia discriminator and the EoE biopsy rule are both diagnostic actions an
intern takes or fails to take at the bedside.**

Present elsewhere and correctly owned: SCC risk factors (`13_06b:81`), pill oesophagitis by
its members — doxycycline (`NEW_Drugs_05:147`, with the upright-and-water instruction) and
bisphosphonates (`NEW_Drugs_10:35`, in full).

### §0.5 Anal lump → **CLAIM-GAPS**

Present: rubber band ligation, rectal prolapse, condylomata, skin tags, abscess.

**Missing: the internal haemorrhoid grades I–IV and the fact that the grade determines the
treatment.** `03_Gastrointestinal:1060` says *"higher-grade internal haemorrhoids"* without
ever defining a grade. **Weight: a management step, and a term used in the corpus without
being defined anywhere in it.**

Also missing: **rectal prolapse shows concentric mucosal rings, prolapsed haemorrhoids show
radial folds** — the bedside discriminator.

### §0.6 Pruritus ani → **CONFIRMED, with one gap**

Threadworm is well covered — `08_09:367` has a section including the **tape test** (*"apply
tape to the perianal area"* — my `adhesive tape` phrase search missed it, rule 2), and
`NEW_Drugs_05:33` has treat-the-whole-household, the repeat dose and the hygiene measures.

**Missing: anal intraepithelial neoplasia, Bowen disease and extramammary Paget disease as
causes of persistent perianal itch**, and the rule that a persistent, unilateral,
well-demarcated or non-responding perianal rash requires **biopsy**. Bowen's disease exists
only as a skin cancer in `09_03a`, never perianally. **Weight: missed malignancy — B's own
framing is that these are "frequently treated as eczema for months or years."**

## Two new collisions for rule 9's register

| Pattern | Hits | What it matched | Real |
|---|---:|---|---:|
| `Cushing` | 44 | **Cushing's syndrome/disease ×31** — the *stress ulcer* eponym is absent | **0** |
| `extramammary` | 3 | *"**extramammary** pain referred to the breast"* — not Paget disease | **0** |

`myotomy` is a third of the same shape: 3 hits, and the only destination hit is
**pyloromyotomy**, a different operation on a different organ.

## Method notes

- Every verdict through `gapcheck.py`. Three phrase patterns were **refused by the tool**
  (`functional dyspepsia`, `pill oesophagitis`, `rebound acid`) and re-run as single words,
  which is the tool working as intended.
- **`adhesive tape` was my own rule-2 failure** — the corpus writes *"apply tape"*. Caught by
  reading the threadworm section rather than trusting the search.
- `rebound` (50 hits) is dominated by **rebound tenderness**; narrowed to `hypersecretion`.
- Self-match warnings fired correctly on `crural`, `relaxations`, `indigestion`,
  `pseudoachalasia`, `furrows`, `enteric coating`, `fundoplication` — in every case the only
  hit was the C6 source file itself.
