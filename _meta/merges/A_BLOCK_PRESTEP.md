---
kind: prestep
block: A1–A5, A9, A10 (emergency and acute care)
against: the emergency files across Corpus A and Corpus C
date: 2026-08-31
tooling: scripts/gapcheck.py
---

# A-block pre-step — named emergency instruments

Run before merging A1–A5, A9 and A10, per the standing instruction: check the named
decision rules and scores against the emergency files **specifically**, with digit folding
and with the rule 9 anchoring the B-block pre-step learned the hard way.

## Result

| Instrument | raw | anchored | Verdict |
|---|---|---|---|
| **Wells** | 16 | 16 | **Present** — `01_Cardiovascular.md` §0.29/§0.30, both DVT and PE |
| **PERC** | **243** | **2** | **Present** — `01_Cardiovascular.md:1073`, with the logic that *all* criteria must be **absent** |
| **GRACE** | 2 | 2 | **Present** — `01_Cardiovascular.md:74` |
| **Ottawa** | 7 | 7 | **Present** — ankle and knee rules |
| **Canadian C-Spine** | 1 | 1 | **Present** — `NEW_Investigations_Orthopaedics_Neurology_and_Other.md:189` |
| **NEXUS** | 1 | 1 | **Present** — same line, as the alternative rule |
| **qSOFA** | 2 | 2 | **Present** — `08_09_Infectious_Disease_-_Miscellaneous.md:159` |
| **Glasgow Coma Scale** | 5 | 5 | **Present** |
| **NEWS** | 11 | 9 | **Present** |
| **Centor** | 11 | 11 | **Present**, with the Australian caveat at `13_05a` |
| **CURB** | 5 | 5 | **Present** |
| **Alvarado** | 7 | 7 | **Present** |
| **Parkland / Rule of Nines** | 3 | 3 | **Present** — `11_09b_Ortho_-_Trauma.md:90`, **with the paediatric correction at `:94`** |
| **TIMI** | **203** | **0** | **ABSENT** |
| **PECARN** | 0 | 0 | **ABSENT** |
| **HAS-BLED** | 0 | 0 | **Absent BY DESIGN** — the vault uses **ORBIT**, in full, at `01_Cardiovascular.md:280`. See the B-block pre-step correction |
| **Wallace rule of nines** (by that name) | 0 | 0 | **Name absent, concept present** — not a gap |

## The two rule 9 artifacts, and why they matter

| Pattern | raw | What it matched | anchored |
|---|---|---|---|
| `TIMI` | **203** | **timi**ng — *"ANZCOR **timi**ng"*, *"adrenaline **timi**ng"*, *"drug **timi**ng in cardiac arrest"*, *"Austroads **timi**ng"* | **0** |
| `PERC` | **243** | hyper**c**holesterolaemia, hyper**C**a, hyper**c**alcaemia, **perc**ussion, **perc**utaneous | **2** |

**`TIMI` is the more dangerous of the two, and in the more dangerous direction.** 203 hits
reads unambiguously as "thoroughly covered". Anchored, it is **zero** — the TIMI score is
absent from the vault entirely. **An unanchored search here produces a false PRESENT**, which
is the direction nothing downstream catches (rule 9).

That both artifacts landed on **emergency scoring instruments**, in a pre-step whose entire
purpose is to check emergency scoring instruments, is the point: the substring trap is not
an occasional nuisance, it is **the default behaviour of the method being used.**

## What this predicts for the merge

**A1–A5, A9 and A10 will yield few named-instrument additives.** Thirteen of seventeen
instruments are present, one is absent by design, and one is a naming variant. Only **TIMI**
and **PECARN** are real absences, and both are single scores rather than domains.

**So the yield, if there is one, will be in mechanism and discriminators rather than named
tools** — which is where B1–B6 actually paid off too: unopposed alpha in the disease context,
the diagnostic half of RV infarction, why Mobitz II resists atropine, why rapid BP lowering
harms. The named-instrument check is worth running to *avoid duplicates*, not to find gaps.

## Method note

Every count above came from `gapcheck.py` — untruncated, destination corpora only. The raw
column is the unanchored pattern and the anchored column is `\bX\b`. **Both are recorded**
because the ratio is the signal (rule 3), and because 203→0 is the single most extreme
artifact this project has recorded.
