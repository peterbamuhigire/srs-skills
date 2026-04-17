---
title: "SRS — Maduuka iOS Platform"
subtitle: "Section 3: iOS-Specific Functional Requirements"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 3: iOS-Specific Functional Requirements

This section defines functional requirements that are specific to the iOS platform, layered on top of the Phase 1 SRS. Every Phase 1 requirement (**FR-POS-001** through **FR-SET-012**) applies to iOS in full. The requirements below describe iOS-native capability implementations, platform constraints, and intentional asymmetries between iOS and other platforms.

Requirement identifier format: `FR-iOS-[MODULE]-[NNN]`

---

## 3.1 Point of Sale — F-001 (iOS)

**FR-iOS-POS-001:** When a cashier taps the camera icon in the iOS POS search field, the system shall request camera permission via `AVCaptureDevice.requestAccess(for: .video)` if not already granted. If permission is denied, the system shall display an alert directing the cashier to enable camera access in iOS Settings. If permission is granted, the system shall open a full-screen `AVCaptureSession` scanning view and automatically add the matching product to the active cart within 1 second of successful barcode detection (EAN-13, EAN-8, Code-128, Code-39, QR) using the Vision framework `VNDetectBarcodesRequest`, without requiring a confirmation tap — satisfying **FR-POS-002** on iOS.

*Verifiability:* Scan 100 barcodes across 10 distinct products on the reference device. 99 of 100 scans must result in a cart addition event within ≤ 1000 ms of the frame containing the barcode being captured by `AVCaptureSession`.

---

**FR-iOS-POS-002:** When a cashier completes a sale on iOS and selects "Print Receipt," the system shall attempt to send the receipt to the paired Bluetooth thermal printer (80mm) via Core Bluetooth using the raw ESC/POS print protocol. The print job shall be transmitted within 5 seconds of the cashier's print action. If no Bluetooth printer is paired, the system shall open the iOS Bluetooth settings flow to guide pairing. — *GAP-004: Compatibility with Epson, Xprinter, and TP-Link 80mm printers must be verified by the dev team on Uganda-market hardware before Phase 2 build commences.*

*Verifiability:* Pair the app with each of the 3 target printer models (Epson, Xprinter, TP-Link 80mm). Complete a sale. Tap "Print Receipt." The printer must produce a correctly formatted 80mm thermal receipt within ≤ 5 seconds for each printer model.

---

**FR-iOS-POS-003:** When a cashier selects "Share Receipt" after a sale on iOS, the system shall generate the receipt as a PDF using `PDFKit` and present the iOS share sheet (`UIActivityViewController`) with the PDF as the share item. The share sheet shall allow the cashier to select WhatsApp, Messages, Mail, Files, AirDrop, or any other installed share target. This satisfies **FR-POS-019** (WhatsApp receipt) on iOS without requiring a direct API call to the share target.

*Verifiability:* Complete a sale. Tap "Share Receipt." The iOS share sheet must appear within 1 second with the PDF receipt attached. Selecting WhatsApp from the share sheet must open WhatsApp with the PDF pre-attached.

---

**FR-iOS-POS-004:** When a cashier holds or resumes a cart on iOS (FR-POS-009, FR-POS-010), the system shall persist the held cart state — all items, quantities, prices, applied discounts, and hold reference number — as a Core Data `HeldCart` entity. The held cart shall survive app termination (process kill) and device restart. On next app launch, all held carts shall be available for resumption without data loss.

*Verifiability:* Add 5 products to the cart. Apply an order discount. Tap "Hold Sale." Force-kill the app via the iOS app switcher. Reopen the app. Navigate to held carts. The held cart must be present with all items, quantities, and the discount intact.

---

**FR-iOS-POS-005:** When a POS session is active on iOS, the system shall hide the iOS status bar and the app tab bar to present a full-screen POS canvas, consistent with Design Covenant DC-002 (sale completion in under 3 minutes) and the full-screen POS requirement in **F-001**. The status bar and tab bar shall be restored when the cashier exits the POS session to the main navigation.

*Verifiability:* Open a POS session on an iPhone X. Verify the status bar (time, battery, signal) and the bottom tab bar are not visible during the active session. Exit the session. Verify both are restored.

---

## 3.2 Inventory and Stock Management — F-002 (iOS)

