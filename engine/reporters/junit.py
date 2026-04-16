"""JUnit XML reporter."""
from __future__ import annotations
from collections import defaultdict
from xml.etree.ElementTree import Element, SubElement, tostring
from engine.findings import FindingCollection, Severity

def render_junit(findings: FindingCollection) -> str:
    by_gate: dict[str, list] = defaultdict(list)
    for f in findings:
        by_gate[f.gate_id].append(f)
    suite = Element("testsuite", name="srs-engine", tests=str(len(by_gate)))
    failures = 0
    for gate_id, items in by_gate.items():
        case = SubElement(suite, "testcase", classname="engine.gates", name=gate_id)
        blocking = [f for f in items if f.severity >= Severity.HIGH]
        if blocking:
            failures += 1
            failure = SubElement(case, "failure", message=blocking[0].message)
            failure.text = "\n".join(
                f"{f.location}:{f.line}: {f.message}" for f in items
            )
    suite.set("failures", str(failures))
    return tostring(suite, encoding="unicode")
