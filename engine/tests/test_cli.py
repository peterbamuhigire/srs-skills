from pathlib import Path
from click.testing import CliRunner
from engine.cli import main

def test_validate_passes_clean_project(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\nClean.\n")
    result = CliRunner().invoke(main, ["validate", str(tmp_path)])
    assert result.exit_code == 0, result.output
    assert "ENGINE CONTRACT: PASS" in result.output

def test_validate_fails_on_unresolved_marker(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\n[V&V-FAIL: missing oracle]\n"
    )
    result = CliRunner().invoke(main, ["validate", str(tmp_path)])
    assert result.exit_code == 1
    assert "kernel.no_unresolved_fail_markers" in result.output

def test_validate_emits_junit_when_requested(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\nClean.\n")
    out_path = tmp_path / "report.xml"
    result = CliRunner().invoke(
        main, ["validate", str(tmp_path), "--junit", str(out_path)]
    )
    assert result.exit_code == 0
    assert out_path.exists()
    assert out_path.read_text().startswith("<testsuite")
