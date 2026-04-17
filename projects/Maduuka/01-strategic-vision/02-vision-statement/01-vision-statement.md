---
title: "Maduuka — Vision Statement"
project: "Maduuka"
version: "1.0"
date: "2026-04-05"
author: "Peter Bamuhigire"
organization: "Chwezi Core Systems"
status: "Draft"
---

# Vision Statement — Maduuka SaaS POS + Bookkeeping Platform

## 1. Document Header

| Field | Value |
|---|---|
| Project | Maduuka |
| Version | 1.0 |
| Date | 2026-04-05 |
| Author | Peter Bamuhigire |
| Organization | Chwezi Core Systems (chwezicore.com) |
| Contact | techguypeter.com · +256784464178 |
| Status | Draft |

## 2. Executive Vision Statement

Maduuka is a mobile-first *Software as a Service* (SaaS) platform that delivers point-of-sale (POS) and bookkeeping capability to small and medium businesses (SMBs) across Africa. The platform runs on any Android device, operates offline, and synchronises all records automatically on reconnection — eliminating the single point of failure that defines pirated desktop software. Any shopkeeper who can operate WhatsApp can complete a sale, record an expense, and read a daily financial summary without training.

Chwezi Core Systems builds Maduuka as a Uganda-first product that expands continent-wide. Phase 1 targets the Android and web channels with 10 core operational modules priced from UGX 30,000 per month — less than a typical mobile-data bundle. Every tier includes EFRIS-ready transaction records, removing the compliance barrier that currently blocks formal tax registration for thousands of informal businesses.

The product displaces pirated Windows POS software not by matching its feature list but by eliminating the hardware dependency, the data-loss risk, and the non-compliance exposure that make pirated software a liability. Maduuka turns a UGX 250,000 Android phone into a fully auditable business system.

## 3. Problem Statement

Hundreds of thousands of SMBs across Uganda — sole traders, market stalls, retail shops, pharmacies, and multi-branch merchants — manage operations using pirated copies of Sage, QuickBooks, or unbranded Chinese POS software installed on ageing Windows PCs. The consequences are systemic:

- Pirated software receives no vendor updates, no cloud backup, and no technical support. A single hard-drive failure destroys all business records permanently.
- All operations are bound to one physical PC. Owners cannot view sales or stock levels remotely, cannot serve customers during power outages, and cannot operate a second location without a second PC licence.
- No mobile access exists. The business owner cannot monitor revenue, debtors, or stock from a phone.
- Pirated software produces no Uganda Revenue Authority-compliant audit trail. Businesses using it cannot register for EFRIS and are exposed to tax-compliance penalties as URA enforcement expands.
- Exercise books, WhatsApp, and Excel carry the same data-loss risk and add reconciliation labour that a small business cannot afford.

No affordable, mobile-native, compliance-ready alternative exists in the Ugandan mass market. The cost floor for legitimate licensed desktop POS software is prohibitive for micro and small businesses. Maduuka closes this gap.

## 4. Market Opportunity

Uganda's informal and semi-formal retail sector contains an estimated 500,000 to 800,000 active SMB trading accounts. The majority operate in Kampala and peri-urban centres including Entebbe, Jinja, Mbarara, and Gulu. A conservatively addressable segment of 50,000 businesses — those already using any form of digital record-keeping — represents an annual recurring revenue (ARR) potential of UGX 18 billion at the Basic plan price point alone.

The target segment for Phase 1 is defined as:

- Ugandan SMBs with 1 to 15 employees operating in retail, wholesale, pharmacy, or general merchandise.
- Businesses currently using pirated desktop POS software, Excel, or manual ledgers.
- Owners or operators who own an Android smartphone and have access to mobile data or WiFi.

Phase 4 extends the addressable market to all sub-Saharan African countries where mobile-money infrastructure and Android penetration exceed 60% of the adult population, encompassing markets including Kenya, Tanzania, Rwanda, Ghana, Nigeria, and Zambia. Currency-neutral architecture and configurable mobile-money gateway support are built into the platform from Phase 1 to ensure zero re-engineering cost on market entry.

