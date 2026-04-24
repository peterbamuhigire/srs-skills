from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase09 import Phase09Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- traceability ----------------------------------------------------------

def test_passes_when_trace_chain_complete(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "01-strategic-vision/goals.md": "# Goals\n\n- **BG-001** Mission.\n",
        "04-functional-requirements/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-0101** traces to BG-001 and TC-0101.\n"
        ),
        "05-testing-documentation/tc.md": (
            "# TC\n"
            "\n"
            "- **TC-0101** covers FR-0101.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.traceability") == []


def test_flags_orphan_fr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-functional-requirements/fr.md": (
            "# FR\n"
            "\n"
            "- **FR-0101** has no upstream or downstream links.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    trace_findings = findings.for_gate("phase09.traceability")
    assert trace_findings, "expected traceability findings"
    for f in trace_findings:
        assert f.gate_id == "phase09.traceability"
        assert "ISO/IEC 27001:2022" in f.message


# -- audit_report_present --------------------------------------------------

def test_passes_when_audit_report_lists_gates(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "09-governance-compliance/audit-report.md": (
            "# Audit Report\n"
            "\n"
            "- phase01: PASS\n"
            "- phase05: PASS\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.audit_report_present") == []


def test_flags_missing_audit_report(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.audit_report_present"]
    assert msgs, "expected an audit_report_present finding"
    assert "No audit report found" in msgs[0]


def test_flags_empty_audit_report(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "09-governance-compliance/audit-report.md": "",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.audit_report_present"]
    assert msgs, "expected an audit_report_present finding"
    assert "is empty" in msgs[0]


def test_flags_audit_report_without_gate_references(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "09-governance-compliance/audit-report.md": (
            "# Audit Report\n"
            "\n"
            "- All systems reviewed.\n"
            "- No issues outstanding.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.audit_report_present"]
    assert msgs, "expected an audit_report_present finding"
    assert "does not list pass/fail status" in msgs[0]


def test_flags_selected_control_without_complete_evidence_section(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "_registry/controls.yaml": (
            "selected:\n"
            "  - id: CTRL-UG-001\n"
            "    applies_because: \"Personal data collection\"\n"
        ),
        "09-governance-compliance/03-compliance.md": (
            "# Compliance\n"
            "## CTRL-UG-001\n"
            "- Evidence: FR-001.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings if f.gate_id == "phase09.compliance_evidence"]
    assert msgs
    assert "lacks complete compliance evidence" in msgs[0]


def test_passes_selected_control_with_complete_evidence_section(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "_registry/controls.yaml": (
            "selected:\n"
            "  - id: CTRL-UG-001\n"
            "    applies_because: \"Personal data collection\"\n"
        ),
        "09-governance-compliance/03-compliance.md": (
            "# Compliance\n"
            "## CTRL-UG-001\n"
            "- Status: Implemented.\n"
            "- Evidence: FR-001 and 03-design-documentation/05-ux-specification/ui-spec.md.\n"
            "- Reviewer: Data Protection Officer.\n"
        ),
        "09-governance-compliance/audit-report.md": "# Audit\n- phase09: PASS\n",
        "09-governance-compliance/risk-register.md": "# Risks\n- **R-001** linked to CTRL-UG-001 and FR-001.\n",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.compliance_evidence") == []


# -- risk_register_links_to_fr --------------------------------------------

def test_passes_when_risks_link_to_fr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "09-governance-compliance/risk-register.md": (
            "# Risk Register\n"
            "\n"
            "- **R-001** Data loss risk; mitigated by FR-0101.\n"
            "- **R-002** Unauthorised access; mitigated by CTRL-0210.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.risk_register_links_to_fr") == []


def test_flags_missing_risk_register(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.risk_register_links_to_fr"]
    assert msgs, "expected a risk_register_links_to_fr finding"
    assert "No risk register found" in msgs[0]


def test_flags_unlinked_risk(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "09-governance-compliance/risk-register.md": (
            "# Risk Register\n"
            "\n"
            "- **R-001** Data loss risk; mitigated by FR-0101.\n"
            "- **R-002** Operational risk with no associated control.\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.risk_register_links_to_fr"]
    assert len(msgs) == 1
    assert "Risk R-002" in msgs[0]
    assert "not linked to any FR-, NFR-, or CTRL- identifier" in msgs[0]


# -- waivers_have_expiry ---------------------------------------------------

def test_skips_waivers_check_when_no_registry_file(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.waivers_have_expiry") == []


def test_passes_when_waivers_within_90_day_window(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "_registry/waivers.yaml": (
            "waivers:\n"
            "  - id: \"W-001\"\n"
            "    gate: \"phase02.smart_nfr\"\n"
            "    scope: \"*\"\n"
            "    reason: \"Plan 03 pending\"\n"
            "    approver: \"peter\"\n"
            "    approved_on: 2026-04-01\n"
            "    expires_on: 2026-05-01\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert findings.for_gate("phase09.waivers_have_expiry") == []


def test_flags_waiver_beyond_90_days(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "_registry/waivers.yaml": (
            "waivers:\n"
            "  - id: \"W-002\"\n"
            "    gate: \"phase02.smart_nfr\"\n"
            "    scope: \"*\"\n"
            "    reason: \"Long-running gap\"\n"
            "    approver: \"peter\"\n"
            "    approved_on: 2026-01-01\n"
            "    expires_on: 2026-06-01\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.waivers_have_expiry"]
    assert len(msgs) == 1
    assert "W-002" in msgs[0]
    assert "max allowed: 90" in msgs[0]


def test_flags_waiver_with_expiry_before_approval(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "_registry/waivers.yaml": (
            "waivers:\n"
            "  - id: \"W-003\"\n"
            "    gate: \"phase02.smart_nfr\"\n"
            "    scope: \"*\"\n"
            "    reason: \"Data error\"\n"
            "    approver: \"peter\"\n"
            "    approved_on: 2026-05-01\n"
            "    expires_on: 2026-04-01\n"
        ),
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase09.waivers_have_expiry"]
    assert len(msgs) == 1
    assert "W-003" in msgs[0]
    assert "expiry before approval date" in msgs[0]


# -- clause attachment ------------------------------------------------------

def test_findings_carry_iso_27001_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase09Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "ISO/IEC 27001:2022" in f.message
