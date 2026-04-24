# Automotive — Security Baseline

## Authentication

- Password + TOTP MFA MUST be available for all back-office roles (owner, accountant, payroll, store manager).
- Biometric unlock (Face ID / Touch ID / Android biometric) is optional for workshop-floor roles (technician, service advisor) on their issued device; biometric templates stay device-local.
- Session token lifetime: 60 minutes for back-office, 12 hours for workshop-floor (long workshop shifts, single-device use). Refresh tokens rotate on use.

## Authorization (RBAC + Branch Scoping)

Roles MUST be defined at the tenant scope, branch-scoped where relevant. Minimum role catalogue:

- Super-admin (platform side, Chwezi Core)
- Owner / admin (tenant)
- Branch manager
- Service advisor
- Workshop controller
- Technician
- Storekeeper
- Accountant
- Payroll officer
- Customer (external, Customer App only)
- Fleet manager (external, corporate customer)

Mobile navigation MUST be role-filtered at render time, not merely at API-call time. A technician signing in MUST NOT see Finance, Reports, Payroll, or Super-Admin surfaces at all.

## Tenant Isolation

See `architecture-patterns.md`. In addition:

- URL manipulation: accessing `/tenants/A/...` while authenticated as tenant B MUST return HTTP 403 without leaking the resource's existence.
- Cross-tenant joins are prohibited at the ORM layer.
- Per-tenant encryption keys (envelope encryption) MUST be used for S-tier fields (payment tokens, personal identifiers, and any category classified as special personal data under the tenant's jurisdiction).

## Photo and Evidence Integrity

Inspection photos and damage photos form evidence for customer approval and potential dispute:

- Client uploads include device-attested metadata where the platform supports it (Android Play Integrity, iOS App Attest).
- Server records upload time, uploader, job card ID, and a content hash (SHA-256).
- Photos MUST NOT be editable after upload. A replacement requires an explicit admin action that keeps the original plus replacement with reason.

## Barcode Scanning Controls

Barcode scanning (parts issue, VIN lookup, job card QR) MUST validate scanned codes against a tenant-scoped registry. Unknown barcodes prompt a decision (register new vs reject) and never silently match to another tenant's item.

## Payment Scope Minimization

- No card data enters the application tier.
- Gateway iframes / SDKs handle card capture.
- Mobile money deep links initiate STK push / USSD / HTTP redirects without the platform touching the PIN.
- All gateway interactions log correlation IDs but NEVER log payloads containing card numbers.

## Super-Admin Impersonation

Chwezi Core staff MUST NOT have read access to tenant data by default. Support impersonation requires:

1. Ticket reference.
2. Reason field.
3. Confirmation that the tenant has consented (per MSA clause) or that the action is emergency maintenance with post-event notification.
4. Session-duration cap (default 30 minutes, max 4 hours).
5. Every action in the session is logged with `impersonator`, `tenant_id`, `actor_role_during_session`, `reason`, `ticket`, and a hash-chained audit record.

## Offline Mutation Trust

Offline mutations MUST be replayed server-authoritatively. The server validates every offline mutation against current state (permissions, pricing, stock availability) before committing. A mutation that would have been rejected had it been online is rejected on sync with a user-visible explanation.

## Photo Redaction and PII

Photos of a vehicle interior may contain PII (documents left on seats, dashcam screens). The Customer App photo capture flow includes a face/plate-blur toggle where applicable and a disclaimer before submission.

## Waste and Chain-of-Custody (High-Value Parts)

High-value or security-relevant parts (airbags, ECUs, catalytic converters) SHOULD support a chain-of-custody audit trail: received → stored → issued-to-job → installed, with photo evidence at each transition.
