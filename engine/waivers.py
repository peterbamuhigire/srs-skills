"""Waiver register: gate-specific exceptions with expiry and approver."""
from __future__ import annotations
import fnmatch
from dataclasses import dataclass
from datetime import date
from pathlib import Path, PureWindowsPath
from typing import Iterator, List, Optional, Tuple
from ruamel.yaml import YAML
from ruamel.yaml.error import YAMLError
from engine.findings import Finding, FindingCollection

class WaiverError(Exception):
    """Raised on malformed waiver file."""

def _as_date(value) -> date:
    """Coerce a YAML value to a date. The waive CLI quotes dates, so they may
    load as ISO strings rather than date objects."""
    if type(value) is date:
        return value
    if not isinstance(value, str):
        raise WaiverError(f"Invalid waiver date type: {type(value).__name__}")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise WaiverError(f"Invalid waiver date: {value!r}") from exc


def _required_text(item: dict, field: str) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value.strip():
        raise WaiverError(f"Waiver field {field!r} must be a non-empty string")
    return value.strip()


def validate_scope(value) -> str:
    if not isinstance(value, str):
        raise WaiverError("Waiver field 'scope' must be a string")
    scope = value.strip()
    if scope in ("", "*"):
        return scope
    if "\\" in scope:
        raise WaiverError("Waiver scope must use repository-relative forward slashes")
    windows_path = PureWindowsPath(scope)
    if scope.startswith("/") or windows_path.drive or ".." in scope.split("/"):
        raise WaiverError("Waiver scope must stay within the project workspace")
    return scope

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
        approval_window = (self.expires_on - self.approved_on).days
        if not 1 <= approval_window <= 90:
            return False
        if finding.gate_id != self.gate:
            return False
        if not self.approved_on <= today <= self.expires_on:
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
        try:
            loaded = yaml.load(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, YAMLError) as exc:
            raise WaiverError(f"Cannot read waiver register {path}: {exc}") from exc
        data = {} if loaded is None else loaded
        if not isinstance(data, dict):
            raise WaiverError(f"Waiver register root in {path} must be a mapping")
        items = data.get("waivers", [])
        if items is None:
            items = []
        if not isinstance(items, list):
            raise WaiverError(f"Waivers in {path} must be a list")

        required = {"id", "gate", "reason", "approver", "approved_on", "expires_on"}
        allowed = required | {"scope"}
        waivers = []
        seen_ids = set()
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                raise WaiverError(f"Waiver #{index + 1} in {path} must be a mapping")
            missing = sorted(required - set(item))
            unknown = sorted(set(item) - allowed)
            if missing or unknown:
                raise WaiverError(
                    f"Malformed waiver #{index + 1} in {path}: "
                    f"missing={missing}, unknown={unknown}"
                )
            waiver_id = _required_text(item, "id")
            if waiver_id in seen_ids:
                raise WaiverError(f"Duplicate waiver id {waiver_id!r} in {path}")
            seen_ids.add(waiver_id)
            waivers.append(
                Waiver(
                    id=waiver_id,
                    gate=_required_text(item, "gate"),
                    scope=validate_scope(item.get("scope", "*")),
                    reason=_required_text(item, "reason"),
                    approver=_required_text(item, "approver"),
                    approved_on=_as_date(item["approved_on"]),
                    expires_on=_as_date(item["expires_on"]),
                )
            )
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
