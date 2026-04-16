"""Gate ABC and Gate registry."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Iterator
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection, Severity

class Gate(ABC):
    id: str = ""
    title: str = ""
    severity: Severity = Severity.HIGH

    @abstractmethod
    def evaluate(self, graph: ArtifactGraph, findings: FindingCollection) -> None: ...

class GateRegistry:
    def __init__(self) -> None:
        self._gates: Dict[str, Gate] = {}

    def register(self, gate: Gate) -> None:
        if not gate.id:
            raise ValueError("Gate id must be a non-empty string")
        if gate.id in self._gates:
            raise ValueError(f"Gate {gate.id} already registered")
        self._gates[gate.id] = gate

    def __contains__(self, gate_id: str) -> bool:
        return gate_id in self._gates

    def __iter__(self) -> Iterator[Gate]:
        return iter(self._gates.values())

    def run_all(
        self, graph: ArtifactGraph, findings: FindingCollection
    ) -> None:
        for gate in self._gates.values():
            gate.evaluate(graph, findings)
