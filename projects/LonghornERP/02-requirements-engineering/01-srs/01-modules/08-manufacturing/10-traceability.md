# Traceability Matrix - Manufacturing Module MES Extension

## 10.1 Overview

This traceability section extends the Manufacturing module coverage for the MES-grade execution requirements added in Section 9. It maps each new functional requirement to at least 1 business goal already defined in the Manufacturing introduction.

## 10.2 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | Test Oracle |
|---|---|---|---|---|
| FR-MFG-046 | 9.1 | Routing definition with ordered operations and execution metadata | BG-001, BG-002 | Create routing with 3 ordered operations and mandatory QC on operation 2; verify sequence and operation metadata are stored and returned correctly. |
| FR-MFG-047 | 9.1 | Operation queue generation and dispatch by work centre and shift | BG-001, BG-005 | Release production order with effective routing; verify operation queue rows are created per operation and visible by work centre. |
| FR-MFG-048 | 9.2 | Operation-level execution state machine and audit capture | BG-002, BG-005 | Transition operation through `ready -> in_progress -> paused -> in_progress -> completed`; verify each state change records actor, timestamp, and reason where applicable. |
| FR-MFG-049 | 9.2 | Material-lot capture and genealogy link at operation level | BG-002, BG-005 | Consume 2 raw-material lots into a batch-tracked finished good; verify genealogy shows both consumed lots linked to the finished batch. |
| FR-MFG-050 | 9.3 | Shift handover continuity for active work centres | BG-005 | Close shift with open quality hold and downtime event; verify handover record contains both and requires incoming supervisor acknowledgement. |
| FR-MFG-051 | 9.4 | Governed rework linked to original production order | BG-002, BG-003 | Fail QC, send batch to rework, and verify recoverable quantity plus original-order linkage are preserved. |
| FR-MFG-052 | 9.4 | Downtime event capture with reason taxonomy | BG-003, BG-005 | Record downtime event with category `waiting_for_material`; verify event timestamps and reason category persist against work centre history. |
| FR-MFG-053 | 9.4 | OEE and work-centre performance dashboard | BG-003, BG-005 | Seed runtime, downtime, output, and rejects for a work centre; verify dashboard computes availability and OEE using configured KPI definitions. |
| FR-MFG-054 | 9.5 | Full genealogy inquiry for finished-goods batch | BG-002, BG-005 | Run genealogy inquiry on finished batch with QC and rework history; verify returned chain includes production order, consumed lots, QC results, and rework events. |
