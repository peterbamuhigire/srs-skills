from pathlib import Path

from engine.sdd_boundaries import find_dependency_cycle, parse_tasks, validate_feature_dir


def write_feature(root: Path, tasks: str = "- [ ] T001 {FR-001} Implement login\n") -> None:
    root.joinpath("spec.md").write_text(
        "# Spec\n\n## User Story 1 (P1)\n\nFR-001: Users can sign in.\n",
        encoding="utf-8",
    )
    root.joinpath("plan.md").write_text(
        "## Requirement Coverage Map\n\n"
        "| Req ID | Component | File Path(s) | Function(s)/Symbol(s) |\n"
        "|---|---|---|---|\n"
        "| FR-001 | Auth | src/auth.py | sign_in(credentials) |\n",
        encoding="utf-8",
    )
    root.joinpath("tasks.md").write_text(tasks, encoding="utf-8")


def test_valid_feature_workspace_has_no_boundary_findings(tmp_path: Path):
    write_feature(tmp_path)
    assert validate_feature_dir(tmp_path) == []


def test_p1_requirement_must_have_task_and_coverage(tmp_path: Path):
    write_feature(tmp_path, "- [ ] T001 Implement login\n")
    findings = validate_feature_dir(tmp_path, "plan-tasks")
    codes = {finding.code for finding in findings}
    assert "untasked-requirement" in codes


def test_cycle_and_missing_dependency_are_detected():
    rows = parse_tasks(
        "- [ ] T001 A after:T002\n"
        "- [ ] T002 B after:T001\n"
    )
    assert find_dependency_cycle(rows) == ["T001", "T002", "T001"]


def test_qc_requires_explicit_overall_pass(tmp_path: Path):
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text("overall: PASS\nchecks: 4\n", encoding="utf-8")
    assert validate_feature_dir(tmp_path, "implement-qc") == []


def test_qc_rejects_overall_fail_even_when_previous_pass_is_mentioned(tmp_path: Path):
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text(
        "overall: FAIL\nprevious test: PASS\n", encoding="utf-8"
    )
    findings = validate_feature_dir(tmp_path, "implement-qc")
    assert {finding.code for finding in findings} == {"qc-verdict-mismatch"}


def test_qc_rejects_negated_pass_without_current_verdict(tmp_path: Path):
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text("overall: FAIL\nNOT PASS\n", encoding="utf-8")
    findings = validate_feature_dir(tmp_path, "implement-qc")
    assert {finding.code for finding in findings} == {"qc-verdict-mismatch"}


def test_qc_rejects_unstructured_pass(tmp_path: Path):
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text("PASS\n", encoding="utf-8")
    findings = validate_feature_dir(tmp_path, "implement-qc")
    assert {finding.code for finding in findings} == {"qc-verdict-mismatch"}


def test_qc_rejects_stale_requirement_baseline(tmp_path: Path):
    import json
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text("overall: PASS\n", encoding="utf-8")
    (tmp_path / "sdd-handoff.json").write_text(json.dumps({
        "status": "blocked", "evidence_status": "not_assessed",
        "requirement_baseline": {"hash": "old"},
    }), encoding="utf-8")
    findings = validate_feature_dir(tmp_path, "implement-qc", "new")
    assert {finding.code for finding in findings} == {"stale-requirement-baseline"}


def test_complete_handoff_with_unverified_evidence_is_blocked(tmp_path: Path):
    import json
    write_feature(tmp_path)
    (tmp_path / ".qc-passed").write_text("", encoding="utf-8")
    (tmp_path / "qc-report.md").write_text("overall: PASS\n", encoding="utf-8")
    (tmp_path / "sdd-handoff.json").write_text(json.dumps({
        "status": "complete", "evidence_status": "not_assessed",
    }), encoding="utf-8")
    findings = validate_feature_dir(tmp_path, "implement-qc")
    assert {finding.code for finding in findings} == {"unverified-handoff"}
