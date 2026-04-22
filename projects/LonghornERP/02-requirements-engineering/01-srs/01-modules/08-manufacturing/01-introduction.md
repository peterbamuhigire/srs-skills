# Introduction to the Manufacturing Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for the Manufacturing module of Longhorn ERP. It targets software engineers, QA analysts, and system architects responsible for implementing and verifying this module. All requirements are prospective and use the prescriptive form "The system shall...".

## 1.2 Scope

The Manufacturing module governs production planning, Bill of Materials (BOM) management, production order lifecycle, routing definition, work centre setup, raw material issue, Work In Progress (WIP) tracking, operation-level execution tracking, production costing, in-process quality checkpoints, rework control, scrap management, downtime capture, Overall Equipment Effectiveness (OEE) monitoring, shift handover visibility, product genealogy, overhead absorption, and yield analysis.

The module therefore covers both core ERP manufacturing controls and MES-grade shop-floor execution depth so that Longhorn ERP can plan, execute, monitor, trace, and continuously improve industrial operations within one governed system.

The module integrates with:

- **Advanced Inventory** â€” raw material issues and finished goods receipts are stock movements (`FR-ADVINV-*`); FEFO picking applies to raw material issues.
- **Accounts Payable / General Ledger** â€” every production order generates GL journal entries for material cost, labour, overhead, and finished goods.
- **Procurement** â€” purchase requisitions may be triggered automatically when BOM components fall below reorder level.
- **Sales** â€” finished goods produced are available to the sales order fulfilment workflow.

## 1.3 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Accurate production cost roll-up so that the landed cost of finished goods is reflected in inventory valuation and product pricing. |
| BG-002 | Quality assurance: no finished goods leave production with an unresolved QC failure. |
| BG-003 | Minimal raw material waste: scrap is tracked, approved, and posted to GL for yield analysis. |
| BG-004 | Uganda-specific BOM support for agro-processing: sugar, edible oil, flour milling, dairy, and brewing. |
| BG-005 | Operation-level production visibility so supervisors can track routings, work centre performance, downtime, rework, and shift output in real time. |
| BG-006 | Full production traceability so each finished lot can be linked to consumed inputs, executed operations, in-process quality results, and responsible shifts. |

## 1.4 Definitions and Acronyms

| Term | Definition |
|---|---|
| BOM | Bill of Materials â€” a structured list of raw materials and quantities required to produce one unit of a finished good. |
| By-product | A secondary output of a production run that has independent commercial value. |
| Co-product | An output that is produced in fixed proportion alongside the primary finished good. |
| Genealogy | End-to-end production traceability linking finished goods and semi-finished goods to consumed materials, executed operations, machines, operators, and quality records. |
| OEE | Overall Equipment Effectiveness â€” a composite performance measure derived from availability, performance, and quality for a work centre or production line. |
| Production Order | A work order authorising the manufacture of a specified quantity of a finished good. |
| Rework | Controlled reprocessing of non-conforming or partially conforming output so it can be brought back into an acceptable quality state. |
| Routing | The ordered sequence of manufacturing operations, work centres, standard times, and control points required to produce an item. |
| Shift Handover | The structured transfer of production status, exceptions, WIP position, and machine state between outgoing and incoming shifts. |
| WIP | Work In Progress â€” the intermediate state of a production order between raw material issue and finished goods receipt. |
| Work Centre | A machine, line, cell, or labour station where one or more routing operations are executed and capacity is consumed. |
| Yield | The ratio of actual finished goods output to the planned output expressed as a percentage: $Yield = (ActualOutput \div PlannedOutput) \times 100$. |

## 1.5 Document Overview

| Section | Content |
|---|---|
| 2 | Bill of Materials |
| 3 | Production Orders and Routing-Controlled Execution |
| 4 | Raw Material Issue |
| 5 | WIP Tracking, Operation Execution, and QC |
| 6 | Finished Goods and By-products |
| 7 | Production Costing, Overhead, and Performance Visibility |
| 8 | Scrap Management and Manufacturing NFRs |
| 9 | Non-Functional Requirements |
| 10 | Traceability Matrix |
