# Scrap Management, NFRs, and Traceability

## 8.1 Scrap Management

**FR-MFG-043** — When a user records scrap during a production order, the system shall capture: scrapped item or semi-finished component, quantity scrapped, scrap reason (configurable: damage, off-spec, process loss, contamination), and the production stage at which scrap occurred.

**FR-MFG-044** — When scrap is confirmed, the system shall post the GL entry: Debit Scrap Loss account, Credit WIP account, for the scrap quantity valued at the current average cost of the scrapped component or WIP.

**FR-MFG-045** — The system shall generate a monthly scrap analysis report per production order and per scrap reason, displaying: total scrap quantity, total scrap value, scrap as a percentage of total raw material issued, and trend vs. prior month.

## 8.2 Non-Functional Requirements

**NFR-MFG-001** — A production order cost roll-up for a BOM with ≤ 50 components across ≤ 5 BOM levels shall complete within 5 seconds.

**NFR-MFG-002** — All production order GL postings (raw material issue, labour, overhead, finished goods receipt) shall execute within a single database transaction; a failure at any step shall roll back all GL and stock changes for that transaction.

**NFR-MFG-003** — Production order records, BOM versions, QC inspection results, and yield variance records shall be retained for a minimum of 10 years for audit and regulatory purposes; deletion shall be prohibited at the application layer.

**NFR-MFG-004** — BOM version history shall be immutable; once a BOM version is used in a production order, the version record shall be locked against further modifications.

## 8.3 Traceability Matrix

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-MFG-001–008 | BOM structure, templates, cost roll-up | BG-001, BG-004 |
| FR-MFG-009–016 | Production orders, scheduling | BG-001 |
| FR-MFG-017–022 | Raw material issue, back-flush, substitutions | BG-001, BG-003 |
| FR-MFG-023–028 | WIP tracking, QC checkpoints | BG-002 |
| FR-MFG-029–034 | Finished goods, by-products | BG-001 |
| FR-MFG-035–042 | Costing, labour, overhead, yield variance | BG-001, BG-003 |
| FR-MFG-043–045 | Scrap management | BG-003 |

**Open verification notes:**
- FR-MFG-005 (Uganda agro BOM templates) shall be reviewed by at least one sugar and one edible oil processor before UAT.
- NFR-MFG-001 (5-second cost roll-up) requires a seeded BOM with 50 components to be included in the load test suite.
