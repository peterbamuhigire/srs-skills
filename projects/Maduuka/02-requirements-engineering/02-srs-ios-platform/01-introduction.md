---
title: "SRS — Maduuka iOS Platform"
subtitle: "Section 1: Introduction"
version: "1.0"
date: "2026-04-05"
status: "Draft"
---

# Section 1: Introduction — Maduuka iOS Platform Software Requirements Specification

## 1.1 Purpose

This document specifies the Software Requirements Specification (SRS) for the Maduuka iOS platform. It defines iOS-specific implementation constraints, platform capabilities, and functional requirements for all 10 Phase 1 core modules as they are delivered on iPhone running iOS 16.0 or later.

This document is a supplement to, not a replacement of, the Phase 1 SRS (`02-requirements-engineering/01-srs/`). Every requirement in the Phase 1 SRS — **FR-POS-001** through **FR-SET-012** (129 functional requirements) — applies in full to the iOS platform unless an explicit iOS-specific override appears in this document. Where this document conflicts with the Phase 1 SRS on an iOS-specific point, this document is authoritative.

## 1.2 Scope

### 1.2.1 In Scope

- iOS-native implementation of all 10 Phase 1 core modules:
  - **F-001** Point of Sale
  - **F-002** Inventory and Stock Management
  - **F-003** Customer Management
  - **F-004** Supplier and Vendor Management
  - **F-005** Expenses and Petty Cash
  - **F-006** Financial Accounts and Cash Flow
  - **F-007** Sales Reporting and Analytics
  - **F-008** HR and Payroll
  - **F-009** Dashboard and Business Health
  - **F-010** Settings and Configuration
- iOS-specific platform constraints (Section 2)
- iOS-specific functional requirements layered on Phase 1 FRs (Section 3)
- Offline sync contract for Core Data (Section 4)
- iOS security requirements (Section 5)
- Distribution via Apple App Store

### 1.2.2 Out of Scope

- Phase 2 industry add-on modules (Restaurant/Bar — F-011; Pharmacy — F-012): iOS parity for these modules is deferred to Phase 2.
- Phase 3 modules (Hotel — F-013; Advanced Inventory — F-014; EFRIS — F-015): out of scope for this document.
- macOS Catalyst or iPad-specific layouts: see Section 1.5.
- Android and Web platform requirements: governed by the Phase 1 SRS.

## 1.3 Relationship to Phase 1 SRS

The Phase 1 SRS (`01-srs/`) was written for Android and Web. The iOS platform is required to satisfy all 129 Phase 1 functional requirements and all non-functional requirements in `01-srs/06-nfr.md` that are not platform-exclusive (Android WorkManager, OkHttp CertificatePinner, Room database, and Android-specific references are replaced by their iOS equivalents defined in this document).

The mapping principle is:

| Phase 1 (Android) | Phase 2 (iOS) |
|---|---|
| Room (SQLite) | Core Data (SQLite) |
| WorkManager | BGAppRefreshTask / BGProcessingTask |
| EncryptedSharedPreferences | Keychain Services |
| OkHttp CertificatePinner | URLSession delegate certificate validation |
| BiometricPrompt | LocalAuthentication (Face ID / Touch ID) |
| ML Kit barcode | AVFoundation + Vision framework |
| FCM push | APNs via Firebase Cloud Messaging |
| Leaflet.js (WebView) | MapKit (native) |
| Android share sheet | iOS UIActivityViewController (share sheet) |

## 1.4 Deployment Target

- *Minimum iOS version:* iOS 16.0
- *Swift version:* Swift 5.9 or later
- *UI framework:* SwiftUI
- *Architecture:* MVVM + Clean Architecture (Presentation / Domain / Data layers)
- *Distribution channel:* Apple App Store (primary); TestFlight for internal and beta testing

### 1.4.1 Minimum Reference Device

Design Covenant DC-004 mandates that the app runs without frame drops below 60 fps on an iPhone X (A11 Bionic, 3 GB RAM, iOS 16). All performance requirements in Section 2 use this device as the baseline test configuration.

## 1.5 iPad Support

[CONTEXT-GAP: iPad support scope] The stakeholder has not confirmed whether Maduuka iOS Phase 2 must deliver an iPad-optimised layout (split view, sidebar navigation, larger canvas POS). iPhone is the primary target device. iPad compatibility (running the iPhone layout scaled) is acceptable as a default App Store behaviour unless the stakeholder explicitly requests an iPad-native layout. This gap must be resolved before App Store submission to set the correct device capability flag in `Info.plist`.

## 1.6 Document Conventions

- All functional requirements follow IEEE 830 stimulus-response format: "When [stimulus], the system shall [response]."
- "The system shall" denotes a mandatory requirement.
- Requirement identifiers follow the pattern `FR-iOS-[MODULE]-[NNN]` for iOS-specific requirements and `NFR-iOS-[NNN]` for iOS-specific non-functional requirements.
- Phase 1 requirement identifiers (e.g., `FR-POS-001`) are referenced without the `iOS` infix when citing requirements that carry over unchanged.

## 1.7 Applicable Standards and References

- IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications
- IEEE Std 610.12-1990: Glossary of Software Engineering Terminology
- IEEE Std 1233-1998: Guide for Developing System Requirements Specifications
- Apple Human Interface Guidelines (HIG) — iOS
- Apple App Store Review Guidelines 4.0 (Privacy)
- Apple Privacy Nutrition Label requirements (App Store Connect)
- ASTM E1340: Standard Guide for Rapid Prototyping of Computerized Systems
- Maduuka Phase 1 SRS (`02-requirements-engineering/01-srs/`)
- Maduuka Gap Analysis (`_context/gap-analysis.md`) — see GAP-004 (iOS Bluetooth printer compatibility)
