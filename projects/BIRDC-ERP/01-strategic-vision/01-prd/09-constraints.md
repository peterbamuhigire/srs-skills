# Section 8: Constraints

The following constraints are binding. No requirement, architecture decision, or implementation choice may violate any constraint in this section without written sign-off from the BIRDC Director and Finance Director.

## 8.1 Deployment: On-Premise Only

The system shall be deployed exclusively on BIRDC-owned server hardware at Nyaruzinga, Bushenyi. No component of the system — application server, database, file storage, or backup — shall reside on any cloud platform, SaaS provider, or third-party hosted infrastructure. This constraint implements Design Covenant DC-006 (Data Sovereignty).

## 8.2 Technology Stack: PHP/MySQL

The web application backend shall be built in PHP 8.3+ with `declare(strict_types=1)` on every file, PSR-4 autoloading, and PSR-12 coding standard, using a Service/Repository architecture pattern with PHP-DI dependency injection. The database shall be MySQL 9.1 InnoDB with utf8mb4 character set. No other server-side language or database engine is permitted without Director-level written approval.

## 8.3 Mobile: Android Only (iOS Deferred)

All 6 mobile applications shall target Android 8.0 (API level 26) as the minimum supported version. iOS development is deferred and is not part of this engagement.

## 8.4 PPDA Compliance

All procurement workflows must comply with the Uganda Public Procurement and Disposal of Public Assets Act and PPDA regulations applicable to PIBID/BIRDC as a government entity. The PPDA approval matrix (BR-005) is a binding business rule. [CONTEXT-GAP: GAP-007 — Exact current PPDA procurement threshold values in UGX must be confirmed with BIRDC Administration before the procurement approval matrix is configured.]

## 8.5 EFRIS Compliance

All commercial invoices, credit notes, and POS receipts shall be submitted in real time to Uganda Revenue Authority via the EFRIS system-to-system REST API. The system shall store the Fiscal Document Number (FDN) and QR code against every successfully submitted transaction and print them on all fiscal documents. [CONTEXT-GAP: GAP-001 — URA EFRIS API sandbox credentials required before Phase 1 invoice testing.]

## 8.6 Data Sovereignty

All BIRDC data — farmer records, financial accounts, production records, employee records, and audit logs — shall be stored on BIRDC-owned servers in Uganda. No data shall be transmitted to or stored on any server outside Uganda except via the EFRIS API (URA), MTN MoMo API, and Airtel Money API, which are Ugandan regulatory interfaces.

## 8.7 7-Year Audit Retention

All financial records, audit trail entries, and payroll records shall be retained in the system for a minimum of 7 years, in compliance with the Uganda Companies Act and Uganda Income Tax Act. Deletion of records within the retention period is not permitted for any user role.

## 8.8 Segregation of Duties

The system shall enforce segregation of duties (BR-003) at the API layer for all financial approvals, procurement approvals, remittance verification, payroll approval, and stock adjustments. UI-level enforcement alone is not sufficient; the API endpoint must reject the transaction if the requester is the same user who created it.

## 8.9 Offline-First Mobile Operations

The Sales Agent App (POS), Farmer Delivery App, and Warehouse App shall function completely offline. All transactions recorded offline shall be stored in local SQLite (Room) and synchronised to the server when connectivity is restored. Loss of internet connectivity at Nyaruzinga must not halt operations in these three applications.

