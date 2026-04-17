---
title: "SRS — Maduuka iOS Platform"
subtitle: "Section 2: iOS Platform Non-Functional Requirements"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 2: iOS Platform Non-Functional Requirements

This section defines iOS-specific non-functional requirements (NFRs). These requirements supplement the platform-neutral NFRs in `01-srs/06-nfr.md`. Where an iOS NFR sets a threshold more specific than the Phase 1 equivalent, the iOS NFR is authoritative for the iOS platform.

---

## 2.1 Performance

**NFR-iOS-001: App Launch Time**

The app shall launch to a fully interactive state (dashboard visible, Core Data stack initialised, biometric prompt shown if required) in under 2 seconds on the reference device (iPhone X, A11 Bionic, 3 GB RAM, iOS 16.0) when launched cold from the iOS home screen.

*Verifiability:* Measure `UIApplicationDidBecomeActiveNotification` timestamp minus process launch timestamp across 10 cold-launch cycles on the reference device using Xcode Instruments (Time Profiler). All 10 measurements must be ≤ 2000 ms.

---

**NFR-iOS-002: SwiftUI Render Performance**

All SwiftUI views shall render at a sustained 60 fps on the reference device under a data load of up to 500 list items in a scrollable list. Frame rate shall be measured via Xcode Instruments (Core Animation).

*Verifiability:* Load the product catalogue list view with 500 products on the reference device. Scroll continuously for 10 seconds. The Instruments trace must show zero frames exceeding 16.7 ms rendering time (frame drops) during the scroll window.

---

**NFR-iOS-003: Core Data Product Search Latency**

Core Data fetch requests for product search (name, SKU, barcode prefix match) shall return the first page of results (up to 50 items) within 500 ms on a local database containing 10,000 product records on the reference device.

*Verifiability:* Seed a test Core Data store with 10,000 products. Execute 100 search queries across varied search terms. The 95th percentile fetch-completion time (measured from the moment the `NSFetchRequest` is executed to the moment results are available on the main thread) must be ≤ 500 ms.

---

## 2.2 Offline Operation

**NFR-iOS-004: Full Offline Mode**

The app shall function in complete offline mode (no internet connectivity, airplane mode active) for the Point of Sale module (FR-POS-001 through FR-POS-029), inventory product lookup, and the dashboard KPI display using cached data. Offline mode shall activate automatically without any user action, consistent with BR-009.

*Verifiability:* Enable airplane mode on the test device. Complete 10 POS sales, perform 5 product inventory lookups, and open the dashboard. All 15 operations must complete without error dialogs or loss of data. Restore connectivity and verify all 10 sales upload to the server within 30 seconds.

---

## 2.3 Security

**NFR-iOS-005: Keychain-Only Token Storage**

JWT access tokens, refresh tokens, and all authentication credentials shall be stored exclusively in the iOS Keychain using `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`. No token or credential value shall be written to `UserDefaults`, `NSUserDefaults`, application sandbox files, or the system pasteboard.

*Verifiability:* Perform static analysis of the iOS codebase; no token write operation shall reference `UserDefaults`, `FileManager`, or `UIPasteboard` APIs. On a jailbroken test device, inspect all accessible application container directories; no token value shall be readable in plaintext.

---

**NFR-iOS-006: AES-256 Encryption at Rest**

All sensitive data stored at rest on the device — authentication tokens, business configuration, cached customer and employee data — shall be protected by AES-256 encryption via Keychain Services. The Core Data persistent store shall use SQLite WAL mode with `NSFileProtectionCompleteUnlessOpen` file protection class.

*Verifiability:* On a locked test device, use a forensic extraction tool (e.g., iMazing) to attempt to read the Core Data SQLite file. The file contents must not be interpretable as plaintext business data. Confirm the Keychain item `kSecAttrAccessible` attribute is set to `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` for all token entries.

---

**NFR-iOS-007: Certificate Pinning**

The app shall implement certificate pinning for all outbound API calls using `URLSession` delegate method `urlSession(_:didReceive:completionHandler:)`. Any API request to a host whose TLS certificate does not match the pinned leaf certificate SHA-256 hash shall be rejected. The user shall be shown a security error; the request shall not proceed.

