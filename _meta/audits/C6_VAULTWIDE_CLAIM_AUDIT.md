---
name: C6 vault-wide claim audit (independent re-run)
description: Every claim in C6 tested against all of Corpus A and Corpus C, ignoring the merge table's dispositions.
built: 2026-08-31
status: REPORT ONLY — nothing merged
---

# C6 — vault-wide claim audit

## Extraction method

**One claim = one assertion that could independently be true or false, and that a reader
could act on differently.**

- A definition is one claim; its mechanism is a separate claim.
- A list is **one** claim where the list is the teaching point; an item **splits out** when it
  carries its own action (bisphosphonates split from the drug-cause list because "take
  upright, do not lie down" is a separate instruction).
- Each named investigation with its *why/what* is one claim. Each distinct management action
  is one claim.
- A discriminator ("X but not Y") is one claim, not two.

**This is a judgement call.** The same text yielded **24 claims from §0.1** on the first pass
and **39** here. The denominators are not comparable; only the absences are.

## Contamination disclosure

I ran C6 earlier in this session, so this is not a clean-room re-run.

**Group A — claims I would have extracted regardless (161 of 164).** Extraction was
mechanical: read each section top to bottom, split on the rules above. Every claim below
traces to a sentence in the source.

**Group B — claims whose *salience* was plausibly anchored by the earlier run (3):**
- **#39 fundoplication** — a management sentence any pass would extract, but I knew to check
  whether it landed.
- **#80/#81 the EoE biopsy rule** — in the text, but I gave it more scrutiny than a first pass
  might.
- **#88 achalasia management** — likewise.

**All three were re-searched from scratch and all three are confirmed ABSENT independently.**
The anchoring affected attention, not the verdict.

**The real contamination risk is not extraction — it is search-term choice**, where knowing
the answer shapes the pattern. Two places where that demonstrably worked *against* me are in
the corrections below.

## Claim density per section

| Section | Claims | Note |
|---|---:|---|
| §0.1 Dyspepsia, reflux, heartburn | 39 | densest — 6 callouts, a 7-item Ix list, 3 Mx tiers |
| §0.2 Peptic ulcer and *H. pylori* | 27 | |
| §0.3 Oesophageal disease | 35 | 5 conditions each with D/discriminator/Ix/Mx |
| §0.4 Anorectal pain | 26 | |
| §0.5 Anal lump | 15 | shortest — largely a differential list |
| §0.6 Pruritus ani | 22 | |
| **Total** | **164** | |

Density tracks section length and callout count, not extraction inconsistency. §0.5 is
genuinely a list; §0.1 genuinely carries six separate teaching callouts.

## TWO CORRECTIONS TO THE FIRST AUDIT — both in the corpus's favour

**1. Haemorrhoid grades ARE defined.** The first audit reported grades I–IV absent and called
it "a term used in the corpus without being defined anywhere in it." **False.**
`03_Gastrointestinal:1047` defines all four: *"Grade 1: protrusion within the anal canal |
Grade 2: protrudes beyond the anal canal, reduces spontaneously on cessation of straining |
Grade 3: reduces on manual pressure | Grade 4: irreducible"*, and `:1058–1062` gives the
graded treatment. **My pattern was `Grade III`; the corpus writes `Grade 3`.**
Roman-versus-Arabic is a numeral-form miss that **digit folding does not cover**, and it is a
new trap for rule 2.

**2. Botulinum toxin for anal fissure IS present**, at `NEW_Drugs_12:199`, alongside GTN 0.2%
and topical diltiazem. The first audit did not test it.

## ONE FINDING THE FIRST AUDIT COULD NOT HAVE MADE — an ADDITIVE row that duplicates base-A

The first audit scoped ADDITIVE rows out. Including them per instruction:

**The Barrett's management block (`13_06b:49`) was merged on a false premise and is a
near-total duplicate.**

The table's justification reads: *"absent — `13_06b` §0.3 gives D, R, S/Smx and Ix but **stops
before management**"*, and the merged block opens *"§0.3 above gives the definition, risk
factors and diagnosis and **stops there**."*

**Base-A `13_06b:41` already read:** *"**Mx:** high-dose PPI (evidence uncertain). If
metaplasia confirmed — endoscopic surveillance with biopsies every 3–5 years. If dysplasia —
offer endoscopic interventions, including **radiofrequency ablation and endoscopic mucosal
resection**."*

Claim by claim: **#73 (PPI + surveillance) duplicate · #74 (dysplastic Barrett treated
endoscopically, RFA and EMR) duplicate, near-verbatim · #75 (low absolute annual risk)
absent, and not in the merged block either.** The one genuinely new element is that the
**interval depends on segment length**, where base-A gives a flat 3–5 years — **which is a
disagreement, not an addition, and no CONFLICT was raised.**

