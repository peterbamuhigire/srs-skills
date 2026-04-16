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
