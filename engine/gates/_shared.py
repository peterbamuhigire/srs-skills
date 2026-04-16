"""Shared helpers for phase gates."""
from __future__ import annotations
from dataclasses import dataclass
from engine.findings import Finding

@dataclass(frozen=True)
class ClauseRef:
    standard: str
    clause: str

    def label(self) -> str:
        return f"[{self.standard} §{self.clause}]"

def attach_clause(finding: Finding, clause: ClauseRef) -> Finding:
    return Finding(
        gate_id=finding.gate_id,
        severity=finding.severity,
        message=f"{finding.message} {clause.label()}",
        location=finding.location,
        line=finding.line,
    )
