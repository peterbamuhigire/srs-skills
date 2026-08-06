"""Deterministic checks for Spec-Driven Development feature workspaces.

This module is intentionally additive to the standards-driven SRS kernel. It
validates the small, portable artifact contract used by SDD-style feature
workspaces without treating prompt-level agent claims as evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


REQ_RE = re.compile(r"\b(?:FR|TR|OR|RR)-\d{3}\b")
TASK_RE = re.compile(r"^\s*-\s*\[([ Xx])\]\s*(T\d{3})\b(.*)$")
AFTER_RE = re.compile(r"\bafter:(T\d{3})\b")
P1_RE = re.compile(r"\bP1\b", re.IGNORECASE)


@dataclass(frozen=True)
class BoundaryFinding:
    severity: str
    code: str
    message: str


def validate_feature_dir(feature_dir: Path, stage: str = "all") -> list[BoundaryFinding]:
    """Return deterministic findings for an SDD feature workspace.

    Supported stages are ``spec-plan``, ``plan-tasks``, ``tasks-implement``,
    ``implement-qc``, and ``all``. Missing artifacts are reported as errors,
    never silently converted into a pass.
    """
    root = feature_dir.resolve()
    findings: list[BoundaryFinding] = []
    stages = {
        "spec-plan": ["spec-plan"],
        "plan-tasks": ["plan-tasks"],
        "tasks-implement": ["tasks-implement"],
        "implement-qc": ["implement-qc"],
        "all": ["spec-plan", "plan-tasks", "tasks-implement", "implement-qc"],
    }
    if stage not in stages:
        return [BoundaryFinding("error", "invalid-stage", f"Unsupported stage: {stage}")]

    for boundary in stages[stage]:
        if boundary == "spec-plan":
            _validate_spec_plan(root, findings)
        elif boundary == "plan-tasks":
            _validate_plan_tasks(root, findings)
        elif boundary == "tasks-implement":
            _validate_tasks_implement(root, findings)
        elif boundary == "implement-qc":
            _validate_implement_qc(root, findings)
    return findings


def _read(root: Path, name: str, findings: list[BoundaryFinding]) -> str | None:
    path = root / name
    if not path.is_file():
        findings.append(BoundaryFinding("error", "missing-artifact", f"Missing {name}"))
        return None
    return path.read_text(encoding="utf-8")


def _validate_spec_plan(root: Path, findings: list[BoundaryFinding]) -> None:
    spec = _read(root, "spec.md", findings)
    plan = _read(root, "plan.md", findings)
    if spec is None or plan is None:
        return

    p1_ids = extract_p1_requirement_ids(spec)
    coverage = parse_coverage_map(plan)
    for req_id in sorted(p1_ids):
        row = coverage.get(req_id)
        if row is None:
            findings.append(BoundaryFinding("error", "missing-coverage", f"P1 requirement {req_id} is absent from the Requirement Coverage Map"))
            continue
        if not row["file"]:
            findings.append(BoundaryFinding("error", "empty-coverage-file", f"P1 requirement {req_id} has no implementation file path"))
        if not row["symbol"]:
            findings.append(BoundaryFinding("error", "empty-coverage-symbol", f"P1 requirement {req_id} has no implementation symbol or API"))


def _validate_plan_tasks(root: Path, findings: list[BoundaryFinding]) -> None:
    spec = _read(root, "spec.md", findings)
    plan = _read(root, "plan.md", findings)
    tasks = _read(root, "tasks.md", findings)
    if spec is None or plan is None or tasks is None:
        return

    if len(tasks.encode("utf-8")) > 6144:
        findings.append(BoundaryFinding("error", "tasks-size", "tasks.md exceeds the 6 KB portability budget"))

    task_rows = parse_tasks(tasks)
    ids = [row["id"] for row in task_rows]
    if len(ids) != len(set(ids)):
        findings.append(BoundaryFinding("error", "duplicate-task-id", "tasks.md contains duplicate task IDs"))

    expected = [f"T{index:03d}" for index in range(1, len(ids) + 1)]
    if ids != expected:
        findings.append(BoundaryFinding("error", "task-id-sequence", "task IDs must be sequential from T001"))

    task_ids = set(ids)
    for row in task_rows:
        for dependency in row["after"]:
            if dependency not in task_ids:
                findings.append(BoundaryFinding("error", "missing-task-dependency", f"{row['id']} depends on missing {dependency}"))
            if dependency == row["id"]:
                findings.append(BoundaryFinding("error", "self-dependency", f"{row['id']} depends on itself"))

    cycle = find_dependency_cycle(task_rows)
    if cycle:
        findings.append(BoundaryFinding("error", "task-cycle", f"Circular task dependency: {' -> '.join(cycle)}"))

    p1_ids = extract_p1_requirement_ids(spec)
    tagged = {req_id for row in task_rows for req_id in row["requirements"]}
    for req_id in sorted(p1_ids - tagged):
        findings.append(BoundaryFinding("error", "untasked-requirement", f"P1 requirement {req_id} has no implementation task"))


def _validate_tasks_implement(root: Path, findings: list[BoundaryFinding]) -> None:
    tasks = _read(root, "tasks.md", findings)
    if tasks is None:
        return
    rows = parse_tasks(tasks)
    incomplete = [row["id"] for row in rows if not row["complete"] and "deferred=true" not in row["tail"].lower() and "[DEFERRED]" not in row["tail"].upper()]
    if (root / ".completed").exists() and incomplete:
        findings.append(BoundaryFinding("error", "false-completed", f".completed exists while tasks remain incomplete: {', '.join(incomplete)}"))


def _validate_implement_qc(root: Path, findings: list[BoundaryFinding]) -> None:
    marker = root / ".qc-passed"
    if not marker.exists():
        return
    report = root / "qc-report.md"
    if not report.is_file():
        findings.append(BoundaryFinding("error", "missing-qc-report", ".qc-passed exists without qc-report.md"))
        return
    body = report.read_text(encoding="utf-8")
    if not re.search(r"\bPASS\b", body, re.IGNORECASE):
        findings.append(BoundaryFinding("error", "qc-verdict-mismatch", ".qc-passed exists but qc-report.md has no PASS verdict"))


def extract_p1_requirement_ids(spec: str) -> set[str]:
    """Extract requirement IDs from lines that explicitly declare P1."""
    ids: set[str] = set()
    p1_section = False
    for line in spec.splitlines():
        if line.startswith("#"):
            p1_section = bool(P1_RE.search(line))
        if P1_RE.search(line):
            ids.update(REQ_RE.findall(line))
        elif p1_section:
            ids.update(REQ_RE.findall(line))
    return ids


def parse_coverage_map(plan: str) -> dict[str, dict[str, str]]:
    """Parse the SDD Pilot-style coverage table without requiring Markdown ASTs."""
    rows: dict[str, dict[str, str]] = {}
    in_table = False
    for line in plan.splitlines():
        if re.match(r"^##\s+Requirement Coverage Map\s*$", line, re.IGNORECASE):
            in_table = True
            continue
        if in_table and re.match(r"^##\s+", line):
            break
        if not in_table or not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or set(cells[0]) <= {"-", ":"}:
            continue
        req_id = cells[0]
        if REQ_RE.fullmatch(req_id):
            rows[req_id] = {"file": cells[2], "symbol": cells[3]}
    return rows


def parse_tasks(tasks: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line in tasks.splitlines():
        match = TASK_RE.match(line)
        if not match:
            continue
        state, task_id, tail = match.groups()
        rows.append({
            "id": task_id,
            "complete": state.upper() == "X",
            "tail": tail,
            "requirements": REQ_RE.findall(tail),
            "after": AFTER_RE.findall(tail),
        })
    return rows


def find_dependency_cycle(rows: Iterable[dict[str, object]]) -> list[str] | None:
    graph = {str(row["id"]): list(row["after"]) for row in rows}
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in visiting:
            index = stack.index(node)
            return stack[index:] + [node]
        if node in visited:
            return None
        visiting.add(node)
        stack.append(node)
        for dependency in graph.get(node, []):
            cycle = visit(dependency)
            if cycle:
                return cycle
        stack.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return None