## The raw list

Verdicts: **ABSENT** · **PRESENT** at file:line · **WEAKER** at file:line, with what is lost.

### §0.1 Dyspepsia, Reflux and Heartburn (39)

| # | Claim | Verdict |
|---:|---|---|
| 1 | dyspepsia = epigastric pain/discomfort, fullness, early satiety, bloating | PRESENT `03_GI:1178` (as symptoms, not a definition) |
| 2 | GORD = symptoms/complications of reflux into oesophagus | PRESENT `03_GI:1176` |
| 3 | antireflux barrier = LOS + crural diaphragm + angle of His | **ABSENT** (`crural` 0, self-match only) |
| 4 | reflux is via **transient** LOS relaxations, not a permanently weak sphincter | **WEAKER** `03_GI:1180` — *"increased relaxation of the lower oesophageal sphincter"*. **Lost: that the relaxations are transient and the sphincter is not permanently weak** — the whole point of the claim |
| 5 | promoted by raised intra-abdominal pressure: obesity, pregnancy, hiatus hernia, large/late meals | **WEAKER** `03_GI:1178` R-list has hiatus hernia, obesity, age, FHx. **Lost: pregnancy, and the intra-abdominal-pressure mechanism that unifies them** |
| 6 | oesophageal mucosa has no protective mucus layer | **WEAKER** `03_GI:1180` — *"epithelial resistance"*. Lost: why the oesophagus is more vulnerable than the stomach |
| 7 | inferior MI presents as epigastric burning with nausea | PRESENT `03_GI:1649`, `03_GI:1699`, `NEW_Gastroenterology_and_Hepatology:24` |
| 8 | "indigestion" that is infarction is a recurring lethal misattribution | **ABSENT** as framing (`indigestion` 0 in vault) |
| 9 | atypical ACS in diabetics, women, older patients, ATSI | PRESENT `NEW_Cardiology_and_Vascular:37`; `03_GI:1649` names diabetics, women, elderly. **ATSI-younger-IHD not found here** |
| 10 | antacid or GTN relief does not distinguish | PRESENT `01_Cardiovascular:328–332` |
| 11 | GTN relieves oesophageal spasm | PRESENT `01_Cardiovascular:329`, `NEW_Cardiology_and_Vascular:27` |
| 12 | get an ECG | PRESENT `03_GI:1649`, `:1699` — **but ABSENT from §0.28 GORD, whose Ix list contains no ECG** |
| 13 | red-flag list mandating endoscopy | PRESENT `NEW_Drugs_12:38` (ALARM), `03_GI:1184`, `13_06b:84`. **Lost: *previous gastric surgery or gastric ulcer*, in none of them** |
| 14 | CCBs and nitrates relax the LOS and worsen reflux | **ABSENT** as a reflux cause |
| 15 | NSAIDs and aspirin worsen dyspepsia | PRESENT `03_GI:1144` (as PUD risk) |
| 16 | bisphosphonates: mucosal injury, take upright with water, do not lie down | PRESENT `NEW_Drugs_10:35` — fuller than B |
| 17 | anticholinergics, theophylline, doxycycline, steroids, KCl worsen reflux | **WEAKER** — doxycycline oesophagitis at `NEW_Drugs_05:147`. **Lost: the class as a reviewable drug list** |
| 18 | reviewing the drug chart is the cheapest intervention and is skipped | **ABSENT** |
| 19 | extra-oesophageal: cough, hoarseness, globus, laryngitis, dental erosion, asthma | **WEAKER** `03_GI:1182` has cough, halitosis, globus, enamel erosion. Lost: hoarseness, laryngitis, asthma worsening |
| 20 | reflux is a common cause of chronic cough | PRESENT `03_GI:1180` (vagal mechanism) |
| 21 | reflux may be entirely silent, with no heartburn | **ABSENT** |
| 22 | long-term PPI harms (7 named) | PRESENT `NEW_Drugs_12:32` — fuller than B |
| 23 | PPIs prescribed indefinitely without review | PRESENT `NEW_Drugs_12:29`, `03_GI:1191` |
| 24 | rebound acid hypersecretion → step down, do not stop abruptly | PRESENT `NEW_Drugs_12:32`, `18_Geriatrics:205` |
| 25 | functional dyspepsia = symptoms + normal endoscopy + no structural cause | **ABSENT** — `functional dyspepsia` has 1 vault hit, `NEW_Drugs_12:105`, as a **prokinetic indication in a list**. No definition |
| 26 | it is a **positive** diagnosis on symptom criteria, not a residual label | **ABSENT** |
| 27 | overlaps IBS and anxiety; explaining the gut-brain mechanism is therapeutic | **ABSENT** |
| 28 | burning retrosternal worse lying flat/bending/after meals; waterbrash | **WEAKER** `03_GI:1182` has heartburn after meals and cough lying down. `waterbrash` **ABSENT** |
| 29 | ECG to exclude cardiac cause in the dyspepsia workup | **ABSENT from §0.28** — see #12 |
| 30 | *H. pylori* test-and-treat in patients without red flags | PRESENT `NEW_Investigations_Gastroenterology:214` |
| 31 | FBC + iron studies; IDA converts dyspepsia to a red flag | PRESENT `03_GI:1184` (anaemia in red flags) |
| 32 | gastroscopy where red flags present | PRESENT `03_GI:1189` |
| 33 | pH/impedance and manometry for refractory, atypical or pre-surgical | PRESENT `03_GI:1186`, `NEW_Investigations_Gastroenterology:378` |
| 34 | coeliac serology — coeliac presents as dyspepsia and bloating with minimal bowel symptoms | **WEAKER** — serology exists at `03_GI:797`, `NEW_Investigations_Infectious_Diseases:362`. **Lost: the link to dyspepsia. Nothing tells a reader working up dyspepsia to consider coeliac** |
| 35 | ultrasound where biliary symptoms plausible | PRESENT `03_GI` biliary sections |
| 36 | weight loss has the strongest evidence of any lifestyle measure | **WEAKER** `03_GI:1192` lists weight loss first without ranking it |
| 37 | elevate head of bed, avoid eating before lying down | **ABSENT** (`head of bed` 0) — `03_GI:1192` has "avoid late-night eating" only |
| 38 | PPI at lowest effective dose with a defined review | PRESENT `03_GI:1192` |
| 39 | **fundoplication for well-selected patients with proven reflux** | **ABSENT** — 0 hits vault-wide, self-match only. Recorded PARTIAL/"folded into the §0.30.5 block"; the `SRC:C6` block that exists covers §0.4 and §0.5 |

