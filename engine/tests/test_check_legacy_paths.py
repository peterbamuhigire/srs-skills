from pathlib import Path
from engine.findings import FindingCollection
from engine.checks.legacy_paths import LegacyPathCheck

def test_passes_when_only_alias_block_legacy(tmp_path: Path):
    f = tmp_path / "SKILL.md"
    f.write_text(
        "# Skill\n<!-- alias-block start -->\n`../project_context/`\n<!-- alias-block end -->\n",
        encoding="utf-8",
    )
    findings = FindingCollection()
    LegacyPathCheck().scan_file(f, findings)
    assert len(findings) == 0

def test_flags_naked_legacy_reference(tmp_path: Path):
    f = tmp_path / "SKILL.md"
    f.write_text("# Skill\nUse the file at ../project_context/vision.md\n", encoding="utf-8")
    findings = FindingCollection()
    LegacyPathCheck().scan_file(f, findings)
    assert len(findings) == 1

def test_flags_multiple_naked_lines(tmp_path: Path):
    f = tmp_path / "SKILL.md"
    f.write_text(
        "# Skill\nUse ../project_context/vision.md\nAlso ../output/report.md\n",
        encoding="utf-8",
    )
    findings = FindingCollection()
    LegacyPathCheck().scan_file(f, findings)
    assert len(findings) == 2
