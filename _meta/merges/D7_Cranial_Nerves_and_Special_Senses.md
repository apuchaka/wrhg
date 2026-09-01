---
name: D7 placement record
description: Where each section of D7 was placed under the section-level merge rule, and why.
bfile: Corpus B/D7_Cranial_Nerves_and_Special_Senses.md
rule: section-level merge
built: 2026-09-01
---

# D7_Cranial_Nerves_and_Special_Senses — placement record

Source path verified against the filesystem:
`/home/user/wrhg/Corpus B/D7_Cranial_Nerves_and_Special_Senses.md`.

| § | Section | Placed under | Fragment |
|---|---|---|---|
| 0.1 | Cranial Nerve Localisation | `## Cranial Nerve Disorders and Vertigo` | none |
| 0.2 | Facial Palsy | `### Bell's Palsy` | none |
| 0.3 | Diplopia and Disorders of Eye Movement | `## Cranial Nerve Disorders and Vertigo` | none |
| 0.4 | Speech, Voice and Swallowing | where the fragment stood | **superseded** |
| 0.5 | Smell and Taste | `## Cranial Nerve Disorders and Vertigo` | none |
| 0.6 | Other Cranial Nerve Syndromes | `## Cranial Nerve Disorders and Vertigo` | none |

**§0.2 under `### Bell's Palsy`** because B's section is facial palsy as a *presentation* —
the upper-versus-lower motor neurone split that decides whether it is Bell's palsy at all,
plus Ramsay Hunt, otitis media, parotid tumour, Lyme and sarcoid — while the destination
entry is the diagnosis.

## §0.4's supersede — what B carries, and the three things it does not

B §0.4 carries the bulbar/pseudobulbar comparison **in full** (fasciculating versus spastic
tongue, jaw jerk, emotional lability) and the write test. So the supersede loses no clinical
claim. What it would have lost is merge-authored:

- **The reasoning.** B stops at *"a fasciculating tongue with brisk reflexes elsewhere is
  motor neurone disease until proven otherwise"*. The fragment said **why** — *"because it
  is the one diagnosis that produces upper and lower motor neurone signs together."*
  The claim without its reason is memorisable; with it, it is derivable.
- **`[[History-Taking]]`**, where the write test lives.
- **The "not repeated here" map** — `§Cranial Nerve Disorders and Vertigo` for the jaw jerk.
  Exactly the connective tissue §1.10 says a supersede must carry, because it exists nowhere
  in Corpus B.

All three inherited. Verified after the write, grep count 1 each, and
`### Horner's Syndrome` — which followed the fragment — survives: **the first supersede
since the blank-line-run boundary fix (`4c26d92`), and it held.**

## THE CITING CLAIM DECIDES THE OWNER — the D6 finding, applied again

`[[A7_Burns__Chemical_Injury__Wounds_and_Crush_Injury]]` is cited in §0.3 for an **orbital
blowout fracture with muscle entrapment**. A7 is burns, chemical injury and crush; nothing
in it is a blowout fracture. This vault's blowout content is at
`13_04_ENT_-_…_Fractures_…:100–104`, including the paediatric **"white-eyed" trapdoor**
variant — which is the emergency the citing sentence is actually pointing at.

Also mapped by claim rather than by file:

| B pointer | Cited for | Owner here |
|---|---|---|
| `[[B6_…]] 0.4` *Eyelid and Facial Swelling* | orbital cellulitis | `[[05_Ophthalmology]]` Orbital and Peri-Orbital Cellulitis |
| `[[D1_…]] 0.4` | secondary headaches | `[[04_Neurology]]` Secondary Headaches Worth Knowing |
| `[[D1_…]] 0.3` | trigeminal neuralgia | `[[04_Neurology]]` Trigeminal Neuralgia |
| `[[D6_…]] 0.5` | parkinsonism | `[[04_Neurology]]` Parkinsonism |
| `[[C6_…]] 0.3` | oesophageal dysphagia | `[[13_06b_…]]` §0.3.1 Oesophageal Disease |

By D7, **every `[[D*]]` pointer resolves to a block merged earlier in this run** — so the
D-block's internal cross-references now reach content that exists rather than the B files
they were written against.

## One marker deliberately left

§0.3 keeps `` `TODO:link — L8 Facial, head & torso trauma (unbuilt)` ``. The `(unbuilt)`
claim is false — `L8_Facial__Head_and_Torso_Trauma.md` exists in `Corpus B-new/` (`f974630`)
— and it stays with the other 33 for the scheduled correction after the B-new merges
(`d92d36a`). The blowout pointer beside it already reaches a real destination, so nothing is
unreachable meanwhile.

## Digits

Every section: `REMOVED {}`.
