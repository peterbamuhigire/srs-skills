# Automotive — Architecture Patterns

## Multi-Tenant, Multi-Branch Model

A single tenant represents one garage business. A tenant owns one or more branches. Every operational entity (job card, vehicle, customer, invoice, stock item, journal entry) carries both `tenant_id` and `branch_id`. Service-layer scoping MUST derive `tenant_id` from the authenticated session token, NEVER from request parameters. Cross-branch reads within a tenant are permitted only when the user role explicitly grants them.

## Job Card State Machine

```
booked -> arrived -> checked-in -> inspecting -> estimated
      -> awaiting-approval -> approved -> in-progress
      -> qc -> completed -> invoiced -> paid -> closed
                                     \-> warranty-return -> in-progress
```

Invariants:

- No state may be skipped except via an administrator-authorised override, which writes an override-reason record.
- Transition from `awaiting-approval` requires an approval artifact (see Regulations — Consumer Protection).
- `in-progress` cannot be entered before `approved` unless the scope is inspection-only.
- `closed` is terminal except for warranty-return, which reopens a derivative job card referencing the original.

## Offline-First Mobile Sync

Two classes of data:

1. **Operationally critical** (must work offline): job cards assigned to the logged-in technician, active inspections, parts catalogue with on-hand per branch, personal time-clock state, customer vehicle lookup for today's appointments.
2. **Server-authoritative** (online required): GL postings, invoice issuance to e-invoicing authority, payment capture, payroll run, inventory valuation close, cross-branch transfers.

Client-side: Room (Android) / SwiftData or Core Data (iOS) with a mutation queue. Each queued mutation carries a client-generated UUID as idempotency key. Server resolves conflicts with last-writer-wins per field for status fields and reject-on-conflict for monetary fields.

## Parts Reservation vs Issue

Estimate approval creates a **reservation** on the parts ledger — quantity is held but not yet consumed. Technician issue at the workshop converts reservation to **issue** — quantity decrements stock-on-hand and becomes costable to the job. Returns reverse either reservation or issue depending on state. Reservations auto-expire on job cancellation or time-out.

## Payment Tokenization Envelope

The platform defines a `PaymentInstrument` record with shape `{tenant_id, customer_id, gateway, token, brand, last4, expiry, default}`. No raw card data transits the application layer. Webhook-driven confirmations reconcile payment intents to invoices; the reconciliation worker is idempotent on `(gateway, payment_intent_id)`.

## OBD-II Integration Envelope

Even at MVP, the mobile API MUST reserve a DTC capture surface:

- `POST /jobs/{id}/dtc` — accepts a list of DTC codes, description, severity, captured-at, source (`manual` | `obd-bt` | `obd-wifi`), vehicle mileage at capture.
- Mobile clients treat this as a drop-in extension point; manual entry is the MVP source, Bluetooth OBD a Phase-2 source.

## White-Label Customer App Strategy

The recommended pattern is a **single multi-tenant Customer App** (one App Store + one Play Store submission) whose theme (logo, primary colour, wordmark, legal footer) is hydrated per tenant after login. Enterprise-plan tenants that demand their own listing MUST be served via a per-tenant build pipeline generating distinct bundle IDs — this option increases maintenance cost (one submission per tenant) and MUST be scoped as a separate architectural track.

## Real-Time vs Batch GL Posting

Recommended pattern: **real-time-async**. On invoice or payment commit, emit a GL posting job onto a durable queue with the invoice as correlation key. A worker posts the journal entry within 60 seconds. The user-facing financial statement endpoints read from committed journals only. This gives the UX of real-time posting without synchronous DB contention at sale time. Batch reconciliation runs at day-end to detect any unposted jobs and raise an alert.

## Mobile-First, Web-Complete

Every operational screen must exist on Android, iOS, and web. Mobile is the primary surface for technicians and service advisors moving around; web is the primary surface for back-office roles (accountant, payroll officer, owner dashboards). Feature parity is required for functions performed by a role that uses both surfaces (e.g. service advisor).

## Tenant Isolation Enforcement

- Database: every operational table has a non-nullable `tenant_id`; queries route through a tenant-scoped repository that injects the predicate automatically. Direct SQL is prohibited in application code.
- Object storage: paths namespaced under `/tenants/{tenant_id}/`. Signed URLs expire in ≤ 10 minutes.
- Queues: message envelopes carry `tenant_id`; worker dispatch rejects mismatches.
- Super-admin impersonation: requires a ticket reference and reason; writes an impersonation session record; all actions during impersonation are double-logged (actor = super-admin, target-tenant = X).
