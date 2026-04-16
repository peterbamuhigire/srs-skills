from datetime import date, timedelta
from pathlib import Path
from click.testing import CliRunner
from ruamel.yaml import YAML
from engine.cli import main


def _mkproject(tmp_path: Path) -> Path:
    project = tmp_path / "proj"
    (project / "_context").mkdir(parents=True)
    (project / "_context/vision.md").write_text("# V\n", encoding="utf-8")
    return project


def test_waive_creates_waiver_entry(tmp_path: Path):
    project = _mkproject(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, [
        "waive", str(project),
        "--gate", "phase02.smart_nfr",
        "--reason", "deferred",
        "--approver", "Tech Lead",
        "--days", "30",
    ])
    assert result.exit_code == 0, result.output
    wpath = project / "_registry" / "waivers.yaml"
    assert wpath.exists()
    yaml = YAML(typ="safe")
    data = yaml.load(wpath.read_text(encoding="utf-8"))
    waivers = data["waivers"]
    assert len(waivers) == 1
    w = waivers[0]
    assert w["id"] == "WAIVE-001"
    assert w["gate"] == "phase02.smart_nfr"
    assert w["approver"] == "Tech Lead"
    assert w["approved_on"] == date.today().isoformat()
    assert w["expires_on"] == (date.today() + timedelta(days=30)).isoformat()


def test_waive_rejects_days_gt_90(tmp_path: Path):
    project = _mkproject(tmp_path)
    runner = CliRunner()
    result = runner.invoke(main, [
        "waive", str(project),
        "--gate", "phase02.smart_nfr",
        "--reason", "deferred",
        "--approver", "Tech Lead",
        "--days", "120",
    ])
    assert result.exit_code == 1


def test_signoff_creates_ledger_entry(tmp_path: Path):
    project = _mkproject(tmp_path)
    art = project / "02-requirements-engineering" / "srs.md"
    art.parent.mkdir(parents=True)
    art.write_text("# SRS\n", encoding="utf-8")
    runner = CliRunner()
    result = runner.invoke(main, [
        "signoff", str(project),
        "--gate", "phase02",
        "--signer", "Jane",
        "--role", "Chief Architect",
        "--artifact", "02-requirements-engineering/srs.md",
    ])
    assert result.exit_code == 0, result.output
    lpath = project / "_registry" / "sign-off-ledger.yaml"
    assert lpath.exists()
    yaml = YAML(typ="safe")
    data = yaml.load(lpath.read_text(encoding="utf-8"))
    assert data["sign_offs"][0]["gate"] == "phase02"
    assert data["sign_offs"][0]["artifact_set"] == [
        "02-requirements-engineering/srs.md"
    ]


def test_pack_cli_writes_zip(tmp_path: Path):
    project = _mkproject(tmp_path)
    out = tmp_path / "pack.zip"
    runner = CliRunner()
    result = runner.invoke(main, [
        "pack", str(project), "--out", str(out),
    ])
    assert result.exit_code == 0, result.output
    assert out.exists() and out.stat().st_size > 0


def test_baseline_snapshot_cli(tmp_path: Path):
    project = _mkproject(tmp_path)
    (project / "02-requirements").mkdir()
    (project / "02-requirements/fr.md").write_text(
        "# FR\n\n- **FR-0101** The system shall do X.\n", encoding="utf-8"
    )
    runner = CliRunner()
    result = runner.invoke(main, [
        "baseline", "snapshot", str(project), "--label", "v1.0",
    ])
    assert result.exit_code == 0, result.output
    snap = project / "09-governance-compliance" / "07-baseline-delta" / "v1.0.yaml"
    assert snap.exists()
