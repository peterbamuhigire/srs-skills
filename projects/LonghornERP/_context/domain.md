# Domain Context — Longhorn ERP

## Domain Classification

Longhorn ERP is a **cross-domain platform**. It does not belong to a single industry vertical — it is industry-agnostic by design. The following domain knowledge bases from `domains/` are applicable and should be consulted when generating the relevant SRS sections:

| Domain | Applicable Modules | Reference |
|---|---|---|
| Finance | Accounting & GL, Procurement, HR & Payroll, Asset Management | `domains/finance/INDEX.md` |
| Retail | Sales, POS, Advanced Inventory, Sales Agents | `domains/retail/INDEX.md` |
| Agriculture | Cooperative Procurement, Advanced Inventory (batch/serial for agro-processing) | `domains/agriculture/INDEX.md` |
| Logistics | Advanced Inventory (inter-branch transfers, landed cost), Procurement | `domains/logistics/INDEX.md` |
| Government | Procurement (PPDA compliance), Audit Log (Uganda Companies Act), Governance | `domains/government/INDEX.md` |

## ERP-Specific Standards (No Domain File — Apply Directly)

The following standards apply to Longhorn ERP that are not covered by the existing domain files:

### Accounting and Financial Reporting

| Standard | Application |
|---|---|
| IFRS (International Financial Reporting Standards) | All financial statements: Balance Sheet, P&L, Cash Flow (IAS 7), Notes |
| IAS 2 — Inventories | Stock valuation methods (FIFO, weighted average), NRV write-down |
| IAS 16 — Property, Plant and Equipment | Asset recognition, depreciation, revaluation, disposal |
| IAS 19 — Employee Benefits | Leave accruals, pension obligations |
| IAS 36 — Impairment of Assets | Asset impairment testing |
| Uganda Income Tax Act | PAYE bands, withholding tax rates |
| Uganda VAT Act | VAT registration thresholds, input/output tax, return format |
| PPDA Act (Uganda) | Public procurement thresholds and approval workflow |

### Multi-Tenant SaaS

| Standard / Pattern | Application |
|---|---|
| OWASP Top 10 | All web and API security requirements |
| NIST SP 800-63B | Authentication assurance levels, password policy, 2FA |
| Uganda Data Protection and Privacy Act 2019 | Data retention, employee data rights, sub-processor obligations |
| ISO/IEC 27001 | Information security management — audit and compliance baseline |
| NITA-U SaaS Guidelines | Cloud SaaS provider obligations in Uganda |

### Manufacturing and Supply Chain

| Standard | Application |
|---|---|
| ISO 9001:2015 | Quality management — QC checkpoints in Manufacturing module |
| GS1 (barcode standards) | Barcode/QR code formats for stock items and asset tagging |
| FEFO (First Expired, First Out) | Mandatory picking strategy for food, pharma, and agro tenants |

## NFR Defaults for ERP Platforms

The following non-functional requirements apply platform-wide and must be verified against IEEE-982.1 metrics in every SRS document:

<!-- [DOMAIN-DEFAULT: ERP] Source: _context/domain.md -->

### NFR-PERF-001: Page Load Response Time

The system shall render any data-entry page in ≤ 2 seconds at P95 under a load of 100 concurrent tenant users, measured at the server response boundary (excluding browser rendering).

### NFR-PERF-002: Report Generation Time

The system shall generate any financial statement or summary report in ≤ 10 seconds at P95 for data sets spanning up to 24 months of transactions.

### NFR-PERF-003: API Response Time

The system shall return any REST API response in ≤ 500 ms at P95 under a load of 50 concurrent mobile API clients per tenant.

### NFR-AVAIL-001: System Availability

The system shall achieve ≥ 99.5% uptime measured on a rolling 30-day window, excluding scheduled maintenance windows announced ≥ 24 hours in advance.

### NFR-SEC-001: Tenant Data Isolation

The system shall ensure that no query, API response, or report returns data belonging to a tenant other than the authenticated tenant. Violation of this requirement is a Critical severity defect.

### NFR-SEC-002: Audit Log Immutability

The system shall ensure that no audit log record can be updated or deleted by any user, including super administrators. The audit log table shall be INSERT-only.

### NFR-SEC-003: Session Security

The system shall invalidate all active sessions for a user within 5 seconds of an administrator disabling that user's account.

### NFR-SCALE-001: Tenant Capacity

The system shall support ≥ 500 concurrent active tenants on a single deployment without degradation beyond the thresholds defined in NFR-PERF-001 and NFR-PERF-003.

### NFR-MOBILE-001: Offline Resilience

The system shall allow the Cooperative Procurement module to record commodity intake transactions offline for up to 72 hours and sync all pending transactions to the server within 60 seconds of connectivity restoration.

### NFR-USAB-001: Task Completion Without Training

A first-time user with general computer literacy shall be able to complete the following tasks without consulting a manual or requesting support: create a customer invoice, record a payment, check current stock level, submit a leave request. Task completion is measured by unassisted success rate ≥ 85% in usability testing with 5 representative users.

<!-- [END DOMAIN-DEFAULT] -->

## Domain Gap Note

An ERP domain file does not yet exist in `domains/`. If Longhorn ERP documentation becomes a reusable template for other ERP projects, create `domains/erp/` following the pattern in `domains/finance/INDEX.md` and register it in `domains/INDEX.md`.
