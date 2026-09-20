"""Validate SRS need, reuse, adaptation and requirement-debt records."""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

STATUSES = {"no_change", "reuse", "adapt", "new_scope"}
EVIDENCE = {"verified", "not_assessed"}
ID_RE = re.compile(r"^RD-[A-Z0-9][A-Z0-9._-]{2,63}$")


def _list(value: Any, name: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"{name} must contain at least one non-empty string")
        return []
    return [item.strip() for item in value]


def validate_decision(record: Any) -> dict[str, Any]:
    errors: list[str] = []
    unassessed: list[str] = []
    if not isinstance(record, dict):
        return {"status": "FAIL", "errors": ["decision must be an object"], "unassessed": []}
    if record.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if not isinstance(record.get("decision_id"), str) or not ID_RE.fullmatch(record["decision_id"]):
        errors.append("decision_id must match RD-<stable identifier>")
    if not isinstance(record.get("problem"), str) or len(record["problem"].strip()) < 20:
        errors.append("problem must explain the requirement problem in at least 20 characters")
    status = record.get("status")
    if status not in STATUSES:
        errors.append("status must be no_change, reuse, adapt, or new_scope")
    source_refs = _list(record.get("source_refs"), "source_refs", errors)
    capability_refs = record.get("capability_refs", [])
    if status in {"reuse", "adapt"}:
        _list(capability_refs, "capability_refs", errors)
    elif not isinstance(capability_refs, list):
        errors.append("capability_refs must be a list")
    accepted = _list(record.get("accepted_scope"), "accepted_scope", errors)
    rejected = _list(record.get("rejected_alternatives"), "rejected_alternatives", errors)
    applicability = record.get("applicability")
    if not isinstance(applicability, dict) or not applicability.get("context") or not applicability.get("retained_constraints"):
        errors.append("applicability must name context and retained_constraints")
    authority = record.get("authority")
    if not isinstance(authority, dict) or not authority.get("owner"):
        errors.append("authority.owner is required")
    approval = authority.get("approval_status") if isinstance(authority, dict) else None
    if approval not in {"approved", "pending", "not_applicable"}:
        errors.append("authority.approval_status is invalid")
    if status == "new_scope" and approval != "approved":
        errors.append("new_scope requires an explicit approved authority status")
    evidence_status = record.get("evidence_status")
    if evidence_status not in EVIDENCE:
        errors.append("evidence_status must be verified or not_assessed")
    elif evidence_status == "not_assessed":
        unassessed.append("decision evidence")
    if not isinstance(record.get("review_trigger"), str) or not record["review_trigger"].strip():
        errors.append("review_trigger is required")
    expiry = record.get("expiry")
    if expiry is not None:
        try:
            if date.fromisoformat(expiry) < date.today():
                errors.append("expiry is in the past")
        except (TypeError, ValueError):
            errors.append("expiry must be an ISO date")
    if not source_refs and status == "no_change" and not record.get("no_change_reason"):
        errors.append("no_change requires no_change_reason when source_refs are absent")
    return {"status": "FAIL" if errors else ("NOT_ASSESSED" if unassessed else "PASS"), "errors": errors, "unassessed": unassessed}


def validate_debt(payload: Any) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(payload, dict) or not isinstance(payload.get("debt"), list):
        return {"status": "FAIL", "errors": ["debt must be a list"]}
    for index, item in enumerate(payload["debt"]):
        if not isinstance(item, dict):
            errors.append(f"debt[{index}] must be an object")
            continue
        for field in ("id", "owner", "reason", "trigger", "expiry", "affected_ids"):
            if not item.get(field):
                errors.append(f"debt[{index}] missing {field}")
        if item.get("expiry"):
            try:
                if date.fromisoformat(item["expiry"]) < date.today():
                    errors.append(f"debt[{index}] expiry is in the past")
            except ValueError:
                errors.append(f"debt[{index}] expiry is invalid")
        if not isinstance(item.get("affected_ids"), list) or not item["affected_ids"]:
            errors.append(f"debt[{index}] affected_ids must be non-empty")
    return {"status": "FAIL" if errors else "PASS", "errors": errors, "count": len(payload["debt"])}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
