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
  study   STUDY_CHECKS.md — the same data, grouped by clinical topic for revision
  precommit  refuse to commit staged conflict markers
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
import subprocess
import os
import re
import sys

# ---------------------------------------------------------------- patterns

RE_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
RE_HEADING = re.compile(r"^(#{2,3})\s+(.*)$")

RE_UNVERIFIED = re.compile(r"`UNVERIFIED\s*[—\-–:]\s*(.+?)`")
RE_VERIFIED_TOK = re.compile(r"`VERIFIED\s+(.+?)`")
# A backticked token opening with a marker word. Used by lint to find markers that were
# written but do not parse — see cmd_lint. Deliberately permissive: it matches the
# ATTEMPT, so lint can compare it against what actually parses.
RE_MARKER_SPAN = re.compile(r"`(UNVERIFIED|VERIFIED)\b([^`]*)`")
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
# Internal spaces are allowed because real drug names have them — `sodium nitroprusside`,
# `magnesium sulfate`, `tranexamic acid`. The original pattern excluded them, so any
# multi-word mirror was SILENTLY ignored: no match, no entry in the dose-mirror report,
# no error. That is the voided-marker failure shape (§1.7), and it was found the only
# way it can be — by writing one and noticing the report did not change.
# RE_MED_LOOSE catches anything that *looks* like a mirror so lint can say so out loud
# rather than letting a mistyped marker vanish.
RE_MED_MIRROR = re.compile(r"`→MED:([A-Za-z0-9_\- ]+)`")
RE_MED_LOOSE = re.compile(r"→MED:")

# NO-BASELINE marks an additive block whose subject had ZERO hits vault-wide before the
# merge, so no inherited layer can disagree with it and no cross-check can catch an error.
# Established 2026-08-31 by testing every additive block against the base-A tree.
RE_NO_BASELINE = re.compile(r"`NO-BASELINE[^`]*`")

# How far past a →MED: marker to look for the figure it mirrors. The marker convention puts
# it on a callout header above a weight/age band table; the longest real one is 7 rows plus
# header and owner lines. 20 is generous without running into the next section.
MED_BLOCK_LOOKAHEAD = 20

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
    r"croup|bronchiolitis|Kawasaki|febrile convulsion|gestation"
    # Added 2026-08-30. The list above has no case for developmental, neonatal-history
    # or childhood-immunisation content, so files carrying only that scored zero and read
    # as adult-only. Every term below was observed in the corpus.
    #
    # `congenital` was REJECTED, then RESTORED on 2026-08-30 after the rejection was found
    # to be wrong. The rejection judged it by reading the *flagged lines*, where it looks
    # like an aetiology label in adult files (congenital long QT, congenital absence of the
    # vas deferens, congenital lymphoedema). Reading the *disease entries those lines sit
    # in* shows it also catches two genuinely paediatric-scope files — `10_06b` (congenital
    # methaemoglobinaemia, presents in infancy) and `11_08c` (osteogenesis imperfecta, type
    # II lethal in the neonatal period). Corrected score: 6 flagged, 2 true positives.
    #
    # Kept because the costs are asymmetric: a false positive costs a `mixed` label, which
    # merely tells the reader to check; a false negative costs a wrong `adult` label over
    # paediatric content, which is the B65 failure. JUDGE A TERM BY THE DISEASE ENTRIES ITS
    # HITS SIT IN, NOT BY THE FLAGGED LINES ALONE.
    #
    # Three candidate terms were tried and REJECTED — do not re-add them bare:
    #   `breast-?feed`— in adult files it is maternal scope, not the infant's: a protective
    #                   factor for ovarian cancer, a cause of dyspareunia, drug safety in
    #                   lactation. Flagged 4 files, 0 true positives.
    #   `weaning`     — two senses; 2 of its 5 corpus hits are ventilator and NIV weaning
    #                   in adult ICU (`F0-4`, `F0-5`), not infant feeding.
    #   `centile`     — matches inside "99th percentile", so it caught assay statistics for
    #                   troponin cut-offs. Kept only in growth-chart compounds below.
    #   `\bBCG\b`      — 3 of its 17 corpus lines are intravesical BCG for bladder cancer,
    #                   an adult therapy. Kept only as `BCG vaccin`.
    r"|prematurity|preterm|premature (?:birth|bab|infant|neonate)"
    r"|(?:growth|weight|height|head circumference) centile|centile chart"
    r"|congenital|birth ?weight|\bApgar\b|fontanelle|teething|nappy"
    r"|pubert|juvenile|trisomy|Down syndrome|perinatal"
    r"|\brubella\b|BCG vaccin|\bmumps\b|\bmeasles\b|varicella|pertussis|whooping cough"
    r"|\bHib\b|\bMMR\b|immunisation schedule|vaccination schedule|milestone"
    r"|\bSIDS\b|\bPICU\b|non-accidental|\bNAI\b|Gillick)",
    re.I,
)

# NOTE for anyone extending the pattern above: do NOT add a bare `\bALL\b` for acute
# lymphoblastic leukaemia. Under re.I it matches the English word "all" and swamps every
# result — 37 of 65 sampled hits in the 2026-08-30 cross-check. That is the Child-Pugh
# defect in a new place. Match `acute lymphoblastic` instead if the disease is wanted.

# Terms that contain a paediatric substring but are not paediatric content.
# "Child-Pugh" is the reason this list exists. Extend it as false positives appear.
# Paediatric FILES, by anchored path pattern — never by substring (rule 9).
RE_PAED_PATH = re.compile(r"(^|/)15_\d\d[ab]?_Paeds_|Paediatric", re.I)

RE_PAED_EXCLUDE = re.compile(
    r"(Child-Pugh|Childs-Pugh|childhood cancer survivor"
    # Adult uses of terms added 2026-08-30, each confirmed present in the corpus:
    # BCG is intravesical immunotherapy for bladder cancer in 3 of its 17 corpus lines.
    r"|premature (?:ovarian|menopause|cardiovascular|ejaculation|ventricular|atrial))",
    re.I,
)

# Non-AU naming -> AU naming.
#
# EVERY ENTRY CARRIES A SOURCE. An entry without one is not applied — that rule exists
# because the previous version of this map was a hand-written list of hedges, and one
# entry was BACKWARDS: it renamed `furosemide` to `frusemide`, when the TGA's Ingredient
# Harmonisation programme moved Australian Approved Names TOWARD the INN, i.e. frusemide
# to furosemide. Applying it would have regressed 14 correct names in the corpus.
#
# Hedged entries were REMOVED rather than kept, because a hedge is not a rename:
#   `co-trimoxazole`          — its own value read "AU naming varies; confirm".
#   `salbutamol sulfate`      — mapped to itself.
#   `hydroxychloroquine sulfate` — mapped to itself.
#   `lignocaine hydrochloride` — redundant with the `lignocaine` entry.
#   `amphetamine sulfate` -> `dexamfetamine` — REMOVED as a drug-identity error, not a
#                             naming one: amphetamine sulfate and dexamfetamine are not
#                             the same substance.
#
# Matched on WORD BOUNDARIES, not as substrings (rule 9): `epinephrine` is contained in
# `norepinephrine`, so a bare substring match told the reader to write "adrenaline" on
# every noradrenaline line.

TGA_IHIN = ("TGA, Updating medicine ingredient names — list of affected ingredients "
            "(Ingredient Harmonisation programme). Open AU source, no login.")
