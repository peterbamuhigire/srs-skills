# 14. Workforce, Planning, and Asset Tables

## 14.1 Overview

These tables extend LonghornERP for the strengthened HR workforce model, the new Supply Chain Planning module, and the deeper enterprise asset-management workflows. They are additive and do not replace the existing execution-ledger tables.

## 14.2 HR Workforce Governance

### 14.2.1 `hr_positions`

Stores governed position master records by tenant.

Key columns:

- `id`
- `tenant_id`
- `position_code`
- `job_code`
- `department_id`
- `branch_id`
- `manager_position_id`
- `cost_center_id`
- `position_status`
- `budget_status`
- `effective_from`
- `effective_to`

### 14.2.2 `hr_position_assignments`

Stores effective-dated employee-to-position assignment history.

Key columns:

- `id`
- `tenant_id`
- `employee_id`
- `position_id`
- `assignment_status`
- `effective_from`
- `effective_to`
- `approved_change_request_id`

### 14.2.3 `payroll_calendars`

Stores payroll operating calendars and release deadlines by pay group.

Key columns:

- `id`
- `tenant_id`
- `pay_group_code`
- `period_start_date`
- `period_end_date`
- `cutoff_date`
- `approval_deadline`
- `payment_date`
- `statutory_due_date`

### 14.2.4 `payroll_validation_runs`

Stores pre-release payroll validation executions and summaries.

Key columns:

- `id`
- `tenant_id`
- `payroll_run_id`
- `validation_status`
- `finding_count`
- `generated_at`
- `generated_by`

### 14.2.5 `people_metric_snapshots`

Stores workforce KPI snapshots for dashboards and trending.

Key columns:

- `id`
- `tenant_id`
- `snapshot_period`
- `scope_type`
- `scope_id`
- `metric_code`
- `metric_value`
- `captured_at`

## 14.3 Supply Chain Planning

### 14.3.1 `demand_plan_versions`

Stores governed demand-plan headers.

Key columns:

- `id`
- `tenant_id`
- `plan_code`
- `planning_horizon_start`
- `planning_horizon_end`
- `version_status`
- `approved_by`
- `approved_at`

### 14.3.2 `demand_plan_lines`

Stores baseline and approved demand quantities by item-location-time bucket.

Key columns:

- `id`
- `tenant_id`
- `demand_plan_version_id`
- `item_id`
- `location_id`
- `time_bucket_start`
- `baseline_qty`
- `approved_qty`
- `forecast_method_code`

### 14.3.3 `demand_plan_overrides`

Stores governed manual overrides.

Key columns:

- `id`
- `tenant_id`
- `demand_plan_line_id`
- `override_qty`
- `reason_code`
- `override_owner_user_id`
- `expires_on`
- `created_at`

### 14.3.4 `supply_plan_runs`

Stores feasible supply-plan headers.

Key columns:

- `id`
- `tenant_id`
- `demand_plan_version_id`
- `run_status`
- `planning_horizon_start`
- `planning_horizon_end`
- `released_at`
- `released_by`

### 14.3.5 `replenishment_recommendations`

Stores released replenishment proposals for downstream execution.

Key columns:

- `id`
- `tenant_id`
- `supply_plan_run_id`
- `recommendation_type`
- `item_id`
- `source_location_id`
- `destination_location_id`
- `recommended_qty`
- `recommended_date`
- `release_status`

### 14.3.6 `inventory_policy_versions`

Stores effective-dated service and stock-policy sets.

Key columns:

- `id`
- `tenant_id`
- `policy_code`
- `service_class_code`
- `effective_from`
- `effective_to`
- `approval_status`
- `approved_by`

### 14.3.7 `sop_cycles`

Stores the monthly S&OP / IBP cycle headers.

Key columns:

- `id`
- `tenant_id`
- `cycle_month`
- `cycle_year`
- `cycle_status`
- `executive_owner_user_id`
- `released_plan_version_id`

### 14.3.8 `planning_scenarios`

Stores sandbox planning scenarios.

Key columns:

- `id`
- `tenant_id`
- `source_plan_type`
- `source_plan_version_id`
- `scenario_name`
- `scenario_status`
- `created_by`
- `created_at`

## 14.4 Enterprise Asset Management

### 14.4.1 `asset_functional_locations`

Stores functional-location hierarchy nodes.

Key columns:

- `id`
- `tenant_id`
- `location_code`
- `location_name`
- `parent_location_id`
- `location_status`
- `criticality_code`

### 14.4.2 `asset_work_requests`

Stores maintenance request intake records.

Key columns:

- `id`
- `tenant_id`
- `asset_id`
- `request_status`
- `symptom_code`
- `description`
- `requested_by_user_id`
- `screened_by_user_id`
- `screened_at`

### 14.4.3 `asset_work_orders`

Stores work-order headers.

Key columns:

- `id`
- `tenant_id`
- `asset_id`
- `work_order_code`
- `work_type_code`
- `priority_code`
- `is_planned_work`
- `work_order_status`
- `scheduled_start_at`
- `scheduled_finish_at`

### 14.4.4 `asset_job_plans`

Stores planning-package details for work orders.

Key columns:

- `id`
- `tenant_id`
- `work_order_id`
- `estimated_labour_hours`
- `required_skills_json`
- `required_materials_json`
- `permit_requirements_json`
- `safety_instructions_json`

### 14.4.5 `asset_condition_events`

Stores inspection, meter, and telemetry events.

Key columns:

- `id`
- `tenant_id`
- `asset_id`
- `event_source`
- `event_timestamp`
- `measurement_code`
- `measurement_value`
- `threshold_status`
- `recommended_action_code`

### 14.4.6 `asset_failure_events`

Stores structured failure and closeout evidence.

Key columns:

- `id`
- `tenant_id`
- `work_order_id`
- `asset_id`
- `failure_code`
- `cause_code`
- `remedy_code`
- `downtime_minutes`
- `recorded_at`

### 14.4.7 `asset_shutdown_packages`

Stores outage and turnaround packages.

Key columns:

- `id`
- `tenant_id`
- `package_code`
- `window_start_at`
- `window_end_at`
- `coordinator_user_id`
- `readiness_status`

## 14.5 Design Notes

- Planning and workforce history tables are effective-dated wherever historical truth must be reconstructable.
- Replenishment recommendations are recommendations, not execution transactions.
- Asset work-management tables preserve a clear split between request, plan, execution, and closeout evidence.
