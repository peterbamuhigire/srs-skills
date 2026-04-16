"""Evidence pack assembler."""
from __future__ import annotations
import csv
import hashlib
import io
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List

_INCLUDE = ("_context", "_registry", "09-governance-compliance")


def _sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def build_evidence_pack(project_root: Path, out: Path) -> None:
    """Build a ZIP bundle of `_context/`, `_registry/`, and
    `09-governance-compliance/` plus a manifest CSV.

    TODO: embed a validation-report.md from `engine validate` once the CLI
    can be invoked cleanly from inside a Phase 09 gate evaluation.
    """
    rows: List[dict] = []
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for top in _INCLUDE:
            base = project_root / top
            if not base.exists():
                continue
            for p in sorted(base.rglob("*")):
                if p.is_file():
                    rel = p.relative_to(project_root).as_posix()
                    z.write(p, arcname=rel)
                    rows.append({
                        "path": rel,
                        "sha256": _sha256(p),
                        "size_bytes": str(p.stat().st_size),
                        "modified": datetime.fromtimestamp(
                            p.stat().st_mtime
                        ).isoformat(timespec="seconds"),
                    })
        buf = io.StringIO()
        w = csv.DictWriter(
            buf,
            fieldnames=["path", "sha256", "size_bytes", "modified"],
        )
        w.writeheader()
        w.writerows(rows)
        z.writestr("manifest.csv", buf.getvalue())
