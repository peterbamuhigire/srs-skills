from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.identifier_registry import IdentifierRegistryCheck

def _ws(tmp_path: Path, files: dict) -> ArtifactGraph:
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

_REGISTRY_YAML = """\
identifiers:
  - id: FR-001
    kind: FR
    defined_in: 02/srs.md
    title: Submit claim
"""

def test_passes_when_all_artifact_ids_in_registry(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** trace", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/identifiers.yaml").write_text(_REGISTRY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    IdentifierRegistryCheck("phase09.id_registry", tmp_path / "_registry/identifiers.yaml").run(graph, findings)
    assert len(findings) == 0, [f.message for f in findings]

def test_flags_unknown_id_in_artifact(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "02").mkdir()
    (tmp_path / "02/srs.md").write_text(
        "---\nphase: '02'\n---\n- **FR-001** ok\n- **FR-999** unknown", encoding="utf-8"
    )
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/identifiers.yaml").write_text(_REGISTRY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    IdentifierRegistryCheck("phase09.id_registry", tmp_path / "_registry/identifiers.yaml").run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("FR-999" in m for m in msgs)

def test_flags_orphan_id_in_registry(tmp_path: Path):
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# V", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    # Registry says FR-001 exists but no artifact references it.
    (tmp_path / "_registry/identifiers.yaml").write_text(_REGISTRY_YAML, encoding="utf-8")
    graph = ArtifactGraph.build(Workspace.load(tmp_path))
    findings = FindingCollection()
    IdentifierRegistryCheck("phase09.id_registry", tmp_path / "_registry/identifiers.yaml").run(graph, findings)
    msgs = [f.message for f in findings]
    assert any("FR-001" in m and "orphan" in m.lower() for m in msgs)