**FR-iOS-INV-001:** When a user opens the stock count workflow on iOS and taps the barcode scan button, the system shall activate an `AVCaptureSession` scanning view using the Vision framework to decode the product barcode. On successful decode, the system shall look up the matching product in the local Core Data store and navigate directly to the stock count entry screen for that product, without requiring a manual search step.

*Verifiability:* Initiate a physical stock count. Scan 20 product barcodes. Each scan must navigate to the correct product's count entry screen within ≤ 1 second of successful barcode detection.

---

**FR-iOS-INV-002:** When a product batch's expiry date is within the configured alert threshold (30, 60, or 90 days — configurable per business, per **FR-INV-012**), the system shall schedule a local `UNUserNotificationCenter` notification to fire at 08:00 on the alert date. Additionally, when connectivity is available, the app shall register the expiry alert with the server so that an Apple Push Notification service (APNs) alert is delivered to the business owner and branch manager regardless of whether the iOS app is currently running.

*Verifiability:* Set a batch expiry date to 29 days from today with a 30-day alert threshold. Verify a local notification fires at 08:00 the following day. Close the app. Verify an APNs push notification is delivered to the owner's device.

---

**FR-iOS-INV-003:** When the iOS app's `BGAppRefreshTask` fires, the system shall request the current stock levels for all products in the local Core Data catalogue from the server API and update the local store with any server-side changes. The background task shall complete within 30 seconds, consistent with NFR-iOS-010. Stock level changes fetched in the background shall be reflected on the dashboard and inventory list the next time those screens appear in the foreground.

*Verifiability:* Update a product's stock level via the web interface while the iOS app is backgrounded. Wait for the background refresh to fire (simulate via Xcode BGTaskScheduler). Foreground the app and open the inventory list. The updated stock level must be visible without a manual refresh.

---

## 3.3 Customer Management — F-003 (iOS)

**FR-iOS-CUS-001:** When a user taps "Send Portal Link" for a customer on iOS, the system shall call the server API to generate the magic-link URL (per **FR-CUS-008**) and then present the iOS share sheet (`UIActivityViewController`) pre-populated with the magic-link URL as plain text. The share sheet shall allow delivery via WhatsApp, Messages (SMS), Mail, or any installed app. The system shall not require the cashier to manually copy the URL.

*Verifiability:* Tap "Send Portal Link" for a test customer. The iOS share sheet must appear within 1 second with the magic-link URL pre-populated. Selecting WhatsApp must open WhatsApp with the URL in the message compose field.

---

**FR-iOS-CUS-002:** When a user opens the customer map view on iOS, the system shall render all customers with a recorded location as annotation pins on a `MapKit` `MKMapView`. Tapping a pin shall present a callout showing the customer's name, outstanding balance, and a "View Profile" button that navigates to the customer detail screen. This replaces the Leaflet.js map used on the web platform and the WebView-embedded Leaflet.js used on Android — iOS uses a fully native MapKit implementation.

*Verifiability:* Open the customer map with 50 customers who have recorded locations. All 50 must appear as pins on the MapKit map. Tapping any pin must show the callout. Tapping "View Profile" must navigate to the correct customer detail screen.

---

**FR-iOS-CUS-003:** When a user generates a customer statement on iOS (per **FR-CUS-007**), the system shall render the statement as a PDF using `PDFKit` and present the iOS share sheet for distribution via WhatsApp, email, AirDrop, or local save to Files app. The PDF shall include all transactions for the selected date range, the customer name, business logo, and closing balance.

*Verifiability:* Generate a customer statement for a customer with 20 transactions. The share sheet must appear with a valid PDF attached. Open the PDF; verify it contains all 20 transactions, the business logo, and the correct closing balance.

---

## 3.4 Supplier and Vendor Management — F-004 (iOS)

**FR-iOS-SUP-001:** When a user taps "Export PDF" on a purchase order on iOS, the system shall render the purchase order as a PDF using `PDFKit` and present the iOS share sheet (`UIActivityViewController`). The PDF shall include: business name and logo, supplier name and address, order date, PO number, line items (product, quantity, unit price, line total), and order total. This satisfies **FR-SUP-003** (PDF purchase order) on iOS.

*Verifiability:* Create a purchase order with 5 line items. Tap "Export PDF." The share sheet must appear within 2 seconds with a PDF attached. Open the PDF; verify all 5 line items, business logo, supplier name, and order total are present.

