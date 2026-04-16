from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.gates.hybrid import HybridSyncGate


def _ws(tmp_path, files):
    for rel, body in files.items():
        full = tmp_path / rel
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


def test_gate_is_noop_when_methodology_not_hybrid(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# V",
        "_context/methodology.md": "---\nmethodology: waterfall\n---\n# Method",
    })
    findings = FindingCollection()
    HybridSyncGate(tmp_path).evaluate(graph, findings)
    assert len(findings) == 0


def test_gate_runs_traces_check_when_hybrid(tmp_path):
    graph = _ws(tmp_path, {
        "_context/vision.md": "# V",
        "_context/methodology.md": "---\nmethodology: hybrid\n---\n# Method",
        "07-agile-artifacts/definitions/dor-dod.md": "# DoR/DoD\nTraces FR-001.",
    })
    findings = FindingCollection()
    HybridSyncGate(tmp_path).evaluate(graph, findings)
    msgs = [f.message for f in findings]
    # No baseline-trace.yaml exists -> HybridTracesCheck emits "missing"
    assert any("missing" in m.lower() for m in msgs)


def test_gate_flags_missing_dor_dod(tmp_path):
    # Baseline trace file exists and is valid.
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/baseline-trace.yaml").write_text(
        "baseline:\n  - id: FR-001\n    locked_on: 2026-04-01\n    change_control_body: SC\n"
        "stories:\n  - id: US-001\n    traces: [FR-001]\n",
        encoding="utf-8",
    )
    graph = _ws(tmp_path, {
        "_context/vision.md": "# V",
        "_context/methodology.md": "---\nmethodology: hybrid\n---\n# Method",
    })
    findings = FindingCollection()
    HybridSyncGate(tmp_path).evaluate(graph, findings)
    msgs = [f.message for f in findings]
    assert any("dor-dod.md" in m.lower() for m in msgs)


def test_gate_flags_decoupled_dor_dod(tmp_path):
    (tmp_path / "_registry").mkdir()
    (tmp_path / "_registry/baseline-trace.yaml").write_text(
        "baseline:\n  - id: FR-001\n    locked_on: 2026-04-01\n    change_control_body: SC\n"
        "stories:\n  - id: US-001\n    traces: [FR-001]\n",
        encoding="utf-8",
    )
    graph = _ws(tmp_path, {
        "_context/vision.md": "# V",
        "_context/methodology.md": "---\nmethodology: hybrid\n---\n# Method",
        "07-agile-artifacts/definitions/dor-dod.md": "# DoR/DoD\nGeneric rules, no IDs.",
    })
    findings = FindingCollection()
    HybridSyncGate(tmp_path).evaluate(graph, findings)
    msgs = [f.message for f in findings]
    joined = " ".join(msgs).lower()
    assert "decoupled" in joined or "does not reference" in joined
