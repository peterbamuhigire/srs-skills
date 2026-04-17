# 5. Mobile UX — Android App Specifications

All 6 Android apps use Kotlin + Jetpack Compose. UI components follow Material Design 3 adapted to the BIRDC colour palette. Minimum supported version: Android 8.0 (API 26).

## 5.1 Common Mobile UX Patterns

These patterns apply to all 6 apps.

### Offline Status Indicator

A persistent banner at the top of every screen when the device has no internet connection:

- **Visual:** Orange banner, full-width, below the app bar.
- **Text:** "Offline — data will sync when you reconnect."
- **Behaviour:** Disappears automatically when connectivity is restored. Replaced by a brief green "Synced" banner for 3 seconds after successful sync.

### Sync Progress Indicator

When background sync is in progress (WorkManager job running):

- A linear progress indicator at the top of the screen (below the app bar or offline banner if both are shown).
- Text beside the indicator: "Syncing [N] records…"
- On completion: "Sync complete — [N] records uploaded." Banner dismisses after 3 seconds.

If sync fails:

- The indicator turns red: "Sync failed — [N] records pending. Tap to retry."
- The pending count persists until sync succeeds. Data is never lost.

### Bluetooth Printer Pairing Flow

Used by: Sales Agent App (80mm receipt printing), Farmer Delivery App (farmer receipt printing).

1. User taps the **Printer** icon in the app bar (top right).
2. A bottom sheet slides up showing: paired printers list and a **Scan for Printers** button.
3. On scan, Bluetooth devices appear in a list within 5 seconds. ESC/POS compatible printers are highlighted with a printer icon.
4. User taps a printer to pair. The Android BluetoothDevice pairing dialog appears.
5. On successful pairing, the printer appears in the paired list with a green "Connected" status badge.
6. The selected printer is persisted in EncryptedSharedPreferences as the default printer for the app.
7. All subsequent print actions use the stored default. The printer icon in the app bar shows green when a default is paired, grey when unpaired.

### Biometric Authentication

Used by: Sales Agent App, Executive Dashboard App (sensitive financial data).

- On app launch after initial login, BiometricPrompt is shown if biometric is enrolled on the device.
- Prompt title: "Confirm your identity to continue."
- On success: app proceeds directly to the home screen with the stored JWT refreshed via the refresh token endpoint.
- On failure (3 attempts): app locks and requires full password entry.
- Users who do not have biometric enrolled are prompted once to set it up; they can skip and use password only.

---

## 5.2 Sales Agent App

**Users:** 1,071 field sales agents (primary access method: this Android app)

**Key screens:**

| Screen | Description |
|---|---|
| Home / Dashboard | S-010 equivalent — cash balance (large), outstanding, quick actions |
| Offline POS | S-011 equivalent — product search, cart, payment types, receipt generation |
| Submit Remittance | S-012 equivalent — amount, payment method, reference; queues if offline |
| Commission Statement | S-013 equivalent — period filter, earnings table |
| My Stock | S-014 equivalent — agent's virtual inventory, FEFO expiry badges |
| Print Receipt | Bluetooth ESC/POS receipt from last sale |

**Offline behaviour:** All POS transactions are written to Room (SQLite) first. WorkManager uploads to the server API whenever a connection is available. Remittance submissions are queued identically. Agent stock balance is read from the local Room cache and updated on sync.

---

## 5.3 Farmer Delivery App

**Users:** Field collection officers (Patrick and peers)

**Key screens:**