## 5. Design Covenant

The following 6 constraints are *binding* and non-negotiable across all phases and all future development decisions. Any feature, architectural change, or third-party integration that violates any constraint is rejected at design review.

1. **Mobile-first, web-equal.** The Android application is the primary delivery channel. The web interface is a full-featured equal — not a reduced dashboard. No feature shipped on web may be withheld from Android, and vice versa.

2. **Zero mandatory training.** A shopkeeper with no formal software training who can operate WhatsApp must be able to complete a sale, generate a receipt, and read a daily summary without assistance. The system shall not require tutorial completion, onboarding flows, or help documentation to perform core POS and bookkeeping operations.

3. **Offline-first, always.** The system shall record sales, update stock levels, and log expenses when no internet connection is present. All locally recorded data shall synchronise automatically and completely upon reconnection. Data integrity after sync shall be identical to data recorded under continuous connectivity.

4. **Works on the cheapest phone.** The Android application shall run without performance degradation on a device with 2 GB RAM, a quad-core processor at 1.4 GHz, and Android 8.0 (Oreo). The minimum supported device price point is UGX 250,000 at the time of Phase 1 release.

5. **Currency-neutral and Africa-ready.** No currency symbol, locale, or language is hardcoded. The system shall support configuration of currency symbol, decimal separator, and date format per tenant account. All monetary values are stored as integers in the smallest currency unit to prevent floating-point rounding errors.

6. **Compliance built in.** Every transaction recorded on any subscription tier shall produce a record that satisfies Uganda Revenue Authority *Electronic Fiscal Receipting and Invoicing System* (EFRIS) data-field requirements. EFRIS API integration ships as a Phase 3 add-on; EFRIS-ready record structure is mandatory from Phase 1.

## 6. Strategic Goals

The following 5 goals define the strategic intent for Maduuka. Each goal carries a measurable target and a time-bound horizon referenced from the Phase 1 public launch date.

1. **Acquire 1,000 paying accounts within 12 months of Phase 1 launch.** Success is measured by 1,000 unique tenant accounts with at least 1 paid billing cycle completed. Trial accounts and internally provisioned accounts are excluded from this count.

2. **Deliver real-time business health visibility on any Android phone.** Every active account shall be able to view current-day revenue, current stock value, and outstanding debtor balance from the Dashboard module on a ≤ 3-second screen load time at P95 on a 3G connection of 1 Mbps downlink.

3. **Achieve EFRIS compliance coverage for mandated businesses via Phase 3.** By Phase 3 general availability, all tenants subject to URA EFRIS mandates shall be able to submit compliant fiscal receipts via the Maduuka EFRIS integration without exporting data to a third-party tool.

4. **Expand to all target African markets with zero re-engineering cost.** By Phase 4, the platform shall support configuration of currency, language pack, and mobile-money gateway (M-Pesa, Flutterwave, Paystack) per tenant without code changes to the core application.

5. **Displace pirated POS software as the dominant solution in Kampala's downtown business district.** Success is defined as a measurable net-promoter-score (NPS) ≥ 40 among Phase 1 accounts at the 12-month mark, and at least 200 of the 1,000 accounts originating from referrals by existing users in Kampala's central business district.

## 7. Competitive Position

The primary competitor is not a commercial software vendor. It is the ecosystem of pirated Windows POS software — primarily pirated Sage Pastel, pirated QuickBooks Point of Sale, and unbranded Chinese POS applications — that currently holds the dominant market position among Ugandan SMBs.

Pirated software's competitive advantages are: zero upfront cost, familiarity through shared pirated copies, and perceived feature depth. Its structural weaknesses are:

- No cloud backup. A hardware failure is a total, unrecoverable data loss event.
- No mobile access. The business owner is operationally blind when away from the PC.
- No EFRIS compliance. As URA enforcement extends to smaller businesses, this becomes an existential compliance risk.
- No updates or vendor support. Security vulnerabilities and software bugs accumulate without remedy.
- Hardware dependency. The business cannot operate during power cuts, PC failure, or relocation.

