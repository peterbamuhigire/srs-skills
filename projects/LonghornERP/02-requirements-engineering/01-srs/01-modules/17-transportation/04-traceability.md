# Traceability Matrix - Transportation and Fleet Operations Module

## 4.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6 and records the deterministic test oracle for each requirement. All FRs without a mapping to a business goal are anomalies and shall be treated as `[TRACE-GAP]`.

## 4.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-TMS-001 | Reduce transport cost through better load planning, route control, and freight validation |
| BG-TMS-002 | Improve service reliability through dispatch discipline, ETA visibility, and exception ownership |
| BG-TMS-003 | Increase fleet utilisation and operational control for organisations running internal vehicles |
| BG-TMS-004 | Create a traceable transport record from shipment planning through proof of delivery and settlement |
| BG-TMS-005 | Give management transport analytics that connect physical movement to financial outcomes |

## 4.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | PRD Reference | Test Oracle |
|---|---|---|---|---|---|
| FR-TMS-001 | 2.1 | Shipment-demand consolidation into a transport-planning workbench | BG-TMS-001, BG-TMS-002, BG-TMS-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Confirm sales order, transfer order, and manual transport request; verify 3 shipment orders appear in the unplanned workbench with correct source references. |
| FR-TMS-002 | 2.2 | Load, route, and stop planning with capacity enforcement | BG-TMS-001, BG-TMS-002, BG-TMS-003 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Create vehicle profile with 5-ton capacity; plan route totalling 6 tons; verify save is blocked and capacity error identifies weight as the violating dimension. |
| FR-TMS-003 | 2.3 | Dispatch with carrier or internal-fleet assignment and availability control | BG-TMS-002, BG-TMS-003, BG-TMS-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Mark vehicle on maintenance hold; attempt dispatch; verify dispatch blocked. Release hold and dispatch with available driver; verify trip record created and notification queued. |
| FR-TMS-004 | 2.4 | Milestone visibility, ETA refresh, and exception queue | BG-TMS-002, BG-TMS-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Dispatch trip with 30-minute delay threshold; post milestone producing projected 45-minute delay; verify high-severity exception appears on dispatcher dashboard within 5 seconds. |
| FR-TMS-005 | 2.5 | Proof capture, trip closure, and actual operational costing | BG-TMS-003, BG-TMS-004, BG-TMS-005 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Complete stop with customer signature and image proof; attempt trip close without actual costs; verify mandatory close-out fields enforced; enter costs and verify trip closes successfully. |
| FR-TMS-006 | 2.6 | Freight audit, settlement, and analytics | BG-TMS-001, BG-TMS-004, BG-TMS-005 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Submit carrier invoice 10% above planned lane cost with 5% tolerance; verify settlement placed in audit hold and payment posting blocked until approval. |
