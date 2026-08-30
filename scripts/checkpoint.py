#!/usr/bin/env python3
"""Per-file checks run after EVERY merged B file, not only at session end.

Three independent checks, each answering a question a passing commit does not:

  ascia   Do the four ASCIA band tables still agree on their CLINICAL columns?
          C1-C7 touches anaphylaxis cross-references, which is exactly the
          circumstance in which one mirror gets edited alone.
  status  Did anything get written that was not part of this change? The
          2026-08-30 stray write to 00_BUILD_QUEUE_v2.md was found only
          because a hook surfaced `git status` — no check the tools ran
          would have shown it.
  digits  Digit multiset per file, against a named git ref.

Deliberately compares only age / weight / volume. The device column is
abbreviated differently at each location on purpose, and an earlier version of
this check compared every column and reported all four files as failing every
row — a broken checker, not four broken files.
"""
import os, re, subprocess, sys, collections

OWNER = "Corpus A/09_01_Dermatology_-_Dermatological_Emergencies.md"
MIRRORS = ["Corpus A/01_Cardiovascular.md",
           "Corpus A/15_01b_Paeds_-_Anaphylaxis.md",
           "Corpus C/NEW_Drugs_01_Allergy_and_Anaphylaxis.md"]
HEADER = re.compile(r"\|\s*Age \(years\)\s*\|\s*Weight \(kg\)\s*\|\s*Volume of 1:1,000")


def strip_md(c):
    return re.sub(r"[*`]", "", c).strip()


def bands(path):
    """Return [(age, weight, volume)] from the ASCIA table, or None if absent."""
    lines = open(path, encoding="utf-8").read().split("\n")
    start = next((i for i, l in enumerate(lines) if HEADER.search(l)), None)
    if start is None:
        return None
    rows = []
    for l in lines[start + 1:]:
        s = l.lstrip("> ").strip()
        if not s.startswith("|"):
            break
        cells = [strip_md(c) for c in s.strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= set("-: "):
            continue
        rows.append(tuple(cells[:3]))
    return rows


def check_ascia():
    ref = bands(OWNER)
    if not ref:
        print(f"ASCIA: FAIL — no band table found in owner {OWNER}")
        return 1
    bad = 0
    print(f"ASCIA band tables — owner {OWNER} ({len(ref)} rows)")
    for m in MIRRORS:
        got = bands(m)
        if got is None:
            print(f"  MISSING  {m} — no band table")
            bad += 1
            continue
        if got == ref:
            print(f"  agrees   {m} ({len(got)} rows)")
        else:
            bad += 1
            print(f"  DIFFERS  {m} ({len(got)} rows)")
            for i in range(max(len(ref), len(got))):
                a = ref[i] if i < len(ref) else None
                b = got[i] if i < len(got) else None
                if a != b:
                    print(f"      row {i}: owner={a} mirror={b}")
    print(f"ASCIA: {'OK — all three mirrors agree' if not bad else f'{bad} mirror(s) disagree'}")
    return bad


def check_status():
    out = subprocess.run(["git", "status", "--porcelain", "--ignored=matching"],
                         capture_output=True, text=True).stdout.rstrip("\n")
    dirty = [l for l in out.split("\n") if l and not l.startswith("!!")]
    ignored = [l for l in out.split("\n") if l.startswith("!!")]
    if dirty:
        print("STATUS: uncommitted changes present —")
        for l in dirty:
            print("   " + l)
    else:
        print("STATUS: clean (no uncommitted tracked or untracked changes)")
    if ignored:
        print("  ignored, expected: " + ", ".join(l[3:] for l in ignored))
    return len(dirty)


def check_digits(ref, paths):
    print(f"DIGIT MULTISET vs {ref}")
    for p in paths:
        try:
            was = subprocess.run(["git", "show", f"{ref}:{p}"],
                                 capture_output=True, text=True, check=True).stdout
        except subprocess.CalledProcessError:
            print(f"  {p}: not present at {ref} (new file)")
            continue
        now = open(p, encoding="utf-8").read()
        a, b = collections.Counter(re.findall(r"\d", was)), collections.Counter(re.findall(r"\d", now))
        if a == b:
            print(f"  {p}: unchanged ({sum(a.values())} digits)")
        else:
            print(f"  {p}: {sum(a.values())} -> {sum(b.values())}"
                  f"  added={dict(b - a)} removed={dict(a - b)}")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    rc = 0
    if cmd in ("ascia", "all"):
        rc += check_ascia()
    if cmd in ("status", "all"):
        print()
        rc += check_status()
    if cmd == "digits":
        rc += check_digits(sys.argv[2], sys.argv[3:])
    sys.exit(1 if rc else 0)
