from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase04 import Phase04Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- coding_standards_referenced --------------------------------------------

def test_passes_when_coding_standards_present(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/coding-standards.md": (
            "# Coding Standards\nUse 4-space indentation."
        ),
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    assert findings.for_gate("phase04.coding_standards_referenced") == []


def test_flags_missing_coding_standards(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/README.md": "# Development",
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase04.coding_standards_referenced"]
    assert msgs, "expected a coding_standards_referenced finding"
    assert "coding-standards.md" in msgs[0]


# -- env_setup_reproducible -------------------------------------------------

def test_passes_when_env_setup_complete(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/coding-standards.md": "# Coding Standards",
        "04-development/env-setup.md": (
            "# Env Setup\n"
            "## Prerequisites\nNode 20, Python 3.11.\n"
            "## Install\nRun `npm install` to bootstrap dependencies.\n"
            "## Verify\nRun `npm test` to validate the setup."
        ),
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    assert findings.for_gate("phase04.env_setup_reproducible") == []


def test_flags_missing_env_setup(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/coding-standards.md": "# Coding Standards",
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase04.env_setup_reproducible"]
    assert msgs, "expected an env_setup_reproducible finding"
    assert "environment setup" in msgs[0].lower()


def test_flags_env_setup_missing_install_step(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "04-development/coding-standards.md": "# Coding Standards",
        "04-development/env-setup.md": (
            "# Env Setup\n"
            "## Prerequisites\nNode 20.\n"
            "## Verify\nRun `npm test`."
        ),
    })
    findings = FindingCollection()
    Phase04Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase04.env_setup_reproducible"]
    assert msgs, "expected an env_setup_reproducible finding when install step missing"
    assert "install" in msgs[0].lower() or "bootstrap" in msgs[0].lower()
