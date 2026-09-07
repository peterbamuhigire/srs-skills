"""Validation for behavioural fixture evidence declarations."""
from __future__ import annotations

REQUIRED_EVIDENCE = {"decision_id", "decision", "evidence_paths", "review_status"}


def validate_fixture_manifest(data: object) -> list[str]:
    if not isinstance(data, dict):
        return ["fixture manifest must be an object"]
    evidence = data.get("evidence")
    if not isinstance(evidence, dict):
        return ["fixture manifest evidence must be an object"]
    errors = [f"evidence missing fields: {sorted(REQUIRED_EVIDENCE - evidence.keys())}"] if REQUIRED_EVIDENCE - evidence.keys() else []
    for field in ("decision_id", "decision", "review_status"):
        if not isinstance(evidence.get(field), str) or not evidence[field].strip():
            errors.append(f"evidence.{field} must be non-empty text")
    if not isinstance(evidence.get("evidence_paths"), list) or not evidence["evidence_paths"] or not all(isinstance(item, str) and item.strip() for item in evidence["evidence_paths"]):
        errors.append("evidence.evidence_paths must be a non-empty list of text paths")
    return errors