### §0.2 Peptic Ulcer Disease and *H. pylori* (27)

| # | Claim | Verdict |
|---:|---|---|
| 40 | aggressive factors vs mucosal defence | PRESENT `03_GI:1147` |
| 41 | NSAIDs inhibit COX-1 prostaglandins | PRESENT `NEW_Drugs_03:166` |
| 42 | **injury is systemic — enteric coating and rectal administration do not protect** | **ABSENT** |
| 43 | *H. pylori* dominant cause of duodenal ulceration | PRESENT `03_GI:1149` |
| 44 | *H. pylori* causes adenocarcinoma and MALT lymphoma | PRESENT `03_GI:1206`, `:1229` |
| 45 | NSAIDs increasingly dominant in Australia as *H. pylori* falls | **ABSENT** |
| 46 | stress ulceration — Curling (burns), Cushing (head injury) | **ABSENT** — `Curling` 0; all 31 `Cushing` hits are the syndrome |
| 47 | Zollinger-Ellison = gastrin-secreting tumour | PRESENT `03_GI:1150` |
| 48 | ZE suspicion pattern (multiple, distal, refractory, with diarrhoea, no *H. pylori*/NSAID) | **ABSENT** — the entity is named, the pattern that should trigger suspicion is not |
| 49 | every gastric ulcer must be biopsied | PRESENT `03_GI:1166` |
| 50 | withhold PPI/antibiotics before testing or you get false negatives | PRESENT `03_GI:1216`, `:1229` |
| 51 | this is the commonest technical error in *H. pylori* testing | **ABSENT** as emphasis |
| 52 | serology cannot confirm eradication — antibodies persist | **ABSENT** |
| 53 | clarithromycin resistance rising in Australia | PRESENT `03_GI:1222`, `NEW_Drugs_12:36` |
| 54 | take the regimen from eTG Antibiotic | PRESENT in effect — `03_GI:1224` gives the RACGP-sourced regimen |
| 55 | always confirm eradication with a repeat test | PRESENT `03_GI:1224` (test of cure ≥4 weeks) |
| 56 | a benign appearance is not sufficient reassurance | **WEAKER** `03_GI:1166` requires biopsy without stating why appearance misleads |
| 57 | repeat endoscopy to confirm healing; non-healing gastric ulcer is cancer until proven otherwise | PRESENT `03_GI:1170` |
| 58 | duodenal ulcers need no routine follow-up | PRESENT `03_GI:1170` |
| 59 | gastroprotection indications where an NSAID is unavoidable | **ABSENT** as an indication list |
| 60 | **NSAID + SSRI / corticosteroid / anticoagulant multiplies bleeding risk** | **WEAKER** `03_GI:1144` lists SSRIs and steroids as PUD risk factors. **Lost: that combining them multiplies risk, and that it is a common avoidable prescribing pattern** |
| 61 | epigastric pain burning or gnawing | **WEAKER** — `gnawing` ABSENT; `03_GI:1155` has the pointing sign |
| 62 | duodenal relieved by food/worse at night; gastric worse on eating | PRESENT `03_GI:1155–1157`, with mechanism |
| 63 | **the distinction is unreliable and should not decide who gets endoscopy** | **ABSENT — and it CONTRADICTS `03_GI:1157`**, which elaborates the rule as mechanism-derived. Unraised conflict; suggest **CF-037 R2** |
| 64 | many NSAID ulcers are silent until they bleed or perforate | **ABSENT** |
| 65 | fasting gastrin **off PPI** — PPIs raise gastrin and make it uninterpretable | **WEAKER** — ZE named at `03_GI:1150`; the test and the PPI caveat not found |
| 66 | erect CXR for suspected perforation | PRESENT `03_GI` perforation sections |

