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
_SPRINT_PREFIX_RE = re.compile(r"sprint-\d+", re.IGNORECASE)
_BULLET_LINE_RE = re.compile(r"^- +")
_BULLET_ID_RE = re.compile(r"\*\*([A-Z]{2,5}-\d{3,5})\*\*")
_RETRO_ACTION_RE = re.compile(
    r"^\s*-\s+\*\*((?:A|ACTION|RETRO)-\d+)\*\*"
)
_OWNER_WORD_RE = re.compile(r"\bowner\s*:\s*\S+", re.IGNORECASE)
_HANDLE_RE = re.compile(r"@\w+")
_DUE_WORD_RE = re.compile(r"\bdue\b", re.IGNORECASE)
_ISO_DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_VELOCITY_NAME_TOKENS = ("velocity", "sprint-metrics", "sprint-history")
_SPRINT_REF_RE = re.compile(r"\bsprint[- ]\d+\b", re.IGNORECASE)


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


def _is_sprint_artifact(art: Artifact) -> bool:
    name = art.path.name.lower()
    if "sprint-plan" in name or "sprint-backlog" in name:
        return True
    if _SPRINT_PREFIX_RE.match(name):
        return True
    return False


def _find_sprint_artifacts(graph: ArtifactGraph):
    out = []
    for art in graph.artifacts:
        if not _under_phase07(art):
            continue
        if _is_sprint_artifact(art):
            out.append(art)
    return out


def _find_retro_artifacts(graph: ArtifactGraph):
    out = []
    for art in graph.artifacts:
        if not _under_phase07(art):
            continue
        name = art.path.name.lower()
        if "retrospective" in name or "retro" in name:
            out.append(art)
    return out


def _find_velocity_artifact(graph: ArtifactGraph):
    for art in graph.artifacts:
        if not _under_phase07(art):
            continue
        name = art.path.name.lower()
        if any(tok in name for tok in _VELOCITY_NAME_TOKENS):
            return art
    return None


class Phase07Gate(Gate):
    id = "phase07"
    title = "Agile Artifacts phase gate"
    severity = Severity.HIGH

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        self._check_dor_references_baseline(graph, findings)
        self._check_dod_references_compliance(graph, findings)
        self._check_sprint_artifacts_have_ids(graph, findings)
        self._check_retro_actions_assigned(graph, findings)
        self._check_velocity_history_present(graph, findings)

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

    # -- Check 3: sprint artifacts have IDs ------------------------------
    def _check_sprint_artifacts_have_ids(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        sprint_arts = _find_sprint_artifacts(graph)
        for art in sprint_arts:
            for idx, line in enumerate(art.body.splitlines(), start=1):
                if not _BULLET_LINE_RE.match(line):
                    continue
                if _BULLET_ID_RE.search(line):
                    continue
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.sprint_artifacts_have_ids",
                    severity=Severity.HIGH,
                    message=(
                        f"Sprint artifact '{_posix(art.path)}' line "
                        f"{idx} has no identifier "
                        f"(expected **XX-###** marker)"
                    ),
                    location=art.path,
                    line=idx,
                ), _CLAUSE))

    # -- Check 4: retro actions assigned ---------------------------------
    def _check_retro_actions_assigned(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        retro_arts = _find_retro_artifacts(graph)
        for art in retro_arts:
            for idx, line in enumerate(art.body.splitlines(), start=1):
                m = _RETRO_ACTION_RE.match(line)
                if not m:
                    continue
                action_id = m.group(1)
                has_owner = bool(
                    _OWNER_WORD_RE.search(line) or _HANDLE_RE.search(line)
                )
                has_due = bool(
                    _DUE_WORD_RE.search(line) or _ISO_DATE_RE.search(line)
                )
                missing_parts = []
                if not has_owner:
                    missing_parts.append("owner")
                if not has_due:
                    missing_parts.append("due date")
                if not missing_parts:
                    continue
                missing = ", ".join(missing_parts)
                findings.add(attach_clause(Finding(
                    gate_id=f"{self.id}.retro_actions_assigned",
                    severity=Severity.HIGH,
                    message=(
                        f"Retro action '{action_id}' in "
                        f"'{_posix(art.path)}' line {idx} "
                        f"missing: {missing}"
                    ),
                    location=art.path,
                    line=idx,
                ), _CLAUSE))

    # -- Check 5: velocity history present -------------------------------
    def _check_velocity_history_present(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        art = _find_velocity_artifact(graph)
        if art is None:
            findings.add(attach_clause(Finding(
                gate_id=f"{self.id}.velocity_history_present",
                severity=Severity.HIGH,
                message=(
                    "No velocity history found under "
                    "07-agile-artifacts/ (expected filename containing "
                    "'velocity', 'sprint-metrics', or 'sprint-history')"
                ),
                location=None,
                line=None,
            ), _CLAUSE))
            return
        n = len(_SPRINT_REF_RE.findall(art.body))
        if n >= 2:
            return
        findings.add(attach_clause(Finding(
            gate_id=f"{self.id}.velocity_history_present",
            severity=Severity.HIGH,
            message=(
                f"Velocity history '{_posix(art.path)}' references "
                f"fewer than 2 sprints (found {n}; need history "
                f"across multiple sprints)"
            ),
            location=art.path,
            line=None,
        ), _CLAUSE))
