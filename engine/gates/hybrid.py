"""Hybrid Sync gate."""
from __future__ import annotations
from pathlib import Path
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity
from engine.gates.base import Gate
from engine.checks.hybrid_traces import HybridTracesCheck


class HybridSyncGate(Gate):
    id = "hybrid"
    title = "Hybrid (Water-Scrum-Fall) synchronisation gate"
    severity = Severity.HIGH

    def __init__(self, project_root: Path) -> None:
        self._root = project_root

    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        meth = next(
            (a for a in graph.artifacts if a.path.name == "methodology.md"),
            None,
        )
        if not meth:
            return
        fm_methodology = str(meth.frontmatter.get("methodology", "")).lower()
        if fm_methodology != "hybrid" and "methodology: hybrid" not in meth.body.lower():
            return
        HybridTracesCheck(
            f"{self.id}.traces",
            self._root / "_registry" / "baseline-trace.yaml",
        ).run(graph, findings)
        # DoR/DoD must reference compliance constraints by ID.
        dor_dod = next(
            (a for a in graph.artifacts if a.path.name == "dor-dod.md"),
            None,
        )
        if dor_dod is None:
            findings.add(Finding(
                gate_id=f"{self.id}.dor_dod_missing",
                severity=Severity.HIGH,
                message="Hybrid project missing 07-agile-artifacts/definitions/dor-dod.md",
                location=None, line=None,
            ))
            return
        body = dor_dod.body
        if "FR-" not in body and "NFR-" not in body and "CTRL-" not in body:
            findings.add(Finding(
                gate_id=f"{self.id}.dor_dod_decoupled",
                severity=Severity.HIGH,
                message="dor-dod.md does not reference any baseline FR/NFR/CTRL by ID",
                location=dor_dod.path, line=None,
            ))
