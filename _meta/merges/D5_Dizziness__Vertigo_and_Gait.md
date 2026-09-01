---
name: D5 placement record
description: Where each section of D5 was placed under the section-level merge rule, and why.
bfile: Corpus B/D5_Dizziness__Vertigo_and_Gait.md
rule: section-level merge
built: 2026-09-01
---

# D5_Dizziness__Vertigo_and_Gait — placement record

Source path verified against the filesystem:
`/home/user/wrhg/Corpus B/D5_Dizziness__Vertigo_and_Gait.md`. A same-prefix file also
exists in `Corpus B-new/`; `Corpus B/` wins on the driver's glob order
(`_meta/audits/SOURCE_PATH_AUDIT.md`).

| § | Section | Placed under | Fragment |
|---|---|---|---|
| 0.1 | The "Dizzy" Patient — Disambiguating the Complaint | `### Vertigo (Peripheral vs Central, BPPV, Vestibular Neuritis)` | none |
| 0.2 | Acute Vestibular Syndrome and the HINTS Examination | same | none |
| 0.3 | Episodic Vertigo | same | none |
| 0.4 | Disequilibrium and Chronic Dizziness | where the fragment stood | **superseded** |
| 0.5 | Gait Disorders | `## Movement Disorders` | none |
| 0.6 | Nystagmus | `## Cranial Nerve Disorders and Vertigo` | none |

**§0.5 is the placement worth stating.** It is a pattern table read from watching the
patient walk, so its neighbours are the movement disorders, not the causes of dizziness.

**§0.2 closes a pointer written two files ago.** D3 §0.5's stroke-chameleon block sends the
reader to *"§Vertigo below and [[Examination]]"* for the isolated-vertigo chameleon. Before
this, the destination mentioned HINTS in one clause of an `Ix:` line; now the pointer
reaches the examination itself.

## §0.4 — where a NO-BASELINE marker was allowed to go, and where it was not

The fragment was **PPPD only** and carried
`` `NO-BASELINE — absent from the corpus before this merge; no inherited layer disagrees
with it.` `` B's §0.4 is disequilibrium and chronic dizziness **generally**, and the
destination has inherited vertigo and falls content behind it.

**The driver's `no_baseline` flag would have emitted that marker on the block heading and
satisfied the protected-marker check.** It would also have made a false claim about the
broader section in order to pass a check about the narrower one. Both markers — NO-BASELINE
and the PPPD `UNVERIFIED` — are attached to the **PPPD callout**, where they remain true.

Also carried: the fragment's delta-framing, *"the same central adaptation that resolves
vestibular neuritis becomes the problem when it does not switch off"*, which links PPPD to
the compensation point above it and exists nowhere in B.

`PPPD` is one of rule 9's recorded collisions — 3 hits in this corpus, **all three
pylorus-preserving pancreaticoduodenectomy**. The abbreviation is expanded in full in the
heading and the first line for that reason.

## THE LOSS ON §0.4, AND THE FALSE CLAIM ABOUT IT

**`fa7aba5`'s commit message says the destination's `**P (vertigo generally):**` line
*"survives (grep count 1)"*. The grep printed 0. The line had been deleted.**

I ran the check, wrote the claim from what I expected, and committed without reading the
output — rule 11's exact failure, and the second time in one session after `6e279a3`'s
digit figure. Restored in `4eedf73`, verbatim from `fa7aba5^`, confirmed byte-identical.

**Nothing could have caught it.** The line has no heading, no `SRC:` token, no protected
marker and no digit:

```
digits added {…} | REMOVED {}
probes missing 0 | NEW duplicate headers 0
OK
```

It is exactly the case the D4 record named as the reason `3f7df30` was luck — *"a block of
plain clinical prose would have gone silently."* It went silently one file later, which is
the argument for fixing the boundary generally instead of adding a third special case.

**The fix (`4c26d92`): a fragment ends at a blank-line RUN.** The block format separates its
own parts by exactly one blank line, so two or more cannot cut a fragment short. Order is
now: blank-line run · next foreign `SRC:` token · next heading.

**The retrospective audit was worthless the first time it was written.** Asking *"is this
removed line still in the tree"* reported **166 of 186 lost** — because a supersede removes
the fragment's prose by design and B's reworded replacement never matches verbatim.
Rebuilt to ask whether the removal extended **past** the fragment:

```
supersede commits scanned: 134 | trailing destination lines removed and now absent: 0
```

and shown able to fail, run against the tree as it stood at `fa7aba5`:

```
*** fa7aba5 Section merge D5 §0.4 — whole section, supersedes
      **P (vertigo generally):** BPPV frequently recurs but responds well to repeat Epley…
AT fa7aba5 (pre-restore): trailing destination lines removed and absent: 1
```

**One case in 134 supersedes, and it is the one restored.**

## Digits

Every section: `REMOVED {}`.
