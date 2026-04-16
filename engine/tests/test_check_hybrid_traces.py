from pathlib import Path
from engine.findings import FindingCollection
from engine.checks.hybrid_traces import HybridTracesCheck


def _trace(tmp_path: Path, body: str) -> Path:
    p = tmp_path / "baseline-trace.yaml"
    p.write_text(body, encoding="utf-8")
    return p


def test_passes_when_every_story_traces_to_baseline(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: Steering Committee
stories:
  - id: US-001
    traces: [FR-001]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    assert len(findings) == 0


def test_flags_orphan_baseline_item(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: Steering Committee
  - id: FR-002
    locked_on: 2026-04-01
    change_control_body: Steering Committee
stories:
  - id: US-001
    traces: [FR-001]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    msgs = [f.message for f in findings]
    assert any("FR-002" in m for m in msgs)


def test_flags_unknown_trace_target(tmp_path: Path):
    p = _trace(tmp_path, """\
baseline:
  - id: FR-001
    locked_on: 2026-04-01
    change_control_body: SC
stories:
  - id: US-001
    traces: [FR-999]
""")
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    msgs = [f.message for f in findings]
    assert any("FR-999" in m for m in msgs)


def test_flags_missing_trace_file(tmp_path: Path):
    p = tmp_path / "missing.yaml"  # does not exist
    findings = FindingCollection()
    HybridTracesCheck("phasehybrid.traces", p).run(None, findings)
    msgs = [f.message for f in findings]
    assert any("missing" in m.lower() for m in msgs)
