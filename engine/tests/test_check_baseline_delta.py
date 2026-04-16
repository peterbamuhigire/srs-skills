from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.baseline_delta import BaselineDeltaCheck


def _base(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    return tmp_path


def _run(project: Path) -> FindingCollection:
    findings = FindingCollection()
    graph = ArtifactGraph.build(Workspace.load(project))
    BaselineDeltaCheck("phase09.baseline_delta", project).run(graph, findings)
    return findings


def test_silent_skip_when_no_baselines_file(tmp_path: Path):
    project = _base(tmp_path)
    findings = _run(project)
    assert list(findings) == []


def test_silent_skip_when_no_current_key(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/baselines.yaml").write_text(
        "baselines:\n  - label: v1.0\n", encoding="utf-8"
    )
    findings = _run(project)
    assert list(findings) == []


def test_flags_missing_current_snapshot(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/baselines.yaml").write_text(
        "current: v1.0\n", encoding="utf-8"
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.baseline_delta.current_missing" in ids
