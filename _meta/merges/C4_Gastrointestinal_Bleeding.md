---
name: C4 placement record
description: Where each section of C4_Gastrointestinal_Bleeding was placed under the section-level merge rule, and why.
bfile: Corpus B/C4_Gastrointestinal_Bleeding.md
rule: section-level merge
built: 2026-08-31
---

# C4_Gastrointestinal_Bleeding — placement record

| § | Section | Destination | Why |
|---|---|---|---|
| 0.1 | Framework and Resuscitation | `03_Gastrointestinal` §0.33.5 | placed under **§0.33 Upper GI Bleed**, the file's own bleeding entry — the reader arrives from haematemesis or melaena, and the framework governs both upper and lower |
| 0.2 | Upper GI — Non-Variceal | `03_Gastrointestinal` §0.33.4 | superseded the §0.2 fragment, already there |
| 0.3 | Variceal Bleeding | `03_Gastrointestinal` §0.6.7 | superseded the §0.3 fragment, under **§0.6 Alcohol-Related Liver Disease**, where the varices already live |
| 0.4 | Lower GI Bleeding | `03_Gastrointestinal` §0.34.1 | **§0.34 Lower GI Bleed** |
| 0.5 | Occult and Obscure Bleeding, IDA | `03_Gastrointestinal` §0.34.2 | with §0.34: the iron-deficiency workup ends in colonoscopy, and FIT and the screening programme sit with lower GI bleeding |

## Cross-references retargeted

| B link | Retargeted to | Verified |
|---|---|---|
| `[[A9_Transfusion…]] 0.1` | `[[10_08_Haemonc…]]` Massive Transfusion Protocol (MTP) | exists |
| `[[C2_Nausea_and_Vomiting]] 0.7` | §0.41.20 Complications of Vomiting — **merged from C2 earlier today** | exists |
| `[[C3_Jaundice…]] 0.6` | §0.38.1 Complications of Cirrhosis — **merged from C3 earlier today** | exists |

**Left as TODO:** M5 paediatric GI. Unbuilt.

## Connective tissue inherited

**Both supersedes were caught by the driver, not by hand** — this is the first file where the
cross-reference refusal did the work:

- §0.2 → `§0.33.2` (AIMS65 alongside Glasgow-Blatchford and Rockall), and **two `§0.33.3`
  pointers that say what the destination list does not**: that adrenaline injection is
  combined with a second modality rather than being an alternative, and that repeat
  endoscopy → embolisation → surgery is an ordered sequence.
- §0.3 → `§0.6.3`, `§0.6.4` and `§0.33.3` on balloon tamponade, where the destination lists
  the Sengstaken-Blakemore tube without qualifying it as a time-limited bridge.

**The §0.33.4 block remains the worked example of good placement** — AIMS65 named, the
existing scores pointed at, nothing reproduced — and the section merge preserved that shape
rather than flattening it.

## Report

```
sections merged      5
destinations         03_Gastrointestinal × 5 (§0.33 × 2, §0.6 × 1, §0.34 × 2)
new-file proposals   0
conflicts raised     0
cross-refs           3 retargeted, 1 left as TODO
digit multiset       pass — no digits removed on any of the 5 sections
```

**No conflict raised.** C4's figures are withheld behind `UNVERIFIED` markers (transfusion
thresholds, Forrest grades, Glasgow-Blatchford components, timing of aspirin restart), so the
placement figure comparison found nothing numeric to disagree with.
