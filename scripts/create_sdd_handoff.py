#!/usr/bin/env python3
"""Create a structured, resumable SDD handoff record."""
from __future__ import annotations

import argparse
from pathlib import Path

from engine.sdd_handoff import STAGES, STATUSES, write_handoff


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feature-dir", type=Path, required=True)
    parser.add_argument("--stage", choices=sorted(STAGES), required=True)
    parser.add_argument("--status", choices=sorted(STATUSES), required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--next-step", required=True)
    parser.add_argument("--blocker", action="append", default=[])
    parser.add_argument("--risk", action="append", default=[])
    parser.add_argument("--evidence", action="append", default=[])
    args = parser.parse_args()
    output = write_handoff(args.feature_dir, stage=args.stage, status=args.status,
                           owner=args.owner, next_step=args.next_step,
                           blockers=args.blocker, risks=args.risk, evidence=args.evidence)
    print(f"Created SDD handoff: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
