# Section 2: Overall Description

## 2.1 Product Perspective

Maduuka is a new, standalone SaaS product. It does not replace or extend an existing Chwezi Core Systems product in Phase 1. It operates as an independent multi-tenant platform with its own dedicated backend, database, and mobile/web clients.

**System boundary:** Maduuka consists of three client components (Android app, iOS app [Phase 2], web application) communicating with a single REST API backend. The backend connects to a MySQL database, Wasabi S3-compatible file storage, and external services (MTN MoMo, Airtel Money, Africa's Talking, Firebase/APNs). No client-to-client communication occurs; all data flows through the API.

**Tenant hierarchy:** Platform (Chwezi Core Systems) --> Business (tenant) --> Branches --> Warehouses/Floors/Room blocks. Every database entity belongs to exactly one franchise_id. Queries that cross franchise boundaries are architecturally impossible.

**Phase 2 integration point:** The Academia Pro school management platform (Chwezi Core Systems) may integrate with Maduuka for canteen POS and school shop management in Phase 4. The API design in Phase 1 must not preclude this integration. No Phase 1 development action is required for this integration.

## 2.2 Product Functions Summary

Phase 1 delivers 10 core modules available on both Android and Web simultaneously:

| Module | Primary Function |
|---|---|
| F-001: POS | Process sales, collect payments, issue receipts |
| F-002: Inventory | Track stock levels, movements, valuation, reorder |
| F-003: Customer Management | Manage customer profiles, credit accounts, debtors |
| F-004: Supplier Management | Manage suppliers, purchase orders, goods receiving |
| F-005: Expenses | Record and categorise all business expenditure |
| F-006: Financial Accounts | Track cash position across all payment accounts |
| F-007: Sales Reporting | Generate sales analytics across all dimensions |
| F-008: HR and Payroll | Manage staff, compute payroll, generate NSSF/PAYE |
| F-009: Dashboard | Real-time business health overview |
| F-010: Settings | Configure all business parameters |

All 10 modules are available on all plans. Subscription plan limits control capacity (number of users, branches, products, storage) -- not feature access.

## 2.3 User Characteristics

Five primary user types interact with Maduuka in Phase 1. Full persona profiles are in `_context/personas.md`.

**Business Owner (Nakato / Namukasa personas):** Primary decision-maker and account holder. Ranges from a sole trader with Standard 7 education (Nakato) to a multi-branch owner with a degree (Namukasa). Accesses dashboard, reports, approvals, and HR on both mobile and web. Mobile is the primary interface for owners who are not at a fixed desk.

**Cashier / POS Operator (Wasswa persona):** Front-line staff processing sales all day. Low to medium tech literacy. Uses only the POS module. Speed and simplicity are critical -- every extra tap costs customer-facing time. Must be able to learn the POS without formal training.

**HR Manager (Apio persona):** Back-office staff with high tech literacy (Excel, web apps). Primarily uses web interface for payroll processing and NSSF/PAYE report generation. Needs accuracy above all else.

**Restaurant Manager (Ocen persona):** Medium-high tech literacy. Uses table management, KOT, and reporting on Android phone. Phase 2 feature -- documented here for context only; no Phase 1 requirements derived from this persona.

**Inventory / Accounts Staff:** Medium tech literacy. Uses inventory and financial modules on both web and mobile. Primarily data entry and report review roles.

## 2.4 General Constraints

### 2.4.1 Regulatory Constraints

- **Uganda Data Protection and Privacy Act 2019:** Maduuka stores customer purchase histories, employee salary records, and business financial records. All personal data collection, storage, and processing must comply with this Act. A legal review of data handling practices is required before Phase 1 release (GAP-002 in _context/gap-analysis.md).
- **Uganda NSSF Act:** Employer payroll contributions (10%) and employee contributions (5%) must be calculated and reported in the format required by NSSF Uganda.
- **Uganda Income Tax Act:** PAYE must be calculated using the current Uganda Revenue Authority tax bands and reported in URA format.
- **LST Ordinances:** Local Service Tax must be calculated using the tier structure of the employee's local government jurisdiction.

### 2.4.2 Hardware Constraints

- The Android application must operate on a device with a minimum of 2 GB RAM and Android API level 26 (Android 8.0 Oreo) or higher.
- The Android application must function on a device costing as little as UGX 250,000 as of 2026 (approximately a Samsung Galaxy A-series entry-level device).
- The web application must function on any modern browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+).
- No minimum hardware requirement is imposed on the web interface beyond a device with a supported browser released within the last 5 years.

### 2.4.3 Offline-First Mandate

The Android application must record POS sales, stock adjustments, and expense entries when internet connectivity is completely unavailable. This is a hard constraint, not an optional feature. Any architecture that requires connectivity for basic transaction recording fails this constraint.

### 2.4.4 Single-API Constraint

The backend must expose a single REST API consumed by both the Android client and the web client. No platform-specific endpoints are permitted. The same endpoint must serve both `Authorization: Bearer <token>` (mobile) and session-cookie (web) authenticated requests, with the authentication method determined by the request headers.

### 2.4.5 Language and Currency

Phase 1 must support English and Swahili as selectable per-user languages. No currency symbol is hardcoded; the functional currency is configured per business account during onboarding. Phase 1 default: Ugandan Shilling (UGX).

## 2.5 Assumptions and Dependencies

| ID | Assumption / Dependency |
|---|---|
| ASS-001 | MTN MoMo Business API credentials and sandbox access are obtained before the POS payment module is built. (GAP-001) |
| ASS-002 | Africa's Talking provides SMS and WhatsApp Business API access for receipt delivery and notifications. |
| ASS-003 | MySQL 8.x is the production database. No other RDBMS is supported in Phase 1. |
| ASS-004 | Wasabi S3-compatible object storage is used for product images, receipt photos, and payslip PDFs. |
| ASS-005 | Firebase Cloud Messaging (FCM) is used for Android push notifications. |
| ASS-006 | Uganda PAYE tax bands in this SRS reflect the Uganda Income Tax Act as of 2026-04-05. A maintenance process for annual URA updates is defined in GAP-008. |
| ASS-007 | The Uganda NSSF employer rate is 10% and the employee rate is 5% as of 2026-04-05. |
| ASS-008 | The web application is deployed on a VPS with Nginx and Let's Encrypt SSL in a Uganda-region or low-latency African data centre. |
| ASS-009 | Users onboard themselves without calling Chwezi Core Systems support. The onboarding wizard (6 steps) must be self-explanatory. |
