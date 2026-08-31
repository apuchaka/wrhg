---
name: Week 1 vault-wide claim audit — C1
description: Every claim in C1_Acute_Abdomen tested against all of Corpus A and Corpus C. Report only.
built: 2026-08-31
status: REPORT ONLY — nothing merged
---

# C1_Acute_Abdomen — vault-wide claim audit

**Extraction rule, verbatim:** one claim = one assertion that could independently be true or
false, and that a reader could act on differently.

```
claims extracted   182
PRESENT            142
WEAKER              21
ABSENT              19
```

## Claim density per section

| § | Topic | Claims |
|---|---|---:|
| 0.1 | Framework | 26 |
| 0.2 | Assessment, peritonism, core Ix | 34 |
| 0.3 | RUQ pain | 18 |
| 0.4 | Epigastric pain | 7 |
| 0.5 | LUQ pain | 9 |
| 0.6 | RIF pain | 24 |
| 0.7 | LIF pain | 8 |
| 0.8 | Suprapubic pain | 9 |
| 0.9 | Generalised pain and the catastrophes | 14 |
| 0.10 | Abdominal trauma | 15 |
| 0.11 | Special groups | 18 |

## THE HEADLINE — C1's additive blocks duplicate one base-A file extensively

**`Corpus C/NEW_Gastroenterology_and_Hepatology.md` "Acute Abdominal Pain" (lines 19–40)
existed in base-A and already carried roughly 40 of C1's 182 claims**, including the ones the
merged blocks present as new:

| C1 claim | base-A line | What base-A already said |
|---|---|---|
| 27–29 watch the patient before touching | `:28` | *"**Observe the patient before touching them**: lying completely still suggests peritonitis; restless and writhing suggests colic."* |
| 10–18 the must-not-miss list | `:19–25` | ruptured AAA **"frequently misdiagnosed as renal colic"**, ruptured ectopic, perforated viscus, mesenteric ischaemia, obstruction, pancreatitis, MI, DKA, torsion |
| 21–25 extra-abdominal mimics | `:25` | *"**medical mimics** — lower lobe pneumonia, herpes zoster before the rash, sickle cell crisis, lead poisoning, familial Mediterranean fever, acute intermittent porphyria"* |
| 9 migrating pain is useful | `:26` | *"**central to right iliac fossa is the classic appendicitis history and remains genuinely useful**"* |
| 30–34, 38, 39 examination sequence | `:29–31` | scars, hernias, Grey Turner and Cullen "late and uncommon"; palpate away from the pain; guarding, rigidity, percussion tenderness; pulsatile expansile mass; Murphy; Rovsing; shifting dullness; "bowel sounds alone are a weak sign" |
| 35 hernial orifices | `:29` | *"**examine all hernial orifices — an incarcerated hernia is easily missed under a gown**"* |
| 36 examine the scrotum | `:32` | *"**examine the external genitalia and scrotum in men**"* |
| 37/44 β-hCG in every woman | `:36` | *"**the single most important test in this presentation**"* |
| 46–52 the core bloods panel | `:38` | FBC, CRP, UEC, LFT, lipase preferred, group and hold, VBG — *"**a rising lactate with a soft abdomen and severe pain should raise mesenteric ischaemia**"* |
| 73 Fitz-Hugh-Curtis · 106 mesenteric adenitis · 110 psoas abscess · 119 diverticulitis · 127 retention · 131 PID | `:20–24` | the regional differential, by quadrant |

**This is the failure CLAUDE.md rule 10 already records for C1 — "C1's check searched Corpus A
alone and produced three further duplicates whose originals were in Corpus C". It is far more
than three.**

**Genuinely new and worth having:** the visceral/parietal pathway with foregut → epigastrium,
midgut → periumbilical, hindgut → suprapubic (**0 hits in base-A**), which is the mechanism
base-A's regional list asserts without explaining; Carnett's sign (**0 in base-A**); the
seat-belt sign; physiological leucocytosis in pregnancy.

## A BURIED DISAGREEMENT — the Barrett shape, on a bedside manoeuvre

Base-A `NEW_Gastroenterology_and_Hepatology:30` instructs:
> *"**Palpate** gently and away from the pain first: guarding, rigidity, **rebound** and
> percussion tenderness"*

The merged C1 block at `03_Gastrointestinal:1671` says:
> *"**Percussion tenderness rather than rebound.** … **Rebound testing is unpleasant, poorly
> reproducible and should largely be abandoned.**"*

