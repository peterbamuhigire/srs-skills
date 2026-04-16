from pathlib import Path
import pytest
from engine.findings import Finding, Severity, FindingCollection

def test_finding_is_immutable():
    f = Finding(
        gate_id="phase01.context_complete",
        severity=Severity.HIGH,
        message="vision.md missing required section",
        location=Path("_context/vision.md"),
        line=12,
    )
    with pytest.raises(Exception):
        f.message = "changed"  # frozen dataclass

def test_collection_blocks_when_high_severity_present():
    coll = FindingCollection()
    coll.add(Finding("g1", Severity.LOW, "ok-ish", None, None))
    assert coll.is_blocking is False
    coll.add(Finding("g2", Severity.HIGH, "broken", None, None))
    assert coll.is_blocking is True

def test_collection_filters_by_gate():
    coll = FindingCollection()
    coll.add(Finding("phase01.x", Severity.HIGH, "a", None, None))
    coll.add(Finding("phase02.y", Severity.HIGH, "b", None, None))
    assert len(coll.for_gate("phase01.x")) == 1
