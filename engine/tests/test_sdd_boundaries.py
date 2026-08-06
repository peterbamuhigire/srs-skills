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
