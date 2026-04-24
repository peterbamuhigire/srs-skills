# LonghornERP Manufacturing, Transportation, Fleet, PLM, and MES Enhancement Roadmap

## Purpose

This document translates the following source books into concrete enhancement decisions for LonghornERP:

- `C:\Users\Peter\Downloads\ERP Playbook\Product Lifecycle Management System Playbook.epub`
- `C:\Users\Peter\Downloads\ERP Playbook\Manufacturing Execution System Playbook.epub`
- `C:\Users\Peter\Downloads\ERP Playbook\Transportation Management System Playbook.epub`

The goal is not to copy the books into LonghornERP. The goal is to decide what LonghornERP must add, what it must not collapse into existing modules, and how to sequence the rollout so manufacturing, transportation, and fleet management become ERP-grade rather than lightweight feature lists.

## Executive Decision

LonghornERP should be enhanced along 3 distinct capability lines:

1. Keep `MANUFACTURING` as the commercial module, but deepen it with true MES-grade execution capabilities.
2. Add a dedicated `TRANSPORTATION` add-on module instead of treating transport as a mixture of Sales delivery and Asset fleet logs.
3. Add a dedicated `PLM` add-on module instead of overloading Inventory item master and Manufacturing BOMs with engineering-control responsibilities.

The books make one point very clearly: ERP, MES, TMS, and PLM are adjacent systems with shared data, but they do not own the same decisions. LonghornERP should preserve that boundary even if some tenants buy the capabilities as a bundled suite.

## Critical Findings from the Books

## 1. PLM is not "better BOM management"

The PLM playbook positions PLM as the system of record for:

- product data management
- controlled BOM and revision history
- engineering change and release workflows
- configuration and variant governance
- effectivity control by date, plant, serial range, and baseline
- new product introduction and stage-gate governance
- quality and compliance evidence linked to product definitions
- digital-thread handoff to ERP, MES, QMS, EAM, SCM, CRM, CAD, CAE, and ALM

Critical implication for LonghornERP:

- Inventory item master and Manufacturing BOMs are necessary, but they are not PLM.
- Without revision control, effectivity, engineering change, release approval, and document linkage, LonghornERP cannot claim serious manufacturing depth for regulated or multi-variant manufacturers.

## 2. MES is not "production orders plus costing"

The MES playbook treats MES as the execution-control layer for:

- order dispatch and order-to-execution control
- material issuance and traceable consumption
- WIP control and operation status discipline
- in-process quality execution
- traceability and genealogy
- shift handover and daily management
- equipment connectivity and performance capture
- downtime, loss-tree, and OEE analytics
- master data discipline for routings, resources, materials, specifications, and event taxonomies

Critical implication for LonghornERP:

- The current Manufacturing module is strong at ERP manufacturing planning and costing.
- It is not yet strong enough at shop-floor execution discipline.
- A manufacturer running batch production, assembly, packaging, or food processing will need routings, operation-level status, material validation, traceability capture, in-process holds, rework controls, and performance event tracking.

## 3. TMS is not "delivery note plus vehicle register"

The TMS playbook defines TMS around:

- transportation planning and optimization
- shipment execution
- visibility and exception management
- freight audit, payment, and analytics
- carrier strategy, sourcing, and performance
- load planning and consolidation
- dispatch, appointment, and delivery recovery workflows
- control-tower operations under network stress
- integration with ERP, WMS, fleet visibility, and external carriers

Critical implication for LonghornERP:

- Sales delivery notes and POD capture are useful, but they are not transportation management.
- Asset fleet mileage, fuel, and service logs are useful, but they are not transportation management either.
- A serious transport-capable ERP needs shipment planning, route assignment, dispatch, ETA visibility, exception ownership, freight-cost control, and settlement.

## Current LonghornERP Position

## Strengths already present

LonghornERP already has a solid base in these areas:

- Manufacturing SRS covers BOMs, production orders, raw material issue, WIP, QC checkpoints, scrap, overhead absorption, and production costing.
- Advanced Inventory already provides batch tracking, FEFO, multi-location warehousing, and stock-in-transit patterns.
- Sales already supports delivery notes and proof of delivery.
- Assets already supports fleet asset master data, mileage logs, fuel logs, service records, service reminders, and fleet utilisation reporting.
- Platform services already provide module activation, auditability, mobile API, localisation, and integration primitives.

## Critical gaps

### Gap A: No PLM bounded context

Current project documentation shows no dedicated PLM capability for:

- engineering document control
- released versus obsolete product revisions
- engineering change request / change order / release workflow
- effectivity dates and serial-range validity
- approved supplier and approved substitute governance from an engineering perspective
- NPI stage-gate control
- product compliance dossier and design history traceability

Result:

- Engineering truth is at risk of being spread across Inventory, Manufacturing, and ad hoc files.
- Multi-variant or regulated manufacturing will break first.

### Gap B: Manufacturing is ERP-centric, not MES-grade

The current Manufacturing scope appears to stop short of full shop-floor execution control. The books imply LonghornERP still needs:

