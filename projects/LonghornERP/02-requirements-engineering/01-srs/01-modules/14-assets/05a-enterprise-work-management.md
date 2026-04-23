# Enterprise Work Management

This section extends the module from maintenance reminders into structured enterprise work management.

**FR-ASSET-069:** The system shall allow an authorised user to define functional locations and parent-child asset hierarchies, and every maintainable asset shall be assignable to exactly 1 active functional location.

**FR-ASSET-070:** The system shall require each maintainable asset to carry a criticality classification using a tenant-defined scale, and work priority rules shall reference asset criticality when calculating recommended response and schedule windows.

**FR-ASSET-071:** The system shall provide a work-request intake process through which operators, supervisors, or authorised technicians may submit a maintenance request containing asset, symptom, problem description, requested date, and optional photo or meter evidence; the system shall detect and flag potential duplicates against open requests for the same asset and issue category.

**FR-ASSET-072:** The system shall allow an authorised planner or supervisor to screen a work request and either reject it with reason, convert it to a work order, or merge it into an existing work order, and each screening decision shall be audit logged.

**FR-ASSET-073:** When a work order is planned, the system shall support a planning package containing task list, estimated labour hours, required skills, required materials, safety instructions, permit requirements, and target schedule window.

**FR-ASSET-074:** The system shall provide a weekly scheduling board that assigns planned work orders to crews, technicians, or contractors based on labour capacity, planned duration, asset criticality, and required shutdown windows, and it shall prevent over-allocation unless an authorised scheduler records an override reason.

**FR-ASSET-075:** Every work order shall store whether it is planned or unplanned work, and the system shall calculate backlog age in calendar days from screening date until completion or cancellation.

**FR-ASSET-076:** The system shall allow an authorised planner to group work orders into a shutdown or turnaround package with shared window, area, coordinator, and readiness status, and packaged work orders shall expose a consolidated readiness summary before execution begins.
