from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase02 import Phase02Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- composition: smart_nfr + stimulus_response -------------------------------

def test_aggregates_smart_nfr_and_stimulus_response_findings(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/nfr.md": (
            "# NFR\n"
            "\n"
            "- **NFR-001** The system shall be fast.\n"
        ),
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-001** The system will accept claim submissions.\n"
        ),
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    gate_ids = [f.gate_id for f in findings]
    assert "phase02.smart_nfr" in gate_ids
    assert "phase02.stimulus_response" in gate_ids
    assert len(findings) >= 2


def test_passes_clean_phase02_project(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/nfr.md": (
            "# NFR\n"
            "\n"
            "- **NFR-001** Response time shall be <= 500 ms at P95.\n"
        ),
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-001** The system shall accept claim submissions.\n"
        ),
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    assert len(findings) == 0


# -- silent skip for missing registries --------------------------------------

def test_skips_registry_checks_when_no_registry_yaml(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    for f in findings:
        assert not f.gate_id.startswith("phase02.id_registry")
        assert not f.gate_id.startswith("phase02.glossary_registry")


def test_runs_identifier_registry_when_yaml_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-0101** The system shall handle claims.\n"
        ),
        "_registry/identifiers.yaml": (
            "identifiers:\n"
            "  - id: \"FR-0202\"\n"
            "    kind: \"FR\"\n"
            "    defined_in: \"02-requirements-engineering/fr.md\"\n"
        ),
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    unknown = [f for f in findings if f.gate_id == "phase02.id_registry.unknown_id"]
    assert unknown, "expected an unknown_id finding for FR-0101"
    assert any("FR-0101" in f.message for f in unknown)


def test_runs_glossary_registry_when_yaml_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/nfr.md": (
            "# NFR\n"
            "\n"
            "FNOL data is retained. IntakeForm records are archived.\n"
        ),
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "FNOL identities are validated at intake. IntakeForm drives flow.\n"
        ),
        "_registry/glossary.yaml": (
            "terms:\n"
            "  - term: \"Submission\"\n"
            "    definition: \"A filed record of intake data.\"\n"
        ),
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    missing = [f for f in findings
               if f.gate_id == "phase02.glossary_registry.missing_term"]
    assert missing, "expected missing_term findings for domain-signal tokens"
    assert any("FNOL" in f.message for f in missing)
    assert any("IntakeForm" in f.message for f in missing)


# -- clause attachment --------------------------------------------------------

def test_findings_carry_ieee_830_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/nfr.md": (
            "# NFR\n"
            "\n"
            "- **NFR-001** The system shall be fast.\n"
        ),
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-001** The system will accept claim submissions.\n"
        ),
    })
    findings = FindingCollection()
    Phase02Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "[IEEE Std 830-1998 §4.3]" in f.message
