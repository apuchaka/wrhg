---
name: CF-038, and the worked example of good placement
description: The rebound-tenderness disagreement buried in C1's merge, and the C4 block that shows how to handle an overlap instead.
built: 2026-08-31
---

# CF-038 — rebound tenderness **R3**

Approved by the user, 2026-08-31. Markers written inline at both claims; **not adjudicated.**

**A (`snippet`)** — `Corpus C/NEW_Gastroenterology_and_Hepatology.md:36`, present in base-A:
> *"**Palpate** gently and away from the pain first: guarding, rigidity, **rebound** and
> percussion tenderness…"*

**B (`unverified`)** — `Corpus A/03_Gastrointestinal.md:1671`, merged from
`SRC:C1_Acute_Abdomen §0.2`:
> *"**Percussion tenderness rather than rebound.** Gentle percussion elicits the same
> information as releasing deep palpation, is far kinder, and is more reproducible.
> **Rebound testing is unpleasant, poorly reproducible and should largely be abandoned.**"*

**Why it matters:** A instructs the examiner to elicit a sign that B says to stop eliciting.
Both are instructions about what to do to a patient at the bedside, and a reader meeting only
one of them will not know the other exists.

**How it was buried:** B was merged as an **addition**. The gap check that authorised it did
not search Corpus C, where A lives — the failure CLAUDE.md rule 10 already records for C1.
Because the merge was additive rather than superseding, **no conflict was raised and no
marker was written**, so nothing downstream could detect it.

**Resolve against:** an Australian surgical or clinical-examination source — RACS resources,
or a current clinical examination text. Not adjudicated here.

Digit multiset: `0`, `3`, `8` added on each side — the conflict ID only. No clinical figure.

---

# The worked example of good placement — C4 §0.33.4

**This is the Barrett failure avoided, for free, and the section merge should reach for it
wherever an overlap is obvious rather than defaulting to duplication.**

`Corpus A/03_Gastrointestinal.md`, `SRC:C4_Gastrointestinal_Bleeding §0.2`:

> **AIMS65** is a further pre-endoscopy risk score alongside the Glasgow-Blatchford and
> Rockall scores **already at §0.33.2**.

Glasgow-Blatchford and Rockall were **already in base-A** — at `03_Gastrointestinal` §0.33.2
and again at `NEW_Gastroenterology_and_Hepatology:69`. The block:

1. **names what it adds** — one score, AIMS65;
2. **points at what already exists**, by section number;
3. **reproduces none of it.**

Contrast the Barrett block, which opened *"§0.3 above gives the definition, risk factors and
diagnosis and **stops there**"* when `13_06b:41` carried the management — high-dose PPI,
surveillance every 3–5 years, and endoscopic treatment of dysplasia including radiofrequency
ablation and endoscopic mucosal resection. Two claims were re-merged near-verbatim, and the
one genuinely new element — that the interval depends on **segment length** rather than being
a flat 3–5 years — is a **disagreement** that went in as an addition.

**The rule the example gives the section merge:** when the destination already covers part of
what a block says, write the pointer and merge only the remainder. The cost is one clause. The
cost of not doing it is a duplicate that buries a disagreement nothing downstream will find.
