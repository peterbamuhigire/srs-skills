# Feature: Workshop Operations

## Purpose

Coordinate the flow of every vehicle through the garage from check-in to close. The workshop-operations module is the operational spine to which inspection, parts, invoicing, payroll, and customer-notification modules attach.

## Core Entities

- **Job Card** — the unit of work. Has `tenant_id`, `branch_id`, `vehicle_id`, `customer_id`, `service_advisor_id`, `assigned_technician_id[]`, `bay_id`, `status`, `opened_at`, `closed_at`, `priority`.
- **Bay** — a physical workshop position. Has `branch_id`, `name`, `type` (lift, flat, alignment, paint, valet), `capability_tags[]`.
- **Appointment** — planned job-card precursor. Has time window, service codes requested, vehicle, customer, confirmation channel.
- **Job Status History** — append-only audit of every state transition with actor, timestamp, and reason.

## State Machine

See `references/architecture-patterns.md` — "Job Card State Machine."

## Key Workflows

1. **Appointment → check-in.** Customer arrives; service advisor scans plate or VIN or selects the appointment; vehicle is assigned to a bay; initial mileage recorded; customer contact preferences confirmed.
2. **Inspection → estimate.** Technician runs the digital inspection (see `vehicle-inspection.md`); findings generate recommended service lines; service advisor composes the estimate.
3. **Approval capture.** Customer approves via the Customer App, by a one-tap email link, by a signed image on the advisor's tablet, or by recorded verbal consent. The approval record is immutable.
4. **Work execution.** Technician clocks on to the job, issues parts as consumed, marks sub-tasks done, captures before/after photos.
5. **Quality control.** Branch manager or designated QC technician reviews; failed QC returns the job to in-progress with reason.
6. **Invoice and close.** Service advisor generates invoice; customer pays in-app, in-branch, or on corporate account; job closes; thank-you and follow-up notifications scheduled.

## Bay Board

The bay board is a live tablet-mounted view of every bay in a branch, refreshing every 15 seconds or on push. Each tile shows: bay name, current job card (or "free"), assigned technician, elapsed time, status, and colour-coded urgency. The controller uses the bay board to drag-drop new jobs onto free bays.

## Multi-Branch Coordination

A job card belongs to a single branch, but vehicles, customers, and staff records are tenant-scoped and visible across branches subject to role permissions. A vehicle serviced at Branch A carrying over to Branch B retains its full history.

## Interfaces To Other Modules

- **Inspection:** a job card has zero or one inspection reports.
- **Parts:** reservations and issues are linked to a job card.
- **Estimate and Invoice:** line items reference job card work orders.
- **Technician productivity:** clock-on/clock-off records roll up per technician per job.
- **Customer App:** live status notifications are emitted on every state transition whose `customer_visible` flag is true.

## Non-Functional Expectations

Inherit NFR-AUTO-001, NFR-AUTO-002, NFR-AUTO-005, NFR-AUTO-006, NFR-AUTO-015.

## Edge Cases Worth Specifying

- Walk-in with no appointment — advisor creates the job card on the fly; appointment record is auto-generated and immediately marked "arrived."
- Multi-day jobs — job stays in-progress; daily status snapshot emitted for customer App.
- Vehicle handover without payment — closing the job in "pay-later" mode requires account credit authority and records the outstanding balance against the customer.
- Technician reassignment mid-job — the prior technician's clock-on record closes automatically; the new technician starts a fresh clock-on record; productivity attribution splits by clock-minutes.
