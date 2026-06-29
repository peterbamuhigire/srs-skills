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


def test_sync_dedupes_repeated_ids_without_collision(tmp_path: Path):
    # The same id appearing (even bold) in multiple artifacts is deduped to one
    # registry entry, NOT treated as a collision — projects legitimately bold
    # the same id in traceability matrices, DoD/DoR, risk registers, etc.
    # first occurrence (build order) wins for defined_in.
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "02").mkdir()
    (tmp_path / "02/a-spec.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** submit claim", encoding="utf-8"
    )
    (tmp_path / "02/b-traceability.md").write_text(
        "---\nphase: '02'\n---\n| **FR-001** | TC-001 |", encoding="utf-8"
    )
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 0, rc.output
    reg = IdentifierRegistry.load(tmp_path / "_registry" / "identifiers.yaml")
    assert [e.id for e in reg].count("FR-001") == 1
    assert reg["FR-001"].defined_in.endswith("a-spec.md")


def test_sync_dedupes_unbolded_module_ids(tmp_path: Path):
    # Module-prefixed, unbolded ids appearing across many artifacts are
    # references, not collisions: deduped to one registry entry each.
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "02").mkdir()
    (tmp_path / "02/a.md").write_text(
        "---\nphase: '02'\n---\nFR-COOP-011 reorder; traces BG-BSC-001", encoding="utf-8"
    )
    (tmp_path / "02/b.md").write_text(
        "---\nphase: '02'\n---\nFR-COOP-011 is verified by NFR-PLAT-002", encoding="utf-8"
    )
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 0, rc.output
    reg = IdentifierRegistry.load(tmp_path / "_registry" / "identifiers.yaml")
    ids = {e.id for e in reg}
    assert {"FR-COOP-011", "BG-BSC-001", "NFR-PLAT-002"} <= ids
    assert reg["NFR-PLAT-002"].kind == "NFR"


def test_sync_ignores_crypto_and_standard_tokens(tmp_path: Path):
    # AES-256 / SHA-256 / ISO-27001 must NOT be read as identifiers.
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "Encrypt with AES-256-GCM and SHA-256; comply with ISO-27001. **FR-001** real.",
        encoding="utf-8",
    )
    rc = CliRunner().invoke(main, ["sync", str(tmp_path)])
    assert rc.exit_code == 0, rc.output
    reg = IdentifierRegistry.load(tmp_path / "_registry" / "identifiers.yaml")
    ids = {e.id for e in reg}
    assert "FR-001" in ids
    assert not any(t in ids for t in ("AES-256", "SHA-256", "ISO-27001"))


def test_sync_identifiers_only_leaves_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# V\n- **Tenant:** an isolated customer\nFR-001 exists", encoding="utf-8"
    )
    reg_dir = tmp_path / "_registry"
    reg_dir.mkdir()
    (reg_dir / "glossary.yaml").write_text("terms: []\n", encoding="utf-8")
    rc = CliRunner().invoke(main, ["sync", str(tmp_path), "--identifiers-only"])
    assert rc.exit_code == 0, rc.output
    # Glossary file left exactly as it was.
    assert (reg_dir / "glossary.yaml").read_text(encoding="utf-8") == "terms: []\n"
    assert (reg_dir / "identifiers.yaml").exists()
