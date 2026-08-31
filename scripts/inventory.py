#!/usr/bin/env python3
"""Enumerate named scores, eponyms and instruments in files, with digit folding.

WHY THIS EXISTS
    Two scores were nearly merged as gaps because ASCII searches could not see their
    Unicode digits: `ABCD²` (superscript) in 04_Neurology and `CHA₂DS₂-VASc` (subscripts)
    in 01_Cardiovascular. Either merge would have put one instrument in the corpus twice
    under two renderings — and in a DIFFERENT FILE from the original, where nothing puts
    the two side by side.

    On its first real use it caught four false PRESENT verdicts on A6: `active cooling` and
    `rewarming` matched malignant hyperthermia, `frostbite` matched cold injury from
    inhaling gas canisters, and `drowning` matched a postnatal cause of cerebral palsy.

WHAT IT IS FOR
    Run it over a destination file BEFORE searching for a claim, so the claim is checked
    against the instruments the file actually contains rather than against a guessed
    search string. Required by MASTER_VERIFICATION_WORKFLOW.md Step 29 before merging
    B1-B6 against 01_Cardiovascular, and A1-A5/A9/A10 against the emergency files.

WHAT IT IS NOT
    It does not decide anything. It is deliberately over-inclusive: it will return
    all-caps prose and section codes alongside real instruments. CLAUDE.md rule 3 applies
    to every hit — read it before treating it as anything.

USAGE
    python3 scripts/inventory.py "Corpus A/01_Cardiovascular.md" [more files...]
    python3 scripts/inventory.py --corpus A          # every file in Corpus A
    python3 scripts/inventory.py --compare FILE_A FILE_B   # what B has that A does not
"""
import os
import re
import sys
import collections

SUBSUP = "₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹"
UNICODE_DIGITS = str.maketrans(SUBSUP, "01234567890123456789")


def fold(text):
    """Strip markdown emphasis and fold Unicode digits to ASCII.

    Mirrors merge_tools.normalise(). Kept separate so this script has no import
    dependency on it — the two must agree, and a divergence here is a defect.
    """
    text = re.sub(r"[*_`]", "", text)
    return text.translate(UNICODE_DIGITS)


# An eponym: Capitalised word(s), optionally hyphenated or possessive, followed by a
# word that marks it as a named instrument.
EPONYM = re.compile(
    r"\b([A-Z][a-z]+(?:[-–][A-Z][a-z]+)*(?:'s)?)\s+"
    r"(score|scale|criteria|criterion|sign|rule|index|classification|"
    r"test|law|triad|manoeuvre|maneuver|syndrome|reflex|phenomenon)\b"
)
# Digits may be INTERSPERSED, not just trailing. Found 2026-08-31 in this script's own
# self-test: the first version required letters-then-digits, so after folding it saw
# ABCD2 but NOT CHA2DS2-VASc — the very score it was written to catch. A tool that misses
# its own worked example is worse than no tool, because it reports a clean inventory.
ACRONYM = re.compile(r"\b([A-Z][A-Z0-9]{2,}(?:[-–][A-Za-z0-9]{2,})*)\b")

# Common clinical abbreviations and English words that are not named instruments.
# Extended 2026-08-31 from what the first runs actually returned — the all-caps prose
# (FIRST, WHY, MULTIPLE, VERTEBRAL, MEDICATIONS) was pure noise and is now filtered,
# while genuinely ambiguous ones are LEFT IN so a human reads them.
STOP = {
    # English words that appear capitalised for emphasis in this corpus
    "AND", "THE", "FOR", "NOT", "BUT", "ALL", "ANY", "NEW", "OLD", "WHY", "HOW", "WHO",
    "FIRST", "NEVER", "ALWAYS", "MULTIPLE", "INCREASE", "MEDICATIONS", "VERTEBRAL",
    "FRACTURES", "STOP", "START", "DO", "NO", "YES", "ONE", "TWO",
    # project markers
    "TODO", "SRC", "UNVERIFIED", "VERIFIED", "CONFLICT", "PENDING",
    # routine clinical abbreviations, not instruments
    "ECG", "EEG", "EMG", "CT", "MRI", "US", "CXR", "AXR", "DXA", "PET",
    "IV", "IM", "IO", "PO", "SC", "PR", "NG", "NBM", "PRN",
    "GP", "ED", "ICU", "HDU", "OT", "MDT", "GCS", "BP", "HR", "RR",
    "FBC", "UEC", "LFT", "CRP", "ESR", "INR", "APTT", "ABG", "VBG", "TFT",
    "AF", "DVT", "PE", "MI", "ACS", "COPD", "CKD", "AKI", "UTI", "GORD", "IBD",
    "IBS", "TIA", "SAH", "ICH", "MND", "MS", "PD", "AD", "NMS", "PPI", "NSAID",
    "SSRI", "SNRI", "TCA", "MAOI", "ACE", "ARB", "CCB", "BNP", "VTE", "DOAC",
    "OSCE", "AMC", "AU", "UK", "USA", "WHO",
}


def instruments(paths):
    found = collections.defaultdict(list)
    for path in paths:
        text = fold(open(path, encoding="utf-8").read())
        base = os.path.basename(path)
        for i, line in enumerate(text.split("\n"), 1):
            for m in EPONYM.finditer(line):
                found[f"{m.group(1)} {m.group(2)}"].append((base, i))
            for m in ACRONYM.finditer(line):
                a = m.group(1)
                if a in STOP or len(a) < 3:
                    continue
                found[a].append((base, i))
    return found


def show(found, title):
    print(f"{title}: {len(found)} candidates "
          f"(over-inclusive by design — read every one, rule 3)\n")
    for k in sorted(found):
        locs = found[k]
        where = "; ".join(f"{f}:{l}" for f, l in locs[:2])
        more = f" (+{len(locs) - 2})" if len(locs) > 2 else ""
        print(f"  {k:32} {where}{more}")


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    if argv[0] == "--corpus":
        d = f"Corpus {argv[1]}"
        paths = [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]
        show(instruments(paths), d)
    elif argv[0] == "--compare":
        a, b = instruments([argv[1]]), instruments([argv[2]])
        only = {k: v for k, v in b.items() if k not in a}
        show(only, f"in {os.path.basename(argv[2])} but NOT {os.path.basename(argv[1])}")
    else:
        show(instruments(argv), "inventory")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
