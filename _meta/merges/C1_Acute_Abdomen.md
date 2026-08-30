---
name: C1 destination table
description: Where every section of Corpus B/C1_Acute_Abdomen.md goes, including the sections that were discarded.
bfile: Corpus B/C1_Acute_Abdomen.md
built: 2026-08-30
---

# C1_Acute_Abdomen — destination table

Committed **before** any content was written, per CLAUDE.md §1.10. The discard rows
are the point: supersession otherwise leaves no trace, so a wrong supersede is
invisible and nothing can audit it.

C1 is 5 863 words in 11 sections. Corpus A's gastrointestinal material is
**disease-organised**; C1 is **region-and-presentation-organised**. That is why most
of it is additive rather than duplicative — A answers "what is diverticulitis", C1
answers "this patient has left iliac fossa pain, what am I reasoning through".

## Vault-wide searches run before placement

Every placement below was preceded by a whole-vault grep with markdown emphasis
stripped (rule 2) and synonyms checked before concluding absence.

| Concept | Verdict | Synonyms also checked |
|---|---|---|
| visceral vs parietal pain | **absent from A** | somatic pain, parietal peritoneum |
| foregut / midgut / hindgut referral | **absent from A** | all three terms |
| typhlitis | **absent from A** | neutropenic enterocolitis, neutropenic colitis, caecitis |
| psoas abscess | **absent from A** | iliopsoas abscess, psoas collection |
| abdominal compartment syndrome | **absent from A** | intra-abdominal pressure/hypertension, decompressive laparotomy |
| FAST (trauma sonography) | **absent from A** | eFAST, "sonography for trauma" |
| seat belt sign | **absent from A** | seatbelt, lap belt, handlebar |
| obturator sign | **absent from A** | obturator |
| appendicitis in pregnancy | **absent from A** | gravid uterus, appendix displaced/upward |
| interval appendicectomy | **absent from A** | — |
| appendiceal neoplasm on histology | **absent from A** | neuroendocrine, mucinous |
| Carnett's sign | **absent from A** | — |
| "non-specific abdominal pain" follow-up | **absent from A** | — |
| peritonism / Rovsing / Meckel / mittelschmerz / ureteric colic / mesenteric ischaemia / free air | **present in A** | — |

### Two search artifacts caught, both rule 9

- **`FAST` matched 14 Corpus A files under a case-insensitive search.** Thirteen were
  the English word *fast*. The single case-sensitive hit is `01_Cardiovascular` L314 —
  the **stroke** mnemonic (Face Arms Speech Time), a different acronym entirely.
  Trauma FAST is genuinely absent.
- **`obturator` matched three files**: an obturator **hernia** (`03_Gastrointestinal`
  L875), the obturator **nerve** (`11_07a`), and obturator **lymph nodes**
  (`07_Renal`). The obturator **sign** appears nowhere. Three different concepts
  sharing one word.
- Also dismissed: `herpes zoster before the rash` appeared "present", but every hit
  was measles **Koplik spots**. Absent.

## Destination table

