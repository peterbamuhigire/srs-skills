#!/usr/bin/env python3
"""For each unique project touched by staged files, run engine.cli validate."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

def project_roots(paths: list[str]) -> set[Path]:
    out: set[Path] = set()
    for p in paths:
        parts = Path(p).parts
        if len(parts) >= 2 and parts[0] == "projects":
            out.add(Path(parts[0]) / parts[1])
    return out

def main(argv: list[str]) -> int:
    failed = 0
    for root in sorted(project_roots(argv)):
        print(f"==> validating {root}")
        rc = subprocess.call([sys.executable, "-m", "engine", "validate", str(root)])
        if rc != 0:
            failed += 1
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
