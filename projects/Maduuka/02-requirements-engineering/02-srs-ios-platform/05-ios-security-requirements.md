---
title: "SRS — Maduuka iOS Platform"
subtitle: "Section 5: iOS Security Requirements"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 5: iOS Security Requirements

This section specifies iOS-specific security requirements. These requirements supplement the platform-neutral security NFRs in `01-srs/06-nfr.md` (NFR-SEC-001 through NFR-SEC-006) with iOS-specific implementation constraints. Where a Phase 1 NFR references Android-specific APIs, the iOS equivalent specified in this section is authoritative for the iOS platform.

---

## 5.1 Keychain Storage Policy

**FR-iOS-SEC-001: What Shall Be Stored in Keychain**

The following items shall be stored exclusively in the iOS Keychain via `SecItemAdd` / `SecItemUpdate`, and only with the access control attribute `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`:

- JWT access token
- JWT refresh token
- TOTP setup confirmation flag (boolean; not the TOTP secret — that is server-only)
- Biometric authentication policy state (`LAPolicy` selection)
- Selected branch identifier (to persist branch context across sessions)
- Certificate pinning public key hash (read-only; written at build time via Keychain pre-seed in the app bundle)

*Verifiability:* Perform static analysis of all Swift source files; search for any write to `UserDefaults`, `NSUserDefaults`, `FileManager`, or the pasteboard that handles any of the above items. Zero violations must be found.

---

**FR-iOS-SEC-002: What Shall Never Be Stored in UserDefaults**

The following data categories shall never be written to `UserDefaults` or `NSUserDefaults`, regardless of whether the values appear sensitive:

- JWT tokens (access or refresh)
- User passwords or PINs
- Biometric evaluation results
- Business TIN or tax identifiers
- Employee NIN values
- Customer credit limit values
- Any value derived from server-side TOTP secrets

Non-sensitive UI preferences (selected theme, preferred language, onboarding completion flag) may use `UserDefaults`.

*Verifiability:* Perform static analysis using a custom lint rule that flags `UserDefaults.standard.set` calls where the key name matches a known sensitive field pattern. Zero violations must be reported.

---

## 5.2 Encrypted Core Data Store

**FR-iOS-SEC-003: Core Data File Protection**

The primary Core Data persistent store file (SQLite) and the WAL journal file shall use iOS Data Protection class `NSFileProtectionCompleteUnlessOpen` (`FileProtectionType.completeUnlessOpen`). This class encrypts the file when the device is locked, while permitting background tasks to read and write when the device is unlocked.

The `PendingSyncQueue` persistent store (Section 4) shall use `NSFileProtectionComplete` (`FileProtectionType.complete`) — no background access is required for the queue file, so the strongest protection class is appropriate.

*Verifiability:* On a locked test device, use a file system inspection tool (e.g., iMazing in forensic mode) to attempt to open the Core Data SQLite file. The file must not be readable as plaintext. Confirm the file's extended attributes include the `com.apple.quarantine` or equivalent Data Protection class marker.

---

**FR-iOS-SEC-004: Core Data Sensitive Field Encryption**

The following Core Data entity attributes shall be stored as AES-256 encrypted `Binary` attributes rather than plaintext `String` or `Decimal` attributes. Encryption and decryption shall occur in the Data layer, transparently to the Domain and Presentation layers:

- `Employee.nin` (National Identification Number)
- `Employee.bankAccountNumber`
- `Customer.phone`
- `Customer.email`
- `SaleTransaction.paymentReference` (Mobile Money transaction reference)

The AES-256 encryption key for these fields shall be stored in Keychain (separate from the JWT token item) with access control `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` and biometric constraint `kSecAccessControlBiometryCurrentSet`.

*Verifiability:* Export the Core Data SQLite file from a development device. Open the file with a SQLite browser tool. The `nin`, `bankAccountNumber`, `phone`, `email`, and `paymentReference` columns must contain binary ciphertext — not plaintext values — for any stored records.

---

## 5.3 Certificate Pinning Implementation

**FR-iOS-SEC-005: Certificate Pinning Configuration**

The app shall implement certificate pinning for all connections to the Maduuka REST API hostname using `URLSession` delegate method `urlSession(_:didReceive:completionHandler:)`. The implementation shall:

