---
name: D1 placement record
description: Where each section of D1 was placed under the section-level merge rule, and why.
bfile: Corpus B/D1_Headache_and_Meningism.md
rule: section-level merge
built: 2026-09-01
---

# D1_Headache_and_Meningism — placement record

All six sections merged whole into `Corpus A/04_Neurology.md`. Headings and structure
kept as B wrote them.

| § | Section | Placed under | Fragment superseded |
|---|---|---|---|
| 0.1 | Headache — Framework and Red Flags | `## Other Headache Causes` | — |
| 0.2 | Thunderclap Headache and Subarachnoid Haemorrhage | `## Other Headache Causes` | — |
| 0.3 | Primary Headache Disorders | `## Other Headache Causes` | — |
| 0.4 | Secondary Headaches Worth Knowing | `## Other Headache Causes` | — |
| 0.5 | Meningism, Meningitis and Encephalitis | `## CNS Infections` | — |
| 0.6 | Neck Stiffness — The Differential | `## CNS Infections` | `### Added from unverified layer — neck stiffness: the differential` |

**`04_Neurology` uses unnumbered headings**, so every D1 block carries B's title with no
section number. That is the reason for the defect below.

## §0.6 — the supersede, and what it inherited

The fragment was **pointer-shaped**: it stated up front that *"every entity below is
covered in its own file … each line points at the owner rather than restating it."* B's
section restates the content. So the supersede replaces the prose and **re-aims the
pointers onto the merged section** rather than discarding them:

| Pointer | Carries |
|---|---|
| `[[15_20a_Paeds_-_Trisomies_and_Sex_Chromosome_Disorders]]` | atlantoaxial instability in Down syndrome |
| `[[13_05a_ENT_-_Sore_Throat_and_Tonsillitis]]` | retropharyngeal abscess |
| `[[08_09_Infectious_Disease_-_Miscellaneous]]` | Lemierre syndrome |
| `[[15_02_Paeds_-_Ill_and_Feverish_Child__Meningitis__Encephalitis]]` | the paediatric two-to-exclude |
| `[[NEW_Drugs_12_Gastrointestinal]] §0.2.2` | dystonic-reaction agents and anticholinergic reversal |
| `§CNS Infections`, `§Strokes` | same-file section pointers |

`§0.2.2` verified before writing the pointer, per rule 1: it is
`### 0.2.2 Dopamine Antagonists (Antiemetic)`, and its danger box names metoclopramide and
prochlorperazine, oculogyric crisis, torticollis and trismus, and benztropine or an
anticholinergic as treatment.

## THREE DEFECTS FOUND ON §0.6 — all in the tooling, none in the content

**1. A retarget written against RAW B text that the linkmap had already rewritten.**
Retargets run *after* the linkmap, so a retarget anchored on a line containing a wikilink
matches 0 times and the driver refuses. Already a recorded trap; repeated anyway. Attach
retargets to lines the linkmap leaves alone.

**2. The subheading rescope had no branch for an UNNUMBERED destination.** `number` was
empty, so B's `### 0.1.1 Mx – Immediate` became a bare `#### Mx – Immediate`. Every B
section emits those three, so the five D1 blocks merged so far produced **15 headings
collapsing to 3 names, five deep each.** base-A `04_Neurology` has **0** duplicate
headings.

Fixed in `e240184` (scope under the block's provenance coordinates — `#### Mx – Immediate
— D1 §0.6.1`, unique because bfile+section is) and repaired in `38ccadd` (15 headings, 15
lines changed, every other line byte-identical, no digit removed).

**The check that should have caught it could not.** It counted duplicate headings across
the whole file, so it could not distinguish one this merge created from one already
present — and once the first duplicate existed, every later run printed the same non-zero
number and it read as background noise. It now diffs the header multiset against the file
as it stood before the merge. Known-answer tested in both directions per rule 11: it
reports 0 on the clean case and names the duplicate on a constructed failing case.

**3. A linkmap rule that was right for one section of a file and wrong for another.**
`[[F0-5_Acute_Respiratory__Headache_and_Head_Injury]] → [[04_Neurology]] CT Head, Head
Injury, and Intracranial Pressure` is correct for F0-5 §0.6–0.8. B §0.6 cites **F0-5
§0.10**, which is *"Tonsillitis and Peritonsillar Abscess (Quinsy)"* — so the
retropharyngeal-abscess pointer was silently re-aimed at an unrelated section **of the
destination file itself**. A specific §0.10 rule now runs ahead of the generic one.

**This one is the worrying shape.** The rewrite produced a real file and a real heading,
so it passed the cross-reference refusal, the digit check, the probe check and the
duplicate-header check. **It was caught by reading the merged block.** No structural test
distinguishes a pointer aimed at the wrong correct place from one aimed at the right one.

## Digits

Every section: `REMOVED {}`. No figure left `04_Neurology` in this file's merge.
