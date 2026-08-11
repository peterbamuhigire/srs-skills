from __future__ import annotations

import json
import shutil
from pathlib import Path

from engine.artifact_graph import ArtifactGraph
from engine.checks.change_impact import ChangeImpactCheck
from engine.checks.test_oracles import TestOraclesCheck as _TestOraclesCheck
from engine.checks.traceability import TraceabilityCheck
from engine.findings import FindingCollection
from engine.gates.phase02 import Phase02Gate
from engine.workspace import Workspace


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "engine" / "tests" / "fixtures" / "requirements_traceability"


def test_traceability_fixture_covers_ambiguity_acceptance_and_controlled_change() -> None:
    manifest = json.loads(
        (FIXTURE / "fixture-manifest.json").read_text(encoding="utf-8")
    )
    requirements = (
        FIXTURE / "02-requirements-engineering" / "requirements.md"
    ).read_text(encoding="utf-8")
    test_case = (FIXTURE / "05-testing-documentation" / "test-case.md").read_text(
        encoding="utf-8"
    )

    assert manifest["classification"] == "behavioural"
    assert manifest["data_classification"] == "synthetic-test-only"
    assert set(manifest["coverage"]) == {
        "ambiguity-resolution",
        "acceptance-criteria",
        "controlled-change",
    }
    assert "Ambiguity status: resolved" in requirements
    assert "**AC-001**" in requirements
    assert "Given" in test_case and "when" in test_case and "then" in test_case

    graph = ArtifactGraph.build(Workspace.load(FIXTURE))

    phase02_findings = FindingCollection()
    Phase02Gate().evaluate(graph, phase02_findings)
    assert not [
        finding
        for finding in phase02_findings
        if finding.gate_id in {
            "phase02.requirement_semantics",
            "phase02.stimulus_response",
        }
    ]

    traceability_findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, traceability_findings)
    assert list(traceability_findings) == []

    oracle_findings = FindingCollection()
    _TestOraclesCheck("phase05.test_oracles").run(graph, oracle_findings)
    assert list(oracle_findings) == []

    change_findings = FindingCollection()
    ChangeImpactCheck("phase09.change_impact", FIXTURE).run(
        graph, change_findings
    )
    assert list(change_findings) == []


def _copy_fixture(tmp_path: Path) -> Path:
    target = tmp_path / "requirements_traceability"
    shutil.copytree(FIXTURE, target)
    return target


def test_malformed_requirement_loses_upward_traceability(tmp_path: Path) -> None:
    target = _copy_fixture(tmp_path)
    requirements_path = target / "02-requirements-engineering" / "requirements.md"
    requirements = requirements_path.read_text(encoding="utf-8")
    requirements_path.write_text(
        requirements.replace(
            "traces to **BG-001** and **TC-001**",
            "has no explicit upstream goal trace",
        ),
        encoding="utf-8",
    )

    findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(
        ArtifactGraph.build(Workspace.load(target)), findings
    )

    assert any("no traceability link to any business goal" in f.message for f in findings)


def test_malformed_test_trace_is_blocked_by_both_checks(tmp_path: Path) -> None:
    target = _copy_fixture(tmp_path)
    test_case_path = target / "05-testing-documentation" / "test-case.md"
    test_case = test_case_path.read_text(encoding="utf-8")
    test_case_path.write_text(
        test_case.replace("requirement_trace:\n  - FR-001", "requirement_trace: []"),
        encoding="utf-8",
    )
    graph = ArtifactGraph.build(Workspace.load(target))

    traceability_findings = FindingCollection()
    TraceabilityCheck("phase09.traceability").run(graph, traceability_findings)
    oracle_findings = FindingCollection()
    _TestOraclesCheck("phase05.test_oracles").run(graph, oracle_findings)

    assert any("no traceability link to any test case" in f.message for f in traceability_findings)
    assert any("empty requirement_trace" in f.message for f in oracle_findings)


def test_malformed_change_impact_yaml_is_blocked(tmp_path: Path) -> None:
    target = _copy_fixture(tmp_path)
    cia_path = target / "_registry" / "change-impact.yaml"
    cia_path.write_text("entries: [", encoding="utf-8")
    findings = FindingCollection()

    ChangeImpactCheck("phase09.change_impact", target).run(
        ArtifactGraph.build(Workspace.load(target)), findings
    )

    assert any("schema_violation" == f.gate_id.rsplit(".", 1)[-1] for f in findings)
