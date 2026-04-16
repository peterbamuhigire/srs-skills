"""FRs must follow stimulus -> response with the verb 'shall'."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_FR = re.compile(r"\*\*(FR-\d{3,5})\*\*\s+(.*)")
_SHALL = re.compile(r"\bshall\b", re.IGNORECASE)


class StimulusResponseCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for art in graph.artifacts:
            for lineno, line in enumerate(art.body.splitlines(), start=1):
                m = _FR.search(line)
                if m and not _SHALL.search(m.group(2)):
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{m.group(1)} does not use the prescriptive verb 'shall'",
                        location=art.path,
                        line=lineno,
                    ))
