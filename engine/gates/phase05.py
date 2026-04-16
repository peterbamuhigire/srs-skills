"""Phase 05 - Testing Documentation gate (BS ISO/IEC/IEEE 29119-3:2013)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("BS ISO/IEC/IEEE 29119-3:2013", "7.2")

_REQUIRED_TC_KEYS = ("inputs", "expected_results", "requirement_trace")
_REQUIRED_EVIDENCE_SUFFIX = "05-testing-documentation/29119-deterministic-checks.md"
_EXIT_REPORT_SUFFIX = "test-completion-report.md"
_MATRIX_SUFFIX = "coverage-matrix.md"
_FR_ID = re.compile(r"\bFR-\d+\b")
_TC_PREFIX = "TC-"
_FR_PREFIX = "FR-"


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _find_by_suffix(graph: ArtifactGraph, suffix: str):
    for art in graph.artifacts:
        if _posix(art.path).endswith(suffix):
            return art
    return None


class Phase05Gate(Gate):
    id = "phase05"
    title = "Testing Documentation phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_normative_test_structure(graph, findings)
        self._check_required_evidence(graph, findings)
        self._check_coverage_measurable(graph, findings)
        self._check_exit_evidence(graph, findings)

    # -- Check 1: normative test structure -------------------------------
    def _check_normative_test_structure(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            if art.phase != "05":
                continue
            missing = [k for k in _REQUIRED_TC_KEYS if k not in art.frontmatter]
            if missing:
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.normative_test_structure",
                    severity=Severity.HIGH,
                    message=(
                        f"Test artifact missing required frontmatter keys: "
                        f"{', '.join(missing)}"
                    ),
                    location=art.path,
                    line=None,
                ), _CLAUSE))

    # -- Check 2: required evidence --------------------------------------
    def _check_required_evidence(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        art = _find_by_suffix(graph, _REQUIRED_EVIDENCE_SUFFIX)
        if art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.required_evidence",
                severity=Severity.HIGH,
                message=(
                    f"Missing required evidence file: {_REQUIRED_EVIDENCE_SUFFIX}"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if art.body.strip() == "":
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.required_evidence",
                severity=Severity.HIGH,
                message=(
                    f"Required evidence file is empty: {_REQUIRED_EVIDENCE_SUFFIX}"
                ),
                location=art.path,
                line=None,
            ), _CLAUSE))

    # -- Check 3: coverage measurable ------------------------------------
    def _check_coverage_measurable(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        ids = graph.all_identifiers()
        tc_count = sum(1 for i in ids if i.startswith(_TC_PREFIX))
        fr_count = sum(1 for i in ids if i.startswith(_FR_PREFIX))
        matrix = _find_by_suffix(graph, _MATRIX_SUFFIX)
        if tc_count >= fr_count or matrix is not None:
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.coverage_measurable",
            severity=Severity.HIGH,
            message=(
                f"Requirement coverage not measurable: {tc_count} TC-* "
                f"versus {fr_count} FR-*, and no coverage-matrix.md present"
            ),
            location=None,
            line=None,
        ), _CLAUSE))

    # -- Check 4: exit evidence ------------------------------------------
    def _check_exit_evidence(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        art = _find_by_suffix(graph, _EXIT_REPORT_SUFFIX)
        if art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.exit_evidence",
                severity=Severity.HIGH,
                message=(
                    f"Missing exit evidence file: {_EXIT_REPORT_SUFFIX}"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        body = art.body
        lower = body.lower()
        missing = []
        if "tested" not in lower:
            missing.append("'tested'")
        if "result" not in lower:
            missing.append("'result'")
        if not _FR_ID.search(body):
            missing.append("at least one FR-<n> reference")
        if missing:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.exit_evidence",
                severity=Severity.HIGH,
                message=(
                    f"{_EXIT_REPORT_SUFFIX} is missing required content: "
                    f"{', '.join(missing)}"
                ),
                location=art.path,
                line=None,
            ), _CLAUSE))
