# 5. Functional Requirements — Farmer Delivery Android Application

The Farmer Delivery App is an Android application used by Field Collection Officers (persona: Patrick) at cooperative collection points. It implements a subset of F-009 and F-010 functions in an offline-first architecture conforming to DC-005. All requirements in this section apply to the Android application unless explicitly stated as "server-side".

**Technology:** Kotlin, Jetpack Compose, Room (SQLite), Retrofit + OkHttp, WorkManager, ML Kit, Bluetooth ESC/POS, BiometricPrompt, EncryptedSharedPreferences. Minimum Android version: Android 8.0 (API 26).

---

## 5.1 Authentication and Session Management

**FR-MOB-001** — When a Field Collection Officer opens the Farmer Delivery App for the first time on a device, the system shall require the officer to authenticate with their ERP username and password over HTTPS; on successful authentication, the server shall return a JWT access token (15-minute expiry) and a 30-day refresh token; the refresh token shall be stored in EncryptedSharedPreferences.

**FR-MOB-002** — When the access token expires, the app shall automatically use the refresh token to obtain a new access token in the background without interrupting the officer's workflow; if the refresh token is also expired or invalid, the app shall prompt re-authentication on the next sync attempt but shall not prevent offline data entry.

**FR-MOB-003** — When the device supports biometric authentication (fingerprint or face recognition via BiometricPrompt) and the officer has enrolled a biometric, the app shall offer biometric unlock after the initial credential login; biometric unlock shall use the stored refresh token to re-obtain an access token without re-entering credentials.

**FR-MOB-004** — When a Field Collection Officer's account is deactivated on the server (e.g., dismissal), the server shall invalidate all refresh tokens for that account; the app shall detect the invalidated token on the next sync attempt and shall log the officer out, preventing any further local data entry from syncing under that account.

---

## 5.2 Offline Data Collection — Core Principle

**FR-MOB-005** — When the Farmer Delivery App is operating without network connectivity, the system shall allow the Field Collection Officer to perform all of the following actions without any connectivity: register new farmers, capture GPS coordinates, photograph farmers, record individual farmer deliveries with weight and quality grade, and print farmer receipts via Bluetooth; none of these actions shall display an error or prompt due to lack of network connectivity.

**FR-MOB-006** — When network connectivity is restored, the app shall automatically initiate a background sync via WorkManager without requiring any officer action; the sync shall complete in the background and notify the officer via an in-app notification (non-disruptive) when complete.

---

## 5.3 Offline Farmer Registration (App)

**FR-MOB-007** — When a Field Collection Officer registers a new farmer using the Farmer Delivery App offline, the system shall capture all mandatory fields defined in FR-FAR-001, store the record in Room (SQLite) with a temporary local ID, capture GPS coordinates using the device GPS (accuracy target: ≤ 10 m CEP), and capture a farmer photo using the device camera stored at minimum 480 × 640 pixels; the registration shall be fully functional without network connectivity.

**FR-MOB-008** — When a farmer registration is synced to the server (FR-FAR-004), the server shall check for NIN duplicates; if a duplicate is found, the server shall return a conflict response containing the existing farmer's name and registration number; the app shall display this conflict to the officer and shall discard the duplicate local record after the officer acknowledges; the permanent farmer ID returned by the server shall replace the local ID in all linked delivery records.

---

## 5.4 Delivery Recording with Bluetooth Scale

**FR-MOB-009** — When a Field Collection Officer initiates a delivery record for a registered farmer, the app shall display a farmer search interface allowing search by name, registration number, or barcode scan (ML Kit barcode scanning of the farmer registration card barcode); search shall operate against the locally cached farmer database without requiring network connectivity.

**FR-MOB-010** — When a farmer is identified for a delivery, the system shall display the farmer's photo, name, registration number, cooperative, and last 3 deliveries (from local cache) to allow visual confirmation by the officer before recording the delivery.

**FR-MOB-011** — When a Bluetooth digital weighing scale is connected to the device, the app shall read the weight value directly from the scale via Bluetooth and auto-populate the weight entry field; the officer shall confirm the reading before saving; the scale model used shall be confirmed and the SDK integrated accordingly [CONTEXT-GAP: GAP-011 — scale model and Bluetooth SDK pending BIRDC Procurement confirmation]; if no scale is connected, the officer shall enter the weight manually.

**FR-MOB-012** — When a delivery weight is entered (via scale or manual), the system shall display the calculated gross payable based on the selected quality grade and the current season's pricing schedule (downloaded and cached from the server during the last sync); the gross payable shall be displayed prominently and the officer shall not be able to modify it.

