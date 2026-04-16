"""Phase 09 - Governance & Compliance gate (ISO/IEC 27001:2022)."""
from __future__ import annotations
import re
from pathlib import Path
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.checks.controls import ControlsCheck
from engine.checks.glossary_registry import GlossaryRegistryCheck
from engine.checks.identifier_registry import IdentifierRegistryCheck
from engine.checks.nfr_threshold_dedup import NfrThresholdDedupCheck
from engine.checks.obligations import ObligationsCheck
from engine.checks.traceability import TraceabilityCheck
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause
from engine.waivers import WaiverRegister

_CLAUSE = ClauseRef("ISO/IEC 27001:2022", "9")

_REPO_ROOT = Path(__file__).resolve().parents[2]
_KNOWN_DOMAINS = (
    "agriculture", "education", "finance", "government",
    "healthcare", "logistics", "retail", "uganda",
)
_DOMAIN_LINE_RE = re.compile(r"domain\s*[:=]\s*([A-Za-z][A-Za-z0-9_\-]*)", re.IGNORECASE)


def _detect_domain(project_root: Path) -> str | None:
    domain_file = project_root / "_context" / "domain.md"
    if not domain_file.exists():
        return None
    body = domain_file.read_text(encoding="utf-8")
    for m in _DOMAIN_LINE_RE.finditer(body):
        candidate = m.group(1).lower()
        if candidate in _KNOWN_DOMAINS:
            return candidate
    lowered = body.lower()
    for dom in _KNOWN_DOMAINS:
        if dom in lowered:
            return dom
    return None

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
        self._check_waivers_have_expiry(graph, findings)
        self._check_identifier_registry(graph, findings)
        self._check_glossary_registry(graph, findings)
        self._check_nfr_threshold_dedup(graph, findings)
        self._check_controls(graph, findings)
        self._check_obligations(graph, findings)

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

    # -- Check 4: waivers have expiry within 90 days ---------------------
    def _check_waivers_have_expiry(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        if graph.root is None:
            return
        waivers_path = graph.root / "_registry" / "waivers.yaml"
        if not waivers_path.exists():
            return
        register = WaiverRegister.load(waivers_path)
        for waiver in register:
            delta = (waiver.expires_on - waiver.approved_on).days
            if delta < 0:
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.waivers_have_expiry",
                    severity=Severity.HIGH,
                    message=(
                        f"Waiver '{waiver.id}' has expiry before approval "
                        f"date ({waiver.approved_on} \u2192 "
                        f"{waiver.expires_on})"
                    ),
                    location=Path("_registry/waivers.yaml"),
                    line=None,
                ), _CLAUSE))
            elif delta > 90:
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.waivers_have_expiry",
                    severity=Severity.HIGH,
                    message=(
                        f"Waiver '{waiver.id}' has expiry {delta} days "
                        f"after approval (max allowed: 90)"
                    ),
                    location=Path("_registry/waivers.yaml"),
                    line=None,
                ), _CLAUSE))

    # -- Check 5: identifier registry (delegates to IdentifierRegistryCheck) -
    def _check_identifier_registry(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        if graph.root is None:
            return
        registry_path = graph.root / "_registry" / "identifiers.yaml"
        if not registry_path.exists():
            return
        tmp = FindingCollection()
        IdentifierRegistryCheck(
            f"{self.id}.id_registry", registry_path
        ).run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))

    # -- Check 6: glossary registry (delegates to GlossaryRegistryCheck) -----
    def _check_glossary_registry(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        if graph.root is None:
            return
        registry_path = graph.root / "_registry" / "glossary.yaml"
        if not registry_path.exists():
            return
        tmp = FindingCollection()
        GlossaryRegistryCheck(
            f"{self.id}.glossary_registry", registry_path
        ).run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))

    # -- Check 7: NFR threshold dedup (delegates to NfrThresholdDedupCheck) --
    def _check_nfr_threshold_dedup(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        tmp = FindingCollection()
        NfrThresholdDedupCheck(
            f"{self.id}.nfr_threshold_dedup"
        ).run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))

    # -- Check 8: domain control selection (delegates to ControlsCheck) ------
    def _check_controls(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        if graph.root is None:
            return
        domain = _detect_domain(graph.root)
        if domain is None:
            return
        domain_register = (
            _REPO_ROOT / "domains" / domain / "controls" / "control-register.yaml"
        )
        if not domain_register.exists():
            return
        tmp = FindingCollection()
        ControlsCheck(
            f"{self.id}.controls", graph.root, domain_register
        ).run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))

    # -- Check 9: regulatory obligations (delegates to ObligationsCheck) -----
    def _check_obligations(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        if graph.root is None:
            return
        domain = _detect_domain(graph.root)
        if domain is None:
            return
        obligations_file = (
            _REPO_ROOT / "domains" / domain / "controls" / "obligations.yaml"
        )
        if not obligations_file.exists():
            return
        tmp = FindingCollection()
        ObligationsCheck(
            f"{self.id}.obligations", graph.root, obligations_file
        ).run(graph, tmp)
        for f in tmp:
            findings.add(attach_clause(f, _CLAUSE))
