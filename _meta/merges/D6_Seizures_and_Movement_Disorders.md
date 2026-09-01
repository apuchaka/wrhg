---
name: D6 placement record
description: Where each section of D6 was placed under the section-level merge rule, and why.
bfile: Corpus B/D6_Seizures_and_Movement_Disorders.md
rule: section-level merge
built: 2026-09-01
---

# D6_Seizures_and_Movement_Disorders — placement record

Source path verified against the filesystem:
`/home/user/wrhg/Corpus B/D6_Seizures_and_Movement_Disorders.md`.

| § | Section | Placed under | Fragment |
|---|---|---|---|
| 0.1 | Seizures — Classification and the First Seizure | `### Focal Seizures` | deferred |
| 0.2 | Status Epilepticus | `### Status Epilepticus` | none |
| 0.3 | Epilepsy Management | where the fragment stood | **superseded** |
| 0.4 | Tremor | `### Abnormal Involuntary Movements` | none |
| 0.5 | Parkinsonism | `### Parkinson's Disease (PD)` | none |
| 0.6 | Chorea, Dystonia, Tics and Myoclonus | `### Abnormal Involuntary Movements` | none |
| 0.7 | Rigidity — The Differential | `## Movement Disorders` | none |

**§0.7 sits at section level, not under an entry** — it is a cross-cutting differential
(parkinsonian rigidity, spasticity, NMS, serotonin syndrome, malignant hyperthermia,
tetanus, stiff-person) that no single movement-disorder entry owns.

**§0.2 is R1 territory.** Status epilepticus is dose and resuscitation timing, so any
disagreement between B's block and the destination's own timings is for a human to resolve
against ANZCOR or Epilepsy Action Australia. No figure was introduced from memory; the
digit report is the evidence — `REMOVED {}`, and everything numeric is B's own text.

## THE CITING CLAIM DECIDES THE OWNER, NOT THE CITED SECTION

The D1 §0.6 finding was that **one blanket rule per source file** is wrong. D6 is the next
refinement: **the same source section, cited for two different claims, has two different
owners.**

| Citing claim | Cited | Owner here |
|---|---|---|
| retropharyngeal abscess (D1 §0.6) | `[[F0-5]] 0.10` | `[[13_05a_ENT_-_Sore_Throat_and_Tonsillitis]]` |
| **Sydenham chorea as a Jones major criterion** (D6 §0.6) | **the same `[[F0-5]] 0.10`** | `[[01_Cardiovascular]]` §0.22 Rheumatic Fever |

F0-5 §0.10 is *Tonsillitis and Peritonsillar Abscess (Quinsy)*. Mapping by source section
alone would have sent a reader after the Jones criteria to a tonsillitis entry.

The same happens within one B file: `[[A6]] 0.3` (drug-induced hyperthermias) → this file's
NMS entry, while `[[A6]] 0.4` (heat intolerance) → `[[11_09b_Ortho_-_Trauma]]` Heat illness,
mapped that way in D3 §0.7. And `[[D2]] 0.3` is Dementia, but cited in §0.5 for *"early
dementia, fluctuating cognition and visual hallucinations"*, so it points at
`### Lewy Body Dementia (LBD)` rather than the general heading.

## §0.3's supersede — the combined fragment, and one thing it took with it

`SRC:D6 §0.1` + `SRC:D6 §0.3` on one line — the fourth combined-source fragment in this
run, so §0.1 merged without superseding.

Carried: the SUDEP `UNVERIFIED` marker (incidence, and how Australian guidance frames and
times the conversation — Epilepsy Action Australia or RACGP), the fragment's argument that
*"avoiding it removes the strongest reason a patient has to take medication reliably"*, and
the `[[NEW_Drugs_15_Neurological]]` pointer on epilepsy-surgery referral.

**Also repointed: B's own internal reference.** Its last line read *"…and the safety advice
in 0.1"* — B's section numbering, meaningless in an unnumbered destination. Now
*"§Seizures — Classification and the First Seizure above"*.

### What the verification missed the first time

Checking the ILAE terms survived, `grep -c "Focal with impaired awareness"` returned **0**.
That is a **case-sensitivity artefact of my own grep** — rule 2's first clause. B's §0.1
writes them lower-case inside a parenthesis at `:1397`. All three current terms and both
obsolete ones are present case-insensitively, each exactly once: the fragment's duplicate
copy removed, §0.1's retained.

### But something WAS lost, and the check that passed could not see it

The fragment gave the mapping **term by term**:

```
- **Focal aware** — … (Formerly *simple partial*.)
- **Focal with impaired awareness** — … (Formerly *complex partial*.)
- **Focal to bilateral tonic-clonic** — … (Formerly *secondary generalised*.)
```

B's §0.1 states the three current terms at `:1397` and, separately, that the three old ones
are obsolete at `:1400`. **It never says which maps to which.** So all six terms survived —
which is what I checked, and reported — and the thing that made them useful did not. A
reader who learnt *"complex partial"* could no longer find what it is now called.

Restored in `09adca1`, as one sentence on §0.1's block. This is §1.11's dual-naming
principle in another form: *a reader who learnt the old name can find the entry*.

**The general lesson: a presence check on the terms passes while the RELATION between them
is destroyed.** Rule 12 names this at claim level for discards; it applies to supersedes
too, and no structural check in the driver can see it.

## Digits

Every section: `REMOVED {}`.
