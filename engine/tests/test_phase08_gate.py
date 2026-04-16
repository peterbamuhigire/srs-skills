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


# -- faq_has_at_least_5_qa -------------------------------------------------

def test_passes_when_faq_has_five_qa_headings(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/faq.md": (
            "# FAQ\n"
            "\n"
            "## How do I reset my password?\n"
            "Use the reset link on the login screen.\n"
            "\n"
            "## How do I contact support?\n"
            "Email support@example.com.\n"
            "\n"
            "## Where is my data stored?\n"
            "Data is stored in a Uganda-based data centre.\n"
            "\n"
            "## How do I export my records?\n"
            "Use the Export button on the Reports screen.\n"
            "\n"
            "## Can I use the system offline?\n"
            "No, an internet connection is required.\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    assert findings.for_gate("phase08.faq_has_at_least_5_qa") == []


def test_passes_when_faq_has_five_bold_q_markers(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/faq.md": (
            "# FAQ\n"
            "\n"
            "**Q1: How do I reset my password?**\n"
            "Use the reset link.\n"
            "\n"
            "**Q2: How do I contact support?**\n"
            "Email support.\n"
            "\n"
            "**Q3: Where is my data stored?**\n"
            "Uganda data centre.\n"
            "\n"
            "**Q4: How do I export records?**\n"
            "Export button.\n"
            "\n"
            "**Q5: Can I use offline?**\n"
            "No.\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    assert findings.for_gate("phase08.faq_has_at_least_5_qa") == []


def test_flags_missing_faq(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/user-manual.md": (
            "# User Manual\n![Home](images/home.png)\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.faq_has_at_least_5_qa"]
    assert msgs, "expected a faq_has_at_least_5_qa finding"
    assert "No FAQ found" in msgs[0]


def test_flags_faq_with_three_questions(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
        "08-end-user-documentation/faq.md": (
            "# FAQ\n"
            "\n"
            "## How do I reset my password?\n"
            "Use the reset link.\n"
            "\n"
            "## How do I contact support?\n"
            "Email support.\n"
            "\n"
            "## Where is my data stored?\n"
            "Uganda data centre.\n"
        ),
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    msgs = [f.message for f in findings
            if f.gate_id == "phase08.faq_has_at_least_5_qa"]
    assert msgs, "expected a faq_has_at_least_5_qa finding"
    assert "has 3 question(s)" in msgs[0]
    assert "at least 5 required" in msgs[0]


# -- clause attachment ------------------------------------------------------

def test_findings_carry_ieee_26514_clause_label(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# Vision",
    })
    findings = FindingCollection()
    Phase08Gate().evaluate(graph, findings)
    assert len(findings) > 0
    for f in findings:
        assert "IEEE Std 26514-2022" in f.message
        assert "8" in f.message
