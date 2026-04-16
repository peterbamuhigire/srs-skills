"""Phase 04 - Development Artifacts gate (ISO/IEC/IEEE 12207:2017)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("ISO/IEC/IEEE 12207:2017", "6.4.5")

_PHASE04_DIR_TOKEN = "/04-development/"
_CODING_STANDARDS_SUFFIXES = (
    "coding-standards.md",
    "coding-guidelines.md",
    "style-guide.md",
)


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _find_by_suffix(graph: ArtifactGraph, suffix: str):
    for art in graph.artifacts:
        if _posix(art.path).endswith(suffix):
            return art
    return None


class Phase04Gate(Gate):
    id = "phase04"
    title = "Development Artifacts phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_coding_standards_referenced(graph, findings)

    # -- Check 1: coding standards referenced ----------------------------
    def _check_coding_standards_referenced(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            posix = f"/{_posix(art.path)}"
            if _PHASE04_DIR_TOKEN not in posix:
                continue
            name = art.path.name.lower()
            if name in _CODING_STANDARDS_SUFFIXES:
                return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.coding_standards_referenced",
            severity=Severity.HIGH,
            message=(
                "No coding standards document found under 04-development/ "
                "(expected 'coding-standards.md', 'coding-guidelines.md', "
                "or 'style-guide.md')"
            ),
            location=None,
            line=None,
        ), _CLAUSE))
