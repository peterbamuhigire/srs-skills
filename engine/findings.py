"""Finding, Severity, and FindingCollection."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Iterable, Optional

class Severity(IntEnum):
    INFO = 10
    LOW = 20
    MEDIUM = 30
    HIGH = 40

@dataclass(frozen=True)
class Finding:
    gate_id: str
    severity: Severity
    message: str
    location: Optional[Path]
    line: Optional[int]

class FindingCollection:
    def __init__(self) -> None:
        self._items: list[Finding] = []

    def add(self, finding: Finding) -> None:
        self._items.append(finding)

    def extend(self, findings: Iterable[Finding]) -> None:
        self._items.extend(findings)

    def for_gate(self, gate_id: str) -> list[Finding]:
        return [f for f in self._items if f.gate_id == gate_id]

    @property
    def is_blocking(self) -> bool:
        return any(f.severity >= Severity.HIGH for f in self._items)

    def __iter__(self):
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)
