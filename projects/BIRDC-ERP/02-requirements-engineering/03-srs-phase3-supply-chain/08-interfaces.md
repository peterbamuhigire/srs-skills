# 7. External Interface Requirements

## 7.1 Internal Module Interfaces

| Interface | Source Module | Target Module | Data Flow |
|---|---|---|---|
| Stock Receipt | F-009 (GRN finalisation) | F-003 (Inventory) | GRN triggers stock balance increment in tbl_stock_balance |
| Raw Material Inventory | F-009 Stage 4 | F-011 (Manufacturing) | Cooperative batch stock available as raw material input for production orders |
| Accounts Payable | F-009 (matched vendor invoice) | F-007 (AP) | Matched invoices appear in AP payment run |
| Farmer Payment | F-009 Stage 5 / F-010 payment | F-007 (AP) | Cooperative Payable balance updated; bulk payment debits bank GL account |
| GL Auto-Post | F-009 Stage 5 and all AP postings | F-005 (GL) | All procurement transactions auto-post to GL via the posting engine from Phase 2 |
| Input Loan Deductions | F-010 (loan records) | F-009 (payment calculation) | Outstanding loan instalments fed into farmer payment deduction calculation |
| PPDA Register | F-009 (all procurement docs) | F-016 (Administration) | Every procurement document status change updates the PPDA compliance register |

## 7.2 Mobile Money API Integration

### MTN MoMo Business API

**INT-001** — The system shall integrate with the MTN MoMo Business API for bulk farmer payment disbursements using the Collections and Disbursements endpoints. The API base URL, merchant wallet ID, subscription key, and API user credentials shall be stored in the `.env` file and configurable via the system administration UI (DC-002). [CONTEXT-GAP: GAP-002]

**INT-002** — Each bulk payment request to MTN MoMo shall include: the recipient's MSISDN (mobile number), amount (UGX), currency code "UGX", external ID (the farmer contribution record ID for traceability), and a payer message with the payment narration.

**INT-003** — The system shall poll the MTN MoMo transaction status endpoint for each submitted payment and update the farmer's payment record status on confirmation or failure; polling shall occur at 30-second intervals for up to 5 minutes before declaring a timeout; timed-out payments shall be marked "Status Unknown — Manual Check Required".

### Airtel Money API

**INT-004** — The system shall integrate with the Airtel Money API for farmer payment disbursements to Airtel number holders, following equivalent integration patterns to INT-001 through INT-003. [CONTEXT-GAP: GAP-003]

### SMS Gateway

**INT-005** — The system shall integrate with a configurable SMS gateway (gateway provider, API key, and sender ID configurable in admin UI) to deliver farmer SMS notifications (FR-FAR-038 through FR-FAR-041, FR-FAR-049); the SMS gateway provider shall be confirmed by BIRDC before development of the SMS module.

## 7.3 NIRA NIN Verification

**INT-006** — When online, the system shall submit a NIN verification request to the NIRA API (if a data sharing agreement is in place) to confirm the NIN and return the registered name; the API credentials and endpoint shall be configurable in the admin UI; if the NIRA API is unavailable, the NIN shall be recorded unverified per FR-FAR-002. [CONTEXT-GAP: GAP-004 — NIRA data sharing agreement required]

## 7.4 Farmer Delivery App — Server API

**INT-007** — The Farmer Delivery App shall communicate with the BIRDC ERP server via a REST API over HTTPS. All endpoints shall require a valid JWT Bearer token. The API shall support the following resource groups:

- `POST /api/v1/farmers` — create new farmer record
- `GET /api/v1/farmers?cooperative_id={id}` — get cached farmer list for offline sync
- `POST /api/v1/batches` — create new batch receipt
- `POST /api/v1/batches/{id}/contributions` — submit individual farmer contribution
- `POST /api/v1/sync` — bulk sync endpoint for offline records
- `GET /api/v1/bpo/active` — get active Bulk Purchase Orders and pricing schedules

**INT-008** — The sync endpoint (`POST /api/v1/sync`) shall accept a JSON payload containing arrays of offline farmer registrations and delivery records; the server shall process each record, return a response array with permanent IDs for successfully created records and error details for rejected records; the app shall update local IDs accordingly.

## 7.5 Hardware Interfaces

| Hardware | Interface Method | Requirement |
|---|---|---|
| Bluetooth 80mm thermal printer | Android Bluetooth ESC/POS | FR-MOB-015, FR-MOB-016 |
| Bluetooth digital weighing scale | Android Bluetooth (scale-specific SDK) | FR-MOB-011; [CONTEXT-GAP: GAP-011] |
| Device GPS | Android Location API (FusedLocationProviderClient) | FR-MOB-007, FR-FAR-001 |
| Device camera | Android CameraX API | FR-FAR-003, FR-MOB-007 |
| ML Kit barcode scanner | Google ML Kit Barcode Scanning | FR-MOB-009 |
