"""Find [TAG: reason] markers in markdown."""
from __future__ import annotations
import re
from dataclasses import dataclass
from typing import List

_PATTERN = re.compile(r"\[(?P<tag>[A-Z&\-]+)(?::\s*(?P<reason>[^\]]*))?\]")
_KNOWN_TAGS = {
    "V&V-FAIL", "CONTEXT-GAP", "GLOSSARY-GAP",
    "SMART-FAIL", "TRACE-GAP", "VERIFIABILITY-FAIL",
    "DPPA-FAIL", "DPIA-REQUIRED", "CONTROL-GAP",
    "DOMAIN-DEFAULT",
}

@dataclass(frozen=True)
class Marker:
    tag: str
    reason: str
    line: int

def find_markers(body: str) -> List[Marker]:
    out: List[Marker] = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        for m in _PATTERN.finditer(line):
            tag = m.group("tag")
            if tag not in _KNOWN_TAGS:
                continue
            reason = (m.group("reason") or "").strip()
            out.append(Marker(tag=tag, reason=reason, line=lineno))
    return out
