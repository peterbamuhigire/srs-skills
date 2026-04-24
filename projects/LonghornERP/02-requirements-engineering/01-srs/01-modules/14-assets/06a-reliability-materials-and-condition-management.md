# Reliability, Materials, and Condition Management

This section defines the reliability and condition-management capabilities expected of an enterprise asset-management workflow.

**FR-ASSET-077:** When a planned work order requires stocked materials, the system shall reserve the required item quantities from Inventory against the work order and show reservation status, short quantity, and staging location on the work-order material list.

**FR-ASSET-078:** When a required work-order material is unavailable in free stock, the system shall flag a material-shortage exception and optionally create a linked procurement request or stock-transfer request without altering the work-order scope.

**FR-ASSET-079:** The system shall accept validated condition events from meter readings, inspection forms, or external telemetry sources and evaluate them against asset-specific or category-default thresholds to determine whether monitoring, inspection, or corrective work is required.

**FR-ASSET-080:** When a work order is closed, the system shall require structured closeout data including failure code, cause code, remedy code, actual labour hours, materials consumed, completion notes, and completion timestamp; closeout without these mandatory fields shall be rejected for work orders classified as corrective or breakdown work.

**FR-ASSET-081:** The system shall provide reliability dashboards showing at minimum PM compliance, planned-versus-unplanned work ratio, schedule compliance, backlog age by priority, mean time between failures (MTBF), and mean time to repair (MTTR) for a user-authorised scope and date range.

**FR-ASSET-082:** The system shall identify repeat-failure or bad-actor assets by configurable thresholds on breakdown count, repeat failure code, downtime impact, or maintenance cost trend, and it shall allow an authorised user to open a root-cause analysis workflow linked to the relevant asset and failure history.

**FR-ASSET-083:** The system shall support technician mobile work execution, including offline capture of start time, stop time, checklist completion, meter readings, parts usage, photos, and completion notes; offline records shall synchronise automatically when connectivity is restored.