### §0.3 Oesophageal Disease (35)

| # | Claim | Verdict |
|---:|---|---|
| 67 | progressive dysphagia + weight loss = cancer until proven otherwise | PRESENT `13_06b:84`, `13_06b:16` |
| 68 | SCC upper/middle third; smoking, alcohol, achalasia, hot beverages | PRESENT `13_06b:81` |
| 69 | adenocarcinoma lower third, from Barrett, obesity and reflux | PRESENT `13_06b:37–39` |
| 70 | adenocarcinoma is now the commoner type in Australia, incidence risen | **ABSENT** |
| 71 | Barrett = intestinal metaplasia replacing squamous epithelium | PRESENT `13_06b:37`, `:42` |
| 72 | progresses through dysplasia to adenocarcinoma | PRESENT `13_06b:42` |
| 73 | Barrett managed with PPI + endoscopic surveillance | **PRESENT IN BASE-A** `13_06b:41` — **and re-merged as ADDITIVE** |
| 74 | dysplastic Barrett treated endoscopically (RFA, EMR) not watched | **PRESENT IN BASE-A** `13_06b:41`, near-verbatim — **and re-merged as ADDITIVE** |
| 75 | the absolute annual risk of progression is low | **ABSENT** — not in base-A and not in the merged block either |
| 76 | EoE in a young, often male, often atopic adult with dysphagia or food bolus | **ABSENT** |
| 77 | EoE frequently misdiagnosed as reflux for years | **ABSENT** |
| 78 | EoE endoscopy: fixed rings, longitudinal furrows, white exudate | **ABSENT** (`furrows` 0) |
| 79 | the oesophagus may look entirely normal | **ABSENT** |
| 80 | **diagnosis needs multiple biopsies proximal AND distal — the disease is patchy** | **ABSENT** |
| 81 | **disimpact a food bolus without biopsies and the opportunity is lost** | **ABSENT** |
| 82 | EoE treated with PPI, swallowed topical steroids, dietary elimination | **ABSENT** |
| — | *EoE overall:* `eosinophilic` returns 24 hits; **exactly one is EoE** — `NEW_Drugs_12:26`, the last item in a list of PPI indications | |
| 83 | achalasia = failed LOS relaxation, absent peristalsis, myenteric plexus degeneration | **ABSENT** — `13_06b` names achalasia twice, both as one word in a list (`:26`, `:81`) |
| 84 | **dysphagia to solids AND liquids from the outset** | **WEAKER** `13_06b:16` — *"Can fluids be drunk as normal?" — YES suggests a stricture; NO suggests a motility disorder.* **Adjacent, phrased as a screening question, and it never names the distinction or ties it to achalasia** |
| 85 | regurgitation of undigested food, nocturnal cough, aspiration, chest pain | **WEAKER** `03_GI:1774` — *"Undigested food with no nausea, immediately after eating — think oesophageal (achalasia, pharyngeal pouch)"*. Lost: nocturnal cough, aspiration, chest pain, weight loss |
| 86 | bird's beak on barium swallow | PRESENT `NEW_Investigations_Gastroenterology:288` |
| 87 | manometry is diagnostic | PRESENT `NEW_Investigations_Gastroenterology:378`, `13_06b:22` |
| 88 | **treated by pneumatic dilatation, POEM or Heller myotomy** | **ABSENT** — `myotomy`'s only destination hit is **Ramstedt pyloromyotomy** for pyloric stenosis |
| 89 | pseudoachalasia — a GOJ tumour mimicking achalasia | **ABSENT** |
| 90 | suspect it with older age, short history, marked weight loss; endoscopy mandatory first | **ABSENT** |
| 91 | peptic stricture: dilatation plus long-term PPI | PRESENT `13_06b:27–28` (dilatation; long-term PPI not stated) |
| 92 | oesophageal spasm / hypercontractile oesophagus is a genuine cardiac mimic | **WEAKER** — spasm named at `NEW_Cardiology_and_Vascular:24`, `History-Taking:46`; `hypercontractile` ABSENT |
| 93 | pill oesophagitis — agents, and taken with insufficient water or lying down | **WEAKER** — doxycycline at `NEW_Drugs_05:147` with the instruction. **Lost: the entity and its other members** |
| 94 | infective oesophagitis — candida, HSV, CMV; consider HIV | PRESENT `08_05-06:226` |
| 95 | gastroscopy with biopsies is the primary Ix | PRESENT `13_06b:22` |
| 96 | biopsy at several levels even when the mucosa looks normal | **ABSENT** |
| 97 | barium swallow defines strictures, pouches, motility | PRESENT `13_06b:22`, `NEW_Investigations_Gastroenterology:288` |
| 98 | high-resolution manometry | PRESENT `NEW_Investigations_Gastroenterology:378` |
| 99 | CT/PET staging; EUS for T and N | PRESENT `13_06b` cancer section |
| 100 | **cannot swallow own saliva = urgent; take biopsies at the same procedure** | **ABSENT** — `food bolus`'s only vault hit is an **inhaled** airway foreign body in a child |
| 101 | nutritional support and dietitian involvement | **ABSENT** for oesophageal disease specifically |

