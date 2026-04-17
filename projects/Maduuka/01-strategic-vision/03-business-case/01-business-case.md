---
title: "Business Case: Maduuka POS & Bookkeeping SaaS"
project: Maduuka
version: "1.0"
date: "2026-04-05"
author: "Peter Bamuhigire — Chwezi Core Systems"
status: Draft
---

# Business Case: Maduuka POS & Bookkeeping SaaS

| Field | Value |
|---|---|
| Project | Maduuka |
| Version | 1.0 |
| Date | 2026-04-05 |
| Author | Peter Bamuhigire — Chwezi Core Systems |
| Status | Draft |

## Executive Summary

Ugandan small businesses — over 1.1 million SMBs — operate on pirated Windows POS software, exercise books, or Excel spreadsheets. These solutions provide no cloud backup, no mobile access, and no path to Uganda Revenue Authority (URA) Electronic Fiscal Receipting and Invoicing System (EFRIS) compliance. A single hardware failure wipes all business records.

Maduuka is a mobile-first SaaS POS and bookkeeping platform targeting this market at UGX 30,000–180,000/month — less than a standard monthly airtime recharge. Phase 1 delivers an Android (Kotlin/Compose) and Web (PHP 8.3+/Bootstrap 5) platform with 10 core modules.

Year 1 revenue target: 1,000 paying accounts × average UGX 80,000/month = UGX 80,000,000 Annual Recurring Revenue (ARR). Total Phase 1 investment is estimated at UGX 18,000,000–36,000,000 (2–5 person team, 6–9 months). Break-even occurs at approximately 250–450 accounts depending on team burn rate.

## Problem Statement

### Operational Context

Uganda's SMB sector operates with no viable, affordable, cloud-connected point-of-sale or bookkeeping solution. The dominant "solution" is pirated Windows POS software distributed on USB drives, typically priced at UGX 50,000–150,000 as a one-time purchase.

### Identified Failure Modes

- *No cloud backup:* All transaction records reside on a single PC. Hardware failure, theft, or power surge causes permanent, unrecoverable data loss.
- *No mobile access:* Business owners cannot view real-time sales, stock levels, or financials from their phone.
- *No EFRIS compliance:* URA mandates EFRIS integration for all VAT-registered businesses. Pirated software cannot interface with the URA EFRIS API. Non-compliance carries UGX 2,000,000+ fines per infraction.
- *No supplier or HR integration:* Pirated POS software handles sales only; expenses, payroll, and supplier management remain in exercise books.
- *No multi-device support:* A business operating 2 tills must buy 2 pirated licenses, install on 2 PCs, and reconcile manually.
- *No updates or support:* Pirated software receives no security patches, feature updates, or vendor support.

### Gap Statement

No locally developed, mobile-first, EFRIS-ready SaaS POS product exists in the Ugandan market at a price point accessible to informal and semi-formal SMBs. This is the market gap Maduuka addresses.

## Market Opportunity

### Target Segment

Maduuka Phase 1 targets Ugandan SMBs in the following verticals:

- Retail shops (general merchandise, hardware, electronics)
- Pharmacies and chemists
- Restaurants and bars
- Guesthouses and budget hotels
- Service businesses (salons, tailors, repair shops)

### Market Size Estimate

| Segment | Estimated Count | Source Basis |
|---|---|---|
| Registered SMBs (URSB) | ~600,000 | Uganda Registration Services Bureau estimates |
| Informal businesses (UBOS) | ~500,000 | Uganda Bureau of Statistics UNHS 2020 |
| Total addressable market | ~1,100,000 | Combined |
| EFRIS-mandated businesses (VAT-registered) | ~80,000 | URA 2023 VAT register estimate |
| Serviceable addressable market (Phase 1) | ~200,000 | Kampala CBD + major urban centres |
| Year 1 target (0.5% penetration) | 1,000 accounts | Phase 1 commercial goal |

