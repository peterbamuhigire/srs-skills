"""Traceability check: every FR links upward to a BG and downward to a TC."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity


_BG_ID = re.compile(r"\bBG-\d{3,5}\b")
_TC_ID = re.compile(r"\bTC-\d{3,5}\b")


def _requirement_trace(frontmatter: dict) -> set[str]:
    value = frontmatter.get("requirement_trace")
    if isinstance(value, str):
        return {value.strip()} if value.strip() else set()
    if isinstance(value, list):
        return {
            item.strip()
            for item in value
            if isinstance(item, str) and item.strip()
        }
    return set()


class TraceabilityCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        all_ids = set(graph.all_identifiers())
        frs = {i for i in all_ids if i.startswith("FR-")}
        bgs = {i for i in all_ids if i.startswith("BG-")}
        for fr in sorted(frs):
            fr_pattern = re.compile(rf"\b{re.escape(fr)}\b")
            linked_goals = {
                goal
                for artifact in graph.artifacts
                for line in artifact.body.splitlines()
                if fr_pattern.search(line)
                for goal in _BG_ID.findall(line)
            }
            if not linked_goals.intersection(bgs):
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any business goal",
                    location=None, line=None,
                ))

            linked_tests = {
                test_id
                for artifact in graph.artifacts
                if artifact.phase == "05" or artifact.path.as_posix().startswith("05-")
                if fr in _requirement_trace(artifact.frontmatter)
                or fr_pattern.search(artifact.body)
                for test_id in _TC_ID.findall(artifact.body)
            }
            if not linked_tests:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr} has no traceability link to any test case",
                    location=None, line=None,
                ))
