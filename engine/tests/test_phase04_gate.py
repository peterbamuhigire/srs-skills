from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase04 import Phase04Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- coding_standards_referenced --------------------------------------------

def test_passes_when_coding_standards_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/coding-standards.md": (
            "# Coding Standards\nUse 4-space indentation."
        ),
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    assert findings.for_gate("phase04.coding_standards_referenced") == []


def test_flags_missing_coding_standards(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/README.md": "# Development",
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase04.coding_standards_referenced"]
    assert msgs, "expected a coding_standards_referenced finding"
    assert "coding-standards.md" in msgs[0]
