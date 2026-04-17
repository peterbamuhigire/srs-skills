# Gap Analysis -- Maduuka

*Sourced from spec section 11. Items marked HIGH must be resolved before the indicated phase begins.*

## HIGH Priority -- Resolve Before Phase 1 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-001 | MTN MoMo Business API | Obtain Business API docs and sandbox credentials from MTN Uganda. POS push payment requires Business API, not the standard Merchant API used in Academia Pro/Medic8. | Peter |
| GAP-002 | Data Protection Act 2019 review | Legal review of customer PII, employee salary data, patient prescription data (Phase 2), and guest ID documents (Phase 3) -- Uganda Data Protection and Privacy Act 2019. | Peter |

## HIGH Priority -- Resolve Before Phase 2 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-003 | NDA Uganda drug codes and formulary | Obtain approved drug list and classification codes from NDA Uganda -- required for pharmacy drug reference database. | Peter |
| GAP-004 | iOS thermal printing compatibility | Test Xprinter, Epson, and TP-Link 80mm thermal printers against iOS Core Bluetooth / Raw Print protocol before Phase 2 iOS build. | Dev team |

## HIGH Priority -- Resolve Before Phase 3 Development

| # | Gap | Action | Owner |
|---|---|---|---|
| GAP-005 | EFRIS API accreditation | Register as URA system-to-system integration partner. Multi-week process. Contact: efris@ura.go.ug -- obtain sandbox credentials and complete integration testing. | Peter |

## MEDIUM Priority -- Resolve Before Phase 2 Build

| # | Gap | Action |
|---|---|---|
| GAP-006 | Africa's Talking WhatsApp Business API | Confirm WhatsApp Business API access through Africa's Talking for receipt delivery, customer statements, and refill reminders. |
| GAP-007 | Hotel channel manager integration | Data model must accommodate external reservations (Booking.com, Airbnb) from Phase 1 DB design -- channel manager integration deferred to Phase 4. |
| GAP-008 | Uganda NSSF / PAYE update trigger | Define process for updating tax bands when URA changes rates annually, and how already-processed payrolls are handled. |
| GAP-009 | Controlled drugs register NDA format | Confirm exact fields, retention period, and format required by NDA Uganda for controlled drugs dispensing records. |
| GAP-010 | Restaurant F&B mixed VAT | Confirm Uganda VAT treatment of restaurant and bar items for EFRIS submission logic (some food items VAT-exempt, others 18% standard-rated). |

## INTERNAL Decisions Required

| # | Decision | Options | Status |
|---|---|---|---|
| INT-001 | Multi-business group pricing | One account for 3 separate businesses -- define pricing tier and data model | Deferred to Phase 2 |
| INT-002 | Academia Pro / Maduuka integration | Canteen POS, school shop management -- define integration boundary | Phase 4 |
| INT-003 | Feature parity timeline for iOS | iOS Phase 2, simultaneous with Restaurant/Bar and Pharmacy add-ons | Confirmed |
| INT-004 | MLM / distributor network | PERMANENTLY EXCLUDED -- will never be built | Closed |
