import sys
from pathlib import Path
import pytest
from click.testing import CliRunner
from engine.cli import main


@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Clearing PATH does not always hide pandoc on Windows (PATHEXT + cwd).",
)
def test_doctor_reports_pandoc_missing(monkeypatch, tmp_path: Path):
    monkeypatch.setenv("PATH", "")  # hide every binary
    rc = CliRunner().invoke(main, ["doctor"])
    assert rc.exit_code != 0
    assert "pandoc" in rc.output.lower()
    assert "install" in rc.output.lower() or "fix:" in rc.output.lower()


def test_doctor_reports_fake_pandoc_missing(monkeypatch):
    import engine.doctor as doc
    monkeypatch.setattr(doc, "_check_pandoc", lambda: (False, "pandoc not on PATH"))
    # Rebuild CHECKS so it picks up the patched function
    original = doc.CHECKS
    patched = [
        doc.Check(c.name, doc._check_pandoc if c.name == "Pandoc available" else c.fn, c.fix_hint)
        for c in original
    ]
    monkeypatch.setattr(doc, "CHECKS", patched)
    rc = CliRunner().invoke(main, ["doctor"])
    assert rc.exit_code != 0
    assert "pandoc" in rc.output.lower()


def test_doctor_passes_in_healthy_env():
    rc = CliRunner().invoke(main, ["doctor"])
    # Will pass if developer ran setup; only assertion: human-readable section headings.
    assert "Python" in rc.output
    assert "Pandoc" in rc.output
