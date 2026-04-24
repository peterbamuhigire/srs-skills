from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase05 import Phase05Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- normative_test_structure ------------------------------------------------

def test_flags_test_case_without_required_keys(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/test-plan/tc.md": (
            "---\nphase: '05'\n---\n- **TC-001** something"
        ),
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase05.normative_test_structure"]
    assert msgs, "expected at least one normative_test_structure finding"
    joined = " ".join(msgs).lower()
    assert (
        "expected_results" in joined
        or "requirement_trace" in joined
        or "inputs" in joined
    )


def test_passes_when_test_case_has_all_required_keys(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/test-plan/tc.md": (
            "---\n"
            "phase: '05'\n"
            "inputs: ['valid claim payload']\n"
            "expected_results: ['claim stored']\n"
            "requirement_trace: ['FR-001']\n"
            "---\n"
            "- **TC-001** something"
        ),
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.normative_test_structure") == []


def test_flags_empty_test_oracle_fields(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/test-plan/tc.md": (
            "---\n"
            "phase: '05'\n"
            "inputs: []\n"
            "expected_results: []\n"
            "requirement_trace: []\n"
            "---\n"
            "- **TC-001** something"
        ),
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings if f.gate_id == "phase05.test_oracles"]
    assert msgs
    assert any("empty expected_results" in m or "empty requirement_trace" in m for m in msgs)


# -- required_evidence -------------------------------------------------------

def test_flags_missing_required_evidence(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/test-plan/tc.md": (
            "---\n"
            "phase: '05'\n"
            "inputs: ['x']\n"
            "expected_results: ['y']\n"
            "requirement_trace: ['FR-001']\n"
            "---\n"
            "- **TC-001** something"
        ),
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.required_evidence"), (
        "expected a required_evidence finding when the file is missing"
    )


def test_flags_empty_required_evidence(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/29119-deterministic-checks.md": "",
        "05-testing-documentation/test-plan/tc.md": (
            "---\n"
            "phase: '05'\n"
            "inputs: ['x']\n"
            "expected_results: ['y']\n"
            "requirement_trace: ['FR-001']\n"
            "---\n"
            "- **TC-001** something"
        ),
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.required_evidence"), (
        "expected a required_evidence finding when the file is empty"
    )


# -- coverage_measurable -----------------------------------------------------

def test_flags_coverage_below_fr_count_without_matrix(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-functional-requirements/frs.md": (
            "# FRs\n- **FR-001** first\n- **FR-002** second"
        ),
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.coverage_measurable"), (
        "expected a coverage_measurable finding when TC count < FR count and no matrix exists"
    )


def test_passes_coverage_when_matrix_exists(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-functional-requirements/frs.md": (
            "# FRs\n- **FR-001** first\n- **FR-002** second"
        ),
        "05-testing-documentation/coverage-matrix.md": "# Coverage\n| FR | TC |",
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.coverage_measurable") == []


def test_passes_coverage_when_tc_count_meets_fr_count(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "03-functional-requirements/frs.md": (
            "# FRs\n- **FR-001** first\n- **FR-002** second"
        ),
        "05-testing-documentation/test-plan/tc.md": (
            "---\n"
            "phase: '05'\n"
            "inputs: ['valid input']\n"
            "expected_results: ['expected output']\n"
            "requirement_trace: ['FR-001','FR-002']\n"
            "---\n"
            "- **TC-001** first\n- **TC-002** second"
        ),
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 and FR-002 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.coverage_measurable") == []


# -- exit_evidence -----------------------------------------------------------

def test_flags_missing_exit_evidence(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.exit_evidence"), (
        "expected an exit_evidence finding when the report is missing"
    )


def test_exit_evidence_missing_required_words(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nAll items closed with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.exit_evidence"), (
        "expected an exit_evidence finding when report lacks required words"
    )


def test_exit_evidence_passes_when_words_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "05-testing-documentation/29119-deterministic-checks.md": "# Checks\n- verified",
        "05-testing-documentation/test-completion-report.md": (
            "# Completion\nTested FR-001 with result pass."
        ),
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert findings.for_gate("phase05.exit_evidence") == []


# -- clause attachment -------------------------------------------------------

def test_findings_carry_iso_29119_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase05Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "BS ISO/IEC/IEEE 29119-3:2013" in f.message
