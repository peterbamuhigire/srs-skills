---
title: "Test Cases — F-001 POS, F-002 Inventory, F-003 Customer Management"
document-id: "MADUUKA-TC-001"
version: "1.0"
date: "2026-04-05"
standard: "IEEE Std 829-2008"
---

# Test Cases: F-001 Point of Sale, F-002 Inventory, F-003 Customer Management

**Document ID:** MADUUKA-TC-001
**Version:** 1.0
**Date:** 2026-04-05
**Parent Plan:** MADUUKA-TP-001

---

## Module F-001: Point of Sale (POS)

---

### FR-POS-001 — Product Search

---

**TC-POS-001**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-001 |
| FR Reference | FR-POS-001 |
| Title | Verify product search returns results within 500 ms of last keystroke |
| Preconditions | 1. A POS session is open with an opening float of UGX 50,000. 2. The product catalogue contains at least 100 products including one named "Coca-Cola 500ml" with SKU "SKU-001". 3. The tester is authenticated as a Cashier role user. |
| Test Steps | 1. Open the POS screen. 2. Tap the search field. 3. Type "Coca" and stop typing. 4. Start a timer at the last keystroke. 5. Observe the search results list. |
| Expected Result | Within 500 ms of the last keystroke, the results list displays at least one entry showing "Coca-Cola 500ml", its current price, and its stock availability. No spinner remains after 500 ms. |
| Pass Criteria | Results list is populated with a matching product entry in ≤ 500 ms as measured from the final keystroke event. |
| Priority | Critical |

---

**TC-POS-002**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-002 |
| FR Reference | FR-POS-001 |
| Title | Verify search by SKU returns correct product |
| Preconditions | 1. A POS session is open. 2. Product "Coca-Cola 500ml" has SKU "SKU-001" in the catalogue. 3. Tester is authenticated as Cashier. |
| Test Steps | 1. Open the POS screen. 2. Tap the search field. 3. Type "SKU-001". 4. Observe the results list. |
| Expected Result | The results list displays exactly "Coca-Cola 500ml" with its price and stock level. No other products are shown. |
| Pass Criteria | 1 result displayed; product name, price, and stock availability match the seeded product record. |
| Priority | High |

---

**TC-POS-003**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-003 |
| FR Reference | FR-POS-001 |
| Title | Verify search by partial barcode returns matching product |
| Preconditions | 1. A POS session is open. 2. Product "Fanta Orange 300ml" has EAN-13 barcode "5900300123457". 3. Tester is authenticated as Cashier. |
| Test Steps | 1. Open the POS screen. 2. Tap the search field. 3. Type "5900300". 4. Observe the results list. |
| Expected Result | The results list includes "Fanta Orange 300ml" within 500 ms of the last keystroke. The product name, price, and stock availability are displayed. |
| Pass Criteria | Matching product appears in results in ≤ 500 ms. |
| Priority | Medium |

---

### FR-POS-002 — Barcode Scan (Android)

---

**TC-POS-004**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-004 |
| FR Reference | FR-POS-002 |
| Title | Verify ML Kit barcode scan adds product to cart within 1 second without confirmation tap |
| Preconditions | 1. A POS session is open on Android. 2. Product "Fanta Orange 300ml" has EAN-13 barcode "5900300123457" in the catalogue. 3. A physical EAN-13 barcode label for "5900300123457" is available. 4. Tester is authenticated as Cashier on Android device (API ≥ 26, camera permission granted). |
| Test Steps | 1. Open the POS screen on Android. 2. Tap the camera icon in the search field. 3. The full-screen camera view opens. 4. Point the camera at the EAN-13 barcode. 5. Note the time of barcode decode. 6. Observe the cart. |
| Expected Result | Within 1 second of the barcode decode event, the cart shows "Fanta Orange 300ml" as a line item with quantity 1 and correct unit price. No confirmation tap is required. The camera view closes automatically. |
| Pass Criteria | Product line item appears in cart in ≤ 1 second from decode event, quantity = 1, no confirmation dialog presented. |
| Priority | Critical |

---

**TC-POS-005**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-005 |
| FR Reference | FR-POS-002 |
| Title | Verify scanning an unregistered barcode shows an informative error |
| Preconditions | 1. A POS session is open on Android. 2. Barcode "9999999999999" does not exist in the catalogue. 3. Camera permission is granted. |
| Test Steps | 1. Open the POS screen on Android. 2. Tap the camera icon. 3. Scan a barcode with value "9999999999999". 4. Observe the screen. |
| Expected Result | The system displays the message "Product not found. Check your catalogue." The cart is unchanged. No crash occurs. |
| Pass Criteria | Error message displayed; cart unchanged; application does not crash. |
| Priority | High |

---

### FR-POS-009 / FR-POS-010 — Hold and Resume Cart

---

