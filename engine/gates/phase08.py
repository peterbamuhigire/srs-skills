"""Phase 08 - End-User Documentation gate (IEEE Std 26514-2022)."""
from __future__ import annotations
import re
from engine.artifact_graph import Artifact, ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.gates._shared import ClauseRef, attach_clause

_CLAUSE = ClauseRef("IEEE Std 26514-2022", "8")

_PHASE08_DIR_TOKEN = "08-end-user-documentation/"

_USER_MANUAL_NAME_TOKENS = ("user-manual", "user-guide", "manual")
_IMAGE_REF_RE = re.compile(r"!\[[^\]]*\]\([^)]+\)")
_FR_ID_RE = re.compile(r"\bFR-\d{3,5}\b")


def _posix(path) -> str:
    return str(path).replace("\\", "/")


def _under_phase08(art: Artifact) -> bool:
    return _PHASE08_DIR_TOKEN in _posix(art.path) or art.phase == "08"


def _find_user_manual(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase08(art):
            continue
        name = art.path.name.lower()
        if any(tok in name for tok in _USER_MANUAL_NAME_TOKENS):
            return art
    return None


def _find_release_notes(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase08(art):
            continue
        name = art.path.name.lower()
        if "release-notes" in name or name == "changelog.md" or name == "release.md":
            return art
    return None


class Phase08Gate(Gate):
    id = "phase08"
    title = "End-User Documentation phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_user_manual_has_screenshots(graph, findings)
        self._check_release_notes_link_to_fr(graph, findings)

    # -- Check 1: user manual has screenshots ----------------------------
    def _check_user_manual_has_screenshots(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        manual = _find_user_manual(graph)
        if manual is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.user_manual_has_screenshots",
                severity=Severity.HIGH,
                message=(
                    "No user manual found under 08-end-user-documentation/ "
                    "(expected filename containing 'user-manual', "
                    "'user-guide', or 'manual')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        images = _IMAGE_REF_RE.findall(manual.body)
        if images:
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.user_manual_has_screenshots",
            severity=Severity.HIGH,
            message=(
                f"User manual '{_posix(manual.path)}' has no screenshots "
                f"(expected markdown image references: ![alt](path))"
            ),
            location=manual.path,
            line=None,
        ), _CLAUSE))

    # -- Check 2: release notes link to FR -------------------------------
    def _check_release_notes_link_to_fr(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        notes = _find_release_notes(graph)
        if notes is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.release_notes_link_to_fr",
                severity=Severity.HIGH,
                message=(
                    "No release notes found under "
                    "08-end-user-documentation/ (expected filename "
                    "containing 'release-notes', 'changelog.md', or "
                    "'release.md')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        if _FR_ID_RE.search(notes.body):
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.release_notes_link_to_fr",
            severity=Severity.HIGH,
            message=(
                f"Release notes '{_posix(notes.path)}' have no FR-* "
                f"traceability links"
            ),
            location=notes.path,
            line=None,
        ), _CLAUSE))
