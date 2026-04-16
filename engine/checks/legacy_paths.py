"""Legacy-path scanner for skill files."""
from __future__ import annotations
import re
from pathlib import Path
from engine.findings import Finding, FindingCollection, Severity

_LEGACY = re.compile(r"\.\./project_context/|\.\./output/")
_ALIAS_OPEN = re.compile(r"<!--\s*alias-block\s+start\s*-->", re.IGNORECASE)
_ALIAS_CLOSE = re.compile(r"<!--\s*alias-block\s+end\s*-->", re.IGNORECASE)

class LegacyPathCheck:
    gate_id = "kernel.legacy_skill_paths"

    def scan_file(self, path: Path, findings: FindingCollection) -> None:
        body = path.read_text(encoding="utf-8")
        in_alias = False
        for lineno, line in enumerate(body.splitlines(), start=1):
            if _ALIAS_OPEN.search(line):
                in_alias = True
                continue
            if _ALIAS_CLOSE.search(line):
                in_alias = False
                continue
            if in_alias:
                continue
            if _LEGACY.search(line):
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"Legacy path reference outside alias-block: {line.strip()[:120]}",
                    location=path, line=lineno,
                ))
