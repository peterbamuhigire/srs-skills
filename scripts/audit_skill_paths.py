#!/usr/bin/env python3
"""Find every legacy ../project_context/ and ../output/ reference in skill files."""
from __future__ import annotations
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY = re.compile(r"\.\./project_context/|\.\./output/")
ALIAS_HINT = re.compile(r"\balias\b", re.IGNORECASE)

SKILL_DIRS = [
    "00-meta-initialization", "01-strategic-vision",
    "02-requirements-engineering", "03-design-documentation",
    "04-development-artifacts", "05-testing-documentation",
    "06-deployment-operations", "07-agile-artifacts",
    "08-end-user-documentation", "09-governance-compliance",
]

def main(out_csv: Path) -> int:
    rows = []
    for d in SKILL_DIRS:
        for path in (ROOT / d).rglob("*.md"):
            try:
                body = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for lineno, line in enumerate(body.splitlines(), start=1):
                if not LEGACY.search(line):
                    continue
                marked_alias = ALIAS_HINT.search(body) is not None
                rows.append({
                    "file": str(path.relative_to(ROOT)),
                    "line": lineno,
                    "snippet": line.strip()[:160],
                    "alias_documented_in_file": marked_alias,
                })
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["file", "line", "snippet", "alias_documented_in_file"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} legacy references written to {out_csv}")
    return 0

if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else (ROOT / "docs/migration/skill-paths-2026-04-16.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    sys.exit(main(out))
