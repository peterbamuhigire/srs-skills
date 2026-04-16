from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase09 import Phase09Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- traceability ----------------------------------------------------------

def test_passes_when_trace_chain_complete(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "01-strategic-vision/goals.md": "# Goals\n\n- **BG-001** Mission.\n",
        "04-functional-requirements/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-0101** traces to BG-001 and TC-0101.\n"
        ),
        "05-testing-documentation/tc.md": (
            "# TC\n"
            "\n"
            "- **TC-0101** covers FR-0101.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.traceability") == []


def test_flags_orphan_fr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-functional-requirements/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-0101** has no upstream or downstream links.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    trace_findings = findings.for_gate("phase09.traceability")
    assert trace_findings, "expected traceability findings"
    for f in trace_findings:
        assert f.gate_id == "phase09.traceability"
        assert "ISO/IEC 27001:2022" in f.message
