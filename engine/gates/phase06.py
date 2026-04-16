"""Phase 06 - Deployment & Operations gate (IEEE Std 1062-2015)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("IEEE Std 1062-2015", "6.3")

_PHASE06_DIR_TOKEN = "06-deployment-operations/"

_DEPLOYMENT_GUIDE_NAMES = ("deployment-guide.md", "deployment.md")

_ROLLBACK_RE = re.compile(r"\b(rollback|roll\s+back)\b", re.IGNORECASE)


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _under_phase06(art: Artifact) -> bool:
    return _PHASE06_DIR_TOKEN in _posix(art.path)


def _find_deployment_guide(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase06(art):
            continue
        if art.path.name.lower() in _DEPLOYMENT_GUIDE_NAMES:
            return art
    return None


class Phase06Gate(Gate):
    id = "phase06"
    title = "Deployment & Operations phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_deployment_guide_has_rollback(graph, findings)

    # -- Check 1: deployment guide has rollback --------------------------
    def _check_deployment_guide_has_rollback(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        guide = _find_deployment_guide(graph)
        if guide is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.deployment_guide_has_rollback",
                severity=Severity.HIGH,
                message=(
                    "No deployment guide found under "
                    "06-deployment-operations/ (expected "
                    "'deployment-guide.md' or 'deployment.md')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if _ROLLBACK_RE.search(guide.body):
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.deployment_guide_has_rollback",
            severity=Severity.HIGH,
            message=(
                f"Deployment guide '{_posix(guide.path)}' has no "
                f"rollback procedure"
            ),
            location=guide.path,
            line=None,
        ), _CLAUSE))
