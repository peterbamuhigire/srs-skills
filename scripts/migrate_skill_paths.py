#!/usr/bin/env python3
"""Apply the Plan 04 skill-path migration.

REWRITE files: substitute legacy paths with canonical projects/<ProjectName>/...
WRAP files: bracket the legacy reference in <!-- alias-block start --> / <!-- alias-block end -->

Usage:
    python scripts/migrate_skill_paths.py            # apply all changes
    python scripts/migrate_skill_paths.py --dry-run  # print what would change

Reads docs/migration/skill-paths-2026-04-16.csv to get the file list; uses a
hard-coded WRAP set (the 5 README files that explain the alias relationship).
"""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

WRAP_FILES = {
    "01-strategic-vision/README.md",
    "02-requirements-engineering/agile/README.md",
    "02-requirements-engineering/waterfall/README.md",
    "03-design-documentation/README.md",
    "06-deployment-operations/README.md",
}

# Longest-match substitutions first so trailing slashes don't get lost.
REWRITE_SUBS = [
    ("../project_context/", "projects/<ProjectName>/_context/"),
    ("../project_context",  "projects/<ProjectName>/_context"),
    ("../output/",           "projects/<ProjectName>/<phase>/<document>/"),
    ("../output",            "projects/<ProjectName>/<phase>/<document>"),
]

ALIAS_OPEN = "<!-- alias-block start -->"
ALIAS_CLOSE = "<!-- alias-block end -->"


def rewrite_body(body: str) -> str:
    for old, new in REWRITE_SUBS:
        body = body.replace(old, new)
    return body


def wrap_body(body: str) -> str:
    """Wrap every line containing a naked legacy reference in alias-block comments.

    Idempotent: if a line is already inside an alias block, leave it alone.
    """
    lines = body.splitlines(keepends=False)
    out: list[str] = []
    in_block = False
    for line in lines:
        lower = line.lower()
        if ALIAS_OPEN.lower() in lower:
            in_block = True
            out.append(line)
            continue
        if ALIAS_CLOSE.lower() in lower:
            in_block = False
            out.append(line)
            continue
        if in_block:
            out.append(line)
            continue
        if "../project_context/" in line or "../output/" in line or \
           "../project_context" in line or "../output" in line:
            out.append(ALIAS_OPEN)
            out.append(line)
            out.append(ALIAS_CLOSE)
        else:
            out.append(line)
    # Preserve trailing newline if original had one.
    joined = "\n".join(out)
    if body.endswith("\n") and not joined.endswith("\n"):
        joined += "\n"
    return joined


def collect_files_from_csv(csv_path: Path) -> set[str]:
    files: set[str] = set()
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            files.add(row["file"].replace("\\", "/"))
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    csv_path = ROOT / "docs" / "migration" / "skill-paths-2026-04-16.csv"
    all_files = collect_files_from_csv(csv_path)

    rewrite_count = 0
    wrap_count = 0
    for rel in sorted(all_files):
        path = ROOT / rel
        if not path.exists():
            print(f"SKIP (missing): {rel}")
            continue
        original = path.read_text(encoding="utf-8")
        if rel in WRAP_FILES:
            new = wrap_body(original)
            action = "WRAP"
        else:
            new = rewrite_body(original)
            action = "REWRITE"
        if new == original:
            continue
        if args.dry_run:
            print(f"DRY {action}: {rel}")
        else:
            path.write_text(new, encoding="utf-8")
            print(f"{action}: {rel}")
        if action == "REWRITE":
            rewrite_count += 1
        else:
            wrap_count += 1
    print(f"\nTotal: {rewrite_count} rewritten, {wrap_count} wrapped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
