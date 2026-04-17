# Section 3: External Interface Requirements

## 3.1 User Interfaces

### 3.1.1 Android Application

The Android application shall present a full-screen POS mode that hides all navigation and exposes only the product search, cart, and payment controls. In POS mode, the interface shall be operable with one hand on a phone screen with a minimum diagonal size of 5 inches.

The Android application shall present a product grid with configurable column counts: 3 columns on a standard phone, 5 columns on a 7-inch tablet, and 6 columns on a 10-inch tablet.

The Android application shall support a persistent navigation bar or bottom sheet providing access to: Dashboard, POS, Inventory, Customers, Reports, and Settings.

All interactive elements in the Android application shall have a minimum tap target size of 48x48 dp, in accordance with Material Design accessibility guidelines.

The Android application shall support a dark mode toggle (system / light / dark) settable per user.

The Android application dashboard shall support an optional Android home screen widget displaying Today's Revenue and Cash Position without requiring the app to be opened.

### 3.1.2 Web Application

The web application shall adapt its layout to the viewport width: sidebar navigation on screens wider than 992 px; bottom-sheet navigation on screens narrower than 992 px.

The web application shall provide a full-screen POS terminal mode accessible via a browser fullscreen action. In this mode, the URL bar, browser toolbar, and all application navigation outside the POS shall be hidden.

The web application shall provide a Kitchen Display System (KDS) URL that renders active KOTs in a full-screen, auto-refreshing view. This URL shall remain accessible after initial authentication without requiring re-login, so that a dedicated kitchen device can remain on the KDS screen without periodic session interruptions.

All interactive elements in the web application shall have a minimum click/tap target size of 44x44 px.

The web application shall support keyboard navigation: all screens shall be navigable by Tab key, with a logical Tab order. The POS module shall support keyboard shortcuts for adding items, applying discounts, and completing checkout.

### 3.1.3 Customer Self-Service Portal

The customer portal shall be accessible via a magic link delivered by SMS or WhatsApp. The link shall not require the customer to create a password or username. Access via the magic link shall expire after 30 days of inactivity.

The customer portal shall display: full purchase history, outstanding credit balance, current credit limit, and downloadable PDF statements. It shall be read-only -- no data modification is permitted.

## 3.2 Hardware Interfaces

### 3.2.1 Bluetooth Thermal Receipt Printer

The Android application shall connect to an 80mm thermal receipt printer via Bluetooth. The supported printer models in Phase 1 are: Epson TM series (Bluetooth variant), Xprinter XP-series Bluetooth, and TP-Link (Bluetooth-enabled) receipt printers.

The web application shall send receipts to a USB-connected or network-connected thermal printer via the browser print dialog (standard Ctrl+P / browser print API). No proprietary browser plugin is required.

### 3.2.2 Barcode Scanner

The Android application shall scan EAN-13, EAN-8, Code-128, Code-39, and QR barcodes using the device camera via ML Kit. A product shall be added to the active POS cart within 1 second of barcode detection.

The Android application and web application shall accept barcode input from a Bluetooth or USB barcode scanner configured in HID keyboard-emulation mode. The scanner shall function without any driver installation by treating scanner output as keyboard input.

### 3.2.3 Bluetooth Weight Scale

The Android application shall accept manual weight entry (kg, g) for weight-based products. Automatic integration with a Bluetooth weight scale is a Phase 2 enhancement; Phase 1 requires manual weight entry only.

## 3.3 Software Interfaces

### 3.3.1 MTN MoMo Business API

The system shall integrate with the MTN MoMo Business API (Uganda) to initiate push payment requests to a customer's MTN MoMo wallet from the POS. The API credentials required are the MTN MoMo Business API key and secret (distinct from the standard Merchant API -- see GAP-001 in `_context/gap-analysis.md`). The integration must handle API response codes: success (transaction confirmed), pending (awaiting customer confirmation), and failure (transaction declined or timed out).

### 3.3.2 Airtel Money API

The system shall integrate with the Airtel Money Uganda API to collect payments from customers' Airtel Money wallets. The integration must handle success, pending, and failure response states equivalent to the MTN MoMo integration.

### 3.3.3 Africa's Talking API

The system shall integrate with Africa's Talking for:

- SMS delivery: transaction notifications, payment reminders, customer statements.
- WhatsApp Business API: digital receipt delivery, customer portal magic links, payslip delivery to staff.

### 3.3.4 Wasabi S3-Compatible Storage

The system shall store the following objects in Wasabi S3-compatible object storage: product images (JPEG/PNG, max 2 MB each), expense receipt photos (JPEG/PNG, max 5 MB each), payslip PDFs, and generated report PDFs. Objects shall be stored with per-tenant path prefixes keyed to `franchise_id`.

### 3.3.5 Firebase Cloud Messaging (FCM)

The Android application shall receive push notifications via Firebase Cloud Messaging (FCM). Notification types include: low stock alert, payment received, leave request (for managers), expense approval needed, daily revenue summary, and payment reminder for overdue customer credit.

### 3.3.6 MySQL 8.x Database

The backend shall connect to a MySQL 8.x database. Every table shall include a `franchise_id` column with a non-nullable foreign key constraint to the `businesses` table. The database shall be the sole source of truth for all persistent data; no persistent data shall be stored exclusively in the application cache or file system.

### 3.3.7 EFRIS API (Phase 3 -- Not in Phase 1 Scope)

The EFRIS API integration is documented here for interface awareness only. Phase 1 data models must be designed to accommodate EFRIS submission in Phase 3 without requiring schema migrations to core sales and invoice tables.

## 3.4 Communications Interfaces

### 3.4.1 REST API

All communication between mobile/web clients and the backend shall use HTTPS REST with JSON payloads. The API shall version its endpoints with a URL prefix (e.g., `/api/v1/`). All API responses shall include: an HTTP status code, a success boolean, a data payload (on success), and an errors array (on failure).

### 3.4.2 Transport Security

All API communication shall use TLS 1.3 or higher. TLS 1.2 and below shall be rejected. The Android application shall implement certificate pinning via OkHttp `CertificatePinner`, pinning the Maduuka server's leaf certificate and its intermediate CA. A pin rotation mechanism must be included to allow certificate renewal without an app update.

### 3.4.3 Mobile Authentication

Mobile clients shall authenticate using JWT Bearer tokens. The access token TTL is 15 minutes. The refresh token TTL is 30 days. Refresh tokens shall be stored in AES-256-GCM `EncryptedSharedPreferences` on Android. Access token renewal shall occur automatically in the background without requiring the user to re-enter credentials, provided the refresh token has not expired.

### 3.4.4 Web Authentication

The web application shall use server-side session authentication. Every state-changing HTTP request (POST, PUT, PATCH, DELETE) shall include a CSRF token validated server-side. Session cookies shall be marked `HttpOnly`, `Secure`, and `SameSite=Strict`.

### 3.4.5 KDS Auto-Refresh

The Kitchen Display System web view shall auto-refresh active KOTs every 10 seconds using either a polling mechanism (HTTP GET to the KOT endpoint) or a WebSocket connection. The refresh mechanism shall not require any user action. If the connection is lost, the display shall show a visible connectivity warning and retry automatically every 5 seconds.
