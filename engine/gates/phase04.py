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
_ENV_SETUP_SUFFIXES = (
    "env-setup.md",
    "environment-setup.md",
    "setup.md",
    "development-environment.md",
)
_ENV_PREREQ_MARKERS = ("prerequisites", "requires", "dependencies")
_ENV_INSTALL_MARKERS = ("install", "bootstrap")
_ENV_VERIFY_MARKERS = ("verify", "test", "check", "validate")

_TECH_SPEC_NAME_TOKENS = ("tech-spec", "technical-specification")
_FR_REF_RE = re.compile(r"\bFR-\d{3,5}\b")

_CONTRIB_GUIDE_SUFFIXES = (
    "contributing.md",
    "contribution-guide.md",
    "contrib.md",
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
        self._check_env_setup_reproducible(graph, findings)
        self._check_tech_spec_links_to_fr(graph, findings)
        self._check_contrib_guide_present(graph, findings)

    # -- Check 1: coding standards referenced ----------------------------
    def _check_coding_standards_referenced(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            posix = f"/{_posix(art.path).lower()}"
            if _PHASE04_DIR_TOKEN not in posix:
                continue
            if any(posix.endswith("/" + sfx) for sfx in _CODING_STANDARDS_SUFFIXES):
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

    # -- Check 2: env setup reproducible ---------------------------------
    def _check_env_setup_reproducible(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        env_art = None
        for art in graph.artifacts:
            posix_lower = f"/{_posix(art.path).lower()}"
            if _PHASE04_DIR_TOKEN not in posix_lower:
                continue
            if any(posix_lower.endswith("/" + sfx) for sfx in _ENV_SETUP_SUFFIXES):
                env_art = art
                break
        if env_art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.env_setup_reproducible",
                severity=Severity.HIGH,
                message=(
                    "No environment setup document found under "
                    "04-development/ (expected 'env-setup.md', "
                    "'environment-setup.md', 'setup.md', or "
                    "'development-environment.md')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        lower = env_art.body.lower()
        missing_parts = []
        if not any(m in lower for m in _ENV_PREREQ_MARKERS):
            missing_parts.append("prerequisites/requirements/dependencies")
        if not any(m in lower for m in _ENV_INSTALL_MARKERS):
            missing_parts.append("install/bootstrap instructions")
        if not any(m in lower for m in _ENV_VERIFY_MARKERS):
            missing_parts.append("verification steps")
        if missing_parts:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.env_setup_reproducible",
                severity=Severity.HIGH,
                message=(
                    f"Environment setup '{_posix(env_art.path)}' is "
                    f"incomplete: missing {', '.join(missing_parts)}"
                ),
                location=env_art.path,
                line=None,
            ), _CLAUSE))

    # -- Check 3: tech spec links to FR ----------------------------------
    def _check_tech_spec_links_to_fr(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            posix_lower = f"/{_posix(art.path).lower()}"
            if _PHASE04_DIR_TOKEN not in posix_lower:
                continue
            name = art.path.name.lower()
            if not any(tok in name for tok in _TECH_SPEC_NAME_TOKENS):
                continue
            if _FR_REF_RE.search(art.body):
                continue
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.tech_spec_links_to_fr",
                severity=Severity.HIGH,
                message=(
                    f"Technical specification '{_posix(art.path)}' has "
                    f"no FR-* traceability links"
                ),
                location=art.path,
                line=None,
            ), _CLAUSE))

    # -- Check 4: contribution guide present -----------------------------
    def _check_contrib_guide_present(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for art in graph.artifacts:
            if art.path.name.lower() in _CONTRIB_GUIDE_SUFFIXES:
                return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.contrib_guide_present",
            severity=Severity.HIGH,
            message=(
                "No contribution guide found (expected 'CONTRIBUTING.md', "
                "'contribution-guide.md', or 'contrib.md')"
            ),
            location=None,
            line=None,
        ), _CLAUSE))