### §0.4 Anorectal Pain (26)

| # | Claim | Verdict |
|---:|---|---|
| 102 | perianal abscess: constant throbbing pain worse sitting, fever, fluctuant swelling | PRESENT `03_GI:1021+` (§0.24) |
| 103 | **deep (intersphincteric, supralevator) abscess may show little externally** | **ABSENT** — `supralevator` 0. The claim that absence of swelling does not exclude is lost |
| 104 | drainage is the treatment; antibiotics are an adjunct, not a substitute | PRESENT `03_GI:1034` |
| 105 | lower threshold in diabetics/immunosuppressed — Fournier gangrene | PRESENT `Fournier` ×4 |
| 106 | a proportion of abscesses are followed by fistula-in-ano | PRESENT `03_GI:1023` |
| 107 | fissure: tearing pain on defecation persisting after, bright red blood on paper | PRESENT `03_GI:995+` |
| 108 | pain out of proportion; avoidance worsens constipation — self-perpetuating | **WEAKER** — the cycle is not stated |
| 109 | posterior midline (anterior in post-partum women), poorly perfused | PRESENT `03_GI:1076` (merged block) |
| 110 | sphincter spasm reduces flow and prevents healing — why treatment targets spasm | PRESENT `03_GI:1076` |
| 111 | chronic fissure: sentinel tag, hypertrophied papilla, visible sphincter fibres | **ABSENT** |
| 112 | Mx: GTN or diltiazem → botulinum → lateral internal sphincterotomy | PRESENT `03_GI:1012–1015`, `NEW_Drugs_12:199` |
| 113 | atypical fissure → Crohn, TB, HIV, syphilis, anal carcinoma, leukaemia | **WEAKER** `03_GI:1077` — *"Crohn disease, malignancy, or infection"*. **Lost: TB, HIV, syphilis and leukaemia as named entities** |
| 114 | perianal disease may be the first sign of Crohn, by years | **WEAKER** `03_GI:1026` names Crohn as a fistula risk without the precedence point |
| 115 | thrombosed external haemorrhoid: tense, tender, blue-purple | PRESENT `03_GI:1079` |
| 116 | excision in the first few days; conservative after | PRESENT `03_GI:1079` |
| 117 | proctalgia fugax | PRESENT `03_GI:1081` |
| 118 | **levator ani syndrome** | **ABSENT** — all `levator` hits are Horner's, ptosis, and the pelvic floor muscle |
| 119 | **anal carcinoma — HPV, HIV, immunosuppression, smoking, receptive anal intercourse; incidence rising** | **ABSENT** — `anal carcinoma` 0; the one `anal cancer` hit is a *colorectal* warning |
| 120 | do not attribute a persistent anal ulcer or lump to a fissure or pile without biopsy | **WEAKER** `NEW_Drugs_12:207` covers rectal bleeding and colorectal cancer, not the anal lesion |
| 121 | perianal Crohn: fistulae, complex abscesses, tags, fissures | PRESENT `03_GI:1026`, `:1030` |
| 122 | coccydynia | **ABSENT** |
| 123 | pain preventing examination warrants EUA | PRESENT `03_GI:1029` (EUA for fistulae) |
| 124 | MRI pelvis maps the tract against the sphincter complex | **WEAKER** `03_GI:1029` — *"imaging for complex fistulae (especially Crohn's)"*. **Lost: that it is MRI, and that the point is continence risk** |
| 125 | anal carcinoma treated with chemoradiotherapy, not surgery | **ABSENT** |
| 126 | long-term stool softening prevents fissure recurrence | PRESENT `03_GI:1010` |
| 127 | sitz baths | PRESENT `03_GI:1010` |