**TC-POS-006**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-006 |
| FR Reference | FR-POS-009 |
| Title | Verify Hold Sale suspends the active cart and assigns a hold reference number |
| Preconditions | 1. A POS session is open. 2. The active cart contains 2 items: "Sugar 1kg" × 2 at UGX 5,000 each, and "Cooking Oil 1L" × 1 at UGX 12,000. 3. A 15% per-item discount has been applied to "Sugar 1kg". 4. Tester is authenticated as Cashier. |
| Test Steps | 1. On the active cart screen, tap "Hold Sale". 2. Observe the screen. 3. Observe the cart state. |
| Expected Result | The system assigns hold reference "HOLD-001" (or the next sequential hold reference). The active cart is cleared, showing an empty cart ready for a new transaction. The hold reference number is visible in the held carts list. |
| Pass Criteria | Active cart is empty after hold; held cart list shows 1 entry with the assigned hold reference; hold reference is a non-empty string. |
| Priority | Critical |

---

**TC-POS-007**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-007 |
| FR Reference | FR-POS-010 |
| Title | Verify resuming a held cart restores all items, quantities, prices, and discounts exactly |
| Preconditions | 1. A POS session is open. 2. One held cart exists (from TC-POS-006) with hold reference "HOLD-001" containing: "Sugar 1kg" × 2 at UGX 5,000 each with 15% discount, and "Cooking Oil 1L" × 1 at UGX 12,000. 3. The active cart is currently empty. |
| Test Steps | 1. Open the held carts list. 2. Select hold reference "HOLD-001". 3. Observe the restored cart. |
| Expected Result | The active cart displays: "Sugar 1kg" × 2 at UGX 5,000 each with a 15% discount applied (line total = UGX 8,500), and "Cooking Oil 1L" × 1 at UGX 12,000 (line total = UGX 12,000). Cart grand total = UGX 20,500. |
| Pass Criteria | All 2 items present; quantities match; discount on "Sugar 1kg" is 15%; grand total = UGX 20,500. |
| Priority | Critical |

---

**TC-POS-008**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-008 |
| FR Reference | FR-POS-009 |
| Title | Verify held cart persists across Android app restart |
| Preconditions | 1. A POS session is open on Android. 2. One held cart exists with hold reference "HOLD-001" containing 1 item: "Bread 400g" × 3 at UGX 3,500 each. 3. The active cart is empty. |
| Test Steps | 1. Force-close the Android application. 2. Relaunch the application. 3. Authenticate as the same Cashier user. 4. Open the POS screen. 5. Open the held carts list. |
| Expected Result | Hold reference "HOLD-001" appears in the held carts list with "Bread 400g" × 3. The cart is fully restorable after the restart. |
| Pass Criteria | Held cart survives app restart; all 3 items and quantities match the pre-restart state. |
| Priority | Critical |

---

### FR-POS-012 — MTN MoMo Push Payment

---

**TC-POS-009** `[BLOCKED: GAP-001]`

| Field | Content |
|---|---|
| Test Case ID | TC-POS-009 |
| FR Reference | FR-POS-012 |
| Title | Verify successful MTN MoMo push payment completes sale and generates receipt |
| Preconditions | 1. MTN MoMo Business API sandbox credentials are configured (GAP-001 resolved). 2. A POS session is open. 3. The active cart total is UGX 25,000. 4. A sandbox MTN MoMo test phone number is available that simulates immediate payment approval. 5. Tester is authenticated as Cashier. |
| Test Steps | 1. On the payment screen, select "MTN MoMo" as the payment method. 2. Enter the sandbox test phone number. 3. Tap "Send Payment Request". 4. Observe the pending indicator. 5. Simulate the sandbox approval event. 6. Observe the result. |
| Expected Result | 1. A pending indicator is displayed immediately after "Send Payment Request" is tapped. 2. After the sandbox approval event, the pending indicator clears and the system navigates to the receipt screen. 3. The receipt displays: payment method "MTN MoMo", amount UGX 25,000, and the transaction reference returned by the sandbox API. 4. Stock levels for physical items in the cart are decremented. |
| Pass Criteria | Receipt generated with payment method = "MTN MoMo" and amount = UGX 25,000; sale record created in the database; stock decremented. |
| Priority | Critical |

---

**TC-POS-010** `[BLOCKED: GAP-001]`

| Field | Content |
|---|---|
| Test Case ID | TC-POS-010 |
| FR Reference | FR-POS-012 |
| Title | Verify MTN MoMo push payment failure displays failure reason and allows retry |
| Preconditions | 1. MTN MoMo Business API sandbox credentials are configured. 2. A POS session is open. 3. The active cart total is UGX 15,000. 4. A sandbox phone number is configured to simulate payment failure ("Insufficient funds" response). |
| Test Steps | 1. On the payment screen, select "MTN MoMo". 2. Enter the sandbox failure phone number. 3. Tap "Send Payment Request". 4. Simulate the sandbox failure response. 5. Observe the screen. |
| Expected Result | The pending indicator clears. The system displays the message "Payment failed: Insufficient funds." (exact text from the API failure reason field). Two buttons are visible: "Retry" and "Switch Payment Method". No receipt is generated. No sale record is created. Stock levels are unchanged. |
| Pass Criteria | Failure reason text displayed; no receipt created; no sale record in database; stock unchanged. |
| Priority | Critical |

---

**TC-POS-011** `[BLOCKED: GAP-001]`

