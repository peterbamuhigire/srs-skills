# Architecture Decision Records

Architecture Decision Records (ADRs) document significant architectural choices, the options considered, and the rationale for the decision taken. They provide the historical context needed to re-evaluate a decision when circumstances change.

---

## ADR-001: Shared Database vs. Separate Database Per Tenant

**Status:** Accepted

**Date:** 2026-04-05

**Context:**

Multi-tenant SaaS platforms may isolate tenant data using (a) a separate database per tenant, (b) a separate schema per tenant within a shared database server, or (c) a shared database with row-level tenant isolation via a `tenant_id` column on every operational table.

**Decision:**

The system adopts option (c): shared database with row-level tenant isolation.

**Rationale:**

- A separate database per tenant requires dynamic database connection management, complicates migrations (each tenant database must be migrated independently), and increases operational cost linearly with tenant count.
- A separate schema per tenant has similar migration complexity and limited support in MySQL 9.1 connection pooling.
- A shared database with row-level isolation allows a single migration script to update all tenants simultaneously, simplifies the connection pool configuration, and reduces infrastructure cost at the SME price points targeted by Longhorn ERP.

**Mitigation:**

Row-level isolation is enforced by strict application-layer controls: `tenant_id` is always sourced from the authenticated session (never from request parameters); the middleware pipeline validates tenant context on every request; cross-tenant access returns HTTP 404 to prevent tenant enumeration; and all SQL queries are parameterised (no raw string concatenation). NFR-SEC-001 defines the compliance requirement.

**Trade-off Accepted:**

A misconfigured query that omits a `WHERE tenant_id = ?` clause could expose cross-tenant data. This risk is mitigated by code review standards, PHPStan 1.11 static analysis, and the PHPUnit integration test suite which verifies tenant isolation on every data-access method.

---

## ADR-002: PHP 8.3 + MySQL 9.1 vs. Node.js / PostgreSQL

**Status:** Accepted

**Date:** 2026-04-05

**Context:**

The backend technology stack must be chosen to support: a service-oriented architecture with dependency injection, a complex relational data model, a WAMP (Windows Apache MySQL PHP) development environment, and a solo developer with deep PHP expertise.

**Decision:**

The system adopts PHP 8.3 (strict types, PSR-4) with MySQL 9.1 (InnoDB, UTF8MB4).

**Rationale:**

- The lead developer's primary expertise is PHP. A technology switch would introduce learning-curve risk without a clear technical benefit for this use case.
- PHP 8.3 offers strong type safety (strict types declaration), modern object-oriented features, named arguments, and fibers. PHP-DI 7.0 provides a production-grade dependency injection container.
- MySQL 9.1 InnoDB is the default engine in the WAMP development environment, ensuring parity between development and production. MySQL's stored procedure support is used for complex transactional operations (General Ledger posting, sequential numbering).
- The PHP ecosystem provides mature, well-maintained libraries for every integration requirement: `firebase/php-jwt`, `mPDF`, `PhpOffice/PhpSpreadsheet`, `PHPMailer`, `respect/validation`.
- Node.js/PostgreSQL would require rebuilding the entire tooling ecosystem, re-evaluating all library choices, and retraining the developer — without a compelling technical advantage for a synchronous, CRUD-heavy ERP workload.

**Trade-off Accepted:**

PHP is not suited to long-lived asynchronous workloads (real-time event streaming, WebSocket servers). These workloads are addressed through polling patterns in the web UI and push notifications in the mobile app rather than persistent server-side connections.

---

## ADR-003: Session Auth (Web) + JWT (Mobile) vs. Unified Token Auth

**Status:** Accepted

**Date:** 2026-04-05

**Context:**

The system must authenticate both browser-based web clients and native mobile clients. Options considered: (a) session-based auth for both, (b) JWT-based auth for both, or (c) session-based auth for web with JWT for mobile.

**Decision:**

The system adopts option (c): session-based authentication for the web UI and JWT Bearer token authentication for the mobile API.

**Rationale:**

