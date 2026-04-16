"""AdrCatalogCheck: reconcile ADR files with the ADR catalog."""
from __future__ import annotations
import json
import re
from pathlib import Path
from ruamel.yaml import YAML
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None


def _coerce_dates(obj):
    """Recursively stringify `datetime.date` objects so jsonschema's
    `format: date` check accepts them."""
    import datetime as _dt
    if isinstance(obj, _dt.date):
        return obj.isoformat()
    if isinstance(obj, list):
        return [_coerce_dates(x) for x in obj]
    if isinstance(obj, dict):
        return {k: _coerce_dates(v) for k, v in obj.items()}
    return obj

_yaml = YAML(typ="safe")
_ADR_FILE_RE = re.compile(r"(\d{4})-[A-Za-z0-9_\-]+\.md$")
_SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "registry" / "schemas" / "adr-catalog.schema.json"
)


class AdrCatalogCheck:
    def __init__(self, gate_id: str, project_root: Path) -> None:
        self.gate_id = gate_id
        self._project = project_root

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        catalog_path = self._project / "_registry" / "adr-catalog.yaml"
        if not catalog_path.exists():
            return
        try:
            data = _yaml.load(catalog_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            findings.add(Finding(
                gate_id=f"{self.gate_id}.schema_violation",
                severity=Severity.HIGH,
                message=f"ADR catalog YAML parse error: {exc}",
                location=catalog_path, line=None,
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
                    message=f"ADR catalog schema violation: {exc.message}",
                    location=catalog_path, line=None,
                ))
                return

        catalog = {entry["id"]: entry for entry in data.get("adrs", []) or []}

        # Collect ADR files from artifacts.
        adr_files: dict[str, Path] = {}
        for art in graph.artifacts:
            posix = str(art.path).replace("\\", "/")
            if "09-governance-compliance/05-adr/" not in posix:
                continue
            if not posix.endswith(".md"):
                continue
            match = _ADR_FILE_RE.search(posix)
            if not match:
                continue
            adr_id = f"ADR-{match.group(1)}"
            adr_files[adr_id] = art.path

        # Uncatalogued ADR files.
        for adr_id, path in adr_files.items():
            if adr_id not in catalog:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.uncatalogued",
                    severity=Severity.HIGH,
                    message=(
                        f"ADR file '{str(path).replace(chr(92), '/')}' has no "
                        f"entry in _registry/adr-catalog.yaml (expected id {adr_id})"
                    ),
                    location=path, line=None,
                ))

        # Missing-file catalog entries.
        for adr_id in catalog:
            if adr_id not in adr_files:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.missing_file",
                    severity=Severity.HIGH,
                    message=(
                        f"Catalog entry {adr_id} has no matching file under "
                        f"09-governance-compliance/05-adr/"
                    ),
                    location=catalog_path, line=None,
                ))

        # Dangling supersession.
        for adr_id, entry in catalog.items():
            superseded_by = entry.get("superseded_by")
            if superseded_by and superseded_by not in catalog:
                findings.add(Finding(
                    gate_id=f"{self.gate_id}.dangling_supersession",
                    severity=Severity.HIGH,
                    message=(
                        f"ADR {adr_id} is superseded_by {superseded_by}, "
                        f"but {superseded_by} does not appear in the catalog"
                    ),
                    location=catalog_path, line=None,
                ))
