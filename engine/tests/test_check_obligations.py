from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.obligations import ObligationsCheck


UGANDA_OBLIGATIONS = (
    Path(__file__).resolve().parents[2]
    / "domains"
    / "uganda"
    / "controls"
    / "obligations.yaml"
)


def _base_project(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    return tmp_path


def test_flags_missing_quality_standards_file(tmp_path: Path):
    project = _base_project(tmp_path)
    findings = FindingCollection()
    chk = ObligationsCheck("phase09.obligations", project, UGANDA_OBLIGATIONS)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    assert "phase09.obligations.missing_framework_coverage" in ids


def test_flags_in_scope_obligation_without_satisfying_control(tmp_path: Path):
    project = _base_project(tmp_path)
    (project / "_context/quality-standards.md").write_text(
        "# Quality Standards\n\nWe comply with Uganda DPPA 2019.\n",
        encoding="utf-8",
    )
    # No controls selected.
    (project / "_registry/controls.yaml").write_text(
        "selected: []\n", encoding="utf-8",
    )
    findings = FindingCollection()
    chk = ObligationsCheck("phase09.obligations", project, UGANDA_OBLIGATIONS)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    assert "phase09.obligations.unsatisfied" in ids
    msgs = [f.message for f in findings]
    assert any("CTRL-UG-001" in m for m in msgs)


def test_passes_when_selected_controls_cover_in_scope_obligations(tmp_path: Path):
    project = _base_project(tmp_path)
    (project / "_context/quality-standards.md").write_text(
        "# Quality Standards\n\nWe comply with Uganda DPPA 2019.\n",
        encoding="utf-8",
    )
    (project / "_registry/controls.yaml").write_text(
        "selected:\n"
        "  - id: CTRL-UG-001\n"
        "    applies_because: \"Collects PII\"\n"
        "  - id: CTRL-UG-002\n"
        "    applies_because: \"Stores S-tier fields\"\n"
        "  - id: CTRL-UG-003\n"
        "    applies_because: \"Incident response mandatory\"\n"
        "  - id: CTRL-UG-004\n"
        "    applies_because: \"DSAR handling needed\"\n",
        encoding="utf-8",
    )
    findings = FindingCollection()
    chk = ObligationsCheck("phase09.obligations", project, UGANDA_OBLIGATIONS)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    assert "phase09.obligations.unsatisfied" not in ids
    assert "phase09.obligations.missing_framework_coverage" not in ids


def test_skips_obligation_whose_framework_is_not_in_scope(tmp_path: Path):
    project = _base_project(tmp_path)
    (project / "_context/quality-standards.md").write_text(
        "# Quality Standards\n\nWe comply with ISO 27001 only.\n",
        encoding="utf-8",
    )
    (project / "_registry/controls.yaml").write_text(
        "selected: []\n", encoding="utf-8",
    )
    findings = FindingCollection()
    chk = ObligationsCheck("phase09.obligations", project, UGANDA_OBLIGATIONS)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    # Uganda DPPA 2019 framework is NOT in the quality-standards text, so none
    # of the obligations should fire.
    assert "phase09.obligations.unsatisfied" not in ids
