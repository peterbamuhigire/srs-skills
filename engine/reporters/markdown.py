"""Markdown reporter."""
from __future__ import annotations
from typing import Iterable
from engine.findings import Finding, FindingCollection

def render_markdown(
    findings: FindingCollection, waived: Iterable[Finding], project: str
) -> str:
    lines = [f"# Engine Validation Report — {project}", ""]
    if len(findings) == 0:
        lines.append("**Status:** PASS — no findings.")
    else:
        lines.append(f"**Status:** {'FAIL' if findings.is_blocking else 'WARN'}")
        lines.append(f"**Findings:** {len(findings)}")
        lines.append("")
        lines.append("| Gate | Severity | Location | Line | Message |")
        lines.append("|---|---|---|---|---|")
        for f in findings:
            loc = f.location.as_posix() if f.location else "-"
            line = f.line if f.line is not None else "-"
            lines.append(
                f"| `{f.gate_id}` | {f.severity.name} | `{loc}` | {line} | {f.message} |"
            )
    waived_list = list(waived)
    if waived_list:
        lines.extend(["", "## Waived findings", ""])
        for f in waived_list:
            lines.append(f"- `{f.gate_id}` — {f.message}")
    return "\n".join(lines) + "\n"
