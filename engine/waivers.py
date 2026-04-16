"""Waiver register: gate-specific exceptions with expiry and approver."""
from __future__ import annotations
import fnmatch
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterator, List, Optional, Tuple
from ruamel.yaml import YAML
from engine.findings import Finding, FindingCollection

class WaiverError(Exception):
    """Raised on malformed waiver file."""

@dataclass(frozen=True)
class Waiver:
    id: str
    gate: str
    scope: str
    reason: str
    approver: str
    approved_on: date
    expires_on: date

    def applies_to(self, finding: Finding, today: date) -> bool:
        if finding.gate_id != self.gate:
            return False
        if today > self.expires_on:
            return False
        if finding.location is None:
            return self.scope in ("*", "")
        return fnmatch.fnmatch(str(finding.location).replace("\\", "/"), self.scope)

class WaiverRegister:
    def __init__(self, waivers: List[Waiver]) -> None:
        self._waivers = waivers

    @classmethod
    def load(cls, path: Path) -> "WaiverRegister":
        if not path.exists():
            return cls([])
        yaml = YAML(typ="safe")
        data = yaml.load(path.read_text(encoding="utf-8")) or {}
        items = data.get("waivers") or []
        try:
            waivers = [
                Waiver(
                    id=item["id"],
                    gate=item["gate"],
                    scope=item.get("scope", "*"),
                    reason=item["reason"],
                    approver=item["approver"],
                    approved_on=item["approved_on"],
                    expires_on=item["expires_on"],
                )
                for item in items
            ]
        except (KeyError, TypeError) as exc:
            raise WaiverError(f"Malformed waiver in {path}: {exc}") from exc
        return cls(waivers)

    def __iter__(self) -> Iterator[Waiver]:
        return iter(self._waivers)

    def __len__(self) -> int:
        return len(self._waivers)

    def matches(self, finding: Finding, today: date) -> Optional[Waiver]:
        for w in self._waivers:
            if w.applies_to(finding, today):
                return w
        return None

    def apply(
        self, findings: FindingCollection, today: date
    ) -> Tuple[List[Finding], List[Finding]]:
        waived: List[Finding] = []
        remaining: List[Finding] = []
        for f in findings:
            if self.matches(f, today):
                waived.append(f)
            else:
                remaining.append(f)
        return waived, remaining
