from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase01 import Phase01Gate

def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_with_full_canonical_inputs(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nReduce claim cycle.",
        "_context/stakeholders.md": "# Stakeholders\n- Provider Office.",
        "_context/features.md": "# Features\n- F-1 Submit Claim — driven by Provider Office",
        "_context/glossary.md": "# Glossary\n- **Claim:** a request for payment.",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    assert len(findings) == 0

def test_flags_missing_stakeholders_file(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nx",
        "_context/features.md": "# Features\n- F-1",
        "_context/glossary.md": "# Glossary\n- **x:** y",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings]
    assert any("stakeholders.md" in m for m in msgs)

def test_flags_orphan_feature(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision\nx",
        "_context/stakeholders.md": "# Stakeholders\n- Provider Office",
        "_context/features.md": "# Features\n- F-1 Mystery — driven by no-one",
        "_context/glossary.md": "# Glossary\n- **x:** y",
    })
    findings = FindingCollection()
    Phase01Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings]
    assert any("F-1" in m for m in msgs)
