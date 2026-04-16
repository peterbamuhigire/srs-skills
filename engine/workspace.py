"""Project workspace locator."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

class WorkspaceNotFoundError(Exception):
    """Raised when a path is not a valid project workspace."""

@dataclass(frozen=True)
class Workspace:
    root: Path
    context_dir: Path

    @classmethod
    def load(cls, root: Path) -> "Workspace":
        root = Path(root).resolve()
        ctx = root / "_context"
        if not ctx.is_dir():
            raise WorkspaceNotFoundError(
                f"{root} is not a project workspace: missing '_context' directory"
            )
        return cls(root=root, context_dir=ctx)

    def iter_artifacts(self) -> Iterator[Path]:
        for p in sorted(self.root.rglob("*.md")):
            if p.is_file():
                yield p
