#!/usr/bin/env python3
"""
merge_tools.py — inspectable tooling for the corpus merge.

Standard library only. No network. No AI. Every operation is a regex or a file write,
so you can read this file and know exactly what it does to your vault.

Commands
--------
  init    add trust/population frontmatter to files that lack it
  scan    extract markers -> verification queue, conflict index, frontmatter counters
  lint    report violations of the conventions
  drugs   flag UK/US drug naming
  paed    sweep non-paediatric files for paediatric signals

Usage
-----
  python3 merge_tools.py scan  --dir /path/to/vault
  python3 merge_tools.py init  --dir /path/to/vault --dry-run
  python3 merge_tools.py lint  --dir /path/to/vault

Always run with --dry-run first. Always run on a branch.
"""

import argparse
import datetime as _dt
import os
import re
import sys

# ---------------------------------------------------------------- patterns

RE_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
RE_HEADING = re.compile(r"^(#{2,3})\s+(.*)$")

RE_UNVERIFIED = re.compile(r"`UNVERIFIED\s*[—\-–:]\s*(.+?)`")
RE_VERIFIED_TOK = re.compile(r"`VERIFIED\s+(.+?)`")
RE_CONFLICT_HEAD = re.compile(
    r"^>\s*\[!fail\]-?\s*CONFLICT\s+(CF-\d+)\s*(?:[—\-–]\s*(.*?))?\s*$"
)
RE_CF_INLINE = re.compile(r"`(CF-\d+)`")
# Anchored to the start of a callout line. Unanchored, this matched example
# stamps quoted inside a conflict block and silently marked it resolved.
RE_STAMP = re.compile(
    r"^>\s*\*\*(RESOLVED|DEFERRED)\s+(\d{4}-\d{2}-\d{2})"
    r"(?:\s+(A|B|NEITHER))?\s*[—\-–]\s*(.+?)\.?\*\*",
    re.M,
)
RE_TIER_TAG = re.compile(r"\*\*(R[123])\*\*")
RE_CHECK_CALLOUT = re.compile(r"^>\s*\[!check\]")
RE_NOT_CHECKED = re.compile(r"^>\s*\*\*NOT checked:\*\*", re.I)
RE_MED_MIRROR = re.compile(r"`→MED:([A-Za-z0-9_\-]+)`")

# a dose-ish figure: number + unit, optionally per kg
RE_DOSE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:mcg|microgram|micrograms|mg|g|units?|IU|mL|ml|L)"
    r"(?:\s*/\s*kg)?\b",
    re.I,
)

# R1 risk signals on a line
RE_R1_SIGNAL = re.compile(
    r"(mg/kg|mcg/kg|/kg\b|\bdose\b|\bdosing\b|\bIV\b|\bIM\b|\bIO\b|"
    r"defibrillat|adrenaline|arrest|resuscitat|notifiab|\bstat\b|maximum|\bmax\b)",
    re.I,
)
RE_R2_SIGNAL = re.compile(
    r"(threshold|score|cut-?off|cut-?point|observation|refer|referral|"
    r"admit|discharge|criteria)",
    re.I,
)

# paediatric signals for the sweep
RE_PAED_SIGNAL = re.compile(
    r"(mg/kg|mcg/kg|\d\s*/\s*kg\b|neonat|infant|newborn|toddler|child|children|"
    r"adolescen|paediatr|pediatr|months old|years old|\bRCH\b|\bAPLS\b|Broselow|"
    r"croup|bronchiolitis|Kawasaki|febrile convulsion|gestation)",
    re.I,
)

# Terms that contain a paediatric substring but are not paediatric content.
# "Child-Pugh" is the reason this list exists. Extend it as false positives appear.
RE_PAED_EXCLUDE = re.compile(r"(Child-Pugh|Childs-Pugh|childhood cancer survivor)", re.I)