| Field | Content |
|---|---|
| Test Case ID | TC-POS-011 |
| FR Reference | FR-POS-012 |
| Title | Verify MTN MoMo push payment timeout displays timeout message and allows retry or switch |
| Preconditions | 1. MTN MoMo Business API sandbox credentials are configured. 2. A POS session is open. 3. The active cart total is UGX 20,000. 4. The sandbox environment is configured to simulate a 60-second timeout (no response). 5. The application's MoMo timeout threshold is 60 seconds. |
| Test Steps | 1. On the payment screen, select "MTN MoMo". 2. Enter the sandbox timeout phone number. 3. Tap "Send Payment Request". 4. Wait for the timeout period to elapse (60 seconds). 5. Observe the screen. |
| Expected Result | After 60 seconds, the pending indicator clears. The system displays the message "Payment request timed out. The customer did not respond in time." Two buttons are visible: "Retry" and "Switch Payment Method". No receipt is generated. No sale record is created. |
| Pass Criteria | Timeout message displayed after the configured timeout period; no receipt; no sale record; "Retry" and "Switch Payment Method" buttons present. |
| Priority | Critical |

---

### FR-POS-014 — Credit Limit Enforcement

---

**TC-POS-012**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-012 |
| FR Reference | FR-POS-014, BR-002 |
| Title | Verify credit sale within limit completes without block |
| Preconditions | 1. A POS session is open. 2. Customer "Nalwoga Sarah" has credit limit = UGX 500,000 and current outstanding balance = UGX 200,000. 3. The active cart total = UGX 150,000 (would bring balance to UGX 350,000, within the limit). 4. Tester is authenticated as Cashier. |
| Test Steps | 1. Select "Nalwoga Sarah" as the customer on the active cart. 2. On the payment screen, select "Credit" as the payment method. 3. Observe the displayed credit information. 4. Tap "Confirm Sale". |
| Expected Result | Before confirmation, the screen displays: Outstanding Balance = UGX 200,000; Credit Limit = UGX 500,000; Available Credit = UGX 300,000. No block message appears. The sale completes; the receipt is generated. "Nalwoga Sarah"'s outstanding balance updates to UGX 350,000 in real time. |
| Pass Criteria | Sale completes; no block; customer's outstanding balance = UGX 350,000 after completion. |
| Priority | Critical |

---

**TC-POS-013**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-013 |
| FR Reference | FR-POS-014, BR-002 |
| Title | Verify credit sale at exactly the credit limit completes without block |
| Preconditions | 1. A POS session is open. 2. Customer "Nalwoga Sarah" has credit limit = UGX 500,000 and current outstanding balance = UGX 350,000. 3. The active cart total = UGX 150,000 (would bring balance to exactly UGX 500,000 = credit limit). 4. Tester is authenticated as Cashier. |
| Test Steps | 1. Select "Nalwoga Sarah" as the customer. 2. Select "Credit" as payment method. 3. Tap "Confirm Sale". |
| Expected Result | No block message appears. The sale completes. Customer outstanding balance = UGX 500,000. |
| Pass Criteria | Sale completes; no block; outstanding balance = UGX 500,000 (exactly equals credit limit). |
| Priority | Critical |

---

**TC-POS-014**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-014 |
| FR Reference | FR-POS-014, BR-002 |
| Title | Verify credit sale over limit is blocked for Cashier role |
| Preconditions | 1. A POS session is open. 2. Customer "Nalwoga Sarah" has credit limit = UGX 500,000 and outstanding balance = UGX 450,000. 3. The active cart total = UGX 100,000 (would bring balance to UGX 550,000, exceeding the limit by UGX 50,000). 4. Tester is authenticated as Cashier. |
| Test Steps | 1. Select "Nalwoga Sarah" as the customer. 2. Select "Credit" as payment method. 3. Tap "Confirm Sale". |
| Expected Result | The system blocks the sale and displays the message: "Credit limit exceeded. Outstanding: UGX 450,000. Limit: UGX 500,000. This sale would exceed the limit by UGX 50,000." The "Confirm Sale" button is disabled. A "Request Manager Override" button is displayed. |
| Pass Criteria | Sale is blocked; message text matches expected format with correct values; "Confirm Sale" disabled; "Request Manager Override" visible. |
| Priority | Critical |

---

**TC-POS-015**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-015 |
| FR Reference | FR-POS-014, BR-002 |
| Title | Verify manager override allows credit sale over limit and records override in audit log |
| Preconditions | 1. Continuation of TC-POS-014 state: credit sale is blocked for Cashier. 2. A Manager-role user credential ("Mugisha James") is available. 3. The system is showing the "Credit limit exceeded" block message. |
| Test Steps | 1. Tap "Request Manager Override". 2. Enter Manager credentials for "Mugisha James". 3. Enter reason code "SPECIAL_CUSTOMER_ARRANGEMENT" in the reason code field. 4. Tap "Approve Override". 5. Observe the result. 6. Check the audit log. |
| Expected Result | 1. The "Confirm Sale" button becomes enabled. 2. The sale completes and a receipt is generated. 3. Customer outstanding balance = UGX 550,000. 4. The audit log contains a new entry with: user = "Mugisha James", action = "CREDIT_OVERRIDE", reason = "SPECIAL_CUSTOMER_ARRANGEMENT", amount = UGX 100,000, customer = "Nalwoga Sarah", timestamp = current date/time (within 5 seconds of action). |
| Pass Criteria | Sale completes; audit log entry exists with correct manager name, reason code, and customer; balance = UGX 550,000. |
| Priority | Critical |