1. Extract the server's leaf certificate from the `SecTrust` object provided by the delegate callback.
2. Compute the SHA-256 hash of the leaf certificate's Subject Public Key Info (SPKI).
3. Compare the computed hash against the set of pinned hashes bundled in the app. The pinned set shall contain at minimum 2 hashes: the current production certificate SPKI hash and one backup hash (the next planned certificate, to allow rotation without forcing a client update).
4. If no hash matches, call `completionHandler(.cancelAuthenticationChallenge)` and log a pinning failure event to the local audit trail.
5. If a hash matches, call `completionHandler(.useCredential, URLCredential(trust: serverTrust))`.

Certificate pin hashes shall be updated via an app update cycle. A minimum of 60 days' overlap between the current and next certificate shall be maintained to prevent service disruption during certificate rotation.

*Verifiability:* Configure Charles Proxy with a custom CA on the test device. Attempt any API call. The connection must fail with `NSURLErrorServerCertificateUntrusted`. The local audit trail must contain a `certificate_pinning_failure` event. Attempt the same call with no proxy; it must succeed.

---

## 5.4 Biometric Re-authentication Policy

**FR-iOS-SEC-006: Biometric Authentication Implementation**

Biometric re-authentication shall be implemented using `LocalAuthentication` framework `LAContext`. The system shall:

1. Evaluate `LAContext().evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason:)` when the app foregrounds after the configured inactivity timeout (default 5 minutes, configurable 1–60 minutes per NFR-iOS-009).
2. Display no app content until the biometric prompt is resolved. A blank screen or the app logo shall be shown while the prompt is pending.
3. On biometric failure (3 consecutive failures on Face ID, or the user taps "Enter Passcode"), fall back to `evaluatePolicy(.deviceOwnerAuthentication)` to allow iOS passcode entry.
4. On successful authentication, record a `biometric_auth_success` event in the local audit trail with timestamp and authentication method.
5. On failure after fallback exhaustion, log the user out: clear the in-memory JWT access token and navigate to the login screen. The Keychain refresh token shall be retained to allow re-login without re-entering credentials from scratch.

*Verifiability:* Background the app for 6 minutes. Foreground it. The biometric prompt must appear before any app content is visible. Fail Face ID 3 times. The passcode prompt must appear. Enter the correct passcode; the app must resume. Enter an incorrect passcode to exhaust the fallback; the app must navigate to the login screen.

---

## 5.5 Root and Jailbreak Detection

**FR-iOS-SEC-007: Jailbreak Detection Checks**

At every cold launch and every foreground event after background, the system shall execute the following jailbreak detection checks in sequence:

1. *File system check:* Attempt to read known jailbreak indicator paths: `/Applications/Cydia.app`, `/Applications/Sileo.app`, `/usr/sbin/sshd`, `/etc/apt`, `/var/lib/cydia`. Any readable path is a positive indicator.
2. *Sandbox escape check:* Attempt to write a temporary file to `/private/jailbreak_test.txt`. Success (no `EPERM` error) is a positive indicator.
3. *Dynamic library check:* Call `dyld_get_image_name` for all loaded dynamic libraries and check for known jailbreak library names (`MobileSubstrate`, `CydiaSubstrate`, `Substrate`).
4. *URL scheme check:* Attempt to open `cydia://` URL scheme; ability to open it is a positive indicator.

If any check returns a positive indicator, the detection result is logged as a `jailbreak_detected` event to the server audit trail (queued for upload if offline). A non-blocking warning dialog shall be displayed to the user. The business owner may enable a hard-block policy via Settings that prevents app use on a detected jailbroken device.

*Verifiability:* Install the app on a jailbroken test device (Checkra1n or Palera1n). Launch the app. The warning dialog must appear within the first app screen. The `jailbreak_detected` event must appear in the server audit trail within 30 seconds of connectivity restoration.

---

## 5.6 App Transport Security Configuration

**FR-iOS-SEC-008: ATS Policy**

The app's `Info.plist` shall not contain any `NSAppTransportSecurity` exceptions that weaken ATS requirements. Specifically:

- `NSAllowsArbitraryLoads` shall be `false`.
- `NSAllowsArbitraryLoadsForMedia` shall be `false`.
- No `NSExceptionDomains` entries shall permit cleartext HTTP or permit certificates with a minimum TLS version below TLS 1.2.

All API calls shall use HTTPS with TLS 1.3 (NFR-SEC-001). The Wasabi S3-compatible file storage endpoint shall also be accessed via HTTPS.

