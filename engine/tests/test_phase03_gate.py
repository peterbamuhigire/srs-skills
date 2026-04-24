from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase03 import Phase03Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- architecture_decisions_recorded ----------------------------------------

def test_passes_when_project_has_adr_directory(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001-choose-framework.md": (
            "# Decision\nWe chose X."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded") == []


def test_passes_when_project_has_adr_identifier(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nSee **ADR-001** for rationale."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded") == []


def test_flags_missing_adr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nNo decisions recorded."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.architecture_decisions_recorded"), (
        "expected an architecture_decisions_recorded finding "
        "when no ADR directory or ADR-### identifier exists"
    )


# -- interfaces_have_contracts ----------------------------------------------

def test_passes_when_api_spec_has_method_and_response(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/03-api-specification/users.md": (
            "# Users API\nGET /users returns 200 response with payload."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.interfaces_have_contracts") == []


def test_flags_api_spec_missing_method(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/03-api-specification/users.md": (
            "# Users API\nReturns 200 response payload but no method declared."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.interfaces_have_contracts"]
    assert msgs, "expected an interfaces_have_contracts finding"
    assert "HTTP method" in msgs[0]


def test_flags_api_spec_missing_response(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/03-api-specification/users.md": (
            "# Users API\nGET /users does a thing."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.interfaces_have_contracts"]
    assert msgs, "expected an interfaces_have_contracts finding"
    assert "response/status" in msgs[0]


def test_skips_interfaces_check_when_no_api_spec(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.interfaces_have_contracts") == []


# -- data_model_has_keys ----------------------------------------------------

def test_passes_when_database_design_has_primary_key(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/04-database-design/schema.md": (
            "# Schema\nusers.id PRIMARY KEY."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.data_model_has_keys") == []


def test_passes_when_database_design_has_lowercase_primary_key(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/04-database-design/schema.md": (
            "# Schema\nusers.id is the primary key of the table."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.data_model_has_keys") == []


def test_flags_database_design_missing_pk(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/04-database-design/schema.md": (
            "# Schema\nA table of users with no key declaration."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.data_model_has_keys"]
    assert msgs, "expected a data_model_has_keys finding"
    assert "no primary key declaration" in msgs[0]


def test_skips_data_model_check_when_no_database_design(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.data_model_has_keys") == []


# -- nfrs_link_to_design_choices --------------------------------------------

def test_passes_when_nfr_referenced_in_design(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-nonfunctional-requirements/nfrs.md": (
            "# NFRs\n- **NFR-001** availability 99.9%"
        ),
        "03-design-documentation/adr/0001.md": (
            "# ADR\nThis decision satisfies NFR-001 under expected load."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.nfrs_link_to_design_choices") == []


def test_flags_nfr_not_referenced_in_design(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-nonfunctional-requirements/nfrs.md": (
            "# NFRs\n- **NFR-001** availability 99.9%\n"
            "- **NFR-002** response time under 500ms"
        ),
        "03-design-documentation/adr/0001.md": (
            "# ADR\nThis decision satisfies NFR-001 under expected load."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.nfrs_link_to_design_choices"]
    assert msgs, "expected an nfrs_link_to_design_choices finding"
    assert "NFR-002" in msgs[0]


def test_passes_nfr_check_when_no_nfrs_declared(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.nfrs_link_to_design_choices") == []


def test_flags_fr_without_design_evidence(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-001** The system shall accept claim submissions.\n"
        ),
        "03-design-documentation/adr/0001.md": (
            "# ADR\nFR-001 is important.\n"
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.requirements_have_design_evidence"]
    assert msgs
    assert "concrete design evidence keywords" in msgs[0]


def test_passes_when_fr_has_design_evidence(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "02-requirements-engineering/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-001** The system shall accept claim submissions.\n"
        ),
        "03-design-documentation/03-api-specification/claims.md": (
            "# Claims API\nPOST /claims returns 201; endpoint fulfils FR-001.\n"
        ),
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/threat-model.md": "# Threat Model",
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.requirements_have_design_evidence") == []


# -- security_threat_model_present ------------------------------------------

def test_passes_when_threat_model_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/05-security/threat-model.md": (
            "# Threat Model\nSTRIDE analysis..."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.security_threat_model_present") == []


def test_passes_when_threat_model_mentioned_in_design_body(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nOur Threat Model analysis is below."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.security_threat_model_present") == []


def test_flags_missing_threat_model_when_design_artifacts_exist(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nNo mention of that topic here."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.security_threat_model_present"), (
        "expected a security_threat_model_present finding when "
        "no threat-model.md exists and body lacks 'threat model'"
    )


# -- iot_signal_inventory_present -------------------------------------------

def test_skips_iot_check_when_not_iot_project(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nRegular web application."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.iot_signal_inventory_present") == []


def test_flags_iot_project_without_signal_inventory(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/07-iot-system-design/overview.md": (
            "# IoT Overview\nDevice layer..."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase03.iot_signal_inventory_present"]
    assert msgs, "expected an iot_signal_inventory_present finding"
    assert "signal inventory" in msgs[0]


def test_passes_iot_project_with_signal_inventory(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/07-iot-system-design/overview.md": (
            "# IoT Overview\nDevice layer..."
        ),
        "03-design-documentation/07-iot-system-design/signal-inventory.md": (
            "# Signal Inventory\n| signal | unit |"
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.iot_signal_inventory_present") == []


def test_passes_iot_project_with_signals_md(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/07-iot-system-design/overview.md": (
            "# IoT Overview\nDevice layer..."
        ),
        "03-design-documentation/07-iot-system-design/signals.md": (
            "# Signals"
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.iot_signal_inventory_present") == []


def test_flags_iot_project_detected_via_body_without_inventory(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-design-documentation/adr/0001.md": "# ADR",
        "03-design-documentation/01-high-level-design/HLD.md": (
            "# HLD\nThis system integrates IoT sensors across buildings."
        ),
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert findings.for_gate("phase03.iot_signal_inventory_present"), (
        "expected an iot_signal_inventory_present finding when "
        "body mentions IoT but no signal inventory exists"
    )


# -- clause attachment ------------------------------------------------------

def test_findings_carry_iso_42010_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase03Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "ISO/IEC/IEEE 42010:2011" in f.message
