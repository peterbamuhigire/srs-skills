"""Sabotage-flag tests: a freshly seeded demo passes; sabotage fails."""
import importlib.util
from pathlib import Path

import pytest
from click.testing import CliRunner
from engine.cli import main

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def demo(tmp_path_factory: pytest.TempPathFactory) -> Path:
    path = ROOT / "scripts" / "seed_demo_project.py"
    spec = importlib.util.spec_from_file_location("seed_demo_project", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.DEMO = tmp_path_factory.mktemp("demo") / "_demo-hybrid-regulated"
    module.main()
    return module.DEMO


def test_clean_demo_passes(demo: Path):
    rc = CliRunner().invoke(main, ["validate", str(demo)])
    assert rc.exit_code == 0, rc.output


def test_sabotage_breaks_specific_gates(demo: Path):
    rc = CliRunner().invoke(main, ["validate", str(demo), "--break-something"])
    assert rc.exit_code != 0
    out = rc.output
    assert "kernel.no_unresolved_fail_markers" in out
    assert "phase02.smart_nfr" in out
    assert "phase09.traceability" in out
