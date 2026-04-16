"""Extract identifiers and glossary terms into _registry/."""
from __future__ import annotations
import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph, Artifact
from engine.registry.identifiers import IdentifierEntry, IdentifierRegistry, RegistryError
from engine.registry.glossary import GlossaryRegistry, GlossaryEntry

_ID = re.compile(r"\*\*([A-Z]{2,5}-\d{3,5})\*\*\s*(.*)")
_TERM = re.compile(r"-\s+\*\*([A-Z][A-Za-z0-9_-]{1,40}):\*\*\s+(.+)")
_KIND_PREFIXES = {"BG": "BG", "FR": "FR", "NFR": "NFR", "US": "US", "TC": "TC",
                  "CTRL": "CTRL", "RISK": "RISK", "ADR": "ADR", "WAIVE": "WAIVE"}

def sync(workspace: Workspace) -> Tuple[IdentifierRegistry, GlossaryRegistry, list[str]]:
    graph = ArtifactGraph.build(workspace)
    seen: dict[str, list[Artifact]] = defaultdict(list)
    titles: dict[str, str] = {}
    glossary: dict[str, GlossaryEntry] = {}
    for art in graph.artifacts:
        for line in art.body.splitlines():
            for m in _ID.finditer(line):
                ident = m.group(1)
                seen[ident].append(art)
                if ident not in titles:
                    titles[ident] = m.group(2).strip()[:120]
            for m in _TERM.finditer(line):
                term = m.group(1)
                key = term.lower()
                if key in glossary:
                    continue  # first occurrence wins
                glossary[key] = GlossaryEntry(
                    term=term,
                    definition=m.group(2).strip(),
                    source="",
                    first_introduced_in=str(art.path),
                )
    errors: list[str] = []
    entries: dict[str, IdentifierEntry] = {}
    for ident, arts in seen.items():
        if len(arts) > 1:
            paths = ", ".join(str(a.path) for a in arts)
            errors.append(f"Identifier collision: {ident} appears in {paths}")
            continue
        kind_prefix = ident.split("-")[0]
        entries[ident] = IdentifierEntry(
            id=ident,
            kind=_KIND_PREFIXES.get(kind_prefix, kind_prefix),
            defined_in=str(arts[0].path),
            title=titles.get(ident, ""),
        )
    return IdentifierRegistry(entries), GlossaryRegistry(glossary), errors
