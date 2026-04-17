# 5. Design and Operational Constraints

## 5.1 Channel Manager Integration — Deferred (GAP-007)

F-013 Phase 3 does not integrate with any external channel manager or OTA (Online Travel Agency) platform. The following constraints govern the deferral:

- The `reservations` table shall include a `booking_source` column (VARCHAR, NOT NULL, DEFAULT `'walk-in'`) from the initial Phase 3 schema. Permitted Phase 3 values: `walk-in`, `phone`.
- The column definition shall include a comment: `-- Phase 4: extend permitted values to include channel manager codes (e.g., 'booking.com', 'airbnb', 'expedia').`
- No schema migration shall be required when Phase 4 implements channel manager feeds; the column exists and accepts new values without structural change.
- No online booking widget, guest-facing self-service portal, or OTA rate synchronisation is included in Phase 3 scope. All reservations are staff-created.

## 5.2 Reservation Creation — Staff-Initiated Only

All reservations in Phase 3 are created by authenticated staff members (Business Owner, Front Desk Staff). There is no guest-facing booking interface. This constraint is by design; a guest-facing booking widget and channel manager are Phase 4 deliverables.

## 5.3 Maximum Property Size

Phase 3 is designed and performance-tested for properties with up to 200 individual rooms per property instance. The availability check NFR (NFR-HTL-002, 500 ms at P95) is specified for up to 500 rooms to provide headroom, but room status board real-time propagation (NFR-HTL-001) is validated at 200 rooms. Properties onboarded above 200 rooms in Phase 3 accept reduced performance guarantees.

## 5.4 Billing Mode Immutability

Per BR-016, the billing mode (Nightly or Hourly) selected at check-in is immutable after checkout has been processed. The system shall not provide any UI pathway to modify the billing mode on a closed folio. If a billing mode error is identified after checkout, the correction must be handled via a folio adjustment (FR-HTL-071 or FR-HTL-072) or a supplementary invoice, not by modifying the original folio record.

## 5.5 F&B Charge Posting Without F-011

When F-011 (Restaurant/Bar) is not active, F&B charges may be posted to a guest folio manually by Front Desk Staff using FR-HTL-066. The system shall not enforce F-011 as a hard dependency for F&B charge posting; manual posting remains available regardless of F-011 subscription status.

## 5.6 Invoice PDF Generation — Platform Constraint

Per the Maduuka platform standard:

- **iOS** — PDF generation uses PDFKit (on-device, no network round-trip). This applies to folio receipts (FR-HTL-088), corporate invoices (FR-HTL-092), and conference invoices (FR-HTL-102).
- **Web** — PDF generation uses a server-side HTML-to-PDF renderer (e.g., Puppeteer or wkhtmltopdf). The output format and content are identical across platforms.
- **Android** — PDF generation uses the same server-side renderer as Web, with the document returned as a binary stream for download or sharing.

## 5.7 Offline Behaviour

F-013 does not extend the Phase 1 offline sale queue (BR-009) to hotel operations. Room status board real-time updates, reservation creation, and check-in/check-out flows require an active internet connection. If connectivity is lost during a check-out payment, the Phase 1 offline payment queue applies to the payment step only; the folio close event shall be queued and replayed on reconnection.

## 5.8 Data Retention

Guest folio records, including attached ID document images, shall be retained for a minimum of 5 years from the check-out date, in accordance with Uganda Revenue Authority record-keeping requirements and the Uganda Data Protection and Privacy Act 2019 (GAP-002). The Business Owner may not delete individual folio records; full data export and account deletion follow the F-010 data export flow.

## 5.9 Currency and Localisation

F-013 displays all monetary amounts in the currency configured in F-010 Settings. No hardcoded currency symbol is used. The default currency for Maduuka Uganda deployments is Uganda Shillings (UGX). All rate and charge fields accept and store values as integers (smallest currency unit, UGX has no subdivisions in practice); no floating-point arithmetic is used in charge calculations.

## 5.10 Applicable Standards

The following standards govern this SRS and the F-013 implementation:

- IEEE Std 830-1998 — *Recommended Practice for Software Requirements Specifications*
- IEEE Std 1233-1998 — *Guide for Developing System Requirements Specifications*
- IEEE Std 610.12-1990 — *Standard Glossary of Software Engineering Terminology*
- IEEE Std 1012-2016 — *Standard for System, Software, and Hardware Verification and Validation*
- Uganda Data Protection and Privacy Act 2019 (GAP-002) — governs guest PII and ID document storage

---

## Human Review Gate

*This document is a first-pass draft. The consultant must review and acknowledge the following before proceeding to downstream skills.*

**Open [CONTEXT-GAP] items requiring consultant input:**

- **[CONTEXT-GAP: GAP-007]** — FR-HTL-026 and FR-HTL-109 reference future `booking_source` values from channel manager integration. Confirm the exact Phase 4 source code strings to embed as placeholder documentation now (e.g., `booking.com`, `airbnb`, `expedia`, or a generic `ota`).
- **[CONTEXT-GAP: Late Checkout Fee Structure]** — FR-HTL-082 states the late checkout fee amount and grace period are configurable per property. Confirm whether a recommended default (e.g., 50% of nightly rate after 1-hour grace) should be pre-populated at property setup, or left blank for the owner to configure.
- **[CONTEXT-GAP: No-Show Policy]** — FR-HTL-043 states the no-show policy governs deposit handling. Confirm whether Maduuka ships a default no-show policy template or requires the Business Owner to configure from scratch.
- **[CONTEXT-GAP: Group Booking Maximum]** — No maximum room count per group booking is defined. Confirm whether a limit (e.g., 50 rooms per group) is required or whether the limit is the property's total room count.
- **[CONTEXT-GAP: Housekeeping Assignment]** — FR-HTL-025 references in-app notification to housekeeping staff. Confirm whether push notifications (FCM/APNs) are available in Phase 3 for Housekeeping Staff, or whether the notification is limited to in-app polling.

**No [V&V-FAIL] tags were raised.** All FR identifiers are unique within FR-HTL-001 to FR-HTL-112. All formulas include defined variables. All stimulus-response pairs are deterministic.

**[GLOSSARY-GAP: OTA]** — The acronym OTA (Online Travel Agency) is used in this SRS. Add to `_context/glossary.md`.
**[GLOSSARY-GAP: PMS]** — The acronym PMS (Property Management System) is used. Add to `_context/glossary.md`.
**[GLOSSARY-GAP: RevPAR]** — Defined in Section 1.4 of this SRS. Confirm entry exists or is added to `_context/glossary.md`.
**[GLOSSARY-GAP: ADR]** — Defined in Section 1.4 of this SRS. Confirm entry exists or is added to `_context/glossary.md`.
