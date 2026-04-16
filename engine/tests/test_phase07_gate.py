from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase07 import Phase07Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- dor_references_baseline ------------------------------------------------

def test_passes_when_dor_references_baseline_id(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# Definition of Ready\n"
            "- Story is linked to **BG-001** and **FR-0102** in the backlog.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.dor_references_baseline") == []


def test_flags_missing_dor(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-plan.md": "# Sprint Plan",
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.dor_references_baseline"]
    assert msgs, "expected a dor_references_baseline finding"
    assert "No Definition of Ready document found" in msgs[0]


def test_flags_dor_without_baseline_reference(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# Definition of Ready\n"
            "- Story has acceptance criteria and is estimated.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.dor_references_baseline"]
    assert msgs, "expected a dor_references_baseline finding"
    assert "does not reference any baseline ID" in msgs[0]


# -- dod_references_compliance ----------------------------------------------

def test_passes_when_dod_references_compliance(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# DoR\n- Linked to **FR-0100**."
        ),
        "07-agile-artifacts/definition-of-done.md": (
            "# Definition of Done\n"
            "- Security review completed, WCAG AA verified, "
            "and compliance checks passed.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.dod_references_compliance") == []


def test_flags_dod_without_compliance_reference(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/definition-of-ready.md": (
            "# DoR\n- Linked to **FR-0100**."
        ),
        "07-agile-artifacts/definition-of-done.md": (
            "# Definition of Done\n"
            "- Code merged and unit tests pass.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.dod_references_compliance"]
    assert msgs, "expected a dod_references_compliance finding"
    assert "does not reference any compliance or quality standard" in msgs[0]


# -- sprint_artifacts_have_ids ----------------------------------------------

def test_passes_when_sprint_items_have_ids(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-plan.md": (
            "# Sprint Plan\n"
            "\n"
            "## Committed items\n"
            "\n"
            "- **FR-0101** Implement loan scoring module.\n"
            "- **FR-0102** Add reviewer assignment UI.\n"
            "- **NFR-0210** Latency budget for scoring endpoint.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.sprint_artifacts_have_ids") == []


def test_flags_sprint_items_without_ids(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-plan.md": (
            "# Sprint Plan\n"
            "\n"
            "## Committed items\n"
            "\n"
            "- Implement loan scoring module.\n"
            "- **FR-0102** Add reviewer assignment UI.\n"
            "- Improve dashboard performance.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.sprint_artifacts_have_ids"]
    assert len(msgs) == 2, f"expected 2 findings, got {len(msgs)}: {msgs}"
    assert all("no identifier" in m for m in msgs)
    assert all("expected **XX-###** marker" in m for m in msgs)


# -- retro_actions_assigned -------------------------------------------------

def test_passes_when_retro_actions_have_owner_and_due(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/retrospective-sprint-01.md": (
            "# Retrospective - Sprint 01\n"
            "\n"
            "## Actions\n"
            "\n"
            "- **A-001** Harden CI pipeline. owner: @alice due 2026-05-01\n"
            "- **ACTION-002** Refresh onboarding docs. "
            "owner: @bob due 2026-05-08\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.retro_actions_assigned") == []


def test_flags_retro_action_missing_owner(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/retro-sprint-01.md": (
            "# Retro - Sprint 01\n"
            "\n"
            "## Actions\n"
            "\n"
            "- **A-001** Harden CI pipeline. due 2026-05-01\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.retro_actions_assigned"]
    assert len(msgs) == 1, f"expected 1 finding, got {len(msgs)}: {msgs}"
    assert "A-001" in msgs[0]
    assert "missing: owner" in msgs[0]


def test_flags_retro_action_missing_due_date(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/retrospective.md": (
            "# Retrospective\n"
            "\n"
            "## Actions\n"
            "\n"
            "- **ACTION-007** Review deployment cadence. owner: @carol\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.retro_actions_assigned"]
    assert len(msgs) == 1, f"expected 1 finding, got {len(msgs)}: {msgs}"
    assert "ACTION-007" in msgs[0]
    assert "missing: due date" in msgs[0]


# -- velocity_history_present -----------------------------------------------

def test_passes_when_velocity_history_has_multiple_sprints(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/velocity.md": (
            "# Velocity History\n"
            "\n"
            "| Sprint    | Points |\n"
            "|-----------|--------|\n"
            "| sprint-01 | 24     |\n"
            "| sprint-02 | 28     |\n"
            "| sprint-03 | 26     |\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert findings.for_gate("phase07.velocity_history_present") == []


def test_flags_missing_velocity_history(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-plan.md": "# Sprint Plan\n- **FR-001** item",
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.velocity_history_present"]
    assert msgs, "expected a velocity_history_present finding"
    assert "No velocity history found" in msgs[0]


def test_flags_velocity_history_with_single_sprint(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "07-agile-artifacts/sprint-metrics.md": (
            "# Sprint Metrics\n"
            "\n"
            "Only sprint-01 has been completed so far.\n"
        ),
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase07.velocity_history_present"]
    assert msgs, "expected a velocity_history_present finding"
    assert "fewer than 2 sprints" in msgs[0]
    assert "found 1" in msgs[0]


# -- clause attachment ------------------------------------------------------

def test_findings_carry_pmbok_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase07Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "PMBOK Guide 7th Edition" in f.message
        assert "2.6" in f.message
