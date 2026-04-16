from datetime import date
from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.baseline import snapshot, save_snapshot, load_snapshot, diff


def _ws(tmp_path: Path, body: str) -> Path:
    (tmp_path / "_context").mkdir(parents=True)
    (tmp_path / "_context/vision.md").write_text("# V\n", encoding="utf-8")
    (tmp_path / "02-requirements").mkdir()
    (tmp_path / "02-requirements/fr.md").write_text(body, encoding="utf-8")
    return tmp_path


def test_snapshot_and_diff_round_trip(tmp_path: Path):
    project_a = _ws(
        tmp_path / "a",
        "# FR\n\n- **FR-0101** The system shall do X.\n- **FR-0102** Y.\n",
    )
    project_b = _ws(
        tmp_path / "b",
        "# FR\n\n- **FR-0101** The system shall do X CHANGED.\n- **FR-0103** Z.\n",
    )
    graph_a = ArtifactGraph.build(Workspace.load(project_a))
    graph_b = ArtifactGraph.build(Workspace.load(project_b))
    snap_a = snapshot(graph_a, "v1.0", today=date(2026, 4, 16))
    snap_b = snapshot(graph_b, "v1.1", today=date(2026, 4, 17))

    path_a = tmp_path / "a.yaml"
    save_snapshot(snap_a, path_a)
    loaded = load_snapshot(path_a)
    assert loaded.label == "v1.0"
    assert loaded.entries == snap_a.entries
    assert loaded.created_on == date(2026, 4, 16)

    d = diff(snap_a, snap_b)
    assert "FR-0103" in d["added"]
    assert "FR-0102" in d["removed"]
    assert "FR-0101" in d["modified"]