*Note: Market size figures are estimates derived from publicly available government statistics. Exact figures require primary market research. Flag: [CONTEXT-GAP: Primary market research data not available in `_context/`].*

### Competitive Landscape

The primary competitor is *not* a legitimate SaaS provider — it is pirated Windows POS software. This distinction is material:

- Pirated software has no vendor, no support, and no upgrade path.
- Maduuka does not need to out-feature a well-funded SaaS competitor; it needs to demonstrate reliability and affordability versus a zero-support tool.
- Legitimate SaaS alternatives (QuickBooks Online, Wave) are priced in USD, require stable internet, and lack EFRIS integration — making them non-viable for the target segment.

### Geographic Expansion

Phase 4 targets pan-Africa expansion with payment gateway integration: M-Pesa (Kenya/Tanzania), Flutterwave, and Paystack (West Africa). The core platform architecture is designed to be locale-configurable from Phase 1.

## Proposed Solution

### Maduuka Phase 1 Scope

Phase 1 delivers a production-ready Android application (Kotlin/Compose) and a Web application (PHP 8.3+/Bootstrap 5) with the following 10 core modules:

1. POS (point-of-sale transaction processing)
2. Inventory management
3. Customer management and receivables
4. Supplier management and payables
5. Expense tracking
6. Financial accounts (chart of accounts, ledger)
7. Sales reports
8. HR and payroll (NSSF/PAYE computation)
9. Business dashboard (real-time KPIs)
10. Settings and multi-user access control

### Key Differentiators

- *Offline-first architecture:* Transactions recorded locally when connectivity is unavailable; synced when restored.
- *Android-native:* Operates on any Android phone — no dedicated POS hardware required.
- *EFRIS-ready:* Architecture supports URA EFRIS API integration (Phase 3), giving VAT-registered businesses a compliant upgrade path.
- *Uganda-native pricing:* Denominated in UGX; payment via MTN MoMo Business API.
- *Modular add-ons:* Restaurant/Bar, Pharmacy, Hotel, and Advanced Inventory add-ons sold separately, allowing businesses to pay only for what they need.

## Financial Projections

### Revenue Model

Maduuka generates revenue through 2 streams:

1. *Monthly SaaS subscriptions* — recurring, tiered by feature set.
2. *Industry add-on modules* — monthly incremental fees layered on top of any base tier.

### Subscription Tiers

| Tier | Price (UGX/month) | Inclusions |
|---|---|---|
| Basic | 30,000 | POS, Inventory, basic reports |
| Business | 80,000 | All 10 core modules |
| Pro | 180,000 | All modules + advanced analytics |
| Enterprise | Custom | Custom SLA and integrations |

### Add-On Modules

| Add-On | Price (UGX/month) |
|---|---|
| Restaurant / Bar | 30,000 |
| Pharmacy | 30,000 |
| Hotel / Accommodation | 50,000 |
| Advanced Inventory | 25,000 |
| EFRIS Integration | 40,000 |

### Year 1 Revenue Target

| Metric | Value |
|---|---|
| Target accounts (Month 12) | 1,000 |
| Average revenue per account | UGX 80,000/month |
| Monthly Recurring Revenue (MRR) at target | UGX 80,000,000 |
| Annual Recurring Revenue (ARR) at target | UGX 960,000,000 |
| Blended ARR (ramp from 0 to 1,000 over 12 months) | ~UGX 480,000,000 |

*Assumption: Linear account acquisition ramp. Actual ramp will vary. EFRIS add-on adoption (25% of Business/Pro tier) adds ~UGX 8,000,000–10,000,000 MRR at Year 1 target.*

### Break-Even Analysis

| Scenario | Monthly Burn (UGX) | Break-Even Account Count | Break-Even Timeline |
|---|---|---|---|
| 2-person team | ~3,000,000 | ~38 accounts @ avg 80K | Month 4–5 (est.) |
| 3-person team | ~5,500,000 | ~69 accounts @ avg 80K | Month 5–6 (est.) |
| 5-person team | ~10,000,000 | ~125 accounts @ avg 80K | Month 7–8 (est.) |

