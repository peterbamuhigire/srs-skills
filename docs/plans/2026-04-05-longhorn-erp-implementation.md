# Longhorn ERP Documentation — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Produce 45 professional, IEEE-compliant documentation deliverables for Longhorn ERP — a multi-tenant SaaS ERP platform by Chwezi Core Concepts — covering all 01-09 document sets.

**Architecture:** Documents are produced in dependency order: Foundation → Platform SRS → Module SRS → Design Documentation → Testing/Operations → End-User → Governance. All output is prospective ("shall" language). Localisation is configuration-only. All 17 modules are universal. Every `.docx` carries Chwezi Core Concepts ownership in its cover page.

**Tech Stack:** PHP 8.3, MySQL 9.1, Bootstrap 5.3, jQuery, PHP-DI, JWT Mobile API, Android (Kotlin/Compose), iOS (Swift/SwiftUI). Build tool: Pandoc via `scripts/build-doc.sh`.

**Working directory:** `C:\wamp64\www\srs-skills` (all paths relative to this root unless stated)

**Project directory:** `projects/LonghornERP/` (gitignored — client documentation, not committed)

**Development skills:** `C:\Users\Peter\.claude\skills` (for implementation tasks on the ERP codebase itself)

**Ownership block (required in every document's `00-cover.md`):**

```
© Chwezi Core Concepts | chwezicore.com | info@chwezicore.com
Lead Developer: Peter Bamuhigire | techguypeter.com | peter@techguypeter.com | +256784464178
Confidential — All Rights Reserved
```

---

## PRE-FLIGHT: Verify Context Files

Before executing any task, verify these files exist and are populated:

```
projects/LonghornERP/_context/vision.md        ✓
projects/LonghornERP/_context/stakeholders.md  ✓
projects/LonghornERP/_context/modules.md       ✓
projects/LonghornERP/_context/tech-stack.md    ✓
projects/LonghornERP/_context/gaps.md          ✓
projects/LonghornERP/_context/domain.md        ✓
projects/LonghornERP/_context/localisation.md  ✓
projects/LonghornERP/_context/glossary.md      ✓
```

---

## TASK 0: Create Ownership Cover Template

**Purpose:** Every `.docx` deliverable must contain the Chwezi ownership block. Create a reusable cover template.

**Files:**
- Create: `projects/LonghornERP/_context/cover-template.md`

**Step 1: Write the cover template**

```markdown
# {DOCUMENT_TITLE}

**Product:** Longhorn ERP

**Version:** 1.0

**Date:** {DATE}

**Prepared by:** Chwezi Core Concepts

---

| Field | Detail |
|---|---|
| Company | Chwezi Core Concepts |
| Website | chwezicore.com |
| Email | info@chwezicore.com |
| Lead Developer | Peter Bamuhigire |
| Developer Website | techguypeter.com |
| Developer Email | peter@techguypeter.com |
| Developer Phone | +256784464178 |

*Confidential — All Rights Reserved. This document is the intellectual property of Chwezi Core Concepts. No part may be reproduced or disclosed without written permission.*

---
```

**Step 2: For every document directory, create `00-cover.md`** from this template with the correct title and date filled in before running `build-doc.sh`.

**No build or commit required for this task — the template is an internal aid only.**

---

## TASK 1: Product Requirements Document (PRD)

**Skill:** `01-strategic-vision/01-prd-generation`

**Output:** `projects/LonghornERP/01-strategic-vision/01-prd/`
**Build output:** `projects/LonghornERP/01-strategic-vision/LonghornERP_PRD.docx`

**Step 1: Verify context is complete**

Read `_context/vision.md`, `_context/modules.md`, `_context/gaps.md`. Confirm all sections are populated with no `<!-- TODO -->` items blocking PRD generation.

**Step 2: Create cover page**

Create `projects/LonghornERP/01-strategic-vision/01-prd/00-cover.md` using the ownership template with title "Product Requirements Document".

**Step 3: Invoke PRD skill**

Run skill: `01-strategic-vision/01-prd-generation`

Source all content from `_context/` files. Generate sections:
- Executive Summary
- Problem Statement (ERP market in East Africa; pain points with SAP, Odoo, ERPNext)
- Product Vision and Golden Rule
- Target Market (all sectors, Uganda-first)
- Module Overview (all 17 modules — universal, no market gating)
- Competitive Positioning (UGX pricing table vs. competitors)
- Revenue Model (subscription plans: UGX 250,000–2,500,000/month)
- Success Metrics (MRR targets by phase, usability benchmark: 85% task success unassisted)
- Open Design Questions (from `_context/gaps.md` GAP-015 through GAP-018)

**Step 4: Flag review**

List all `[CONTEXT-GAP]`, `[GLOSSARY-GAP]`, `[SMART-FAIL]` flags. Resolve or acknowledge each before proceeding.

**Step 5: Create manifest**

Create `projects/LonghornERP/01-strategic-vision/01-prd/manifest.md`:
```
00-cover.md
01-executive-summary.md
02-problem-statement.md
03-vision-golden-rule.md
04-target-market.md
05-module-overview.md
06-competitive-positioning.md
07-revenue-model.md
08-success-metrics.md
09-open-questions.md
```

**Step 6: Build .docx**

```bash
cd /c/wamp64/www/srs-skills
bash scripts/build-doc.sh projects/LonghornERP/01-strategic-vision/01-prd LonghornERP_PRD
```

Expected: `projects/LonghornERP/01-strategic-vision/LonghornERP_PRD.docx`

---

## TASK 2: Vision Statement and Competitive Positioning

**Skill:** `01-strategic-vision/03-vision-statement`

**Output:** `projects/LonghornERP/01-strategic-vision/02-vision-statement/`
**Build output:** `projects/LonghornERP/01-strategic-vision/LonghornERP_Vision.docx`

**Step 1: Create cover**

Create `00-cover.md` with title "Vision Statement and Competitive Positioning".

**Step 2: Invoke vision skill**

Source from `_context/vision.md`. Generate:
- Mission statement
- Vision statement (5-year horizon)
- Golden Rule statement (no training required)
- Competitive differentiation matrix
- Market positioning map (vs. SAP, Oracle, Dynamics, Odoo, ERPNext)
- Target client profile (company size, sector, geography)

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/01-strategic-vision/02-vision-statement LonghornERP_Vision
```

---

## TASK 3: Business Case and Pricing Model

**Skill:** `01-strategic-vision/02-business-case`

**Output:** `projects/LonghornERP/01-strategic-vision/03-business-case/`
**Build output:** `projects/LonghornERP/01-strategic-vision/LonghornERP_BusinessCase.docx`

**Step 1: Create cover**

Create `00-cover.md` with title "Business Case and Pricing Strategy".

**Step 2: Generate business case**

Source from `_context/modules.md` (pricing section) and `_context/vision.md` (revenue milestones). Generate:

- Executive Summary
- Problem and Opportunity
- Proposed Solution
- Pricing Strategy (full UGX tiered table with rationale):
  - Starter: UGX 250,000/month — 5 users, 2 branches, core modules
  - Small Business: UGX 500,000/month — 15 users, 5 branches, core + 2 add-ons
  - Professional: UGX 1,000,000/month — 30 users, 10 branches, core + 5 add-ons
  - Business: UGX 1,750,000/month — 60 users, 20 branches, all add-ons
  - Enterprise: UGX 2,500,000/month — unlimited users and branches, all modules + priority support
- Annual billing incentive (10 months billed, 12 months access)
- A-la-carte add-on pricing table
- Upgrade trigger mechanics (stacking add-ons toward Enterprise threshold)
- Revenue model (MRR targets: UGX 56M → 188M → 450M → 1.1B+)
- Break-even analysis
- Risk register (from `_context/gaps.md`)

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/01-strategic-vision/03-business-case LonghornERP_BusinessCase
```

---

## TASK 4: Lean Canvas

**Skill:** `01-strategic-vision/04-lean-canvas`

**Output:** `projects/LonghornERP/01-strategic-vision/04-lean-canvas/`
**Build output:** `projects/LonghornERP/01-strategic-vision/LonghornERP_LeanCanvas.docx`

**Step 1: Generate Lean Canvas**

Source from `_context/vision.md` and `_context/stakeholders.md`. Populate all 9 Lean Canvas blocks:
- Problem, Customer Segments, Unique Value Proposition, Solution, Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage.

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/01-strategic-vision/04-lean-canvas LonghornERP_LeanCanvas
```

---

## TASK 5: Stakeholder Analysis

**Output:** `projects/LonghornERP/02-requirements-engineering/03-stakeholder-analysis/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/LonghornERP_StakeholderAnalysis.docx`

**Step 1: Generate stakeholder analysis**

Source from `_context/stakeholders.md`. Produce:
- Stakeholder register (all 10 personas from context file)
- Influence/interest matrix
- Communication plan (who gets which documents)
- Approval matrix (pending `_context/stakeholders.md` TODO items — flag as `[CONTEXT-GAP]` if unresolved)
- RACI matrix for key decisions

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/03-stakeholder-analysis LonghornERP_StakeholderAnalysis
```

---

## TASK 6: High-Level Architecture Document (HLD)

**Skill:** `03-design-documentation/01-high-level-design`

**Output:** `projects/LonghornERP/03-design-documentation/01-hld/`
**Build output:** `projects/LonghornERP/03-design-documentation/LonghornERP_HLD.docx`

**Step 1: Create cover**

Title: "High-Level Architecture Document".

**Step 2: Generate HLD**

Source from `_context/tech-stack.md`, `_context/domain.md`. Generate:

- System overview (3-tier panel architecture: Tenant Workspace `/public/`, Super Admin `/public/superadmin/`, End-User Portal `/public/portal/`)
- Architectural style (service-oriented, domain-driven, DI with PHP-DI)
- Component diagram (panels → middleware stack → service layer → database)
- Middleware stack: `EnsureAuthenticated → EnsureTenantSelected → EnsureTenantActive → EnsureBranchSelected → RequirePermission`
- Multi-tenancy model (shared database, row-level isolation, `tenant_id` always from session)
- Security architecture (session auth web; JWT mobile; CSRF; rate limiting; audit log)
- API architecture (web API session-based; mobile API v1 JWT; 497 endpoints organized by domain)
- Database architecture (MySQL 9.1, InnoDB, UTF8MB4, stored procedures for GL posting)
- Frontend architecture (Bootstrap 5.3, jQuery, one JS file per page)
- Mobile architecture (Android Kotlin/Compose + iOS Swift/SwiftUI consuming JWT REST API)
- Localisation Engine design (config-driven profiles, no code changes per market)
- Module system (core always active; add-ons per-tenant activation; module registry)
- Integration Layer overview (EFRIS, MoMo, Airtel, M-Pesa, Africa's Talking)
- Key architecture decisions and rationale (ADRs)

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/03-design-documentation/01-hld LonghornERP_HLD
```

---

## TASK 7: Database Design Document

**Skill:** `03-design-documentation/04-database-design`

**Output:** `projects/LonghornERP/03-design-documentation/04-database-design/`
**Build output:** `projects/LonghornERP/03-design-documentation/LonghornERP_DatabaseDesign.docx`

**Step 1: Generate database design**

Source from `_context/tech-stack.md`, `_context/modules.md`. Generate:

- Database engine specification (MySQL 9.1, InnoDB, UTF8MB4, UTF8MB4_unicode_ci)
- Multi-tenancy schema pattern (`tenant_id` FK on every operational table, always first in WHERE clauses)
- Entity groups and key tables per domain (Accounting, Inventory, Sales, Procurement, HR, POS, Manufacturing, Projects, Cooperative, Strategy, Assets)
- Core infrastructure tables (`tenants`, `users`, `roles`, `role_permissions`, `branches`, `audit_log`, `sessions`, `subscriptions`, `tenant_modules`, `module_registry`)
- ERD (logical model — all entities and relationships)
- Stored procedures specification (`sp_post_invoice_to_gl`, `sp_post_purchase_to_gl`, `sp_post_return_to_gl`, `sp_generate_entry_number`, `sp_get_account_mapping`)
- Views specification (`v_current_stock`, `v_customer_aging_analysis`, `v_supplier_aging_analysis`, `v_low_stock_items`, and all reporting views)
- Migration strategy (versioned migrations, idempotent, `run_migrations.php` entry point)
- Audit log design (INSERT-only, immutable, 7-year retention)
- Indexing strategy (tenant_id always first; composite indexes per domain)
- Data types and constraints standards

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/03-design-documentation/04-database-design LonghornERP_DatabaseDesign
```

---

## TASK 8: Coding Guidelines

**Skill:** `04-development-artifacts/02-coding-guidelines`

**Output:** `projects/LonghornERP/04-development-artifacts/02-coding-guidelines/`
**Build output:** `projects/LonghornERP/04-development-artifacts/LonghornERP_CodingGuidelines.docx`

**Step 1: Generate coding guidelines**

Source from `_context/tech-stack.md`. Cover:

- PHP 8.3 strict types (`declare(strict_types=1)` mandatory on every file)
- Tenant isolation rule (NEVER accept `tenant_id` from client; always from `TenantContext::getTenantId()`)
- Prepared statements only (NEVER concatenate user input into SQL)
- Output escaping (`htmlspecialchars()` on all user-derived output)
- CSRF validation on all state-changing operations
- Module gating (`requireModuleAccess('MODULE_CODE')` at top of every add-on page)
- Date storage (`Y-m-d`), display (`d M Y`)
- Number formatting (store without commas, display with commas)
- One JS file per page (no inline scripts); relative API paths in JS
- Service layer pattern (business logic in `src/Services/[Domain]/`, not in endpoints)
- Dependency injection (register all services in `bootstrap/container.php`)
- Response format (`ApiResponse` class for all REST responses)
- Error handling (no raw PHP errors to client; structured JSON errors only)
- Testing requirements (PHPUnit 11.2; PHPStan 1.11; PHP CS Fixer 3.64)
- Git commit message format

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/04-development-artifacts/02-coding-guidelines LonghornERP_CodingGuidelines
```

---

## TASK 9: Dev Environment Setup

**Output:** `projects/LonghornERP/04-development-artifacts/03-dev-environment-setup/`
**Build output:** `projects/LonghornERP/04-development-artifacts/LonghornERP_DevSetup.docx`

**Step 1: Generate setup guide**

Source from `_context/tech-stack.md`. Cover (prospective — written as specification, not as current state):
- Prerequisites (PHP 8.3+, MySQL 9.1+, Apache with mod_rewrite, Composer, WAMP for Windows)
- Repository setup and structure
- Environment configuration (`.env` from `.env.example` — all required variables)
- Database setup (schema application via `run_migrations.php`)
- Composer dependency installation
- Apache virtual host configuration
- Development tools setup (PHPUnit, PHPStan, PHP CS Fixer)
- Running the test suite
- Common setup issues and resolution

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/04-development-artifacts/03-dev-environment-setup LonghornERP_DevSetup
```

---

## TASK 10: Security Model and Compliance Framework

**Output:** `projects/LonghornERP/09-governance-compliance/03-compliance/`
**Build output:** `projects/LonghornERP/09-governance-compliance/LonghornERP_SecurityCompliance.docx`

**Step 1: Generate security and compliance document**

Source from `_context/domain.md` (NFR defaults), `_context/gaps.md` (GAP-004, GAP-007, GAP-014). Cover:
- Security architecture (OWASP Top 10 compliance, NIST SP 800-63B)
- Authentication model (session-based web; JWT mobile with refresh rotation)
- RBAC model (roles → permissions → functions × actions)
- Tenant isolation controls (middleware stack, session scoping, query isolation)
- Audit log immutability guarantee
- Data protection (Uganda Data Protection and Privacy Act 2019 — `[CONTEXT-GAP]` for unresolved items from GAP-007)
- NITA-U SaaS compliance obligations (`[CONTEXT-GAP: GAP-014]`)
- Uganda Companies Act data retention (7-year minimum)
- TLS 1.3 in transit; AES-256 at rest for sensitive fields
- Rate limiting design (token bucket, per-tenant and per-user)
- Penetration testing and security review requirements (GAP-004)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/09-governance-compliance/03-compliance LonghornERP_SecurityCompliance
```

---

## TASK 11: Platform SRS — Multi-Tenancy, Tenant Lifecycle, and Billing

**Skill:** `02-requirements-engineering/waterfall/01-initialize-srs` then `02-requirements-engineering/waterfall/05-feature-decomposition`

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/01-multitenancy-billing/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Platform_Tenancy.docx`

**Step 1: Initialize SRS**

Run skill `02-requirements-engineering/waterfall/01-initialize-srs` for this section. Set document ID prefix: `FR-PLAT-` and `NFR-PLAT-`.

**Step 2: Generate requirements**

FR categories to generate:
- Tenant provisioning (create, configure, activate)
- Tenant lifecycle state machine (Trial → Active → Overdue → Suspended → Archived)
- Module activation per tenant (`tenant_modules` table)
- Branch creation and management
- Subscription plan management (Starter/Small Business/Professional/Business/Enterprise)
- A-la-carte add-on activation and billing
- Annual billing with 2-month bonus
- Payment processing (card, bank transfer, MTN MoMo, M-Pesa)
- Super admin impersonation (audited, session-scoped)
- Tenant suspension and data archival
- Multi-currency per tenant (UGX, KES, TZS, RWF, etc.)

NFR categories: availability, data isolation, provisioning speed (≤ 10 minutes for new tenant).

**Step 3: Apply stimulus-response pattern**

Every FR must follow: *"The system shall [action] when [stimulus]."*
Example: *"The system shall activate the tenant's selected add-on module within 60 seconds when the Super Administrator confirms the module subscription."*

**Step 4: Flag all gaps**

Flag `[CONTEXT-GAP: GAP-015]` for white-labelling decision; `[CONTEXT-GAP: GAP-005]` for module dependency map.

**Step 5: Run semantic audit**

Run skill `02-requirements-engineering/waterfall/08-semantic-auditing`. Apply all IEEE 830 criteria.

**Step 6: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/01-multitenancy-billing LonghornERP_SRS_Platform_Tenancy
```

---

## TASK 12: Platform SRS — User Management and RBAC

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/02-rbac/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_RBAC.docx`

**Step 1: Generate RBAC requirements**

FR categories:
- User lifecycle (create, activate, deactivate, password reset, 2FA enrollment)
- Role management (create, clone, assign permissions)
- Permission model (function × action matrix: view/create/edit/approve/delete)
- Branch restrictions per user
- Approval limits per user per transaction type
- Session management (concurrent session control, session timeout, forced logout)
- 2FA (TOTP implementation)
- Biometric login integration (Zkteco)
- USSD access for warehouse workers
- Password policy enforcement (complexity, expiry, history)
- Super admin impersonation logging

NFRs: session invalidation within 5 seconds of account disable (NFR-SEC-003 from domain.md).

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/02-rbac LonghornERP_SRS_RBAC
```

---

## TASK 13: Platform SRS — Audit Log

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/03-audit-log/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_AuditLog.docx`

**Step 1: Generate audit log requirements**

FR categories:
- Immutability guarantee (INSERT-only; no UPDATE or DELETE permitted by any role including super admin)
- Scope (every create, update, delete, approve action across all modules)
- Record content (old values, new values, user ID, user name, IP address, timestamp, module, action, affected record ID)
- Search and filter (by date range, module, user, action type, record ID)
- Export (CSV, Excel, PDF)
- External auditor read-only role access
- Retention enforcement (7-year minimum; Uganda Companies Act)
- Tamper detection (hash chain or equivalent integrity mechanism)

NFR: audit log write latency ≤ 100 ms at P99 (must not degrade transaction performance).

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/03-audit-log LonghornERP_SRS_AuditLog
```

---

## TASK 14: Platform SRS — Localisation Engine

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/04-localisation/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Localisation.docx`

**Step 1: Generate localisation requirements**

Source from `_context/localisation.md`. FR categories:
- Localisation profile structure (all parameters from context file)
- Profile assignment per tenant
- Currency configuration (ISO 4217, symbol, decimal places)
- Language configuration (English, French, Swahili UI)
- Date and number format configuration
- Financial year configuration
- VAT/tax rate configuration per profile
- Statutory deduction rates per profile (PAYE, NSSF/CNSS, NHIF)
- Chart of accounts starter template per profile
- Invoice legal text per profile
- SMS gateway per profile
- Mobile money gateway per profile
- Fiscal receipt integration per profile (EFRIS, eTIMS, TRA, RRA)
- Global extension pattern (new country via profile, no code deployment)
- Uganda reference profile (full specification)
- Kenya, Tanzania, Rwanda profiles (specify; note external API gaps where applicable)
- Francophone profile structure (`[CONTEXT-GAP: GAP-010]` for OHADA COA)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/04-localisation LonghornERP_SRS_Localisation
```

---

## TASK 15: Platform SRS — Mobile API

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/05-mobile-api/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_MobileAPI.docx`

**Step 1: Generate mobile API requirements**

FR categories:
- JWT authentication (login, token issuance, refresh rotation, logout)
- Token claims (tenant_id, user_id, role, enabled modules)
- Tenant isolation enforcement (same rules as web; `tenant_id` from token, never from request body)
- API versioning strategy (v1/v2, backward compatibility)
- Rate limiting (per-tenant and per-user token bucket)
- Offline sync protocol (last-modified timestamp, delta sync, conflict resolution)
- Push notifications (module events → push to registered device tokens)
- SMS fallback (Africa's Talking when push unavailable)
- Data-lite mode (compressed responses for 3G/low-bandwidth connections)
- CORS policy (all origins permitted for native app clients)
- Error response structure (`{ "success": bool, "data": {}, "error": {} }`)
- Supported modules in mobile API (Sales, Inventory, HR, Approvals, Projects, Cooperative Procurement)

NFRs: API response ≤ 500 ms at P95 (NFR-PERF-003); offline resilience 72 hours (NFR-MOBILE-001).

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/05-mobile-api LonghornERP_SRS_MobileAPI
```

---

## TASK 16: Platform SRS — Integration Layer

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/06-integrations/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Integrations.docx`

**Step 1: Generate integration requirements**

FR categories per integration:
- **URA EFRIS** (`[CONTEXT-GAP: GAP-001]` — API spec pending): invoice submission, receipt retrieval, error handling
- **URA PAYE e-returns** (`[CONTEXT-GAP: GAP-002]`): payroll export in current URA format
- **NSSF Uganda** (`[CONTEXT-GAP: GAP-003]`): employer schedule export in portal format
- **MTN MoMo Uganda** (`[CONTEXT-GAP: GAP-011]`): B2C bulk payment, C2B payment verification
- **Airtel Money Uganda/Kenya**: B2C bulk payment, C2B payment verification
- **M-Pesa Daraja B2C** (`[CONTEXT-GAP: GAP-012]`): Kenya bulk payment
- **Africa's Talking**: SMS sending, USSD session management
- **KRA iTax** (`[CONTEXT-GAP: GAP-009]`): Kenya PAYE e-returns
- **NITA-U**: compliance reporting (`[CONTEXT-GAP: GAP-014]`)
- **Sibling products** (`[CONTEXT-GAP: GAP-017]`): Academia Pro, Medic8, Kulima integration points TBD

NFRs: integration failure handling (graceful degradation — core functions must not fail if integration is unavailable).

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/00-platform/06-integrations LonghornERP_SRS_Integrations
```

---

## TASK 17: Module SRS — Accounting and General Ledger

**Skill:** Full waterfall SRS pipeline (Skills 01–08)

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/01-accounting/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Accounting.docx`

**Step 1: Run full waterfall SRS pipeline**

Execute in order:
1. `02-requirements-engineering/waterfall/01-initialize-srs` — ID prefix: `FR-ACCT-`, `NFR-ACCT-`
2. `02-requirements-engineering/waterfall/02-context-engineering` — Source: `_context/`
3. `02-requirements-engineering/waterfall/03-descriptive-modeling` — Process model for GL posting cycle
4. `02-requirements-engineering/waterfall/04-interface-specification` — GL posting API, URA EFRIS interface, bank reconciliation import
5. `02-requirements-engineering/waterfall/05-feature-decomposition` — All features listed below
6. `02-requirements-engineering/waterfall/06-logic-modeling` — VAT calculation, WHT calculation, currency revaluation, period close logic (LaTeX formulas where applicable)
7. `02-requirements-engineering/waterfall/07-attribute-mapping` — Data types, constraints, validations
8. `02-requirements-engineering/waterfall/08-semantic-auditing` — IEEE 830 compliance check

**Step 2: Feature scope to cover**

- Chart of accounts (hierarchical, IFRS-compliant, Uganda COA starter, OHADA starter for Francophone)
- Double-entry journal entry (debit = credit validation; `[V&V-FAIL]` if imbalanced)
- Auto GL posting (from Sales, Procurement, HR, Manufacturing via stored procedures)
- Account mapping rules (item-level → category-level → system default, 3-level lookup)
- Accounts Payable (supplier invoices, payment allocation, aging report)
- Accounts Receivable (customer invoices, payment allocation, aging report)
- Bank accounts and bank reconciliation
- Multi-currency (exchange rates, revaluation, FX gain/loss posting)
- VAT/tax management (input tax, output tax, net VAT, URA return export — `[CONTEXT-GAP: GAP-002]`)
- Withholding tax (6% on services to non-VAT registered suppliers)
- Budgets (annual budget by account and cost centre; variance reporting)
- Cost centres
- Accounting periods and period close (flag `[CONTEXT-GAP: GAP-008]` for close behaviour specification)
- Financial statements: Balance Sheet, P&L, Cash Flow (IAS 7), Trial Balance
- URA EFRIS invoice submission (`[CONTEXT-GAP: GAP-001]`)
- URA VAT return export (`[CONTEXT-GAP: GAP-002]`)

**Step 3: LaTeX formulas required**

- VAT calculation: $VAT = BaseAmount \times Rate$
- WHT calculation: $WHT = GrossAmount \times WHTRate$
- Currency revaluation: $FXGain = (CurrentRate - BookRate) \times ForeignBalance$
- Account balance: $Balance = \sum Debits - \sum Credits$ (or vice versa depending on account type)

**Step 4: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/01-accounting LonghornERP_SRS_Accounting
```

---

## TASK 18: Module SRS — Inventory Management

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/02-inventory/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Inventory.docx`

**Step 1: Feature scope**

- Item catalogue (item master, categories, UOM, variants)
- UOM conversion matrix (purchase UOM → stock UOM → sales UOM)
- Stock valuation (FIFO, weighted average — configurable per item)
- Goods Receipt Note (GRN) — against PO or standalone
- Stock adjustments (positive and negative with reason codes)
- Reorder levels and reorder quantity
- Physical stock count (freeze → count → variance → post)
- Stock transfer between branches
- Stock ledger (immutable movement journal — analogous to GL for inventory)
- Barcode / QR code support (scan for item lookup, GRN, stock count)
- Mobile offline sync (last-modified timestamp)
- Real-time stock balance (from `v_current_stock` view)
- Low stock alerts (`v_low_stock_items` view)

**Step 2: LaTeX formulas**

- Weighted average cost: $WAC = \frac{\sum (Qty_i \times Cost_i)}{\sum Qty_i}$
- FIFO layer consumption: consumed from oldest layer first until quantity satisfied

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/02-inventory LonghornERP_SRS_Inventory
```

---

## TASK 19: Module SRS — Sales

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/03-sales/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Sales.docx`

**Step 1: Feature scope**

- Customer master (customer contacts, credit limits, payment terms)
- Price lists (multiple pricelists, currency-specific, date-effective)
- Quotation → Sales Order → Delivery Note → Invoice workflow
- Credit notes and sales returns
- Receipts and payment allocation (full and partial)
- Customer aging analysis
- EFRIS invoice submission (`[CONTEXT-GAP: GAP-001]`)
- MTN/Airtel MoMo payment verification via API
- WhatsApp invoice delivery
- PDF invoice generation (mPDF, branded with tenant logo)
- Delivery note with signature capture

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/03-sales LonghornERP_SRS_Sales
```

---

## TASK 20: Module SRS — Procurement

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/04-procurement/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Procurement.docx`

**Step 1: Feature scope**

- Supplier master (contacts, bank details, payment terms, WHT status)
- Purchase Requisition → RFQ → Supplier Comparison → LPO → GRN → Invoice → Payment workflow
- Three-way matching (PO ↔ GRN ↔ Supplier Invoice — auto flag mismatches)
- Approval workflow (PPDA thresholds — `[CONTEXT-GAP: GAP-006]` for current limits)
- Withholding tax deduction on supplier payments
- Supplier aging analysis
- Import landed cost allocation
- PPDA compliance workflow for government/parastatal tenants

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/04-procurement LonghornERP_SRS_Procurement
```

---

## TASK 21: Module SRS — HR and Payroll

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/05-hr-payroll/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_HRPayroll.docx`

**Step 1: Feature scope**

- Employee master (personal data, contracts, org structure, grade/salary scale)
- Leave types, leave requests, leave balances, leave calendar
- Attendance (biometric/mobile, shift management)
- Payroll elements (configurable earn/deduction components)
- Payroll run (monthly batch: gross → deductions → net)
- Statutory compliance (PAYE, NSSF, NITA — Uganda; NHIF/PAYE — Kenya; PSSSF — Tanzania; RSSB — Rwanda)
- Payslip generation (PDF, branded)
- Bank payment file generation
- MTN/Airtel bulk mobile money salary payment
- NSSF employer schedule export (`[CONTEXT-GAP: GAP-003]`)
- URA PAYE e-return (`[CONTEXT-GAP: GAP-002]`)
- Loans and advances (deduction from payroll)
- Exit management (terminal benefits calculation)
- Employee self-service portal (payslips, leave requests, attendance)
- Data protection compliance (`[CONTEXT-GAP: GAP-007]` — Uganda Data Protection Act)

**Step 2: LaTeX formulas**

- PAYE: $PAYE = \sum_{i=1}^{n} (Band_i \times Rate_i)$ where $Band_i$ is the taxable slice in band $i$
- NSSF: $NSSF_{employer} = GrossSalary \times 0.10$; $NSSF_{employee} = GrossSalary \times 0.05$
- Net Pay: $NetPay = GrossPay - \sum Deductions$

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/05-hr-payroll LonghornERP_SRS_HRPayroll
```

---

## TASK 22: Module SRS — Point of Sale

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/06-pos/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_POS.docx`

**Step 1: Feature scope**

- Touch-optimised terminal (Android tablet optimised)
- Barcode scanning (physical scanner and camera)
- Multi-payment modes (cash, mobile money, card, split)
- Mobile money push payment (MTN/Airtel — customer pays on prompt)
- Cash session management (open, close, cash reconciliation)
- Shift management (handover between cashiers)
- Multi-terminal (multiple tills per branch)
- Restaurant/bar table mode (table assignment, split bills, rounds)
- Thermal receipt printing (ESC/POS protocol)
- EFRIS fiscal receipt (`[CONTEXT-GAP: GAP-001]`)
- 4-hour offline mode (queue transactions, sync on reconnect)
- Real-time stock deduction on sale
- Real-time GL posting on cash session close
- Daily sales summary and Z-report

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/06-pos LonghornERP_SRS_POS
```

---

## TASK 23: Module SRS — Advanced Inventory

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/07-advanced-inventory/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_AdvancedInventory.docx`

**Dependency:** Requires `FR-INV-*` IDs from Task 18.

**Step 1: Feature scope** (extends core Inventory)

- Multi-location warehousing (bin/rack locations within warehouse)
- Batch tracking (batch number, manufacturing date, expiry date)
- Serial number tracking
- FEFO picking strategy (mandatory for food, pharma, agro tenants)
- Expiry management and expiry alerts
- Inter-branch transfers with stock-in-transit state
- Landed cost allocation (distribute freight/duty across GRN items by weight/value/quantity)
- Stock reservation (reserve stock for a sales order before delivery)
- Recall management (identify and quarantine all affected batches)
- Cold chain compliance fields (temperature ranges for storage/transit)
- UNBS certification tracking
- Maize/grain batch fields (Uganda-specific agro-processing)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/07-advanced-inventory LonghornERP_SRS_AdvancedInventory
```

---

## TASK 24: Module SRS — Manufacturing

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/08-manufacturing/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Manufacturing.docx`

**Dependency:** Requires `FR-ADVINV-*` from Task 23.

**Step 1: Feature scope**

- BOM management (multiple versions, effective dates)
- Production orders (schedule, issue raw materials, track WIP)
- Raw material issue (from warehouse to production; stock deduction)
- WIP tracking (current production state per order)
- Yield and variance analysis (planned vs. actual output)
- By-products and co-products
- QC checkpoints (pass/fail at each checkpoint; block completion on fail)
- Scrap management (scrap recording and GL posting)
- Overhead absorption (machine time, labour time → finished goods cost)
- Production costing (full cost roll-up to finished goods)
- Uganda-specific BOM structures: sugar, edible oil, flour milling, dairy, brewing

**Step 2: LaTeX formulas**

- Production cost: $Cost_{FG} = Cost_{RM} + Cost_{Labour} + Cost_{Overhead} - Value_{ByProduct}$
- Yield variance: $YieldVariance = (ActualOutput - PlannedOutput) \times StandardCost$

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/08-manufacturing LonghornERP_SRS_Manufacturing
```

---

## TASK 25: Module SRS — Sales and CRM

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/09-sales-crm/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_SalesCRM.docx`

**Step 1: Feature scope**

- Leads pipeline (create, qualify, convert)
- Opportunities management (Kanban view, stage tracking, close probability)
- Activity logging (calls, emails, meetings, WhatsApp conversations)
- Contact management (individual contacts, linked to customers)
- Quotation tracking (link opportunity → quotation → sales order)
- Sales forecasting (weighted pipeline, monthly/quarterly)
- Territory management (assign reps to territories)
- Lost deal analysis (reason codes, competitor attribution)
- Customer satisfaction (NPS surveys, score tracking)
- Mobile CRM for field reps

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/09-sales-crm LonghornERP_SRS_SalesCRM
```

---

## TASK 26: Module SRS — Sales Agents and Commissions

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_SalesAgents.docx`

**Step 1: Feature scope**

- Agent register (personal details, territory, active products)
- Sales target setting (monthly/quarterly by agent)
- Sales attribution (link sales invoices to agent)
- Commission rules (flat rate, tiered, product-specific)
- Monthly commission run (batch calculation and approval)
- Commission approval workflow
- Mobile money bulk payment to agents (MTN/Airtel)
- Agent self-service portal (view sales, commissions, targets, statements)
- Agent stock management (agents who hold inventory: stock balance, issue, return)
- Remittance verification (money collected by agent, verified against sales)
- Daily activity summaries

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents LonghornERP_SRS_SalesAgents
```

---

## TASK 27: Module SRS — Cooperative Procurement

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/11-cooperative/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Cooperative.docx`

**Step 1: Feature scope**

- Commodity configuration (commodity types, grade, price per grade)
- Farmer/outgrower registration (NIN, GPS coordinates, bank/MoMo details)
- Group/society hierarchy (individual → group → primary society → union)
- Seasonal intake periods
- Commodity intake recording (weight, grade, price, deductions)
- Weighbridge RS-232 serial integration (auto-capture weight)
- Input loan deductions (deduct outstanding loan from payment)
- Levy deductions (society levy, union levy)
- Mobile money bulk farmer payment (MTN/Airtel/M-Pesa)
- Farmer statement generation (per season, per farmer)
- Price management (floor price, market price, premium)
- Offline intake mode (mobile app, 72-hour offline support — NFR-MOBILE-001)
- Uganda cooperatives: tea, coffee, sugarcane, matooke
- Kenya: KTDA structure
- Rwanda: NAEB cooperatives

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/11-cooperative LonghornERP_SRS_Cooperative
```

---

## TASK 28: Module SRS — Project Management

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/12-projects/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Projects.docx`

**Step 1: Feature scope**

- Project register (name, client, budget, dates, type)
- Project budget by cost category
- Milestones and milestone billing
- Tasks / Work Breakdown Structure (WBS)
- Timesheets (employee time logging against tasks)
- Resource allocation (assign employees to projects)
- Project costs (pull from: procurement POs, payroll timesheets, expense claims)
- Project billing: time-and-materials (timesheets × billing rate) and milestone-based
- Subcontractor management
- Project P&L (revenues vs. costs)
- Gantt chart view
- Portfolio view (all projects by status, health, budget utilisation)
- Retention management (construction industry: hold X% until completion)
- NGO donor project tracking (donor, grant, budget lines)
- PPDA procurement linkage for government projects

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/12-projects LonghornERP_SRS_Projects
```

---

## TASK 29: Module SRS — Strategy and Balanced Scorecard

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/13-strategy-bsc/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_StrategyBSC.docx`

**Step 1: Feature scope**

- Strategic framework (mission, vision, strategic themes)
- BSC perspectives (configurable: Financial, Customer, Internal Process, Learning — or custom)
- Strategic objectives per perspective
- KPIs per objective (definition, formula, unit, target, frequency)
- Actual data collection (manual entry or auto-pull from ERP modules)
- Traffic-light scoring (green/amber/red based on thresholds)
- Scorecard dashboard (executive view)
- Initiative tracking (link strategic initiatives to objectives)
- Executive report generation (PDF)
- OKR mode (Objectives and Key Results — alternative framework)
- NGO logframe mapping (Output, Outcome, Impact)
- NDP III indicators (Uganda National Development Plan)
- Department workplans linked to strategic objectives

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/13-strategy-bsc LonghornERP_SRS_StrategyBSC
```

---

## TASK 30: Module SRS — Asset Management

**Output:** `projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/14-assets/`
**Build output:** `projects/LonghornERP/02-requirements-engineering/01-srs/LonghornERP_SRS_Assets.docx`

**Step 1: Feature scope**

- Asset register (asset master, category, location, custodian)
- Depreciation (straight-line and reducing balance; configurable per asset class)
- Asset revaluation (upward and downward; revaluation reserve posting)
- Disposal (sale/write-off with gain/loss GL posting)
- Asset transfer (between branches or custodians; with GL entry)
- Maintenance scheduling (planned maintenance calendar, work order generation)
- Maintenance history
- Insurance tracking (policy number, insurer, renewal date, sum insured)
- QR/barcode asset tagging (print labels, scan for lookup)
- Physical verification (scan assets to confirm existence and location)
- Book vs. tax depreciation (deferred tax computation — Uganda requirement)
- Vehicle fleet management (mileage tracking, service records, fuel logs)

**Step 2: LaTeX formulas**

- Straight-line depreciation: $Dep = \frac{Cost - ResidualValue}{UsefulLife}$
- Reducing balance: $Dep_n = NBV_{n-1} \times Rate$
- Deferred tax: $DTL = (TaxBase - CarryingAmount) \times TaxRate$

**Step 3: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/14-assets LonghornERP_SRS_Assets
```

---

## TASK 31: Low-Level Design (LLD)

**Skill:** `03-design-documentation/02-low-level-design`

**Output:** `projects/LonghornERP/03-design-documentation/02-lld/`
**Build output:** `projects/LonghornERP/03-design-documentation/LonghornERP_LLD.docx`

**Step 1: Generate LLD**

For each module, specify:
- Service class names and responsibilities (e.g., `AccountingService`, `InvoiceService`, `StockLedgerService`)
- Key methods with signatures
- Inter-service dependencies (which services call which)
- Database interaction patterns (which tables each service reads/writes)
- Stored procedure call points
- Event triggers (what causes GL auto-posting, stock ledger entries, audit log writes)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/03-design-documentation/02-lld LonghornERP_LLD
```

---

## TASK 32: API Specification

**Skill:** `03-design-documentation/03-api-specification`

**Output:** `projects/LonghornERP/03-design-documentation/03-api-spec/`
**Build output:** `projects/LonghornERP/03-design-documentation/LonghornERP_APISpec.docx`

**Step 1: Generate API specification**

Produce OpenAPI 3.0-compatible specification covering all endpoint domains:
- Authentication (session login, JWT mobile login, logout, refresh)
- Accounting (GL accounts, journals, invoices, payments, reports)
- Inventory (items, stock balance, GRN, adjustments, transfers)
- Sales (customers, quotations, orders, invoices, receipts, returns)
- Procurement (suppliers, requisitions, LPOs, GRN, supplier invoices)
- HR & Payroll (employees, leave, attendance, payroll, payslips)
- POS (sessions, transactions, receipts)
- Mobile v1 (all mobile API endpoints)
- Super Admin (tenant management, module activation, billing)

For each endpoint document: method, path, description, request headers, request body schema, response schema, error codes, authentication requirement, rate limit.

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/03-design-documentation/03-api-spec LonghornERP_APISpec
```

---

## TASK 33: UX Specification

**Skill:** `03-design-documentation/05-ux-specification`

**Output:** `projects/LonghornERP/03-design-documentation/05-ux-spec/`
**Build output:** `projects/LonghornERP/03-design-documentation/LonghornERP_UXSpec.docx`

**Step 1: Generate UX specification**

Cover:
- Design principles (Golden Rule: zero mandatory training; usability benchmark NFR-USAB-001)
- Layout system (Bootstrap 5.3 12-column grid, 3-panel sidebar layout)
- Navigation structure (left sidebar, role-based menu items, module-gated visibility)
- Typography and colour system
- Component library (DataTables, Select2, SweetAlert2, Flatpickr, Dropzone)
- Form design patterns (validation feedback, required fields, save/cancel)
- Table interaction patterns (server-side pagination, column sorting, search, export)
- Confirmation patterns (SweetAlert2 for all destructive actions)
- Mobile UX patterns (Android tablet POS; mobile app interaction design)
- Per-module wireframe specifications:
  - Dashboard (KPI widgets, charts, quick actions)
  - GL Journal Entry
  - Sales Invoice
  - POS Terminal
  - HR Payroll Run
  - Cooperative Intake (offline-capable)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/03-design-documentation/05-ux-spec LonghornERP_UXSpec
```

---

## TASK 34: Test Strategy

**Skill:** `05-testing-documentation/01-test-strategy`

**Output:** `projects/LonghornERP/05-testing-documentation/01-test-strategy/`
**Build output:** `projects/LonghornERP/05-testing-documentation/LonghornERP_TestStrategy.docx`

**Step 1: Generate test strategy**

Cover:
- Test objectives (IEEE 1012 V&V requirements)
- Test levels (unit: PHPUnit 11.2; integration; system; UAT)
- Test types (functional, security, performance, usability, regression, mobile)
- Static analysis (PHPStan 1.11 level 8)
- Security test approach (OWASP Top 10; tenant isolation penetration testing per GAP-004)
- Performance test targets (from NFR-PERF-001, NFR-PERF-002, NFR-PERF-003)
- Mobile test approach (Android emulator + physical device; iOS simulator + physical device)
- Test data management (per-tenant test data isolation)
- Defect severity classification (Critical, High, Medium, Low; definition of done)
- Continuous integration approach

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/05-testing-documentation/01-test-strategy LonghornERP_TestStrategy
```

---

## TASK 35: Test Plan

**Skill:** `05-testing-documentation/02-test-plan`

**Output:** `projects/LonghornERP/05-testing-documentation/02-test-plan/`
**Build output:** `projects/LonghornERP/05-testing-documentation/LonghornERP_TestPlan.docx`

**Step 1: Generate test plan**

For each module, specify test cases covering:
- Happy path (standard workflow end-to-end)
- Boundary conditions (zero values, maximum values, edge dates)
- Negative cases (invalid input, insufficient stock, unauthenticated access)
- Tenant isolation (cross-tenant data access attempt must return 404)
- Permission enforcement (access without required permission must be denied)
- Audit log creation (every state-changing action must produce an audit record)

Include: PHPUnit test class name, test method name, expected output for each case.

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/05-testing-documentation/02-test-plan LonghornERP_TestPlan
```

---

## TASK 36: Deployment Guide

**Skill:** `06-deployment-operations/01-deployment-guide`

**Output:** `projects/LonghornERP/06-deployment-operations/01-deployment-guide/`
**Build output:** `projects/LonghornERP/06-deployment-operations/LonghornERP_DeploymentGuide.docx`

**Step 1: Generate deployment guide**

May reference the specified tech stack as a design decision (not as current state). Cover:
- Server requirements (PHP 8.3+, MySQL 9.1+, Apache 2.4+ with mod_rewrite, TLS certificate)
- Recommended server specifications by tenant count (up to 100 tenants, 100–500 tenants, 500+ tenants)
- File system setup (document root, storage directory, log directory, permissions)
- Environment configuration (all `.env` variables with descriptions and example values)
- Database setup (schema deployment via `run_migrations.php`, initial seed data)
- Apache virtual host configuration (SSL, mod_rewrite rules)
- PHP configuration (`php.ini` settings: memory_limit, upload_max_filesize, session settings)
- MySQL configuration (`my.cnf` tuning for InnoDB performance)
- First-run checklist (super admin account, first tenant, subscription plan)
- Security hardening checklist (TLS 1.3 only; disable PHP display_errors; strict file permissions)
- Backup procedure (automated MySQL dump + file storage backup)
- Update procedure (migration runner, zero-downtime deployment steps)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/06-deployment-operations/01-deployment-guide LonghornERP_DeploymentGuide
```

---

## TASK 37: Runbook and Incident Response

**Output:** `projects/LonghornERP/06-deployment-operations/02-runbook/`
**Build output:** `projects/LonghornERP/06-deployment-operations/LonghornERP_Runbook.docx`

**Step 1: Generate runbook**

Cover:
- Daily operations checklist
- Common incidents and resolution steps (DB connection failure, session issues, payment gateway timeout, EFRIS submission failure)
- Log file locations and interpretation
- Database backup verification
- Performance degradation diagnosis
- Tenant suspension / reactivation procedure
- Data export / tenant offboarding procedure
- Emergency contact escalation path (Chwezi Core Concepts support)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/06-deployment-operations/02-runbook LonghornERP_Runbook
```

---

## TASK 38: User Manual

**Skill:** `08-end-user-documentation/01-user-manual`

**Output:** `projects/LonghornERP/08-end-user-documentation/01-user-manual/`
**Build output:** `projects/LonghornERP/08-end-user-documentation/LonghornERP_UserManual.docx`

**Step 1: Structure by role and module**

Produce role-based sections. Each section covers only what that role can see and do:
- **Finance Manager:** Accounting, Budgets, Financial Reports, Bank Reconciliation
- **Inventory Officer:** Inventory, GRN, Stock Counts, Stock Transfers
- **Sales Representative:** Sales, Quotations, Invoices, Payments, CRM
- **HR/Payroll Officer:** HR, Leave Management, Attendance, Payroll Run
- **Purchasing Officer:** Procurement, Requisitions, LPO, Supplier Management
- **POS Cashier:** POS Terminal, Cash Session, Receipt Printing
- **Field Agent:** Sales Agent Portal, Commission View, Mobile App
- **Cooperative Officer:** Farmer Registration, Commodity Intake, Payment Processing
- **Project Manager:** Projects, Tasks, Timesheets, Billing
- **System Administrator:** User Management, Role Configuration, Module Activation, Branch Setup

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/08-end-user-documentation/01-user-manual LonghornERP_UserManual
```

---

## TASK 39: Installation Guide (Tenant Onboarding)

**Output:** `projects/LonghornERP/08-end-user-documentation/02-installation-guide/`
**Build output:** `projects/LonghornERP/08-end-user-documentation/LonghornERP_OnboardingGuide.docx`

**Step 1: Generate tenant onboarding guide**

Cover:
- Subscription signup and plan selection
- Tenant workspace first-time setup wizard
- Chart of accounts configuration (choose starter template or customise)
- Opening balances entry
- Branch and warehouse setup
- User creation and role assignment
- Module activation (add-on selection)
- Localisation profile selection (country, currency, tax configuration)
- Integration setup (EFRIS credentials, MoMo API keys, SMTP)
- Import existing data (customers, suppliers, items, employees)
- Migrating from Odoo / ERPNext (`[CONTEXT-GAP: GAP-013]` — migration scripts pending)
- Go-live checklist

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/08-end-user-documentation/02-installation-guide LonghornERP_OnboardingGuide
```

---

## TASK 40: Traceability Matrix

**Output:** `projects/LonghornERP/09-governance-compliance/01-traceability-matrix/`
**Build output:** `projects/LonghornERP/09-governance-compliance/LonghornERP_TraceabilityMatrix.docx`

**Step 1: Generate traceability matrix**

For every FR-*-* identifier in every Module SRS (Tasks 17–30):
- Link to business goal in PRD
- Link to test case in Test Plan
- Flag `[TRACE-GAP: <FR-ID>]` for any FR missing either link

Produce summary statistics: total FRs, FRs with full traceability, FRs with gaps.

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/09-governance-compliance/01-traceability-matrix LonghornERP_TraceabilityMatrix
```

---

## TASK 41: Risk Assessment

**Output:** `projects/LonghornERP/09-governance-compliance/04-risk-assessment/`
**Build output:** `projects/LonghornERP/09-governance-compliance/LonghornERP_RiskAssessment.docx`

**Step 1: Generate risk assessment**

Source from `_context/gaps.md`. For each of the 18 gaps, produce a risk entry:
- Risk ID, description, probability (H/M/L), impact (H/M/L), risk score
- Mitigation action
- Owner
- Target resolution date

Add additional operational risks:
- EFRIS downtime (URA API unavailable — mitigation: queue and retry)
- Mobile money API changes (mitigation: abstraction layer in Integration Service)
- Uganda Data Protection Act non-compliance (mitigation: legal review per GAP-007)
- Tenant data breach (mitigation: multi-tenancy security review per GAP-004)
- Exchange rate volatility affecting UGX pricing (mitigation: annual price review mechanism)

**Step 2: Build .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/09-governance-compliance/04-risk-assessment LonghornERP_RiskAssessment
```

---

## TASK 42: Definition of Done and Definition of Ready

**Output:** `projects/LonghornERP/07-agile-artifacts/02-dod/` and `projects/LonghornERP/07-agile-artifacts/03-dor/`
**Build outputs:** `LonghornERP_DoD.docx` and `LonghornERP_DoR.docx`

**Step 1: Definition of Done**

A module feature is Done when:
1. All FR-*-* requirements for the feature are implemented
2. PHPUnit tests pass with ≥ 80% line coverage for the service class
3. PHPStan reports zero errors at level 8
4. PHP CS Fixer reports zero violations
5. All state-changing operations produce audit log records (verified by integration test)
6. All API endpoints for the feature return correct responses (functional test)
7. Tenant isolation verified: cross-tenant access attempt returns 404 (security test)
8. Feature reviewed against UX Specification for layout and interaction compliance
9. No `[CONTEXT-GAP]`, `[V&V-FAIL]`, or `[TRACE-GAP]` flags open for the feature

**Step 2: Definition of Ready**

A feature is Ready to develop when:
1. SRS section for the feature has no open `[CONTEXT-GAP]` flags
2. All referenced FR identifiers exist in the SRS
3. DB schema for the feature is defined in `database/schema/`
4. API endpoint spec is defined in the API Specification
5. Glossary entries for all new terms are present in `_context/glossary.md`
6. Design decision on any open gaps (from `_context/gaps.md`) is recorded

**Step 3: Build both .docx**

```bash
bash scripts/build-doc.sh projects/LonghornERP/07-agile-artifacts/02-dod LonghornERP_DoD
bash scripts/build-doc.sh projects/LonghornERP/07-agile-artifacts/03-dor LonghornERP_DoR
```

---

## COMMIT CADENCE

Commit after each completed task batch:

```bash
# After Foundation tasks (Tasks 1–10):
git add docs/plans/
git commit -m "docs: complete Longhorn ERP foundation documentation (01-strategic-vision, HLD, DB design, security)"

# After Platform SRS (Tasks 11–16):
git commit -m "docs: complete Longhorn ERP platform SRS (tenancy, RBAC, audit, localisation, mobile API, integrations)"

# After Module SRS Tasks 17–23 (Core modules):
git commit -m "docs: complete Longhorn ERP core module SRS (accounting, inventory, sales, procurement, HR, POS, advanced inventory)"

# After Module SRS Tasks 24–30 (Add-on modules):
git commit -m "docs: complete Longhorn ERP add-on module SRS (manufacturing, CRM, agents, cooperative, projects, BSC, assets)"

# After Design Documentation Tasks 31–33:
git commit -m "docs: complete Longhorn ERP design documentation (LLD, API spec, UX spec)"

# After remaining tasks (34–42):
git commit -m "docs: complete Longhorn ERP testing, operations, user docs, and governance documentation"
```

---

## DOCUMENT EXECUTION ORDER SUMMARY

| Task | Document | Output File |
|---|---|---|
| 0 | Cover Template | (internal — no .docx) |
| 1 | PRD | `LonghornERP_PRD.docx` |
| 2 | Vision Statement | `LonghornERP_Vision.docx` |
| 3 | Business Case | `LonghornERP_BusinessCase.docx` |
| 4 | Lean Canvas | `LonghornERP_LeanCanvas.docx` |
| 5 | Stakeholder Analysis | `LonghornERP_StakeholderAnalysis.docx` |
| 6 | HLD | `LonghornERP_HLD.docx` |
| 7 | Database Design | `LonghornERP_DatabaseDesign.docx` |
| 8 | Coding Guidelines | `LonghornERP_CodingGuidelines.docx` |
| 9 | Dev Environment Setup | `LonghornERP_DevSetup.docx` |
| 10 | Security & Compliance | `LonghornERP_SecurityCompliance.docx` |
| 11 | SRS: Platform — Multi-Tenancy & Billing | `LonghornERP_SRS_Platform_Tenancy.docx` |
| 12 | SRS: Platform — RBAC | `LonghornERP_SRS_RBAC.docx` |
| 13 | SRS: Platform — Audit Log | `LonghornERP_SRS_AuditLog.docx` |
| 14 | SRS: Platform — Localisation Engine | `LonghornERP_SRS_Localisation.docx` |
| 15 | SRS: Platform — Mobile API | `LonghornERP_SRS_MobileAPI.docx` |
| 16 | SRS: Platform — Integration Layer | `LonghornERP_SRS_Integrations.docx` |
| 17 | SRS: Accounting & GL | `LonghornERP_SRS_Accounting.docx` |
| 18 | SRS: Inventory Management | `LonghornERP_SRS_Inventory.docx` |
| 19 | SRS: Sales | `LonghornERP_SRS_Sales.docx` |
| 20 | SRS: Procurement | `LonghornERP_SRS_Procurement.docx` |
| 21 | SRS: HR & Payroll | `LonghornERP_SRS_HRPayroll.docx` |
| 22 | SRS: Point of Sale | `LonghornERP_SRS_POS.docx` |
| 23 | SRS: Advanced Inventory | `LonghornERP_SRS_AdvancedInventory.docx` |
| 24 | SRS: Manufacturing | `LonghornERP_SRS_Manufacturing.docx` |
| 25 | SRS: Sales & CRM | `LonghornERP_SRS_SalesCRM.docx` |
| 26 | SRS: Sales Agents | `LonghornERP_SRS_SalesAgents.docx` |
| 27 | SRS: Cooperative Procurement | `LonghornERP_SRS_Cooperative.docx` |
| 28 | SRS: Project Management | `LonghornERP_SRS_Projects.docx` |
| 29 | SRS: Strategy & BSC | `LonghornERP_SRS_StrategyBSC.docx` |
| 30 | SRS: Asset Management | `LonghornERP_SRS_Assets.docx` |
| 31 | Low-Level Design | `LonghornERP_LLD.docx` |
| 32 | API Specification | `LonghornERP_APISpec.docx` |
| 33 | UX Specification | `LonghornERP_UXSpec.docx` |
| 34 | Test Strategy | `LonghornERP_TestStrategy.docx` |
| 35 | Test Plan | `LonghornERP_TestPlan.docx` |
| 36 | Deployment Guide | `LonghornERP_DeploymentGuide.docx` |
| 37 | Runbook | `LonghornERP_Runbook.docx` |
| 38 | User Manual | `LonghornERP_UserManual.docx` |
| 39 | Tenant Onboarding Guide | `LonghornERP_OnboardingGuide.docx` |
| 40 | Traceability Matrix | `LonghornERP_TraceabilityMatrix.docx` |
| 41 | Risk Assessment | `LonghornERP_RiskAssessment.docx` |
| 42 | Definition of Done / Ready | `LonghornERP_DoD.docx` + `LonghornERP_DoR.docx` |
