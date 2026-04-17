# Supplier Management

## 2.1 Overview

Supplier Management maintains the supplier master and all associated reference data required by downstream procurement workflows. Every active supplier record is globally unique per tenant.

## 2.2 Functional Requirements

**FR-PROC-001** — When a user submits a new supplier record, the system shall validate that the supplier name is unique within the tenant and that the Tax Identification Number (TIN) conforms to the URA 10-digit numeric format; if either validation fails, the system shall reject the record and return a descriptive error message.

**FR-PROC-002** — When a supplier record is saved, the system shall persist the following mandatory fields: supplier name, TIN, primary contact name, primary phone number, payment terms (net days), and withholding tax (WHT) status (exempt or subject to WHT).

**FR-PROC-003** — When a user adds a bank account to a supplier record, the system shall store bank name, branch name, account number, and account name; the system shall permit multiple bank accounts per supplier and designate exactly one as the default payment account.

**FR-PROC-004** — When a user updates a supplier record, the system shall write the previous field values, new field values, user identity, and timestamp to the audit log before committing the change.

**FR-PROC-005** — When a user deactivates a supplier, the system shall block creation of new purchase orders against that supplier and display a warning on any in-progress documents linked to that supplier.

**FR-PROC-006** — The system shall provide a supplier search interface that filters by supplier name, TIN, and active/inactive status and returns results within 500 ms for a tenant dataset of ≤ 10,000 supplier records.

## 2.3 Supplier Categories and Tags

**FR-PROC-007** — The system shall allow users to assign one or more configurable category tags to each supplier (e.g., "Goods", "Services", "Contractor", "Import") and shall support filtering purchase reports by tag.

**FR-PROC-008** — When a supplier is tagged as "Import", the system shall expose a landed cost allocation option on all goods receipt notes raised against that supplier.