*Burn rate estimates assume Ugandan market salary benchmarks for software engineers (UGX 1,200,000–2,500,000/month), hosting costs (UGX 500,000–1,500,000/month on DigitalOcean/AWS Lightsail), and operating overhead (UGX 300,000–500,000/month). These are estimates; a detailed financial model requires actual salary agreements and infrastructure benchmarks. Flag: [CONTEXT-GAP: Confirmed team salaries and infrastructure cost breakdown not in `_context/`].*

### Add-On Revenue Potential

If 20% of the Year 1 account base purchases 1 add-on at an average of UGX 35,000/month:

- 200 add-on accounts × UGX 35,000 = UGX 7,000,000 additional MRR.
- This represents an 8.75% uplift on the base MRR target.

## Strategic Alternatives Considered

### Alternative 1: Desktop-Only Windows Application (Rejected)

**Description:** Develop a locally installed Windows application sold as a one-time or annual license.

**Rejection Rationale:**

- No cloud synchronisation — data loss risk identical to the problem being solved.
- No mobile access — fails the "real-time business health on Android" strategic goal.
- No EFRIS integration path — URA EFRIS API requires a server-side component.
- Distribution via USB is the piracy vector being displaced; this alternative reinforces it.
- No multi-device or multi-branch capability.

### Alternative 2: White-Label an Existing SaaS Platform (Rejected)

**Description:** License and rebrand an existing SaaS POS product (e.g., a regional African SaaS or a global platform).

**Rejection Rationale:**

- No offline-first capability in any evaluated candidate product — Uganda's internet reliability makes this a blocking deficiency.
- No EFRIS API integration — Uganda-specific compliance cannot be retrofitted into a foreign platform on a short timeline.
- White-label pricing eliminates the margin required to sustain a UGX 30,000/month entry tier.
- No control over the feature roadmap — Africa-expansion and Uganda-specific HR/payroll rules cannot be guaranteed.
- Long-term vendor lock-in with no IP ownership.

### Alternative 3: Maduuka — Mobile-First, Offline-First SaaS (Selected)

**Description:** Build a proprietary SaaS platform, Android-native + web, owned entirely by Chwezi Core Systems.

**Selection Rationale:**

- Offline-first architecture directly addresses the connectivity gap.
- Android-native eliminates the need for dedicated POS hardware.
- EFRIS integration is a planned phase — the architecture is designed for it from Phase 1.
- Full IP ownership enables Africa-wide expansion without third-party constraints.
- UGX-denominated pricing and MTN MoMo payment integration are feasible only on a proprietary stack.

## Risk Summary

The following risks from the Maduuka risk register are material to the business case decision.

### RISK-001 — MTN MoMo Business API Credentials Not Obtained (High)

| Field | Detail |
|---|---|
| Risk ID | RISK-001 |
| Severity | High |
| Description | MTN MoMo Business API sandbox credentials have not been obtained. Payment collection via MoMo cannot be tested or implemented until credentials are approved. |
| Impact | Phase 1 launch cannot include MoMo payment collection, blocking UGX-denominated subscription billing for the target market. |
| Mitigation | Submit MTN MoMo Business API application immediately. In parallel, implement manual bank transfer + M&E confirmation as a fallback billing mechanism. Set a gate: credentials must be obtained before Sprint 3. |
| Status | Open — tracked as GAP-001 |

### RISK-008 — Uganda Data Protection and Privacy Act 2019 Legal Review Not Complete (Critical)

| Field | Detail |
|---|---|
| Risk ID | RISK-008 |
| Severity | Critical |
| Description | Maduuka collects customer PII (names, phone numbers, purchase history) and employee PII (NIN, salary, NSSF number). No legal review of the Uganda Data Protection and Privacy Act 2019 (DPPA) has been completed. |
| Impact | Non-compliant data handling exposes Chwezi Core Systems to regulatory enforcement by the Personal Data Protection Office (PDPO). Potential fines and forced suspension of service. |
| Mitigation | Engage a Ugandan data protection legal counsel before Phase 1 launch. Implement DPPA-compliant data retention, consent, and access policies. Privacy policy and Terms of Service must be reviewed and approved. |
| Status | Open — blocking pre-launch compliance gate |

