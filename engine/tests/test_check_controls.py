from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.controls import ControlsCheck


UGANDA_REGISTER = (
    Path(__file__).resolve().parents[2]
    / "domains"
    / "uganda"
    / "controls"
    / "control-register.yaml"
)


def _base_project(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    return tmp_path


def test_flags_missing_evidence_for_selected_control(tmp_path: Path):
    project = _base_project(tmp_path)
    (project / "_registry/controls.yaml").write_text(
        "selected:\n"
        "  - id: CTRL-UG-002\n"
        "    applies_because: \"App stores patient NIN numbers\"\n",
        encoding="utf-8",
    )
    findings = FindingCollection()
    chk = ControlsCheck("phase09.controls", project, UGANDA_REGISTER)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    msgs = [f.message for f in findings]
    assert any("CTRL-UG-002" in m for m in msgs)


def test_flags_selection_without_registry_file(tmp_path: Path):
    project = _base_project(tmp_path)
    # No _registry/controls.yaml is written.
    findings = FindingCollection()
    chk = ControlsCheck("phase09.controls", project, UGANDA_REGISTER)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    assert "phase09.controls.no_selection" in ids


def test_flags_unknown_control_id_in_selection(tmp_path: Path):
    project = _base_project(tmp_path)
    (project / "_registry/controls.yaml").write_text(
        "selected:\n"
        "  - id: CTRL-UG-999\n"
        "    applies_because: \"Fake control for test\"\n",
        encoding="utf-8",
    )
    findings = FindingCollection()
    chk = ControlsCheck("phase09.controls", project, UGANDA_REGISTER)
    chk.run(ArtifactGraph.build(Workspace.load(project)), findings)
    ids = [f.gate_id for f in findings]
    assert "phase09.controls.unknown_control" in ids
    msgs = [f.message for f in findings]
    assert any("CTRL-UG-999" in m for m in msgs)
