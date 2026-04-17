# Data Protection and Privacy

## 6.1 Governing Legislation

Longhorn ERP processes personal data on behalf of its tenants. The primary governing legislation is the Uganda Data Protection and Privacy Act 2019 (PDPA). Longhorn ERP operates as a *data processor* for each tenant, who is the *data controller* for their employees, customers, and suppliers. The obligations of both parties shall be documented in the Tenant Service Agreement.

*[CONTEXT-GAP: GAP-007] — A full legal review of Uganda Data Protection and Privacy Act 2019 obligations is required before the Human Resources (HR) and Payroll module is launched. The review shall cover: data retention limits for employee personal data, the employee right of access to personal data, sub-processor obligations, and consent requirements for HR medical and financial data. All requirements in this section marked with `[PENDING GAP-007]` are provisional and shall be updated once the legal review is complete.*

## 6.2 Known PDPA Obligations

The following obligations are known at the time of writing. They represent a minimum compliance baseline and shall be superseded by the findings of the GAP-007 legal review.

### 6.2.1 Data Retention Limits `[PENDING GAP-007]`

The system shall support configurable data retention periods per data category. Default retention periods shall be defined in consultation with legal counsel following the GAP-007 review. The system shall provide a tenant-accessible data retention policy configuration screen in the Tenant Workspace settings module.

### 6.2.2 Employee Right of Access

The system shall provide a mechanism for a tenant administrator to generate a structured export of all personal data held for a named employee, in response to a subject access request. The export shall include: employee profile data, payroll history, leave records, and any HR documents linked to the employee. The export shall be producible within 72 hours of request. The exact data scope and format shall be confirmed after the GAP-007 legal review.

### 6.2.3 Sub-Processor Obligations

Chwezi Core Systems, as data processor, shall maintain a register of sub-processors (cloud infrastructure provider, email service provider, third-party API integrations). The register shall be made available to tenants upon request. Changes to sub-processors that materially affect data processing shall be notified to tenants ≥ 30 days in advance.

### 6.2.4 Consent for Sensitive HR Data

The system shall record explicit consent from employees before capturing medical data (e.g., disability status, medical leave diagnoses) or detailed financial data beyond standard payroll fields. Consent records shall be stored in the `employee_consents` table with timestamp, consent type, and employee identifier. `[PENDING GAP-007]`

## 6.3 Sensitive Field Encryption at Rest

The following field categories shall be encrypted at rest using Advanced Encryption Standard (AES) with a 256-bit key (AES-256). Encryption shall be applied at the application layer before values are written to the database, using the `encryption_key` environment variable loaded via `vlucas/phpdotenv`.

| Field Category | Examples | Encryption Required |
|---|---|---|
| Salary and compensation data | Basic salary, gross pay, net pay, allowances | AES-256 |
| Biometric identifiers | Fingerprint hash, face recognition token | AES-256 |
| National Identification Number (NIN) | Uganda NIN, passport number | AES-256 |
| Bank account numbers | Employee bank account, supplier bank account | AES-256 |
| Tax Identification Number (TIN) | Uganda TIN | AES-256 |
| Password hashes | Already hashed; not additionally encrypted | Bcrypt (minimum cost 12) |

The encryption key shall be rotated on a schedule defined by the deployment operations team. A key rotation procedure shall be documented in the deployment runbook (`08-end-user-documentation/02-installation-guide/`).

Encrypted fields shall not be searchable by their plaintext value through standard SQL queries. Where search on an encrypted field is required (e.g., look up employee by NIN), the system shall use a deterministic blind index stored in a separate indexed column. The blind index shall be derived using HMAC-SHA256 with a separate secret key (`blind_index_key` environment variable).

## 6.4 Data Residency

*[CONTEXT-GAP: GAP-007] — A legal determination is required before production deployment on whether tenant data must be stored on Uganda-based cloud infrastructure or whether international cloud hosting is permitted under the PDPA. This determination affects the choice of cloud provider, data centre region, and the sub-processor register. No production deployment shall proceed without a confirmed data residency position.*

The deployment runbook shall document the production hosting environment, the data centre region, and the legal basis for the chosen residency position.

## 6.5 Data Minimisation

The system shall not collect personal data fields beyond those required for the activated modules. Module deactivation shall not expose personal data collected for that module to users of other modules. Fields marked as personally identifiable in the schema shall be excluded from bulk export operations unless the user holds an explicit data export permission within their role.

## 6.6 Tenant Offboarding and Data Deletion

When a tenant's subscription is terminated, the following data lifecycle procedure shall apply:

1. The tenant's operational data (invoices, inventory, HR records, etc.) shall be archived to an encrypted, tenant-specific export within 30 days of termination.
2. The encrypted archive shall be retained for 90 days after export generation and then purged, unless a longer retention period is required by a legal hold.
3. Audit log records within the 7-year retention window shall not be purged at offboarding. They shall be retained in cold storage in a format accessible to Chwezi Core Systems for legal and compliance purposes.
4. The tenant's user accounts, configuration data, and module subscriptions shall be deactivated immediately upon termination.
5. The tenant `tenant_id` shall be flagged as `OFFBOARDED` in the `tenants` table and shall not be reused.

The exact purge timeline and legal hold procedure shall be finalised after the GAP-007 legal review.