---

### FR-POS-021 — POS Session Opening Float

---

**TC-POS-016**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-016 |
| FR Reference | FR-POS-021, BR-007 |
| Title | Verify POS session requires opening float before any sale can be processed |
| Preconditions | 1. No POS session is currently open for the test branch. 2. Tester is authenticated as Cashier. |
| Test Steps | 1. Open the POS screen. 2. Attempt to add a product to the cart. 3. Observe the system response. |
| Expected Result | The system displays a modal or blocking message: "No session open. Please enter your opening float to start a session." The cart is inaccessible. No product can be added. |
| Pass Criteria | Cart is inaccessible; opening float prompt is displayed; product add is blocked. |
| Priority | Critical |

---

**TC-POS-017**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-017 |
| FR Reference | FR-POS-021, BR-007 |
| Title | Verify opening float amount is recorded against the session and visible in the session report |
| Preconditions | 1. No POS session is currently open. 2. Tester is authenticated as Cashier. |
| Test Steps | 1. Open the POS screen. 2. Enter opening float = UGX 75,000. 3. Tap "Open Session". 4. Close the session at end of test. 5. View the session reconciliation report. |
| Expected Result | 1. After "Open Session" is tapped, the POS cart becomes accessible. 2. The session reconciliation report (FR-POS-022) shows Opening Float = UGX 75,000. |
| Pass Criteria | Opening float = UGX 75,000 recorded in session record; POS becomes operational immediately. |
| Priority | Critical |

---

**TC-POS-018**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-018 |
| FR Reference | FR-POS-021, BR-007 |
| Title | Verify API rejects a sale request when no session is open |
| Preconditions | 1. No POS session is open for the test tenant and branch. 2. A valid JWT for a Cashier-role user is available. |
| Test Steps | 1. Send a POST request to `POST /api/v1/sales` with a valid cart payload and a valid JWT, but with no open session for the authenticated branch. 2. Observe the HTTP response. |
| Expected Result | The API returns HTTP 409 with error code `NO_OPEN_SESSION` in the response body. No sale record is created in the database. |
| Pass Criteria | HTTP 409 returned; error code = `NO_OPEN_SESSION`; 0 sale records created. |
| Priority | Critical |

---

### BR-008 — Receipt Gap Detection

---

**TC-POS-019**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-019 |
| FR Reference | FR-POS-023, FR-REP-008, BR-008 |
| Title | Verify sequential receipts with no gap produce no receipt gap event on session close |
| Preconditions | 1. A POS session is open. 2. 5 sales are completed in sequence, generating receipts REC-1001, REC-1002, REC-1003, REC-1004, REC-1005 with no gaps. |
| Test Steps | 1. Complete 5 sales in the POS session producing the 5 sequential receipts. 2. Close the POS session. 3. View the receipt gap report for this session. |
| Expected Result | The receipt gap report shows 0 gaps for this session. No gap event is logged. |
| Pass Criteria | Receipt gap report shows gap count = 0 for the session. |
| Priority | High |

---

**TC-POS-020**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-020 |
| FR Reference | FR-POS-023, FR-REP-008, BR-008 |
| Title | Verify a missing receipt number in the sequence is flagged as a gap event on session close |
| Preconditions | 1. A POS session is open. 2. Sales have been completed, generating receipts REC-1001, REC-1002, REC-1003, REC-1005 (REC-1004 is missing — simulated via direct database deletion of the pending record before sync, or via the test harness). 3. Session is ready to be closed. |
| Test Steps | 1. Close the POS session. 2. View the receipt gap report for this session. |
| Expected Result | The receipt gap report shows 1 gap entry for this session: Expected receipt number = REC-1004, Session ID = the current session ID, Cashier = the test cashier's name, Date = today's date. |
| Pass Criteria | Receipt gap report contains exactly 1 entry for REC-1004; all fields (session ID, cashier, expected receipt number, date) are populated correctly. |
| Priority | Critical |

---

### BR-009 — Offline Sale Queue and Sync

---

**TC-POS-021**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-021 |
| FR Reference | FR-POS-026, FR-POS-027, BR-009 |
| Title | Verify sales processed in airplane mode are stored locally with status pending_sync |
| Preconditions | 1. A POS session is open on Android. 2. The device has a populated product catalogue cached locally in Room. 3. Airplane mode is OFF. The cashier is authenticated with a valid session. |
| Test Steps | 1. Enable airplane mode on the Android device. 2. Confirm no network connectivity (observe the no-internet indicator). 3. Complete 5 sales totalling at least UGX 100,000. 4. After each sale, observe that a receipt is generated locally. 5. Open the pending sync queue view (if accessible in the UI) or query the local Room database. |
| Expected Result | All 5 sales are stored in the local Room database with `sync_status = "pending_sync"`. Each sale has: a local receipt number, a sale total, a timestamp, and the cashier's ID. No sale is lost or corrupted. The POS operates without displaying any error related to connectivity. |
| Pass Criteria | 5 records in Room with `sync_status = "pending_sync"`; each has a non-null receipt number, total, timestamp, and cashier ID; POS usable throughout. |
| Priority | Critical |