Maduuka's competitive strategy is to make every structural weakness of pirated software a product differentiator. The pricing model removes the "free pirated copy" cost advantage at the Basic tier (UGX 30,000/month). The offline-first architecture removes the connectivity dependency. The EFRIS-ready record structure neutralises the compliance risk. No feature comparison with commercial SaaS ERP or accounting platforms is required — Maduuka competes with an illegal, unsupported product, and its bar is to be unambiguously better on every axis that matters to an SMB owner.

Secondary competitors include kiosk-based POS systems marketed by mobile-money agents, basic Android cash-register apps available on the Google Play Store, and informal Excel templates circulated by accounting consultants. None of these provide the combination of offline-first operation, inventory management, bookkeeping, and EFRIS-ready records in a single subscription.

## 8. Product Roadmap Summary

**Phase 1 — Android + Web Foundation (current phase).** Phase 1 delivers the complete Android (Kotlin/Jetpack Compose) and web (PHP 8.3+/Bootstrap 5) platform with 10 core modules: POS, Inventory, Customers, Suppliers, Expenses, Financial Accounts, Sales Reports, HR/Payroll, Dashboard, and Settings. All modules operate offline-first. Subscription tiers Basic (UGX 30,000), Business (UGX 80,000), Pro (UGX 180,000), and Enterprise (custom) are live at launch. Phase 1 targets Uganda exclusively.

**Phase 2 — iOS Parity and Vertical Add-ons.** Phase 2 delivers a feature-complete iOS application and introduces the Restaurant/Bar and Pharmacy industry add-ons. Restaurant/Bar adds table management, kitchen order routing, and beverage stock control. Pharmacy adds batch tracking, expiry-date management, and controlled-substance logging. No Phase 1 module is altered; add-ons extend the platform without replacing core functionality.

**Phase 3 — EFRIS Integration and Advanced Inventory.** Phase 3 delivers the EFRIS API integration module, enabling direct fiscal receipt submission to the Uganda Revenue Authority from within Maduuka. Advanced Inventory adds warehouse-level stock management, transfer orders between branches, and reorder-point automation. The Hotel/Accommodation add-on is also released in Phase 3, adding room booking, housekeeping status, and folio billing.

**Phase 4 — Africa Expansion.** Phase 4 activates the multi-market configuration layer, enabling per-tenant currency, language pack, and mobile-money gateway selection without code changes. M-Pesa (Kenya, Tanzania), Flutterwave (pan-African), and Paystack (Nigeria, Ghana) integrations are certified. Country-specific tax rule packs are introduced as configurable extensions, allowing Maduuka to operate compliantly across jurisdictions without forking the core codebase.

## 9. Success Criteria for Phase 1

Phase 1 is complete when all of the following criteria are verified:

1. The Android application installs and runs without error on a device meeting the minimum specification: 2 GB RAM, quad-core 1.4 GHz, Android 8.0, UGX 250,000 device price point.

2. All 10 core modules are functional on both Android and web with feature parity confirmed by a documented test matrix.

3. The offline-first sync mechanism passes a test scenario in which 50 consecutive sales are recorded with no network connection and all 50 records appear in the cloud database within 60 seconds of reconnection, with zero data loss and zero duplicate records.

4. A shopkeeper with no prior software training completes a simulated sale, issues a receipt, adds a stock item, and reads the daily Dashboard summary within 10 minutes of first opening the application, with no assistance.

5. All 4 subscription tiers are active in the billing system and at least 1 test account has completed a full 30-day billing cycle on each tier.

6. Every transaction record produced by Phase 1 contains all EFRIS-required data fields as specified in the Uganda Revenue Authority EFRIS technical integration guide, verified by a field-by-field audit against the published schema.

7. The Phase 1 production environment achieves < 1% unplanned downtime in the first 30 days post-launch, measured from the load balancer access log.
