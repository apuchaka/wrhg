---
name: D2 placement record
description: Where each section of D2 was placed under the section-level merge rule, and why.
bfile: Corpus B/D2_Altered_Consciousness_and_Cognition.md
rule: section-level merge
built: 2026-09-01
---

# D2_Altered_Consciousness_and_Cognition — placement record

All six sections merged whole into `Corpus A/04_Neurology.md`. Headings and structure
kept as B wrote them. `04_Neurology` is unnumbered, so every block carries B's title
without a number, and its `Mx` subheadings are scoped `— D2 §0.N.n`.

| § | Section | Placed under | Fragment |
|---|---|---|---|
| 0.1 | Reduced Consciousness | after `### Glasgow Coma Scale (GCS)` | deferred — see below |
| 0.2 | Delirium | end of `## Delirium` | not superseded — see below |
| 0.3 | Dementia | end of `## Dementias` | not superseded — see below |
| 0.4 | Delirium, Dementia and Depression — The Distinction | end of `## Delirium vs Dementia vs Depression` | none |
| 0.5 | Amnesia and Memory Impairment | where the fragment stood | **superseded** |
| 0.6 | MCI and the "Worried About My Memory" Consultation | end of `### Mild Cognitive Impairment (MCI)` | none |

## The combined-source fragment — why §0.1 merged before §0.5 superseded

`04_Neurology`'s fragment carried **two** source sections on one line:

```
`SRC:D2_… §0.1` `SRC:D2_… §0.5` `UNVERIFIED — model knowledge, not source-checked.`
```

**A supersede removes the whole fragment.** Doing it on §0.1 would have deleted §0.5's
transient-amnesia half with nothing carrying it; doing it on §0.5 would have deleted the
structural-versus-metabolic half. So §0.1 merged **without** superseding, and §0.5
superseded once both halves were present. Same ordering constraint as C7 §0.1/§0.2, and
the same reason: **the digit check cannot see this**, because the deleted half's figures
may be reproduced by the other section.

**How to spot it:** a fragment whose SRC line names more than one section. That is an
exact-token grep, so it cannot fail — unlike everything else in §1.3.

## The out-of-file fragment — §0.2 and §0.3, deliberately NOT superseded

`Investigation-Interpretation.md:557` holds `SRC:D2 §0.2` `SRC:D2 §0.3` inside a
`> [!info]` callout naming **RUDAS, 4AT and CAM**.

§1.10's supersede-and-inherit rule assumes the fragment sits **in the destination**. This
one does not, and its destination is right for what it is:

- it is **narrowed assembly** — it argues directly from the KICA `[!danger]` box above it,
  which exists only in that file, and names RUDAS as *"the instrument the danger box above
  argues for and does not name"*;
- **a reader wanting a screening cutoff goes to the instruments file, not to the disease
  file.** That is the reachability the fragment was written to provide.

Superseding it would move screening-instrument content into `04_Neurology` and break
exactly that. It stays. **Duplication accepted, per the section rule.**

## Cross-references — mapped by SECTION, not by source file

The D1 §0.6 finding (a blanket `[[F0-5]]` rule rewrote a pointer to a real-but-wrong
section, and passed every structural check) changed how the linkmap is built. A10 in
particular has **three different owners** in this vault:

| B pointer | Owner here |
|---|---|
| `[[A10_…]] 0.1` capacity | `[[Clinical-Process-EBM-Consent-Capacity]]` Capacity assessment — the general framework |
| `[[A10_…]] 0.3` advance care planning | `[[Clinical-Process-EBM-Consent-Capacity]]` Right to refuse treatment |
| `[[A10_…]] 0.6` driving | `[[04_Neurology]]` Austroads Driving Standards (Neurological Conditions) |
| `[[C2_Nausea_and_Vomiting]] 0.7` Wernicke/thiamine | `[[03_Gastrointestinal]]` §0.6 ArLD — where the AU-verified thiamine dose lives |
| `[[C2_Nausea_and_Vomiting]]` otherwise | `[[03_Gastrointestinal]]` §0.41.16 |
| `[[C3_Jaundice_and_Liver_Disease]] 0.6` | `[[03_Gastrointestinal]]` §0.6.3 Hepatic encephalopathy |

**One rule exists purely to prevent a doubled link.** B:90 already reads
`[[GER1_Comprehensive_Geriatric_Assessment]] and [[18_Geriatrics_and_Older_Persons_Health]]`.
Mapping GER1 onto 18_Geriatrics in bulk gives `[[18_…]] and [[18_…]]` — the
`furosemide (furosemide)` failure §1.11 names. A specific rule collapses the pair first.

**The linkmap was previewed on all six sections before any write**, listing every wikilink
that survived it and checking each resolves to a real Corpus A file. All six came back
clean. One `` `TODO:link — N6 Dissociation & somatic (unbuilt)` `` is left in §0.5, which is
correct: N6 is one of the 50 codes B reserved for files nobody built.

## What §0.5's supersede inherited by hand

The driver's automatic cross-reference refusal sees `[[wikilinks]]` and `§<digits>` only.
Three of this fragment's pointers are neither:

- **`§Seizures and Epilepsy` and `§Focal Seizures`** on transient epileptic amnesia. B says
  only *"it is under-diagnosed"*; the fragment said what to do about that — **order an EEG**.
- **The Wernicke-Korsakoff "not repeated here" map.** The fragment's backticked target was a
  **prefix**, `14a-1_Psych_-_Substance_Misuse`; the real file is
  `14a-1_Psych_-_Substance_Misuse__Recreational_Drug_Profiles_.md`. Written to the full name
  so it resolves — the same prefix-not-placeholder problem §1.10 records for B's wikilinks.
- **The `TGA` abbreviation warning**, carried and strengthened. It matters *more* after the
  merge than before it: the fragment used `TGA` once, B's §0.5 uses it throughout for
  transient global amnesia, and in this vault `TGA` otherwise means **transposition of the
  great arteries** or the **Therapeutic Goods Administration**. This is rule 9's collision
  problem written into the file for the reader instead of into a report.

## Digits

Every section: `REMOVED {}`. §0.4 adds only the digits of its own SRC token — B's
distinction table states no figures at all, which is what it should be.
