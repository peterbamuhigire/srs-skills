# Workforce, Planning, and Asset Operations Test Cases

This section covers the newly strengthened HR governance controls, the Supply Chain Planning module, and enterprise asset-management workflows.

## HR Governance

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-HRG-001 | `PayrollShadowRunTest` | `test_shadow_run_never_posts_live_artifacts` | Execute a shadow payroll run for 50 employees | Valid payroll scope; mode = `SHADOW` | Shadow run completes; no GL journal, payment file, statutory payload, or employee-visible payslip is created |
| TC-HRG-002 | `PayrollSegregationTest` | `test_preparer_cannot_finally_approve_own_run_without_override` | Same user computes and attempts to approve payroll | `run_id`; session user = run preparer | HTTP 403 or validation error unless emergency override with second approval is provided |
| TC-HRG-003 | `PositionGovernanceTest` | `test_effective_dated_position_change_preserves_history` | Approve a position change effective next month | `employee_id`; target `position_id`; `effective_date` next month | Historical assignment remains unchanged before effective date; new assignment becomes active on effective date only |

## Supply Chain Planning

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-SCP-001 | `ForecastOverrideTest` | `test_override_preserves_baseline_and_reason` | Planner overrides baseline forecast | `line_id`; baseline 100; override 140; reason provided | Baseline remains 100; approved value = 140; reason, owner, and timestamp stored |
| TC-SCP-002 | `PlanReleaseTest` | `test_plan_release_is_idempotent_on_retry` | Release same approved supply plan twice due to retry | `run_id` released twice | Exactly 1 recommendation set published; no duplicate downstream records |
| TC-SCP-003 | `ScenarioIsolationTest` | `test_scenario_changes_do_not_touch_released_plan` | Planner edits a scenario cloned from released plan | Released plan version and scenario version | Released plan values unchanged; scenario values changed; comparison report reflects delta |
| TC-SCP-004 | `SopCycleTest` | `test_unresolved_major_exception_is_escalated_to_executive_review` | Shortage above escalation threshold remains unresolved | Cycle with configured threshold; shortage exception above threshold | Exception appears on executive-review agenda with escalation metadata |

## Enterprise Asset Management

| Test ID | PHPUnit Class | Method | Scenario | Input | Expected Result |
|---|---|---|---|---|---|
| TC-EAM-001 | `WorkRequestTest` | `test_duplicate_request_is_flagged_during_intake` | Submit a similar maintenance request for same asset twice | Same `asset_id`; matching symptom and category | Second request is saved or held with duplicate flag visible to planner |
| TC-EAM-002 | `MaterialReservationTest` | `test_short_material_creates_shortage_exception` | Reserve unavailable spare part against planned work order | `work_order_id`; required qty > available qty | Shortage exception created; linked procurement or transfer request action available |
| TC-EAM-003 | `ConditionEventTest` | `test_threshold_breach_creates_recommended_action` | Submit meter or inspection event above threshold | `asset_id`; threshold breached | Condition event stored; recommended inspection or corrective action generated |
| TC-EAM-004 | `WorkOrderCloseoutTest` | `test_corrective_work_order_requires_failure_coding` | Attempt to close corrective work without failure code | `work_order_id`; missing failure code | HTTP 422 or validation error; work order remains open |
