---
name: known-absences
description: Topics absent from the vault AND from every Corpus B file covering the surrounding area, so no merge closes them. Hand-maintained. Verified against main 2026-08-31.
---

# Known absences — recognised, not rediscovered

Every entry here has been **searched for and confirmed absent**. They are recorded so a
future session recognises them as **known** rather than reporting them as findings.

**Why they need their own file.** The `NO-BASELINE` markers in the corpus attach to content
that *exists*. These have **no page to mark** — that is the whole problem. An absence with
nowhere to live is invisible to every check the project runs, because every check starts
from a file.

**How to use this file.** Before reporting a gap, search it. Before removing an entry,
confirm the content is genuinely present with `scripts/gapcheck.py` — not with a plain grep
(CLAUDE.md rule 11).

**Verification command for every entry below:**
```
python3 scripts/gapcheck.py '<pattern>' --dirs "Corpus A" "Corpus C"
```

---

## 1. Dubin-Johnson syndrome · Rotor syndrome

| | |
|---|---|
| **Where it should live** | `03_Gastrointestinal.md` §0.44 Jaundice, in the conjugated-hyperbilirubinaemia differential alongside Gilbert's and Crigler-Najjar |
| **How it was found** | C3 merge (jaundice). The three-way jaundice classification was merged; the two benign conjugated hyperbilirubinaemias were **not supplied by C3 either**, so the merge could not close it |
| **Verified absent** | `Dubin.Johnson` → 1 hit, which is **the in-place note recording the gap itself** at `03_Gastrointestinal.md:1805`. `Rotor syndrome` → 0 |
| **Status** | **Already recorded in place.** This file cross-references that note rather than duplicating it |
| **Why it matters** | Gilbert's is covered and is the common one. A reader meeting a *conjugated* hyperbilirubinaemia with no haemolysis and normal LFTs has nowhere to go |

## 2. Schatzki ring

| | |
|---|---|
| **Where it should live** | `13_06b_ENT_-_Dysphagia_and_Oesophageal_Pathology.md`, in the structural dysphagia differential with webs, strictures and achalasia |
| **How it was found** | C6 merge (dysphagia, oesophageal). Merged content covered achalasia, eosinophilic oesophagitis and Barrett's; the ring was in neither layer |
| **Verified absent** | `Schatzki` → 0 |
| **Why it matters** | It is the classic cause of **intermittent solid-food dysphagia with food bolus obstruction** in an otherwise well patient — a presentation the file otherwise routes toward malignancy |

## 3. Hunt and Hess — and any subarachnoid haemorrhage grading scale

| | |
|---|---|
| **Where it should live** | `04_Neurology.md` SAH section |
| **How it was found** | D1 merge (headache and meningism). SAH is well covered — thunderclap onset, CT-then-LP, the timing of xanthochromia — but **graded nowhere** |
| **Verified absent** | `Hunt and Hess` → 0 · `Fisher grade\|WFNS\|SAH grad` → **0**. This is not one missing eponym: **the vault has no SAH severity scale at all** |
| **Why it matters** | Grade drives prognosis and the urgency of transfer, and it is the first thing a neurosurgical registrar asks for |

## 4. Weber syndrome · Millard-Gubler syndrome — brainstem stroke beyond Wallenberg

| | |
|---|---|
| **Where it should live** | `04_Neurology.md` stroke syndromes, beside the existing lateral medullary content |
| **How it was found** | D3 merge (stroke and focal deficit). **Wallenberg is present (2 hits) and is the only brainstem syndrome represented** |
| **Verified absent** | `Weber syndrome` → 0 · `Millard.Gubler` → 0 |
| **Why it matters** | The corpus teaches one brainstem stroke. **Crossed findings** — ipsilateral cranial nerve, contralateral long tract — are the localising principle, and one example does not convey it. Weber (III + hemiparesis) and Millard-Gubler (VI/VII + hemiparesis) are the standard midbrain and pontine pair |

## 5. Decompression sickness