*Verifiability:* Configure a man-in-the-middle proxy (e.g., Charles Proxy) with a custom CA certificate installed on the test device. Attempt any API call from the app. The call must fail with a certificate validation error (`NSURLErrorServerCertificateUntrusted`), not succeed with a proxied response.

---

**NFR-iOS-008: Root and Jailbreak Detection**

At every app launch, the system shall execute a jailbreak detection check. The detection shall inspect: presence of Cydia or Sileo app directories, writability of system directories outside the app sandbox, and presence of known jailbreak tool binaries. If a jailbreak is detected, the result shall be logged to the server-side audit trail and an informational warning shall be displayed to the user. The app shall remain usable after dismissing the warning (warning-only, not a hard block), unless the business owner configures a hard-block policy in Settings.

*Verifiability:* Install the app on a known-jailbroken test device. Launch the app. The audit trail must contain a jailbreak detection event with device identifier and timestamp. The warning dialog must appear before the main dashboard is accessible.

---

**NFR-iOS-009: Biometric Re-authentication After Inactivity**

When the app returns to the foreground after more than 5 minutes in the background state, the system shall require Face ID or Touch ID re-authentication via `LocalAuthentication` (`LAContext.evaluatePolicy`) before displaying any business data. The authentication timeout threshold (5 minutes) shall be configurable by the business owner in the range of 1 to 60 minutes.

*Verifiability:* Launch the app, authenticate, background the app for 6 minutes, foreground it. The biometric prompt must appear before any screen content is visible. Confirm that foregrounding after 4 minutes (below the threshold) does not trigger the prompt.

---

## 2.4 Background Operation

**NFR-iOS-010: Background Sync Frequency**

The app shall register a `BGAppRefreshTask` to attempt a pending-queue sync every 15 minutes when the OS grants background execution time. The task shall complete all sync operations and call `BGTask.setTaskCompleted(success:)` within 30 seconds to comply with Apple's background execution limits.

*Verifiability:* Simulate background task execution using the Xcode debug menu (`BGTaskScheduler` simulation). Verify the sync task completes and calls `setTaskCompleted(success: true)` within 30 seconds. Confirm that pending queue items created during offline operation are uploaded when the background task fires.

---

## 2.5 Accessibility

**NFR-iOS-011: Dynamic Type Support**

All text in the app shall scale correctly with the system Dynamic Type size setting, from `UIContentSizeCategory.extraSmall` to `UIContentSizeCategory.accessibilityExtraExtraExtraLarge`. No text shall be truncated, overlapped, or hidden at any Dynamic Type size.

*Verifiability:* Set the device accessibility text size to the maximum (`accessibilityExtraExtraExtraLarge`) in iOS Settings. Navigate through all primary screens (Dashboard, POS, Inventory list, Customer list, HR, Reports). All visible text must be legible and no UI element must overlap or clip adjacent elements.

---

**NFR-iOS-012: Dark Mode Contrast**

The app shall support iOS Dark Mode. All foreground-background colour pairs shall meet WCAG 2.1 Level AA contrast ratio (≥ 4.5:1 for normal text, ≥ 3:1 for large text). No white-on-white or black-on-black text/background combination shall appear in any SwiftUI view in either light or dark appearance mode.

*Verifiability:* Switch the device to Dark Mode. Navigate all screens. Use Xcode Accessibility Inspector to measure contrast ratios for a representative set of 20 text/background pairs. All measurements must be ≥ 4.5:1 for body text and ≥ 3:1 for text at 18pt or larger.

---

## 2.6 API Compatibility

**NFR-iOS-013: Shared API Endpoints**

The iOS app shall consume the identical REST API endpoints as the Android and Web clients. No iOS-specific endpoints, iOS-specific response fields, or iOS-specific query parameters shall be created on the server. All platform differentiation shall be handled in the iOS client layer.

*Verifiability:* Compare the iOS network layer request URLs against the Android and Web network layer request URLs. The base path, endpoint names, and required parameters must be identical across all three clients for every module.
