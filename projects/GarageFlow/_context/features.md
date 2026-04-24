# Features — GarageFlow

Canonical feature inventory from the source specification (23 April 2026). Modules marked **[MVP]** are phase 1; **[P2]** is phase 2; **[ADD-ON]** is a paid add-on.

## Garage Manager App

### Operations

- [MVP] Appointment booking and calendar.
- [MVP] Check-in with plate / VIN scan and mileage capture.
- [MVP] Bay assignment and live bay board (tablet-mounted).
- [MVP] Job card state machine (booked → closed, with warranty-return branch).
- [MVP] Job status history audit log.
- [MVP] Walk-in flow.
- [P2] Multi-day job daily snapshot.

### Inspection

- [MVP] Digital multi-point inspection with tenant-editable templates.
- [MVP] Measurement-typed checkpoints (pass/fail, mm, psi, percent, etc.).
- [MVP] Traffic-light severity mapping (green / amber / red).
- [MVP] Photo evidence capture with SHA-256 integrity.
- [MVP] Manual DTC entry (OBD-II adapter stub reserved).
- [P2] Bluetooth OBD-II integration.
- [P2] AI-assisted classification (tyre tread, brake pad wear, corrosion).

### Customer & vehicle CRM

- [MVP] Customer record (individual and fleet).
- [MVP] Vehicle record with VIN decode, plate, ownership transfer audit.
- [MVP] Service history per vehicle.
- [MVP] Communication preferences.

### Estimates, approvals, invoicing

- [MVP] Estimate composition from inspection recommendations and service catalogue.
- [MVP] Customer digital approval (in-app, email-click, signed image, recorded verbal).
- [MVP] Approval artifact immutability.
- [MVP] Invoice issuance with itemised labour, parts, tax, shop supplies.
- [MVP] Warranty statement block on invoice.
- [ADD-ON] EFRIS e-invoicing (Uganda) at USD 30/month.
- [P2] ZATCA, KRA eTIMS, RRA EBM, CFDI adapters.

### Parts & inventory

- [MVP] Tenant-scoped parts catalogue with barcodes and fitment tags.
- [MVP] Multi-branch stock-on-hand.
- [MVP] Reservation vs issue semantics tied to job cards.
- [MVP] Purchase orders and supplier receipts.
- [MVP] FIFO / weighted-average / standard-cost valuation (tenant choice).
- [MVP] Cycle counting with variance workflow.
- [MVP] Cross-branch transfer.
- [P2] Core-charge handling for remanufactured parts.
- [P2] Chain-of-custody for security-relevant parts.

### Accounting (native)

- [MVP] Chart of accounts (tenant-configurable, seeded by service-type template).
- [MVP] Double-entry journal.
- [MVP] Real-time-async GL posting from invoices, payments, inventory, payroll.
- [MVP] Trial balance, P&L, balance sheet, cash-flow statement.
- [MVP] Period close.
- [MVP] Bank reconciliation.
- [MVP] Multi-currency.
- [MVP] Tax configuration per jurisdiction.

### Payroll

- [MVP] Staff records, pay structures, overtime rules.
- [MVP] Technician productivity link (billable hours from clock-on/clock-off vs clocked hours).
- [MVP] Pay run with GL posting.
- [MVP] Statutory deductions (configurable per jurisdiction).

### Technician productivity

- [MVP] Clock-on / clock-off per job.
- [MVP] Billable vs non-billable hours.
- [MVP] Productivity dashboard per technician and per branch.

### Quality control

- [MVP] QC checklist per job.
- [MVP] QC failure flow back to in-progress.

### Analytics

- [MVP] Owner dashboard (revenue, jobs, customer retention, inventory turn).
- [MVP] Branch manager dashboard.
- [MVP] Service advisor dashboard (estimate approval rate).
- [MVP] Technician dashboard (productivity, inspection findings rate).

### Fleet / corporate

- [MVP] Corporate invoice accounts with purchase orders.
- [MVP] Statement billing per period.
- [ADD-ON] Advanced fleet management at USD 49/month (driver, fuel, mileage, renewals, cost-per-km).
- [P2] Insurance claim workflow (damage map, assessor scheduling, insurer-specific invoice format).
- [P2] Body-shop damage-panel assessment.
- [P2] OEM dealer module (warranty claim, service intervals, OEM reporting).

### Marketing & retention (tenant-operated)

- [MVP] Scheduled maintenance reminders (within quiet window plus 30-day cadence limit).
- [MVP] Post-service follow-up and review request.

### Administration (tenant)

- [MVP] Branch configuration.
- [MVP] User and role management.
- [MVP] Service catalogue with labour rate templates (general workshop, tyre centre, body shop, quick-fit).
- [MVP] Tax settings.
- [MVP] Notification templates.

## Garage Customer App

- [MVP] Phone / email sign-up with OTP verification.
- [MVP] Link vehicle by plate or VIN.
- [MVP] Book appointment (branch + service + time slot).
- [MVP] Live job status timeline with push notifications.
- [MVP] View inspection report with photos and plain-language explanations.
- [MVP] Per-line approve / decline recommendations.
- [MVP] Receive and pay invoice (saved card token or mobile money push).
- [MVP] Service history viewer per vehicle.
- [MVP] Invoice PDF export.
- [MVP] Service record PDF export (right-to-repair portability).
- [MVP] Maintenance reminders (monthly cadence maximum).
- [MVP] Offline reading of cached invoices, inspection reports, service history.
- [P2] Multi-tenant account linking (same human across multiple garages).
- [P2] White-label rendering (tenant logo and colour scheme post-login).
- [P2] Fleet manager consolidated view.

## Super Admin Panel (Chwezi-side)

- [MVP] Tenant provisioning and suspension.
- [MVP] Subscription plan and add-on management.
- [MVP] Feature toggles.
- [MVP] Platform health monitoring.
- [MVP] Support impersonation with ticket plus reason plus audit.
- [MVP] Billing and invoicing of tenants.
- [P2] Channel-partner management (if go-to-market decision lands on partners).

## Shared platform capabilities

- [MVP] Multi-tenant SaaS with service-layer tenant scoping.
- [MVP] Role-based access control with branch scoping.
- [MVP] Offline-first mobile with conflict-safe sync (scope per NFR-AUTO-002).
- [MVP] Barcode scanning via device camera (ML Kit / Vision).
- [MVP] Camera-first photo capture with geotag plus timestamp plus hash.
- [MVP] Push notifications as an operational tool (actionable).
- [MVP] Multi-language (English at launch; languages added as localisation add-on per tenant).
- [MVP] Multi-currency.
- [MVP] Payment gateway envelope (Stripe plus mobile money rails).
