"""Phase 03 - Design Documentation gate (ISO/IEC/IEEE 42010:2011)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("ISO/IEC/IEEE 42010:2011", "5.3")

_ADR_DIR_TOKEN = "/adr/"
_ADR_ID_PREFIX = "ADR-"
_API_SPEC_TOKENS = ("/03-api-specification/", "/api-specification/")
_DB_DESIGN_TOKENS = ("/04-database-design/", "/database-design/")
_PHASE03_ROOT = "03-design-documentation/"
_THREAT_MODEL_SUFFIX = "threat-model.md"
_IOT_DIR_TOKEN = "/07-iot-system-design/"
_IOT_ROOT = "07-iot-system-design/"
_SIGNAL_INVENTORY_SUFFIXES = ("signal-inventory.md", "signals.md")
_NFR_PREFIX = "NFR-"

_HTTP_METHOD_RE = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE)\b")
_RESPONSE_RE = re.compile(
    r"(response|status|\b200\b|\b201\b|\b204\b|\b400\b|\b404\b|\b500\b)",
    re.IGNORECASE,
)
_PRIMARY_KEY_RE = re.compile(r"\b(PRIMARY KEY|primary\s+key|\bPK\b)\b")


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _find_by_suffix(graph: ArtifactGraph, suffix: str):
    for art in graph.artifacts:
        if _posix(art.path).endswith(suffix):
            return art
    return None


class Phase03Gate(Gate):
    id = "phase03"
    title = "Design Documentation phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_architecture_decisions_recorded(graph, findings)
        self._check_interfaces_have_contracts(graph, findings)

    # -- Check 1: architecture decisions recorded ------------------------
    def _check_architecture_decisions_recorded(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            if _ADR_DIR_TOKEN in f"/{_posix(art.path)}":
                return
        for ident in graph.all_identifiers():
            if ident.startswith(_ADR_ID_PREFIX):
                return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.architecture_decisions_recorded",
            severity=Severity.HIGH,
            message=(
                "No Architecture Decision Records found: expected an "
                "'adr/' directory or ADR-### identifiers in design artifacts"
            ),
            location=None,
            line=None,
        ), _CLAUSE))

    # -- Check 2: interfaces have contracts ------------------------------
    def _check_interfaces_have_contracts(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            posix = f"/{_posix(art.path)}"
            if not any(tok in posix for tok in _API_SPEC_TOKENS):
                continue
            missing = []
            if not _HTTP_METHOD_RE.search(art.body):
                missing.append("HTTP method")
            if not _RESPONSE_RE.search(art.body):
                missing.append("response/status")
            if missing:
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.interfaces_have_contracts",
                    severity=Severity.HIGH,
                    message=(
                        f"API spec '{_posix(art.path)}' missing required "
                        f"contract fields: {', '.join(missing)}"
                    ),
                    location=art.path,
                    line=None,
                ), _CLAUSE))