- Browser clients benefit from session cookies: the browser manages the cookie lifecycle automatically, HttpOnly prevents JavaScript access, and SameSite=Strict provides CSRF protection at the browser level. There is no need for the web application to manage token storage in JavaScript.
- Native mobile clients cannot use HTTP cookies reliably across app restarts and background/foreground transitions. JWT tokens stored in the device secure enclave (Android Keystore, iOS Secure Enclave) provide the appropriate security model for stateless mobile authentication.
- JWT tokens carry the tenant context (`tid`, `uid`, `role`, `modules`) as claims, removing the need for a server-side session lookup on every mobile API request — important for stateless horizontal scaling.
- A unified JWT approach for the web would require the web application to manage token storage in JavaScript (localStorage or sessionStorage), increasing the XSS attack surface.

**Trade-off Accepted:**

Two separate authentication mechanisms increase implementation complexity and mean that session management code and JWT validation code must both be maintained. This is accepted because the security properties of each mechanism align well with the respective client environment.

---

## ADR-004: Configuration-Driven Localisation vs. Per-Country Code Forks

**Status:** Accepted

**Date:** 2026-04-05

**Context:**

Longhorn ERP targets multiple countries in Uganda (Phase 1), East Africa (Phase 2), Francophone Africa (Phase 3), and global markets (Phase 4). Each market has different currencies, tax rates, statutory deductions, regulatory integrations, and document formats. Options: (a) maintain a separate code branch per country, or (b) encode all jurisdiction-specific behaviour in a configuration profile consumed by a single codebase.

**Decision:**

The system adopts option (b): configuration-driven localisation. All jurisdiction-specific behaviour is stored in a `localisation_profiles` table. The application code references the active profile via `TenantContext::getLocalisationProfile()`.

**Rationale:**

- Per-country code forks diverge over time and create unsustainable maintenance overhead. A bug fix in the core engine must be applied to every fork.
- Configuration-driven localisation allows the platform to expand to a new market without a code deployment. Only a new profile record and, if required, a new gateway adapter in the Integration Layer are needed.
- The approach enforces a clean boundary between business logic ("how to calculate PAYE") and jurisdiction data ("what are Uganda's PAYE bands") — the same boundary required by IFRS and tax compliance standards.
- Uganda is the Phase 1 reference implementation. The profile structure is validated against a fully defined Uganda profile before any additional market is onboarded.

**Trade-off Accepted:**

Some integrations (URA EFRIS, KRA iTax) require implementing gateway adapter classes in the Integration Layer. These adapters are code, not configuration. The ADR does not claim zero code per market — it claims zero code in the core business logic per market.

---

## ADR-005: Module Activation Per Tenant vs. Per User

**Status:** Accepted

**Date:** 2026-04-05

**Context:**

Module access can be controlled at two granularities: (a) per-tenant (all users of a tenant either have access to the module or do not), or (b) per-user (individual users within a tenant can be granted or denied access to specific modules).

**Decision:**

Module activation is controlled at the tenant level as the primary gate. Within an activated module, per-user access is controlled by the Role-Based Access Control (RBAC) system.

**Rationale:**

- Module activation is a commercial decision tied to the tenant's subscription plan. It is appropriate to gate this at the tenant level because the subscription fee covers the whole organisation, not individual users.
- Per-user module activation would create an inconsistent user experience: two colleagues at the same company could see different navigation menus and features with no clear commercial reason.
- RBAC already provides per-user access control within a module. A user with the HR & Payroll module active can still be restricted from specific HR operations (e.g., payroll processing) by the `RequirePermission` middleware. This is the correct granularity for per-user control.
- Keeping module gating at the tenant level simplifies the billing and subscription management logic: one activation record per module per tenant.

**Trade-off Accepted:**

A tenant cannot activate a module for some users only. If a tenant wants only 2 out of 20 users to access the CRM module, they activate the module for the tenant and then restrict the remaining 18 users via RBAC role configuration. This is operationally straightforward and aligns with how ERP systems are typically administered.
