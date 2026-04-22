# System Overview

## 1.1 What Longhorn ERP Is

Longhorn ERP is a multi-tenant, service-oriented, cloud-hosted Enterprise Resource Planning (ERP) platform built for small-to-medium enterprises (SMEs) and cooperative organisations across Uganda and East Africa. The platform delivers a unified suite of business management modules — accounting, inventory, sales, procurement, human resources, manufacturing, cooperative procurement, and more — through a single shared codebase that serves every tenant simultaneously.

For industrial and logistics-intensive tenants, the high-level architecture treats Product Lifecycle Management (PLM), MES-grade Manufacturing, and Transportation & Fleet Operations as first-class bounded capabilities within the same platform. These capabilities are designed as peer domains alongside finance, inventory, procurement, and HR so that engineering control, production execution, and transport execution can evolve independently while still sharing the same tenancy, security, integration, audit, and master-data foundations.

For finance-intensive tenants, the architecture also treats the finance domain as more than basic bookkeeping. Finance is designed as a control-heavy platform capability that supports operational accounting, period close orchestration, approval-governed journal processing, recurring entries, and consolidation-ready group reporting. This allows Longhorn ERP to serve owner-managed businesses and multi-entity groups on the same platform without fragmenting the financial control model across separate tools.

The architecture is designed around five non-negotiable qualities:

- **Multi-tenancy:** Every tenant operates in a logically isolated workspace within a shared infrastructure. Row-level tenant isolation ensures no cross-tenant data leakage.
- **Modularity:** Business capabilities are packaged as independently activatable modules. Tenants activate only the modules their subscription plan permits.
- **Localisation-via-configuration:** The system supports multiple markets without code changes. All jurisdiction-specific behaviour — currency, tax rates, statutory deductions, date formats, legal text — is driven by a per-tenant localisation profile.
- **Extensibility:** New modules and integrations are added without modifying the core platform. The service-oriented architecture (SOA) and dependency injection container isolate business logic from the routing and rendering layers.
- **Performance:** The system shall render any data-entry page in ≤ 2 seconds at P95 under a load of 100 concurrent tenant users (NFR-PERF-001) and return any REST API response in ≤ 500 ms at P95 under 50 concurrent mobile clients per tenant (NFR-PERF-003).

## 1.2 System Context Diagram

```
                        ┌─────────────────────────────────────────────────┐
                        │                  LONGHORN ERP                   │
                        │              (Apache / PHP 8.3)                 │
                        │                                                 │
  ┌──────────────┐      │  ┌─────────────┐  ┌───────────────────────┐   │
  │  Tenant      │─────▶│  │  Tenant     │  │  Super Admin Panel    │   │
  │  Staff       │      │  │  Workspace  │  │  /public/superadmin/  │   │
  │  (Browser)   │◀─────│  │  /public/   │  │  (Chwezi operators)   │   │
  └──────────────┘      │  └─────────────┘  └───────────────────────┘   │
                        │         │                                       │
  ┌──────────────┐      │  ┌──────▼──────┐  ┌───────────────────────┐   │
  │  End Users   │─────▶│  │  End-User   │  │  Service Layer        │   │
  │  Employees / │      │  │  Portal     │  │  src/Services/        │   │
  │  Customers / │◀─────│  │  /public/   │  │  PLM / Manufacturing  │   │
  │  Agents /    │      │  │  portal/    │  └───────────┬───────────┘   │
  │  Farmers     │      │  └─────────────┘              │               │
  └──────────────┘      │                               │               │
                        │  ┌─────────────────────────────▼─────────┐   │
  ┌──────────────┐      │  │         MySQL 9.1 (InnoDB)            │   │
  │  Mobile Apps │─────▶│  │  Shared Database — Row-Level          │   │
  │  Android /   │      │  │  Tenant Isolation via tenant_id FK    │   │
  │  iOS         │◀─────│  └───────────────────────────────────────┘   │
  └──────────────┘      │                                               │
                        │  ┌───────────────────────────────────────┐   │
  ┌──────────────┐      │  │  Integration Layer                    │   │
  │  External    │◀────▶│  │  MTN MoMo · Airtel Money · M-Pesa    │   │
  │  Services    │      │  │  URA EFRIS · NSSF · KRA iTax         │   │
  └──────────────┘      │  │  Africa's Talking (SMS/USSD)         │   │
                        │  └───────────────────────────────────────┘   │
                        └─────────────────────────────────────────────────┘
```

