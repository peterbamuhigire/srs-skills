import json

import pytest

from engine.sdd_handoff import write_handoff


def test_write_handoff_is_resumable(tmp_path):
    output = write_handoff(tmp_path / "feature", stage="implement-qc", status="blocked",
                           owner="release-captain", next_step="Resolve failing integration test",
                           blockers=["API contract mismatch"], risks=["Migration timing"],
                           evidence=["qc-report.md"])
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["schema_version"] == 1
    assert payload["status"] == "blocked"
    assert payload["blockers"] == ["API contract mismatch"]


def test_complete_handoff_rejects_blockers(tmp_path):
    with pytest.raises(ValueError, match="cannot contain blockers"):
        write_handoff(tmp_path / "feature", stage="all", status="complete",
                      owner="release-captain", next_step="Close", blockers=["still blocked"])


def test_complete_handoff_requires_verified_evidence(tmp_path):
    with pytest.raises(ValueError, match="verified evidence_status"):
        write_handoff(tmp_path / "feature", stage="all", status="complete",
                      owner="release-captain", next_step="Close")


def test_handoff_carries_requirement_and_invariant_context(tmp_path):
    output = write_handoff(
        tmp_path / "feature", stage="implement-qc", status="blocked",
        owner="release-captain", next_step="Resolve security decision",
        requirement_baseline={"hash": "abc", "version": "r3"},
        decision_ids=["SD-001"], invariants=["tenant isolation"],
        fit_criteria=["negative permission test"], evidence_status="not_assessed",
    )
    payload = json.loads(output.read_text(encoding="utf-8"))
    assert payload["handoff_contract_version"] == 2
    assert payload["requirement_baseline"]["version"] == "r3"
    assert payload["invariants"] == ["tenant isolation"]


def test_handoff_rejects_path_escape(tmp_path):
    with pytest.raises(ValueError, match="repository-relative"):
        write_handoff(tmp_path / "feature", stage="all", status="blocked",
                      owner="release-captain", next_step="Investigate", evidence=["../secret"])
