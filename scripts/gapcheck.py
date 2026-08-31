#!/usr/bin/env python3
"""gapcheck.py — the ABSENT-verdict search path, which cannot truncate.

Standard library only. No network. Every operation is a regex over files you can read.

WHY THIS EXISTS
---------------
CLAUDE.md rule 2 has always prohibited concluding absence from truncated output. It was
violated twice in one block (B3, B4 — 2026-08-31) by someone who had, the same day, written
the rule against it. A written prohibition did not hold, so the verdict path gets a tool
that makes the failure impossible rather than merely forbidden:

  * every matching line is printed IN FULL — there is no --limit, no --head, no width cap,
    and none will be added. Truncation is the defect this file exists to prevent.
  * a zero result is NOT reported as ABSENT. It triggers the rule 2 component re-search and
    prints the retry commands, because rules 9 and 10 passing is exactly when rule 2 is the
    backstop.
  * a pattern that looks like a PROXIMITY or PHRASE search is rejected before it runs
    (rule 10, ADJACENCY and PARAPHRASE clauses).

USAGE
    python3 scripts/gapcheck.py 'micturition'
    python3 scripts/gapcheck.py 'atrial stunning' --allow-phrase
    python3 scripts/gapcheck.py 'shear' --dirs "Corpus A" "Corpus C"
"""
import argparse
import os
import re
import sys

DEFAULT_DIRS = ["Corpus A", "Corpus B", "Corpus C"]

# Words too common in medical prose to carry a search on their own. Used to pick the rarest
# term for the rule 2 retry, not to reject anything.
COMMON = {
    "the", "a", "an", "and", "or", "of", "in", "on", "to", "is", "are", "was", "be", "not",
    "with", "for", "by", "at", "from", "it", "its", "this", "that", "these", "those",
    "patient", "patients", "cause", "causes", "caused", "acute", "chronic", "severe",
    "risk", "high", "low", "blood", "pressure", "heart", "rate", "disease", "syndrome",
    "management", "treatment", "diagnosis", "clinical", "common", "history", "test",
    "normal", "abnormal", "level", "levels", "own", "usual", "baseline", "relative",
}

RE_PROXIMITY = re.compile(r"\.\{\d*,\d+\}|\.\*")


def looks_like_phrase(pattern):
    """Two or more non-common words separated by a literal space, outside a character class."""
    bare = re.sub(r"\[[^\]]*\]", "", pattern)
    for alt in bare.split("|"):
        words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]{2,}", alt)]
        meaningful = [w for w in words if w.lower() not in COMMON]
        if " " in alt.strip() and len(meaningful) >= 2:
            return True
    return False


def rarest_term(pattern):
    words = re.findall(r"[A-Za-z][A-Za-z'-]{3,}", pattern)
    meaningful = [w for w in words if w.lower() not in COMMON]
    if not meaningful:
        return None
    return max(meaningful, key=len)


def md_files(dirs):
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith(".md"):
                yield os.path.join(d, name)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern", help="regex, case-insensitive")
    ap.add_argument("--dirs", nargs="+", default=DEFAULT_DIRS)
    ap.add_argument("--allow-phrase", action="store_true",
                    help="permit a multi-word or proximity pattern. Use only AFTER the "
                         "single-word search has been run and read.")
    args = ap.parse_args()

    if not args.allow_phrase:
        if RE_PROXIMITY.search(args.pattern):
            rare = rarest_term(args.pattern)
            print("REFUSED — proximity pattern (rule 10, ADJACENCY clause).\n"
                  "  A `.{0,N}` or `.*` asserts the corpus puts your two terms near each "
                  "other. It frequently does not.\n"
                  f"  Search the rarer term alone first:  python3 scripts/gapcheck.py "
                  f"'{rare or '<rarer-term>'}'\n"
                  "  Then re-run with --allow-phrase if you still need the proximity form.")
            return 2
        if looks_like_phrase(args.pattern):
            rare = rarest_term(args.pattern)
            print("REFUSED — phrase pattern (rule 10, PARAPHRASE clause).\n"
                  "  The corpus rewords. A phrase is the author's; the concept is not.\n"
                  f"  Search its least-common word alone first:  python3 "
                  f"scripts/gapcheck.py '{rare or '<rarest-word>'}'\n"
                  "  Then re-run with --allow-phrase if you still need the phrase form.")
            return 2

    rx = re.compile(args.pattern, re.I)
    hits = []
    for path in md_files(args.dirs):
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if rx.search(line):
                    hits.append((path, i, line.rstrip("\n")))

    print(f"gapcheck: {len(hits)} hit(s) for /{args.pattern}/ in {', '.join(args.dirs)}")
    print("Every line below is printed IN FULL. There is no limit flag and none will be "
          "added — truncation is the defect this tool exists to prevent.\n")
    for path, i, line in hits:
        print(f"{path}:{i}: {line}")

    if not hits:
        rare = rarest_term(args.pattern)
        print("\nZERO HITS — this is NOT an ABSENT verdict yet (rule 2).")
        print("  Rules 9 and 10 passing is exactly when rule 2 is the backstop. Before "
              "recording ABSENT, run the component re-search:")
        print(f"    1. the rarest word bare        : python3 scripts/gapcheck.py "
              f"'{rare or '<rarest-word>'}'")
        print("    2. a distinctive letter-run     : e.g. 'aemolysis' for '**H**aemolysis' "
              "(rule 2, markdown emphasis)")
        print("    3. spelling and naming variants : ae/e, -ise/-ize, AU vs international "
              "drug name, acronym vs expansion")
        print("    4. the CONCEPT, not the phrase  : what would the corpus call this if it "
              "used different words?")
        print("  Record which of these you ran. A zero result you did not re-search is not "
              "a finding.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
