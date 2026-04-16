from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.glossary_registry import GlossaryRegistryCheck

_GLOSSARY_YAML = """\
terms:
  - term: Claim
    definition: a formal request for payment from an insurer
  - term: Orphan
    definition: a glossary term with no artifact occurrence
"""

def test_passes_when_used_terms_are_in_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    # "Claim" appears in 2 distinct files -> triggers domain-term detection.
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nClaim processing is core.", encoding="utf-8"
    )
    (tmp_path / "_context/glossary.md").write_text(
        "# Glossary\n- **Claim:** thing", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** Handle Claim submission", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(
        # Include Orphan too — will produce an orphan finding; test narrows to "Claim not flagged".
        _GLOSSARY_YAML, encoding="utf-8"
    )
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck("phase09.glossary_registry", tmp_path / "_registry/glossary.yaml").run(graph, findings)
    msgs = [f.message for f in findings]
    # "Claim" is in glossary AND used -> no "missing" finding for Claim.
    assert not any("Claim" in m and "missing" in m.lower() for m in msgs)

def test_flags_term_used_in_artifacts_but_missing_from_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    # Use "Underwriting" in 2 distinct files, NOT in glossary.
    (tmp_path / "_context/vision.md").write_text(
        "# Vision\nUnderwriting flows are critical.", encoding="utf-8"
    )
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\nUnderwriting is performed by AI.", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    # Glossary contains only "Claim" + "Orphan", not Underwriting.
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck("phase09.glossary_registry", tmp_path / "_registry/glossary.yaml").run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("Underwriting" in m and "missing" in m.lower() for m in msgs)

def test_flags_orphan_term_in_glossary(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/glossary.yaml").write_text(_GLOSSARY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    GlossaryRegistryCheck("phase09.glossary_registry", tmp_path / "_registry/glossary.yaml").run(graph, findings)
    msgs = [f.message for f in findings]
    # Both "Claim" and "Orphan" are unused in this fixture (vision.md only has "V").
    assert any("Orphan" in m and "orphan" in m.lower() for m in msgs)
