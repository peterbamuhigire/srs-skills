# Traceability Matrix — Inventory Management

## 9.1 Business Goals Reference

The following business goals are the upstream drivers for all functional requirements in this module.

- *BG-001* — Operational Accuracy: maintain real-time, correct stock balances across all warehouses and branches to eliminate fulfilment errors caused by inaccurate inventory data.
- *BG-002* — Financial Compliance: value inventory in accordance with IAS 2 (FIFO, WAC, NRV write-down) to produce audit-ready financial statements.
- *BG-003* — Supply Chain Efficiency: automate reorder alerts and inter-branch transfers to minimise stockouts and excess stockholding costs.
- *BG-004* — Audit Readiness: retain a complete, immutable history of every stock movement, stock take, and valuation change to satisfy internal and external audit requirements.

## 9.2 Traceability Table

| Requirement ID | Requirement Summary | BG-001 | BG-002 | BG-003 | BG-004 |
|---|---|:---:|:---:|:---:|:---:|
| **FR-INV-001** | Create item master record | X | | | |
| **FR-INV-002** | Enforce item code uniqueness | X | | | |
| **FR-INV-003** | Support stocked/service/composite types | X | | | |
| **FR-INV-004** | Multi-level category hierarchy | X | | | |
| **FR-INV-005** | Multiple UOM per item | X | | | |
| **FR-INV-006** | UOM conversion on movement posting | X | X | | |
| **FR-INV-007** | GS1 barcode validation | X | | X | |
| **FR-INV-008** | Item attributes incl. shelf life and reorder | X | | X | |
| **FR-INV-009** | Item image attachments | X | | | |
| **FR-INV-010** | Item soft-delete with history preservation | | | | X |
| **FR-INV-011** | Item variant creation | X | | | |
| **FR-INV-012** | Variant UOM consistency | X | | | |
| **FR-INV-013** | Variant matrix display | X | | | |
| **FR-INV-014** | Composite item BOM definition | X | | | |
| **FR-INV-015** | Block deletion of items with movements | | | | X |
| **FR-INV-016** | Item master audit metadata | | | | X |
| **FR-INV-017** | Bulk CSV item import | X | | | |
| **FR-INV-018** | Custom item attributes | X | | | |
| **FR-INV-019** | Warehouse-level reorder settings | | | X | |
| **FR-INV-020** | Auto-numbering for item codes | X | | | |
| **FR-INV-021** | Create warehouse record | X | | | |
| **FR-INV-022** | Warehouse type restrictions | X | | | |
| **FR-INV-023** | Bin-location tracking per warehouse | X | | | |
| **FR-INV-024** | Bin creation within warehouse | X | | | |
| **FR-INV-025** | Default warehouse per branch | X | | | |
| **FR-INV-026** | Warehouse override permission | X | | | |
| **FR-INV-027** | Inter-branch Transfer Order creation | | | X | |
| **FR-INV-028** | Transfer Order status workflow | X | | X | |
| **FR-INV-029** | Auto-post transfer journal entry | | X | | X |
| **FR-INV-030** | Consignment stock segregation | X | X | | X |
| **FR-INV-031** | Move stock to quarantine | X | | | X |
| **FR-INV-032** | Quarantine resolution (dispose or restore) | | X | | X |
| **FR-INV-033** | Real-time stock balance inquiry | X | | | |
| **FR-INV-034** | Block warehouse deletion with stock | X | | | |
| **FR-INV-035** | Warehouse configuration audit log | | | | X |
| **FR-INV-036** | Immutable movement ledger entry | X | | | X |
| **FR-INV-037** | FIFO cost layer creation on receipt | | X | | X |
| **FR-INV-038** | WAC recalculation on receipt | | X | | X |
| **FR-INV-039** | FEFO picking strategy | X | X | | |
| **FR-INV-040** | Block negative stock (HTTP 422) | X | X | | |
| **FR-INV-041** | Allow negative stock (configurable) | X | | | |
| **FR-INV-042** | Stock adjustment authorisation | | X | | X |
| **FR-INV-043** | Adjustment journal entry | | X | | X |
| **FR-INV-044** | Opening balance movement type | X | X | | X |
| **FR-INV-045** | Landed cost allocation across GRN lines | | X | | X |
| **FR-INV-046** | Record landed cost allocation method | | X | | X |
| **FR-INV-047** | Prevent editing of posted movements | | | | X |
| **FR-INV-048** | Purchase return movement auto-generation | X | X | | X |
| **FR-INV-049** | Sales return movement and COGS reversal | X | X | | X |
| **FR-INV-050** | Item ledger inquiry with running balance | X | | | X |
| **FR-INV-051** | UOM conversion on ledger write | X | X | | |
| **FR-INV-052** | Unique movement ID | | | | X |
| **FR-INV-053** | Draft vs. posted movement distinction | | | | X |
| **FR-INV-054** | Min stock level notification on movement | | | X | |
| **FR-INV-055** | Batch/lot number recording | X | X | | X |
| **FR-INV-056** | Valuation method per item or tenant | | X | | |
| **FR-INV-057** | Block valuation method change post-movement | | X | | X |
| **FR-INV-058** | FIFO cost layer table structure | | X | | X |
| **FR-INV-059** | FIFO/FEFO layer consumption order | | X | | X |
| **FR-INV-060** | COGS calculation and posting | | X | | X |
| **FR-INV-061** | WAC recalculation storage | | X | | X |
| **FR-INV-062** | WAC used as COGS unit cost on issue | | X | | X |
| **FR-INV-063** | NRV write-down entry | | X | | X |
| **FR-INV-064** | NRV write-down journal entry | | X | | X |
| **FR-INV-065** | Cost revaluation with variance journal | | X | | X |
| **FR-INV-066** | Stock Valuation Report | | X | | X |
| **FR-INV-067** | Landed cost in carrying value | | X | | |
| **FR-INV-068** | Initiate full or cycle stock take | X | | | X |
| **FR-INV-069** | Freeze movements during stock take | X | | | X |
| **FR-INV-070** | Printable count sheets | | | | X |
| **FR-INV-071** | Mobile/web count entry | X | | | |
| **FR-INV-072** | Double-blind count workflow | | | | X |
| **FR-INV-073** | Variance calculation per line | X | X | | X |
| **FR-INV-074** | Financial impact of variances | | X | | X |
| **FR-INV-075** | Stock take approver authorisation | | X | | X |
| **FR-INV-076** | Auto-create adjustment movements on approval | X | X | | X |
| **FR-INV-077** | Release movement freeze on completion | X | | | |
| **FR-INV-078** | Stock take history record | | | | X |
| **FR-INV-079** | ABC classification report | | | X | |
| **FR-INV-080** | Reorder point evaluation post-movement | | | X | |
| **FR-INV-081** | Reorder alert to purchasing officers | | | X | |
| **FR-INV-082** | Critical stock alert to purchasing manager | | | X | |
| **FR-INV-083** | Auto-generate draft Purchase Requisition | | | X | |
| **FR-INV-084** | Suppress duplicate reorder alerts | | | X | |
| **FR-INV-085** | Reorder Report by warehouse | | | X | X |
| **FR-INV-086** | Days of Supply calculation | | | X | |
| **FR-INV-087** | Projected stockout date on Reorder Report | | | X | |
| **FR-INV-094** | Storage policy by item-location | X | | X | |
| **FR-INV-095** | Putaway recommendation from policy and capacity | X | | X | X |
| **FR-INV-096** | Bin-level capacity controls | X | | X | X |
| **FR-INV-097** | Reserve-to-forward-pick replenishment tasks | X | | X | |
| **FR-INV-098** | Picking modes for batch/wave/zone/single-order | X | | X | |
| **FR-INV-099** | Pick-path sequencing and audit trail | X | | X | X |
| **FR-INV-100** | Warehouse performance dashboard | X | | X | |

