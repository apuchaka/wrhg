---
name: D1 destination table
description: Where every section of Corpus B/D1_Headache_and_Meningism.md goes, including the sections that were discarded.
bfile: Corpus B/D1_Headache_and_Meningism.md
built: 2026-08-31
---

# D1_Headache_and_Meningism — destination table

Committed **before** any content was written. 5 051 words, 6 sections.
**1 placement · 5 discards.** The most heavily superseded file of either block so far.

`04_Neurology` is **28 637 words** — larger than `03_Gastrointestinal` — and its first
eight sections are headache. `NEW_Neurology` (Corpus C, `snippet`) covers much of the
rest. **All 33 of D1's callout topics were tested; 32 were already present.**

## The eponym check, run as now required by Step 29

Every named instrument was searched **by its components as well as its name**.

| Instrument | Name search | Component search | Verdict |
|---|---|---|---|
| SNOOP4 red flags | found | *red flag* + *headache* found | present |
| Hunt and Hess | **absent** | *grade* + *nuchal rigidity/drowsy* **absent** | **genuinely absent** |
| Fisher grade | found | *blood in cisterns* found | present |
| Kernig / Brudzinski | found | *neck flexion → hip*, *passive knee extension* found | present |
| Glasgow Coma Scale | found (`04_Neurology` §GCS) | — | present |
| CSF interpretation | found | *protein/glucose* × *bacterial/viral* found | present |

**No eponym trap fired on D1** — every present instrument was found by name too. The check
cost little and would have caught the C7-class error had one existed.

**One false flag from my own detector, recorded so it is not mistaken for a finding:**
`dexamethasone in meningitis` showed "name absent, components present in 23 files". The
component pattern was the bare word `dexamethasone`, which appears throughout the corpus
for unrelated indications. A component pattern has to be **specific to the instrument**,
or it flags everything. Not a trap; a badly written check.

## A gap D1 does not close

**Hunt and Hess grading of subarachnoid haemorrhage** is absent from the whole vault — and
**D1 does not mention it either**, nor WFNS, nor any SAH grading scale. `04_Neurology`
§SAH is otherwise thorough (the 6-hour CT rule, the ≥12-hour LP for xanthochromia,
nimodipine, coiling versus clipping, definitive management within 24 h). Recorded and
added to the study list, not written from memory — the fourth such entry after
Dubin-Johnson, Rotor and Schatzki ring.

## A structural finding, reported rather than fixed

**`History-Taking.md` — the presentation-led file, Template A — has no headache entry.**
31 headings, including *Confusion, Disorientation and Altered Conscious State* (§1.17) and
*Fever and Suspected Infection* (§1.22), but nothing for headache, the commonest
neurological presentation there is. Not a merge item: creating a new §1.x in the
presentation-led file is a structural decision, not an additive block.

## Destination table

| D1 § | Topic | Destination | Disposition |
|---|---|---|---|
| 0.1 | Headache framework, SNOOP4, onset speed, the examination | — | **DISCARD** — `04_Neurology` §Other Headache Causes L135 has the red flags, and onset speed is in `NEW_Neurology` |
| 0.2 | Thunderclap and SAH | — | **DISCARD** — `04_Neurology` §SAH is more detailed, including the 6-hour and 12-hour rules D1 lacks |
| 0.3 | Primary headache disorders — migraine, aura, triptans, cluster, TACs, trigeminal neuralgia | — | **DISCARD** — §Migraine, §Trigeminal Autonomic Cephalalgias, §Cluster Headache, §Tension Headache, §Trigeminal Neuralgia; the aura-versus-TIA-versus-seizure distinction is already in `04_Neurology`, and migraine-with-aura versus the COC is in `NEW_Drugs_16` |
| 0.4 | Secondary headaches — GCA, IIH, CVST, MOH, intracranial hypotension, raised ICP | — | **DISCARD** — §Temporal Arteritis, §Medication Overuse Headache, §Brain Tumours; IIH, CVST and spontaneous intracranial hypotension are all in `NEW_Neurology` |
| 0.5 | Meningism, meningitis, encephalitis, CSF | — | **DISCARD** — §CNS Infections is 130 lines covering bacterial and viral meningitis, encephalitis, brain abscess, spinal epidural abscess and §CSF Interpretation |
| 0.6 | **Neck stiffness — the differential** | `Corpus A/04_Neurology.md`, after §CNS Infections | **ADDITIVE** |

## What the one placement actually adds, stated honestly

**Every constituent of the neck-stiffness differential already exists — in nine different
files.** Atlantoaxial instability is in `15_20a` and `NEW_Investigations_Orthopaedics`;
Lemierre in `08_09` and `13_05a`; retropharyngeal abscess in `NEW_ENT_and_Oral` and
`NEW_Respiratory`; tetanus in `08_01-03`; acute dystonic reaction in `14_03` and
`NEW_Drugs_12`; discitis in `04_Neurology` and `08_09`.

**The addition is the assembly, not the facts.** A patient presents with a stiff neck, not
with a diagnosis, and nothing in the vault answers that presentation in one place. This is
the same case as `03_Gastrointestinal` §0.41 — a presentation-organised section inside a
disease-organised file — and §1.10 names it explicitly. Recorded this way so nobody later
reads it as new clinical content.

No new file required. **No `CONFLICT` raised** — D1 contradicts nothing.