| Screen | Description |
|---|---|
| Farmer Registration (offline) | Full registration form: name, NIN, cooperative, contact, mobile money number, photo capture. GPS coordinates auto-captured. Stored in Room until sync. |
| Batch Delivery Entry | Select cooperative, enter batch weight, select quality grade. Individual farmer entries added one by one. |
| Individual Delivery | Farmer search (local Room cache, searchable offline), weight (manual entry or Bluetooth scale integration via serial port), grade, print receipt. |
| Bluetooth Scale Integration | When a Bluetooth scale is paired, the weight field auto-populates from the scale reading. A "Capture Weight" button locks the reading. |
| Farmer Receipt Print | ESC/POS receipt: farmer name, NIN, cooperative, batch no., weight, grade, unit price, net payable, date. |
| GPS Farm Profiling | Map view (cached OpenStreetMap tiles) — tap to mark farm boundary polygon. Saved to Room, synced when online. |

---

## 5.4 Warehouse App

**Users:** Warehouse staff (David and peers)

**Key screens:**

| Screen | Description |
|---|---|
| Receive Stock (GRN) | Scan PO barcode (ML Kit), confirm received quantities, post GRN. |
| Transfer Confirm | Scan transfer order barcode, confirm items transferred, update local stock. |
| Physical Count | Scan item barcodes, enter counted quantities, system quantity shown for comparison. |
| Stock Enquiry | Search by barcode or name, view balance by location, FEFO expiry status. |

**Offline behaviour:** GRN posting and transfer confirmation are queued in Room when offline. Stock count worksheets are downloaded before going to the warehouse floor (in case of no signal in storage areas).

---

## 5.5 Executive Dashboard App

**Users:** Director, Finance Director

**Key screens:**

| Screen | Description |
|---|---|
| Dashboard | S-044 equivalent — 5 KPI cards, P&L snapshot, push notification history. Pull-to-refresh. |
| P&L Statement | Full current-period P&L, expandable by category. Export to PDF. |
| Trial Balance | Condensed trial balance. Export to PDF. |
| Cash Position | Bank accounts, petty cash, total liquid position. |
| Budget Variance | Vote-by-vote expenditure vs. approved budget. Traffic-light colour coding. |
| Alert History | All system alerts: budget threshold breaches, EFRIS failures, agent anomalies. |

**Push notifications:** Firebase Cloud Messaging (FCM) delivers the following alerts:

| Trigger | Notification Text |
|---|---|
| Parliamentary vote reaches 80% | "Budget alert: Development Vote is 80% spent — UGX [balance] remaining." |
| Parliamentary vote reaches 95% | "URGENT: Development Vote at 95%. Director override required for further expenditure." |
| Agent remittance overdue > 7 days | "Agent [Name] — UGX [amount] outstanding for 7 days. Review required." |
| EFRIS submission fails after 3 retries | "EFRIS failure — Invoice [INV-#] not submitted to URA. Finance Manager alerted." |

---

## 5.6 HR Self-Service App

**Users:** All BIRDC/PIBID staff (150+)

**Key screens:**

| Screen | Description |
|---|---|
| Home | Leave balance cards (annual, sick, etc.), last payslip summary card. |
| Apply for Leave | Leave type selector, date range picker, days auto-calculated, supporting document photo attach, submit. |
| Payslip History | List of payslips by period. Tap to view full payslip PDF. |
| Attendance Record | Calendar view with daily attendance status: Present / Absent / Leave / Holiday. |
| Leave Status | Status of pending leave applications (Pending / Approved / Rejected). |

---

## 5.7 Factory Floor App

**Users:** Moses (Production Supervisor) and QC staff

**Key screens:**

| Screen | Description |
|---|---|
| Active Production Orders | List of in-progress orders with status, progress %, and mass balance indicator. |
| Production Order Detail | S-033 equivalent — mobile-first layout; job card steps, worker assignment, mass balance calculator. |
| Record Completion | Enter primary product qty, by-product qty, scrap. Mass balance validates before submit. |
| Worker Attendance | Mark daily attendance for factory workers assigned to the active order. |
| QC Submission | Inspection form (dynamic template), photo capture for visual parameters, submit results. |

**Offline behaviour:** Production completion data and QC inspection results are stored in Room if offline. WorkManager uploads when connectivity returns. The mass balance validation runs locally so Moses can see the result immediately even without a connection.
