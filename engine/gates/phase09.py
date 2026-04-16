"""Phase 09 - Governance & Compliance gate (ISO/IEC 27001:2022)."""
from __future__ import annotations
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.checks.traceability import TraceabilityCheck
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("ISO/IEC 27001:2022", "9")

_PHASE09_DIR_TOKEN = "09-governance-compliance/"


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _under_phase09(art: Artifact) -> bool:
    return _PHASE09_DIR_TOKEN in _posix(art.path) or art.phase == "09"


class Phase09Gate(Gate):
    id = "phase09"
    title = "Governance & Compliance phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_traceability(graph, findings)

    # -- Check 1: traceability (delegates to TraceabilityCheck) ----------
    def _check_traceability(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        tmp = FindingCollection()
        TraceabilityCheck(f"{self.id}.traceability").run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))
