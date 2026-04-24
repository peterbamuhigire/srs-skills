# Workforce, Planning, and Asset Services - Low-Level Design

## Overview

This section specifies the service-layer design for the expanded workforce, planning, and enterprise asset-management capabilities introduced in this documentation pass.

---

## PositionGovernanceService

**Namespace:** `App\Modules\HRPayroll`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `ApprovalWorkflowService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createPosition(array $data): int` | Position payload with `position_code`, `job_code`, `department_id`, `branch_id`, `manager_position_id`, and `cost_center_id` | New `hr_positions.id` | Creates a budgetable position record. |
| `submitWorkforceChange(int $employeeId, array $change): int` | Employee primary key and change payload | New `hr_workforce_change_requests.id` | Creates a governed workforce change request with effective date and approval path. |
| `applyApprovedChange(int $requestId): void` | Request primary key | `void` | Writes effective-dated assignment history after approval. |

**Tables read/written:** `hr_positions`, `hr_position_assignments`, `hr_workforce_change_requests`

---

## PayrollControlService

**Namespace:** `App\Modules\HRPayroll`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `PayrollEngineService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createPayrollCalendar(array $data): int` | Pay-group calendar payload | New `payroll_calendars.id` | Creates a payroll operating calendar and deadlines. |
| `generateValidationPack(int $runId): int` | Payroll run primary key | New `payroll_validation_runs.id` | Runs pre-release validation and stores findings. |
| `runShadowPayroll(array $scope): int` | Shadow-run scope and comparison inputs | New `payroll_shadow_runs.id` | Computes a non-posting payroll run for variance review. |

**Tables read/written:** `payroll_calendars`, `payroll_validation_runs`, `payroll_validation_findings`, `payroll_shadow_runs`

---

## WorkforceAnalyticsService

**Namespace:** `App\Modules\HRPayroll`

**Module guard:** `ModuleRegistry::isActive('HR_PAYROLL', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `refreshSnapshot(string $period): int` | Period in `YYYY-MM` format | New `people_metric_snapshots.id` | Rebuilds workforce metrics for the tenant and period. |
| `getManagerDashboard(int $managerUserId, array $filters): array` | Manager user primary key and scope filters | Dashboard payload | Returns approvals, leave, attendance, probation, and headcount widgets. |
| `getWorkforceMetrics(array $filters): array` | Date and scope filters | Analytics rows and KPI totals | Returns workforce and payroll metrics for dashboards. |

**Tables read/written:** `people_metric_snapshots`, `people_metric_snapshot_lines`

---

## DemandPlanningService

**Namespace:** `App\Modules\SupplyChainPlanning`

**Module guard:** `ModuleRegistry::isActive('SUPPLY_CHAIN_PLANNING', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createDemandPlanVersion(array $scope): int` | Horizon, item, location, and segment filters | New `demand_plan_versions.id` | Creates a demand-plan header and baseline lines. |
| `applyOverride(int $lineId, array $override): int` | Demand-plan line primary key and override payload | New `demand_plan_overrides.id` | Applies a governed override while preserving the baseline value. |
| `approveConsensusDemand(int $versionId): void` | Demand-plan version primary key | `void` | Sets the version to approved consensus demand. |

**Tables read/written:** `demand_plan_versions`, `demand_plan_lines`, `demand_plan_overrides`

---

## SupplyPlanningService

**Namespace:** `App\Modules\SupplyChainPlanning`

**Module guard:** `ModuleRegistry::isActive('SUPPLY_CHAIN_PLANNING', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `DemandPlanningService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createSupplyPlan(int $demandVersionId, array $scope): int` | Approved demand-plan version and planning scope | New `supply_plan_runs.id` | Creates a feasible supply-plan run. |
| `publishRecommendations(int $runId): int` | Supply-plan run primary key | Count of recommendations published | Writes released replenishment recommendations. |
| `getExceptionWorkbench(array $filters): array` | Filters for shortage, capacity, late-supply, or policy exceptions | Exception rows | Returns actionable planning exceptions. |

**Tables read/written:** `supply_plan_runs`, `supply_plan_lines`, `planning_exceptions`, `replenishment_recommendations`

---

## SopCycleService

**Namespace:** `App\Modules\SupplyChainPlanning`

**Module guard:** `ModuleRegistry::isActive('SUPPLY_CHAIN_PLANNING', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `DemandPlanningService`, `SupplyPlanningService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createCycle(array $data): int` | Cycle payload with horizon and due dates | New `sop_cycles.id` | Creates the monthly S&OP / IBP cycle. |
| `createScenario(int $sourceVersionId, array $meta): int` | Source plan version and scenario metadata | New `planning_scenarios.id` | Clones plan data into an isolated scenario. |
| `recordExecutiveDecision(int $cycleId, array $decision): int` | Cycle primary key and decision payload | New `sop_decisions.id` | Records an approved trade-off or escalation outcome. |

**Tables read/written:** `sop_cycles`, `sop_cycle_steps`, `planning_scenarios`, `planning_scenario_lines`, `sop_decisions`

---

## AssetWorkManagementService

**Namespace:** `App\Modules\Assets`

**Module guard:** `ModuleRegistry::isActive('ASSETS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `InventoryReservationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createWorkRequest(array $data): int` | Work-request payload | New `asset_work_requests.id` | Creates a new screened maintenance request candidate. |
| `convertToWorkOrder(int $requestId, array $plan): int` | Work-request primary key and planning payload | New `asset_work_orders.id` | Creates the work order and optional planning package. |
| `createShutdownPackage(array $data): int` | Shared outage metadata and work-order list | New `asset_shutdown_packages.id` | Groups work orders into a governed outage package. |

**Tables read/written:** `asset_work_requests`, `asset_work_orders`, `asset_job_plans`, `asset_shutdown_packages`, `asset_shutdown_package_lines`

---

## AssetReliabilityService

**Namespace:** `App\Modules\Assets`

**Module guard:** `ModuleRegistry::isActive('ASSETS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `recordCloseout(int $workOrderId, array $closeout): void` | Work-order primary key and closeout payload | `void` | Stores structured closeout and failure coding. |
| `ingestConditionEvent(array $event): int` | Condition payload from inspection, meter, or telemetry source | New `asset_condition_events.id` | Persists and evaluates condition event thresholds. |
| `refreshReliabilityMetrics(array $scope): void` | Scope filters | `void` | Recomputes MTBF, MTTR, PM compliance, and bad-actor markers. |

**Tables read/written:** `asset_work_order_closeouts`, `asset_failure_events`, `asset_condition_events`, `asset_reliability_snapshots`
