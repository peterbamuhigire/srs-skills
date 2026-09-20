from engine.requirements_decision import validate_decision, validate_debt


def _record(status="reuse", evidence="verified"):
    return {
        "schema_version": 1,
        "decision_id": "RD-REUSE-001",
        "problem": "A proposed requirement duplicates an approved capability but its applicability is unclear.",
        "status": status,
        "source_refs": ["REQ-BASELINE-1"],
        "capability_refs": ["existing.capability"],
        "accepted_scope": ["Retain the approved identifier and adapt only the tenant rule."],
        "rejected_alternatives": ["Create a parallel requirement without lineage."],
        "applicability": {"context": "tenant portal", "retained_constraints": "permission and audit"},
        "authority": {"owner": "requirements-lead", "approval_status": "approved"},
        "evidence_status": evidence,
        "review_trigger": "Source or tenant rule changes",
    }


def test_reuse_decision_passes():
    assert validate_decision(_record())["status"] == "PASS"


def test_new_scope_without_approval_fails():
    record = _record(status="new_scope")
    record["authority"]["approval_status"] = "pending"
    assert validate_decision(record)["status"] == "FAIL"


def test_unassessed_decision_is_explicit():
    assert validate_decision(_record(evidence="not_assessed"))["status"] == "NOT_ASSESSED"


def test_debt_ledger_requires_owner_trigger_and_scope():
    result = validate_debt({"debt": [{"id": "D-1", "owner": "team", "reason": "temporary", "trigger": "new policy", "expiry": "2099-01-01", "affected_ids": ["FR-001"]}]})
    assert result["status"] == "PASS"
    broken = validate_debt({"debt": [{"id": "D-1"}]})
    assert broken["status"] == "FAIL"
