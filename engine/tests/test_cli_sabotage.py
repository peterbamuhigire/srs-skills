"""Sabotage-flag tests: the clean demo passes; --break-something fails."""
from click.testing import CliRunner
from engine.cli import main

DEMO = "projects/_demo-hybrid-regulated"


def test_clean_demo_passes():
    rc = CliRunner().invoke(main, ["validate", DEMO])
    assert rc.exit_code == 0, rc.output


def test_sabotage_breaks_specific_gates():
    rc = CliRunner().invoke(main, ["validate", DEMO, "--break-something"])
    assert rc.exit_code != 0
    out = rc.output
    assert "kernel.no_unresolved_fail_markers" in out
    assert "phase02.smart_nfr" in out
    assert "phase09.traceability" in out
