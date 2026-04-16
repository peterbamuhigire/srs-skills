from pathlib import Path
import pytest
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.nfr_smart import SmartNfrCheck

def _ws(tmp_path: Path, body: str) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/nfrs.md").write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))

def test_passes_when_nfr_has_metric_and_threshold(tmp_path: Path):
    body = "# NFRs\n- **NFR-001** Response time shall be ≤ 500 ms at P95 under normal load."
    findings = FindingCollection()
    SmartNfrCheck("phase02.smart_nfr").run(_ws(tmp_path, body), findings)
    assert len(findings) == 0

def test_flags_vague_nfr(tmp_path: Path):
    body = "# NFRs\n- **NFR-002** The system shall be fast and reliable."
    findings = FindingCollection()
    SmartNfrCheck("phase02.smart_nfr").run(_ws(tmp_path, body), findings)
    items = list(findings)
    assert len(items) == 1
    assert "fast" in items[0].message
