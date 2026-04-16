"""BaselineDeltaCheck: confirm the declared current baseline file exists."""
from __future__ import annotations
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")


class BaselineDeltaCheck:
    def __init__(self, gate_id: str, project_root: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root

    def run(self, _graph: ArtifactGraph, findings: FindingCollection) -> None:
        baselines_path = self._project / "_registry" / "baselines.yaml"
        if not baselines_path.exists():
            return
        try:
            data = _yaml.load(baselines_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.current_missing",
                severity=Severity.HIGH,
                message=f"_registry/baselines.yaml parse error: {exc}",
                location=baselines_path, line=None,
            ))
            return
        current = data.get("current")
        if not current:
            return
        snap_path = (
            self._project / "09-governance-compliance" / "07-baseline-delta"
            / f"{current}.yaml"
        )
        if not snap_path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.current_missing",
                severity=Severity.HIGH,
                message=(
                    f"_registry/baselines.yaml declares current={current} but "
                    f"'09-governance-compliance/07-baseline-delta/{current}.yaml' "
                    f"is missing"
                ),
                location=baselines_path, line=None,
            ))