| C1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Acute abdomen framework — visceral/parietal physiology, must-not-miss list, extra-abdominal causes | `Corpus A/03_Gastrointestinal.md` **new §0.41.3** | **ADDITIVE** — the visceral→parietal transition and foregut/midgut/hindgut referral are absent from A and explain the classical histories A states without deriving |
| 0.1 | "DDx by system" enumeration within it | — | **DISCARD** — duplicates A §0.41.2, which is more complete (13 system headings vs C1's 6) |
| 0.1 | Red-flag list within it | — | **DISCARD** — duplicates A §0.41's existing `[!danger] Red flags` |
| 0.2 | Assessment, peritonism, examination sequence, Carnett's sign, the analgesia myth, core Ix panel | `Corpus A/03_Gastrointestinal.md` **new §0.41.4** | **ADDITIVE** — "still vs writhing", percussion over rebound, the three skipped examinations, and Carnett's are all absent |
| 0.3 | Right upper quadrant pain | — | **DISCARD** — the biliary spectrum is A §0.3, §0.3.1, §0.3.2, §0.4; the RUQ differential adds nothing A lacks |
| 0.4 | Epigastric pain — "get an ECG first" | `Corpus A/03_Gastrointestinal.md` §0.41.3 (folded into the extra-abdominal block) | **PARTIAL** — the ECG-before-GI-diagnosis point is kept; PUD/GORD/pancreatitis detail discarded as A §0.27, §0.28, §0.11 |
| 0.5 | Left upper quadrant pain | — | **DISCARD** — splenic causes are in A §0.37 and `11_09b` Splenic trauma |
| 0.6 | Right iliac fossa pain — appendicitis sequence, atypical positions, the young woman, the rest of the DDx | `Corpus A/03_Gastrointestinal.md` §0.18 | **ADDITIVE + CONFLICT** — see the conflict note below |
| 0.7 | Left iliac fossa pain | — | **DISCARD** — A §0.36 Diverticular Disease covers it at greater depth |
| 0.8 | Suprapubic pain, PID | — | **DISCARD** — A `07_Renal_Medicine_and_Urology` and `17_05_PID__Endometriosis__Fibroids` both cover it |
| 0.9 | The catastrophes — ruptured AAA as the mimic of renal colic, mesenteric ischaemia, generalised causes | `Corpus A/03_Gastrointestinal.md` **new §0.41.5** | **ADDITIVE** — A has mesenteric ischaemia as a disease (§0.37) but not the AAA-mimics-renal-colic trap, and not abdominal compartment syndrome |
| 0.10 | Abdominal trauma — unstable patient does not go to CT, FAST, seat belt sign, non-operative management | `Corpus A/11_09b_Ortho_-_Trauma.md` **new section** after Splenic/Liver trauma | **ADDITIVE** — A's trauma file has splenic and liver trauma but no abdominal-trauma overview, no FAST, no blunt-vs-penetrating framing |
| 0.11 | Special groups — elderly, pregnancy, immunosuppressed/neutropenic, children | `Corpus A/03_Gastrointestinal.md` **new §0.41.6** | **ADDITIVE** — typhlitis and appendicitis-in-pregnancy are absent from A entirely |
| 0.11 | Children sub-block | — | **DISCARD** — `15_07_Paeds_-_Abdominal_Pain` and `15_08_Paeds_-_Surgical_Abdomen` both cover it; C1 adds nothing and A's paediatric files are the owners |

**7 additive placements · 6 discards · 1 partial.**

## No new file was needed

C1 §0.10 looked like it required a trauma file that did not exist. It does exist —
`Corpus A/11_09b_Ortho_-_Trauma.md`, found by grepping rather than by the filename,
which does not contain "abdomen" or "surgery". This is the case CLAUDE.md §1.10 warns
about directly: "Corpus A is not purely disease-organised."

## Conflict raised by C1 §0.6 — and a correction to the premise

C1 §0.6 and A §0.18 **disagree on appendicitis imaging**:

- **A §0.18 (`inherited`):** "Imaging generally not indicated unless diagnostic
  uncertainty… **US not useful for visualising the appendix** but can assess for
  gynaecological pathology mimics." CT is reserved for Alvarado 4–6.
- **C1 §0.6 (`unverified`):** "**CT abdomen and pelvis in adults** — the most accurate
  test"; "**Ultrasound first in children, young women and pregnancy** … *what:*
  **non-compressible appendix**, adnexal pathology, free fluid."

A says ultrasound cannot visualise the appendix. C1 says the non-compressible appendix
is the thing you look for. Both cannot be right.

> [!important] **`CF-012` is not in `03_Gastrointestinal.md`. It never was.**
> The instruction for this merge was to reference the existing `CONFLICT CF-012` in
> §0.18 rather than duplicate it. **There is no such block.** A whole-vault grep
> returns `CF-012` in exactly three files — `MERGE_SPEC.md`, `CLAUDE.md` and
> `MASTER_VERIFICATION_WORKFLOW.md` — in all three as the **worked example** of
> conflict-block formatting. `MERGE_SPEC.md` L524 additionally discusses it in prose
> as though it were live ("the appendicitis imaging conflict (CF-012) exists only
> because B covered a topic A already had"), which is probably where the belief came
> from.
>
> Writing "see CF-012" into §0.18 would have been a cross-reference to something that
> does not exist — CLAUDE.md rule 1 exactly. **No CF reference was written, and no new
> CF was opened.** The disagreement is recorded here and in the morning report for a
> human decision, because the instruction not to open a second marker for it was given
> on the premise that a first one existed.

The R2 disagreement is left **unmarked in the clinical file** pending that decision.
Nothing has been adjudicated.