---

**TC-POS-022**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-022 |
| FR Reference | FR-POS-027, BR-009 |
| Title | Verify all offline sales sync to the server within 30 seconds of connectivity restoration |
| Preconditions | 1. Continuation of TC-POS-021: 5 sales are in Room with `sync_status = "pending_sync"`. 2. Airplane mode is currently ON. |
| Test Steps | 1. Disable airplane mode (restore internet connectivity). 2. Start a timer at the moment connectivity is restored. 3. Wait up to 30 seconds. 4. Check the server-side sales history via the web interface or API. |
| Expected Result | Within 30 seconds of connectivity restoration, all 5 offline sales appear in the server-side sales history with: correct `franchise_id`, sale amounts matching the local records, correct timestamps, and `sync_status = "synced"` in the local Room database. 0 sales are lost. |
| Pass Criteria | All 5 sales on server with correct amounts and franchise_id; local records show `sync_status = "synced"`; all within 30-second window. |
| Priority | Critical |

---

**TC-POS-023**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-023 |
| FR Reference | FR-POS-027, BR-009 |
| Title | Verify idempotency key prevents duplicate sale creation on double-submit |
| Preconditions | 1. 1 pending-sync sale exists with `idempotency_key = "IDEM-TEST-001"` in the queue. 2. The server has not yet received this sale. |
| Test Steps | 1. Submit the pending-sync payload with `idempotency_key = "IDEM-TEST-001"` to `POST /api/v1/sales/sync`. 2. Immediately submit the same payload with the same `idempotency_key` a second time. 3. Query the database for sales with `idempotency_key = "IDEM-TEST-001"`. |
| Expected Result | The first submission returns HTTP 201 and creates exactly 1 sale record. The second submission returns HTTP 200 (idempotent repeat acknowledged) and does not create a second sale record. The database contains exactly 1 sale record with `idempotency_key = "IDEM-TEST-001"`. |
| Pass Criteria | First POST = HTTP 201; second POST = HTTP 200; exactly 1 sale record in database. |
| Priority | Critical |

---

### FR-POS-015 — Multi-Payment (BR-010)

---

**TC-POS-024**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-024 |
| FR Reference | FR-POS-015, BR-010 |
| Title | Verify multi-payment sale records each component separately and sum equals cart total |
| Preconditions | 1. A POS session is open. 2. The active cart total = UGX 50,000. 3. Two payment accounts exist: "Cash Drawer" and "MTN MoMo Account". 4. MTN MoMo sandbox is available (else execute cash + credit only for this test). `[BLOCKED: GAP-001]` for MoMo component. |
| Test Steps | 1. On the payment screen, select "Split Payment". 2. Enter Cash = UGX 30,000 against "Cash Drawer". 3. Enter MTN MoMo = UGX 20,000 against "MTN MoMo Account". 4. Observe the remaining balance indicator. 5. Tap "Confirm Sale". 6. Check the sale_payments table for this sale. |
| Expected Result | 1. After entering both components, the remaining balance shows UGX 0. 2. The "Confirm Sale" button is enabled. 3. The sale record in the database has 2 rows in `sale_payments`: one for UGX 30,000 against Cash Drawer and one for UGX 20,000 against MTN MoMo. 4. The sum of the two payment rows = UGX 50,000 = cart total. |
| Pass Criteria | 2 payment rows in `sale_payments`; sum = UGX 50,000 = cart total; sale completes. |
| Priority | Critical |

---

**TC-POS-025**

| Field | Content |
|---|---|
| Test Case ID | TC-POS-025 |
| FR Reference | FR-POS-015, BR-010 |
| Title | Verify payment components that do not sum to cart total block sale completion |
| Preconditions | 1. A POS session is open. 2. The active cart total = UGX 50,000. 3. Split payment mode is active. |
| Test Steps | 1. Enter Cash = UGX 30,000. 2. Enter MTN MoMo = UGX 15,000. 3. Observe the total and the "Confirm Sale" button. |
| Expected Result | The remaining balance displays UGX 5,000 (50,000 - 30,000 - 15,000). The "Confirm Sale" button is disabled. An inline message reads: "Total payments (UGX 45,000) do not equal the cart total (UGX 50,000). Add UGX 5,000 to proceed." |
| Pass Criteria | "Confirm Sale" disabled; remaining balance = UGX 5,000; message text is accurate. |
| Priority | Critical |

---

## Module F-002: Inventory and Stock Management

---

### FR-INV-011 — FEFO Batch Selection (BR-006)

---

