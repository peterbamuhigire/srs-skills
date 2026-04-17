# Non-Functional Requirements for the Sales Module

## 9.1 Overview

This section specifies the measurable non-functional requirements (NFRs) governing performance, security, and data integrity for the Sales module. All thresholds are stated as 95th percentile (P95) values under normal operating load, defined as up to 500 concurrent users per tenant.

## 9.2 Performance Requirements

**NFR-SALES-001:** The system shall generate a Standard Invoice PDF within 3 seconds at P95 under normal operating load, measured from the time the user triggers the "Generate PDF" action to the time the PDF is available for download.

*Verification method:* Load test with 500 concurrent users, each triggering simultaneous PDF generation. Pass criterion: ≤ 5% of requests exceed 3 seconds.

**NFR-SALES-002:** The system shall generate a customer statement for a date range spanning 24 months of transactions within 5 seconds at P95 under normal operating load, measured from the time the user submits the statement request to the time the PDF is rendered.

*Verification method:* Benchmark test using a seeded customer record with 24 months of synthetic transactions (minimum 500 transactions). Pass criterion: ≤ 5% of requests exceed 5 seconds.

**NFR-SALES-003:** The system shall generate the debtors aging report across all active customers for a tenant within 8 seconds at P95 under normal operating load.

*Verification method:* Load test using a tenant with a minimum of 10,000 active customers and outstanding invoice records. Pass criterion: ≤ 5% of report generation requests exceed 8 seconds.

**NFR-SALES-004:** The system shall resolve and return the price list price for a given item, UOM, customer, and quantity within 500 ms at P95 when a line is added to an invoice, quotation, or sales order.

*Verification method:* API-level load test simulating 500 concurrent line-add events. Pass criterion: ≤ 5% of price resolution calls exceed 500 ms.

**NFR-SALES-005:** The system shall prevent invoicing a quantity greater than the confirmed Sales Order quantity for a given line without an explicit override by a user holding the `sales.order.override` permission; the enforcement check shall execute within 200 ms at P95.

*Verification method:* Automated integration test submitting an invoice line quantity 1 unit above the SO quantity without the override permission. Pass criterion: system returns a rejection response within 200 ms on ≥ 95% of attempts.

## 9.3 Security Requirements

**NFR-SALES-006:** The system shall enforce role-based access control (RBAC) on every Sales module action — create, read, update, delete, approve, and override — such that a user without the required permission receives an HTTP 403 response and an in-app "Access Denied" message.

**NFR-SALES-007:** The system shall store no customer payment card data within the Sales module. All payment tokenisation is delegated to the Platform Integration Layer.

## 9.4 Data Integrity Requirements

**NFR-SALES-008:** The system shall ensure that all financial postings initiated by the Sales module — invoice posting, receipt allocation, credit note application — are executed within atomic database transactions, such that a partial failure results in a full rollback with no orphaned ledger entries.

**NFR-SALES-009:** The system shall retain all Sales module records — invoices, receipts, delivery notes, returns, credit notes — for a minimum of 7 years in compliance with the Uganda Income Tax Act retention requirements, and shall prevent hard deletion of any financial record regardless of user permission level.

## 9.5 Availability and Reliability Requirements

**NFR-SALES-010:** The Sales module shall maintain 99.5% monthly uptime, excluding scheduled maintenance windows communicated to tenants at least 48 hours in advance, consistent with the Longhorn ERP platform Service Level Agreement.
