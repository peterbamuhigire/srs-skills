from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_b10_fit_and_trace_references_cover_normal_and_failure_paths() -> None:
    problem_goal = _read(
        "02-requirements-engineering/references/problem-goal-fixture.md"
    )
    event_slice = _read(
        "02-requirements-engineering/references/event-centred-slice.md"
    )
    fit_criteria = _read(
        "02-requirements-engineering/references/fit-criteria-oracles.md"
    )

    assert "status: ready-for-review" in problem_goal
    assert "solution-only" in problem_goal
    assert "BLOCKED" in problem_goal
    assert "trace_links:" in event_slice
    assert "PG-001" in event_slice and "REQ-001" in event_slice and "TEST-001" in event_slice
    assert "Orphan-link check" in event_slice
    assert "normal_case" in fit_criteria
    assert "boundary_case" in fit_criteria
    assert "Adjective-only criterion" in fit_criteria
    assert "NOT_ASSESSED" in fit_criteria


def test_pause_dependency_contract_blocks_missing_resource() -> None:
    checklist = _read("references/pause-point-checklist.md")
    dependency = _read("references/checklist-dependency-exceptions.md")

    assert "Pause outcome" in checklist
    assert "omitted-step fixture must produce `BLOCKED` or `NOT_ASSESSED`" in checklist
    assert "status: missing" in dependency
    assert "expected_result: BLOCKED" in dependency
    assert "must not infer a" in dependency
    assert "never `PASS`" in dependency


def test_pilot_template_downgrades_post_only_evidence() -> None:
    pilot = _read("references/checklist-pilot-evaluation.md")

    assert "baseline" in pilot
    assert "countercase" in pilot
    assert "confounders" in pilot
    assert "post-pilot measure" in pilot
    assert "NOT_ASSESSED" in pilot
    assert "association" in pilot


def test_healthcare_state_and_review_contracts_preserve_human_controls() -> None:
    care_to_cash = _read("references/healthcare-care-to-cash-state-and-evidence.md")
    denial = _read("references/healthcare-denial-and-compliance-review.md")
    roles = _read("references/healthcare-role-credential-and-competency-lifecycle.md")
    listening = _read("references/healthcare-listening-and-safe-service-blueprint.md")

    assert "paid-reconciled" in care_to_cash
    assert "without remittance and reconciliation evidence" in care_to_cash
    assert "quarantined" in care_to_cash
    assert "No denial closes without disposition evidence" in denial
    assert "expected_result: BLOCKED" in denial
    assert "automated diagnosis" in denial
    assert "Expired, missing, or unverified evidence blocks restricted action" in roles
    assert "expected_result: BLOCKED" in roles
    assert "preserves the current state, escalation route" in listening
    assert "No clinical action is automated" in listening


def test_all_wave_one_references_declare_source_boundary() -> None:
    references = [
        "02-requirements-engineering/references/problem-goal-fixture.md",
        "02-requirements-engineering/references/event-centred-slice.md",
        "02-requirements-engineering/references/fit-criteria-oracles.md",
        "references/pause-point-checklist.md",
        "references/checklist-dependency-exceptions.md",
        "references/checklist-pilot-evaluation.md",
        "references/healthcare-care-to-cash-state-and-evidence.md",
        "references/healthcare-denial-and-compliance-review.md",
        "references/healthcare-role-credential-and-competency-lifecycle.md",
        "references/healthcare-listening-and-safe-service-blueprint.md",
    ]

    for relative in references:
        text = _read(relative)
        assert "## Source and currentness" in text
        assert "independent synthesis" in text
        assert "NOT_ASSESSED" in text or "NO_TIME_SENSITIVE_CLAIMS" in text
