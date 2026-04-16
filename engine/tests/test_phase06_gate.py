from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase06 import Phase06Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- deployment_guide_has_rollback -----------------------------------------

def test_passes_when_deployment_guide_has_rollback(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "06-deployment-operations/deployment-guide.md": (
            "# Deployment Guide\n"
            "## Rollback procedure\n"
            "If deployment fails, rollback to the previous release tag."
        ),
    })
    findings = FindingCollection()
    Phase06Gate().evaluate(graph, findings)
    assert findings.for_gate("phase06.deployment_guide_has_rollback") == []


def test_flags_missing_deployment_guide(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "06-deployment-operations/runbook.md": "# Runbook",
    })
    findings = FindingCollection()
    Phase06Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase06.deployment_guide_has_rollback"]
    assert msgs, "expected a deployment_guide_has_rollback finding"
    assert "No deployment guide found" in msgs[0]


def test_flags_deployment_guide_without_rollback(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "06-deployment-operations/deployment-guide.md": (
            "# Deployment Guide\nDeploy via the CI pipeline only."
        ),
    })
    findings = FindingCollection()
    Phase06Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase06.deployment_guide_has_rollback"]
    assert msgs, "expected a deployment_guide_has_rollback finding"
    assert "no rollback procedure" in msgs[0]


# -- runbook_has_escalation ------------------------------------------------

def test_passes_when_runbook_has_escalation(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "06-deployment-operations/deployment-guide.md": (
            "# Deployment Guide\nRollback via tag."
        ),
        "06-deployment-operations/runbook.md": (
            "# Runbook\n"
            "## Escalation\n"
            "Page the on-call SRE, then escalate to the platform lead."
        ),
    })
    findings = FindingCollection()
    Phase06Gate().evaluate(graph, findings)
    assert findings.for_gate("phase06.runbook_has_escalation") == []


def test_flags_runbook_without_escalation(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "06-deployment-operations/deployment-guide.md": (
            "# Deployment Guide\nRollback via tag."
        ),
        "06-deployment-operations/runbook.md": (
            "# Runbook\nGeneral operations only; no handoff defined."
        ),
    })
    findings = FindingCollection()
    Phase06Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase06.runbook_has_escalation"]
    assert msgs, "expected a runbook_has_escalation finding"
    assert "no escalation path" in msgs[0]
