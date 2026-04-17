---
title: "Risk Assessment — Maduuka Phase 1"
author: "Peter Bamuhigire / Chwezi Core Systems"
date: "2026-04-05"
version: "1.0"
status: "Draft"
---

# Risk Assessment — Maduuka Phase 1

## 1. Introduction

### 1.1 Purpose

This document identifies, assesses, and defines mitigation strategies for risks that threaten the successful delivery and operation of Maduuka Phase 1. It serves as the authoritative risk register for the Phase 1 build cycle (Android + Web, 10 core modules) and is maintained throughout the project lifecycle in accordance with IEEE 1058.

### 1.2 Scope

This assessment covers:

- Technical integration risks (Mobile Money APIs, third-party services, device compatibility)
- Software architecture risks (multi-tenancy, offline sync, data integrity)
- Legal and compliance risks (Uganda Data Protection and Privacy Act 2019, EFRIS mandate)
- People and resource risks (team bandwidth, knowledge concentration)
- Market and business risks (competitive environment, connectivity conditions)

Risks pertaining exclusively to Phase 2 or Phase 3 modules are noted where they require Phase 1 design decisions but are not assessed as active Phase 1 delivery risks.

### 1.3 Methodology

Risk exposure is calculated using the probability × impact matrix defined in Section 2, aligned with IEEE 1058 risk management principles. Each risk is assigned:

1. A unique **RISK-ID** for traceability.
2. A **Category** drawn from five classes: Technical, Compliance, People, Market, or Architecture.
3. A **Probability** score (1–5) and an **Impact** score (1–5).
4. A **Risk Exposure** value (Probability × Impact) mapped to a qualitative **Rating**.
5. A **Mitigation** action (preventive, to be executed during development).
6. A **Contingency** action (reactive, executed if mitigation fails).
7. An **Owner** responsible for tracking and resolving the risk.

### 1.4 Definitions

| Term | Definition |
|---|---|
| Risk | An uncertain event or condition that, if it occurs, has a positive or negative effect on project objectives. *(IEEE 1058)* |
| Probability | The likelihood that a risk event will occur, expressed on a 1–5 ordinal scale defined in Section 2.1. |
| Impact | The consequence severity if the risk event occurs, expressed on a 1–5 ordinal scale defined in Section 2.2. |
| Risk Exposure | The product of Probability × Impact; a composite measure of overall risk significance. |
| Mitigation | A proactive action taken before a risk event occurs to reduce probability, impact, or both. |
| Contingency | A reactive action plan activated after a risk event occurs to limit damage to project objectives. |
| Risk Owner | The named individual accountable for monitoring the risk, executing mitigation, and activating contingency if required. |

---

## 2. Risk Rating Scale

### 2.1 Probability Scale

| Score | Label | Probability Range |
|---|---|---|
| 1 | Rare | < 10% |
| 2 | Unlikely | 10–30% |
| 3 | Possible | 31–50% |
| 4 | Likely | 51–70% |
| 5 | Almost Certain | > 70% |

### 2.2 Impact Scale

| Score | Label | Description |
|---|---|---|
| 1 | Negligible | No measurable effect on delivery or quality. |
| 2 | Minor | Slight delay (< 1 sprint) or minor quality reduction; self-recoverable. |
| 3 | Moderate | Significant feature scope reduction or timeline slip of 1–2 sprints. |
| 4 | Major | Phase 1 delivery date at risk; core module functionality compromised. |
| 5 | Critical | Product unusable, legal or compliance breach, or data exposure event. |

### 2.3 Risk Exposure and Rating Bands

**Risk Exposure = Probability × Impact**

| Exposure Range | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–14 | High |
| 15–25 | Critical |

---

## 3. Risk Register

The full risk register is presented below. Risks are ordered by exposure score (descending). All 13 risks are derived from the gap analysis (`_context/gap-analysis.md`), business rules (`_context/business_rules.md`), and project feature scope (`_context/features.md`).