**TC-INV-001**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-001 |
| FR Reference | FR-INV-011, BR-006 |
| Title | Verify FEFO selects the batch with the nearest expiry date for stock decrement |
| Preconditions | 1. Product "Yoghurt 250ml" has batch tracking enabled. 2. Two batches exist: Batch A (expiry 2026-05-01, quantity = 50) and Batch B (expiry 2026-07-15, quantity = 60). 3. A POS session is open. 4. Tester is authenticated as Cashier. |
| Test Steps | 1. Add "Yoghurt 250ml" × 5 to the POS cart. 2. Complete the sale as a cash payment. 3. Check the stock levels for both batches after sale completion. |
| Expected Result | Batch A (expiry 2026-05-01, nearest expiry) is decremented by 5 (remaining: 45). Batch B (expiry 2026-07-15) remains at 60. An immutable stock movement record is created linking the sale to Batch A. |
| Pass Criteria | Batch A quantity = 45; Batch B quantity = 60; stock movement record references Batch A. |
| Priority | Critical |

---

**TC-INV-002**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-002 |
| FR Reference | FR-INV-011, BR-006 |
| Title | Verify manager can override FEFO batch selection |
| Preconditions | 1. Same two-batch state as TC-INV-001: Batch A (expiry 2026-05-01, qty 50), Batch B (expiry 2026-07-15, qty 60). 2. A POS session is open. 3. Tester is authenticated as Manager. |
| Test Steps | 1. Add "Yoghurt 250ml" × 3 to the POS cart. 2. On the cart, tap the batch override option for "Yoghurt 250ml". 3. Select Batch B (expiry 2026-07-15) manually. 4. Complete the sale. 5. Check stock levels for both batches. |
| Expected Result | Batch B is decremented by 3 (remaining: 57). Batch A remains at 50. An override event is recorded in the audit log with the manager's user ID, the overridden batch (Batch A), the selected batch (Batch B), and the timestamp. |
| Pass Criteria | Batch B = 57; Batch A = 50; audit log override entry exists with manager ID, batch IDs, and timestamp. |
| Priority | High |

---

**TC-INV-003**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-003 |
| FR Reference | FR-INV-011, BR-006 |
| Title | Verify FEFO exhausts batch A fully before consuming batch B |
| Preconditions | 1. Batch A (expiry 2026-05-01, qty 3). Batch B (expiry 2026-07-15, qty 60). 2. A POS session is open. |
| Test Steps | 1. Add "Yoghurt 250ml" × 5 to the POS cart. 2. Complete the sale. 3. Check stock levels for both batches. |
| Expected Result | Batch A is fully consumed (remaining: 0). Batch B is decremented by 2 (remaining: 58). The system issues no error; the sale completes normally. 2 stock movement records are created: 1 for 3 units from Batch A and 1 for 2 units from Batch B. |
| Pass Criteria | Batch A = 0; Batch B = 58; 2 stock movement records for this sale; no error displayed. |
| Priority | Critical |

---

### FR-INV-012 — Near-Expiry Batch Alert

---

**TC-INV-004**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-004 |
| FR Reference | FR-INV-012 |
| Title | Verify a batch within 30 days of expiry appears in the near-expiry alert list |
| Preconditions | 1. Today's date is 2026-04-05. 2. Product "Milk UHT 1L" has a batch with expiry date 2026-04-25 (20 days away). 3. The near-expiry alert threshold is configured at 30 days for this business. |
| Test Steps | 1. Open the dashboard. 2. Navigate to the near-expiry alerts section or expand the near-expiry panel. |
| Expected Result | The near-expiry alert list displays "Milk UHT 1L" with batch expiry date 2026-04-25 and days to expiry = 20. The alert is also visible as a badge or item on the dashboard. |
| Pass Criteria | "Milk UHT 1L" batch entry present in near-expiry list with expiry date 2026-04-25 and days to expiry = 20. |
| Priority | High |

---

**TC-INV-005**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-005 |
| FR Reference | FR-INV-012 |
| Title | Verify a batch with 31 days to expiry does NOT appear in the 30-day near-expiry alert list |
| Preconditions | 1. Today's date is 2026-04-05. 2. Product "Juice 1L" has a batch with expiry date 2026-05-06 (31 days away). 3. Near-expiry alert threshold = 30 days. |
| Test Steps | 1. Open the dashboard. 2. Navigate to the near-expiry alerts section. |
| Expected Result | "Juice 1L" is not listed in the near-expiry alert section. |
| Pass Criteria | "Juice 1L" absent from the near-expiry alert list. |
| Priority | Medium |

---

### FR-INV-009 — Stock Adjustment Approval Threshold (BR-005)

---

**TC-INV-006**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-006 |
| FR Reference | FR-INV-009, BR-005 |
| Title | Verify stock adjustment below approval threshold is applied immediately |
| Preconditions | 1. The approval threshold is configured at UGX 500,000 (quantity × cost price). 2. Product "Sugar 1kg" has cost price = UGX 4,500 and current stock = 100 units. 3. Tester is authenticated as Stock Manager. |
| Test Steps | 1. Navigate to Inventory > Stock Adjustment. 2. Select product "Sugar 1kg". 3. Enter adjustment quantity = -10 (reducing stock by 10 units; value = 10 × UGX 4,500 = UGX 45,000 — below threshold). 4. Select reason code "DAMAGED". 5. Save the adjustment. |
| Expected Result | The adjustment is applied immediately. Stock for "Sugar 1kg" = 90 units. The adjustment record shows status = "applied". No approval notification is sent. A stock movement record of type "adjustment" is created. |
| Pass Criteria | Stock = 90; adjustment status = "applied"; no pending approval notification generated. |
| Priority | High |

