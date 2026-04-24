"""Functional requirements should be observable and narrowly scoped."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_FR = re.compile(r"\*\*(FR-\d{3,5})\*\*\s+(.*)")
_OBSERVABLE_VERB = re.compile(
    r"\b("
    r"accept|store|display|send|create|update|delete|return|record|"
    r"calculate|generate|queue|reject|validate|notify|log|allow|deny|"
    r"encrypt|decrypt|sync|export|import|archive|restore|capture|issue|"
    r"assign|mark|publish|submit|approve|reconcile|retry|persist|render|"
    r"show|fulfil|enforce|append|schedule|require|authenticate|authorise|"
    r"authorize|support"
    r")\b",
    re.IGNORECASE,
)
_WEAK = re.compile(
    r"\b(user[- ]friendly|easy to use|appropriate|sufficient|etc\.?|and/or)\b",
    re.IGNORECASE,
)
_SHALL = re.compile(r"\bshall\b", re.IGNORECASE)


class RequirementSemanticsCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        for art in graph.artifacts:
            for lineno, line in enumerate(art.body.splitlines(), start=1):
                m = _FR.search(line)
                if not m:
                    continue
                fr_id, text = m.group(1), m.group(2).strip()
                lowered = text.lower()
                if not _SHALL.search(text):
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{fr_id} is not written as a normative requirement using 'shall'",
                        location=art.path,
                        line=lineno,
                    ))
                    continue
                weak = _WEAK.search(text)
                if weak:
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{fr_id} uses ambiguous phrase '{weak.group(0)}'",
                        location=art.path,
                        line=lineno,
                    ))
                if not _OBSERVABLE_VERB.search(text):
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{fr_id} does not state an observable system behaviour",
                        location=art.path,
                        line=lineno,
                    ))
                if lowered.count(" shall ") > 1 or " and/or " in lowered:
                    findings.add(Finding(
                        gate_id=self.gate_id,
                        severity=Severity.HIGH,
                        message=f"{fr_id} appears to combine multiple behaviours in one requirement",
                        location=art.path,
                        line=lineno,
                    ))