TGA_KEEP = ("TGA IHIN — adrenaline/noradrenaline explicitly RETAINED as the Australian "
            "approved names; the -ephrine forms are not adopted.")
INN_AU   = "Already the INN and the Australian approved name; never changed."

DRUG_NAMING = {
    # (replacement, source)
    "frusemide":      ("furosemide", TGA_IHIN),
    "amoxycillin":    ("amoxicillin", TGA_IHIN),
    "lignocaine":     ("lidocaine", TGA_IHIN),
    "rifampin":       ("rifampicin", TGA_IHIN),
    "cyclosporine":   ("ciclosporin", TGA_IHIN),
    "epinephrine":    ("adrenaline", TGA_KEEP),
    "norepinephrine": ("noradrenaline", TGA_KEEP),
    "acetaminophen":  ("paracetamol", INN_AU),
    "glyburide":      ("glibenclamide", INN_AU),
    "albuterol":      ("salbutamol", INN_AU),
    "meperidine":     ("pethidine", INN_AU),
    "co-amoxiclav":   ("amoxicillin+clavulanate",
                       "Not an ingredient name at all — a UK combination shorthand. The "
                       "TGA IHIN ingredient names are amoxicillin and clavulanic acid; "
                       "the corpus already renders the pair as amoxicillin+clavulanate "
                       "in 4 of its 5 existing occurrences. Renaming the NAME does not "
                       "confirm the REGIMEN, which needs Therapeutic Guidelines (login)."),
}

# Blocks that deliberately quote non-Australian material — a UK schedule kept for
# reference, a "UK figures (unverified for AU use)" comparison. RENAMING INSIDE ONE MAKES
# FOREIGN FIGURES READ AS AUSTRALIAN, which is worse than leaving the foreign name in
# place: the name is the only thing marking the content as foreign.
RE_NON_AU_BLOCK = re.compile(
    r"(unverified for AU use|UK figures|UK schedule|retained for reference only|"
    r"not confirmed as Australian|not verified against an Australian source|"
    r"UK-specific|the UK's|UK guidance|was UK-specific guidance)", re.I)

DRUG_PATTERNS = {k: re.compile(r"\b" + re.escape(k) + r"\b", re.I) for k in DRUG_NAMING}

# Sources requiring an institutional login. Items naming only these can never be
# closed under the current working constraints, and should be labelled as permanently
# noted rather than sitting in a queue that will never empty.
RE_LOGIN_SOURCE = re.compile(
    r"(therapeutic guidelines|\beTG\b|\bAMH\b|australian medicines handbook|"
    r"australian injectable drugs handbook|\bAIDH\b|\beviQ\b)", re.I
)

# Openly accessible Australian sources — items naming these are actionable without a login.
RE_OPEN_SOURCE = re.compile(
    # Every acronym is word-anchored (rule 9). Unanchored, `ASCIA` matched inside
    # "f-ascia" and "f-ascial" on 33 corpus lines and `APEG` inside "sc-apeg-oating" on 1,
    # so any line mentioning fascial planes was scored OPEN — i.e. routed into the
    # actionable verification queue as though ASCIA could settle it.
    #
    # Extended 2026-08-30. Candidates were checked two ways before being added: an
    # in-word collision test against all 240 corpus files (all clean), and a reading of
    # how the corpus actually uses the token.
    #
    # REJECTED — `ADA`. Ambiguous between the Australian Dental Association and the
    # AMERICAN Diabetes Association, and the corpus's only use is the American one:
    # "current international consensus (including the ADA's own position statement)".
    # Adding it would route American guidance into the actionable-Australian queue.
    # `eviQ` is login-gated and stays in RE_LOGIN_SOURCE.
    r"(\bANZCOR\b|\bASCIA\b|\bRCH\b|royal children|immunisation handbook|\bNIP\b|"
    r"\bPBS\b|\bTGA\b|queensland (children|health)|\bNSW ACI\b|\bSA Health\b|"
    r"\bRACGP\b|\bRANZCOG\b|kidney health|\bAPEG\b|\bCDNA\b|\bNBA\b|"
    r"cancer council|\bAIHW\b"
    # colleges and societies whose guidance is publicly readable
    r"|\bGESA\b|\bRACP\b|\bANZCA\b|\bACEM\b|\bRANZCR\b|\bASID\b|\bANZBA\b"
    r"|\bSOMANZ\b|\bADS\b|\bADEA\b|\bRANZCO\b|\bRACS\b|\bASHM\b"
    # foundations, agencies and named open Australian references
    r"|heart foundation|lung foundation|stroke foundation|diabetes australia"
    r"|cancer australia|\bNHMRC\b|Austroads|australian asthma handbook"
    r"|national asthma council|NPS MedicineWise|australian prescriber"
    r"|national cervical screening|pregnancy care guidelines)", re.I
)


def actionability(text):
    """OPEN, MIXED, LOGIN or UNKNOWN.

    MIXED exists because a marker can name BOTH kinds of source, and the previous
    single-label version checked OPEN first and returned it — so
    "all doses from eTG and the Australian Asthma Handbook" was reported as "actionable
    without login". That overstates it: the open source may settle part of the item, but
    the login source settles the rest, and an item filed as fully actionable never gets
    the standing "look it up at the point of use" treatment §1.8 requires.

    Four markers in the corpus have this shape (A3, B2, F0-4, F0-5 at 2026-08-30).
    """
    open_hit = bool(RE_OPEN_SOURCE.search(text))
    login_hit = bool(RE_LOGIN_SOURCE.search(text))
    if open_hit and login_hit:
        return "MIXED"
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

# Vault-root infrastructure documents. These are *about* the conventions, so they
# contain worked examples of every marker the scans look for — CLAUDE.md alone holds
# four example `UNVERIFIED` markers and an example CONFLICT block. Walked as content
# they inject 9 phantom verification items and 4 phantom conflicts into the generated
# queues, which is CLAUDE.md rule 3 (every scan produces false positives) arriving via
# the scanner's own documentation.
#
# Matched at the VAULT ROOT ONLY, never by bare basename. An unanchored skip would drop a
# clinical file that happened to share one of these names from every scan, with no error
# and nothing downstream detecting the loss. The vault root is the nearest ancestor
# directory holding CLAUDE.md, so this works whether --dir is the vault or one corpus.
SKIP_FILES = {
    "CLAUDE.md",
    "MASTER_VERIFICATION_WORKFLOW.md",
    "MERGE_SPEC.md",
    "MERGE_STEPS.md",
    "PENDING_GUIDELINE_CHECKS.md",
    "START_HERE.md",
    "WORKED_EXAMPLE_appendicitis.md",
    "RUN_STATE.md",
}

# Infrastructure files that live INSIDE a corpus directory. SKIP_FILES is matched
# by basename and only at vault root, so it cannot reach these; matching them by
# basename anywhere would be skip logic keyed on an unanchored name, which is what
# CLAUDE.md rule 9 forbids ("never write skip logic on a substring"). These are
# full vault-relative paths, each resolving to exactly one file, and every entry is
# a file whose own text declares it is not clinical content.
#
# Why it matters: without this the scan writes provenance frontmatter and conflict
# counters into build queues, i.e. it asserts a trust level about clinical claims
# the file does not contain. Found twice — Step 26 stamped 00_BUILD_QUEUE.md, and
# the 2026-08-30 scan stamped 00_BUILD_QUEUE_v2.md.
SKIP_PATHS = {
    "Corpus B/00_BUILD_QUEUE.md",
    "Corpus B/00_BUILD_QUEUE_v2.md",
}


