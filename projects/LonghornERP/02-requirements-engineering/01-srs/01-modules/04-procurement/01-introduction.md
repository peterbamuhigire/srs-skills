# Introduction to the Procurement Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for the Procurement module of Longhorn ERP. The document targets software engineers, quality assurance analysts, and system architects responsible for implementing and verifying this module. All requirements are prospective and use the prescriptive form "The system shall...".

## 1.2 Scope

The Procurement module governs the end-to-end acquisition of goods and services within Longhorn ERP. It covers supplier lifecycle management, purchase requisitions, request for quotations (RFQ), purchase orders (PO), goods receipt, supplier invoice processing, payment management, and compliance with the Uganda Public Procurement and Disposal of Public Assets (PPDA) Act.

The module integrates with:

- **Inventory** — goods receipt posts stock movements.
- **Accounts Payable** — supplier invoices and payments post to the General Ledger.
- **General Ledger** — every procurement transaction generates journal entries.
- **RBAC** — approval workflows enforce role-based access at each threshold level.

The module does not cover customer-facing sales, payroll disbursements, or fixed asset disposal.

## 1.3 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Cost control through enforced PO approval and three-way match before payment. |
| BG-002 | Regulatory compliance with the PPDA Act and Uganda tax obligations (VAT, WHT). |
| BG-003 | Cash-flow visibility through creditors aging and scheduled payment runs. |
| BG-004 | Audit readiness via immutable approval chains and PPDA procurement reports. |

## 1.4 Applicable Standards and Regulations

- Uganda Public Procurement and Disposal of Public Assets Act (PPDA Act) — procurement method thresholds and open-tender obligations.
- Uganda VAT Act — input VAT recording on supplier invoices.
- Uganda Income Tax Act — withholding tax (WHT) deduction on qualifying supplier payments.
- IEEE Std 830-1998 — SRS quality attributes: correct, unambiguous, complete, consistent, ranked, verifiable, modifiable, traceable.
- IEEE Std 610.12-1990 — standard glossary of software engineering terminology.
- IEEE Std 1012-2016 — software verification and validation.

## 1.5 Definitions and Acronyms

| Term | Definition |
|---|---|
| GRN | Goods Receipt Note — document recording physical receipt of goods against a PO. |
| PO | Purchase Order — a binding document issued to a supplier authorising delivery of goods or services. |
| PPDA | Public Procurement and Disposal of Public Assets — Uganda's public procurement regulatory body. |
| PR | Purchase Requisition — an internal request to purchase goods or services. |
| RFQ | Request for Quotation — a solicitation sent to suppliers to obtain competitive price quotations. |
| SRS | Software Requirements Specification. |
| TIN | Tax Identification Number — issued by the Uganda Revenue Authority. |
| VAT | Value Added Tax — applied to supplier invoices per the Uganda VAT Act. |
| WHT | Withholding Tax — tax deducted at source from qualifying supplier payments. |
| 3-way match | Cross-validation of PO price, GRN quantity, and supplier invoice values before approving payment. |

## 1.6 Document Conventions

- Functional requirements carry the identifier pattern `FR-PROC-NNN`.
- Non-functional requirements carry the identifier pattern `NFR-PROC-NNN`.
- `[CONTEXT-GAP: <topic>]` marks a requirement whose detail cannot be confirmed from available context.
- `[GLOSSARY-GAP: <term>]` marks a term used but not yet defined in the project glossary.
- `[V&V-FAIL: <reason>]` marks a requirement that fails the IEEE 1012 verification criteria.

## 1.7 Overview of This Document

| Section | Content |
|---|---|
| 2 | Supplier Management |
| 3 | Purchase Requisitions and RFQ |
| 4 | Purchase Orders |
| 5 | Goods Receipt |
| 6 | Supplier Invoices |
| 7 | Payments and Creditors Aging |
| 8 | PPDA Compliance |
| 9 | Non-Functional Requirements |
| 10 | Traceability Matrix |