| Risk ID | Category | Description | P | I | Exposure | Rating | Mitigation | Contingency | Owner |
|---|---|---|---|---|---|---|---|---|---|
| **RISK-006** | Architecture | Multi-tenant data isolation breach — `franchise_id` scoping must be applied on every database query (BR-001). A single omitted `WHERE` clause exposes cross-tenant data. | 2 | 5 | 10 | High | Implement `franchise_id` injection at the ORM/service layer, not per individual query. Require automated integration tests asserting HTTP 403 on every API endpoint when accessed with a mismatched `franchise_id`. Execute these tests in CI on every pull request. | Activate incident response plan immediately. Notify affected tenants. File Uganda DPA 2019 breach notification with the Personal Data Protection Office within 72 hours of confirmed exposure. | Peter |
| **RISK-008** | Compliance | Uganda Data Protection and Privacy Act 2019 — Phase 1 stores customer PII (names, phone numbers, credit balances). Phase 2/3 collect patient records and guest ID documents. Legal obligations under DPA 2019 apply from Phase 1 launch (GAP-002). | 3 | 5 | 15 | Critical | Retain a Uganda data privacy legal advisor before Phase 1 launch. Implement data minimisation, purpose limitation, consent capture, and right-to-erasure features in Phase 1 per DPA 2019 Chapter 3. Complete legal review before go-live. | Delay Phase 1 general availability until legal review is complete. Delay Phase 2/3 modules until all sensitive data handling requirements are confirmed by the retained advisor. | Peter |
| **RISK-010** | People | Small team bandwidth — 2–5 people must deliver Android app, web frontend, backend API, and QA across 10 modules. Scope overrun is likely without strict discipline. | 4 | 4 | 16 | Critical | Enforce a formal Phase 1 feature freeze at development kickoff. No gold-plating. Conduct weekly sprint retrospectives with a scope creep check as a standing agenda item. Track all 10 module completion percentages against a shared burn-down. | If timeline is at risk by the midpoint sprint review, defer HR/Payroll (F-008) or Advanced Reports (F-007 custom builder) to Phase 1.1 patch, reducing Phase 1 to 8 core modules. | Peter |
| **RISK-001** | Technical | MTN MoMo Business API sandbox access not yet obtained (GAP-001). POS push payment (F-001) requires the Business API; the standard Merchant API used in Academia Pro and Medic8 is insufficient. Testing is blocked without sandbox credentials. | 3 | 4 | 12 | High | Apply for MTN MoMo Business API sandbox credentials from MTN Uganda immediately (before development of F-001 payment processing begins). Implement the POS payment flow with a fallback toggle: a "MoMo received" manual confirmation that records the payment without API verification. | If sandbox credentials are not available by the Phase 1 development freeze date, ship Phase 1 without automated push payment. Deliver automated push payment as a Phase 1.1 patch once sandbox access and integration testing are complete. | Peter |
| **RISK-005** | Architecture | Offline sync conflict resolution undefined (GAP-005) — when the same product is sold offline on 2 or more devices simultaneously, stock levels will conflict on sync. BR-009 requires offline sales to always be recorded and synced in chronological order. | 3 | 4 | 12 | High | Define and document the conflict resolution protocol in the SRS before development begins. Recommended protocol: last-write-wins on stock decrement with an immutable audit log entry for each conflicting transaction; flag to manager dashboard when stock goes negative after sync. | If conflict resolution cannot be fully automated, require mandatory manual reconciliation review from the manager before the sync is marked complete when a negative stock conflict is detected. | Peter |
| **RISK-007** | Compliance | Payroll statutory deduction accuracy (GAP-008) — NSSF (employer 10%, employee 5%), PAYE per Income Tax Act, and LST computations require verified interpretation of Uganda Revenue Authority rules. Incorrect payslips create URA audit exposure and staff trust damage. | 3 | 4 | 12 | High | Engage URA PAYE guidelines, NSSF Act Cap 222, and LST regulations as primary sources. Have a qualified Uganda HR/payroll professional review and sign off on 10 computed payslip samples covering all salary bands before Phase 1 release of F-008. | Add a mandatory disclaimer on every generated payslip: "This payslip is generated by software using publicly available URA and NSSF rates. Verify computations with a certified HR professional before statutory filing." Lock the payroll module until the professional review is complete. | Peter |
| **RISK-009** | Compliance | EFRIS scope creep — EFRIS integration is scoped to Phase 3 (F-015), but URA announced mandatory EFRIS expansion from July 2025. Clients in the mandatory category may demand EFRIS before Phase 3 is built (GAP-005). | 4 | 3 | 12 | High | Reserve EFRIS column placeholders (`efris_fdn`, `efris_status`, `efris_verification_url`) in the Phase 1 sales table schema. Design the invoice generation API to accept EFRIS fields as optional extensions without breaking changes. This ensures Phase 3 EFRIS integration requires no schema migration on the production database. | If market demand from mandatory EFRIS clients materialises before Phase 3, accelerate the EFRIS module as a standalone Phase 2.5 delivery, using the pre-reserved schema columns. | Peter |
| **RISK-011** | People | Single point of knowledge failure — if the lead developer is unavailable, institutional knowledge of business logic, architecture decisions, and integration details is not transferable without documentation. | 2 | 4 | 8 | Medium | Maintain live documentation throughout development: SRS, High-Level Design, Database Design, API Specification, and Architectural Decision Records (ADRs) for all key technical choices. Add inline code comments on all business rule implementations (referencing BR-001 through BR-016). | If the lead developer is unavailable for > 2 weeks, engage a contract developer using the documentation package as the onboarding contract. The documentation package must be sufficient to onboard within 3 working days. | Peter |
| **RISK-002** | Technical | Airtel Money merchant API availability in Uganda is unconfirmed. Multi-payment support (F-001) requires both MTN MoMo and Airtel Money channels. | 3 | 3 | 9 | Medium | Contact Airtel Uganda Business team to confirm merchant API availability, obtain API documentation, and apply for sandbox access in parallel with MTN MoMo application. | Apply the same fallback implemented for RISK-001: a manual "Airtel Money received" confirmation toggle that records the payment without API verification. Deliver automated Airtel Money push as a Phase 1.1 patch. | Peter |
| **RISK-012** | Market | Competing free and pirated POS software — Maduuka's target market currently uses pirated Windows POS with no ongoing cost. Ugandan SMEs have demonstrated low willingness to pay for software subscriptions. | 4 | 3 | 12 | High | Position Basic tier at UGX 30,000/month, competitive with the total cost of ownership of pirated alternatives (hardware maintenance, data loss, no cloud backup, no EFRIS compliance). Offer a 14-day free trial with full feature access. Emphasise EFRIS compliance as a non-negotiable legal driver for all taxable businesses from July 2025 onward. | Introduce a freemium tier (unlimited transactions, single device, no advanced reports) if paid conversion rate falls below 10% of registered trial accounts at the 90-day post-launch mark. | Peter |
| **RISK-013** | Market | Unreliable internet connectivity — Ugandan SMEs in peri-urban and rural areas operate on intermittent 3G/4G. POS blocking on connectivity loss is commercially unacceptable. | 5 | 3 | 15 | Critical | Implement offline-first architecture from Phase 1 day 1: Room Database for local persistence on Android, WorkManager sync queue for background upload. BR-009 mandates that the POS never prevents a sale due to connectivity loss. Sync all pending transactions within 30 seconds of connectivity restoration (quality_standards.md threshold). | Enable SMS-based data entry as an ultra-low-bandwidth fallback for critical operations (stock counts, cash float entries) if WorkManager sync queue exceeds 100 pending transactions for > 4 hours. | Peter |
| **RISK-003** | Technical | Africa's Talking SMS and WhatsApp delivery reliability in low-connectivity areas of Uganda is unverified (GAP-006). Receipt delivery and customer statements (F-001, F-003) depend on this channel. | 2 | 3 | 6 | Medium | Load-test Africa's Talking SMS and WhatsApp delivery in representative Ugandan network conditions (MTN Uganda, Airtel Uganda on 3G) before Phase 1 launch. Implement retry logic with exponential backoff (initial delay: 30 seconds; maximum retries: 5; maximum delay: 30 minutes). Monitor delivery rate: target ≥ 95% delivery within 5 minutes. | If delivery rate falls below 95% in testing, activate offline-only receipt printing (80mm thermal Bluetooth) as the primary receipt method and demote digital receipt to a secondary option. | Peter |
| **RISK-004** | Technical | ML Kit barcode scan performance on low-end Android devices (target market: UGX 150,000–250,000 handsets) is untested (GAP-004). Slow or unreliable scanning creates cashier friction at POS. | 3 | 3 | 9 | Medium | Test ML Kit barcode scanning performance on 3 minimum-spec target devices before F-001 development is finalised: Tecno Spark 9, Itel A57, and Samsung Galaxy A05. Pass criterion: scan-to-cart-add latency ≤ 1 second (quality_standards.md threshold) for EAN-13 and QR codes in normal retail lighting. A manual barcode entry field is always present as a fallback. | If ML Kit scan latency exceeds 1 second on any of the 3 target devices, integrate a USB/Bluetooth HID barcode scanner (physical) as a supported peripheral. Document supported scanner models in the user guide. | Peter |

