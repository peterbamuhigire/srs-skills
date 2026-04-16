"""Phase 09 - Governance & Compliance gate (ISO/IEC 27001:2022)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.checks.traceability import TraceabilityCheck
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("ISO/IEC 27001:2022", "9")

_PHASE09_DIR_TOKEN = "09-governance-compliance/"
_AUDIT_REPORT_SUFFIX = "09-governance-compliance/audit-report.md"
_RISK_REGISTER_SUFFIXES = (
    "09-governance-compliance/risk-register.md",
    "09-governance-compliance/risk-assessment.md",
)
_PHASE_REF_RE = re.compile(r"\bphase\d{2}\b", re.IGNORECASE)
_RISK_ENTRY_RE = re.compile(
    r"^\s*-\s+\*\*(R-\d{3,5}|RISK-\d{3,5})\*\*", re.MULTILINE
)
_FR_ID_RE = re.compile(r"\bFR-\d{3,5}\b")
_NFR_ID_RE = re.compile(r"\bNFR-\d{3,5}\b")
_CTRL_ID_RE = re.compile(r"\bCTRL-\d{3,5}\b")


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _under_phase09(art: Artifact) -> bool:
    return _PHASE09_DIR_TOKEN in _posix(art.path) or art.phase == "09"


def _find_by_suffix(graph: ArtifactGraph, suffix: str):
    for art in graph.artifacts:
        if _posix(art.path).endswith(suffix):
            return art
    return None


def _find_risk_register(graph: ArtifactGraph):
    for suffix in _RISK_REGISTER_SUFFIXES:
        art = _find_by_suffix(graph, suffix)
        if art is not None:
            return art
    return None


class Phase09Gate(Gate):
    id = "phase09"
    title = "Governance & Compliance phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_traceability(graph, findings)
        self._check_audit_report_present(graph, findings)
        self._check_risk_register_links_to_fr(graph, findings)

    # -- Check 1: traceability (delegates to TraceabilityCheck) ----------
    def _check_traceability(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        tmp = FindingCollection()
        TraceabilityCheck(f"{self.id}.traceability").run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))

    # -- Check 2: audit report present -----------------------------------
    def _check_audit_report_present(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        art = _find_by_suffix(graph, _AUDIT_REPORT_SUFFIX)
        if art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.audit_report_present",
                severity=Severity.HIGH,
                message=(
                    "No audit report found (expected "
                    "'09-governance-compliance/audit-report.md')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if art.body.strip() == "":
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.audit_report_present",
                severity=Severity.HIGH,
                message=f"Audit report '{_posix(art.path)}' is empty",
                location=art.path,
                line=None,
            ), _CLAUSE))
            return
        if not _PHASE_REF_RE.findall(art.body):
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.audit_report_present",
                severity=Severity.HIGH,
                message=(
                    f"Audit report '{_posix(art.path)}' does not list "
                    f"pass/fail status for any phase gate (expected "
                    f"'phaseNN' references)"
                ),
                location=art.path,
                line=None,
            ), _CLAUSE))

    # -- Check 3: risk register links to FR/NFR/CTRL ---------------------
    def _check_risk_register_links_to_fr(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        art = _find_risk_register(graph)
        if art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.risk_register_links_to_fr",
                severity=Severity.HIGH,
                message=(
                    "No risk register found (expected "
                    "'09-governance-compliance/risk-register.md' or "
                    "'risk-assessment.md')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        body = art.body
        for m in _RISK_ENTRY_RE.finditer(body):
            risk_id = m.group(1)
            line_start = body.rfind("\n", 0, m.start()) + 1
            line_end = body.find("\n", m.end())
            if line_end == -1:
                line_end = len(body)
            line_text = body[line_start:line_end]
            if (
                _FR_ID_RE.search(line_text)
                or _NFR_ID_RE.search(line_text)
                or _CTRL_ID_RE.search(line_text)
            ):
                continue
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.risk_register_links_to_fr",
                severity=Severity.HIGH,
                message=(
                    f"Risk {risk_id} in '{_posix(art.path)}' is not "
                    f"linked to any FR-, NFR-, or CTRL- identifier"
                ),
                location=art.path,
                line=None,
            ), _CLAUSE))
