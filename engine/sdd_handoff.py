"""Write a resumable SDD stop or release handoff record."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Mapping

STAGES = {"spec-plan", "plan-tasks", "tasks-implement", "implement-qc", "all"}
STATUSES = {"in_progress", "blocked", "complete"}


def write_handoff(feature_dir: Path, *, stage: str, status: str, owner: str,
                  next_step: str, blockers: Iterable[str] = (),
                  risks: Iterable[str] = (), evidence: Iterable[str] = (),
                  requirement_baseline: Mapping[str, str] | None = None,
                  decision_ids: Iterable[str] = (), invariants: Iterable[str] = (),
                  fit_criteria: Iterable[str] = (), evidence_status: str = "not_assessed",
                  waiver: Mapping[str, str] | None = None) -> Path:
    if stage not in STAGES:
        raise ValueError(f"unsupported stage: {stage}")
    if status not in STATUSES:
        raise ValueError(f"unsupported status: {status}")
    if not owner.strip() or not next_step.strip():
        raise ValueError("owner and next_step are required")
    if evidence_status not in {"verified", "not_assessed"}:
        raise ValueError("evidence_status must be verified or not_assessed")
    blockers = [item.strip() for item in blockers if item.strip()]
    if status == "complete" and blockers:
        raise ValueError("complete handoff cannot contain blockers")
    if status == "complete" and evidence_status != "verified":
        raise ValueError("complete handoff requires verified evidence_status")
    def clean_refs(values: Iterable[str]) -> list[str]:
        result = []
        for item in values:
            item = item.strip()
            if item and (".." in Path(item).parts or Path(item).is_absolute()):
                raise ValueError("handoff references must be repository-relative")
            if item:
                result.append(item)
        return result
    payload = {
        "schema_version": 1,
        "handoff_contract_version": 2,
        "feature": feature_dir.name,
        "stage": stage,
        "status": status,
        "owner": owner.strip(),
        "next_step": next_step.strip(),
        "blockers": blockers,
        "risks": [item.strip() for item in risks if item.strip()],
        "evidence": clean_refs(evidence),
        "evidence_status": evidence_status,
        "requirement_baseline": dict(requirement_baseline or {}),
        "decision_ids": clean_refs(decision_ids),
        "invariants": [item.strip() for item in invariants if item.strip()],
        "fit_criteria": [item.strip() for item in fit_criteria if item.strip()],
        "waiver": dict(waiver) if waiver else None,
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }
    feature_dir.mkdir(parents=True, exist_ok=True)
    output = feature_dir / "sdd-handoff.json"
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return output
