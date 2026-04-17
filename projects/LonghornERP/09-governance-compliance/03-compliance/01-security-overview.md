# Security Design Philosophy

## 1.1 Governing Principles

Security in Longhorn ERP is not a layer applied after design — it is a design constraint applied before every architectural decision. The following five principles govern all security controls in this platform.

### 1.1.1 Defence in Depth

The system shall enforce multiple independent security controls at each tier: network, application, data, and audit. The failure of any single control shall not expose tenant data or enable unauthorised access. Controls include, but are not limited to: transport-layer encryption, application-layer authentication, database-level tenant isolation, and an immutable audit trail.

### 1.1.2 Least Privilege

Every user, service account, and database user shall hold the minimum permissions required to perform its defined function. The application database user shall hold SELECT, INSERT, UPDATE, and DELETE on operational tables only. It shall hold INSERT-only access on the `audit_log` table. It shall hold no DROP, ALTER, TRUNCATE, or GRANT permissions in any production environment.

### 1.1.3 Zero Trust Between Tenant Boundaries

No tenant context shall be inferred from request parameters, URL segments, HTTP headers, or request body fields. The system shall resolve tenant identity exclusively from server-side session state or cryptographically verified token claims. Every service layer invocation shall receive `$tenantId` as an explicit, server-resolved parameter — never from caller-supplied input.

### 1.1.4 Immutable Audit Trail

Every state-changing operation — create, update, delete, approve, reject, impersonate — shall produce an audit record that cannot be modified or deleted by any database user, application user, or super administrator. The `audit_log` table shall be INSERT-only, enforced at the database privilege level.

### 1.1.5 OWASP Top 10 Compliance

The system shall address all ten vulnerability categories defined in the Open Web Application Security Project (OWASP) Top 10 (2021 edition). Section 8 of this document maps each category to the specific controls implemented.

## 1.2 Security Requirements Are Functional Requirements

Security requirements in this document are classified as functional requirements, not optional non-functional requirements (NFRs). A security requirement not met is a feature not delivered. A critical-severity security defect — defined as any defect that permits cross-tenant data access, audit log tampering, or privilege escalation — blocks the release of the affected module. No exception process exists for critical security defects.

## 1.3 Applicable Standards

| Standard | Scope |
|---|---|
| OWASP Top 10 (2021) | Web and Application Programming Interface (API) security |
| NIST Special Publication (SP) 800-63B | Authentication assurance levels, password policy, two-factor authentication (2FA) |
| Uganda Data Protection and Privacy Act 2019 | Data retention, employee data rights, sub-processor obligations |
| ISO/IEC 27001:2022 | Information security management — audit and compliance baseline |
| NITA-U SaaS Guidelines | Cloud Software as a Service (SaaS) provider obligations in Uganda |
| IEEE Std 830-1998 | Requirement verifiability criteria |