---

**FR-iOS-SUP-002:** When a user is in the goods receiving workflow on iOS and taps "Scan Barcode," the system shall open an `AVCaptureSession` view to scan the barcode on the incoming goods. On successful decode, the system shall match the decoded barcode to a product on the open purchase order line items and highlight the matching line for quantity confirmation. This supports the goods receipt verification step in **FR-SUP-004**.

*Verifiability:* Open a goods receipt for a PO with 5 line items. Scan the barcode of item 3. The matching PO line must be highlighted within ≤ 1 second of barcode detection. The quantity entry field for that line must gain focus automatically.

---

**FR-iOS-SUP-003:** When a user views a supplier's profile on iOS and taps "Generate Statement," the system shall produce a supplier statement PDF via `PDFKit` and present the iOS share sheet, satisfying **FR-SUP-007** on iOS. The PDF shall list all purchase orders, goods receipts, invoices, and payments within the selected date range with a closing balance.

*Verifiability:* Generate a supplier statement for a supplier with 10 transactions. The share sheet must appear with a valid PDF. Open the PDF; verify all 10 transactions and the closing balance are present.

---

## 3.5 Expenses and Petty Cash — F-005 (iOS)

**FR-iOS-EXP-001:** When a user taps "Attach Receipt Photo" in the expense entry screen on iOS, the system shall request camera permission via `AVCaptureDevice.requestAccess(for: .video)`. If granted, the system shall activate the camera using `AVCaptureSession`. On image capture, the system shall store the photo and pass it to a Vision framework `VNRecognizeTextRequest` (Optical Character Recognition) pipeline to extract the total amount and vendor name from the receipt image. Extracted values shall be pre-populated in the expense amount and vendor description fields, satisfying **FR-EXP-002** on iOS.

*Verifiability:* Photograph 10 distinct printed receipts with legible amounts and vendor names. In ≥ 7 of 10 cases, the correct amount and vendor name must be pre-populated in the expense fields within 3 seconds of image capture.

---

**FR-iOS-EXP-002:** When a user configures a recurring expense on iOS (per **FR-EXP-008**), the system shall schedule a `UNUserNotificationCenter` local notification to fire at 08:00 on the recurrence date, prompting the user to review and confirm the draft expense. The notification payload shall include the expense category name and configured amount.

*Verifiability:* Configure a monthly recurring expense. Advance the test device clock to the recurrence date at 08:00. A local notification must appear showing the expense category and amount. Tapping the notification must open the app directly to the pending draft expense.

---

**FR-iOS-EXP-003:** When a user completes an expense entry on iOS and the expense includes a receipt photo, the system shall upload the photo to the server file storage (Wasabi S3-compatible) using a background `URLSession` upload task. The upload shall proceed even if the user navigates away from the expense screen before the upload completes. The expense record shall be saved locally in Core Data immediately; the photo URL field shall be updated when the upload confirms.

*Verifiability:* Submit an expense with a receipt photo. Immediately navigate away to the Dashboard. After 30 seconds, open the expense record; the receipt photo URL must be populated and the photo must be accessible from the server.

---

## 3.6 Financial Accounts and Cash Flow — F-006 (iOS)

**FR-iOS-FIN-001:** Bank statement CSV import (FR-FIN-005) is not available on the iOS platform. This is an intentional design asymmetry: CSV file import is a web-only feature because iOS file management imposes friction that would reduce usability for the target persona. On the iOS cash flow and bank reconciliation screens, the "Import CSV" action shall be hidden. If a user asks a support question about this feature, the app help text shall direct them to the web interface. This intentional asymmetry shall be documented in the Help section of the iOS app.

*Verifiability:* Open the bank reconciliation screen on iOS. Verify that no "Import CSV" button or menu item is visible.

---

**FR-iOS-FIN-002:** When a user opens the Financial Accounts screen on iOS, the system shall display real-time account balances fetched from the Core Data local store (last sync). All cash transfer, deposit, withdrawal, and reconciliation workflows available on the Android platform (**FR-FIN-001** through **FR-FIN-007**, excluding **FR-FIN-005**) shall be fully functional on iOS.

