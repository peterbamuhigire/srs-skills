"""Requirements should have concrete downstream design evidence."""
from __future__ import annotations
import re
from engine.artifact_graph import ArtifactGraph
from engine.findings import Finding, FindingCollection, Severity

_DESIGN_EVIDENCE = re.compile(
    r"\b("
    r"api|endpoint|schema|table|column|database|component|service|queue|"
    r"cache|worker|sequence|flow|model|class|state|rbac|encrypt|threat|"
    r"ui|ux|wizard|screen|payload|contract|event|controller"
    r")\b",
    re.IGNORECASE,
)


def _posix(path) -> str:
    return str(path).replace("\\", "/")


class DesignSufficiencyCheck:
    def __init__(self, gate_id: str) -> None:
        self.gate_id = gate_id

    def run(self, graph: ArtifactGraph, findings: FindingCollection) -> None:
        fr_ids = sorted({
            ident for ident in graph.all_identifiers() if ident.startswith("FR-")
        })
        if not fr_ids:
            return
        design_artifacts = [
            art for art in graph.artifacts
            if art.phase == "03" or _posix(art.path).startswith("03-design-documentation/")
        ]
        if not design_artifacts:
            return
        for fr_id in fr_ids:
            refs = [art for art in design_artifacts if fr_id in art.body]
            if not refs:
                findings.add(Finding(
                    gate_id=self.gate_id,
                    severity=Severity.HIGH,
                    message=f"{fr_id} is not referenced by any Phase 03 design artifact",
                    location=None,
                    line=None,
                ))
                continue
            if any(_DESIGN_EVIDENCE.search(art.body) for art in refs):
                continue
            findings.add(Finding(
                gate_id=self.gate_id,
                severity=Severity.HIGH,
                message=(
                    f"{fr_id} is referenced in design, but the referencing artifact "
                    f"does not contain concrete design evidence keywords"
                ),
                location=refs[0].path,
                line=None,
            ))
