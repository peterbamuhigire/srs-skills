#!/usr/bin/env python3
"""Validate an elicitation decision graph and report the current frontier."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

STATES = {"blocked", "frontier", "proposed", "confirmed", "superseded"}
REQUIRED = {"id", "question", "owner", "prerequisites", "options", "evidence", "state", "downstream"}


def validate(data: object) -> tuple[list[str], list[str]]:
    if not isinstance(data, dict) or not isinstance(data.get("decisions"), list):
        return ["root must contain a decisions list"], []
    findings: list[str] = []
    records: dict[str, dict] = {}
    for index, record in enumerate(data["decisions"]):
        if not isinstance(record, dict):
            findings.append(f"decision {index} must be a mapping")
            continue
        missing = REQUIRED - set(record)
        if missing:
            findings.append(f"decision {index} missing: {', '.join(sorted(missing))}")
            continue
        decision_id = record["id"]
        if not isinstance(decision_id, str) or not decision_id.strip():
            findings.append(f"decision {index} has invalid id")
            continue
        if decision_id in records:
            findings.append(f"duplicate decision id: {decision_id}")
        records[decision_id] = record
        if record["state"] not in STATES:
            findings.append(f"{decision_id}: unsupported state {record['state']!r}")
        for field in ("question", "owner"):
            if not isinstance(record[field], str) or not record[field].strip():
                findings.append(f"{decision_id}: {field} must be non-empty text")
        for field in ("prerequisites", "options", "evidence", "downstream"):
            if not isinstance(record[field], list):
                findings.append(f"{decision_id}: {field} must be a list")

    for decision_id, record in records.items():
        if not isinstance(record.get("prerequisites"), list):
            continue
        for dependency in record["prerequisites"]:
            if dependency not in records:
                findings.append(f"{decision_id}: unknown prerequisite {dependency!r}")

    frontier: list[str] = []
    if not findings:
        for decision_id, record in records.items():
            ready = all(records[item]["state"] in {"confirmed", "superseded"} for item in record["prerequisites"])
            if record["state"] == "frontier" and not ready:
                findings.append(f"{decision_id}: frontier decision has unresolved prerequisites")
            if record["state"] == "blocked" and ready:
                findings.append(f"{decision_id}: blocked decision is ready and should enter the frontier")
            if record["state"] == "frontier" and ready:
                frontier.append(decision_id)
    return sorted(findings), sorted(frontier)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path)
    args = parser.parse_args()
    try:
        data = yaml.safe_load(args.graph.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        print(f"[FAIL] cannot read decision graph: {exc}")
        return 1
    findings, frontier = validate(data)
    for finding in findings:
        print(f"[FAIL] {finding}")
    if findings:
        return 1
    print(f"decision-frontier: decisions={len(data['decisions'])} findings=0 frontier={','.join(frontier) or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
