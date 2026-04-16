from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.traceability import TraceabilityCheck

def _ws(tmp_path: Path, files: dict) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_when_fr_has_business_goal_and_test_case(tmp_path: Path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\n- **BG-001** Reduce claim cycle to 3 days.",
        "02-requirements-engineering/srs/3.2.md": "---\nphase: '02'\n---\n# FRs\n- **FR-001** trace: BG-001",
        "05-testing-documentation/test-plan/cases.md": "---\nphase: '05'\n---\n# Cases\n- **TC-001** verifies FR-001",
    })
    findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, findings)
    assert len(findings) == 0

def test_flags_orphan_fr(tmp_path: Path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\n- **BG-001** thing.",
        "02-requirements-engineering/srs/3.2.md": "---\nphase: '02'\n---\n# FRs\n- **FR-002** lonely.",
    })
    findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("FR-002" in m for m in msgs)
