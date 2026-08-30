# START HERE

Final workflow for consolidating Corpora A, B and C.

Two earlier drafts are superseded and should be deleted: `WORKFLOW.md` (named
`Medications_Reference.md` as the canonical dose owner, which reading that file disproved)
and `RUNBOOK.md` (a competing phase driver, replaced by `MERGE_STEPS.md` once
`MASTER_VERIFICATION_WORKFLOW.md` turned out to already have 26 steps, a queue and a
trigger word).

---

## The document set

| File | What it is | Who reads it |
|---|---|---|
| **START_HERE.md** | This. Gather list, first actions, time estimates. | You, once |
| **MERGE_STEPS.md** | Steps 27–31, appended to `MASTER_VERIFICATION_WORKFLOW.md`. Run with `next`. | The agent, every session |
| **CLAUDE.md** | Your existing rules 1.1–1.5 verbatim, plus merge rules as 1.6–1.14. **Already merged — drop in as-is.** | The agent, every step |
| **merge_tools.py** | Deterministic scans. Stdlib only, no network, no AI. | Invoked by phases |
| **MERGE_SPEC.md** | Design rationale — why each decision was made. | You, when a rule seems wrong |
| **WORKED_EXAMPLE_appendicitis.md** | The convention applied to a real A/B overlap. | You, once, to sanity-check the format |

---

## Step 1 — Gather (30 min)

Everything into one git repo.

**The corpora:** ~150 Corpus A · 37 Corpus B · 53 Corpus C.

**Infrastructure you already have:**
- `CLAUDE.md` — **already merged for you.** Your §1.1–1.5 are verbatim and §1.3's rule
  numbering is untouched, since Corpus C cites "rule 8" by number. Merge rules are appended
  as §1.6–1.14. Diff it against your copy before committing.
- `PENDING_GUIDELINE_CHECKS.md` — 65 rows, append-never-delete. **No script writes this.**
- `MASTER_VERIFICATION_WORKFLOW.md` — the 26-step method. **Phase 0 halts without it.**
- `Medications_Reference.md` — class pharmacology, not a dose reference
- `checklist.csv` — 872 topics, 24 categories. Read with `encoding='utf-8-sig'`.

**New files:** `MERGE_STEPS.md` (paste into `MASTER_VERIFICATION_WORKFLOW.md`), `MERGE_SPEC.md`, `scripts/merge_tools.py`, and this file.

```bash
cd /path/to/vault
git init && git add -A
git commit -m "Baseline: corpora A, B, C untouched"
git tag base-A          # never amend
```

Then push to GitHub:

```bash
git remote add origin <your-repo>
git push -u origin main --tags
```

---

## Step 2 — Append the merge steps, then run `next`

**One phase = one session = one branch = one PR.** Web sessions can only push to their own
working branch, so each phase produces a PR you review on GitHub and merge.

**These steps append to your existing workflow — they do not replace it.** Paste Steps 27–31
into `MASTER_VERIFICATION_WORKFLOW.md` and the queue entries into §1.1. The trigger stays
**`next`**, as it already is. A second driver with its own trigger word would give you two
queues that disagree.

Start a session on the repo and say **`next`**. Read the report, review the PR, merge, then
start the next session and say `next` again.

Session context does not carry between sessions — `_meta/RUN_STATE.md` is what makes this
work, and every phase commits it.

### The sync rule that will bite you if you ignore it

You will be stamping conflict resolutions in Obsidian during study while PRs sit open on
the same files. **A merge conflict in clinical markdown is the worst failure mode here**,
because resolving one badly loses a correction silently and nothing detects it.

- Pull `main` into Obsidian **before** every study session
- Push Obsidian edits **before** starting a Claude Code session
- Never leave a PR open on files you are actively studying
- Resolve any conflict on a computer, never on the phone

### Guidelines cannot be fetched from the sandbox

Web sessions are network-proxied, and Australian primary sources are the same ones your
corpus already records as egress-blocked. **No phase fetches a guideline.** Phases flag
what needs checking, and names an open Australian source where one exists.

| Step | What | Your involvement |
|---|---|---|
| **11** *(existing)* | AU drug dosing and product names | one confirmation per fix |
| **17** *(existing)* | UK-localisation sweep | judge each hit |
| **27** | Trust and population frontmatter, ~240 files | review the unsure list |
| **28** | Verification-scope audit — retrofit `NOT checked:` | review per file |
| **29** | Corpus C remediation and integration | six to eight sessions |
| **30** | Corpus B merge, one file per session | destination table, then per-section commits |
| **31** | Conflict adjudication | yours, during study |

Steps 1, 8, 12, 14, 19, 20 and 25 already cover structural integrity, citation accuracy,
cross-file consistency, guideline currency and the final sweep. **The merge steps do not
repeat them.**

Step 27 touches no clinical claim, so it runs start to finish. Step 30 is where real review
begins, deliberately.

---

## Time

**Per Corpus B file** (~30 KB, ~10 sections) — the only unit that generalises, since GI has
seven B files and most systems have one or two:

| | Agent | You |
|---|---|---|
| Destination table, merge, commits | 20–40 min | 10 min on the table, 20–30 min on the diff |
| Conflicts raised: 5–15, of which 2–4 R1 | — | 5–10 min each, **spread through study** |

**≈ 1 hour concentrated + 30–90 min adjudication spread across the week.**

**Per system:**

| System | B files | Concentrated | Realistic span |
|---|---|---|---|
| Gastroenterology | 7 | 7–9 h | **3–4 weeks** |
| Typical | 1–2 | 1–2 h | 1 week |

**Front-loaded, before any B merge:**

| Phases | Time |
|---|---|
| 0–4 — setup, frontmatter, population, scans | 1.5 h |
| 5 — drug naming | 1 h |
| 6 — C remediation | 2–3 h |
| 7 — C integration | 4–5 h |
| **Total** | **9–11 h** |

At 3 h/week that is all of September.

---

## What to actually do before 27 September

Run **phases 0 through 5**. That is about 3 hours and gets you:

- every file honestly labelled, so `inherited` content stops reading as verified
- the R1 backlog visible as draft rows for your tracker
- UK drug naming fixed corpus-wide — the highest risk reduction per minute available

**Then stop building and study.** Defer phases 6–9 to October, after the MCQ.

The reasoning: GI alone is three to four weeks of merging, so it is not a pre-exam project
whichever way you cut it. A labelled corpus is much safer than what you have now. A merged
corpus is a better artefact, but it is not what passes the exam in four weeks.

If you want one B file merged before the MCQ, make it the system you are weakest on, and
merge exactly one.

---

## Three things that will bite you

**Scans produce false positives and false negatives.** I found three bugs in
`merge_tools.py` by running it against your own files — an unanchored regex that read an
example stamp as a real resolution, `Child-Pugh` matching the paediatric `child` signal, and
markdown emphasis defeating word matching. Your rule 3 predicts this rate. Treat every hit
as something to verify, and the dismissal ratio as the signal of whether a run was careful.

**Agreement between A and B is not corroboration.** They share ancestry. A model asked
about appendicectomy prophylaxis would likely reproduce A's `co-amoxiclav + metronidazole`
and agree perfectly. Only a named Australian source closes a verification item.

**Pointers can fail silently.** Your own B50 is the case: two files point at `09_01` as
owner of the ASCIA adrenaline table, the table stopped at 7.5 kg, and a reader following the
pointer for an infant reached a table that did not cover them. That is why `_meta/OWNERS.md`
records the range each owner table covers, not just its location.
