"""HybridTracesCheck: enforce baseline to story trace integrity."""
from __future__ import annotations
from pathlib import Path
from ruamel.yaml import YAML
from engine.findings import Finding, FindingCollection, Severity

_yaml = YAML(typ="safe")


class HybridTracesCheck:
    def __init__(self, gate_id: str, trace_path: Path) -> None:
        self.gate_id = gate_id
        self._path = trace_path

    def run(self, _graph, findings: FindingCollection) -> None:
        if not self._path.exists():
            findings.add(Finding(
                gate_id=f"{self.gate_id}.missing",
                severity=Severity.HIGH,
                message=f"Hybrid project missing {self._path}",
                location=None, line=None,
            ))
            return
        data = _yaml.load(self._path.read_text(encoding="utf-8")) or {}
        baseline_ids = {b["id"] for b in (data.get("baseline") or [])}
        stories = data.get("stories") or []
        # All trace targets exist.
        for s in stories:
            for tgt in s.get("traces", []) or []:
                if tgt not in baseline_ids:
                    findings.add(Finding(
                        gate_id=f"{self.gate_id}.unknown_trace",
                        severity=Severity.HIGH,
                        message=f"Story {s['id']} traces to {tgt} which is not in the baseline",
                        location=self._path, line=None,
                    ))
        # Every baseline item is implemented.
        traced = {tgt for s in stories for tgt in (s.get("traces") or [])}
        for bid in sorted(baseline_ids - traced):
            findings.add(Finding(
                gate_id=f"{self.gate_id}.orphan_baseline",
                severity=Severity.HIGH,
                message=f"Baseline item {bid} has no implementing story",
                location=self._path, line=None,
            ))
