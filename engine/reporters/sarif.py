"""SARIF 2.1.0 reporter."""
from __future__ import annotations
import json
from collections import defaultdict
from engine.findings import FindingCollection, Severity

_LEVELS = {Severity.HIGH: "error", Severity.MEDIUM: "warning",
           Severity.LOW: "note", Severity.INFO: "note"}

def render_sarif(findings: FindingCollection) -> str:
    rules: dict[str, dict] = {}
    results = []
    for f in findings:
        rules.setdefault(f.gate_id, {
            "id": f.gate_id,
            "shortDescription": {"text": f.gate_id},
        })
        results.append({
            "ruleId": f.gate_id,
            "level": _LEVELS[f.severity],
            "message": {"text": f.message},
            "locations": [{
                "physicalLocation": {
                    "artifactLocation": {
                        "uri": f.location.as_posix() if f.location else "",
                    },
                    "region": {"startLine": f.line or 1},
                },
            }],
        })
    sarif = {
        "version": "2.1.0",
        "$schema": "https://json.schemastore.org/sarif-2.1.0.json",
        "runs": [{
            "tool": {"driver": {
                "name": "srs-skills-engine",
                "rules": list(rules.values()),
            }},
            "results": results,
        }],
    }
    return json.dumps(sarif, indent=2)
