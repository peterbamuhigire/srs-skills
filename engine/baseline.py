"""Baseline snapshot and diff utilities."""
from __future__ import annotations
import hashlib
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict
from ruamel.yaml import YAML
from engine.artifact_graph import Artifact, ArtifactGraph

_yaml = YAML(typ="safe")


@dataclass(frozen=True)
class Snapshot:
    label: str
    created_on: date
    entries: Dict[str, str]  # id -> sha256


def _first_line_mentioning(ident: str, art: Artifact) -> str:
    needle = f"**{ident}**"
    for line in art.body.splitlines():
        if needle in line:
            return line
    return ""


def snapshot(graph: ArtifactGraph, label: str, today: date | None = None) -> Snapshot:
    today = today or date.today()
    entries: Dict[str, str] = {}
    for art in graph.artifacts:
        for ident in art.identifiers:
            line = _first_line_mentioning(ident, art)
            h = hashlib.sha256(line.encode("utf-8")).hexdigest()
            entries[ident] = h
    return Snapshot(label=label, created_on=today, entries=entries)


def save_snapshot(snap: Snapshot, path: Path) -> None:
    data = {
        "label": snap.label,
        "created_on": snap.created_on.isoformat(),
        "entries": [{"id": k, "sha256": v} for k, v in sorted(snap.entries.items())],
    }
    with path.open("w", encoding="utf-8") as f:
        _yaml.dump(data, f)


def load_snapshot(path: Path) -> Snapshot:
    data = _yaml.load(path.read_text(encoding="utf-8"))
    entries = {e["id"]: e["sha256"] for e in data.get("entries", [])}
    created = data["created_on"]
    if isinstance(created, str):
        created = date.fromisoformat(created)
    return Snapshot(
        label=data["label"],
        created_on=created,
        entries=entries,
    )


def diff(old: Snapshot, new: Snapshot) -> dict:
    added = sorted(set(new.entries) - set(old.entries))
    removed = sorted(set(old.entries) - set(new.entries))
    modified = sorted(
        k for k in set(old.entries) & set(new.entries)
        if old.entries[k] != new.entries[k]
    )
    return {"added": added, "removed": removed, "modified": modified}
