# Workforce, Planning, and Asset Operations Architecture

## 15.1 Purpose

This section defines the high-level architecture for 3 cross-functional operating domains strengthened in this revision:

- governed workforce operations inside `HR_PAYROLL`
- forward-looking planning inside `SUPPLY_CHAIN_PLANNING`
- enterprise asset work management and reliability inside `ASSETS`

These domains remain peers of the existing accounting, inventory, procurement, manufacturing, and transportation capabilities. None should be collapsed into generic admin screens or ungoverned side workflows.

## 15.2 Bounded Contexts

### 15.2.1 HR and Payroll Workforce Operations

`HR_PAYROLL` is the system of record for:

- worker and employment history
- job and position governance
- manager and employee self-service workflows
- payroll calendars, validation, and release controls
- workforce analytics and operational HR dashboards

`ACCOUNTING` remains the owner of the finance book of record. `USER_MGMT` remains the owner of platform identity and permission enforcement.

### 15.2.2 Supply Chain Planning

`SUPPLY_CHAIN_PLANNING` is the system of record for:

- consensus demand versions
- supply-plan versions
- inventory-policy versions
- S&OP / IBP cycle state
- planning scenarios and released plan views

Execution modules remain the owners of actual transactions:

- `PROCUREMENT` owns purchase execution
- `INVENTORY` and `ADV_INVENTORY` own stock movements and location truth
- `MANUFACTURING` owns production execution
- `TRANSPORTATION` owns movement execution

### 15.2.3 Enterprise Asset Management

`ASSETS` is the system of record for:

- asset registry and functional locations
- asset criticality and lifecycle status
- work requests, work orders, and shutdown packages
- maintenance history, failure evidence, and condition events
- asset-side reliability analytics

`INVENTORY` owns stocked-material balances and reservations. `PROCUREMENT` owns purchasing and supplier obligations. `TRANSPORTATION` remains the owner of live fleet dispatch and trip state.

## 15.3 Component Model

### HR and Payroll Components

- `PositionGovernance Service` - job families, positions, approvals, and effective-dated workforce changes
- `PayrollControl Service` - calendars, validation packs, variance review, shadow runs, and release checklists
- `ManagerSelfService Service` - manager approvals and scoped workforce actions
- `WorkforceAnalytics Service` - headcount, absenteeism, overtime, payroll, and change metrics

### Supply Chain Planning Components

- `DemandPlanning Service` - baseline forecasts, overrides, and consensus-demand governance
- `SupplyPlanning Service` - feasible supply, replenishment recommendations, and shortage exceptions
- `InventoryPolicy Service` - service classes, safety stock, and policy versioning
- `SopCycle Service` - demand review, supply review, executive review, and plan release
- `Scenario Service` - sandbox scenario creation, comparison, and decision capture

### Asset Management Components

- `AssetHierarchy Service` - functional locations, hierarchy, and asset criticality
- `WorkManagement Service` - work requests, planning packages, scheduling, and shutdown packages
- `Reliability Service` - failure coding, repeat-failure detection, and KPI computation
- `ConditionEvent Service` - inspection, meter, and telemetry threshold evaluation

## 15.4 Cross-Module Integration Flows

### 15.4.1 Workforce to Finance and Access Control

1. A manager or HR officer initiates a workforce or payroll control action.
2. `HR_PAYROLL` validates reporting scope, position state, and payroll calendar state.
3. Approved payroll runs publish GL-ready outcomes to `ACCOUNTING`.
4. Access scope remains enforced through `USER_MGMT` and RBAC claims.

### 15.4.2 Planning to Execution

1. `SUPPLY_CHAIN_PLANNING` ingests demand, inventory, procurement, manufacturing, and transport context.
2. Demand, supply, and inventory-policy versions are generated and reviewed.
3. Approved plans are released as recommendations.
4. Downstream execution modules decide whether and when to turn those recommendations into live transactions.

### 15.4.3 Assets to Materials and Supply

1. `ASSETS` creates or plans work orders.
2. Required materials are reserved against `INVENTORY` when available.
3. Shortages raise procurement or transfer demand through controlled handoff.
4. Closeout data and reliability events remain owned by `ASSETS`.

## 15.5 Data Ownership Rules

| Concern | Owning Module |
|---|---|
| Effective-dated worker history | `HR_PAYROLL` |
| Payroll release checklist and shadow-run evidence | `HR_PAYROLL` |
| Consensus demand version | `SUPPLY_CHAIN_PLANNING` |
| Released replenishment recommendation | `SUPPLY_CHAIN_PLANNING` |
| Purchase order and goods receipt | `PROCUREMENT` / `INVENTORY` |
| Functional location and asset criticality | `ASSETS` |
| Work-request and work-order closeout evidence | `ASSETS` |
| Stock balance and reserved quantity | `INVENTORY` |

## 15.6 Failure and Recovery Boundaries

- Failure of a shadow payroll run shall not affect live payroll postings, payslips, or disbursement artifacts.
- Failure of plan release shall not create duplicate downstream recommendations; release retry remains idempotent.
- Failure of external telemetry ingestion shall not block manual inspection or work-order workflows inside `ASSETS`.
- Failure of inventory reservation during asset work planning shall create a shortage exception rather than silently dropping required materials.