---

**TC-INV-007**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-007 |
| FR Reference | FR-INV-009, BR-005 |
| Title | Verify stock adjustment above approval threshold is held as pending_approval |
| Preconditions | 1. Approval threshold = UGX 500,000. 2. Product "Cooking Oil 20L" has cost price = UGX 150,000 and stock = 50 units. 3. Adjustment quantity = -5 (value = 5 × UGX 150,000 = UGX 750,000 — above threshold). 4. Tester is authenticated as Stock Manager. |
| Test Steps | 1. Navigate to Inventory > Stock Adjustment. 2. Select "Cooking Oil 20L". 3. Enter adjustment quantity = -5. 4. Select reason code "DAMAGED". 5. Save the adjustment. |
| Expected Result | The adjustment is NOT applied. Stock for "Cooking Oil 20L" remains at 50 units. The adjustment record shows status = "pending_approval". A push notification is sent to the branch manager. |
| Pass Criteria | Stock = 50 (unchanged); adjustment status = "pending_approval"; push notification triggered. |
| Priority | High |

---

**TC-INV-008**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-008 |
| FR Reference | FR-INV-009, BR-005 |
| Title | Verify manager approval of a pending stock adjustment applies the adjustment |
| Preconditions | 1. Continuation of TC-INV-007: adjustment for "Cooking Oil 20L" is in status "pending_approval" with quantity = -5. 2. Tester is authenticated as Manager. |
| Test Steps | 1. Navigate to the pending approvals list. 2. Find the stock adjustment for "Cooking Oil 20L". 3. Tap "Approve". 4. Check stock levels. |
| Expected Result | The stock adjustment is applied: "Cooking Oil 20L" stock = 45 units. The adjustment record status changes to "applied". An immutable stock movement record of type "adjustment" is created. |
| Pass Criteria | Stock = 45; adjustment status = "applied"; stock movement record created. |
| Priority | High |

---

### FR-INV-014 — Physical Stock Count

---

**TC-INV-009**

| Field | Content |
|---|---|
| Test Case ID | TC-INV-009 |
| FR Reference | FR-INV-014 |
| Title | Verify physical stock count freezes movements, records variance, and creates pending adjustment |
| Preconditions | 1. Product "Rice 5kg" has a system stock level = 120 units. 2. Tester is authenticated as Stock Manager. |
| Test Steps | 1. Navigate to Inventory > Stock Count. 2. Select "Rice 5kg" and initiate a count. 3. Confirm that no new stock movements for "Rice 5kg" are accepted during the count window (attempt a sale — observe that the system blocks or queues it). 4. Enter physical count = 115 units. 5. Save the count. 6. Observe the adjustment created. |
| Expected Result | 1. During the count window, stock movements for "Rice 5kg" are frozen. 2. After entering physical count = 115, the system calculates variance = 115 - 120 = -5. 3. A pending adjustment for -5 units is created with status "pending_approval". 4. The count is not applied until a manager approves the adjustment. |
| Pass Criteria | Variance = -5; pending adjustment created with status = "pending_approval"; system stock remains 120 until approved. |
| Priority | High |

---

## Module F-003: Customer Management

---

### FR-CUS-001 — Customer Create

---

**TC-CUS-001**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-001 |
| FR Reference | FR-CUS-001 |
| Title | Verify customer create with required fields only succeeds |
| Preconditions | 1. Tester is authenticated as Cashier or Manager. 2. The Customers module is accessible. |
| Test Steps | 1. Navigate to Customers > New Customer. 2. Enter Name = "Apio Grace". 3. Enter Phone = "+256701234567". 4. Leave all optional fields blank. 5. Tap "Save". |
| Expected Result | The customer record is saved. The customer profile page for "Apio Grace" is displayed, showing Name = "Apio Grace" and Phone = "+256701234567". No error messages are shown. |
| Pass Criteria | Customer record created; profile page loads with correct name and phone. |
| Priority | High |

---

**TC-CUS-002**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-002 |
| FR Reference | FR-CUS-001 |
| Title | Verify customer create without required phone number is rejected with an error |
| Preconditions | 1. Tester is authenticated as Cashier or Manager. |
| Test Steps | 1. Navigate to Customers > New Customer. 2. Enter Name = "Opio Fred". 3. Leave Phone blank. 4. Tap "Save". |
| Expected Result | The system displays an inline validation error: "Phone number is required." The customer record is not saved. |
| Pass Criteria | Save is blocked; error message "Phone number is required." displayed; 0 new customer records in database. |
| Priority | High |

---

### FR-CUS-004 / FR-CUS-005 — Credit Management

---

