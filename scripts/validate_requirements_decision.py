#!/usr/bin/env python3
"""Validate an SRS need/reuse decision or requirement-debt ledger."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.requirements_decision import load, validate_decision, validate_debt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--kind", choices=("decision", "debt"), default="decision")
    args = parser.parse_args()
    try:
        payload = load(args.path)
    except (OSError, json.JSONDecodeError) as exc:
        result = {"status": "FAIL", "errors": [str(exc)]}
    else:
        result = validate_debt(payload) if args.kind == "debt" else validate_decision(payload)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
