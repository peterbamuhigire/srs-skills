from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.adr_catalog import AdrCatalogCheck


def _base(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    adr_dir = tmp_path / "09-governance-compliance" / "05-adr"
    adr_dir.mkdir(parents=True)
    return tmp_path


def _run(project: Path) -> FindingCollection:
    findings = FindingCollection()
    graph = ArtifactGraph.build(Workspace.load(project))
    AdrCatalogCheck("phase09.adr_catalog", project).run(graph, findings)
    return findings


def test_happy_path(tmp_path: Path):
    project = _base(tmp_path)
    (project / "09-governance-compliance/05-adr/0001-choose-postgres.md").write_text(
        "# ADR-0001: Choose Postgres\n", encoding="utf-8"
    )
    (project / "_registry/adr-catalog.yaml").write_text(
        "adrs:\n"
        "  - id: ADR-0001\n"
        "    title: Choose Postgres\n"
        "    status: accepted\n"
        "    decided_on: 2026-04-16\n"
        "    deciders: [\"Chief Architect\"]\n",
        encoding="utf-8",
    )
    findings = _run(project)
    assert list(findings) == []


def test_flags_uncatalogued_adr(tmp_path: Path):
    project = _base(tmp_path)
    (project / "09-governance-compliance/05-adr/0002-use-kafka.md").write_text(
        "# ADR-0002: Use Kafka\n", encoding="utf-8"
    )
    (project / "_registry/adr-catalog.yaml").write_text(
        "adrs: []\n", encoding="utf-8"
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.adr_catalog.uncatalogued" in ids


def test_flags_missing_file(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/adr-catalog.yaml").write_text(
        "adrs:\n"
        "  - id: ADR-0003\n"
        "    title: Missing file\n"
        "    status: accepted\n"
        "    decided_on: 2026-04-16\n"
        "    deciders: [\"X\"]\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.adr_catalog.missing_file" in ids


def test_flags_dangling_supersession(tmp_path: Path):
    project = _base(tmp_path)
    (project / "09-governance-compliance/05-adr/0001-old.md").write_text(
        "# ADR-0001\n", encoding="utf-8"
    )
    (project / "_registry/adr-catalog.yaml").write_text(
        "adrs:\n"
        "  - id: ADR-0001\n"
        "    title: Old\n"
        "    status: superseded\n"
        "    superseded_by: ADR-0099\n"
        "    decided_on: 2026-04-16\n"
        "    deciders: [\"X\"]\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.adr_catalog.dangling_supersession" in ids
