"""Reusable check: no unresolved fail markers."""
from __future__ import annotations
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate

_BLOCKING_TAGS = {
    "V&V-FAIL", "CONTEXT-GAP", "GLOSSARY-GAP",
    "SMART-FAIL", "TRACE-GAP", "VERIFIABILITY-FAIL",
    "DPPA-FAIL", "CONTROL-GAP",
}

class NoUnresolvedFailMarkersGate(Gate):
    id = "kernel.no_unresolved_fail_markers"
    title = "No unresolved [V&V-FAIL]/[CONTEXT-GAP]/etc. markers"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for path, marker in graph.all_markers():
            if marker.tag not in _BLOCKING_TAGS:
                continue
            findings.add(Finding(
                gate_id=self.id,
                severity=self.severity,
                message=f"Unresolved [{marker.tag}: {marker.reason}]",
                location=path,
                line=marker.line,
            ))
