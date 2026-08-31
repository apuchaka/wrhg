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
  * hits are grouped by corpus, and a result whose hits ALL sit in the SOURCE corpus is
    reported as ZERO with a loud warning. A merge gap check that matches the B file being
    merged has found itself, not the destination — a false PRESENT, which is the silent
    direction nothing downstream catches (rule 9). Found 2026-08-31 by running this tool on
    B5: six real gaps read as "present", every hit a self-match.

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


def search(pattern, dirs):
    """Every matching line, in full. The one place a search happens."""
    rx = re.compile(pattern, re.I)
    out = []
    for path in md_files(dirs):
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if rx.search(line):
                    out.append((path, i, line.rstrip("\n")))
    return out


def retry_terms(pattern):
    """The single-word retry set, derived mechanically from the pattern.

    THIS IS A STANDING STEP, NOT A FALLBACK. Promoted 2026-08-31 after the rarer-word
    retry caught a duplicate for the THIRD time — Glasgow-Imrie (C7), West Haven (C3),
    and `lipohaemarthrosis` (L1), where a 0-hit verdict would have merged a block that
    Corpus C already stated. A retry run only when something "looks suspicious" is a
    retry that does not run, because a clean-looking zero is exactly what it is for.

    Two shapes, because the three worked examples are two different failures:
      * MULTI-WORD — the corpus reworded the phrase. Retry each meaningful word bare.
        `Glasgow-Imrie` -> `Glasgow`, `Imrie`.  `West Haven` -> `Haven`.
      * SINGLE LONG WORD — the corpus used a different compound, or markdown emphasis
        split it. Retry internal substrings, which covers `haemarthrosis` inside
        `lipohaemarthrosis` AND `aemolysis` inside `**H**aemolysis`.
    """
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", pattern)
             if w.lower() not in COMMON]
    terms = []
    if len(words) > 1:
        terms = sorted(set(words), key=len, reverse=True)
    for w in words:
        for part in re.split(r"[-']", w):
            if len(part) >= 4 and part not in terms and part.lower() not in COMMON:
                terms.append(part)
    if len(words) == 1 and len(words[0]) >= 8:
        w = words[0]
        for cut in (3, 4, 5, 6):
            if len(w) - cut >= 5:
                for cand in (w[cut:], w[:-cut]):
                    if cand not in terms:
                        terms.append(cand)
    seen, out = set(), []
    for x in terms:
        if x.lower() not in seen:
            seen.add(x.lower())
            out.append(x)
    return out[:8]


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
    ap.add_argument("--source", default="Corpus B",
                    help="the corpus being merged FROM. Hits here are self-matches and do "
                         "not count towards PRESENT. Pass '' to disable.")
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

    hits = search(args.pattern, args.dirs)

    src = args.source.strip()
    self_hits = [h for h in hits if src and h[0].startswith(src + os.sep)]
    dest_hits = [h for h in hits if h not in self_hits]

    print(f"gapcheck: {len(hits)} hit(s) for /{args.pattern}/ in {', '.join(args.dirs)}"
          f"  —  {len(dest_hits)} in destination corpora, {len(self_hits)} self-match"
          f"{'' if len(self_hits) == 1 else 'es'} in {src or 'n/a'}")
    print("Every line below is printed IN FULL. There is no limit flag and none will be "
          "added — truncation is the defect this tool exists to prevent.\n")
    for path, i, line in dest_hits:
        print(f"{path}:{i}: {line}")
    if self_hits:
        print(f"\n--- {len(self_hits)} SELF-MATCH(ES) in {src}, which do NOT count towards "
              f"PRESENT ---")
        for path, i, line in self_hits:
            print(f"{path}:{i}: {line}")

    if not dest_hits:
        if self_hits:
            print(f"\n*** WARNING: every hit is a SELF-MATCH in {src}. ***")
            print("    The search found the file being merged, not the destination. Treat "
                  "this as ZERO, not as PRESENT.")
            print("    A self-match reported as PRESENT is a FALSE PRESENT — the silent "
                  "direction, which nothing downstream catches (rule 9).")
        print("\nZERO HITS IN THE DESTINATION CORPORA — this is NOT an ABSENT verdict yet "
              "(rule 2).")
        terms = retry_terms(args.pattern)
        if terms:
            print(f"\nSINGLE-WORD RETRY — RUN AUTOMATICALLY, not suggested. "
                  f"{len(terms)} term(s), every hit printed in full.")
            print("(A standing step since 2026-08-31: the rarer-word retry has now caught a "
                  "duplicate three times —\n Glasgow-Imrie, West Haven, lipohaemarthrosis — "
                  "and in each case the original search looked clean.)\n")
            found = 0
            for term in terms:
                rhits = [h for h in search(re.escape(term), args.dirs)
                         if not (src and h[0].startswith(src + os.sep))]
                print(f"  retry /{term}/ -> {len(rhits)} hit(s)")
                for path, i, line in rhits:
                    print(f"    {path}:{i}: {line}")
                found += len(rhits)
            if found:
                print(f"\n*** {found} HIT(S) FROM THE RETRY. READ THEM BEFORE RECORDING "
                      f"ABSENT. ***")
                print("    A retry hit is how Glasgow-Imrie, West Haven and "
                      "lipohaemarthrosis were each caught.")
            else:
                print("\n  Retry found nothing either.")
        else:
            print("\n  No retry term could be derived from this pattern.")
        print("\nStill to consider by hand, which no tool can derive:")
        print("    * spelling and naming variants : ae/e, -ise/-ize, AU vs international "
              "drug name, acronym vs expansion")
        print("    * the CONCEPT, not the phrase  : what would the corpus call this if it "
              "used different words?")
        print("  A zero result you did not re-search is not a finding.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