# UK / US naming -> AU naming. Extend as you find more.
DRUG_NAMING = {
    "co-amoxiclav": "amoxicillin+clavulanate (check TG for the AU regimen)",
    "furosemide": "frusemide (AU convention; confirm local usage)",
    "acetaminophen": "paracetamol",
    "epinephrine": "adrenaline",
    "norepinephrine": "noradrenaline",
    "albuterol": "salbutamol",
    "meperidine": "pethidine",
    "glyburide": "glibenclamide",
    "lignocaine hydrochloride": "lidocaine (check current AU nomenclature)",
    "rifampin": "rifampicin",
    "cyclosporine": "ciclosporin",
    "amphetamine sulfate": "dexamfetamine (check AU spelling)",
    "co-trimoxazole": "trimethoprim+sulfamethoxazole (AU naming varies; confirm)",
    "salbutamol sulfate": "salbutamol sulfate (check AU spelling: sulfate/sulphate)",
    "hydroxychloroquine sulfate": "hydroxychloroquine sulfate (check AU spelling)",
}

# Sources requiring an institutional login. Items naming only these can never be
# closed under the current working constraints, and should be labelled as permanently
# noted rather than sitting in a queue that will never empty.
RE_LOGIN_SOURCE = re.compile(
    r"(therapeutic guidelines|\beTG\b|\bAMH\b|australian medicines handbook|"
    r"australian injectable drugs handbook|\bAIDH\b|eviQ)", re.I
)

# Openly accessible Australian sources — items naming these are actionable without a login.
RE_OPEN_SOURCE = re.compile(
    r"(ANZCOR|ASCIA|\bRCH\b|royal children|immunisation handbook|\bNIP\b|\bPBS\b|"
    r"\bTGA\b|queensland (children|health)|NSW ACI|SA Health|RACGP|RANZCOG|"
    r"kidney health|APEG|CDNA|\bNBA\b|cancer council|AIHW)", re.I
)


def actionability(text):
    """OPEN (checkable without a login), LOGIN (needs TG/AMH), or UNKNOWN."""
    open_hit = bool(RE_OPEN_SOURCE.search(text))
    login_hit = bool(RE_LOGIN_SOURCE.search(text))
    if open_hit:
        return "OPEN"
    if login_hit:
        return "LOGIN"
    return "UNKNOWN"


CORPUS_DEFAULTS = {
    "a": ("inherited", "mixed"),
    "b": ("unverified", "mixed"),
    "c": ("snippet", "mixed"),
}

SKIP_DIRS = {".git", ".obsidian", "_meta", "node_modules", ".trash"}


# ---------------------------------------------------------------- helpers


def md_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)


def normalise(line):
    """Strip markdown emphasis so patterns are not defeated by it.

    Per the project CLAUDE.md rule 2: this corpus bolds acronym expansions letter
    by letter (`**H**aemolysis`), and emphasis can split a word or a figure
    (`**10**mg/kg`, `co-**amoxiclav**`). A naive regex silently misses those, and a
    false negative here looks exactly like a clean file. Always match against the
    normalised form as well as the raw line.
    """
    return line.replace("**", "").replace("__", "").replace("*", "").replace("`", "")


def matches(pattern, line):
    """True if pattern hits the raw OR the emphasis-stripped line."""
    return bool(pattern.search(line) or pattern.search(normalise(line)))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def split_frontmatter(text):
    """Return (frontmatter_string_or_None, body)."""
    m = RE_FRONTMATTER.match(text)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def fm_get(fm, key):
    if fm is None:
        return None
    m = re.search(rf"^{re.escape(key)}:\s*(.*)$", fm, re.M)
    return m.group(1).strip() if m else None


def fm_set(fm, key, value):
    """Set or replace a key in a frontmatter string."""
    if re.search(rf"^{re.escape(key)}:", fm, re.M):
        return re.sub(rf"^{re.escape(key)}:.*$", f"{key}: {value}", fm, flags=re.M)
    return fm.rstrip("\n") + f"\n{key}: {value}"


def rebuild(fm, body):
    return f"---\n{fm}\n---\n{body}"


def current_section(lines, idx):
    """Nearest preceding ## / ### heading."""
    for j in range(idx, -1, -1):
        m = RE_HEADING.match(lines[j])
        if m:
            return m.group(2).strip()
    return "(no heading)"


def tier_for(line, explicit=None):
    if explicit:
        return explicit
    if RE_R1_SIGNAL.search(line) or RE_DOSE.search(line):
        return "R1"
    if RE_R2_SIGNAL.search(line):
        return "R2"
    return "R3"