*Verifiability:* Complete a cash transfer between two accounts on iOS. Verify the source account balance decreases and the destination account balance increases in the local Core Data store. Verify the transfer records appear on the web platform after sync.

---

**FR-iOS-FIN-003:** [CONTEXT-GAP: iOS home screen widget scope — F-006] The stakeholder has not confirmed whether an iOS WidgetKit widget displaying account cash position is required for Phase 2. If confirmed, the widget shall display the current sum of all payment account balances from the most recent sync. This requirement is deferred pending stakeholder decision.

---

## 3.7 Sales Reporting and Analytics — F-007 (iOS)

**FR-iOS-REP-001:** When a user navigates to any chart view in the Sales Reporting module on iOS (revenue trend, top sellers, gross margin analysis), the system shall render all charts using the Swift Charts framework (`Charts`). No web-view-embedded chart library shall be used. Charts shall support interactive touch (tap to reveal data point values, drag to scrub a date range).

*Verifiability:* Open the revenue trend chart with 30 days of data. Tap a data point; a tooltip showing the date and revenue value must appear within 200 ms. Drag across the chart; the tooltip must track the finger position continuously.

---

**FR-iOS-REP-002:** When a user taps "Export PDF" on any report screen on iOS, the system shall render the report as a PDF using `PDFKit` + `Core Graphics` and present the iOS share sheet within 5 seconds. The PDF shall include the report title, selected date range, business name, and all data rows visible in the on-screen report.

*Verifiability:* Generate a "Sales by Product" report for a 30-day period with 50 products. Tap "Export PDF." The share sheet must appear within ≤ 5 seconds with a valid PDF attached. Open the PDF; verify all 50 product rows are present.

---

**FR-iOS-REP-003:** When a user taps "Export CSV" on any report screen on iOS, the system shall generate a CSV string, write it to a temporary file in the app's `Caches` directory, and present the iOS share sheet with the CSV file attached. The CSV shall be accepted by Files app, Numbers, and Excel for iOS.

*Verifiability:* Export a daily sales report as CSV on iOS. Open the CSV via Files app. Open the CSV in Numbers for iOS. Verify all columns and rows match the on-screen report.

---

## 3.8 HR and Payroll — F-008 (iOS)

**FR-iOS-HR-001:** When a payroll run is approved on iOS and payslips are generated, the system shall render each payslip as a PDF using `PDFKit`. The payslip PDF shall include: business name and logo, employee name, NIN, pay period, earnings breakdown, deductions breakdown, gross pay, total deductions, and net pay. This satisfies **FR-HR-014** on iOS using a native PDF engine rather than a server-side HTML-to-PDF conversion.

*Verifiability:* Approve a test payroll run on iOS for 3 employees. Three payslip PDFs must be generated within 30 seconds. Open each PDF; verify all required fields are present and the business logo is rendered correctly.

---

