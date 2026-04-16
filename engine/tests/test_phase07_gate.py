from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase07 import Phase07Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- dor_references_baseline ------------------------------------------------

def test_passes_when_dor_references_baseline_id(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# Definition of Ready\n"
            "- Story is linked to **BG-001** and **FR-0102** in the backlog.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.dor_references_baseline") == []


def test_flags_missing_dor(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-plan.md": "# Sprint Plan",
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.dor_references_baseline"]
    assert msgs, "expected a dor_references_baseline finding"
    assert "No Definition of Ready document found" in msgs[0]


def test_flags_dor_without_baseline_reference(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# Definition of Ready\n"
            "- Story has acceptance criteria and is estimated.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.dor_references_baseline"]
    assert msgs, "expected a dor_references_baseline finding"
    assert "does not reference any baseline ID" in msgs[0]
