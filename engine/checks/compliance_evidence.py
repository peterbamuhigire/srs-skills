"""Selected controls must carry evidence, owner/reviewer, and status."""
from __future__ import annotations
import re
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")
_EVIDENCE = re.compile(r"\bEvidence\b", re.IGNORECASE)
_OWNER = re.compile(r"\b(Reviewer|Owner|Approver)\b", re.IGNORECASE)
_STATUS = re.compile(r"\b(Status|Implemented|Planned|Partial|Pass|FAIL|PASS)\b", re.IGNORECASE)
_ARTIFACT_LINK = re.compile(
    r"\b(?:FR|NFR|TC|ADR|CTRL|BG)-\d{3,5}\b|"
    r"\b\d{2}-[A-Za-z0-9_\-./]+\.md\b",
    re.IGNORECASE,
)
_HEADING = re.compile(r"^##\s+", re.MULTILINE)


class ComplianceEvidenceCheck:
    def __init__(self, gate_id: str, project_root: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root

    def _load_selected(self) -> list[str]:
        path = self._project / "_registry" / "controls.yaml"
        if not path.exists():
            return []
        data = _yaml.load(path.read_text(encoding="utf-8")) or {}
        return [
            str(item.get("id", "")).strip()
            for item in data.get("selected", []) or []
            if str(item.get("id", "")).strip()
        ]

    def _sections(self, body: str) -> list[str]:
        parts = _HEADING.split(body)
        if len(parts) <= 1:
            return [body]
        return parts

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        selected = self._load_selected()
        if not selected:
            return
        compliance_artifacts = [
            art for art in graph.artifacts
            if art.phase == "09"
            or "09-governance-compliance/" in str(art.path).replace("\\", "/")
        ]
        for ctrl_id in selected:
            matched = []
            for art in compliance_artifacts:
                for section in self._sections(art.body):
                    if ctrl_id in section:
                        matched.append((art, section))
            if not matched:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{ctrl_id} has no compliance section under 09-governance-compliance/",
                    location=None,
                    line=None,
                ))
                continue
            ok = False
            for art, section in matched:
                if (
                    _EVIDENCE.search(section)
                    and _OWNER.search(section)
                    and _STATUS.search(section)
                    and _ARTIFACT_LINK.search(section)
                ):
                    ok = True
                    break
            if ok:
                continue
            findings.add(Finding(
                gate_id=self.gate_id,
                severity=Severity.HIGH,
                message=(
                    f"{ctrl_id} is documented but lacks complete compliance evidence "
                    f"(need evidence, owner/reviewer, status, and linked artifacts)"
                ),
                location=matched[0][0].path,
                line=None,
            ))