---

## 4. Risk Heat Map

The heat map below positions each risk by Probability (rows, 1 = bottom, 5 = top) against Impact (columns, 1 = left, 5 = right). Cell contents list the Risk IDs occupying that cell.

| Probability \ Impact | I=1 (Negligible) | I=2 (Minor) | I=3 (Moderate) | I=4 (Major) | I=5 (Critical) |
|---|---|---|---|---|---|
| **P=5 (Almost Certain)** | — | — | RISK-013 | — | — |
| **P=4 (Likely)** | — | — | RISK-009, RISK-012 | RISK-010 | — |
| **P=3 (Possible)** | — | — | RISK-002, RISK-003, RISK-004 | RISK-001, RISK-005, RISK-007 | RISK-008 |
| **P=2 (Unlikely)** | — | — | — | RISK-006, RISK-011 | — |
| **P=1 (Rare)** | — | — | — | — | — |

**Colour zone reference:**

- Cells where Exposure ≥ 15 = Critical zone: RISK-008 (P3×I5=15), RISK-010 (P4×I4=16), RISK-013 (P5×I3=15)
- Cells where Exposure 10–14 = High zone: RISK-001, RISK-005, RISK-006, RISK-007, RISK-009, RISK-012
- Cells where Exposure 5–9 = Medium zone: RISK-002, RISK-003, RISK-004, RISK-011
- No risks currently occupy the Low zone (Exposure 1–4)

