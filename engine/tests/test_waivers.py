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

def test_waiver_only_applies_during_approved_interval(tiny_project: Path):
    from datetime import timedelta
    reg = WaiverRegister.load(tiny_project / "_registry" / "waivers.yaml")
    waiver = next(iter(reg))
    finding = Finding("kernel.no_unresolved_fail_markers", Severity.HIGH,
                      "x", Path("_context/vision.md"), 4)
    assert reg.matches(finding, waiver.approved_on - timedelta(days=1)) is None
    assert reg.matches(finding, waiver.approved_on) is not None
    assert reg.matches(finding, waiver.expires_on) is not None
    assert reg.matches(finding, waiver.expires_on + timedelta(days=1)) is None


def test_waiver_outside_approved_duration_cannot_suppress_findings(tmp_path: Path):
    path = tmp_path / "waivers.yaml"
    path.write_text(
        "waivers:\n"
        "  - id: W-LONG\n"
        "    gate: kernel.no_unresolved_fail_markers\n"
        "    scope: '*'\n"
        "    reason: invalid duration must not suppress findings\n"
        "    approver: owner\n"
        "    approved_on: 2026-01-01\n"
        "    expires_on: 2026-06-01\n",
        encoding="utf-8",
    )
    reg = WaiverRegister.load(path)
    finding = Finding(
        "kernel.no_unresolved_fail_markers",
        Severity.HIGH,
        "x",
        Path("_context/vision.md"),
        4,
    )

    assert reg.matches(finding, today=date(2026, 4, 1)) is None

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


def _write_register(tmp_path: Path, content: str) -> Path:
    path = tmp_path / "waivers.yaml"
    path.write_text(content, encoding="utf-8")
    return path


@pytest.mark.parametrize(
    "content",
    [
        "waivers: [\n",
        "- not-a-mapping\n",
        "[]\n",
        "0\n",
        "''\n",
        "waivers: {}\n",
        "waivers:\n  - not-a-mapping\n",
        (
            "waivers:\n  - id: W-1\n    gate: gate.one\n    reason: ''\n"
            "    approver: owner\n    approved_on: 2026-04-01\n"
            "    expires_on: 2026-05-01\n"
        ),
        (
            "waivers:\n  - id: W-1\n    gate: gate.one\n    reason: test\n"
            "    approver: owner\n    approved_on: true\n"
            "    expires_on: 2026-05-01\n"
        ),
    ],
)
def test_rejects_malformed_register_shapes_and_types(tmp_path: Path, content: str):
    with pytest.raises(WaiverError):
        WaiverRegister.load(_write_register(tmp_path, content))


@pytest.mark.parametrize(
    "scope", ["../outside.md", "/absolute.md", "C:/outside.md", "docs\\file.md"]
)
def test_rejects_scope_outside_project_workspace(tmp_path: Path, scope: str):
    content = (
        "waivers:\n  - id: W-1\n    gate: gate.one\n"
        f"    scope: {scope!r}\n    reason: test\n    approver: owner\n"
        "    approved_on: 2026-04-01\n    expires_on: 2026-05-01\n"
    )
    with pytest.raises(WaiverError, match="scope"):
        WaiverRegister.load(_write_register(tmp_path, content))


def test_rejects_duplicate_waiver_ids(tmp_path: Path):
    item = (
        "  - id: W-1\n    gate: gate.one\n    scope: '*'\n"
        "    reason: test\n    approver: owner\n"
        "    approved_on: 2026-04-01\n    expires_on: 2026-05-01\n"
    )
    with pytest.raises(WaiverError, match="Duplicate waiver id"):
        WaiverRegister.load(_write_register(tmp_path, "waivers:\n" + item + item))
