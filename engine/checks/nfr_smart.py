"""SMART NFR check: every NFR must have a measurable metric + threshold."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_VAGUE = re.compile(r"\b(fast|intuitive|reliable|robust|seamless|user[- ]friendly|scalable)\b", re.IGNORECASE)
_METRIC = re.compile(r"(?:≤|<=|≥|>=|<|>|=)\s*\d+(\.\d+)?\s*(ms|s|min|MB|GB|%|req/s|RPS|users)", re.IGNORECASE)
_NFR_LINE = re.compile(r"\*\*(NFR-\d{3,5})\*\*\s+(.*)")

class SmartNfrCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for art in graph.artifacts:
            for lineno, line in enumerate(art.body.splitlines(), start=1):
                m = _NFR_LINE.search(line)
                if not m:
                    continue
                nfr_id, text = m.group(1), m.group(2)
                vague = _VAGUE.search(text)
                metric = _METRIC.search(text)
                if vague and not metric:
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{nfr_id} uses vague adjective '{vague.group(0)}' with no metric/threshold",
                        location=art.path,
                        line=lineno,
                    ))
