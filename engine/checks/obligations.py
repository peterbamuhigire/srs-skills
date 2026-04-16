"""ObligationsCheck: every relevant regulatory obligation has a satisfying control."""
from __future__ import annotations
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")


class ObligationsCheck:
    def __init__(self, gate_id: str, project_root: Path, obligations_file: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root
        self._obligations_file = obligations_file

    def _load_yaml(self, path: Path) -> dict:
        return _yaml.load(path.read_text(encoding="utf-8")) or {}

    def run(self, _graph: ArtifactGraph, findings: FindingCollection) -> None:
        standards_path = self._project / "_context" / "quality-standards.md"
        if not standards_path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.missing_framework_coverage",
                severity=Severity.HIGH,
                message=(
                    "Project missing _context/quality-standards.md; cannot "
                    "determine which regulatory frameworks apply"
                ),
                location=None, line=None,
            ))
            return
        standards_text = standards_path.read_text(encoding="utf-8").lower()
        sel_path = self._project / "_registry" / "controls.yaml"
        selected_ids: set[str] = set()
        if sel_path.exists():
            selected_ids = {
                c["id"]
                for c in self._load_yaml(sel_path).get("selected", []) or []
            }
        if not self._obligations_file.exists():
            return
        obligations = self._load_yaml(self._obligations_file).get("obligations", []) or []
        for ob in obligations:
            framework = (ob.get("framework") or "").lower()
            if not framework or framework not in standards_text:
                continue
            satisfied_by = ob.get("satisfied_by") or []
            if not any(cid in selected_ids for cid in satisfied_by):
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.unsatisfied",
                    severity=Severity.HIGH,
                    message=(
                        f"Obligation '{ob.get('obligation', '?')}' "
                        f"({ob.get('framework', '?')} {ob.get('clause', '')}) "
                        f"is in scope but no satisfying control is selected "
                        f"(needs one of: {', '.join(satisfied_by) or 'none mapped'})"
                    ),
                    location=self._obligations_file, line=None,
                ))
