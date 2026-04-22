# Industrial Module Architecture

## 12.1 Purpose

This section defines the first-class high-level architecture for Longhorn ERP's industrial domains: Product Lifecycle Management (PLM), MES-grade Manufacturing, and Transportation & Fleet Operations. These capabilities are modelled as peer bounded contexts, not as secondary features hidden inside inventory or asset accounting.

## 12.2 Bounded Contexts

### 12.2.1 PLM

`PLM` is the system of record for engineering truth. It owns:

- engineering item master
- controlled revisions
- EBOM and MBOM governance
- engineering change request and order workflow
- technical document control
- effectivity logic
- NPI stage gates
- controlled publication of released definitions downstream

### 12.2.2 Manufacturing

`Manufacturing` is the system of record for production execution and production economics. It owns:

- routings and work centres
- production orders and operation queues
- raw-material issue and backflush logic
- WIP state
- genealogy and traceability capture
- in-process quality execution
- rework and downtime tracking
- labour, overhead, yield, and scrap costing

### 12.2.3 Transportation & Fleet Operations

`Transportation` is the system of record for shipment movement and live fleet operations. It owns:

- shipment demand consolidation
- load and route planning
- dispatch and resource assignment
- trip milestones and ETA visibility
- transport exception management
- proof capture and trip closure
- freight settlement and transport analytics

`Assets` remains the owner of the vehicle as a capital asset, but not of live dispatch or trip state.

## 12.3 Component Model

### PLM Components

- `ProductDefinition Service` - engineering items, revisions, and BOM structures
- `EngineeringChange Service` - ECR/ECO workflow and approvals
- `DocumentControl Service` - controlled files, certificates, and release blockers
- `ReleasePublisher Service` - downstream publication to Inventory, Procurement, and Manufacturing
- `NPI Service` - stage-gate governance and readiness tracking

### Manufacturing Components

- `Routing Service` - operation definitions, work-centre sequencing, and standards
- `ProductionExecution Service` - order release, operation progression, and shift control
- `Genealogy Service` - lot/serial trace links from input to output
- `QualityExecution Service` - in-process checks, holds, and rework paths
- `Costing Service` - WIP, labour, overhead, and variance control

### Transportation Components

- `ShipmentPlanning Service` - shipment-order intake, grouping, and prioritisation
- `RoutePlanning Service` - route, stop, load, and capacity planning
- `Dispatch Service` - internal-fleet or carrier assignment and trip release
- `TripExecution Service` - milestones, ETA refresh, proof capture, and close-out
- `TransportControlTower Service` - exception queue and service recovery actions
- `FreightSettlement Service` - audit hold, approval, and cost posting

## 12.4 Cross-Module Integration Flows

### 12.4.1 PLM to Operations

1. Engineering releases a revision in `PLM`.
2. `ReleasePublisher Service` creates a controlled publication event.
3. `Inventory` receives stocking and identification metadata.
4. `Procurement` receives approved component and substitute context.
5. `Manufacturing` receives effective BOM and routing baseline.

No downstream module may silently mutate the released engineering baseline.

### 12.4.2 Operations to Transportation

1. `Sales`, `Procurement`, or `Inventory` creates physical-movement demand.
2. `Transportation` converts demand into shipment orders.
3. Loads and routes are planned.
4. Internal fleet or carrier resources are assigned.
5. Trip events and proofs are captured.
6. Settlement is posted to `Accounting`.

### 12.4.3 Transportation to Assets

`Transportation` may reference `Assets` for vehicle identity, maintenance hold state, insurance status, and odometer context. `Assets` does not own trip records, route stops, or dispatch queues.

## 12.5 High-Level Data Ownership Rules

| Concern | Owning Module |
|---|---|
| Engineering revision | `PLM` |
| Effective BOM and release baseline | `PLM` |
| Production operation status | `Manufacturing` |
| Production genealogy | `Manufacturing` |
| Vehicle asset book value and depreciation | `ASSETS` |
| Shipment route and dispatch state | `TRANSPORTATION` |
| Proof of delivery and freight settlement | `TRANSPORTATION` |

## 12.6 Failure and Recovery Boundaries

- Failure of PLM downstream publication shall not corrupt the released engineering revision; publication retries occur asynchronously with visible failure state.
- Failure of telematics or ETA refresh shall not block manual transportation execution, proof capture, or settlement.
- Failure of manufacturing machine-event ingestion shall not block manual operation progression.
- Cross-module financial postings shall remain transactionally consistent inside the owning module's posting boundary.
