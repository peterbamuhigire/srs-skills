# 12. Workforce, Planning, and Asset Endpoints

## 12.1 HR Workforce Operations

### 12.1.1 Create Position

- `POST /api/v1/hr/positions`
- Purpose: create a governed position record with organisational and costing context.

### 12.1.2 Submit Workforce Change Request

- `POST /api/v1/hr/workforce-change-requests`
- Purpose: submit promotion, transfer, grade, or manager-change requests.

### 12.1.3 Generate Payroll Validation Pack

- `POST /api/v1/hr/payroll-runs/{runId}/validation-pack`
- Purpose: run pre-release payroll validation checks.

### 12.1.4 Start Shadow Payroll Run

- `POST /api/v1/hr/payroll/shadow-runs`
- Purpose: compute a non-posting payroll run for comparison and risk review.

### 12.1.5 Get Manager Dashboard

- `GET /api/v1/hr/manager-dashboard`
- Purpose: return scoped approvals, attendance exceptions, leave, and workforce metrics for the authenticated manager.

## 12.2 Supply Chain Planning

### 12.2.1 Create Demand Plan Version

- `POST /api/v1/scp/demand-plans`
- Purpose: generate a baseline demand-plan version for a planning horizon.

### 12.2.2 Apply Demand Override

- `POST /api/v1/scp/demand-plan-lines/{lineId}/overrides`
- Purpose: apply a governed forecast override.

### 12.2.3 Approve Consensus Demand

- `POST /api/v1/scp/demand-plans/{versionId}/approve`
- Purpose: promote a demand-plan version into approved consensus demand.

### 12.2.4 Create Supply Plan Run

- `POST /api/v1/scp/supply-plans`
- Purpose: generate a feasible supply-plan run from an approved demand-plan version.

### 12.2.5 Publish Replenishment Recommendations

- `POST /api/v1/scp/supply-plans/{runId}/publish`
- Purpose: release approved recommendations to downstream execution modules.

### 12.2.6 Create Planning Scenario

- `POST /api/v1/scp/scenarios`
- Purpose: clone an existing plan version into a scenario sandbox.

### 12.2.7 Compare Scenario

- `POST /api/v1/scp/scenarios/{scenarioId}/compare`
- Purpose: compare a scenario with the released plan using service, shortage, inventory, and financial metrics.

### 12.2.8 Create S&OP Cycle

- `POST /api/v1/scp/sop-cycles`
- Purpose: create a monthly S&OP / IBP governance cycle.

## 12.3 Asset Work Management and Reliability

### 12.3.1 Create Work Request

- `POST /api/v1/assets/work-requests`
- Purpose: register a maintenance request against an asset.

### 12.3.2 Convert Request to Work Order

- `POST /api/v1/assets/work-requests/{requestId}/convert`
- Purpose: screen a request and convert it into a planned work order.

### 12.3.3 Reserve Materials for Work Order

- `POST /api/v1/assets/work-orders/{workOrderId}/materials/reserve`
- Purpose: reserve MRO materials through inventory integration.

### 12.3.4 Create Shutdown Package

- `POST /api/v1/assets/shutdown-packages`
- Purpose: group work orders into a governed outage package.

### 12.3.5 Record Condition Event

- `POST /api/v1/assets/condition-events`
- Purpose: capture and evaluate inspection, meter, or telemetry events.

### 12.3.6 Close Work Order

- `POST /api/v1/assets/work-orders/{workOrderId}/close`
- Purpose: submit structured closeout with failure coding and completion evidence.

### 12.3.7 Get Reliability Dashboard

- `GET /api/v1/assets/reliability-dashboard`
- Purpose: return PM compliance, MTBF, MTTR, backlog, and bad-actor metrics.

## 12.4 API Notes

- All mutating endpoints require authenticated users, RBAC checks, and audit-event capture.
- Shadow payroll and planning scenario endpoints must preserve isolation from live posted state.
- Plan-publication endpoints must support idempotency to avoid duplicate downstream recommendation events.
- Asset work-order and condition-event endpoints must accept mobile-friendly payloads for field execution workflows.
