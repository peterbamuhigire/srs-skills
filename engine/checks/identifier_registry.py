"""Identifier registry check."""
from __future__ import annotations
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.registry.identifiers import IdentifierRegistry

class IdentifierRegistryCheck:
    def __init__(self, gate_id: str, registry_path: Path) -> None:
        self.gate_id = gate_id
        self._registry = IdentifierRegistry.load(registry_path)

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        registry_ids = {e.id for e in self._registry}
        artifact_ids = set(graph.all_identifiers())
        for ident in artifact_ids - registry_ids:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.unknown_id",
                severity=Severity.HIGH,
                message=f"Artifact references {ident} but it is not in _registry/identifiers.yaml",
                location=None, line=None,
            ))
        for ident in registry_ids - artifact_ids:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.orphan_id",
                severity=Severity.MEDIUM,
                message=f"Registry contains orphan identifier {ident} — no artifact references it",
                location=None, line=None,
            ))