**FR-MOB-013** — When a Field Collection Officer selects a quality grade (A, B, or C) for a delivery, the system shall display the per-kg price for that grade from the cached pricing schedule and the calculated gross payable; the grade selection shall require a single tap with a confirmation step to prevent accidental grade changes.

**FR-MOB-014** — When a delivery record is saved offline, the system shall store: farmer registration number, batch number (from the active batch on the device), weight (kg), quality grade, calculated gross payable, GPS coordinates of the recording point, device timestamp, and officer user ID; the record shall be assigned a local delivery ID prefixed `DLOC-` until synced.

---

## 5.5 Bluetooth Thermal Receipt Printing

**FR-MOB-015** — When a delivery record is saved, the app shall automatically trigger printing of a farmer receipt on the connected Bluetooth 80mm thermal printer using ESC/POS commands; if the printer is not connected, the app shall display a "Print Failed — Printer not connected" message and offer a retry option without losing the saved delivery record.

**FR-MOB-016** — When a farmer receipt is printed, it shall contain: BIRDC/PIBID header, batch number, date and time, farmer name, registration number, cooperative name, weight delivered (kg), quality grade, gross payable (UGX), officer name, and a receipt sequence number; the receipt shall also include a QR code encoding the delivery local ID for traceability.

---

## 5.6 Batch Management on Device

**FR-MOB-017** — When a Field Collection Officer opens the app at the start of a collection day, the app shall display all active cooperative Bulk Purchase Orders (downloaded during last sync) and allow the officer to create a new batch receipt (Stage 2) against an active BPO; the batch number shall be assigned by the server on sync, with a temporary local batch identifier used in all offline records created before sync.

**FR-MOB-018** — When the officer taps "Close Batch" at the end of the collection session, the app shall display: total weight recorded in the batch, number of farmer contribution records, unallocated weight (total batch weight minus sum of farmer contribution weights), and a warning if unallocated weight > 0.5 kg; the batch shall not be marked "Ready for Stage 3 → 4 transition" from the app — that transition occurs on the server after sync and full validation per BR-011.

---

## 5.7 Data Sync and Conflict Resolution

**FR-MOB-019** — When the Farmer Delivery App syncs offline records to the server, the sync shall follow these conflict resolution rules: (1) server record takes priority for farmer profile updates (name, NIN, cooperative, contact details) — if the server has a newer version of a farmer profile than the local cache, the server version overwrites the local version; (2) field delivery records take priority over server records — delivery records created offline on the device are authoritative and shall not be overwritten by the server during sync.

**FR-MOB-020** — When a sync conflict is detected (same record modified both locally and on server between syncs), the app shall log the conflict with: record type, local version timestamp, server version timestamp, and the differing field values; all sync conflicts shall be reported in a "Sync Conflict Log" accessible to the IT Administrator on the web ERP for manual resolution.

**FR-MOB-021** — When a sync completes successfully, the app shall display a sync summary to the officer: number of farmer records synced, number of delivery records synced, number of conflicts detected, and the timestamp of the last successful sync; the last sync timestamp shall be visible on the app home screen.

---

## 5.8 Master Data Caching for Offline Use

**FR-MOB-022** — When the app performs a full sync (at least once per day when connected), the system shall download and cache in Room (SQLite): the complete farmer register for the officer's assigned cooperatives, the active cooperative Bulk Purchase Orders and pricing schedules, the quality grade definitions, the rejection reason codes, and the SMS notification templates; this cached data shall be sufficient for a full offline collection day.

**FR-MOB-023** — When cached master data is more than 7 days old (i.e., the device has been offline for 7+ days), the app shall display a prominent warning to the officer: "Master data is [N] days old. Connect to update before starting today's collection." The app shall continue to function with stale cache but shall clearly indicate the cache age on every delivery record.

---

## 5.9 App Security

**FR-MOB-024** — When a Field Collection Officer leaves the app idle for more than 10 minutes, the app shall require re-authentication (PIN, password, or biometric) before allowing further data entry; any unsaved delivery record in progress shall be preserved in a draft state during the lock period.

**FR-MOB-025** — When sensitive farmer data (NIN, mobile money number) is stored in the local Room database, the system shall encrypt the local database using Android's SQLCipher integration or Room's built-in encryption; the encryption key shall be derived from the officer's credentials and stored in EncryptedSharedPreferences; loss of the officer's credentials shall result in local data becoming inaccessible on that device (data is recoverable from the server for already-synced records).
