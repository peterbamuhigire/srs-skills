from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.change_impact import ChangeImpactCheck


def _base(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    return tmp_path


def _run(project: Path) -> FindingCollection:
    findings = FindingCollection()
    graph = ArtifactGraph.build(Workspace.load(project))
    ChangeImpactCheck("phase09.change_impact", project).run(graph, findings)
    return findings


def test_happy_path(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/change-impact.yaml").write_text(
        "entries:\n"
        "  - id: CIA-001\n"
        "    raised_on: 2026-04-16\n"
        "    affected_baseline_ids: [\"FR-0101\"]\n"
        "    decision: approved\n"
        "    rollback_plan: \"Revert FR-0101 to prior baseline hash.\"\n",
        encoding="utf-8",
    )
    findings = _run(project)
    assert list(findings) == []


def test_flags_missing_rollback(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/change-impact.yaml").write_text(
        "entries:\n"
        "  - id: CIA-002\n"
        "    raised_on: 2026-04-16\n"
        "    affected_baseline_ids: [\"FR-0202\"]\n"
        "    decision: approved\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.change_impact.missing_rollback_plan" in ids


def test_flags_schema_violation(tmp_path: Path):
    project = _base(tmp_path)
    # decision is not in enum.
    (project / "_registry/change-impact.yaml").write_text(
        "entries:\n"
        "  - id: CIA-003\n"
        "    raised_on: 2026-04-16\n"
        "    affected_baseline_ids: [\"FR-0303\"]\n"
        "    decision: maybe\n"
        "    rollback_plan: \"x\"\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.change_impact.schema_violation" in ids