| | |
|---|---|
| **Where it should live** | `11_09b_Ortho_-_Trauma.md`, beside the environmental-injury and drowning content added in the A6 merge |
| **How it was found** | The envenomation and environmental coverage audit. Heat illness, hypothermia and drowning were all closed by A6; **DCS was in no B file**, so nothing closed it |
| **Verified absent** | `decompression sickness` → 1 hit, and it is **not the topic**: the nitrous-oxide entry at `NEW_Drugs_02_Anaesthetics.md:131` on expansion of closed air spaces |
| **Why it matters** | Australian-relevant — diving is a common recreational exposure. Also the one condition where the treatment is a **location** (a recompression chamber), so knowing it exists changes the disposition, not just the diagnosis |
| **Decision on record** | Flagged on the study list, **deliberately not filled** from model knowledge |

## 6. Myocarditis as an entity

| | |
|---|---|
| **Where it should live** | `01_Cardiovascular.md`, as its own section beside §0.32 Pericarditis |
| **How it was found** | B1 merge. `grep -i myocarditis` returns **27 hits**; `grep "^#+.*[Mm]yocarditis"` returns **0** |
| **Verified absent** | Every one of the 27 is **someone else's complication** — diphtheria (`15_04a`), clozapine (`14_03`), Chagas (`08_07`), measles (`15_03a`), Lyme (`08_01-03`), and a cause of dilated cardiomyopathy (`01_Cardiovascular` §0.26) |
| **Why this one is different from the rest of this file** | It is **densely present and structurally absent.** Every search for the word succeeds, so **no search reveals there is nothing to find**, and a coverage audit keyed on term presence scores it as covered. That is why it needs writing down |
| **What exists now** | The B1 merge added a **myopericarditis** block inside `§0.32 Pericarditis` — troponin rise or impaired function reclassifies the illness, and exercise restriction matters because exertion in active myocarditis is associated with arrhythmic death. **That block is a fragment inside another disease's entry, is `unverified`, and states in place that it is not a substitute for an entry** |
| **What a real entry needs** | aetiology (viral, drug, autoimmune, peripartum) · presentation · overlap with pericarditis · ECG and echo findings · troponin pattern · when to suspect fulminant disease · exercise restriction with a duration |
| **Also on** | the PRIORITY study list in `_meta/RUN_STATE.md`, at the same tier as heat illness, recognising dying and foreign bodies |

## 7. Phaeochromocytoma as an entity

| | |
|---|---|
| **Where it should live** | `06_Metabolic_Medicine_and_Endocrinology.md`, as its own section |
| **How it was found** | B2 merge (hypertension). `grep "^#+.*haeochromocytoma"` → **0**; it appears only inside the MEN2A/MEN2B lists at `06_Metabolic` §0.9 |
| **Verified absent** | 0 headings |
| **Why it is recorded but NOT treated as a gap** | **All three parts a reader needs exist, scattered:** the presentation at `NEW_Cardiology_and_Vascular` §Paroxysmal Hypertension · the screening test at `NEW_Investigations_Renal_and_Urology` §0.10 (plasma free / 24-hour urinary metanephrines) · the **alpha-before-beta** safety rule at `NEW_Drug_Classes_Cardiovascular_Antihypertensives:86` |
| **Open question for a later round** | ~~whether that scattering is acceptable, or whether the entity needs consolidating. Recorded so the question is asked once rather than rediscovered each time~~ |
| **ANSWERED AND CLOSED 2026-08-31** | **The scattering was not acceptable, and the reason is specific: the alpha-before-beta rule was findable only from inside an alpha-blocker pharmacology entry**, i.e. only by a reader who already knew to look for it. Consolidated into `06_Metabolic_Medicine_and_Endocrinology.md` §*Phaeochromocytoma and Paraganglioma — consolidated owner*, per §1.11's one-owner-plus-pointers pattern. **No content was moved out of Corpus C and no figure was added anywhere** — the three components stay where they are, each keeps what it owns (the paroxysmal-hypertension differential, the test itself, the class pharmacology), and each now carries a pointer to the owner. This entry stays in the file: the absence was real, and the record of how it was closed is the point |

---

## What this file is not

It is **not** a list of everything missing from the vault. It is the set of absences that
**survived a merge that should have closed them** — each was searched for during a B-file
merge covering the surrounding area, and the B file did not supply it either.

The complementary question — *what does an Australian intern meet that the checklist never
names?* — cannot be answered from inside the vault and is recorded separately in
`_meta/CHECKLIST_CATEGORY_AUDIT.md` (Finding 5) as the external-reference question.
