---
name: Corpus-wide base-A duplicate check
description: Every merged block carrying a SRC: marker, tested against base-A. Includes the three metrics that failed validation.
built: 2026-08-31
status: INCOMPLETE — screening done, 4 of 21 same-file candidates read. Resume point at the end.
---

# Base-A duplicate check — every block carrying a `SRC:` marker

## First correction: there are 137 blocks, not 61

`SRC:` markers across `Corpus A` + `Corpus C`: **142**, of which **5** are claims quoted
inside existing `CONFLICT` blocks and **137** are merged blocks. The 61 figure predates weeks
2 and 3. **This is the fifth sampled count in this project to be wrong when measured** —
after "Corpus C states no doses" (8 of 22 do), "65 backticked references" (276), "42 wikilinks
in C" (195) and "167 placeholder links in B" (798).

## THE METHOD FAILED THREE TIMES BEFORE IT WORKED — read this before trusting any number

The task was framed as mechanical: block text against base-A. **It is not mechanical, and I
have the failures to show it.** Each metric was validated against two blocks whose answers I
already knew — **Barrett** (`13_06b:48`, a confirmed duplicate of base-A `13_06b:41`) and
**Stemmer's sign** (`NEW_Investigations_Haematology_Part2`, `Stemmer` returns **0** in base-A,
so certainly new).

| Metric | Barrett (expect HIGH) | Stemmer (expect LOW) | Verdict |
|---|---|---|---|
| 6-word shingle overlap | **0.0** | **1.0** | **fails both directions** |
| rare-term presence in base-A | 0.917 | excluded | over-flags: **61 of 134 blocks ≥0.90** |
| rare-term locality concentration | **0.417** | — (masked hypertension **0.745**) | **inverted** — ranks a known non-duplicate above a known duplicate |
| **block TITLE words vs base-A** | **2/2 = 1.0** | **9/25 = 0.36** | **passes both** |

**Why the first three fail.** Shingles are brittle against paraphrase: base-A writes *"offer
endoscopic interventions, including radiofrequency ablation and endoscopic mucosal
resection"* and the block writes *"treated endoscopically rather than watched — radiofrequency
ablation and endoscopic mucosal resection"*, and no 6-gram survives. Rare-term overlap
saturates: a long block on a topic the destination file already covers shares that file's
whole vocabulary without duplicating a single claim. Locality concentration then rewards
exactly that saturation, which is why it inverts.

**And the first version had a worse bug than any of them.** My block extractor ended a block
at the next `#` heading. For a block written as a `>` bullet inside a callout, that swallowed
the entire pre-existing section beneath it — so the Stemmer block scored **1.0 against
content it did not contain.** Caught only because `grep Stemmer baseA` returns nothing and
the score said otherwise.

**The metric that works is the one CLAUDE.md rule 2 already prescribes:** *"before merging a
block, grep the destination for the words in your own block's TITLE."* It is the only search
phrased the way a reader would phrase it.

**A title match is a shortlist entry, not a verdict.** Of the four I read, three were false
positives — the title words matched, the content did not.

## Screening result

134 blocks scored (3 had too few title keywords to score). **21 blocks match densely in their
own destination file**, which is the Barrett shape. **4 read so far:**

| Block | Title | base-A match | Verdict |
|---|---|---|---|
| `13_06b:48` | Barrett's management | `13_06b:41` | **DUPLICATE — disagreement buried** (below) |
| `01_Cardiovascular:369` | coronary vasospasm (Prinzmetal) | `01_Cardiovascular:524` | **PARTIAL DUPLICATE** — base-A names *"Prinzmetal angina (coronary artery spasm)"* as **one item in an ST-elevation causes list**. The entity was named; the block supplies the substance. No disagreement found |
| `03_Gastrointestinal:1085` | rectal foreign body | `03_Gastrointestinal:931` | **GENUINELY NEW** — base-A hit is *"rectal foreign bodies"* in a **risk-factor list for anal fistula** |
| `06_Metabolic:385` | the adrenal incidentaloma | `NEW_Investigations_Endocrine:126` | **GENUINELY NEW** — base-A mentions *"hypertension with an adrenal incidentaloma"* as an **indication for aldosteronism screening**, not the workup |
| `01_Cardiovascular:80` | why radial, and what femoral access does | `01_Cardiovascular:58` | **GENUINELY NEW** — base-A says only *"Obtain radial access (preferred to femoral)"*; the block is about **access complications** (retroperitoneal haematoma, pseudoaneurysm) |

## The two confirmed duplicates, and the disagreements in them

### 1. Barrett — `13_06b:48`. **DUPLICATE, DISAGREEMENT BURIED.**

base-A `13_06b:41` already read: *"**Mx:** high-dose PPI (evidence uncertain). If metaplasia
confirmed — endoscopic surveillance with biopsies **every 3–5 years**. If dysplasia — offer
endoscopic interventions, including radiofrequency ablation and endoscopic mucosal
resection."*

The block asserts the destination *"stops there"* and restates both claims. The one new
element is that the interval depends on **segment length and dysplasia grade** — which
**contradicts base-A's flat 3–5 years** and went in as an addition.

**Conflict not yet raised** — the user approved CF-038 for the C1 rebound disagreement only.
**Suggested CF-039, R2** (a surveillance interval drives disposition). Not adjudicated.

### 2. C1 §0.2 — `03_Gastrointestinal:1660`. **DUPLICATE, DISAGREEMENT BURIED → CF-038, raised.**

Duplicates base-A `NEW_Gastroenterology_and_Hepatology:19–40` across roughly 40 claims.
The disagreement: base-A `:36` instructs the examiner to elicit **rebound**; the block says
rebound *"should largely be abandoned."* **`CF-038` markers written at both claims.**

**Note the shape:** this duplicate is **cross-file** — the original is in Corpus C, not the
destination file — so the same-file filter above does **not** surface it. Cross-file
candidates still need working through.

## What the evidence says so far about scale

The user's expectation was C1-scale rather than Barrett-scale. **The evidence to date does not
support C1 being typical.** Of the five files audited claim-by-claim, **C2, C3 and C4 tested
completely clean against base-A**, and C4 contains the model for *avoiding* duplication. C1 is
so far an outlier, and its cause is specific and known: **its gap check searched Corpus A
alone**, and the file it duplicated lives in Corpus C — the exact failure CLAUDE.md rule 10
already records for C1.

That is a reason to prioritise **cross-file** screening over same-file for the remaining work.

## RESUME POINT

- **Done:** 137 blocks enumerated; 134 screened by title; 21 same-file candidates identified;
  4 read; 2 duplicates confirmed (both previously known); CF-038 raised.
- **Next:** read the remaining **17 same-file candidates**, then screen **cross-file**
  candidates — weighting Corpus C destinations, since that is where C1's duplicate hid.
- **Nothing deleted, nothing adjudicated.**
- Scripts: `blocks.py` (extractor, fixed), `title.py` (the validated screen), and the three
  failed scorers kept in the scratchpad as the record of what does not work.