**FR-iOS-HR-002:** When a payslip PDF is generated on iOS, the system shall present the iOS share sheet (`UIActivityViewController`) with the PDF attached, allowing the HR manager to deliver it via WhatsApp, email, AirDrop, or Messages. This satisfies **FR-HR-015** (payslip delivery) on iOS. The system shall also invoke the server-side delivery trigger (Africa's Talking WhatsApp API) as a parallel action so that the employee receives delivery on their phone even if the manager does not manually share the PDF.

*Verifiability:* Generate a payslip on iOS. The share sheet must appear with the PDF attached. Simultaneously, within 60 seconds, the employee's registered phone must receive a WhatsApp message containing the payslip PDF, delivered via Africa's Talking.

---

**FR-iOS-HR-003:** When a staff member submits a leave application from the iOS app, the system shall send the leave request to the server API and the server shall dispatch an APNs push notification to the manager's iOS device within 1 minute of submission, consistent with **FR-HR-005**. The notification payload shall include the staff member's name, leave type, and requested dates. Tapping the notification shall deep-link the manager directly to the pending leave approval screen.

*Verifiability:* Submit a leave request on iOS as a staff member. Within 60 seconds, an APNs notification must arrive on the manager's iOS device. Tap the notification. The app must open directly to the leave request detail screen for the submitted request.

---

## 3.9 Dashboard and Business Health — F-009 (iOS)

**FR-iOS-DASH-001:** When the Dashboard screen is active in the foreground on iOS, the system shall refresh all KPI card values (Today's Revenue, Transaction Count, Outstanding Credit, Cash Position) automatically every 2 minutes using a `Timer.publish(every: 120, on: .main, in: .default)` stream combined with a `task` modifier. The refresh shall fetch updated data from the local Core Data store. If connectivity is available, the refresh shall also trigger a pull from the server API before updating the display.

*Verifiability:* Open the Dashboard. Complete a sale on the web interface while the iOS Dashboard is visible. Within 2 minutes and 30 seconds (refresh interval + API response time), the Today's Revenue KPI on the iOS Dashboard must reflect the new sale without any manual user action.

---

**FR-iOS-DASH-002:** [CONTEXT-GAP: iOS WidgetKit widget scope — F-009] The stakeholder has not confirmed whether a WidgetKit home screen widget displaying Today's Revenue and Transaction Count is required for Phase 2. If confirmed, the widget shall: display Today's Revenue and Transaction Count as a small-size widget, refresh using `WidgetKit` `TimelineProvider` every 15 minutes, read cached values from App Group `UserDefaults` shared between the main app and the widget extension, and not require the user to open the app to see current data. This requirement is deferred pending stakeholder decision.

---

**FR-iOS-DASH-003:** When a user switches branches using the branch switcher on the iOS Dashboard (per **FR-DASH-006**), the system shall reload all KPI cards and the recent transactions list from the Core Data local store scoped to the selected branch within 2 seconds of the branch selection. The selected branch context shall persist across app sessions in Keychain.

*Verifiability:* Switch branches on the iOS Dashboard. All 4 KPI cards must update within ≤ 2 seconds. Relaunch the app; the previously selected branch must be restored.

---

## 3.10 Settings and Configuration — F-010 (iOS)

**FR-iOS-SET-001:** When a business owner enables two-factor authentication (2FA) on iOS (per **FR-SET-011**), the system shall display the TOTP secret as a QR code using a `Core Image` `CIQRCodeGenerator` filter, sized for scanning by Google Authenticator or compatible TOTP apps. A fallback manual entry code shall be displayed below the QR code. After the user scans the QR code and enters the first 6-digit TOTP code to confirm setup, the system shall POST the confirmed setup to the server API. The TOTP secret shall never be stored on the device; only the server retains it.

*Verifiability:* Enable 2FA on iOS. Scan the QR code with Google Authenticator. Enter the generated 6-digit code in the confirmation field. The system must confirm 2FA is active. Log out and log in from a second device; TOTP code entry must be required.

---

**FR-iOS-SET-002:** When a user views Connected Devices on iOS (per **FR-SET-012**), the system shall display a list of all active sessions retrieved from the server API, showing device name, last active date, and IP address. When the user taps "Revoke" on any device entry, the system shall call the server API to invalidate that device's refresh token immediately. If the user revokes the current device, the app shall log out and clear the local Keychain and Core Data store.

*Verifiability:* Log in from 3 devices. Open Connected Devices on iOS. All 3 devices must be listed. Revoke device 2. Attempt to use device 2; the next API call must return HTTP 401 Unauthorized.

---

**FR-iOS-SET-003:** When a user requests a full data export on iOS (per **FR-SET-008**), the system shall call the server API to initiate the export job. When the server sends an APNs push notification indicating the export is ready, the app shall receive the notification and display an alert offering to open the download link. The user shall be able to save the ZIP file to the Files app via the iOS share sheet.

*Verifiability:* Request a data export on iOS. Within 10 minutes, an APNs notification must arrive. Tap the notification; the app must present the share sheet with the ZIP file download link or file. Save to Files app; verify the ZIP contains CSV files for all modules.

---

**FR-iOS-SET-004:** When a business owner initiates account deletion on iOS (per **FR-SET-009**), the system shall display a confirmation alert requiring the owner to type the word "DELETE" to proceed. On confirmation, the system shall call the server API to initiate the deletion sequence. Immediately after the server acknowledges the request, the app shall clear all local Core Data stores, purge all Keychain entries, and navigate to the app's login screen. The server retains data for 30 days before permanent deletion per **FR-SET-009**.

*Verifiability:* Initiate account deletion on iOS. Verify the confirmation alert requires "DELETE" input. After confirmation, open the app's Core Data file in a debug session; all entities must be empty. Inspect Keychain items; no Maduuka-prefixed items must remain.
