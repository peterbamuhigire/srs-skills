"""Immutable in-memory graph of project artifacts."""
from __future__ import annotations
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Tuple
from engine.workspace import Workspace
from engine.parsers.frontmatter import parse_frontmatter
from engine.parsers.markers import Marker, find_markers

_ID_PATTERN = re.compile(r"\*\*([A-Z]{2,5}-\d{3,5})\*\*")

@dataclass(frozen=True)
class Artifact:
    path: Path
    title: str
    phase: Optional[str]
    document: Optional[str]
    section: Optional[str]
    identifiers: Tuple[str, ...]
    markers: Tuple[Marker, ...]
    body: str
    frontmatter: Dict[str, Any] = field(default_factory=dict, compare=False, hash=False)

    @classmethod
    def from_file(cls, root: Path, path: Path) -> "Artifact":
        raw = path.read_text(encoding="utf-8")
        fm, content = parse_frontmatter(raw)
        title = _extract_title(content)
        ids = tuple(sorted(set(_ID_PATTERN.findall(content))))
        markers = tuple(find_markers(content))
        return cls(
            path=path.relative_to(root),
            title=title,
            phase=fm.get("phase"),
            document=fm.get("document"),
            section=fm.get("section"),
            identifiers=ids,
            markers=markers,
            body=content,
            frontmatter=fm,
        )

def _extract_title(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""

@dataclass(frozen=True)
class ArtifactGraph:
    artifacts: Tuple[Artifact, ...]

    @classmethod
    def build(cls, workspace: Workspace) -> "ArtifactGraph":
        items = tuple(
            Artifact.from_file(workspace.root, p)
            for p in workspace.iter_artifacts()
        )
        return cls(artifacts=items)

    def in_phase(self, phase: str) -> Iterator[Artifact]:
        return (a for a in self.artifacts if a.phase == phase)

    def all_identifiers(self) -> List[str]:
        out: List[str] = []
        for a in self.artifacts:
            out.extend(a.identifiers)
        return out

    def all_markers(self) -> List[Tuple[Path, Marker]]:
        return [(a.path, m) for a in self.artifacts for m in a.markers]