**TC-CUS-003**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-003 |
| FR Reference | FR-CUS-004 |
| Title | Verify credit sale increments customer outstanding balance in real time |
| Preconditions | 1. Customer "Byamukama Tom" has outstanding balance = UGX 0 and credit limit = UGX 200,000. 2. A POS session is open. 3. Cart total = UGX 80,000. |
| Test Steps | 1. Select "Byamukama Tom" as the customer. 2. Process a credit sale for UGX 80,000. 3. Navigate to "Byamukama Tom"'s customer profile immediately after sale completion. |
| Expected Result | "Byamukama Tom"'s Outstanding Balance = UGX 80,000. The change is reflected immediately without a page reload or manual refresh. |
| Pass Criteria | Outstanding balance = UGX 80,000 immediately after sale completion. |
| Priority | Critical |

---

**TC-CUS-004**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-004 |
| FR Reference | FR-CUS-005 |
| Title | Verify payment against customer balance reduces outstanding balance and generates receipt |
| Preconditions | 1. Customer "Byamukama Tom" has outstanding balance = UGX 80,000 (from TC-CUS-003). 2. Tester is authenticated as Cashier or Manager. |
| Test Steps | 1. Navigate to "Byamukama Tom"'s profile. 2. Tap "Record Payment". 3. Enter amount = UGX 50,000, method = Cash. 4. Tap "Save". 5. Select "Generate Receipt". |
| Expected Result | "Byamukama Tom"'s outstanding balance = UGX 30,000 (80,000 - 50,000). A receipt is generated showing: customer name "Byamukama Tom", payment amount UGX 50,000, payment method Cash, date and time. |
| Pass Criteria | Balance = UGX 30,000; receipt generated with correct customer name, amount, and method. |
| Priority | High |

---

### FR-CUS-006 — Debtors Ageing Report

---

**TC-CUS-005**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-005 |
| FR Reference | FR-CUS-006 |
| Title | Verify debtors ageing report groups customers correctly into 0-30, 31-60, 61-90, and 90+ day buckets |
| Preconditions | 1. Today's date = 2026-04-05. 2. Customer A: outstanding balance = UGX 100,000 from a sale on 2026-04-01 (4 days ago — 0-30 bucket). 3. Customer B: outstanding balance = UGX 200,000 from a sale on 2026-02-20 (44 days ago — 31-60 bucket). 4. Customer C: outstanding balance = UGX 50,000 from a sale on 2026-01-10 (85 days ago — 61-90 bucket). 5. Customer D: outstanding balance = UGX 300,000 from a sale on 2025-11-01 (155 days ago — 90+ bucket). |
| Test Steps | 1. Navigate to Reports > Debtors Ageing. 2. Generate the report for today's date. |
| Expected Result | The report shows 4 ageing buckets. Customer A appears in the 0-30 days bucket with UGX 100,000. Customer B appears in the 31-60 days bucket with UGX 200,000. Customer C appears in the 61-90 days bucket with UGX 50,000. Customer D appears in the "Over 90 days" bucket with UGX 300,000. Total per bucket sums are correct. |
| Pass Criteria | Each customer in the correct bucket; all balances match seeded values; no customer is in the wrong bucket. |
| Priority | High |

---

### FR-CUS-008 / FR-CUS-009 — Customer Portal Magic Link

---

**TC-CUS-006**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-006 |
| FR Reference | FR-CUS-008 |
| Title | Verify magic link generation creates a unique expiring URL and sends it to the customer's phone |
| Preconditions | 1. Customer "Nakato Rita" has registered phone number "+256702345678". 2. Africa's Talking sandbox is configured. 3. Tester is authenticated as Manager. |
| Test Steps | 1. Navigate to "Nakato Rita"'s customer profile. 2. Tap "Send Portal Link". 3. Select delivery method = SMS. 4. Confirm dispatch. 5. Check the Africa's Talking sandbox outbox. |
| Expected Result | 1. The system generates a unique URL (format: `https://app.maduuka.com/portal/<unique-token>`). 2. An SMS is dispatched to "+256702345678" containing the portal URL. 3. The token is recorded in the database with status = "active" and expiry = 30 days from now. |
| Pass Criteria | SMS dispatched to correct number; token in database with status = "active" and expiry date = today + 30 days. |
| Priority | High |

---

**TC-CUS-007**

| Field | Content |
|---|---|
| Test Case ID | TC-CUS-007 |
| FR Reference | FR-CUS-009 |
| Title | Verify customer portal displays correct data in read-only mode with no login required |
| Preconditions | 1. A valid portal magic link exists for "Nakato Rita" with outstanding balance = UGX 120,000 and credit limit = UGX 500,000. 2. The portal URL is accessible via a browser. |
| Test Steps | 1. Open the portal URL in a browser without logging in. 2. Observe the page content. 3. Attempt to edit the outstanding balance field (if visible). 4. Attempt to modify any data. |
| Expected Result | 1. The portal displays: "Nakato Rita", outstanding balance = UGX 120,000, credit limit = UGX 500,000, full purchase history for the customer, and a download button for the PDF statement. 2. No login form is shown. 3. No form fields or edit controls are present. All data is read-only. |
| Pass Criteria | Portal accessible without login; correct balance and credit limit displayed; no editable fields present; PDF statement download available. |
| Priority | High |

---

*End of MADUUKA-TC-001 v1.0 — Test Cases: F-001 POS, F-002 Inventory, F-003 Customer Management*

**Total test cases in this file: 41**
