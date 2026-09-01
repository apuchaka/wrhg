---
name: D3 placement record
description: Where each section of D3 was placed under the section-level merge rule, and why.
bfile: Corpus B/D3_Stroke_and_Focal_Neurological_Deficit.md
rule: section-level merge
built: 2026-09-01
---

# D3_Stroke_and_Focal_Neurological_Deficit — placement record

All seven sections merged whole into `Corpus A/04_Neurology.md`. Headings and structure
kept as B wrote them; the file is unnumbered, so blocks carry B's title with no number and
`Mx` subheadings are scoped `— D3 §0.N.n`.

| § | Section | Placed under | Fragment |
|---|---|---|---|
| 0.1 | Acute Stroke — Recognition and Hyperacute Management | `### Ischaemic Stroke` | none |
| 0.2 | Stroke Syndromes and Localisation | `### Bamford-Oxford Classification` | none |
| 0.3 | Transient Ischaemic Attack and Secondary Prevention | `### Transient Ischaemic Attack (TIA)` | none |
| 0.4 | Intracerebral Haemorrhage | `### Haemorrhagic Stroke` | none |
| 0.5 | Stroke Mimics and Stroke Chameleons | alongside the territory entries | deferred |
| 0.6 | The Paresis Patterns | where the fragment stood | **superseded** |
| 0.7 | Subacute and Chronic Focal Deficit | `## Weakness — Differential Diagnosis` | none |

**§0.7 is the one placement that is not obvious.** It is organised by **time course** —
seconds to minutes vascular, hours to days inflammatory, weeks to months neoplastic — not
by stroke. It belongs with the general weakness differential, and that is where it went.

## The combined-source fragment — second instance in one day

`SRC:D3 §0.5` `SRC:D3 §0.6` on one line, so §0.5 merged **without** superseding and §0.6
superseded once both were present. Identical to D2's `§0.1 + §0.5` fragment.

**Two in one file-pair is a shape, not an accident.** The test is cheap and cannot fail:
**a fragment whose SRC line names more than one section cannot be superseded by the first
of them.** Grep the SRC line and count the `§` tokens.

## What the supersede would have destroyed

**`Pronator drift` is in neither B §0.5 nor B §0.6.** It is merge-authored, and a supersede
deletes the fragment's prose — so it would have gone silently. It is carried, with its
`[[Examination]]` pointer.

Also carried: **vertical gaze and blinking to command** in an apparently unresponsive
patient, with the `§Glasgow Coma Scale` pointer explaining why. B's §0.6 *names* locked-in
syndrome; the fragment said what to **do** about it. And the neighbouring-material map —
`§Weakness — Differential Diagnosis`, `§Vertigo`, `[[Examination]]` for HINTS, `§Delirium`.

## TWO TOOLING DEFECTS, both surfacing on §0.6

**1. A `SRC:` token was being read as a cross-reference.** The refusal compared the
fragment's `§n.n` refs against the block's, and a two-section SRC line looks like a
reference to `§0.5` — the very section the merge replaces. Fixed (`202ac36`): SRC lines are
excluded from the fragment side, as the protected-marker loop already did.

**2. D2 §0.5's supersede had passed that same check FOR THE WRONG REASON**, found while
chasing defect 1. Its fragment carried `SRC:D2 §0.1`, which should have been reported lost —
and was not, because the *note* I wrote happened to contain the string `"§0.1 above"`.

```
$ awk '/^### Amnesia and Memory Impairment/,/^## Seizures/' 04_Neurology.md | grep -n "§0\.1"
3:*Supersedes the former ... is carried by §0.1 above.*
```

**One coincidence in prose satisfied a structural check.** The pointer was also meaningless
— `04_Neurology` is unnumbered and has no §0.1 — so it was replaced with
`§Reduced Consciousness above` (`a14a902`), and the whole file audited for the same class:
**0 unqualified `§0.N` pointers remain.**

## Cross-references — three B files, three sections, three different owners

| B pointer | What that section actually is | Owner here |
|---|---|---|
| `[[F0-5_…]] 0.5` | Neuromuscular Respiratory Failure | `[[04_Neurology]]` Guillain-Barré Syndrome (GBS) |
| `[[F0-5_…]]` other | head injury / ICP | `[[04_Neurology]]` CT Head, Head Injury, and ICP |
| `[[A6_…]] 0.4` | Heat Intolerance (cited for Uhthoff) | `[[11_09b_Ortho_-_Trauma]]` Heat illness |
| `[[A9_…]] 0.4` | Anticoagulant-Associated Bleeding and **Reversal** | `[[10_09a_Haemonc_-_Anticoagulants_and_Antiplatelets]]` |
| `[[A9_…]]` bare | transfusion | `[[10_08_Haemonc_-_Blood_Products_and_Transfusion]]` |
| `[[B3_…]] 0.4` | Atrial Fibrillation | `[[01_Cardiovascular]]` §0.4 |
| `[[D2_…]] 0.3` | Dementia (cited for NPH) | `[[04_Neurology]]` Normal Pressure Hydrocephalus |
| `[[D1_…]] 0.3` | Primary Headache Disorders (cited for aura) | `[[04_Neurology]]` Migraine |

**A9 is the sharpest case.** `§0.4` is *reversal*; bare `[[A9]]` is *transfusion*. They are
different files here, and a single blanket rule would silently send a reader after
prothrombinex to the blood-products file. Checked by content — `prothrombinex` and
`idarucizumab` — not by filename.

## Digits

`REMOVED {}` on six of seven sections. §0.6 removed `{'5': 1}`, established as correct by
extracting the fragment from HEAD and printing its digits **per line**:

```
['3','0','5','3','0','6']  <- `SRC:D3_… §0.5` `SRC:D3 §0.6` `UNVERIFIED — …`
```

That was the fragment's **only** line containing a digit. The removed `5` is the `§0.5` half
of the combined provenance token, and §0.5 now carries its own. No clinical figure moved.

## One item deliberately left alone

§0.5 and §0.6 each carry a `` `TODO:link — … (unbuilt)` `` marker whose `(unbuilt)` claim is
**false** — every such code now has a file in `Corpus B-new/` (`f974630`). All 34 already
merged into Corpus A/C are scheduled for correction as one commit after the B-new merges
(`d92d36a`). Fixing two of thirty-four here would leave the rest inconsistent.
