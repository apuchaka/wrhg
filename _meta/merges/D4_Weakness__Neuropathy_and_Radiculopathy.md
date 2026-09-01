---
name: D4 placement record
description: Where each section of D4 was placed under the section-level merge rule, and why.
bfile: Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md
rule: section-level merge
built: 2026-09-01
---

# D4_Weakness__Neuropathy_and_Radiculopathy — placement record

Source path verified against the filesystem, not the run order:
`/home/user/wrhg/Corpus B/D4_Weakness__Neuropathy_and_Radiculopathy.md`. A same-prefix
file also exists in `Corpus B-new/`; `Corpus B/` wins because the driver globs it first.
See `_meta/audits/SOURCE_PATH_AUDIT.md`.

| § | Section | Destination | Fragment |
|---|---|---|---|
| 0.1 | Localising the Lesion | `04_Neurology` · `## Weakness — Differential Diagnosis` | none |
| 0.2 | Peripheral Neuropathy | `04_Neurology` · `### Diabetic Neuropathy` | none |
| 0.3 | Radiculopathy | **`11_06_Ortho_-_Spinal_Orthopaedics`** | **superseded** |
| 0.4 | Mononeuropathies and Entrapment | `04_Neurology` · `### Charcot-Marie-Tooth Disease` | deferred |
| 0.5 | Neuromuscular Junction Disorders | `04_Neurology` · `### Myasthenia Gravis (MG)` | none |
| 0.6 | Myopathy | `04_Neurology`, where the fragment stood | **superseded** |
| 0.7 | Sensory Disturbance — Numbness and Paraesthesia | `04_Neurology` · `### Subacute Combined Degeneration` | none |

**§0.3 is the only section that leaves `04_Neurology`.** Its fragment already sat in
`11_06`, between `## Scoliosis` and `## Discitis`, and back pain with radicular features is
that file's subject.

## D4 IS THE FILE THAT BROKE THE TOOLING FOUR TIMES

Every one of these was found by *reading before merging* or by *reading a number the tool
printed* — none by a check failing.

### 1. `UNVERIFIED` was never in the protected list — and seven had already been destroyed

§0.3's fragment carries
`` `UNVERIFIED — the prevalence of asymptomatic disc findings by age band, and the
Australian imaging referral criteria for radicular pain; RACGP.` `` and B's own version of
the same warning carries no marker. The supersede would have deleted it silently: **no
digits move.**

