# Technical Risks and Debt Assessment

**Project:** Maduuka
**Date:** 2026-04-05
**Source:** `09-governance-compliance/04-risk-assessment/01-risk-assessment.md` → `RiskAssessment_Maduuka.docx`
**Risk register:** 13 risks documented — 3 Critical, 6 High (per RiskAssessment_Maduuka.docx)

---

## Critical Blockers (Must Resolve Before Phase 1 Dev)

| ID | Risk | Category | Impact | Action |
|---|---|---|---|---|
| GAP-001 | MTN MoMo Business API — no sandbox credentials | External Dependency | POS payment feature cannot be built or tested | Peter to contact MTN Uganda Business; register for Business API sandbox |
| GAP-002 / RISK-008 | Data Protection Act 2019 — no legal review | Legal / Compliance | Customer PII, salary data potentially non-compliant. Could block launch. | Engage Uganda-qualified data protection adviser before any PII data model is finalised |

---

## High Priority Risks (Resolve Before Respective Phase)

| ID | Risk | Phase | Category | Action |
|---|---|---|---|---|
| GAP-003 | NDA Uganda drug codes not obtained | Before Phase 2 | External Dependency | Contact NDA Uganda; obtain approved drug list and classification codes |
| GAP-004 | iOS thermal printer compatibility untested | Before Phase 2 | Technical | Test Xprinter, Epson, TP-Link 80mm printers against iOS Core Bluetooth |
| GAP-005 | EFRIS API accreditation not started | Before Phase 3 | External Dependency / Process | Register as URA system-to-system integration partner (multi-week process) |
| GAP-008 | NSSF / PAYE legal verification pending | Before Phase 1 | Legal / Compliance | Verify computation logic against current Income Tax Act and NSSF Act Uganda |

---

## Medium Priority (Resolve Before Phase 2 Build)

| ID | Risk | Action |
|---|---|---|
| GAP-006 | Africa's Talking WhatsApp Business API access unconfirmed | Confirm API tier; WhatsApp Business API requires Meta approval |
| GAP-007 | Hotel channel manager data model deferred | Ensure DB schema accommodates external reservation source field from Phase 1 |
| GAP-009 | Controlled drugs NDA register format unconfirmed | Confirm exact fields, retention period, and NDA format before Phase 2 DB design |
| GAP-010 | Restaurant F&B mixed VAT treatment | Confirm Uganda VAT classification of food vs beverage items for EFRIS submission |

---

## Internal Decisions Deferred

| ID | Decision | Status |
|---|---|---|
| INT-001 | Multi-business group pricing model | Deferred to Phase 2 |
| INT-002 | Academia Pro / Maduuka integration boundary | Phase 4 |
| INT-003 | iOS feature parity timeline | Confirmed: Phase 2, simultaneous with Restaurant/Bar and Pharmacy |
| INT-004 | MLM / distributor network | Permanently excluded — closed |

---

## Architectural Risk Assessment

| Risk Area | Severity | Notes |
|---|---|---|
| Offline-first sync conflicts | High Debt | Two-way sync (Android Room ↔ server) can produce write conflicts. No conflict resolution strategy documented in SRS. Add to UX Spec and SRS NFRs. |
| Offline POS on web (PWA) | High Debt | PWA offline capability for sales transactions requires Service Worker + IndexedDB. Not explicitly specified. |
| Multi-tenant data isolation | Medium | HLD documents multi-tenant model. Verify `tenant_id` scoping is enforced at the ORM/query layer in the PHP backend, not only at the DB schema level. |
| PAYE / NSSF calculation accuracy | High | Payroll errors are legal liability. Computation logic must be verified against URA tax tables before any test plan is signed off. |
| MoMo callback security | High Debt | Inbound webhooks from MTN MoMo must be authenticated (signature/HMAC). Not yet documented in the API spec. |
| Receipt gap detection | Medium | FR-POS receipt gap detection requires sequential receipt numbering per session. Ensure the DB schema enforces gap-free sequences. |

---

## Risk Summary

| Severity | Count |
|---|---|
| Critical Blocker | 2 |
| High | 6 |
| Medium (architectural) | 6 |
| Deferred Internal | 4 |
| **Total tracked** | **18** |
