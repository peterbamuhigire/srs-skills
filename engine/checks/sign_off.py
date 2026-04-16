"""SignOffCheck: confirm sign-off ledger entries reference existing files."""
from __future__ import annotations
import json
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


def _coerce_dates(obj):
    import datetime as _dt
    if isinstance(obj, _dt.date):
        return obj.isoformat()
    if isinstance(obj, list):
        return [_coerce_dates(x) for x in obj]
    if isinstance(obj, dict):
        return {k: _coerce_dates(v) for k, v in obj.items()}
    return obj

_yaml = YAML(typ="safe")
_SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "registry" / "schemas" / "sign-off-ledger.schema.json"
)


class SignOffCheck:
    def __init__(self, gate_id: str, project_root: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root

    def run(self, _graph: ArtifactGraph, findings: FindingCollection) -> None:
        ledger_path = self._project / "_registry" / "sign-off-ledger.yaml"
        if not ledger_path.exists():
            return
        try:
            data = _yaml.load(ledger_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.schema_violation",
                severity=Severity.HIGH,
                message=f"sign-off-ledger YAML parse error: {exc}",
                location=ledger_path, line=None,
            ))
            return
        if jsonschema is not None:
            schema = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
            try:
                jsonschema.validate(_coerce_dates(data), schema)
            except jsonschema.ValidationError as exc:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.schema_violation",
                    severity=Severity.HIGH,
                    message=f"sign-off-ledger schema violation: {exc.message}",
                    location=ledger_path, line=None,
                ))
                return
        for entry in data.get("sign_offs", []) or []:
            for rel in entry.get("artifact_set", []) or []:
                artifact_path = self._project / rel
                if not artifact_path.is_file():
                    findings.add(Finding(
                        gate_id=f"{self.gate_id}.missing_artifact",
                        severity=Severity.HIGH,
                        message=(
                            f"Sign-off for gate '{entry.get('gate', '?')}' "
                            f"references artifact '{rel}' which does not exist"
                        ),
                        location=ledger_path, line=None,
                    ))
