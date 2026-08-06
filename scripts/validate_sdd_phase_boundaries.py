#!/usr/bin/env python3
"""Validate an SDD-style feature workspace at artifact boundaries."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.sdd_boundaries import validate_feature_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feature-dir", required=True, type=Path)
    parser.add_argument("--stage", choices=["spec-plan", "plan-tasks", "tasks-implement", "implement-qc", "all"], default="all")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    findings = validate_feature_dir(args.feature_dir, args.stage)
    if args.as_json:
        print(json.dumps([finding.__dict__ for finding in findings], indent=2))
    else:
        print(f"sdd-phase-boundary-validator: stage={args.stage}")
        if findings:
            for finding in findings:
                print(f"[{finding.severity.upper()}] {finding.code}: {finding.message}")
        else:
            print("PASS: no boundary findings")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