*Verifiability:* Inspect the production `Info.plist`; confirm `NSAllowsArbitraryLoads` is absent or `false`. Attempt to make an HTTP (not HTTPS) request from the app to any domain; it must fail with an ATS error. Use a network analyser to confirm TLS 1.3 is negotiated for all API connections.

---

## 5.7 iOS Privacy Manifest

**FR-iOS-SEC-009: Privacy Nutrition Label — Required Declarations**

The App Store Connect Privacy Nutrition Label for Maduuka iOS shall declare the following data types as collected and linked to the user's identity:

- *Contact Info:* Name, phone number, email address (collected for customer and staff profiles)
- *Financial Info:* Payment information (sale amounts, payment method types — not raw card numbers), purchase history
- *Identifiers:* User ID (JWT sub claim), device identifier (for connected devices list)
- *Usage Data:* App interaction data (for audit trail purposes)
- *Diagnostics:* Crash data (via Firebase Crashlytics, if integrated)

The following data types shall be declared as collected but *not* linked to the user's identity:

- *Location:* GPS coordinates (staff clock-in — coarse location only, not continuous tracking)

The following data type shall be declared as *not collected*:

- *Health and Fitness:* Not applicable to Maduuka.
- *Browsing History:* Not applicable.

*Verifiability:* Review the App Store Connect Privacy Nutrition Label submission prior to App Store review. Confirm all declared categories match the data types actually transmitted to the Maduuka server API or third-party SDKs (Firebase).

---

## 5.8 Required iOS Permission Strings

**FR-iOS-SEC-010: Info.plist Permission Usage Descriptions**

The app's `Info.plist` shall include the following permission usage description strings. Each string shall explain the specific use of the permission in plain language appropriate for the App Store review:

| Key | Required Value Description |
|---|---|
| `NSCameraUsageDescription` | "Maduuka uses your camera to scan product barcodes at the point of sale and to photograph expense receipts for OCR processing." |
| `NSFaceIDUsageDescription` | "Maduuka uses Face ID to protect your business data when the app resumes from background." |
| `NSBluetoothAlwaysUsageDescription` | "Maduuka uses Bluetooth to connect to 80mm thermal receipt printers. Bluetooth is used only when you initiate a receipt print." |
| `NSLocationWhenInUseUsageDescription` | "Maduuka requests your location when you clock in, so your attendance record shows the location of clock-in. Location is not tracked continuously." |
| `NSUserNotificationsUsageDescription` | "Maduuka sends notifications for low stock alerts, leave request approvals, expense approvals, and expiry date reminders." |
| `NSPhotoLibraryUsageDescription` | "Maduuka accesses your photo library to let you attach an existing photo as an expense receipt image." |

The `NSBluetoothPeripheralUsageDescription` key (deprecated since iOS 13) shall not be used; `NSBluetoothAlwaysUsageDescription` is the current required key.

*Verifiability:* Submit the app to App Store review. Confirm no App Store rejection is issued for missing or inadequate permission descriptions. Confirm each permission prompt shown to the user displays the corresponding description string.

---

## 5.9 RBAC Enforcement on iOS Client

**FR-iOS-SEC-011: Role-Based UI Restriction**

The iOS app shall enforce role-based access control at the UI layer as a usability safeguard, in addition to the server-enforced RBAC (NFR-SEC-004). The role permissions matrix from the Phase 1 SRS shall be reflected in iOS navigation:

- A Cashier-role user shall not see navigation items for HR/Payroll, Financial Reports, or Supplier Management.
- A Stock Manager-role user shall not see Payroll screens.
- The Business Owner role sees all modules.

Role restrictions shall be applied based on the `role` claim in the decoded JWT access token, which is fetched and stored in Keychain at login. If the server updates a user's role, the new role shall be effective at the next app foreground event (token refresh cycle), consistent with **FR-SET-006**.

UI-layer RBAC is a UX aid only. All data access decisions are enforced server-side per NFR-SEC-004. A Cashier who manually navigates to a restricted API endpoint (e.g., via a URL manipulation) must receive HTTP 403.

*Verifiability:* Log in as a Cashier-role user. Verify HR/Payroll, Financial Reports, and Supplier Management navigation items are absent from the tab bar and side menu. Attempt a direct API call to `GET /api/v1/reports/financial` using the Cashier JWT; the server must return HTTP 403.
