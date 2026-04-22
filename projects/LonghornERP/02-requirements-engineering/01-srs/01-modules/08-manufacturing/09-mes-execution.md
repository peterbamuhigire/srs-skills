# MES-Grade Execution Extension

## 9.1 Routing and Operation Governance

**FR-MFG-046** - The system shall support routing definitions per finished good or BOM version, where each routing contains an ordered set of operations. Each operation shall record: operation code, operation name, work centre, standard setup time, standard run time, labour skill requirement, and whether in-process quality clearance is mandatory before the next operation may begin.

**FR-MFG-047** - When a production order is released, the system shall generate an operation queue derived from the effective routing, and shall allow supervisors to dispatch operations by work centre, shift, and priority. The operation queue shall show at minimum: production order, operation sequence, planned quantity, assigned work centre, planned start, planned finish, and current operation status.

## 9.2 Operation Execution and Event Capture

**FR-MFG-048** - The system shall support operation-level execution events with the statuses `queued`, `ready`, `in_progress`, `paused`, `quality_hold`, `completed`, and `rework`. Every status transition shall record actor identity, timestamp, work centre, and optional reason code where the transition is not part of the normal happy path.

**FR-MFG-049** - When a production order uses batch-tracked, serial-tracked, or lot-controlled raw materials, the system shall support scan-based or manual capture of the exact consumed lots or serials at the operation where consumption occurs. The system shall link the consumed material identity to the in-process or finished output identity so that upstream-to-downstream genealogy is reconstructible for every production batch.

## 9.3 Shift Handover and Exception Continuity

**FR-MFG-050** - At the close of a production shift, the system shall provide a shift handover record per active work centre showing: operations in progress, operations blocked, outstanding quality holds, unresolved material shortages, downtime events still open, and supervisor notes. The incoming shift supervisor shall acknowledge the handover before taking over the work centre queue.

## 9.4 Rework, Downtime, and Performance

**FR-MFG-051** - When a production batch or operation enters rework, the system shall require the supervisor to record the source failure, the operation to which the batch is being returned, the estimated recoverable quantity, and the reason for rework. Rework quantities shall remain traceably linked to the original production order and shall not be treated as a new unrelated batch.

**FR-MFG-052** - The system shall allow users or machine integrations to record downtime events against a work centre or operation, capturing downtime start, downtime end, reason category, and free-text note. Downtime reason categories shall be tenant-configurable but shall support at minimum breakdown, changeover, waiting_for_material, waiting_for_quality, and planned_stop.

**FR-MFG-053** - The system shall compute work-centre performance metrics including runtime, downtime, availability percentage, output quantity, reject quantity, and Overall Equipment Effectiveness (OEE) using the tenant's approved KPI formula definitions. A production supervisor dashboard shall display current-shift performance for up to 50 work centres within 3 seconds at P95.

## 9.5 Genealogy and Traceability Inquiry

**FR-MFG-054** - When an authorised user initiates a genealogy inquiry for a finished-goods batch, the system shall return the full traceability chain including production order, routing revision, work centres used, operators who completed each operation, consumed raw-material lots or serials, in-process quality results, rework events if any, and by-product outputs. The genealogy inquiry shall return results within 5 seconds at P95 for a batch whose full chain contains up to 500 linked records.
