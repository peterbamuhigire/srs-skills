from datetime import date
from pathlib import Path
import pytest
from engine.findings import Finding, FindingCollection, Severity
from engine.waivers import WaiverRegister, WaiverError

def test_loads_waivers_from_yaml(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    assert len(reg) == 1
    w = next(iter(reg))
    assert w.id == "WAIVE-001"
    assert w.gate == "kernel.no_unresolved_fail_markers"
    assert w.expires_on == date(2026, 5, 15)

def test_returns_empty_when_file_missing(tmp_path: Path):
    reg = WaiverRegister.load(tmp_path / "missing.yaml")
    assert len(reg) == 0

def test_matches_finding_within_scope(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    finding = Finding(
        gate_id="kernel.no_unresolved_fail_markers",
        severity=Severity.HIGH,
        message="x",
        location=Path("_context/vision.md"),
        line=4,
    )
    assert reg.matches(finding, today=date(2026, 4, 16)) is not None

def test_does_not_match_after_expiry(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    finding = Finding(
        gate_id="kernel.no_unresolved_fail_markers",
        severity=Severity.HIGH,
        message="x",
        location=Path("_context/vision.md"),
        line=4,
    )
    assert reg.matches(finding, today=date(2026, 6, 1)) is None

def test_apply_strips_waived_findings(tiny_project: Path):
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    findings = FindingCollection()
    findings.add(Finding(
        "kernel.no_unresolved_fail_markers", Severity.HIGH, "m",
        Path("_context/vision.md"), 4))
    findings.add(Finding(
        "kernel.no_unresolved_fail_markers", Severity.HIGH, "m",
        Path("_context/glossary.md"), 7))
    waived, remaining = reg.apply(findings, today=date(2026, 4, 16))
    assert len(waived) == 1
    assert len(remaining) == 1
    assert remaining[0].location.name == "glossary.md"
