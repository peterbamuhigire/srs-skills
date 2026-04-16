from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase03 import Phase03Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- architecture_decisions_recorded ----------------------------------------

def test_passes_when_project_has_adr_directory(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001-choose-framework.md": (
            "# Decision\nWe chose X."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded") == []


def test_passes_when_project_has_adr_identifier(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nSee **ADR-001** for rationale."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded") == []


def test_flags_missing_adr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nNo decisions recorded."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded"), (
        "expected an architecture_decisions_recorded finding "
        "when no ADR directory or ADR-### identifier exists"
    )
