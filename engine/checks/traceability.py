"""Traceability check: every FR links upward to a BG and downward to a TC."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

class TraceabilityCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        all_text = "\n".join(a.body for a in graph.artifacts)
        all_ids = set(graph.all_identifiers())
        frs = {i for i in all_ids if i.startswith("FR-")}
        bgs = {i for i in all_ids if i.startswith("BG-")}
        for fr in sorted(frs):
            mentioned_with_bg = re.search(rf"{re.escape(fr)}.*BG-\d+|BG-\d+.*{re.escape(fr)}", all_text)
            if not mentioned_with_bg or not bgs:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any business goal",
                    location=None, line=None,
                ))
            mentioned_with_tc = re.search(rf"TC-\d+.*{re.escape(fr)}|{re.escape(fr)}.*TC-\d+", all_text)
            if not mentioned_with_tc:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any test case",
                    location=None, line=None,
                ))
