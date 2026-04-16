"""Phase 07 - Agile Artifacts gate (PMBOK Guide 7th Edition)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("PMBOK Guide 7th Edition", "2.6")

_PHASE07_DIR_TOKEN = "07-agile-artifacts/"

_DOR_NAME_RE = re.compile(r"\b(definition-of-ready|dor)\b", re.IGNORECASE)
_DOD_NAME_RE = re.compile(r"\b(definition-of-done|dod)\b", re.IGNORECASE)
_BASELINE_ID_RE = re.compile(
    r"\bBG-\d{3,5}\b|\bFR-\d{3,5}\b|\bF-\d+\b|\bNFR-\d{3,5}\b"
)
_DOD_SIGNAL_RE = re.compile(
    r"\bCTRL-\d{3,5}\b"
    r"|\bcompliance\b"
    r"|\bsecurity[- ]review\b"
    r"|\baccessibility\b"
    r"|\bWCAG\b"
    r"|\bISO\s*/?\s*IEC\b"
    r"|\bIEEE\s+\d+\b"
    r"|\bGDPR\b|\bHIPAA\b|\bPCI[- ]DSS\b|\bDPPA\b",
    re.IGNORECASE,
)


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _under_phase07(art: Artifact) -> bool:
    return _PHASE07_DIR_TOKEN in _posix(art.path) or art.phase == "07"


def _find_dor(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase07(art):
            continue
        if _DOR_NAME_RE.search(art.path.name):
            return art
    return None


def _find_dod(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase07(art):
            continue
        if _DOD_NAME_RE.search(art.path.name):
            return art
    return None


class Phase07Gate(Gate):
    id = "phase07"
    title = "Agile Artifacts phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_dor_references_baseline(graph, findings)
        self._check_dod_references_compliance(graph, findings)

    # -- Check 1: DoR references baseline --------------------------------
    def _check_dor_references_baseline(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        dor = _find_dor(graph)
        if dor is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.dor_references_baseline",
                severity=Severity.HIGH,
                message=(
                    "No Definition of Ready document found under "
                    "07-agile-artifacts/ (expected filename containing "
                    "'definition-of-ready' or 'DoR')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if _BASELINE_ID_RE.search(dor.body):
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.dor_references_baseline",
            severity=Severity.HIGH,
            message=(
                f"Definition of Ready '{_posix(dor.path)}' does not "
                f"reference any baseline ID (expected BG-, FR-, NFR-, "
                f"or F- identifier)"
            ),
            location=dor.path,
            line=None,
        ), _CLAUSE))

    # -- Check 2: DoD references compliance ------------------------------
    def _check_dod_references_compliance(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        dod = _find_dod(graph)
        if dod is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.dod_references_compliance",
                severity=Severity.HIGH,
                message=(
                    "No Definition of Done document found under "
                    "07-agile-artifacts/ (expected filename containing "
                    "'definition-of-done' or 'DoD')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if _DOD_SIGNAL_RE.search(dod.body):
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.dod_references_compliance",
            severity=Severity.HIGH,
            message=(
                f"Definition of Done '{_posix(dod.path)}' does not "
                f"reference any compliance or quality standard "
                f"(expected CTRL-*, 'compliance', 'security review', "
                f"'WCAG', 'ISO/IEC', 'IEEE ###', or a named regulation)"
            ),
            location=dod.path,
            line=None,
        ), _CLAUSE))