# ---------------------------------------------------------------- helpers


def vault_root(start):
    """Nearest ancestor of `start` containing CLAUDE.md, else abspath(start)."""
    d = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(d, "CLAUDE.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.abspath(start)
        d = parent


def md_files(root):
    vault = vault_root(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        at_vault_root = os.path.abspath(dirpath) == vault
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            if at_vault_root and fn in SKIP_FILES:
                continue
            full = os.path.join(dirpath, fn)
            if os.path.relpath(os.path.abspath(full), vault).replace(os.sep, "/") \
                    in SKIP_PATHS:
                continue
            yield full


def normalise(line):
    """Strip markdown emphasis so patterns are not defeated by it.

    Per the project CLAUDE.md rule 2: this corpus bolds acronym expansions letter
    by letter (`**H**aemolysis`), and emphasis can split a word or a figure
    (`**10**mg/kg`, `co-**amoxiclav**`). A naive regex silently misses those, and a
    false negative here looks exactly like a clean file. Always match against the
    normalised form as well as the raw line.
    """
    line = line.replace("**", "").replace("__", "").replace("*", "").replace("`", "")
    return line.translate(UNICODE_DIGITS)


# Sub- and superscript digits fold to ASCII. Found 2026-08-31 while merging D3: a search
# for `ABCD2` returned ABSENT while `04_Neurology` carried `ABCD²` with a superscript, and
# `CHA2DS2-VASc` returned ABSENT while `01_Cardiovascular` carried `CHA₂DS₂-VASc` with
# subscripts. Both scores were about to be merged as gaps, which would have put one
# instrument in the corpus twice under two renderings — in a different file from the
# original, so harder to notice than an ordinary duplicate.
UNICODE_DIGITS = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹", "01234567890123456789")


def matches(pattern, line):
    """True if pattern hits the raw OR the emphasis-stripped line."""
    return bool(pattern.search(line) or pattern.search(normalise(line)))


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# Set by main() from --dry-run. A dry run must not touch the working tree AT ALL —
# not the corpus, not _meta/, not the run logs. The previous behaviour gated only the
# frontmatter-counter writes, so `scan --dry-run` still rewrote VERIFICATION_QUEUE.md,
# CONFLICTS.md, DOSE_MIRRORS.md and PENDING_ROWS_DRAFT.md on every invocation, and
# lint/drugs/paed still wrote a timestamped log. Running a scan merely to LOOK at the
# corpus therefore dirtied the tree, which is how generated output kept being swept into
# commits by `git add -A`. A flag that says dry and mutates the tree is a defect.
DRY_RUN = False

# Every path passed to write() this run, named in the output by report_writes().
WRITES = []


def write(path, text):
    """Write a file, recording the path in WRITES.

    Every command reports WRITES before exiting. A bare count ("counters updated
    in 3 files") makes a misdirected write indistinguishable from a correct run —
    the only way to notice one was `git status`. Naming the paths makes it visible
    in the run output itself.
    """
    WRITES.append(path)
    if DRY_RUN:
        print(f"    [dry-run] would write {path}")
        return
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def report_writes(root, name):
    """Print every path written this run and mirror it to a run log."""
    if not WRITES:
        print(f"  files written: none{' (dry run)' if DRY_RUN else ''}")
        return
    print(f"  files written ({len(WRITES)}){' (dry run)' if DRY_RUN else ''}:")
    for w in WRITES:
        print(f"    {rel(root, w)}")
    # the log itself is a write; snapshot first so it does not list itself
    lines = [f"# {name} — files written {_dt.datetime.now().isoformat(timespec='seconds')}",
             ""] + [rel(root, w) for w in WRITES]
    log_run(root, f"{name}-writes", lines)


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


def vault_root(start):
    """Walk up from `start` to the directory that holds CLAUDE.md, else .git.

    Run logs must land at the vault root and nowhere else. Before this existed,
    `log_run` used the caller's --dir, so `--dir "Corpus A"` wrote its log to
    `Corpus A/_meta/runs/` — inside a corpus, which is the one place nothing
    non-clinical belongs. .gitignore did not catch them either: `_meta/runs/`
    contains a slash, so git anchors it to the repository root and it never
    matched `Corpus A/_meta/runs/`. Fourteen stray log files, invisible to the
    ignore rules and one `git add -A` away from a commit.

    Falls back to `start` when no marker is found, so the function is safe to
    call on a directory outside any vault.
    """
    d = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(d, "CLAUDE.md")) or os.path.isdir(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return os.path.abspath(start)
        d = parent


def log_run(root, name, lines):
    d = os.path.join(vault_root(root), "_meta", "runs")
    if DRY_RUN:
        return f"(dry-run: no log written to {d})"
    os.makedirs(d, exist_ok=True)
    stamp = _dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")
    p = os.path.join(d, f"{stamp}_{name}.log")
    write(p, "\n".join(lines) + "\n")
    return p



# ---------------------------------------------------------------- study

# Destination file -> clinical topic. Ordered as a reader revises, not as the filesystem
# sorts. Corpus A is numbered by area; Corpus C is NEW_<area>; Corpus B is block-lettered.
TOPIC_RULES = [
    (r"^Corpus A/01_", "Cardiology"),
    (r"^Corpus A/02_", "Respiratory"),
    (r"^Corpus A/03_Gastro", "Gastroenterology"),
    (r"^Corpus A/03a_", "Anaesthetics and Perioperative"),
    (r"^Corpus A/04_", "Neurology"),
    (r"^Corpus A/05_", "Ophthalmology"),
    (r"^Corpus A/06_", "Endocrinology and Metabolic"),
    (r"^Corpus A/07_", "Renal and Urology"),
    (r"^Corpus A/08_", "Infectious Diseases"),
    (r"^Corpus A/09_", "Dermatology"),
    (r"^Corpus A/10_", "Haematology and Oncology"),
    (r"^Corpus A/11_", "Orthopaedics and Trauma"),
    (r"^Corpus A/12_", "Rheumatology"),
    (r"^Corpus A/13_", "ENT"),
    (r"^Corpus A/14", "Psychiatry and Toxicology"),
    (r"^Corpus A/15_", "Paediatrics"),
    (r"^Corpus A/16_", "Obstetrics"),
    (r"^Corpus A/17_", "Gynaecology"),
    (r"^Corpus A/18_", "Geriatrics"),
    (r"^Corpus A/19_", "General Practice and Prevention"),
    (r"^Corpus C/NEW_Cardio|^Corpus C/NEW_Investigations_Cardio|^Corpus C/NEW_Drugs_06|^Corpus C/NEW_Drug_Classes_Cardio", "Cardiology"),
    (r"^Corpus C/NEW_Resp|^Corpus C/NEW_Investigations_Resp", "Respiratory"),
    (r"^Corpus C/NEW_Gastro|^Corpus C/NEW_Investigations_Gastro|^Corpus C/NEW_Drugs_12", "Gastroenterology"),
    (r"^Corpus C/NEW_Neuro|^Corpus C/NEW_Drugs_15", "Neurology"),
    (r"^Corpus C/NEW_Ophthal|^Corpus C/NEW_Drugs_11", "Ophthalmology"),
    (r"^Corpus C/NEW_Investigations_Endocrine|^Corpus C/NEW_Drugs_10", "Endocrinology and Metabolic"),
    (r"^Corpus C/NEW_Investigations_Renal|^Corpus C/NEW_Drugs_07", "Renal and Urology"),
    (r"^Corpus C/NEW_Infectious|^Corpus C/NEW_Drugs_05", "Infectious Diseases"),
    (r"^Corpus C/NEW_Derm|^Corpus C/NEW_Drugs_08", "Dermatology"),
    (r"^Corpus C/NEW_Investigations_Haem|^Corpus C/NEW_Drugs_14", "Haematology and Oncology"),
    (r"^Corpus C/NEW_Ortho|^Corpus C/NEW_Investigations_Ortho", "Orthopaedics and Trauma"),
    (r"^Corpus C/NEW_Investigations_Rheum", "Rheumatology"),
    (r"^Corpus C/NEW_ENT|^Corpus C/NEW_Drugs_09", "ENT"),
    (r"^Corpus C/NEW_Psych|^Corpus C/NEW_Drugs_17|^Corpus C/NEW_Drugs_03", "Psychiatry and Toxicology"),
    (r"^Corpus C/NEW_Drugs_04", "Psychiatry and Toxicology"),
    (r"^Corpus C/NEW_Investigations_Obstetrics|^Corpus C/NEW_Gynae", "Obstetrics and Gynaecology"),
    (r"^Corpus C/NEW_Safeguarding|^Corpus C/NEW_Investigations_General", "General Practice and Prevention"),
    (r"^Corpus C/NEW_Exam_Manoeuvres|^Corpus C/NEW_Drugs_01|^Corpus C/NEW_Drugs_02", "Clinical Skills and Process"),
    (r"^Corpus C/NEW_Breast", "General Practice and Prevention"),
    (r"^Corpus C/NEW_Acid-Base", "Renal and Urology"),
    (r"^Corpus C/NEW_Renal_and_Urology|^Corpus C/NEW_Drugs_13", "Renal and Urology"),
    (r"^Corpus C/NEW_Obstetrics|^Corpus C/NEW_Drugs_16", "Obstetrics and Gynaecology"),
    (r"^Corpus C/NEW_Drugs_18", "Respiratory"),
    (r"^Corpus C/NEW_Rheumatology|^Corpus C/NEW_Drugs_19", "Rheumatology"),
    (r"^Corpus C/NEW_Drugs_20", "General Practice and Prevention"),
    (r"^Corpus C/NEW_Drugs_21", "Clinical Skills and Process"),
    (r"^Corpus C/NEW_Geriatrics", "Geriatrics"),
    (r"^Corpus C/NEW_Investigations_Infectious", "Infectious Diseases"),
    (r"^Corpus A/(History-Taking|Examination|Investigation-Interpretation|Clinical-Process|Communication|Medications_Reference)", "Clinical Skills and Process"),
    (r"^Corpus B/A(1|2|3|4|5|6|7|8|9)_|^Corpus B/A10_|^Corpus B/F0", "Emergency (Corpus B, unmerged source)"),
    (r"^Corpus B/B[1-6]_", "Cardiology (Corpus B, unmerged source)"),
    (r"^Corpus B/C[1-7]_", "Gastroenterology (Corpus B, unmerged source)"),
    (r"^Corpus B/D[1-7]_", "Neurology (Corpus B, unmerged source)"),
    (r"^Corpus B/GER", "Geriatrics (Corpus B, unmerged source)"),
]
TOPIC_ORDER = [
    "Cardiology", "Respiratory", "Gastroenterology", "Neurology",
    "Endocrinology and Metabolic", "Renal and Urology", "Infectious Diseases",
    "Haematology and Oncology", "Orthopaedics and Trauma", "Rheumatology",
    "Dermatology", "ENT", "Ophthalmology", "Psychiatry and Toxicology",
    "Paediatrics", "Obstetrics", "Gynaecology", "Obstetrics and Gynaecology",
    "Geriatrics", "General Practice and Prevention",
    "Anaesthetics and Perioperative", "Clinical Skills and Process",
]


def topic_of(relpath):
    for pat, name in TOPIC_RULES:
        if re.search(pat, relpath):
            return name
    return "Unclassified"


def _cells(line):
    """Split a markdown table row, stripping emphasis from each cell.

    B26 is written `| **B26** |`. A naive `^\| *[A-Z][0-9]` misses exactly that one row —
    and it is the row carrying the reasoning that both 15% and 20% appear in Australian
    sources and must not be tidied to one number. Measured: 126 naive vs 127 tolerant.
    Rule 2, markdown emphasis, in a table field.
    """
    # Split on unescaped pipes only. A cell may contain `\|` — the SAH known-absence row
    # holds the pattern `Fisher grade\|WFNS\|SAH grad`, and a naive split truncated it at
    # the first alternation, losing the finding that there is no SAH grading scale at all.
    parts = [c.replace("\x00", "|").strip()
             for c in line.strip().strip("|").replace("\\|", "\x00").split("|")]
    return [re.sub(r"^\*+|\*+$", "", c).strip() for c in parts]


def parse_pending(root):
    """Open (unticked) rows from PENDING_GUIDELINE_CHECKS.md. READ-ONLY."""
    path = os.path.join(root, "PENDING_GUIDELINE_CHECKS.md")
    if not os.path.isfile(path):
        return []
    rows = []
    for i, line in enumerate(read(path).split("\n"), 1):
        if not line.startswith("|") or "⬜" not in line:
            continue
        c = _cells(line)
        if len(c) < 3:
            continue
        ident = c[0]
        if not re.match(r"^[A-Z][0-9A-Za-z-]*$", ident):
            continue
        fname = c[1].replace("`", "").strip()
        rest = [x for x in c[2:] if x and x != "⬜" and not x.startswith("⬜")]
        # Sections D and E use a different column layout: field 2 is a TOPIC DESCRIPTION,
        # not a file. 89 of 164 open rows are like this. Classifying them by file would be
        # fabricating a mapping, so they are flagged and routed to their own section.
        has_file = bool(re.search(r"\.md\b", fname))
        rows.append({"id": ident, "file": fname if has_file else "", "line": i,
                     "subject": "" if has_file else fname,
                     "text": " · ".join(rest)})
    return rows


def parse_known_absences(root):
    path = os.path.join(root, "_meta", "KNOWN_ABSENCES.md")
    if not os.path.isfile(path):
        return []
    out, cur = [], None
    for line in read(path).split("\n"):
        m = re.match(r"^## \d+\.\s*(.+)$", line)
        if m:
            cur = {"title": m.group(1).strip(), "where": "", "why": "",
                   "found": "", "verified": ""}
            out.append(cur)
            continue
        if cur is None:
            continue
        c = _cells(line) if line.startswith("|") else []
        if len(c) >= 2:
            k = c[0].lower()
            if "where it should live" in k:
                cur["where"] = c[1]
            elif "why it matters" in k or "why this one" in k:
                cur["why"] = cur["why"] or c[1]
            elif "how it was found" in k:
                cur["found"] = c[1]
            elif "verified absent" in k:
                # The finding often lives HERE, not in "why it matters": the SAH row is
                # where "Fisher grade|WFNS|SAH grad -> 0" is recorded, which is the point
                # that it is not one missing eponym but no grading scale at all.
                cur["verified"] = c[1]
    return out


def parse_no_baseline(root):
    out = []
    for path in md_files(root):
        r = rel(root, path)
        lines = read(path).split("\n")
        for i, line in enumerate(lines):
            for m in RE_NO_BASELINE.finditer(line):
                head = ""
                for j in range(i, max(-1, i - 8), -1):
                    if "Added from unverified layer" in lines[j] or re.match(r"^#{2,4} ", lines[j]):
                        head = re.sub(r"^[>#\s]*(\[![a-z]+\])?\s*", "", lines[j]).strip()
                        head = head.replace("Added from unverified layer — ", "")
                        break
                out.append({"file": r, "line": i + 1, "heading": head.strip("* "),
                            "marker": m.group(0).strip("`")})
    return out



def check_pending_staleness(root, rows):
    """Flag open tracker rows whose file is gone or whose section no longer resolves.

    REPORT ONLY — never edits PENDING_GUIDELINE_CHECKS.md (§1.14: manual ID sequence,
    append-never-delete history). The tracker predates the merge; Step 28b refiled
    sections and Step 29 added them, so a row citing a moved section number reads as
    authoritative while pointing at the wrong place — the inherited-0.7 failure.
    """
    by_base = {}
    for f in md_files(root):
        by_base.setdefault(os.path.basename(f), []).append(f)
    stale = []
    for r in rows:
        # A cell can hold several backticked filenames, and the tracker abbreviates long
        # ones with an ellipsis. A naive basename() on the whole cell reported 16 false
        # FILE NOT FOUNDs on the first run — rule 3, the scan's own false positives.
        names = re.findall(r"[\w.\-]+\.md", r["file"])
        if not names:
            continue
        if any("..." in n or "…" in n for n in names):
            continue          # abbreviated in the tracker; not resolvable, not stale
        missing_files = [n for n in names if not by_base.get(os.path.basename(n))]
        if missing_files:
            stale.append((r, "file not found: " + ", ".join(missing_files)))
            continue
        cands = by_base[os.path.basename(names[0])]
        # ONLY explicit section references. A bare decimal in this tracker is
        # overwhelmingly a DOSE: the first version of this check flagged B8 (gentamicin
        # 4.5-7 mg/kg), B50 (the ASCIA <7.5 kg band) and B43 (0.15 mg / 0.3 mg adrenaline)
        # as missing sections. Three flags, three false positives, all of them the
        # paediatric figures rule 5 exists for. Rule 3: fix the scan, do not report the noise.
        # Drop cross-document references first: `CLAUDE.md §1.6` points at the project
        # rules, not at the clinical file this row cites. That was the fourth and last
        # artifact class this check produced before it reported anything true.
        txt = re.sub(r"[\w.\-]+\.md\s*§\s*\d+(?:\.\d+)*", " ", r["text"])
        txt = re.sub(r"\bCLAUDE\b[^§]{0,20}§\s*\d+(?:\.\d+)*", " ", txt)
        secs = re.findall(r"(?:§|\bsections?\s+)(\d+\.\d+(?:\.\d+)*)", txt)
        if not secs:
            continue
        body = read(cands[0])
        missing = [x for x in secs
                   if not re.search(r"^#{2,4} " + re.escape(x) + r"[ \b]", body, re.M)]
        if missing and len(missing) == len(secs):
            stale.append((r, "section(s) not found as a heading: " + ", ".join(missing)))
    return stale


def cmd_study(args):
    root = args.dir
    unverified, conflicts, mirrors, _pf = collect(root)
    pending = parse_pending(root)
    absences = parse_known_absences(root)
    nobase = parse_no_baseline(root)
    op = [c for c in conflicts if c.get("status", "OPEN").upper() == "OPEN"]

    buckets = {}
    def add(topic, key, item):
        buckets.setdefault(topic, {}).setdefault(key, []).append(item)

    for n in nobase:
        if n["file"].startswith("Corpus B/"):
            continue
        add(topic_of(n["file"]), "nb", n)
    for c in op:
        add(topic_of(c["file"]), "cf", c)
    nofile_pending = []
    for r in pending:
        if not r["file"]:
            nofile_pending.append(r)
            continue
        t = "Unclassified"
        for pat, name in TOPIC_RULES:
            bare = pat.replace("^Corpus A/", "").replace("^Corpus C/", "").replace("^Corpus B/", "").replace("^", "")
            if re.search(bare, r["file"]):
                t = name
                break
        add(t, "pg", r)
    # Corpus B is the unmerged SOURCE, not study material. Its markers duplicate content
    # already merged into A and C, and counting them made "Emergency" show 38 actionable
    # items in files the reader never opens. VERIFICATION_QUEUE.md still covers all of it.
    skipped_b = 0
    for u in unverified:
        if u["file"].startswith("Corpus B/"):
            skipped_b += 1
            continue
        add(topic_of(u["file"]), {"OPEN": "act", "MIXED": "act",
                                  "UNKNOWN": "tri", "LOGIN": "not"}[u["act"]], u)
    for a in absences:
        t = "Unclassified"
        for pat, name in TOPIC_RULES:
            if re.search(pat.replace("^Corpus A/", "").replace("^Corpus C/", "").replace("^", ""), a["where"]):
                t = name
                break
        add(t, "ka", a)

    stale = check_pending_staleness(root, pending)
    today = _dt.date.today().isoformat()
    tri_order = {"R1": 0, "R2": 1, "R3": 2}
    o = []
    o.append("---")
    o.append("name: study-checks")
    o.append("description: Generated by `merge_tools.py study`. Do not hand-edit — edit the "
             "marker in the file, or the hand-maintained source, then rerun.")
    o.append("---")
    o.append("")
    o.append(f"# Study checks — by clinical topic — generated {today}")
    o.append("")
    o.append("**What this is for.** `_meta/VERIFICATION_QUEUE.md` answers *what is my "
             "highest-risk unverified content, corpus-wide*. **This file answers *what "
             "should I check while reading gastro today*.** Both are generated; neither "
             "replaces the other, and the queue is unchanged.")
    o.append("")
    o.append("**ACTIONABLE means an open Australian source is named in the marker** — ANZCOR, "
             "ASCIA, RCH, RACGP, the Immunisation Handbook, PBS and similar. No login. "
             "The number at the head of each topic is that count and nothing else, because "
             "it is the only number you can act on in an afternoon.")
    o.append("")
    o.append("> [!warning] Provenance — three of these sections are NOT derived from markers")
    o.append("> Regenerating cannot recreate them, and a future session must not try.")
    o.append("> - **NO-BASELINE · OPEN CONFLICTS · VERIFICATION MARKERS** — derived from "
             "markers in the corpus. Regenerate freely.")
    o.append("> - **GUIDELINE CHECKS** — read from `PENDING_GUIDELINE_CHECKS.md`, which is "
             "**hand-maintained with a manual ID sequence and an append-never-delete "
             "history**. This file reads it and never writes back (§1.14).")
    o.append("> - **KNOWN ABSENCES** — read from `_meta/KNOWN_ABSENCES.md`, hand-maintained. "
             "These have no marker because they have **no page to mark**.")
    o.append("")

    total_act = sum(len(b.get("act", [])) for b in buckets.values())
    o.append(f"**Corpus-wide: {total_act} actionable, {len(op)} open conflicts, "
             f"{len(nobase)} NO-BASELINE blocks, {len(pending)} open guideline checks.**")
    o.append("")
    o.append("| Topic | Actionable | NO-BASELINE | Conflicts | Guideline | Triage | Noted |")
    o.append("|---|---|---|---|---|---|---|")
    ordered = [t for t in TOPIC_ORDER if t in buckets] + \
              sorted(t for t in buckets if t not in TOPIC_ORDER)
    for t in ordered:
        b = buckets[t]
        o.append(f"| [{t}](#{t.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '')}) "
                 f"| **{len(b.get('act', []))}** | {len(b.get('nb', []))} | {len(b.get('cf', []))} "
                 f"| {len(b.get('pg', []))} | {len(b.get('tri', []))} | {len(b.get('not', []))} |")
    o.append("")
    o.append("---")
    o.append("")

    for t in ordered:
        b = buckets[t]
        o.append(f"## {t}")
        o.append("")
        o.append(f"> **{len(b.get('act', []))} ACTIONABLE** — open AU source named, no login. "
                 f"({len(b.get('nb', []))} no-baseline · {len(b.get('cf', []))} conflicts · "
                 f"{len(b.get('pg', []))} guideline checks · {len(b.get('tri', []))} triage · "
                 f"{len(b.get('not', []))} noted)")
        o.append("")

        if b.get("nb"):
            o.append(f"### NO-BASELINE blocks ({len(b['nb'])}) · *derived from markers*")
            o.append("")
            o.append("**Nothing in the corpus disagrees with these, so no cross-check will "
                     "ever catch an error in them.** Read them as the only account of their "
                     "topic in the vault.")
            o.append("")
            for n in sorted(b["nb"], key=lambda x: (x["file"], x["line"])):
                o.append(f"- **{n['heading'] or '(block)'}** — `{n['file']}` L{n['line']}")
                o.append(f"  - {n['marker']}")
            o.append("")

        if b.get("cf"):
            o.append(f"### OPEN CONFLICTS ({len(b['cf'])}) · *derived from markers*")
            o.append("")
            for c in sorted(b["cf"], key=lambda x: tri_order.get(x["tier"], 9)):
                o.append(f"- **{c['id']}** [{c['tier']}] — {c['title']}")
                o.append(f"  - `{c['file']}` L{c['line']} · _{c['section']}_")
            o.append("")

        if b.get("pg"):
            o.append(f"### GUIDELINE CHECKS ({len(b['pg'])}) · *READ-ONLY from "
                     "`PENDING_GUIDELINE_CHECKS.md` — hand-maintained, never written back*")
            o.append("")
            for r in sorted(b["pg"], key=lambda x: x["id"]):
                o.append(f"- **{r['id']}** · `{r['file']}`")
                o.append(f"  - {r['text']}")
            o.append("")

        if b.get("act"):
            o.append(f"### VERIFICATION — ACTIONABLE ({len(b['act'])}) · *derived from markers*")
            o.append("")
            for u in sorted(b["act"], key=lambda x: (tri_order.get(x["tier"], 9), x["file"], x["line"])):
                o.append(f"- **[{u['tier']}]** `{u['file']}` L{u['line']} · _{u['section']}_ "
                         f"· `{u['trust']}`")
                o.append(f"  - {u['scope']}")
            o.append("")

        if b.get("tri"):
            o.append(f"### VERIFICATION — TRIAGE ({len(b['tri'])}) · *derived from markers*")
            o.append("")
            o.append("No source named in the marker. **Scope shown so you can judge whether "
                     "it matters** — these are not hidden, they are unsorted.")
            o.append("")
            for u in sorted(b["tri"], key=lambda x: (tri_order.get(x["tier"], 9), x["file"], x["line"])):
                o.append(f"- **[{u['tier']}]** `{u['file']}` L{u['line']} · _{u['section']}_ — "
                         f"{u['scope'][:200]}")
            o.append("")

        if b.get("not"):
            o.append(f"### VERIFICATION — PERMANENTLY NOTED ({len(b['not'])}) · "
                     "*derived from markers*")
            o.append("")
            o.append("Therapeutic Guidelines / AMH / AIDH / eviQ — **login-gated, and by §1.8 "
                     "nobody will consult them.** These are a standing instruction to look it "
                     "up at the point of use, which is correct for dosing anyway. **Not a "
                     "to-do list. Never delete one.**")
            o.append("")
            for u in sorted(b["not"], key=lambda x: (tri_order.get(x["tier"], 9), x["file"], x["line"])):
                o.append(f"- **[{u['tier']}]** `{u['file']}` L{u['line']} · _{u['section']}_ — "
                         f"{u['scope'][:160]}")
            o.append("")

        if b.get("ka"):
            o.append(f"### KNOWN ABSENCES ({len(b['ka'])}) · *READ-ONLY from "
                     "`_meta/KNOWN_ABSENCES.md` — hand-maintained, no marker exists*")
            o.append("")
            for a in b["ka"]:
                o.append(f"- **{a['title']}**")
                if a["where"]:
                    o.append(f"  - *Should live in:* {a['where']}")
                if a["verified"]:
                    o.append(f"  - *Verified absent:* {a['verified']}")
                if a["why"]:
                    o.append(f"  - *Why it matters:* {a['why']}")
            o.append("")
        o.append("---")
        o.append("")

    if nofile_pending:
        o.append("## GUIDELINE CHECKS with no file reference "
                 f"({len(nofile_pending)}) · *READ-ONLY from `PENDING_GUIDELINE_CHECKS.md`*")
        o.append("")
        o.append("Sections D and E of the tracker use a different column layout: the second "
                 "field is a **topic description, not a file**. These are Phase 5 build items "
                 "awaiting an Australian source — content that does not exist yet, so there "
                 "is no file to file them under. **Assigning them to a topic by keyword "
                 "would be fabricating a mapping**, so they are listed together.")
        o.append("")
        for r in sorted(nofile_pending, key=lambda x: x["id"]):
            o.append(f"- **{r['id']}** — {r['subject']}")
            if r["text"]:
                o.append(f"  - {r['text'][:220]}")
        o.append("")

    o.append("## Structural notes — hand-maintained, not derivable from any marker")
    o.append("")
    o.append("- **Unicode search forms.** `CHA₂DS₂-VASc` is stored with subscripts. A "
             "plain-ASCII search finds none of its seven occurrences. `inventory.py` folds "
             "₀–₉ and ⁰–⁹; a bare grep does not.")
    o.append("- **Checklist stub categories.** `checklist.csv` has 24 categories; several are "
             "stubs of ≤11 rows. See `_meta/CHECKLIST_CATEGORY_AUDIT.md` — the corpus is "
             "complete against its own specification and **the specification has holes**.")
    o.append("- **`NEW_Drugs_04_Antidotes_and_Antivenoms` is reachable only via its four "
             "pointers.** Nothing in Corpus A linked to it before those were added; it is "
             "thorough and was effectively unreachable.")
    o.append(f"- **Corpus B is excluded from this file.** It is the unmerged *source*, not "
             f"study material — its markers duplicate content already merged into A and C. "
             f"{skipped_b} markers were skipped here and remain in "
             f"`_meta/VERIFICATION_QUEUE.md`, which is corpus-wide and unchanged.")
    o.append("")

    if stale:
        o.append("## ⚠ STALE TRACKER ROWS — reported, NOT edited")
        o.append("")
        o.append(f"{len(stale)} open row(s) in `PENDING_GUIDELINE_CHECKS.md` cite a file or "
                 "section that no longer resolves. **The tracker predates the merge** — Step "
                 "28b refiled sections and Step 29 added them — so a row citing a moved "
                 "section reads as authoritative while pointing at the wrong place.")
        o.append("")
        o.append("**Not edited** (§1.14: manual ID sequence, append-never-delete history). "
                 "Fix by hand.")
        o.append("")
        o.append("**Scope of this check.** It resolves *filenames* and *explicit* `§x.y` "
                 "section references only. **Bare line numbers in the tracker's Line column "
                 "are not checked and cannot be** — every merge shifts them, so they are "
                 "stale by construction rather than by error. Treat a Line value as a hint, "
                 "never as a location.")
        o.append("")
        for r, why in stale:
            o.append(f"- **{r['id']}** · `{r['file']}` — {why}")
            o.append(f"  - {r['text'][:180]}")
        o.append("")

    if not args.dry_run:
        os.makedirs(os.path.join(root, "_meta"), exist_ok=True)
    write(os.path.join(root, "_meta", "STUDY_CHECKS.md"), "\n".join(o))
    print(f"study: {len(ordered)} topics · {total_act} actionable · {len(op)} conflicts · "
          f"{len(nobase)} no-baseline · {len(pending)} guideline checks "
          f"({len(nofile_pending)} with no file) · {len(absences)} known absences · "
          f"{skipped_b} Corpus B markers excluded")
    if stale:
        print(f"  ⚠ {len(stale)} stale tracker row(s) reported (not edited):")
        for r, why in stale:
            print(f"      {r['id']} · {r['file']} — {why}")
    report_writes(root, "study")


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
                    # SCOPE ONLY — never the surrounding line. A marker's source is what
                    # the MARKER names. Passing the line let an unrelated source name leak
                    # in: 08_09 L17 is a verification box mentioning RCH that happens to
                    # contain a marker scoped "AU regimen; Therapeutic Guidelines (login)",
                    # and the box's RCH made it read as partly actionable. A box mentioning
                    # RCH does not make an eTG marker RCH-settleable.
                    #
                    # Deliberately UNDER-claims: a marker wrongly in triage costs a read; one
                    # wrongly in actionable costs a wasted lookup and a false sense that the
                    # queue is shorter than it is.
                    "act": actionability(m.group(1)),
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
    if not args.dry_run:
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
        [r for r in unverified if r["act"] == "MIXED"],
        "Partly actionable — an open source settles part, a login source settles the rest",
        "**These name BOTH kinds of source.** Work the open-source part now; the remainder "
        "stays a standing instruction to look up at the point of use, exactly as a "
        "login-only item does. Do not file these as done when the open part is closed.",
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
        if r["tier"] != "R1" or r["act"] in ("LOGIN", "MIXED"):
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
    stamped = []
    # Files with a NO-BASELINE marker but no conflict would otherwise never be stamped —
    # a counter that only appears on files that already had a counter is not a counter.
    for extra in md_files(root):
        if extra not in per_file and RE_NO_BASELINE.search(read(extra)):
            per_file[extra] = (0, 0)
    for path, (open_ct, r1_ct) in per_file.items():
        text = read(path)
        fm, body = split_frontmatter(text)
        if fm is None:
            continue
        nb_ct = len(RE_NO_BASELINE.findall(text))
        if (fm_get(fm, "conflicts_open") == str(open_ct)
                and fm_get(fm, "conflicts_r1") == str(r1_ct)
                and fm_get(fm, "no_baseline") == str(nb_ct)):
            continue
        fm = fm_set(fm, "conflicts_open", open_ct)
        fm = fm_set(fm, "conflicts_r1", r1_ct)
        fm = fm_set(fm, "no_baseline", nb_ct)
        if not args.dry_run:
            write(path, rebuild(fm, body))
        stamped.append((rel(root, path), open_ct, r1_ct, nb_ct))

    acts = {}
    for r in unverified:
        acts[r["act"]] = acts.get(r["act"], 0) + 1
    print(f"  actionable without login: {acts.get('OPEN', 0)} · "
          f"partly actionable (open + login): {acts.get('MIXED', 0)} · "
          f"needs triage: {acts.get('UNKNOWN', 0)} · "
          f"login-required (permanently noted): {acts.get('LOGIN', 0)}")
    print(f"scan: {len(unverified)} unverified · {len(op)} open conflicts "
          f"({len([c for c in op if c['tier'] == 'R1'])} R1) · "
          f"{len(mirrors)} dose mirrors")
    print(f"  frontmatter counters updated in {len(stamped)} files"
          + (" (dry run)" if args.dry_run else ""))
    for r, o, r1, nb in stamped:
        print(f"    {r} — conflicts_open={o} conflicts_r1={r1} no_baseline={nb}")
    report_writes(root, "scan")


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

            # Malformed inline markers. A marker that is WRITTEN but does not PARSE is
            # the worst failure shape in this design: the file looks annotated, the
            # verification queue never hears about it, and nothing raises an error.
            # Found 2026-08-31 — two markers written as `UNVERIFIED **R1** — ...`, where
            # RE_UNVERIFIED requires the separator to follow the word immediately. Both
            # silently contributed nothing.
            #
            # The bare token `UNVERIFIED` is EXEMPT: 36 Corpus B files and one Corpus C
            # file use it in prose to refer to the convention itself ("carries an
            # `UNVERIFIED` marker naming what to check"), which is not an attempted
            # marker. The failure shape is content present but unparseable.
            for m in RE_MARKER_SPAN.finditer(line):
                word, rest = m.group(1), m.group(2)
                if not rest.strip():
                    continue                      # bare prose reference, not a marker
                span = m.group(0)
                ok = (RE_UNVERIFIED.search(span) if word == "UNVERIFIED"
                      else RE_VERIFIED_TOK.search(span))
                if not ok:
                    problems.append(
                        f"{r} L{i+1}: MALFORMED {word} marker — written but does not "
                        f"parse, so it contributes nothing to the verification queue: "
                        f"{span[:80]}"
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

        # →MED: mirrors a FIGURE owned elsewhere (§1.7). A mirror on a line carrying no
        # figure is a cross-reference wearing a mirror's marker: it enters the dose-mirror
        # report as an entry with nothing to compare, so the report overstates how many
        # mirrored figures the vault actually has. Found 2026-08-31, when two such markers
        # were written during the B1 and B2 merges and the report showed 4 entries against
        # 3 real ones. Semantic misuse is not checkable in general; THIS case is.
        # Scope is the BLOCK, not the line. The established convention puts the marker on a
        # callout header and the figures in the table beneath it — all three real mirrors in
        # the vault look like that. A line-scoped test flagged every one of them as a
        # violation on its first run (rule 4: the scan's own false positives are the signal).
        for i, line in enumerate(lines):
            for m in RE_MED_MIRROR.finditer(line):
                block, j = [line], i + 1
                quoted = line.lstrip().startswith(">")
                while j < len(lines) and j - i <= MED_BLOCK_LOOKAHEAD:
                    nxt = lines[j]
                    if quoted:
                        if not nxt.lstrip().startswith(">"):
                            break
                    elif not nxt.strip():
                        break
                    block.append(nxt)
                    j += 1
                if not RE_DOSE.search("\n".join(block)):
                    problems.append(
                        f"{r} L{i+1}: →MED:{m.group(1)} in a block stating no figure — "
                        f"→MED mirrors a figure owned elsewhere; a pointer with no figure "
                        f"should be a plain cross-reference — {line.strip()[:80]}"
                    )
            # a marker that looks like a mirror but does not parse contributes nothing and
            # raises nothing — the same silence the MALFORMED check exists to break.
            if RE_MED_LOOSE.search(line) and not RE_MED_MIRROR.search(line):
                problems.append(
                    f"{r} L{i+1}: MALFORMED →MED marker — written but does not parse, so "
                    f"it contributes nothing to the dose-mirror report: {line.strip()[:80]}"
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
    """Report non-AU drug names, and mark hits inside deliberately non-Australian blocks.

    A block flagged as UK/non-AU is skipped for renaming: the foreign drug name is often
    the only thing marking that content as foreign, so renaming it makes UK figures read
    as Australian. Found in 02_Respiratory, where "UK figures (unverified for AU use):
    co-amoxiclav 500/125mg tds" sits directly under an Australian regimen.
    """
    hits, skipped, dual = [], [], []
    for path in md_files(args.dir):
        text = read(path)
        r = rel(args.dir, path)
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            # a non-AU flag on this line, or on the callout block it belongs to
            block_flag = matches(RE_NON_AU_BLOCK, line)
            if not block_flag and line.lstrip().startswith(">"):
                for j in range(i - 2, max(-1, i - 12), -1):
                    if not lines[j].lstrip().startswith(">"):
                        break
                    if matches(RE_NON_AU_BLOCK, lines[j]):
                        block_flag = True
                        break
            for bad, (good, src) in DRUG_NAMING.items():
                pat = DRUG_PATTERNS[bad]
                if not (pat.search(line) or pat.search(normalise(line))):
                    continue
                # Dual naming: "furosemide (frusemide)", "adrenaline (epinephrine)",
                # "lidocaine (lignocaine)". The AU name is already present and leading,
                # so this is correct as written, not a leftover. Corpus C's drug files
                # do this deliberately.
                if re.search(r"\b" + re.escape(good.split("+")[0]) + r"\b",
                             normalise(line), re.I):
                    dual.append(f"{r} L{i}: `{bad}` alongside `{good}` — dual naming, "
                                f"correct as written")
                    continue
                entry = (f"{r} L{i}: `{bad}` -> {good}\n      {line.strip()[:120]}"
                         f"\n      source: {src}")
                (skipped if block_flag else hits).append(entry)

    print(f"drugs: {len(hits)} actionable non-AU naming hits "
          f"· {len(skipped)} skipped inside a flagged non-AU block "
          f"· {len(dual)} dual-naming, correct as written")
    for h in hits[: args.limit]:
        print(f"  {h}")
    if len(hits) > args.limit:
        print(f"  ... and {len(hits) - args.limit} more")
    if skipped:
        print("\n  SKIPPED — inside a block flagged as non-Australian; renaming here would "
              "make foreign figures read as Australian:")
        for h in skipped:
            print(f"    {h.splitlines()[0]}")
    if dual:
        print("\n  DUAL NAMING — AU name already present and leading; correct as written:")
        for h in dual:
            print(f"    {h}")
    p = log_run(args.dir, "drugs",
                hits + ["", "SKIPPED (non-AU blocks):"] + skipped
                     + ["", "DUAL NAMING (no action):"] + dual)
    print(f"  log: {p}")


# ---------------------------------------------------------------- paed


def cmd_paed(args):
    report = []
    for path in md_files(args.dir):
        r = rel(args.dir, path)
        text = read(path)
        fm, _ = split_frontmatter(text)
        # CLAUDE.md rule 9. The previous test was `"paed" in r.lower()`, and the word
        # ortho-PAED-ics contains "paed", so this sweep silently skipped 5 orthopaedic
        # files (11_01, 11_06, 11_09a, NEW_Investigations_Orthopaedics..., 
        # NEW_Orthopaedics_and_Trauma) for a reason unrelated to their content, and
        # reported no error. Skip on the frontmatter label or an anchored path pattern.
        if fm_get(fm, "population") == "paed" or RE_PAED_PATH.search(r):
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


# ---------------------------------------------------------------- precommit


# Anchored to line start. A conflict marker only ever appears at column 0; matching it
# unanchored would fire on prose about conflict markers — including this file and the
# workflow document that documents the guard (rule 9).
RE_CONFLICT_MARKER = re.compile(r"^(<{7}|={7}|>{7})(\s|$)")


def cmd_precommit(args):
    """Refuse to let a conflict marker reach a commit.

    `git add -A` stages a file containing conflict markers without complaint, and
    `git commit` commits it. Nothing in git refuses this. A markdown file with markers in
    it still renders and still opens in Obsidian, so in a clinical vault the corrupted
    region reads as two competing versions of the same guidance with nothing saying which
    is current. This is the guard that git does not provide.

    Checks STAGED content, not the working tree — that is what is about to be committed.
    """
    staged = subprocess.run(["git", "diff", "--cached", "--name-only", "-z"],
                            cwd=args.dir, capture_output=True, text=True)
    if staged.returncode != 0:
        print("precommit: not a git repository, or git unavailable")
        return 1
    names = [n for n in staged.stdout.split("\0") if n]
    if not names:
        print("precommit: nothing staged")
        return 0

    bad = []
    for name in names:
        blob = subprocess.run(["git", "show", f":{name}"],
                              cwd=args.dir, capture_output=True, text=True)
        if blob.returncode != 0:          # deleted, or not a regular blob
            continue
        for i, line in enumerate(blob.stdout.split("\n"), 1):
            if RE_CONFLICT_MARKER.match(line):
                bad.append((name, i, line[:70]))

    # An unresolved merge/rebase is itself a refusal condition, even with nothing marked:
    # it means files are still in a conflicted state and `git add -A` would sweep them in.
    unmerged = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"],
                              cwd=args.dir, capture_output=True, text=True).stdout.split()

    if bad or unmerged:
        print(f"precommit: REFUSED — {len(bad)} conflict marker(s) staged"
              + (f", {len(unmerged)} file(s) still unmerged" if unmerged else ""))
        for name, i, line in bad[: args.limit]:
            print(f"    {name} L{i}: {line}")
        if len(bad) > args.limit:
            print(f"    ... and {len(bad) - args.limit} more")
        for u in unmerged:
            print(f"    STILL UNMERGED: {u}")
        print("\n  Resolve every conflicted file, re-check `git status`, then re-run.")
        return 1

    print(f"precommit: OK — {len(names)} staged file(s), no conflict markers")
    return 0


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
    p = sub.add_parser("precommit"); common(p); p.set_defaults(fn=cmd_precommit)
    p = sub.add_parser("lint"); common(p); p.set_defaults(fn=cmd_lint)
    p = sub.add_parser("drugs"); common(p); p.set_defaults(fn=cmd_drugs)
    p = sub.add_parser("paed"); common(p); p.set_defaults(fn=cmd_paed)
    p = sub.add_parser("study"); common(p); p.set_defaults(fn=cmd_study)

    args = ap.parse_args()
    global DRY_RUN
    DRY_RUN = bool(getattr(args, "dry_run", False))
    if not os.path.isdir(args.dir):
        sys.exit(f"not a directory: {args.dir}")
    sys.exit(args.fn(args) or 0)


if __name__ == "__main__":
    main()
