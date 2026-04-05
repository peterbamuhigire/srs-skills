# Integration and API Status

**Project:** Maduuka
**Date:** 2026-04-05
**Source:** `03-design-documentation/03-api-spec/01-api-spec.md` → `APISpec_Maduuka_Phase1.docx`

---

## API Specification Summary

- Total documented endpoints: **64**
- Sections: 6
- RBAC matrix: documented
- Error codes: documented
- Authentication: JWT + Session (per tech stack)

---

## Integration Checklist

| Check | Status | Notes |
|---|---|---|
| All documented API endpoints exist in spec | Pass | 64 endpoints in APISpec_Maduuka_Phase1.docx |
| Authentication covers all endpoints | Assumed Pass | RBAC matrix documented; verify in actual implementation |
| Response payloads match client schemas | [CONTEXT-GAP: payload schemas] | API spec documents endpoints; JSON payload shapes need cross-check with DB design |
| Pagination implemented where needed | [CONTEXT-GAP: pagination strategy] | Not explicitly documented for list endpoints (products, customers, transactions) |
| Error responses follow consistent format | Pass | Error codes documented in API spec |
| Webhook/callback endpoints | [CONTEXT-GAP: MoMo callback endpoint] | MTN MoMo push payment requires an inbound callback; confirm endpoint is in the spec |
| Offline sync mechanism | Assumed Pass | Offline-first is a Design Covenant constraint; Room (Android) and PWA sync pattern assumed |

---

## External API Integrations

| Integration | Purpose | Status | Blocker |
|---|---|---|---|
| MTN MoMo Business API | POS push payment (FR-POS-012) | Blocked | GAP-001: No sandbox credentials |
| Airtel Money API | POS push payment (FR-POS-013) | Pending | Not flagged as blocked; confirm API access |
| Africa's Talking (SMS) | SMS receipts (FR-POS-020), salary payslips | Pending | GAP-006: WhatsApp Business API access to confirm |
| Africa's Talking (WhatsApp) | Digital receipts, customer portal magic-links | Pending | GAP-006: Confirm WhatsApp Business API tier |
| ML Kit (Android) | Barcode scanning (FR-POS-002) | No external dependency | Google library, bundled |
| Leaflet.js | Customer location map (Web, F-003) | No external dependency | Open source, no API key needed |
| URA EFRIS API | Fiscal receipts (F-015, Phase 3) | Not started | GAP-005: URA accreditation required |
| NDA Uganda | Drug reference database (F-012, Phase 2) | Not started | GAP-003: Drug codes not yet obtained |

---

## Cross-Platform Consistency Check

The Design Covenant mandates web-equal parity: every feature on web must exist on mobile and vice versa.

| Feature | Android | Web | Parity |
|---|---|---|---|
| Barcode scanning (ML Kit) | Yes | No — camera API alternative | Asymmetric by design (acceptable) |
| Thermal receipt printing | Bluetooth | Browser print dialog | Asymmetric by design (acceptable) |
| Offline sales | Room database | PWA / Service Worker | Parity required — confirm PWA offline strategy |
| Bank statement CSV import | Not planned | Yes (F-006) | Asymmetric — confirm this is intentional |
| Custom report builder | Not planned | Yes (F-007) | Asymmetric — confirm this is intentional |
| Dashboard widget (home screen) | Optional Android widget | Web auto-refresh | Asymmetric by design (acceptable) |

---

## Gaps Flagged

- [CONTEXT-GAP: MoMo callback endpoint] — Confirm the MTN MoMo payment callback URL is documented in the API spec. If missing, FR-POS-012 cannot be fully implemented.
- [CONTEXT-GAP: pagination strategy] — Document the pagination model (cursor-based vs offset) for all list endpoints. Required before mobile developers implement infinite scroll or paged lists.
- [CONTEXT-GAP: PWA offline strategy] — The web application's offline-first mechanism is not documented. The Android offline strategy (Room + sync queue) is implied by the tech stack, but the web equivalent needs a specification.
- [CONTEXT-GAP: bank statement CSV import on mobile] — Confirm intent: is this web-only by design, or does Android need a matching import flow?
