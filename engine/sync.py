"""Extract identifiers and glossary terms into _registry/."""
from __future__ import annotations
import re
from pathlib import Path
from typing import Tuple
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.idscan import scan_line, kind_of
from engine.registry.identifiers import IdentifierEntry, IdentifierRegistry
from engine.registry.glossary import GlossaryRegistry, GlossaryEntry

_TERM = re.compile(r"-\s+\*\*([A-Za-z][A-Za-z0-9_-]{1,40}):\*\*\s+(.+)")


def sync(workspace: Workspace) -> Tuple[IdentifierRegistry, GlossaryRegistry, list[str]]:
    """Build the identifier and glossary registries from the artifact corpus.

    Identifiers are module-aware (see :mod:`engine.idscan`). Definition model:
    **first occurrence wins**. Each distinct ID is registered once; its
    ``defined_in`` is the first artifact (build order) that bold-defines it
    (``**FR-001**``), or — if it is never bold — the first artifact in which it
    appears at all. Repeated appearances (traceability matrices, DoD/DoR, risk
    registers, release notes, test reports, …) are references and are deduped,
    not treated as collisions: real projects legitimately bold the same ID in
    many places, so a bold-uniqueness rule produces false collisions. The
    returned error list is always empty and is retained only for the caller's
    stable signature.
    """
    graph = ArtifactGraph.build(workspace)
    first_seen: dict[str, Path] = {}
    bold_defined: dict[str, Path] = {}
    titles: dict[str, str] = {}
    glossary: dict[str, GlossaryEntry] = {}
    for art in graph.artifacts:
        for line in art.body.splitlines():
            for hit in scan_line(line):
                if hit.id not in first_seen:
                    first_seen[hit.id] = art.path
                if hit.bold and hit.id not in bold_defined:
                    bold_defined[hit.id] = art.path
                if hit.id not in titles and hit.trailing:
                    titles[hit.id] = hit.trailing[:120]
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
    entries: dict[str, IdentifierEntry] = {}
    for ident, first_path in first_seen.items():
        entries[ident] = IdentifierEntry(
            id=ident,
            kind=kind_of(ident),
            defined_in=str(bold_defined.get(ident, first_path)),
            title=titles.get(ident, ""),
        )
    errors: list[str] = []
    return IdentifierRegistry(entries), GlossaryRegistry(glossary), errors
