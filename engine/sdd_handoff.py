"""Write a resumable SDD stop or release handoff record."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

STAGES = {"spec-plan", "plan-tasks", "tasks-implement", "implement-qc", "all"}
STATUSES = {"in_progress", "blocked", "complete"}


def write_handoff(feature_dir: Path, *, stage: str, status: str, owner: str,
                  next_step: str, blockers: Iterable[str] = (),
                  risks: Iterable[str] = (), evidence: Iterable[str] = ()) -> Path:
    if stage not in STAGES:
        raise ValueError(f"unsupported stage: {stage}")
    if status not in STATUSES:
        raise ValueError(f"unsupported status: {status}")
    if not owner.strip() or not next_step.strip():
        raise ValueError("owner and next_step are required")
    blockers = [item.strip() for item in blockers if item.strip()]
    if status == "complete" and blockers:
        raise ValueError("complete handoff cannot contain blockers")
    payload = {
        "schema_version": 1,
        "feature": feature_dir.name,
        "stage": stage,
        "status": status,
        "owner": owner.strip(),
        "next_step": next_step.strip(),
        "blockers": blockers,
        "risks": [item.strip() for item in risks if item.strip()],
        "evidence": [item.strip() for item in evidence if item.strip()],
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    feature_dir.mkdir(parents=True, exist_ok=True)
    output = feature_dir / "sdd-handoff.json"
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return output
