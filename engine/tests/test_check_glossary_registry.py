from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.glossary_registry import GlossaryRegistryCheck

_GLOSSARY_YAML = """\
terms:
  - term: NIN
    definition: Uganda National Identification Number
  - term: Orphan
    definition: a glossary term with no artifact occurrence
"""


def test_passes_when_used_acronym_is_in_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nNIN validation is core.", encoding="utf-8"
    )
    (tmp_path / "_context/glossary.md").write_text(
        "# Glossary\n- **NIN:** national id", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** Validate NIN on enrolment.",
        encoding="utf-8",
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    assert not any("NIN" in m and "missing" in m.lower() for m in msgs)


def test_flags_acronym_used_in_artifacts_but_missing_from_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nUNEB grading must conform.", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\nUNEB export is mandatory.", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("UNEB" in m and "missing" in m.lower() for m in msgs)


def test_flags_camelcase_term_used_in_artifacts_but_missing_from_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nTenantScope enforces isolation.", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\nTenantScope is applied to every model.",
        encoding="utf-8",
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("TenantScope" in m and "missing" in m.lower() for m in msgs)


def test_does_not_flag_regular_capitalised_english_words(tmp_path: Path):
    """Action, Access, Claim — regular English capitalised nouns are not
    domain-term candidates and must not be flagged."""
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nAction items: Access control is critical. Claim submission.",
        encoding="utf-8",
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\nAction and Access and Claim appear here too.",
        encoding="utf-8",
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    for noise in ("Action", "Access", "Claim"):
        assert not any(
            f"'{noise}'" in m and "missing" in m.lower() for m in msgs
        ), f"{noise} wrongly flagged: {msgs}"


def test_ignores_stoplisted_acronyms(tmp_path: Path):
    """Universal acronyms like HTTP, JSON, CSV must never be flagged as
    missing glossary terms."""
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text(
        "API over HTTP returns JSON; CSV export is supported.", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\nHTTP, JSON, CSV are universal.", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    for universal in ("HTTP", "JSON", "CSV"):
        assert not any(
            f"'{universal}'" in m and "missing" in m.lower() for m in msgs
        ), f"{universal} wrongly flagged: {msgs}"


def test_flags_orphan_term_in_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck(
        "phase09.glossary_registry", tmp_path / "_registry/glossary.yaml"
    ).run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("Orphan" in m and "orphan" in m.lower() for m in msgs)