## 9.3 Coverage Summary

| Business Goal | FR Count |
|---|---|
| BG-001 — Operational Accuracy | 46 |
| BG-002 — Financial Compliance | 38 |
| BG-003 — Supply Chain Efficiency | 22 |
| BG-004 — Audit Readiness | 43 |

*Note: individual FRs may satisfy more than 1 business goal; counts reflect all FRs that carry an X in each column.*

## 9.4 NFR Traceability

| NFR ID | Quality Attribute | Standard / Basis |
|---|---|---|
| **NFR-INV-001** | Performance — stock query ≤ 2 s P95 | IEEE 982.1 response time metric |
| **NFR-INV-002** | Performance — GRN posting ≤ 3 s P95 | IEEE 982.1 response time metric |
| **NFR-INV-003** | Performance — variance report ≤ 5 s P95 | IEEE 982.1 response time metric |
| **NFR-INV-004** | Performance — Reorder Report ≤ 8 s P95 | IEEE 982.1 response time metric |
| **NFR-INV-005** | Data integrity — negative stock prevention | IAS 2 / business rule |
| **NFR-INV-006** | Data integrity — valuation method immutability | IAS 2 |
| **NFR-INV-007** | Data integrity — FIFO layer reconciliation | IAS 2 / IEEE 982.1 |
| **NFR-INV-008** | Availability — ≥ 99.5% uptime | ISO/IEC 25010 reliability |
| **NFR-INV-009** | Reliability — RPO ≤ 1 h, RTO ≤ 4 h | ISO/IEC 27001 |
| **NFR-INV-010** | Security — RBAC enforcement | ISO/IEC 27001 |
| **NFR-INV-011** | Security — TLS 1.2+ encryption | ISO/IEC 27001 |
| **NFR-INV-012** | Scalability — 500,000 SKUs per tenant | IEEE 982.1 capacity metric |
| **NFR-INV-013** | Scalability — 100M movement records | IEEE 982.1 capacity metric |
| **NFR-INV-014** | Usability — screen load ≤ 3 s | WCAG 2.1 / ISO/IEC 25010 |
| **NFR-INV-015** | Usability — mobile touch targets ≥ 44 × 44 px | WCAG 2.1 Level AA |