The instruction that produced the hard refusal named four things — `[!fail]`, `[!check]`,
and an UNVERIFIED/VERIFIED marker. The list implemented **three**. `` `VERIFIED [^`]*` ``
cannot match `UNVERIFIED`; the backtick anchors it.

Retrospective audit (`aa6beb2`) found **seven already gone**, across five commits and three
files: D2 §0.5 ×2, C7 §0.3, C7 §0.2 ×2, C6 §0.4, C6 §0.3. Restored in `0a76b66`,
`1a7852c`, `3050204`. **Six of seven byte-identical**, pulled from the pre-supersede blob
and matched against the tree. The seventh was deliberately reworded: its closing clause read
*"neither is the 48-hour CRP cut-off"* and the replacing section **states** that figure, so
restoring it verbatim would have put a marker on the page contradicting the line above it.

**Then the list was audited against §1.7 rather than extended per casualty** (`bad5e8d`):
`[paed]`/`[adult]`, `→MED:` and `TODO:link` were also unprotected. Retrospective audit for
those three: **0 lost**, so that one is ahead of the incident.

### 2. The supersede boundary was the next HEADING

§0.6's fragment is followed — before any heading — by a **separate merged block written as
a callout**:

```
> [!info] Added from unverified layer — **the incidental raised CK in a patient with no symptoms**
> `SRC:L3_Muscle_Symptoms_and_Widespread_Pain §0.4` `UNVERIFIED — …` `NO-BASELINE — …`
```

A callout has no heading, so the whole of it fell inside D4 §0.6's deletion range. The
protected-marker list would have refused this one — it carries NO-BASELINE, UNVERIFIED and
a wikilink — **but that is luck. A block of plain clinical prose would have gone silently.**
Fixed (`3f7df30`): stop at the next foreign `SRC:` token.

### 3. …and the fix's walk-back crossed blank lines

The boundary walks back over the callout its stop-token sits inside, so the block is not cut
in half. The condition was `startswith('>') or blank` — and a fragment whose **own** body is
callouts separated by blanks is one continuous run of exactly that, all the way back. It
walked from the L3 block to the fragment's own SRC line:

```
block 34 lines | superseded 2 lines        <- WRONG
```

**Nothing failed.** The write succeeded, digits clean, probes clean, headers clean, printed
`OK`. The only signal was a superseded-line count implausibly small for a 16-line fragment —
a number reported on every merge and, until then, never read. Fixed in `e9ae615`; the earlier
test passed only because its fragment body was plain prose.

### 4. `carry_refs`, and a guard of mine that could not fail

D4's fragment splits its pointers across both halves: the foot-drop half cites
`[[11_07a_Ortho_-_Dermatomes_and_Myotomes_Reference]]` and belongs with §0.4, already merged.
The cross-reference refusal is block-local, so it fired on a pointer that was not lost.

`carry_refs` declares such a pointer relocated **and the driver verifies it is present**.
My first version checked the destination **including the fragment about to be deleted**, so
it always found the pointer — in the very text being removed:

```
before:  *** FAIL  declared relocated but NOT present anywhere     accepted
after:   PASS      declared relocated but NOT present — must refuse
                   carry_refs declared 'Some_Reference_File' relocated, but it is NOT in dest.md
```

The three lines read correctly. Running them showed a check that could not fail.

**And when it was fixed, it refused for real** — B §0.4 genuinely lacks the pointer. So the
pointer went where it belongs, onto §0.4's block (`6e279a3`), as its own commit, rather than
being dumped into the superseding block to satisfy a check.

## Cross-references — every one mapped by SECTION

| B pointer | What that section is | Owner here |
|---|---|---|
| `[[F0-5_…]] 0.5` | Neuromuscular Respiratory Failure | `[[04_Neurology]]` Guillain-Barré Syndrome (GBS) |
| `[[F0-4_…]] 0.9` | Adult Analgesia (pregabalin, ScriptCheckSA) | `[[NEW_Drugs_03_Analgesics]]` §0.4 Drugs for Pain Relief |
| `[[F0-1_…]] 0.3` | Cholinergic Toxidrome (organophosphates) | `[[14a-2_Psych_-_Overdose_and_Poisoning_Management]]` |
| `[[B5_…]] 0.5` | Claudication and PAD | `[[01_Cardiovascular]]` §0.36.1 PAD |
| `[[A7_…]] 0.6` | Crush Injury and Rhabdomyolysis | `[[11_01_Ortho_-_Orthopaedic_Emergencies]]` Rhabdomyolysis |
| `[[B6_…]] 0.6` | Generalised Weakness | `[[04_Neurology]]` Weakness — Differential Diagnosis |
| `[[D3_…]] 0.6` | The Paresis Patterns | `[[04_Neurology]]` The Paresis Patterns |

## Digits

`REMOVED {}` on six of seven. §0.6 removed `{'7': 1, '5': 2}`, established correct by
extracting the fragment from HEAD and printing digits **per line**: the `7` is its copy of
the `11_07a` filename and the two `5`s its copies of `L5`, all preserved in §0.4's block one
heading above (`grep`: L5 present ×4, 11_07a present ×1, the S1 line carried).

## One correction to the record

`6e279a3`'s commit message states its digit delta as `{'1': 1, '7': 1, '0': 1, '5': 1}`.
The script printed `{'0': 1, '1': 2, '7': 1, '5': 1}` — two `1`s, from `11_07a`. The figure
was written before the output was read, which is the exact failure rule 11 exists to
prevent. Corrected in `4add9b9`'s message rather than by amending, so the record shows both.