- routing and operation-sequence design
- work centre and resource calendars
- dispatch lists and operation start/complete controls
- operation-level labour, machine-hour, and downtime event capture
- shift handover workflow
- in-process status definitions stronger than a generic production-order state
- genealogy capture across raw material lots, WIP, finished goods, and rework
- quality hold, deviation, nonconformance, and governed rework flows at operation level
- OEE and loss-code model grounded in a standard KPI dictionary
- equipment / PLC / machine-signal integration as a later-phase extension

Result:

- LonghornERP can support manufacturing accounting and order management.
- It will struggle to control actual shop-floor execution for higher-discipline manufacturers.

### Gap C: Transportation is fragmented across modules

Current transportation-related capability is split across:

- Sales delivery note workflows
- Inventory transfer dispatch and receipt
- Asset fleet logging

What is missing compared with the TMS playbook:

- shipment planning workbench
- load building and consolidation
- route planning and optimization
- carrier management and rate logic
- dispatch board
- live shipment milestones and ETA management
- severity-based exception queue
- delivery appointment and recovery workflow
- freight audit and invoice validation
- transport cost allocation and lane analytics
- planner control-tower workflow

Result:

- LonghornERP can record that goods moved.
- It cannot yet manage transport as an operating discipline.

### Gap D: Fleet operations are mixed with fleet accounting

The current Assets fleet coverage is appropriate for:

- capitalisation
- depreciation
- maintenance records
- mileage and fuel history
- service due alerts

It is not sufficient for:

- trip planning
- route adherence
- vehicle dispatch
- driver scheduling
- load assignment
- live GPS / telematics ingestion
- delivery execution visibility
- transport exception handling

Result:

- The current fleet design is an asset-management view of vehicles, not a transport-operations view of vehicles.

## Recommended Module Boundaries

## 1. `MANUFACTURING` remains, but gains an MES execution subdomain

Recommendation:

- Keep the existing `MANUFACTURING` add-on as the tenant-facing commercial module.
- Internally split it into 2 subdomains:
  - Manufacturing Planning and Costing
  - Manufacturing Execution

Manufacturing Planning and Costing should continue to own:

- BOM consumption logic for released structures
- production order commercial quantities
- material cost, labour cost, overhead, WIP, yield, scrap, and GL posting

Manufacturing Execution should newly own:

- routings and operation definitions
- work centres and resources
- dispatching and execution states
- operation-level confirmations
- in-process quality checks
- genealogy and traceability events
- downtime and performance events
- rework loops and exception controls

This keeps pricing simple for SMEs while preserving a correct architecture.

## 2. Add `PLM` as a distinct add-on module

Recommendation:

- Create a new `PLM` module with its own SRS and data model.

`PLM` should own:

- product family and product structure governance
- engineering BOM and revision control
- document control for drawings, specifications, and technical files
- engineering change workflow
- release approval and effectivity logic
- NPI stage-gate control
- compliance and certification evidence tied to product revision

`PLM` should publish released product definitions to:

- `MANUFACTURING` for routings and production use
- `INVENTORY` for item and stocking master updates
- `PROCUREMENT` for approved part and supplier visibility

Do not let `MANUFACTURING` own engineering release governance.

## 3. Add `TRANSPORTATION` as a distinct add-on module

Recommendation:

- Create a dedicated `TRANSPORTATION` module instead of stretching Sales and Assets beyond their natural boundaries.

`TRANSPORTATION` should own:

- shipment planning
- trip / route / stop planning
- dispatch and assignment
- carrier or internal-fleet allocation
- ETA and milestone visibility
- exception management
- freight audit and settlement
- transport analytics by lane, carrier, vehicle, customer, and branch

It should integrate with:

- `SALES` for outbound delivery demand
- `PROCUREMENT` for inbound logistics and supplier shipment visibility
- `INVENTORY` and `ADV_INVENTORY` for shipment origin, destination, staging, and receipt confirmation
- `ASSETS` for vehicle identity and depreciation linkage
- `HR_PAYROLL` for driver master and payroll-cost interfaces where relevant
- `ACCOUNTING` for accrued freight, carrier payables, and cost allocation

## 4. Keep fleet accounting in `ASSETS`; move fleet operations to `TRANSPORTATION`

Recommendation:

- `ASSETS` remains the owner of the vehicle as a capital asset.
- `TRANSPORTATION` becomes the owner of the vehicle as an operating transport resource.

Boundary rule:

- If the concern is depreciation, insurance, maintenance capitalization, tax treatment, or asset register integrity, it belongs in `ASSETS`.
- If the concern is dispatch, route execution, driver assignment, GPS tracking, trip exceptions, or transport utilization, it belongs in `TRANSPORTATION`.

This is the cleanest way to support both accounting integrity and operational control.

## Must-Have Capability Additions

## A. MES-grade additions to Manufacturing

LonghornERP should add the following requirements to the Manufacturing stream:

- routing versioning and release status
- work centre master and capacity calendar
- operation queue and dispatch status
- operation start, pause, complete, and hold events
- scan-based material issue validation by lot / serial / batch
- genealogy graph from consumed material to produced lot
- in-process QC plan tied to operation or stage
- nonconformance, deviation, and governed rework records
- shift handover checklist and unresolved-issue carry-forward
- downtime taxonomy and OEE metrics
- machine-event integration interface for later IoT rollout