### §0.5 Anal Lump (15)

| # | Claim | Verdict |
|---:|---|---|
| 128 | internal haemorrhoid grades I–IV defined | **PRESENT** `03_GI:1047` — as Grade 1–4 |
| 129 | the grade determines the treatment | PRESENT `03_GI:1058–1062` |
| 130 | internal haemorrhoids are above the dentate line and therefore painless | PRESENT `03_GI:1072` (merged block) |
| 131 | pain means something else | PRESENT `03_GI:1073` |
| 132 | visceral above, somatic below | PRESENT `03_GI:1072` |
| 133 | fibre/fluid; banding I–III; surgery for IV or failure | PRESENT `03_GI:1059–1062` |
| 134 | bleeding over 40 or with red flags needs colonic investigation | PRESENT `NEW_Drugs_12:207`, `03_GI:1055` |
| 135 | haemorrhoids are common enough to coexist with cancer | PRESENT `NEW_Drugs_12:207` in effect |
| 136 | skin tags: residue of a thrombosed pile, or chronic fissure or Crohn | PRESENT `03_GI:1082` |
| 137 | anal warts: screen STIs, consider HIV, partner notification | PRESENT `08_08`, `17_07` |
| 138 | rectal prolapse shows **concentric** rings vs the **radial** folds of piles | **ABSENT** as a discriminator — `concentric` hits are unrelated |
| 139 | prolapse in children: constipation and cystic fibrosis | PRESENT `15_*` CF sections |
| 140 | any indurated, ulcerated or non-healing lump requires biopsy | **WEAKER** — see #120 |
| 141 | molluscum, condylomata lata, hidradenitis in the differential | PRESENT `hidradenitis` ×11 |
| 142 | proctoscopy is required to see internal haemorrhoids | PRESENT `NEW_Drugs_12:207`, `03_GI:1056` |