def rel(root, path):
    return os.path.relpath(path, root)


def log_run(root, name, lines):
    d = os.path.join(root, "_meta", "runs")
    os.makedirs(d, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    p = os.path.join(d, f"{stamp}_{name}.log")
    write(p, "\n".join(lines) + "\n")
    return p


# ---------------------------------------------------------------- init


def cmd_init(args):
    trust, population = CORPUS_DEFAULTS[args.corpus]
    changed, skipped = [], []

    for path in md_files(args.dir):
        text = read(path)
        fm, body = split_frontmatter(text)
        if fm is None:
            fm = f"trust: {trust}\npopulation: {population}"
            new = rebuild(fm, text)
        else:
            if fm_get(fm, "trust") and not args.force:
                skipped.append(rel(args.dir, path))
                continue
            fm2 = fm_set(fm, "trust", trust)
            fm2 = fm_set(fm2, "population", population)
            new = rebuild(fm2, body)
        changed.append(rel(args.dir, path))
        if not args.dry_run:
            write(path, new)

    print(f"init [{args.corpus}] trust={trust} population={population}")
    print(f"  would change: {len(changed)}" if args.dry_run else f"  changed: {len(changed)}")
    print(f"  skipped (already had trust): {len(skipped)}")
    for f in changed[:20]:
        print(f"    {f}")
    if len(changed) > 20:
        print(f"    ... and {len(changed) - 20} more")
    print("\n  Population is set to a placeholder. Correct it per file — "
          "do not trust the default.")


# ---------------------------------------------------------------- scan


def collect(root):
    """Walk the vault once and gather every marker."""
    unverified, conflicts, mirrors = [], [], []
    per_file = {}

    for path in md_files(root):
        text = read(path)
        fm, _ = split_frontmatter(text)
        trust = fm_get(fm, "trust") or "UNSET"
        lines = text.split("\n")
        open_ct = r1_ct = 0

        i = 0
        while i < len(lines):
            line = lines[i]

            for m in RE_UNVERIFIED.finditer(line):
                unverified.append({
                    "file": rel(root, path),
                    "line": i + 1,
                    "section": current_section(lines, i),
                    "scope": m.group(1).strip(),
                    "tier": tier_for(line, (RE_TIER_TAG.search(line) or [None, None])[1]
                                     if RE_TIER_TAG.search(line) else None),
                    "trust": trust,
                    "act": actionability(m.group(1) + " " + line),
                })

            for m in RE_MED_MIRROR.finditer(line):
                doses = RE_DOSE.findall(line)
                mirrors.append({
                    "file": rel(root, path),
                    "line": i + 1,
                    "drug": m.group(1),
                    "figures": doses,
                    "text": line.strip()[:160],
                })

            hm = RE_CONFLICT_HEAD.match(line)
            if hm:
                cf_id, title = hm.group(1), (hm.group(2) or "").strip()
                block = [line]
                j = i + 1
                while j < len(lines) and lines[j].startswith(">"):
                    block.append(lines[j])
                    j += 1
                blob = "\n".join(block)
                stamp = RE_STAMP.search(blob)
                tier_m = RE_TIER_TAG.search(blob)
                tier = tier_m.group(1) if tier_m else tier_for(blob)
                status = stamp.group(1) if stamp else "OPEN"
                conflicts.append({
                    "id": cf_id,
                    "file": rel(root, path),
                    "line": i + 1,
                    "section": current_section(lines, i),
                    "title": title,
                    "tier": tier,
                    "status": status,
                    "verdict": (stamp.group(3) if stamp and stamp.group(3) else ""),
                    "source": (stamp.group(4) if stamp else ""),
                    "date": (stamp.group(2) if stamp else ""),
                })
                if status == "OPEN":
                    open_ct += 1
                    if tier == "R1":
                        r1_ct += 1
                i = j
                continue

            i += 1

        per_file[path] = (open_ct, r1_ct)

    return unverified, conflicts, mirrors, per_file


def cmd_scan(args):
    root = args.dir
    unverified, conflicts, mirrors, per_file = collect(root)
    meta = os.path.join(root, "_meta")
    os.makedirs(meta, exist_ok=True)
    today = _dt.date.today().isoformat()
    order = {"R1": 0, "R2": 1, "R3": 2}

    # --- verification queue
    unverified.sort(key=lambda r: (order.get(r["tier"], 3), r["file"], r["line"]))
    out = [
        "---", "name: verification-queue",
        "description: Generated. Do not hand-edit — edit the marker in the file and rescan.",
        "---", "",
        f"# Verification queue — generated {today}", "",
        f"{len(unverified)} open items. "
        "Close one by editing its marker in the file, then rerunning `scan`.", "",
    ]
    def block(rows, heading, note):
        if not rows:
            return []
        seg = [f"# {heading} ({len(rows)})", "", note, ""]
        for tier in ("R1", "R2", "R3"):
            tr = [r for r in rows if r["tier"] == tier]
            if not tr:
                continue
            label = {"R1": "could kill someone this rotation",
                     "R2": "changes disposition",
                     "R3": "everything else"}[tier]
            seg += [f"## {tier} — {label} ({len(tr)})", ""]
            for r in tr:
                seg.append(
                    f"- **{r['file']}** L{r['line']} · _{r['section']}_ "
                    f"· `{r['trust']}` — {r['scope']}"
                )
            seg.append("")
        return seg

    out += block(
        [r for r in unverified if r["act"] == "OPEN"],
        "Actionable — openly accessible Australian sources",
        "These name ANZCOR, ASCIA, RCH, the Immunisation Handbook, PBS or similar. "
        "No login needed. **This is the working queue.**",
    )
    out += block(
        [r for r in unverified if r["act"] == "UNKNOWN"],
        "Triage — source not named in the marker",
        "The marker does not say what to check against. Read the entry and either name an "
        "open source (moving it to the working queue) or reclassify it as login-required.",
    )
    out += block(
        [r for r in unverified if r["act"] == "LOGIN"],
        "Permanently noted — requires Therapeutic Guidelines or AMH",
        "**Not a to-do list.** These cannot be closed without an institutional login. "
        "The marker stays in the file as a permanent flag: look it up at the point of use. "
        "Do not delete these, and do not resolve them from memory or from a non-AU source.",
    )
    write(os.path.join(meta, "VERIFICATION_QUEUE.md"), "\n".join(out))

    # Rows in PENDING_GUIDELINE_CHECKS.md format, ready to paste into that file.
    # This tool does NOT edit PENDING_GUIDELINE_CHECKS.md — that file has an
    # append-never-delete protocol and a manual ID sequence, and a script that
    # rewrote it could destroy resolution history.
    rows = ["# New rows for PENDING_GUIDELINE_CHECKS.md",
            "",
            f"Generated {today}. Review, assign IDs continuing the existing sequence,",
            "and paste into the appropriate section. Do not let a script write that file.",
            "",
            "| # | File | Line | What to re-check | Status |",
            "|---|---|---|---|---|"]
    for r in unverified:
        if r["tier"] != "R1" or r["act"] == "LOGIN":
            continue
        scope = r["scope"].replace("|", "\\|")
        rows.append(f"| _ | `{r['file']}` | {r['line']} | **{r['section']}** — {scope} "
                    f"(`{r['trust']}` layer) | ⬜ |")
    write(os.path.join(meta, "PENDING_ROWS_DRAFT.md"), "\n".join(rows) + "\n")

    # --- conflict index
    conflicts.sort(key=lambda r: (order.get(r["tier"], 3), r["file"], r["line"]))
    op = [c for c in conflicts if c["status"] == "OPEN"]
    rs = [c for c in conflicts if c["status"] == "RESOLVED"]
    df = [c for c in conflicts if c["status"] == "DEFERRED"]
    out = [
        "---", "name: conflicts",
        "description: Generated. Do not hand-edit — stamp the block in the file and rescan.",
        "---", "",
        f"# Conflict index — generated {today}", "",
        f"Open {len(op)} · deferred {len(df)} · resolved {len(rs)}", "",
        "## Open", "",
    ]
    for c in op:
        out.append(
            f"- **{c['id']}** [{c['tier']}] {c['file']} L{c['line']} "
            f"· _{c['section']}_ — {c['title']}"
        )
    out += ["", "## Deferred", ""]
    for c in df:
        out.append(f"- **{c['id']}** [{c['tier']}] {c['file']} — {c['source']} ({c['date']})")
    out += ["", "## Resolved", ""]
    for c in rs:
        out.append(
            f"- **{c['id']}** [{c['tier']}] {c['file']} — verdict "
            f"**{c['verdict'] or '?'}** via {c['source']} ({c['date']})"
        )
    write(os.path.join(meta, "CONFLICTS.md"), "\n".join(out) + "\n")

    # --- mirror drift report
    by_drug = {}
    for m in mirrors:
        by_drug.setdefault(m["drug"], []).append(m)
    out = [f"# Dose mirror report — generated {today}", "",
           "Figures marked `→MED:` grouped by drug. Differing figures for the same drug "
           "need a population token or are drift.", ""]
    for drug in sorted(by_drug):
        rows = by_drug[drug]
        sets = {tuple(r["figures"]) for r in rows if r["figures"]}
        flag = "  ← **DIFFERING FIGURES**" if len(sets) > 1 else ""
        out.append(f"## {drug}{flag}")
        for r in rows:
            out.append(f"- {r['file']} L{r['line']} — {r['text']}")
        out.append("")
    write(os.path.join(meta, "DOSE_MIRRORS.md"), "\n".join(out))

    # --- frontmatter counters
    touched = 0
    for path, (open_ct, r1_ct) in per_file.items():
        text = read(path)
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        if (fm_get(fm, "conflicts_open") == str(open_ct)
                and fm_get(fm, "conflicts_r1") == str(r1_ct)):
            continue
        fm = fm_set(fm, "conflicts_open", open_ct)
        fm = fm_set(fm, "conflicts_r1", r1_ct)
        if not args.dry_run:
            write(path, rebuild(fm, body))
        touched += 1

    acts = {}
    for r in unverified:
        acts[r["act"]] = acts.get(r["act"], 0) + 1
    print(f"  actionable without login: {acts.get('OPEN', 0)} · "
          f"needs triage: {acts.get('UNKNOWN', 0)} · "
          f"login-required (permanently noted): {acts.get('LOGIN', 0)}")
    print(f"scan: {len(unverified)} unverified · {len(op)} open conflicts "
          f"({len([c for c in op if c['tier'] == 'R1'])} R1) · "
          f"{len(mirrors)} dose mirrors")
    print(f"  frontmatter counters updated in {touched} files"
          + (" (dry run)" if args.dry_run else ""))
    print(f"  wrote {meta}/VERIFICATION_QUEUE.md, CONFLICTS.md, DOSE_MIRRORS.md")


# ---------------------------------------------------------------- lint


def cmd_lint(args):
    problems = []
    fact_locations = {}

    for path in md_files(args.dir):
        text = read(path)
        fm, _ = split_frontmatter(text)
        r = rel(args.dir, path)
        lines = text.split("\n")

        if fm is None:
            problems.append(f"{r}: no frontmatter")
        else:
            if not fm_get(fm, "trust"):
                problems.append(f"{r}: frontmatter missing `trust`")
            if not fm_get(fm, "population"):
                problems.append(f"{r}: frontmatter missing `population`")

        # [!check] callouts must carry NOT checked:
        for i, line in enumerate(lines):
            if RE_CHECK_CALLOUT.match(line):
                j, found = i + 1, False
                while j < len(lines) and lines[j].startswith(">"):
                    if RE_NOT_CHECKED.match(lines[j]):
                        found = True
                        break
                    j += 1
                if not found:
                    problems.append(
                        f"{r} L{i+1}: [!check] callout missing mandatory "
                        f"`NOT checked:` line"
                    )

        # unmarked doses in non-verified files
        trust = fm_get(fm, "trust") if fm else None
        if trust in ("inherited", "unverified"):
            for i, line in enumerate(lines):
                if matches(RE_DOSE, line) and not (
                    RE_MED_MIRROR.search(line)
                    or RE_UNVERIFIED.search(line)
                    or RE_VERIFIED_TOK.search(line)
                    or line.strip().startswith(">")
                ):
                    problems.append(
                        f"{r} L{i+1}: dose figure in `{trust}` file with no "
                        f"marker or →MED mirror — {line.strip()[:90]}"
                    )

        # figures: none files must contain no doses
        if fm and fm_get(fm, "figures") == "none":
            for i, line in enumerate(lines):
                if matches(RE_DOSE, line):
                    problems.append(
                        f"{r} L{i+1}: file declares `figures: none` but states a "
                        f"figure — {line.strip()[:90]}"
                    )

        # three-appearances rule for mirrored drugs
        for m in RE_MED_MIRROR.finditer(text):
            fact_locations.setdefault(m.group(1), set()).add(r)

    for drug, files in sorted(fact_locations.items()):
        if len(files) > 3:
            problems.append(
                f"→MED:{drug} appears in {len(files)} files — "
                f"owner registry violation ({', '.join(sorted(files)[:4])}...)"
            )

    print(f"lint: {len(problems)} problems")
    for p in problems[: args.limit]:
        print(f"  {p}")
    if len(problems) > args.limit:
        print(f"  ... and {len(problems) - args.limit} more (raise --limit)")
    log_run(args.dir, "lint", problems)
    return 1 if problems else 0


# ---------------------------------------------------------------- drugs


def cmd_drugs(args):
    hits = []
    for path in md_files(args.dir):
        text = read(path)
        r = rel(args.dir, path)
        for i, line in enumerate(text.split("\n"), 1):
            low = line.lower()
            low_n = normalise(line).lower()
            for bad, good in DRUG_NAMING.items():
                if bad in low or bad in low_n:
                    hits.append(f"{r} L{i}: `{bad}` -> {good}\n      {line.strip()[:120]}")
    print(f"drugs: {len(hits)} non-AU naming hits")
    for h in hits[: args.limit]:
        print(f"  {h}")
    if len(hits) > args.limit:
        print(f"  ... and {len(hits) - args.limit} more")
    p = log_run(args.dir, "drugs", hits)
    print(f"  log: {p}")


# ---------------------------------------------------------------- paed


def cmd_paed(args):
    report = []
    for path in md_files(args.dir):
        r = rel(args.dir, path)
        text = read(path)
        fm, _ = split_frontmatter(text)
        if fm_get(fm, "population") == "paed" or "Paeds" in r or "paed" in r.lower():
            continue
        lines = text.split("\n")
        hits = []
        for i, line in enumerate(lines, 1):
            if matches(RE_PAED_SIGNAL, line):
                if "[paed]" in line or "[adult]" in line:
                    continue
                # drop the line if its only paed-looking token is an excluded term
                stripped = RE_PAED_EXCLUDE.sub("", line)
                if not matches(RE_PAED_SIGNAL, stripped):
                    continue
                hits.append((i, current_section(lines, i - 1), line.strip()[:110]))
        if hits:
            report.append(f"\n## {r} — {len(hits)} unmarked paediatric signals "
                          f"(population: {fm_get(fm, 'population')})")
            for ln, sec, txt in hits[:40]:
                report.append(f"- L{ln} · _{sec}_ — {txt}")
            if len(hits) > 40:
                report.append(f"- ... and {len(hits) - 40} more")

    total = sum(1 for l in report if l.startswith("- L"))
    print(f"paed: {total} unmarked paediatric signals in non-paediatric files")
    for line in report[: args.limit]:
        print(line)
    p = log_run(args.dir, "paed", report)
    print(f"  full report: {p}")


# ---------------------------------------------------------------- cli


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--dir", required=True, help="vault root")
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--limit", type=int, default=40)

    p = sub.add_parser("init"); common(p)
    p.add_argument("--corpus", choices=["a", "b", "c"], required=True)
    p.add_argument("--force", action="store_true",
                   help="overwrite an existing trust value")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("scan"); common(p); p.set_defaults(fn=cmd_scan)
    p = sub.add_parser("lint"); common(p); p.set_defaults(fn=cmd_lint)
    p = sub.add_parser("drugs"); common(p); p.set_defaults(fn=cmd_drugs)
    p = sub.add_parser("paed"); common(p); p.set_defaults(fn=cmd_paed)

    args = ap.parse_args()
    if not os.path.isdir(args.dir):
        sys.exit(f"not a directory: {args.dir}")
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    main()
