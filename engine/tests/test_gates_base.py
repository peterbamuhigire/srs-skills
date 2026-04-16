from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate, GateRegistry

class _AlwaysFails(Gate):
    id = "test.always_fails"
    title = "Always fails"
    severity = Severity.HIGH
    def evaluate(self, graph, findings):
        findings.add(Finding(self.id, self.severity, "synthetic", None, None))

def test_registry_collects_gates_by_id():
    reg = GateRegistry()
    reg.register(_AlwaysFails())
    assert "test.always_fails" in reg

def test_registry_runs_gates(tiny_project: Path):
    ws = Workspace.load(tiny_project)
    graph = ArtifactGraph.build(ws)
    reg = GateRegistry()
    reg.register(_AlwaysFails())
    findings = FindingCollection()
    reg.run_all(graph, findings)
    assert len(findings.for_gate("test.always_fails")) == 1
