"""Identifier registry for a project."""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Tuple
import jsonschema
from ruamel.yaml import YAML

class RegistryError(Exception):
    """Malformed or inconsistent registry."""

@dataclass(frozen=True)
class IdentifierEntry:
    id: str
    kind: str
    defined_in: str
    title: str = ""
    links: Tuple[str, ...] = ()

_SCHEMA = json.loads(
    (Path(__file__).parent / "schemas" / "identifiers.schema.json").read_text()
)
_yaml = YAML(typ="safe")

class IdentifierRegistry:
    def __init__(self, entries: dict[str, IdentifierEntry]) -> None:
        self._entries = entries

    @classmethod
    def load(cls, path: Path) -> "IdentifierRegistry":
        if not path.exists():
            return cls({})
        data = _yaml.load(path.read_text(encoding="utf-8")) or {"identifiers": []}
        try:
            jsonschema.validate(data, _SCHEMA)
        except jsonschema.ValidationError as exc:
            raise RegistryError(f"Schema violation in {path}: {exc.message}") from exc
        entries: dict[str, IdentifierEntry] = {}
        for item in data["identifiers"]:
            if item["id"] in entries:
                raise RegistryError(f"Duplicate identifier: {item['id']}")
            entries[item["id"]] = IdentifierEntry(
                id=item["id"],
                kind=item["kind"],
                defined_in=item["defined_in"],
                title=item.get("title", ""),
                links=tuple(item.get("links", [])),
            )
        return cls(entries)

    def save(self, path: Path) -> None:
        items = [
            {"id": e.id, "kind": e.kind, "defined_in": e.defined_in,
             "title": e.title, "links": list(e.links)}
            for e in self._entries.values()
        ]
        _yaml.dump({"identifiers": items}, path.open("w", encoding="utf-8"))

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, ident: str) -> IdentifierEntry:
        return self._entries[ident]

    def __iter__(self) -> Iterator[IdentifierEntry]:
        return iter(self._entries.values())
