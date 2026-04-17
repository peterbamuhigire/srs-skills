## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the Audit Log module of Longhorn ERP. The Audit Log is a Platform Core module — it is always active for every tenant and cannot be disabled.

The primary purpose of this document is to specify an immutable, tamper-evident audit trail that captures every create, update, delete, approval, and authentication event occurring within the system, across all modules and all tenants. This specification governs the capture, storage, immutability enforcement, access control, search, export, and retention of audit records.

### 1.2 Scope

The Audit Log module provides:

- Automated, system-generated capture of all state-changing operations across every module.
- Immutable storage of audit records enforced at the database privilege level.
- SHA-256 hash-based tamper detection for each stored record.
- A read-only search and export interface for authorised users and external auditors.
- Configurable retention with a 7-year system default, in compliance with the Uganda Companies Act Cap. 110 (minimum 5-year retention for financial records, extended to 7 years in this system).

The Audit Log does not replace application-level error logs or infrastructure logs. It is exclusively concerned with user- and system-initiated data operations within the Longhorn ERP application boundary.

### 1.3 Definitions

The following terms are defined per IEEE Std 610.12-1990 and the Longhorn ERP glossary (`_context/glossary.md`).

| Term | Definition |
|---|---|
| Audit Log | An immutable, INSERT-only record of every create, update, delete, and approval action performed within the system, capturing old values, new values, user identity, IP address, and timestamp. |
| Immutability | The property of the `audit_log` table by which no existing record can be modified or removed once written, enforced at the database privilege level. |
| Old Values | A JSON snapshot of a record's field values immediately before an UPDATE or DELETE operation. |
| New Values | A JSON snapshot of a record's field values immediately after a CREATE or UPDATE operation. |
| Tamper Detection | The process of re-computing the SHA-256 hash of a stored audit record and comparing it to the hash stored at insert time to detect unauthorised modification. |
| Retention Period | The minimum duration for which audit records must be preserved before they are eligible for archival or deletion. System default: 7 years. |
| External Auditor | A user assigned the read-only `auditor` role, with access limited to audit log search and export. This role has no write access to any table. |
| Super Admin | A platform-level administrator with cross-tenant management capabilities. Super admins are subject to audit logging in the same manner as all other users. |
| Impersonation Session | A session in which a super admin acts as a user within a tenant's environment for support or diagnostic purposes. |
| INSERT-only | A database privilege configuration in which the application database user holds only `INSERT` rights on the `audit_log` table; `UPDATE` and `DELETE` rights are not granted. |

### 1.4 Applicable Standards and Regulations

| Standard / Regulation | Relevance |
|---|---|
| IEEE Std 830-1998 | Software Requirements Specification structure and verifiability criteria. |
| Uganda Companies Act Cap. 110 | Mandates a minimum 5-year retention period for financial and transactional records. Longhorn ERP defaults to 7 years. |
| ISO/IEC 27001 | Information security management — audit trail requirements as part of the access control and logging control objectives. |
| NIST SP 800-92 | Guide to computer security log management — log capture, protection, and analysis. |
| OWASP Logging Cheat Sheet | Application-level logging best practices covering sensitive data exclusion and log integrity. |
| Uganda Data Protection and Privacy Act 2019 | Governs retention and handling of personal data contained within audit records (user identity, IP address). |