### RISK-007 — NSSF/PAYE Computation Legal Verification Pending (High)

| Field | Detail |
|---|---|
| Risk ID | RISK-007 |
| Severity | High |
| Description | The HR/Payroll module computes NSSF and PAYE deductions. The computation logic has not been verified against Uganda Revenue Authority PAYE tables and National Social Security Fund Act thresholds by a qualified accountant or tax adviser. |
| Impact | Incorrect NSSF/PAYE computation creates statutory liability for Maduuka customers. A single incorrect payroll filing can expose a customer business to URA penalties. |
| Mitigation | Engage a certified public accountant (CPA) to verify NSSF and PAYE computation logic against current URA PAYE tables and NSSF Act 2022 before the HR/Payroll module is released. Hard-code the verified formulas with a version-stamp and update mechanism tied to regulatory changes. |
| Status | Open — computation logic review gate before HR/Payroll module release |

## Investment Required

### Phase 1 Development Scope

Phase 1 delivers the full 10-module Android + Web platform described in Section 5. The estimated timeline is 6–9 months from project kickoff to production launch.

### Team Composition

| Role | Count | Type |
|---|---|---|
| Lead developer (Android + Backend) | 1 | Full-time |
| Web / Backend developer | 1 | Full-time or contract |
| UI/UX designer | 1 | Contract or shared |
| QA engineer | 1 | Contract or shared |
| Project lead / Product owner | 1 | Peter Bamuhigire (owner) |

### Infrastructure Estimate (Monthly, Phase 1)

| Item | Estimated Cost (UGX/month) |
|---|---|
| Cloud hosting (app server + DB) | 500,000–1,500,000 |
| Android Play Store developer account | ~30,000 (annual, one-time) |
| SMS/OTP gateway (Africa's Talking) | 200,000–500,000 |
| Domain + SSL + CDN | 100,000–300,000 |
| **Total infrastructure** | **830,000–2,330,000** |

### Total Phase 1 Investment Estimate

| Component | Estimated Cost (UGX) |
|---|---|
| Development salaries (6–9 months, 2–3 devs) | 14,400,000–33,750,000 |
| Infrastructure (6–9 months) | 4,980,000–20,970,000 |
| Legal and compliance (DPPA review, ToS) | 1,500,000–3,000,000 |
| Marketing and launch (digital, SMB outreach) | 2,000,000–5,000,000 |
| **Total Phase 1 estimate** | **22,880,000–62,720,000** |

*Flag: [CONTEXT-GAP: Confirmed developer salary agreements are not in `_context/`. Refine this estimate when actual team contracts are signed.]*

## Recommendation

The analysis in this document supports the following recommendation:

**Proceed with Phase 1 of Maduuka as specified.**

The following conditions must be satisfied before development begins:

1. Resolve **GAP-001**: Submit MTN MoMo Business API application and obtain sandbox credentials. Define a fallback billing mechanism in writing before Sprint 1.
2. Resolve **GAP-002**: Engage Ugandan data protection legal counsel and complete initial DPPA compliance review. No customer PII may be collected in production until consent and retention policies are approved.
3. Verify NSSF/PAYE computation logic with a certified public accountant before the HR/Payroll module is released to customers.
4. Conduct primary market research in Kampala CBD (minimum 30 SMB interviews) to validate the UGX 30,000–80,000 price point and identify the highest-priority vertical for Phase 1 go-to-market.

The market opportunity is real, the competitive moat (offline-first, Android-native, EFRIS-ready, UGX-priced) is defensible, and the Year 1 ARR target of UGX 960,000,000 at 1,000 accounts is achievable with a 2–5 person team if the compliance and API dependency risks are resolved before development gates.
