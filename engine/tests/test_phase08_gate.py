from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.phase08 import Phase08Gate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


# -- user_manual_has_screenshots -------------------------------------------

def test_passes_when_user_manual_has_screenshots(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/user-manual.md": (
            "# User Manual\n"
            "\n"
            "## Login\n"
            "\n"
            "![Login screen](images/login.png)\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    assert findings.for_gate("phase08.user_manual_has_screenshots") == []


def test_flags_missing_user_manual(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/faq.md": "# FAQ",
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.user_manual_has_screenshots"]
    assert msgs, "expected a user_manual_has_screenshots finding"
    assert "No user manual found" in msgs[0]


def test_flags_user_manual_without_screenshots(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/user-manual.md": (
            "# User Manual\n"
            "\n"
            "## Login\n"
            "\n"
            "Follow these steps to sign in.\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.user_manual_has_screenshots"]
    assert msgs, "expected a user_manual_has_screenshots finding"
    assert "has no screenshots" in msgs[0]


# -- release_notes_link_to_fr ----------------------------------------------

def test_passes_when_release_notes_cite_fr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/user-manual.md": (
            "# User Manual\n![Home](images/home.png)\n"
        ),
        "08-end-user-documentation/release-notes.md": (
            "# Release Notes v1.0\n"
            "\n"
            "- Added scoring workflow (FR-0101).\n"
            "- Added reviewer assignment (FR-0102).\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    assert findings.for_gate("phase08.release_notes_link_to_fr") == []


def test_flags_missing_release_notes(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/user-manual.md": (
            "# User Manual\n![Home](images/home.png)\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.release_notes_link_to_fr"]
    assert msgs, "expected a release_notes_link_to_fr finding"
    assert "No release notes found" in msgs[0]


def test_flags_release_notes_without_fr(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/release-notes.md": (
            "# Release Notes v1.0\n"
            "\n"
            "- Minor UI polish.\n"
            "- Performance improvements.\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.release_notes_link_to_fr"]
    assert msgs, "expected a release_notes_link_to_fr finding"
    assert "no FR-* traceability links" in msgs[0]
