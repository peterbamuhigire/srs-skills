## 7. Traceability Matrix

This matrix traces every functional and non-functional requirement in this specification to its originating business goal and confirms the existence of a deterministic test oracle (pass/fail criterion), per IEEE 1012 and the V&V Standard Operating Procedure in `CLAUDE.md`.

### 7.1 Business Goals Reference

| ID | Business Goal |
|---|---|
| BG-01 | Maintain a complete, tamper-evident record of all system activity to support financial audits and regulatory compliance. |
| BG-02 | Comply with the Uganda Companies Act Cap. 110 minimum 5-year records retention requirement (system default: 7 years). |
| BG-03 | Enable external auditors to independently search, review, and export audit data without requiring system staff involvement. |
| BG-04 | Detect and report any unauthorised modification to stored audit records. |
| BG-05 | Ensure audit logging does not degrade application performance under normal operating load. |
| BG-06 | Provide a complete authentication trail to support incident response and security investigations. |
| BG-07 | Ensure super admin impersonation is fully visible and traceable to prevent privilege abuse. |

### 7.2 Functional Requirements Traceability

| Requirement ID | Title | Business Goal | Test Oracle Present | Section |
|---|---|---|---|---|
| **FR-AUDIT-001** | Universal event capture | BG-01 | Yes | 2.1 |
| **FR-AUDIT-002** | Audit record schema — all 12 fields | BG-01 | Yes | 2.1 |
| **FR-AUDIT-003** | old_values / new_values on UPDATE | BG-01, BG-04 | Yes | 2.1 |
| **FR-AUDIT-004** | Action enumeration | BG-01 | Yes | 2.1 |
| **FR-AUDIT-005** | tenant_id from session context only | BG-01, BG-03 | Yes | 2.1 |
| **FR-AUDIT-006** | Login attempt logging | BG-06 | Yes | 2.2 |
| **FR-AUDIT-007** | Failed login — no password logging | BG-06 | Yes | 2.2 |
| **FR-AUDIT-008** | Logout logging | BG-06 | Yes | 2.2 |
| **FR-AUDIT-009** | Impersonation session start | BG-07 | Yes | 2.3 |
| **FR-AUDIT-010** | Impersonation session end | BG-07 | Yes | 2.3 |
| **FR-AUDIT-011** | Super admin attribution during impersonation | BG-07 | Yes | 2.3 |
| **FR-AUDIT-012** | Per-row bulk operation logging | BG-01 | Yes | 2.4 |
| **FR-AUDIT-013** | bulk_operation_id grouping | BG-01 | Yes | 2.4 |
| **FR-AUDIT-014** | Mobile API action logging | BG-01 | Yes | 2.5 |
| **FR-AUDIT-015** | API user_agent capture | BG-01 | Yes | 2.5 |
| **FR-AUDIT-016** | Background job logging | BG-01 | Yes | 2.6 |
| **FR-AUDIT-017** | job_execution_id grouping | BG-01 | Yes | 2.6 |
| **FR-AUDIT-018** | Tenant configuration change logging | BG-01 | Yes | 2.7 |
| **FR-AUDIT-019** | RBAC change logging | BG-01, BG-07 | Yes | 2.7 |
| **FR-AUDIT-020** | Tenant account lifecycle logging | BG-01 | Yes | 2.7 |
| **FR-AUDIT-030** | No UPDATE/DELETE on audit_log | BG-01, BG-04 | Yes | 3.1 |
| **FR-AUDIT-031** | INSERT-only privilege grant | BG-01, BG-04 | Yes | 3.1 |
| **FR-AUDIT-032** | Database trigger second-layer enforcement | BG-04 | Yes | 3.1 |
| **FR-AUDIT-033** | SHA-256 hash at insert | BG-04 | Yes | 3.2 |
| **FR-AUDIT-034** | Tamper verification report | BG-04 | Yes | 3.2 |
| **FR-AUDIT-035** | Tamper report — flagged record fields | BG-04 | Yes | 3.2 |
| **FR-AUDIT-036** | Tamper report execution logged | BG-01, BG-04 | Yes | 3.2 |
| **FR-AUDIT-037** | AuditLogService exclusive write path | BG-04 | Yes | 3.3 |
| **FR-AUDIT-038** | AuditLogService public interface restriction | BG-04 | Yes | 3.3 |
| **FR-AUDIT-039** | Dedicated connection pool for audit writes | BG-01, BG-05 | Yes | 3.3 |
| **FR-AUDIT-040** | Durable queue for audit writes under DB failure | BG-01 | Yes | 3.3 |
| **FR-AUDIT-050** | Role-based audit log read restriction | BG-03 | Yes | 4.1 |
| **FR-AUDIT-051** | external_auditor role definition | BG-03 | Yes | 4.1 |
| **FR-AUDIT-052** | Tenant isolation on audit log queries | BG-01, BG-03 | Yes | 4.1 |
| **FR-AUDIT-053** | Search filter interface | BG-03 | Yes | 4.2 |
| **FR-AUDIT-054** | Independent filter combination | BG-03 | Yes | 4.2 |
| **FR-AUDIT-055** | Default 30-day date range | BG-03 | Yes | 4.2 |
| **FR-AUDIT-056** | Search results column set | BG-03 | Yes | 4.2 |
| **FR-AUDIT-057** | Server-side pagination | BG-03, BG-05 | Yes | 4.2 |
| **FR-AUDIT-058** | CSV export | BG-03 | Yes | 4.3 |
| **FR-AUDIT-059** | Excel export | BG-03 | Yes | 4.3 |
| **FR-AUDIT-060** | PDF export with header metadata | BG-03 | Yes | 4.3 |
| **FR-AUDIT-061** | All fields in all export formats | BG-03 | Yes | 4.3 |
| **FR-AUDIT-062** | Export action logged | BG-01 | Yes | 4.3 |
| **FR-AUDIT-063** | Record detail view with JSON rendering | BG-03 | Yes | 4.4 |
| **FR-AUDIT-064** | Direct URL per audit record | BG-03 | Yes | 4.4 |
| **FR-AUDIT-065** | Hyperlink to affected record | BG-03 | Yes | 4.4 |
| **FR-AUDIT-070** | 7-year minimum retention period | BG-02 | Yes | 5.1 |
| **FR-AUDIT-071** | Retention period display | BG-02 | Yes | 5.1 |
| **FR-AUDIT-072** | Automatic archival to audit_log_archive | BG-02 | Yes | 5.2 |
| **FR-AUDIT-073** | audit_log_archive immutability | BG-02, BG-04 | Yes | 5.2 |
| **FR-AUDIT-074** | Unified search spanning live and archived records | BG-03 | Yes | 5.2 |
| **FR-AUDIT-075** | Super admin deletion with confirmation phrase | BG-02 | Yes | 5.3 |
| **FR-AUDIT-076** | Deletion event logged | BG-01, BG-02 | Yes | 5.3 |
| **FR-AUDIT-077** | Deletion prohibited before retention period expires | BG-02 | Yes | 5.3 |