## 1.2.1 First-Class Bounded Capabilities

Within the service layer, Longhorn ERP organises its industrial workflows into explicit bounded capabilities so that high-change operational domains remain cohesive and independently evolvable:

- **PLM:** Owns product definitions, product structures, revisions, engineering change control, specifications, and controlled release of approved product master data into downstream operational modules.
- **Manufacturing (MES-grade):** Owns production planning and execution, including bills of materials, routings, work centres, dispatching, work-order execution, in-process quality, traceability, downtime capture, and production performance monitoring.
- **Transportation & Fleet Operations:** Owns transport planning, dispatch, route and trip execution, load assignment, proof of delivery, vehicle and driver utilisation, fleet telemetry integration, and transport-operational visibility.

These bounded capabilities integrate with Inventory, Procurement, Sales, Assets, Finance, CRM, and mobile channels through the shared service layer and tenant-aware data platform shown above. This preserves the existing service-oriented SaaS architecture while making industrial lifecycle management and logistics execution explicit in the high-level design.

## 1.2.2 Finance Control and Group Reporting Capability

Within the same service-oriented architecture, Finance is treated as a first-class control and reporting capability with explicit sub-domains that can scale from SME bookkeeping to enterprise-grade financial governance:

- **Core Accounting:** Owns the chart of accounts, journal processing, subledger posting, bank reconciliation, tax accounting, budgets, and statutory ledgers.
- **Financial Close Management:** Owns period calendars, close checklists, task assignment, dependency tracking, completion evidence, and close-status governance at tenant and entity level.
- **Journal Governance and Approvals:** Owns approval-policy metadata, submission and review workflow, segregation-of-duties enforcement, and approval history for manual, recurring, and adjustment journals.
- **Recurring and Automated Accounting:** Owns recurring journal templates, generation schedules, accrual and prepayment automation patterns, and controlled creation of draft journals for review.
- **Consolidation and Eliminations:** Owns multi-entity group structures, consolidation periods, elimination and top-side adjustments, minority-interest-ready adjustment foundations, and group-reporting data sets.
- **Finance Control Evidence:** Owns attachment, attestation, reviewer sign-off, and immutable evidence trails for reconciliations, close tasks, approvals, and audit support.

This finance capability integrates tightly with Sales, Procurement, Payroll, Inventory, Manufacturing, Transportation, and Assets so that operational events generate financial postings while still remaining subject to close governance, approval controls, and group-reporting rules. The result is a platform architecture in which financial accuracy, auditability, and period-end discipline are treated as core architectural concerns rather than downstream reporting concerns.

## 1.3 Key Technology Decisions

| Layer | Technology | Version |
|---|---|---|
| Backend language | PHP (strict types, PSR-4) | 8.3+ |
| Architecture pattern | Service-oriented, Domain-Driven Design | — |
| Dependency injection | PHP-DI | 7.0 |
| Database engine | MySQL, InnoDB | 9.1 |
| Character set | UTF8MB4 | — |
| Web frontend framework | Bootstrap | 5.3.0 |
| JavaScript library | jQuery | 3.7.0 |
| Mobile — Android | Kotlin + Jetpack Compose | — |
| Mobile — iOS | Swift + SwiftUI | — |
| Web server | Apache with mod\_rewrite | — |

## 1.4 Deployment Model

Longhorn ERP operates as a single-instance, multi-tenant Software as a Service (SaaS) platform. All tenants share one Apache/PHP application process pool and one MySQL database server. Tenant isolation is enforced at the application layer (middleware pipeline) and at the data layer (row-level `tenant_id` foreign key). The platform shall support ≥ 500 concurrent active tenants on a single deployment without degradation beyond NFR-PERF-001 and NFR-PERF-003 thresholds (NFR-SCALE-001).