### §0.6 Pruritus Ani (22)

| # | Claim | Verdict |
|---:|---|---|
| 143 | persistent perianal itch, worse at night, itch-scratch-damage cycle | PRESENT `09_08_Dermatology` |
| 144 | faecal contamination, moisture and trauma break the barrier | PRESENT `09_08` |
| 145 | **the itch outlasts and replaces its original cause** | **ABSENT** — the reason treating the original cause alone fails |
| 146 | either inadequate **or excessive** cleaning | **WEAKER** — over-cleaning as a cause not found |
| 147 | anorectal conditions causing leakage and moisture | PRESENT `09_08` |
| 148 | threadworm — intense nocturnal perianal itch in children | PRESENT `08_09:367–370` |
| 149 | candida in diabetics and after antibiotics | PRESENT `09_08`, `NEW_Drugs_05` |
| 150 | psoriasis (inverse), eczema, lichen sclerosus, contact dermatitis | PRESENT `lichen sclerosus` ×5, `17_07` |
| 151 | **topical anaesthetics and long-used steroids are frequent sensitisers** | **ABSENT** |
| 152 | ask what the patient has been applying — it is often the cause | **ABSENT** |
| 153 | systemic: diabetes, cholestasis, iron deficiency, lymphoma, CKD | PRESENT `09_08` pruritus causes |
| 154 | **AIN, Bowen and extramammary Paget present as perianal itch and are treated as eczema for years** | **ABSENT** — Bowen's exists only as a skin cancer at `09_03a:31–57`, never perianally; `extramammary` matches *"extramammary pain referred to the breast"* |
| 155 | a persistent, unilateral or non-responding perianal rash requires biopsy | **ABSENT** |
| 156 | treat the whole household, repeat the dose, hygiene measures | PRESENT `NEW_Drugs_05:33`, `08_09:371` |
| 157 | stop all current topicals, especially anaesthetics and long-term steroids | **ABSENT** |
| 158 | clean gently with water; no soap, no wipes, no rubbing | **WEAKER** — general emollient/soap-avoidance advice exists in `09_*`, not perianally |
| 159 | barrier preparation; treat constipation or leakage | PRESENT `09_08` |
| 160 | a short mild steroid course may break the itch, but not long-term (atrophy) | PRESENT `NEW_Drugs_08` steroid-atrophy warnings |
| 161 | dietary triggers — coffee, citrus, spicy food, chocolate | **ABSENT** (`citrus` 0) |
| 162 | tape test in the morning before washing | PRESENT `08_09:370` |
| 163 | glucose and HbA1c for undiagnosed diabetes | PRESENT `09_08`, `06_Metabolic` |
| 164 | patch testing for contact dermatitis | PRESENT `patch test` ×7 |

