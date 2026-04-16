import csv
import io
import zipfile
from pathlib import Path
from engine.pack import build_evidence_pack


def test_pack_contains_required_files(tmp_path: Path):
    project = tmp_path / "proj"
    (project / "_context").mkdir(parents=True)
    (project / "_context/vision.md").write_text("# V\n", encoding="utf-8")
    (project / "_registry").mkdir()
    (project / "_registry/identifiers.yaml").write_text(
        "identifiers: []\n", encoding="utf-8"
    )
    (project / "09-governance-compliance").mkdir()
    (project / "09-governance-compliance/audit-report.md").write_text(
        "# Audit\n", encoding="utf-8"
    )

    out = tmp_path / "pack.zip"
    build_evidence_pack(project, out)
    assert out.stat().st_size > 0
    with zipfile.ZipFile(out) as z:
        names = set(z.namelist())
        assert "manifest.csv" in names
        assert any(n.startswith("_context/") for n in names)
        assert any(n.startswith("_registry/") for n in names)
        assert any(n.startswith("09-governance-compliance/") for n in names)
        manifest_text = z.read("manifest.csv").decode("utf-8")
    reader = csv.DictReader(io.StringIO(manifest_text))
    rows = list(reader)
    assert any(r["path"] == "_context/vision.md" for r in rows)
    for r in rows:
        assert len(r["sha256"]) == 64


def test_pack_handles_missing_directories(tmp_path: Path):
    project = tmp_path / "sparse"
    (project / "_context").mkdir(parents=True)
    (project / "_context/vision.md").write_text("# V\n", encoding="utf-8")

    out = tmp_path / "pack.zip"
    build_evidence_pack(project, out)
    assert out.stat().st_size > 0
    with zipfile.ZipFile(out) as z:
        names = set(z.namelist())
        assert "manifest.csv" in names
