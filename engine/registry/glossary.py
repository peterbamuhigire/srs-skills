"""Glossary registry for a project."""
from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator
import jsonschema
from ruamel.yaml import YAML
from engine.registry.identifiers import RegistryError


@dataclass(frozen=True)
class GlossaryEntry:
    term: str
    definition: str
    source: str = ""
    first_introduced_in: str = ""


_SCHEMA = json.loads(
    (Path(__file__).parent / "schemas" / "glossary.schema.json").read_text()
)
_yaml = YAML(typ="safe")


class GlossaryRegistry:
    def __init__(self, entries: dict[str, GlossaryEntry]) -> None:
        # keyed by lowercased term
        self._entries = entries

    @classmethod
    def load(cls, path: Path) -> "GlossaryRegistry":
        if not path.exists():
            return cls({})
        data = _yaml.load(path.read_text(encoding="utf-8")) or {"terms": []}
        try:
            jsonschema.validate(data, _SCHEMA)
        except jsonschema.ValidationError as exc:
            raise RegistryError(f"Schema violation in {path}: {exc.message}") from exc
        entries: dict[str, GlossaryEntry] = {}
        for item in data["terms"]:
            key = item["term"].lower()
            if key in entries:
                raise RegistryError(f"Duplicate term: {item['term']}")
            entries[key] = GlossaryEntry(
                term=item["term"],
                definition=item["definition"],
                source=item.get("source", ""),
                first_introduced_in=item.get("first_introduced_in", ""),
            )
        return cls(entries)

    def save(self, path: Path) -> None:
        items = [
            {"term": e.term, "definition": e.definition,
             "source": e.source, "first_introduced_in": e.first_introduced_in}
            for e in self._entries.values()
        ]
        _yaml.dump({"terms": items}, path.open("w", encoding="utf-8"))

    def __len__(self) -> int:
        return len(self._entries)

    def __getitem__(self, term: str) -> GlossaryEntry:
        return self._entries[term.lower()]

    def __iter__(self) -> Iterator[GlossaryEntry]:
        return iter(self._entries.values())
