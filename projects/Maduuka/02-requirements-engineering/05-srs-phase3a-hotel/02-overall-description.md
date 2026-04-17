# 2. Overall Description

## 2.1 Product Perspective

F-013 is a module that extends the Maduuka multi-tenant SaaS platform. It shares the same tenant isolation model (BR-001), audit trail infrastructure (BR-003), payment account definitions (F-006), and multi-payment engine (BR-010) established in Phase 1. No new authentication or multi-tenancy layer is introduced; F-013 operates within the existing role-based access control framework.

The module introduces a property-management layer above the existing product/inventory layer. A property is scoped to a single Maduuka business (tenant). A tenant may have multiple properties if they operate more than one accommodation site; each property maintains its own room inventory, reservations, and folios.

## 2.2 Prerequisites and Dependencies

### 2.2.1 Mandatory Prerequisites

F-013 requires the following Phase 1 modules to be active and correctly configured before activation:

- **F-001 (POS)** — Payment collection at checkout uses the POS payment engine.
- **F-003 (Customer Management)** — Corporate account billing maps to the customer credit account model.
- **F-006 (Financial Accounts)** — Room revenue posts to the business's configured payment accounts.
- **F-010 (Settings and Configuration)** — Business profile, SMS gateway (Africa's Talking), and currency settings are consumed by F-013.

### 2.2.2 Recommended Integration

- **F-011 (Restaurant/Bar Module)** — When active alongside F-013, enables waitstaff to post food and beverage charges directly to an occupied room's folio from the restaurant order screen. F-013 functions without F-011; if F-011 is absent, F&B charges may still be posted manually to a folio by front desk staff.

### 2.2.3 Deferred Integrations

- **GAP-007 — Channel Manager** — Integration with OTA channel managers (Booking.com, Airbnb, Expedia) is deferred to Phase 4. The Phase 3 data model includes a `booking_source` field (VARCHAR, not null, default `'walk-in'`) on the reservations table. Permitted Phase 3 values: `walk-in`, `phone`. Phase 4 will extend the permitted value set without a schema migration.

## 2.3 User Classes and Characteristics

| User Class | Description | Typical Interaction |
|---|---|---|
| Business Owner | Tenant administrator; full access to all F-013 functions including configuration, analytics, and corporate accounts | Property setup, seasonal pricing, analytics review, corporate billing |
| Front Desk Staff | Handles reservations, check-in, check-out, folio posting, and room status updates | Daily operational flow; no access to property configuration or analytics |
| Housekeeping Staff | Views assigned cleaning tasks; marks rooms as clean | Mobile-first; limited read access to room status board |
| Maintenance Staff | Flags rooms for maintenance; marks maintenance complete | Mobile-first; limited write access to room status only |
| Accountant | Reviews folios, corporate invoices, and financial reports; no operational check-in/check-out capability | Reporting, corporate billing, revenue reconciliation |

## 2.4 Platform and Deployment

F-013 is deployed across 3 platforms in the following sequence:

1. **Web (Phase 3)** — Full-featured browser application; primary platform for property setup, reservations, room status board, analytics, and corporate accounts.
2. **Android (Phase 3)** — Mobile application providing front desk, housekeeping, and maintenance workflows.
3. **iOS (Phase 3)** — iOS parity build; invoice PDF generation uses PDFKit on-device.

The room status board requires WebSocket (or equivalent long-polling fallback) connectivity to deliver real-time status propagation within 2 seconds (NFR-HTL-001).

## 2.5 Assumptions and Dependencies

- The property operates in Uganda Shillings (UGX) by default; the currency setting from F-010 governs the display symbol.
- Standard check-in and check-out times are configurable per property (not hardcoded).
- SMS confirmation via Africa's Talking is available; if the gateway is unavailable, reservation creation succeeds and the SMS is queued for retry.
- A maximum of 200 individual rooms per property is the tested scale for Phase 3 (see Section 5).
- Guest ID document photos are stored in the tenant's cloud storage bucket, subject to Uganda Data Protection and Privacy Act 2019 (GAP-002).
