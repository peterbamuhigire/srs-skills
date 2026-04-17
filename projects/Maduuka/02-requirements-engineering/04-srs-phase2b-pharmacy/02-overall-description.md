---
title: "SRS Phase 2b — Pharmacy/Drug Store Add-on Module (F-012)"
subtitle: "Section 2: Overall Description"
project: Maduuka
version: 0.1-draft
date: 2026-04-05
status: Draft — Pending Human Review
---

# Section 2: Overall Description of the Pharmacy/Drug Store Module

## 2.1 Product Perspective

The Pharmacy/Drug Store module (F-012) is a bounded add-on within the Maduuka multi-tenant SaaS platform. It is not a standalone product. It depends on the following Phase 1 modules being active and correctly configured for the tenant:

- **F-002 (Inventory and Stock Management):** Pharmacy products are inventory items. Drug-specific attributes (drug class, dispensing unit, controlled classification, storage type) extend the F-002 product record. FEFO batch tracking and expiry management use the F-002 batch/lot tracking mechanism. All stock deductions from dispensing flow through F-002 stock movement records.
- **F-001 (Point of Sale):** The pharmacy POS is a specialised operating mode of F-001. POS session management, void, refund, and payment processing are inherited from F-001.
- **F-006 (Financial Accounts):** Insurance claim payments and cash collections from pharmacy sales post to F-006 payment accounts.
- **F-010 (Settings and Configuration):** SMS gateway (Africa's Talking), notification preferences, and subscription management are configured via F-010.

## 2.2 Prerequisites

The following conditions must be satisfied before F-012 can be activated for a tenant:

1. The tenant's Maduuka subscription must include the Pharmacy add-on (UGX 30,000/month).
2. F-002 must be active and at least one product must be configured with pharmacy attributes.
3. At least one user must be assigned the Pharmacist role.
4. The drug reference database must be loaded by the platform admin prior to the first dispensing event.

## 2.3 User Classes

| User Class | Description | Access Level |
|---|---|---|
| Pharmacist | Licensed pharmacist responsible for dispensing prescription and non-prescription drugs, managing the controlled drugs register, and generating compliance reports. | Full pharmacy module access including controlled drugs register write. |
| Pharmacy Technician | Supports dispensing of non-controlled, non-prescription items. Cannot dispense controlled substances independently. Cannot override FEFO selection or allergy hard blocks without Pharmacist authorisation. | Restricted: no controlled drugs dispensing, no FEFO override, no prescription-only dispensing without linked prescription. |
| Business Owner | Views sales, stock, insurance claim, and compliance reports across all modules. Does not dispense. | Read access to all pharmacy reports and audit logs. Write access to configuration settings. |
| NDA Inspector | Regulatory inspector granted temporary read-only access for compliance audit purposes. Access is time-limited and revoked by the Business Owner. | Read-only: controlled drugs register export, NDA audit log, batch records. No access to patient PII beyond what is required for the register. |

## 2.4 Platform Scope

| Platform | Phase 2 Status |
|---|---|
| Web (browser) | Included — full pharmacy module. File upload for prescription scans. Label printing to A4 PDF or label printer. |
| iOS | Included — Phase 2. Camera-based prescription photo capture. Bluetooth label printer support (subject to GAP-004 iOS printing compatibility resolution). |
| Android | Separate roadmap — not in scope for Phase 2b. |

## 2.5 Regulatory Context

The Pharmacy/Drug Store module operates under the oversight of the National Drug Authority (NDA) of Uganda. The key regulatory instruments governing module behaviour are:

- *Uganda Pharmacy and Drugs Act Cap 280:* Defines prescription-only classification, controlled substance scheduling, and pharmacist obligations.
- *NDA Uganda Drug Registration and Classification:* Assigns NDA drug codes and schedules S1–S4 to registered drug products. [CONTEXT-GAP: GAP-003 — NDA Uganda approved formulary and drug codes not yet obtained. Drug reference database content is pending.]
- *National Drug Policy and Authority Act (Cap 206):* Establishes NDA mandate and inspector access rights.
- *Uganda Data Protection and Privacy Act 2019:* Governs storage and processing of patient PII including name, NIN, medical history, and prescription records.

## 2.6 Assumptions and Dependencies

- Patient NIN entry is voluntary unless required by NDA regulations for controlled drug dispensing. The system shall not block a patient profile creation for absence of NIN.
- Drug interaction checks are performed against the internally loaded drug reference database only. No external clinical API is integrated in Phase 2.
- Refill reminders depend on Africa's Talking SMS/WhatsApp API availability (see GAP-006).
- Cold chain temperature logging is manual data entry. No IoT sensor integration is in scope for Phase 2.
- All monetary values are stored in the tenant's configured currency (UGX default for Uganda deployments), consistent with F-010 configuration.

## 2.7 Constraints Overview

Detailed constraints are specified in Section 5 of this SRS. The following high-level constraints shape module design:

- Maduuka is not a clinical decision support system (CDSS). Drug interaction warnings are category-level informational alerts only, always accompanied by the mandatory disclaimer (Section 1.6).
- The controlled drugs register is append-only. No user role — including platform admin acting on behalf of a tenant — may edit or delete a register entry once written.
- NDA audit log export must be available on demand and must complete within the performance thresholds defined in Section 4.