## Totals

```
claims extracted     164
PRESENT               89
WEAKER                26
ABSENT                49
```

## Comparison with the first audit — the number that matters

The first audit was row-level. It named **~14 missing claims** across 6 rows and classified
4 rows as CLAIM-GAPS/AREA-LEVEL.

**The vault-wide claim rule finds 49 ABSENT and 26 WEAKER — 75 claims not fully carried,
against ~14.**

**Absences the first audit did NOT find (28):**
`#3` antireflux barrier anatomy · `#8` the misattribution framing · `#14` CCB/nitrate reflux ·
`#18` drug-chart review · `#21` silent reflux · `#28` waterbrash · `#37` head-of-bed ·
`#45` NSAIDs overtaking *H. pylori* · `#48` the ZE suspicion pattern · `#51` the commonest
testing error · `#52` serology cannot confirm eradication · `#64` silent NSAID ulcers ·
`#70` adenocarcinoma now commoner · `#75` low annual progression risk · `#76`–`#79`, `#82`
the rest of EoE · `#90` pseudoachalasia suspicion features · `#96` biopsy at several levels ·
`#100` cannot-swallow-saliva · `#101` dietitian · `#103` supralevator abscess · `#111`
chronic-fissure signs · `#118` levator ani syndrome · `#122` coccydynia · `#125`
chemoradiotherapy for anal cancer · `#138` concentric vs radial · `#145` the itch outlasting
its cause · `#151`/`#152` sensitisers and asking what was applied · `#155` biopsy the rash ·
`#161` dietary triggers.

**Plus one finding of a different class entirely: the Barrett ADDITIVE row duplicates
base-A `13_06b:41`, merged on a stated premise that was false.**

**And two the first audit got wrong in the corpus's favour** — haemorrhoid grades and
botulinum.

## What this implies for the other 33 tables

**The row-level rule under-reports by roughly 5×** on this file. The under-report is not
uniform: it is concentrated in **claims that sit inside a section whose *topic* is present**,
which is precisely the dyspepsia shape, and in **discriminators and negative claims** —
"does not distinguish", "is unreliable", "may look entirely normal", "the itch outlasts its
cause" — which no topic-level search will ever surface because they are not topics.

**Two new traps for rule 2:**
- **Roman versus Arabic numerals.** `Grade III` vs `Grade 3`. Digit folding does not cover it.
- **`extramammary`** matches *"extramammary pain referred to the breast"*, and **`Cushing`**
  (44 hits, 31 the syndrome) hides the absence of the stress-ulcer eponym.
