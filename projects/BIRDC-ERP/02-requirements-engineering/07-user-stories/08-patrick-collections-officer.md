# Persona 8: Patrick — Collections Officer (Cooperative Procurement)

**Profile:** Age 28, Certificate in Agriculture, basic smartphone user. Travels to rural collection points 3–4 days per week. Receives matooke from cooperative farmers. Records individual farmer contributions using the Farmer Delivery Android app in areas with no internet. Prints farmer receipts using a Bluetooth printer.

**Critical requirement:** Farmer Delivery App — fully offline, GPS coordinates, Bluetooth scale integration, Bluetooth receipt printer.

---

## US-070: Register a New Farmer Offline

**US-070:** As Patrick, I want to register a new farmer in the Farmer Delivery App while at a rural collection point with no internet, so that no farmer is turned away because of connectivity issues.

**Acceptance criteria:**

- The Farmer Delivery App supports full farmer registration offline: Patrick enters name, NIN, contact number, cooperative, mobile money number, and GPS coordinates (auto-captured by device GPS).
- Patrick captures the farmer's photo using the device camera; the photo is stored locally with the farmer record.
- The new farmer record is synced to the server when connectivity is restored; the server assigns the farmer's permanent ID and returns it to the app.
- Until sync completes, the farmer is assigned a local temporary ID visible to Patrick with a "Pending Sync" indicator; Patrick can continue recording deliveries against the temporary ID.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-002

---

## US-071: Record a Farmer Delivery with Bluetooth Scale Integration

**US-071:** As Patrick, I want to record a farmer's matooke delivery by connecting to a Bluetooth weighing scale, so that the weight is captured directly from the scale without manual transcription errors.

**Acceptance criteria:**

- The Farmer Delivery App scans for and connects to a paired Bluetooth scale; when Patrick taps "Capture Weight," the app reads the current scale reading and populates the weight field automatically.
- If the Bluetooth scale is unavailable, Patrick can enter the weight manually; manually entered weights are flagged with an "M" indicator in the delivery record.
- Patrick selects the quality grade (A, B, C) as assessed at the collection point; the app displays the applicable unit price per grade from the active Bulk PO.
- The delivery record shows the calculated gross payable (weight × unit price) before Patrick confirms, so he can verify the amount verbally with the farmer.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-003

---

## US-072: Print a Farmer Delivery Receipt via Bluetooth Printer

**US-072:** As Patrick, I want to print a delivery receipt for the farmer immediately after recording their delivery, so that the farmer has documented proof of what was received and the amount owed.

**Acceptance criteria:**

- After confirming a farmer delivery, the Farmer Delivery App sends the print command to the paired Bluetooth 80mm thermal printer within 3 seconds.
- The printed receipt includes: BIRDC/PIBID header, collection date, collection point, farmer name and NIN, matooke weight (kg), quality grade, unit price, gross payable (UGX), and transaction reference number.
- If the Bluetooth printer is unavailable, the app offers an SMS receipt option: the receipt details are sent as an SMS to the farmer's registered mobile number.
- Patrick can reprint any receipt from the current session's delivery list.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-004

---

## US-073: Capture GPS Farm Location During Registration

**US-073:** As Patrick, I want to record the GPS coordinates of each farmer's farm during field registration, so that BIRDC has accurate spatial data for planning collection routes and zone management.

**Acceptance criteria:**

- The Farmer Delivery App captures GPS coordinates (latitude and longitude) to ±10 metres accuracy when Patrick is at the farm location and taps "Capture Location."
- Patrick can capture multiple farm locations per farmer (a farmer may have several plots); each farm is named and linked to the farmer's profile.
- GPS coordinates are stored with the farmer's profile and synced to the server; they are visible in the Farmer Management module (F-010) on the web ERP as a map view.
- If GPS signal is unavailable (indoors or under dense canopy), Patrick receives a message: "GPS signal weak. Move to an open area or enter coordinates manually."

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-005

---

## US-074: View the Cooperative Batch Delivery Summary Before Closing

**US-074:** As Patrick, I want to see the total weight received per farmer for the current collection session before closing the batch, so that I can identify any missing farmers before I leave the collection point.

**Acceptance criteria:**

- The batch summary screen shows the current collection session: cooperative name, collection date, list of farmers with individual weights delivered, quality grades, and gross payable amounts.
- Patrick can tap any farmer in the list to review or amend their delivery record before batch closure (amendments before closure only).
- The batch total weight is displayed prominently at the top of the summary; Patrick compares it against his paper backup count before closing.
- When Patrick closes the batch, the status changes to "Stage 2 — Batch Received" and the batch enters the Stage 2 to Stage 3 workflow in the web ERP for individual contribution breakdown approval.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-009-010

---

## US-075: View Farmer Payment Confirmation Notifications

**US-075:** As Patrick, I want to see when farmers in my cooperatives have been paid via mobile money, so that I can confirm payment at the next collection and resolve any payment failures.

**Acceptance criteria:**

- The Farmer Delivery App displays a payment notification feed showing mobile money payment confirmations for farmers in Patrick's assigned cooperative zones.
- Each notification shows: farmer name, payment amount (UGX), payment date, and mobile money transaction reference.
- Failed payments (invalid number, limit exceeded) are also displayed so Patrick can collect updated mobile money details from the affected farmer at the next collection.
- Payment notifications are synced from the server and available offline once downloaded.

**MoSCoW Priority:** Should Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-006

---

## US-076: View a Farmer's Complete Delivery and Payment History

**US-076:** As Patrick, I want to view any registered farmer's delivery history and payment record from the Farmer Delivery App, so that I can answer farmer questions about their earnings in the field without calling the office.

**Acceptance criteria:**

- Patrick searches for a farmer by name or NIN; the app displays the farmer's profile: photo, cooperative, farm location, and contact.
- The history tab shows all deliveries: date, weight (kg), quality grade, unit price, gross payable, deductions, and net paid, sorted by date (most recent first).
- The cumulative totals are shown at the top: total matooke delivered (kg) and total net paid (UGX).
- Farmer history is available offline based on the most recent sync; Patrick sees a "Data as of [sync date]" notice.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-007

---

## US-077: Sync All Offline Deliveries When Connectivity Is Restored

**US-077:** As Patrick, I want all deliveries I recorded offline to sync automatically when I reach an area with internet, so that I never need to manually upload data or re-enter records.

**Acceptance criteria:**

- When the Farmer Delivery App detects internet connectivity, it automatically syncs all pending deliveries, farmer registrations, and farm location records without Patrick initiating any action.
- The sync completes within 5 minutes for up to 200 pending delivery records.
- Patrick receives an in-app notification: "[n] deliveries synced successfully. [m] farmers synced."
- If any record fails to sync (e.g., a duplicate farmer NIN detected at the server), the system flags the specific failed record with the reason and keeps the remaining records synced; Patrick is notified of the failure and the corrective action required.

**MoSCoW Priority:** Must Have

**Delivery Phase:** Phase 3

**FR Reference:** FR-010-008
