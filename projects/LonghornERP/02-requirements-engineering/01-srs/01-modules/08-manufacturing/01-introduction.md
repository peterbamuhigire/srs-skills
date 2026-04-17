# Introduction to the Manufacturing Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for the Manufacturing module of Longhorn ERP. It targets software engineers, QA analysts, and system architects responsible for implementing and verifying this module. All requirements are prospective and use the prescriptive form "The system shall...".

## 1.2 Scope

The Manufacturing module governs production planning, Bill of Materials (BOM) management, production order lifecycle, raw material issue, Work In Progress (WIP) tracking, production costing, quality checkpoints, scrap management, overhead absorption, and yield analysis.

The module integrates with:

- **Advanced Inventory** — raw material issues and finished goods receipts are stock movements (`FR-ADVINV-*`); FEFO picking applies to raw material issues.
- **Accounts Payable / General Ledger** — every production order generates GL journal entries for material cost, labour, overhead, and finished goods.
- **Procurement** — purchase requisitions may be triggered automatically when BOM components fall below reorder level.
- **Sales** — finished goods produced are available to the sales order fulfilment workflow.

## 1.3 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Accurate production cost roll-up so that the landed cost of finished goods is reflected in inventory valuation and product pricing. |
| BG-002 | Quality assurance: no finished goods leave production with an unresolved QC failure. |
| BG-003 | Minimal raw material waste: scrap is tracked, approved, and posted to GL for yield analysis. |
| BG-004 | Uganda-specific BOM support for agro-processing: sugar, edible oil, flour milling, dairy, and brewing. |

## 1.4 Definitions and Acronyms

| Term | Definition |
|---|---|
| BOM | Bill of Materials — a structured list of raw materials and quantities required to produce one unit of a finished good. |
| By-product | A secondary output of a production run that has independent commercial value. |
| Co-product | An output that is produced in fixed proportion alongside the primary finished good. |
| Production Order | A work order authorising the manufacture of a specified quantity of a finished good. |
| WIP | Work In Progress — the intermediate state of a production order between raw material issue and finished goods receipt. |
| Yield | The ratio of actual finished goods output to the planned output expressed as a percentage: $Yield = (ActualOutput \div PlannedOutput) \times 100$. |

## 1.5 Document Overview

| Section | Content |
|---|---|
| 2 | Bill of Materials |
| 3 | Production Orders |
| 4 | Raw Material Issue |
| 5 | WIP Tracking and QC |
| 6 | Finished Goods and By-products |
| 7 | Production Costing and Overhead |
| 8 | Scrap Management |
| 9 | Non-Functional Requirements |
| 10 | Traceability Matrix |
