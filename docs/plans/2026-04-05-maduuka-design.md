# Maduuka — Project Design Document

**Date:** 2026-04-05
**Owner:** Peter Bamuhigire · Chwezi Core Systems · chwezicore.com · +256784464178
**Methodology:** Hybrid (Water-Scrum-Fall) — formal requirements sign-off per phase, iterative delivery within phases
**Team size:** 2-5 people
**Spec source:** `C:\Users\Peter\Downloads\maduuka_spec.docx`

---

## 1. Product Summary

Maduuka (Swahili: shops/stores) is a mobile-first SaaS business management platform for Ugandan and African small businesses — from a single butcher stall in Owino Market to a multi-branch pharmacy chain or a hotel in Fort Portal. One app, one subscription, one place to run any business.

**Core value proposition:** Replace pirated Windows POS software and exercise-book bookkeeping with a subscription that costs less than a monthly airtime top-up, works on any Android phone, never loses data, and provides EFRIS compliance when needed.

**Primary target market:** Uganda. **Secondary:** Pan-Africa. **Currency:** UGX primary, Africa-configurable.

**Branding:** Chwezi Core Systems product. No Byoosi.com association. No MLM module — ever.

---

## 2. Architecture

### 2.1 Platform Stack

| Layer | Technology |
|---|---|
| Android (Phase 1) | Kotlin + Jetpack Compose, MVVM + Clean Architecture, Room, Hilt, WorkManager, CameraX + ML Kit |
| iOS (Phase 2) | Swift + SwiftUI, MVVM + Clean Architecture, Core Data, identical feature parity — not a port |
| Web (Phase 1) | PHP 8.3+, Bootstrap 5 / Tabler UI, responsive, PWA-enabled |
| Backend API | Single REST API consumed by all three clients — no platform-specific endpoints |
| Authentication | JWT (mobile): 15-min access token + 30-day refresh token. Session + CSRF (web) |

### 2.2 Multi-Tenancy

Every database table carries a `franchise_id` column. Every API query is scoped to that identifier at the service layer — cross-tenant data access is architecturally impossible. Hierarchy: Platform → Business (tenant) → Branches → Warehouses / Floors / Room blocks.

Support access goes through a logged, audited impersonation mechanism — every support session recorded with timestamp, reason, and actions taken.

### 2.3 Offline-First Strategy

- Android: Room (SQLite) caches products, customers, payment methods, pending transactions
- iOS: Core Data (SQLite) — identical cache scope
- Failed writes queue locally and replay automatically on reconnect
- Background sync: WorkManager (Android) / BackgroundTasks (iOS) — every 15 minutes
- Sync status indicator on dashboard showing last sync time and pending local changes
- Web: PWA caches critical assets; bridges iOS users until the Phase 2 native iOS app ships

### 2.4 Security

- TLS 1.3 for all data in transit
- Passwords hashed with bcrypt — never stored in plain text
- Encrypted local storage: AES-256-GCM (Android EncryptedSharedPreferences), AES-256 Keychain (iOS)
- Certificate pinning on mobile — prevents API interception on compromised networks
- Biometric re-authentication on app resume (BiometricPrompt / Face ID / Touch ID)
- Root/jailbreak detection at app launch
- Immutable audit log: every create, edit, delete, void, adjustment, and payment recorded with actor, timestamp, device, and IP — cannot be deleted through any UI
- RBAC enforced at every API endpoint — not just at UI layer

---

## 3. Phase Structure

### Phase 1 — Android + Web, All 10 Core Modules

| # | Module |
|---|---|
| 1 | Point of Sale (POS) |
| 2 | Inventory & Stock Management |
| 3 | Customer Management |
| 4 | Supplier & Vendor Management |
| 5 | Expenses & Petty Cash |
| 6 | Financial Accounts & Cash Flow |
| 7 | Sales Reporting & Analytics |
| 8 | HR & Payroll |
| 9 | Dashboard & Business Health |
| 10 | Settings & Configuration |

Both Android and Web ship all 10 core modules simultaneously. No feature gating between platforms within Phase 1.

### Phase 2 — iOS Parity + Restaurant/Bar + Pharmacy

- All 10 core modules on iOS (Swift/SwiftUI, Core Data) — identical feature parity with Android
- **Restaurant/Bar add-on:** table management, KOT, Kitchen Display System, bar tabs, Bill of Materials, restaurant reports
- **Pharmacy add-on:** patient management, prescription tracking, drug reference database, controlled drugs register, FEFO dispensing, NDA Uganda compliance log, allergy alerts, basic drug interaction warnings (category-level only, with disclaimer — not a clinical decision support system)

### Phase 3 — Hotel/Accommodation + Advanced Inventory + EFRIS

