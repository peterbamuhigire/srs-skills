"""ControlsCheck: every selected control has the artifacts the domain requires."""
from __future__ import annotations
import fnmatch
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")


class ControlsCheck:
    def __init__(self, gate_id: str, project_root: Path, domain_register: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root
        self._domain_register = domain_register

    def _load_yaml(self, path: Path) -> dict:
        return _yaml.load(path.read_text(encoding="utf-8")) or {}

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        sel_path = self._project / "_registry" / "controls.yaml"
        if not sel_path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.no_selection",
                severity=Severity.HIGH,
                message="Project missing _registry/controls.yaml",
                location=None, line=None,
            ))
            return
        selected = {
            c["id"]: c for c in self._load_yaml(sel_path).get("selected", [])
        }
        register = {
            c["id"]: c for c in self._load_yaml(self._domain_register).get("controls", [])
        }
        expectations_path = self._domain_register.parent / "evidence-expectations.yaml"
        expectations = (
            self._load_yaml(expectations_path).get("expectations", {})
            if expectations_path.exists()
            else {}
        )
        artifact_paths = [str(a.path).replace("\\", "/") for a in graph.artifacts]
        for cid in selected:
            ctrl = register.get(cid)
            if ctrl is None:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.unknown_control",
                    severity=Severity.HIGH,
                    message=f"{cid} selected but not defined in domain register",
                    location=sel_path, line=None,
                ))
                continue
            cat = ctrl["category"]
            for pattern in expectations.get(cat, {}).get("must_appear_in", []):
                hits = [p for p in artifact_paths if fnmatch.fnmatch(p, pattern)]
                if not hits:
                    findings.add(Finding(
                        gate_id=f"{self.gate_id}.missing_evidence",
                        severity=Severity.HIGH,
                        message=(
                            f"{cid} ({cat}) requires an artifact matching "
                            f"'{pattern}', none found"
                        ),
                        location=None, line=None,
                    ))
            # Mention check: control ID appears in at least one artifact body
            mentioned = any(cid in a.body for a in graph.artifacts)
            if not mentioned:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.unused_in_artifacts",
                    severity=Severity.HIGH,
                    message=f"{cid} selected but never referenced in any artifact",
                    location=None, line=None,
                ))
