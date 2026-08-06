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
