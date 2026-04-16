from pathlib import Path
from engine.workspace import Workspace
from engine.artifact_graph import ArtifactGraph
from engine.findings import FindingCollection
from engine.checks.nfr_threshold_dedup import NfrThresholdDedupCheck


def _ws(tmp_path: Path, body: str) -> ArtifactGraph:
    (tmp_path / "_context").mkdir()
    (tmp_path / "_context/nfrs.md").write_text(body, encoding="utf-8")
    return ArtifactGraph.build(Workspace.load(tmp_path))


def test_passes_when_thresholds_are_consistent(tmp_path: Path):
    body = (
        "# NFRs\n"
        "- **NFR-001** Response time shall be <= 500 ms at P95.\n"
        "- **NFR-002** Response time shall be <= 500 ms at P99.\n"
    )
    findings = FindingCollection()
    NfrThresholdDedupCheck("phase09.nfr_threshold_dedup").run(
        _ws(tmp_path, body), findings
    )
    assert len(findings) == 0, [f.message for f in findings]


def test_flags_contradicting_response_time_thresholds(tmp_path: Path):
    body = (
        "# NFRs\n"
        "- **NFR-001** Response time shall be <= 500 ms at P95.\n"
        "- **NFR-007** Response time shall be <= 1 s for reads.\n"
    )
    findings = FindingCollection()
    NfrThresholdDedupCheck("phase09.nfr_threshold_dedup").run(
        _ws(tmp_path, body), findings
    )
    msgs = [f.message for f in findings]
    assert len(msgs) == 1
    assert "response_time" in msgs[0]
    assert "NFR-001" in msgs[0] and "NFR-007" in msgs[0]


def test_flags_cross_unit_contradiction(tmp_path: Path):
    # Same metric, same comparator, different canonical values
    # -> contradiction.
    body = (
        "# NFRs\n"
        "- **NFR-010** Availability shall be >= 99.9%.\n"
        "- **NFR-011** Availability shall be >= 99.5%.\n"
    )
    findings = FindingCollection()
    NfrThresholdDedupCheck("phase09.nfr_threshold_dedup").run(
        _ws(tmp_path, body), findings
    )
    msgs = [f.message for f in findings]
    assert any(
        "availability" in m and "NFR-010" in m and "NFR-011" in m
        for m in msgs
    )


def test_ignores_unrecognized_metric(tmp_path: Path):
    body = (
        "# NFRs\n"
        "- **NFR-042** Code complexity shall be <= 10.\n"
        "- **NFR-043** Code complexity shall be <= 20.\n"
    )
    findings = FindingCollection()
    NfrThresholdDedupCheck("phase09.nfr_threshold_dedup").run(
        _ws(tmp_path, body), findings
    )
    # "code complexity" is not in the whitelist -> both NFRs skipped -> no
    # findings.
    assert len(findings) == 0