- **Hotel/Accommodation add-on:** room management, reservations, check-in/out, housekeeping, F&B posting to room account, corporate accounts, conference room booking
- **Advanced Inventory add-on:** multi-warehouse, serial/batch traceability, landed cost allocation, BOM + production orders, demand forecasting, compliance audit report
- **EFRIS compliance add-on:** URA system-to-system API, Fiscal Document Number generation, QR code on receipts, offline transaction queuing, monthly reconciliation report

### Phase 4 — Africa Expansion & Integrations

- Additional languages: French, Arabic, Luganda (English and Swahili ship in Phase 1)
- Additional mobile money gateways: M-Pesa (Kenya/Tanzania), Flutterwave, Paystack
- BrightSoma / Academia Pro integration: canteen POS, school shop management, supplier payments
- Hotel channel manager integration: Booking.com, Airbnb (via third-party channel manager — data model designed from Phase 1 to accommodate external reservations)

### Permanently Out of Scope

- MLM / distributor network module — will never be built

---

## 4. Business Groups & User Roles

### 4.1 Business Groups

| Group | Industries | Core Modules | Add-on |
|---|---|---|---|
| General merchants | Retail shops, supermarkets, hardware, kiosks, butchers, wholesalers, market traders | All 10 core | Advanced Inventory (optional) |
| Restaurants & bars | Restaurants, cafés, bars, nightclubs, fast food, canteens | All 10 core | Restaurant/Bar module |
| Pharmacies & drug stores | Pharmacies, drug stores, clinic dispensaries, vet drug shops | All 10 core | Pharmacy module |
| Accommodation | Hotels, lodges, guesthouses, Airbnb, serviced apartments, conference centres | All 10 core | Hotel/Accommodation module |

### 4.2 User Roles

Platform Admin, Business Owner, Branch Manager, Cashier/POS Operator, Stock/Inventory Manager, Accountant, HR Manager, Waiter/Server (restaurant), Kitchen Staff (restaurant), Front Desk (hotel), Pharmacist (pharmacy), Customer (portal — read-only via magic link).

---

## 5. Subscription Pricing

| Plan | Price (UGX/month) | Users | Branches | Products |
|---|---|---|---|---|
| Basic | 30,000 | 2 | 1 | 100 |
| Business | 80,000 | 10 | 3 | 1,000 |
| Pro | 180,000 | Unlimited | Unlimited | Unlimited |
| Enterprise | Custom | Unlimited | Unlimited | Unlimited |

All plans include all core modules, Android + iOS apps, web interface, offline mode, and mobile money payments. Industry add-ons charged separately: Restaurant/Bar +30K/mo, Pharmacy +30K/mo, Hotel +50K/mo, Advanced Inventory +25K/mo, EFRIS +40K/mo.

Annual discount: 10 months paid, 12 months access (2 months free).

---

## 6. Key Design Decisions

| Decision | Resolution |
|---|---|
| Offline strategy | Offline-first on mobile; PWA bridges iOS until Phase 2 native app |
| Customer portal access | Magic link via WhatsApp/SMS — no login required (simpler, appropriate for Uganda market) |
| Drug interaction checking | Basic category-level warnings + prominent disclaimer — not a clinical decision support system |
| MLM module | Permanently excluded — will never be built |
| Multi-business group pricing | Decision deferred — required before Phase 2 SRS (one account for multiple separate businesses) |
| iOS thermal printing | Verify 3 Uganda-market printer models against iOS Core Bluetooth before Phase 2 build begins |

---

## 7. High-Priority Gaps (resolve before Phase 1 development)

| Gap | Action Required |
|---|---|
| MTN MoMo Business API | Obtain Business API docs and sandbox credentials from MTN Uganda — required for POS push payment |
| Data Protection Act 2019 review | Legal review of customer, employee, patient, and guest data handling — required before Phase 2/3 modules |

**Resolve before Phase 3 development:**

| Gap | Action Required |
|---|---|
| EFRIS API accreditation | Register as URA system-to-system partner — multi-week process, start early (efris@ura.go.ug) |
| NDA Uganda drug codes | Obtain approved drug list and classification codes from NDA Uganda for pharmacy module |
| iOS thermal printing compatibility | Test Xprinter, Epson, TP-Link against iOS Core Bluetooth / Raw Print protocol |

---

## 8. Domain Classification

Multi-domain SRS: **Retail/Commerce** (core + general merchants) + **Hospitality** (restaurant/bar + hotel) + **Healthcare** (pharmacy). Domain files: `domains/retail/`, `domains/hospitality/`, `domains/healthcare/`.

---

*Confidential product design — Chwezi Core Systems · 2026-04-05*