## B. PLM additions

LonghornERP should add the following PLM capabilities:

- controlled engineering item master separate from stock item convenience fields
- EBOM to MBOM transformation rule set
- revision and effectivity engine
- engineering change request, change review, change order, and release workflow
- drawing / spec / SOP document linkage
- configurable product family and option governance
- NPI stage-gate tracker
- compliance artifact store for approvals, certifications, and test evidence

## C. Transportation additions

LonghornERP should add the following Transportation capabilities:

- shipment order creation from sales, procurement, and stock transfer demand
- route and stop planning
- load consolidation and cube / weight checks
- internal fleet versus third-party carrier allocation
- dispatch board and trip sheet
- shipment milestone tracking
- ETA calculation and late-shipment alerting
- severity-ranked exception queue with ownership and SLA
- appointment scheduling and rescheduling
- freight invoice audit against planned lane / trip cost
- proof of pickup and proof of delivery capture
- transport performance scorecards and cost analytics

## D. Fleet operations additions

LonghornERP should add the following operational fleet capabilities under Transportation:

- driver-to-vehicle assignment history
- trip authorisation and trip close-out
- route adherence and deviation capture
- telematics ingestion interface
- utilisation by vehicle, driver, route, and branch
- fuel-event reconciliation against trip and odometer context
- maintenance-block rule so unavailable vehicles cannot be dispatched

## Cross-Module Digital Thread

The books repeatedly reinforce that value appears when lifecycle systems are linked, not isolated.

LonghornERP should implement this digital thread:

1. `PLM` releases a product revision, BOM, routing baseline, and quality instructions.
2. `MANUFACTURING` consumes the released baseline for execution and costing.
3. `ADV_INVENTORY` and `INVENTORY` manage physical material, lot, bin, and finished-goods state.
4. `TRANSPORTATION` plans and executes inbound, inter-branch, and outbound movement.
5. `SALES`, `PROCUREMENT`, and `ACCOUNTING` consume operational facts for commercial and financial closure.
6. `AUDIT` preserves who changed what, when, why, and under which approval.

This is the correct LonghornERP interpretation of the digital thread. It does not require external systems on day 1, but it does require proper ownership boundaries on day 1.

## Anti-Patterns to Avoid

- Do not treat PLM as an extra tab on the Inventory item master.
- Do not treat MES as a more detailed production-order screen.
- Do not treat TMS as a prettier delivery note module.
- Do not treat fleet management as only fuel and maintenance logs.
- Do not let product revision, routing release, shipment dispatch, and financial posting share one generic status field.
- Do not mix engineering truth, execution truth, and accounting truth in the same table without explicit state and audit boundaries.

## Rollout Recommendation

## Phase 1. Architectural correction and module inventory update

Update project-level vision and module documentation so LonghornERP explicitly includes:

- deeper MES-grade Manufacturing scope
- new `PLM` add-on
- new `TRANSPORTATION` add-on
- clarified `ASSETS` versus `TRANSPORTATION` fleet boundary

## Phase 2. Manufacturing SRS uplift

Extend the current Manufacturing SRS with MES-grade sections for:

- routing and operations
- work centres and resources
- execution dispatch and confirmations
- traceability and genealogy
- in-process quality and rework
- downtime and OEE
- shift handover

## Phase 3. Transportation SRS creation

Create a new `TRANSPORTATION` module SRS covering:

- planning
- dispatch
- visibility
- exceptions
- freight settlement
- fleet operations integration

## Phase 4. PLM SRS creation

Create a new `PLM` module SRS covering:

- product data
- revision and effectivity
- engineering change
- NPI
- compliance and release control

## Phase 5. HLD and ERD alignment

Update HLD, LLD, and database design artifacts so the new module boundaries are reflected in:

- bounded contexts
- integration flows
- event ownership
- shared keys and reference objects
- audit and approval patterns

## Priority File Changes for the Next Authoring Pass

The next document-authoring pass should update or create these project files:

- `projects/LonghornERP/_context/modules.md`
- `projects/LonghornERP/01-strategic-vision/01-prd/05-module-overview.md`
- `projects/LonghornERP/01-strategic-vision/01-prd/06-feature-requirements.md`
- `projects/LonghornERP/03-design-documentation/01-hld/01-system-overview.md`
- `projects/LonghornERP/03-design-documentation/04-database-design/01-overview.md`
- `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/08-manufacturing/`
- `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/14-assets/`
- `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/16-plm/`
- `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/17-transportation/`

## Final Recommendation

If LonghornERP wants to serve manufacturers and transport-heavy organisations seriously, the correct strategy is:

- deepen Manufacturing into true MES-grade execution
- add PLM as the engineering-control layer
- add Transportation as the logistics-control layer
- keep Assets focused on asset accounting and maintenance integrity
- let fleet operations live primarily in Transportation with controlled sync back to Assets

That is the cleanest route to an ERP that handles manufacturing, transportation, and fleet management properly without collapsing unlike business domains into one oversized module.
