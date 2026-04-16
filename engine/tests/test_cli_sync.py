from pathlib import Path
from click.testing import CliRunner
from engine.cli import main
from engine.registry.identifiers import IdentifierRegistry


def test_sync_extracts_ids_from_artifacts(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\n- **BG-001** Cycle <= 3 days", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** trace BG-001", encoding="utf-8"
    )
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 0, rc.output
    reg = IdentifierRegistry.load(tmp_path / "_registry" / "identifiers.yaml")
    ids = {e.id for e in reg}
    assert "FR-001" in ids
    assert "BG-001" in ids


def test_sync_aborts_on_collision(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/a.md").write_text(
        "- **FR-001** in a", encoding="utf-8"
    )
    (tmp_path / "_context/b.md").write_text(
        "- **FR-001** in b", encoding="utf-8"
    )
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 1
    assert "FR-001" in rc.output
