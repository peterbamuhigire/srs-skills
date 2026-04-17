# Non-Functional Requirements — Point of Sale

## 7.1 Performance

**NFR-POS-001** — The terminal shall complete a standard 5-item cash transaction (item scan, payment confirmation, and receipt print trigger) within 3 seconds end-to-end under normal network conditions (≥ 3 Mbps), as measured from the cashier's **Confirm Payment** action to the printed receipt.

**NFR-POS-002** — Item barcode lookup and basket addition shall complete within 300 ms for an item catalogue of ≤ 50,000 items; the local cache shall be used for all offline lookups.

**NFR-POS-003** — The session close Z-report shall generate within 5 seconds for a session containing ≤ 2,000 transactions.

## 7.2 Reliability

**NFR-POS-004** — The POS application shall not lose any confirmed transaction data due to a device reboot or application crash; all confirmed transactions shall be written to the local database before the confirmation response is returned to the cashier UI.

**NFR-POS-005** — The online POS server API shall maintain 99.5% uptime measured monthly; offline mode (FR-POS-052 to FR-POS-061) provides continuity during API unavailability.

## 7.3 Security

**NFR-POS-006** — Each terminal session shall be bound to a single authenticated cashier JWT; the JWT shall expire at the end of the session or after 12 hours of inactivity, whichever comes first.

**NFR-POS-007** — Supervisor override actions (void threshold, discount override, session closure with variance) shall require the supervisor to authenticate using their own credentials, not the cashier's; the supervisor authentication event shall be recorded in the audit log with action type, transaction reference, and UTC timestamp.

**NFR-POS-008** — The local offline database shall be encrypted using AES-256; the encryption key shall be derived from the tenant's terminal secret stored in the Longhorn ERP key management service.

## 7.4 Usability

**NFR-POS-009** — A trained cashier shall be able to complete a 3-item cash transaction without assistance within 60 seconds of session open, as measured during user acceptance testing on a standard Android tablet (minimum: Android 10, 10-inch screen, 4 GB RAM).

**NFR-POS-010** — The POS interface shall be touch-optimised with minimum tappable target size of 44 × 44 dp per Android Material Design guidelines; no transaction-critical action shall require double-tap or long-press.

## 7.5 Compliance

**NFR-POS-011** — All VAT-inclusive receipt amounts shall be computed and displayed to 2 decimal places; rounding shall follow the half-up rule per URA fiscal receipt specifications.

**NFR-POS-012** — EFRIS fiscal receipt submission shall be attempted within 5 seconds of sale confirmation when the terminal is online; offline queued submissions shall be transmitted within 60 seconds of connectivity restoration.
