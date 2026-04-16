from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.sign_off import SignOffCheck


def _base(tmp_path: Path) -> Path:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/vision.md").write_text("# Vision\n", encoding="utf-8")
    (tmp_path / "_registry").mkdir()
    return tmp_path


def _run(project: Path) -> FindingCollection:
    findings = FindingCollection()
    graph = ArtifactGraph.build(Workspace.load(project))
    SignOffCheck("phase09.sign_off", project).run(graph, findings)
    return findings


def test_happy_path(tmp_path: Path):
    project = _base(tmp_path)
    art = project / "02-requirements-engineering" / "srs.md"
    art.parent.mkdir(parents=True)
    art.write_text("# SRS\n", encoding="utf-8")
    (project / "_registry/sign-off-ledger.yaml").write_text(
        "sign_offs:\n"
        "  - gate: phase02\n"
        "    signer: \"Jane\"\n"
        "    role: \"Chief Architect\"\n"
        "    signed_on: 2026-04-16\n"
        "    artifact_set:\n"
        "      - \"02-requirements-engineering/srs.md\"\n",
        encoding="utf-8",
    )
    findings = _run(project)
    assert list(findings) == []


def test_flags_missing_artifact(tmp_path: Path):
    project = _base(tmp_path)
    (project / "_registry/sign-off-ledger.yaml").write_text(
        "sign_offs:\n"
        "  - gate: phase02\n"
        "    signer: \"Jane\"\n"
        "    role: \"Chief Architect\"\n"
        "    signed_on: 2026-04-16\n"
        "    artifact_set:\n"
        "      - \"02-requirements-engineering/missing.md\"\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.sign_off.missing_artifact" in ids


def test_flags_schema_violation(tmp_path: Path):
    project = _base(tmp_path)
    # artifact_set empty array violates minItems: 1.
    (project / "_registry/sign-off-ledger.yaml").write_text(
        "sign_offs:\n"
        "  - gate: phase02\n"
        "    signer: \"Jane\"\n"
        "    role: \"Chief Architect\"\n"
        "    signed_on: 2026-04-16\n"
        "    artifact_set: []\n",
        encoding="utf-8",
    )
    findings = _run(project)
    ids = [f.gate_id for f in findings]
    assert "phase09.sign_off.schema_violation" in ids
