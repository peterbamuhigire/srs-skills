# Automotive — Non-Functional Requirement Defaults

Each block below is injected into the scaffolded SRS under `<!-- [DOMAIN-DEFAULT: automotive] -->` markers. Consultants review, edit, or delete per tenant context before the SRS is built.

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-001: Workshop-Floor Mobile Responsiveness
The Garage Manager App SHALL complete a job-status transition (state change, photo capture, note add, or clock-on/clock-off) end-to-end within 1.5 seconds at P95 on a mid-range Android device (4 GB RAM, Android 10+) over a 4G cellular link, and SHALL queue the mutation locally without user-visible blocking when the connection is offline.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-002: Offline-First Scope for Operational Modules
The Garage Manager App SHALL permit the following operations while offline for up to 12 continuous hours and reconcile without user-visible data loss on reconnection: job-card status updates, inspection photo capture, parts issue confirmation, technician clock-on/clock-off, and local vehicle lookup against cached appointments. Accounting postings, invoice issuance to e-invoicing authorities, and payment capture are explicitly out of offline scope.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-003: Tenant Data Isolation
The platform SHALL enforce tenant isolation at the service layer such that any request whose authenticated session tenant_id does not match the requested resource's tenant_id returns HTTP 403 with no resource metadata disclosure. Automated isolation tests SHALL execute on every CI build and fail the pipeline on any leak.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-004: VIN and Registration Plate Integrity
The platform SHALL validate VINs against ISO 3779 (17-character length, check-digit computation per SAE J853 where applicable) on entry and SHALL enforce uniqueness of the pair (tenant_id, VIN) and (tenant_id, registration_plate). Bypass requires an explicit admin-authorised override recorded with actor, timestamp, and reason.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-005: Odometer Monotonicity
The platform SHALL reject any odometer reading lower than the highest previously recorded reading for the same vehicle unless accompanied by an admin-authorised odometer-reset record citing a reason (cluster replacement, data-entry correction). The rejection SHALL return a user-visible message naming the prior value and date.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-006: Customer Approval Artifact Integrity
For every job card that transitions from "awaiting-approval" to "approved," the platform SHALL persist an immutable approval record containing: actor identity, timestamp, approved line items with quantities and amounts, approval channel (in-app, email-click, signed-image, verbal-recorded), and a content hash. The record SHALL be retained for the statutory minimum period of the tenant's jurisdiction or 7 years, whichever is longer.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-007: Cardholder Data Scope Minimization
The platform SHALL NOT persist primary account numbers (PAN), card verification values (CVV), or magnetic-stripe track data at any tier. All card capture SHALL occur through a PCI-certified gateway iframe or SDK, and the platform SHALL persist only tokens, last-four digits, brand, and expiry for display and reconciliation purposes.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-008: Real-Time-Async General Ledger Posting
The platform SHALL post a GL journal entry for every invoice issuance, payment capture, inventory issue, and payroll commit within 60 seconds at P95 of the triggering event. The user-facing financial-statement endpoints SHALL read only from committed journals. A daily reconciliation worker SHALL detect any unposted event and raise a platform-health alert.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-009: Photo Evidence Integrity
Inspection and damage photos SHALL be stored with a SHA-256 content hash, uploader identity, job-card reference, and server-assigned upload timestamp. Photos SHALL NOT be mutable after upload; replacements SHALL require an administrator action that preserves the original record alongside the replacement together with the replacement reason.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-010: Super-Admin Impersonation Audit
Every super-admin impersonation session SHALL be preceded by a ticket reference and reason, SHALL expire after a configurable maximum of 30 minutes (absolute ceiling 4 hours), and SHALL produce a hash-chained audit log where every action performed during the session is recorded with impersonator identity, tenant_id, target record, and timestamp. The tenant owner SHALL be notified within 24 hours of any impersonation session that occurred against their tenant.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-011: Appointment Booking Latency
The Customer App SHALL return the list of available appointment slots for a chosen branch and service within 1 second at P95 and SHALL complete booking confirmation within 2 seconds at P95 measured from submit to user-visible confirmation.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-012: Notification Timing Windows
The platform SHALL suppress all non-emergency customer-facing notifications outside the tenant-configured quiet window (default 21:00 to 07:00 in the customer's time zone). Appointment reminders SHALL be dispatched at the evening before and the morning of the appointment; maintenance reminders SHALL not be dispatched more frequently than once per 30 days per vehicle.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-013: E-Invoicing Submission Reliability
Where a tenant enables an e-invoicing authority adapter (EFRIS, KRA eTIMS, RRA EBM, ZATCA, CFDI, or equivalent), the platform SHALL submit the invoice within 10 seconds at P95, SHALL retry with exponential backoff on transient failures for up to 24 hours, and SHALL record the authority's fiscal reference against the invoice. An invoice that fails final submission SHALL be flagged on the owner's dashboard with remediation guidance.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-014: Parts Stock Accuracy
The parts ledger SHALL reconcile computed on-hand quantity with physical count to within 1% variance per stock-keeping unit on any tenant-initiated cycle count. Variance beyond 1% SHALL raise an audit anomaly and require adjustment-entry approval by the branch manager.
<!-- [END DOMAIN-DEFAULT] -->

<!-- [DOMAIN-DEFAULT: automotive] Source: domains/automotive/references/nfr-defaults.md -->
#### NFR-AUTO-015: Role-Filtered Mobile Navigation
The Garage Manager App SHALL render navigation surfaces strictly from the signed-in user's role permission set. A technician session SHALL NOT render Finance, Reports, Payroll, or Super-Admin entry points under any circumstances, including deep-links received from external applications.
<!-- [END DOMAIN-DEFAULT] -->
