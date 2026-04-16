from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.stimulus_response import StimulusResponseCheck


def _ws(tmp_path, body):
    (tmp_path / "_context").mkdir()
    (tmp_path / "02/srs.md").parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / "02/srs.md").write_text(body)
    return ArtifactGraph.build(Workspace.load(tmp_path))


def test_passes_when_fr_uses_shall_with_action(tmp_path):
    graph = _ws(tmp_path, "---\nphase: '02'\n---\n- **FR-001** When a provider submits a claim, the system shall persist it within 2 seconds.")
    findings = FindingCollection()
    StimulusResponseCheck("phase02.stimulus_response").run(graph, findings)
    assert len(findings) == 0


def test_flags_fr_without_shall(tmp_path):
    graph = _ws(tmp_path, "---\nphase: '02'\n---\n- **FR-002** The system can submit claims.")
    findings = FindingCollection()
    StimulusResponseCheck("phase02.stimulus_response").run(graph, findings)
    assert len(list(findings)) == 1
