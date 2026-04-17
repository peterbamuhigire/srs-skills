---
title: "SRS Phase 2a — Restaurant/Bar Add-on Module (F-011)"
subtitle: "Section 5: Constraints"
project: Maduuka
version: "0.1-draft"
date: 2026-04-05
---

# Section 5: Constraints

## 5.1 Licensing and Subscription Constraints

**CON-RES-001:** F-011 is a paid add-on at UGX 30,000 per month per tenant. The system shall not activate F-011 features on a tenant's account unless the active subscription includes the F-011 entitlement. Feature access shall be revoked within 24 hours of subscription expiry or cancellation of the add-on.

**CON-RES-002:** F-001 (Point of Sale) and F-002 (Inventory and Stock Management) must be active Phase 1 modules on the tenant account. F-011 shares the payment processing engine of F-001 and the stock management engine of F-002. If F-001 or F-002 is suspended on the tenant account, F-011 shall be suspended concurrently and the tenant notified.

## 5.2 Device and Browser Constraints

**CON-RES-003:** The Kitchen Display System (KDS) requires a dedicated display device running a Chromium-based browser at version 90 or later (e.g., Google Chrome 90+, Microsoft Edge 90+). The KDS web view is optimised for landscape orientation at a minimum resolution of 1024 × 600 pixels. Safari is supported but is not the reference browser for KDS testing.

**CON-RES-004:** After a kitchen display device completes initial login per FR-RES-035, the KDS session shall remain active without requiring re-authentication for normal kitchen operations. This is a deliberate design constraint reflecting the shared-screen nature of kitchen display hardware. Each KDS device must complete initial login with valid credentials before this constraint applies.

**CON-RES-005:** The floor plan designer uses a browser-based drag-and-drop canvas. It requires a pointer device (mouse or trackpad). The floor plan designer is not supported on touch-only devices (iOS Safari, Android Chrome) due to the precision required for table placement. Table status board consumption on iOS is fully supported.

## 5.3 Platform Scope Constraints

**CON-RES-006:** Android support for F-011 is not in scope for Phase 2a. Android parity for table management, KOT entry, and bar tab management is a separate delivery track and will be addressed in a subsequent phase increment. The Phase 1 Android application shall not display F-011 menu items to tenants with F-011 active.

**CON-RES-007:** The iOS implementation of F-011 supports KOT entry, table status board (read-only floor plan view), and bar tab management. The KDS on iOS is delivered as a browser web view rather than a native screen, using the same web KDS URL. iOS-native KDS controls (mark done, mark complete) shall be accessible from within the web view.

## 5.4 Integration and Phase Constraints

**CON-RES-008:** F&B charge posting to hotel room accounts (F-013) is not implemented in Phase 2a. The F-011 bill settlement flow does not include a "Post to Room" payment option. The data model shall reserve a nullable `room_account_id` field on the F-011 bill record for the Phase 3 integration, but the field shall not be exposed in the Phase 2a user interface.

**CON-RES-009:** EFRIS fiscal document generation for F-011 bills is deferred pending resolution of [CONTEXT-GAP: GAP-010]. F-011 bills in Phase 2a shall apply the tenant's standard tax configuration (FR-SET-003) and shall not generate URA Fiscal Document Numbers (FDNs). This constraint shall be lifted when GAP-010 is resolved and the F-015 EFRIS module is extended to cover F-011.

## 5.5 Data and Audit Constraints

**CON-RES-010:** All KOT records, BOM deduction movements, bar tab records, and billing records are subject to the audit trail requirement (BR-003) and the stock movement immutability requirement (BR-004). No user interface action within F-011 shall permit deletion or in-place modification of a confirmed KOT, BOM deduction movement, settled bar tab, or paid bill.

**CON-RES-011:** All F-011 data is scoped by `franchise_id` per BR-001. Table definitions, KOTs, BOMs, floor plans, and bar tabs created by one tenant are never accessible to another tenant, regardless of shared infrastructure.