**A (`snippet`) says elicit rebound. B (`unverified`) says abandon it.** Merged as an
addition, no `CONFLICT` block, no `CF-` id. This is a direct contradiction about what to do to
a patient at the bedside. **Suggested CF-038, R3** — not adjudicated.

## The 19 ABSENT

| # | Claim | Note |
|---:|---|---|
| 8 | the visceral-to-parietal transition is a **general** principle, not an appendicitis quirk | merged block carries it; **base-A did not** |
| 58 | involve the surgical team early rather than after all results return | |
| 60 | discharge advice with explicit return criteria | |
| 62 | right shoulder tip pain = diaphragmatic irritation via **C3–C5** | the dermatome reasoning |
| 67 | **Reynolds' pentad** adds hypotension and confusion | Charcot's triad is present |
| 72 | **subphrenic abscess** — post-operative, shoulder tip pain, raised hemidiaphragm | |
| 75 | **HIDA scan** — non-visualisation confirms cystic duct obstruction | 0, self-match only |
| 76 | laparoscopic cholecystectomy **on the index admission** preferred over interval surgery | |
| 78 | **interval cholecystectomy after gallstone pancreatitis**, because recurrence risk while waiting is significant | |
| 85 | review NSAID and aspirin use after an ulcer | |
| 87 | **Kehr's sign** — splenic pathology refers to the left shoulder tip | 0, self-match only |
| 89 | contact sport restricted after glandular fever, and why | |
| 90 | **splenic abscess** in endocarditis, immunosuppression, injecting drug use | 0, self-match only |
| 91 | **the splenic flexure is a watershed between SMA and IMA territories** | `watershed`'s only hits are a Jones fracture and arterial ulcer sites |
| 104 | **Doppler flow does not exclude ovarian torsion** — the ovary has a dual blood supply | a lethal false-reassurance trap |
| 112 | **pyuria occurs in appendicitis** when the appendix lies against the ureter, so an abnormal urine does not exclude it | |
| 118 | an appendiceal **neuroendocrine tumour or mucinous neoplasm** on histology must be checked and acted on | |
| 161 | the **initial haemoglobin is unreliable** in acute bleeding | |
| 174 | **surgery is not contraindicated in pregnancy**; delay harms the fetus more than the operation | |

## The 21 WEAKER (selected — full list in the table below)

| # | Claim | Where, and what is lost |
|---:|---|---|
| 123 | ischaemic colitis: watershed distribution, pain then bloody diarrhoea in an older vasculopath | **5 hits, every one a single word in a list** (`03_GI:1398`, `:1608`, `08_10:26`, `14a-1:56`, `NEW_Investigations_ID:187`). No definition, no mechanism, no presentation. The achalasia shape |
| 32 | rebound should be abandoned in favour of percussion | present only in the merged block, and **base-A says the opposite** — see the conflict above |
| 45 | a normal white cell count does not exclude a surgical abdomen | present for appendicitis; not as a general rule, and not for the elderly |
| 53 | haematuria also occurs in a leaking aneurysm and does not confirm a stone | AAA/renal-colic mimicry present at `NEW_Gastro:19`; the **haematuria** trap is not |
| 96 | vomiting preceding pain suggests a diagnosis other than appendicitis | the sequence is present; the negative discriminator is not |
| 115 | a non-visualised appendix on ultrasound does not exclude appendicitis | in the merged CF block at `03_GI:882`, nowhere else |
| 141 | peritonism in mesenteric ischaemia appears **late**, once bowel is infarcted | "out of proportion" is present; the late-signs corollary is not |
| 147 | gastroenteritis is a diagnosis of exclusion **in the elderly** | gastroenteritis is listed; the age caveat is not |
| 156 | pancreatic/duodenal injury from a **handlebar injury in a child**; enzymes may be normal early | trauma sections cover solid organs, not this |
| 166 | delayed diagnosis is the main driver of excess mortality in the elderly | the blunted presentation is merged; the mortality attribution is not |

## Two search-method notes

- **`watershed` is a rule-9 too-generic component.** It returned hits and none was colonic.
  Reading them is what produced the ABSENT on claim 91.
- **`contrast enema` was my own phrase artifact.** The corpus writes **"air enema works in
  75%"** at `15_08`. Claim 179 is PRESENT. Rule 2, my error, not the corpus's.
