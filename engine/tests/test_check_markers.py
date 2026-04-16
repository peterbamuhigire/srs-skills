from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection, Severity
from engine.checks.markers import NoUnresolvedFailMarkersGate

def _graph(tmp_path: Path, files: dict[str, str]) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_clean_project_has_no_findings(tmp_path: Path):
    graph = _graph(tmp_path, {"_context/vision.md": "# Vision\nClean."})
    findings = FindingCollection()
    NoUnresolvedFailMarkersGate().evaluate(graph, findings)
    assert len(findings) == 0

def test_finds_v_v_fail_marker(tmp_path: Path):
    graph = _graph(tmp_path, {
        "_context/vision.md": "# Vision\n[V&V-FAIL: missing oracle for FR-001]",
    })
    findings = FindingCollection()
    NoUnresolvedFailMarkersGate().evaluate(graph, findings)
    items = findings.for_gate("kernel.no_unresolved_fail_markers")
    assert len(items) == 1
    assert items[0].severity == Severity.HIGH
    assert "FR-001" in items[0].message