### 7.3 Non-Functional Requirements Traceability

| Requirement ID | Category | Business Goal | Measurable Metric | Section |
|---|---|---|---|---|
| **NFR-AUDIT-001** | Security / Immutability | BG-01, BG-04 | 100% permission denied on UPDATE/DELETE via pen test | 6 |
| **NFR-AUDIT-002** | Performance — Write Latency | BG-05 | Audit INSERT P99 ≤ 100 ms | 6 |
| **NFR-AUDIT-003** | Performance — Search Latency | BG-03, BG-05 | Search P95 ≤ 5 s at 10M records | 6 |
| **NFR-AUDIT-004** | Concurrency | BG-03 | Search P95 ≤ 5 s under 10 concurrent auditor sessions | 6 |
| **NFR-AUDIT-005** | Performance — Page Load | BG-05 | Page render P95 ≤ 2 s at 100 concurrent users | 6 |
| **NFR-AUDIT-006** | Compliance — Retention | BG-02 | Zero records deleted before 7-year threshold | 6 |

### 7.4 Compliance Cross-Reference

| Regulation / Standard | Requirements Addressed |
|---|---|
| Uganda Companies Act Cap. 110 (5-year minimum) | FR-AUDIT-070, FR-AUDIT-072, FR-AUDIT-075, FR-AUDIT-077, NFR-AUDIT-006 |
| ISO/IEC 27001 — A.12.4 Logging and Monitoring | FR-AUDIT-001 through FR-AUDIT-020, FR-AUDIT-030 through FR-AUDIT-040 |
| OWASP Logging Cheat Sheet | FR-AUDIT-007 (no password logging), FR-AUDIT-005 (tenant isolation) |
| NIST SP 800-92 | FR-AUDIT-033, FR-AUDIT-034, FR-AUDIT-040 |
| Uganda Data Protection and Privacy Act 2019 | FR-AUDIT-070, FR-AUDIT-075, FR-AUDIT-007 |

### 7.5 Open Gaps

No context gaps or V&V failures were identified during the authoring of this document. All requirements trace to a defined business goal and carry a deterministic test oracle.

*Consultant review is required before this document is promoted to baseline. Apply the Human Review Gate as specified in `CLAUDE.md` Section "Skill Execution Workflow."*