---

## 5. Top Risks Summary

The 5 risks with the highest exposure score are listed below, ranked by exposure (descending). Where exposure scores are equal, the risk with the higher impact score ranks first.

| Rank | Risk ID | Exposure | Rating | Description | One-Line Mitigation |
|---|---|---|---|---|---|
| 1 | **RISK-010** | 16 | Critical | Small team bandwidth across 10 modules | Strict feature freeze + weekly scope reviews; defer F-008 or F-007 custom builder if timeline slips. |
| 2 | **RISK-008** | 15 | Critical | Uganda DPA 2019 legal compliance | Retain data privacy legal advisor; implement DPA 2019 consent and erasure features before launch. |
| 3 | **RISK-013** | 15 | Critical | Unreliable internet in target markets | Offline-first architecture (Room DB + WorkManager) with 30-second sync-on-reconnect guarantee. |
| 4 | **RISK-001** | 12 | High | MTN MoMo Business API sandbox not obtained | Apply for sandbox access immediately; implement manual confirmation fallback for Phase 1. |
| 5 | **RISK-012** | 12 | High | Competition from free/pirated POS software | UGX 30,000/month Basic tier + 14-day trial + EFRIS compliance as legal differentiator. |

---

## 6. Risk Monitoring Plan

### 6.1 Review Cadence

- The full risk register is reviewed at every sprint retrospective (bi-weekly).
- All Critical and High rated risks (Exposure ≥ 10) are reviewed weekly by the product owner.
- Any risk whose exposure rating changes during a review period is re-scored and the register is updated before the next sprint begins.

### 6.2 New Risk Identification

- Any team member who identifies a new risk during development logs it immediately in this register with: description, initial probability/impact estimate, proposed mitigation, and an owner.
- New risks with Exposure ≥ 10 are escalated to the product owner within 24 hours of identification.

### 6.3 Risk Closure

- A risk is marked **Closed** when: the mitigation action is fully implemented and the conditions that could trigger the risk event no longer apply (e.g., MTN MoMo sandbox obtained and integration tested → RISK-001 closed).
- Closed risks are retained in the register with their closure date for audit trail purposes.

### 6.4 Owners and Accountability

- **Peter Bamuhigire** (Product Owner, Chwezi Core Systems) is the default owner for all risks in this register unless explicitly delegated.
- Owner reassignment is recorded in the register with the effective date.
- The owner is accountable for: monitoring the risk indicator, executing the mitigation on schedule, and activating the contingency if the risk event occurs.

### 6.5 Escalation Thresholds

| Condition | Action |
|---|---|
| Any Critical risk (Exposure ≥ 15) mitigation action not started within 1 sprint of identification | Product owner convenes immediate resolution session; no new feature development begins until the mitigation is initiated. |
| Any risk event (risk materialises) with Impact ≥ 4 | Contingency plan activated within 24 hours; sprint plan revised; stakeholders notified. |
| Uganda DPA 2019 breach confirmed (RISK-006 or RISK-008 materialises) | Incident response activated immediately; breach notification filed with the Personal Data Protection Office within 72 hours as required by DPA 2019 Section 25. |
