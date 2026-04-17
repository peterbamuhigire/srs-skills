# 8. Requirements Traceability Matrix

## 8.1 Business Goals Reference

| ID | Business Goal |
|---|---|
| BG-001 | Regulatory compliance — Uganda (URA EFRIS e-invoicing; NSSF Uganda contribution submission) |
| BG-002 | Regulatory compliance — Kenya (KRA eTIMS e-invoicing; NSSF Kenya contribution submission) |
| BG-003 | Revenue collection and payment operations (SaaS billing; customer invoice settlement; supplier disbursement via mobile money) |
| BG-004 | Partner ecosystem extensibility (real-time event notifications for third-party integrations via webhook framework) |

## 8.2 Functional Requirements Traceability

| FR Identifier | Requirement Summary | Business Goal | Integration Domain |
|---|---|---|---|
| **FR-INTG-001** | Submit sales invoice to EFRIS before customer delivery | BG-001 | EFRIS |
| **FR-INTG-002** | Submit credit note to EFRIS before customer delivery | BG-001 | EFRIS |
| **FR-INTG-003** | Construct EFRIS payload per URA field mapping | BG-001 | EFRIS |
| **FR-INTG-004** | Include TIN, line items, tax amounts in EFRIS payload | BG-001 | EFRIS |
| **FR-INTG-005** | Transmit EFRIS payloads over TLS 1.2+ | BG-001 | EFRIS |
| **FR-INTG-006** | Parse fiscal document number and QR code from EFRIS response | BG-001 | EFRIS |
| **FR-INTG-007** | Store fiscal document number and QR code on invoice record | BG-001 | EFRIS |
| **FR-INTG-008** | Embed fiscal document number and QR code in printed invoice | BG-001 | EFRIS |
| **FR-INTG-009** | Mark invoice `EFRIS_SUBMITTED` on successful response | BG-001 | EFRIS |
| **FR-INTG-010** | Retry failed EFRIS submission with exponential backoff (3 attempts) | BG-001 | EFRIS |
| **FR-INTG-011** | Queue payload and mark invoice `EFRIS_QUEUED` after 3 failures | BG-001 | EFRIS |
| **FR-INTG-012** | Do not block invoicing workflow when submission is queued | BG-001 | EFRIS |
| **FR-INTG-013** | Retain queued EFRIS payloads for 72 hours | BG-001 | EFRIS |
| **FR-INTG-014** | Display EFRIS status indicator on invoice record | BG-001 | EFRIS |
| **FR-INTG-015** | Auto-process offline queue on EFRIS endpoint reconnection | BG-001 | EFRIS |
| **FR-INTG-016** | Update invoice to `EFRIS_SUBMITTED` after queued submission succeeds | BG-001 | EFRIS |
| **FR-INTG-017** | Generate daily EFRIS reconciliation report | BG-001 | EFRIS |
| **FR-INTG-018** | Allow manual resubmission of `EFRIS_FAILED` invoices | BG-001 | EFRIS |
| **FR-INTG-019** | Retrieve EFRIS credentials from encrypted store only | BG-001 | EFRIS |
| **FR-INTG-020** | Never log EFRIS credentials in plaintext | BG-001 | EFRIS |
| **FR-INTG-021** | Provider-plugin architecture for mobile money adapters | BG-003 | Mobile Money |
| **FR-INTG-022** | Activate provider plugins without modifying Integration Layer core | BG-003, BG-004 | Mobile Money |
| **FR-INTG-023** | Activate MTN MoMo for profiles `UG`/`RW` | BG-003 | Mobile Money |
| **FR-INTG-024** | Activate Airtel Money for profiles `UG`/`KE`/`TZ` | BG-003 | Mobile Money |
| **FR-INTG-025** | Activate M-Pesa Daraja for profiles `KE`/`TZ` | BG-003 | Mobile Money |
| **FR-INTG-026** | Collect SaaS subscription fee via mobile money | BG-003 | Mobile Money |
| **FR-INTG-027** | Collect customer invoice payment via mobile money | BG-003 | Mobile Money |
| **FR-INTG-028** | Disburse supplier payment via mobile money | BG-003 | Mobile Money |
| **FR-INTG-029** | Transmit amount, currency, mobile number, and reference on initiation | BG-003 | Mobile Money |
| **FR-INTG-030** | Assign UUID v4 reference to every mobile money request | BG-003 | Mobile Money |
| **FR-INTG-031** | Record provider transaction ID alongside internal reference | BG-003 | Mobile Money |
| **FR-INTG-032** | Poll provider status at 15s, 30s, 60s when no callback received | BG-003 | Mobile Money |
| **FR-INTG-033** | Mark transaction `TIMEOUT` and cease polling after 5 minutes | BG-003 | Mobile Money |
| **FR-INTG-034** | Expose tenant-isolated inbound callback endpoint per provider | BG-003 | Mobile Money |
| **FR-INTG-035** | Validate provider callback signature before processing | BG-003 | Mobile Money |
| **FR-INTG-036** | Update payment ledger to `PAID` within 3 seconds of successful callback | BG-003 | Mobile Money |
| **FR-INTG-037** | Update transaction to `FAILED` on declined callback | BG-003 | Mobile Money |
| **FR-INTG-038** | Generate daily mobile money reconciliation report per provider | BG-003 | Mobile Money |
| **FR-INTG-039** | Flag reconciliation anomalies for Finance administrator review | BG-003 | Mobile Money |
| **FR-INTG-040** | Submit reversal request to provider on authorised refund | BG-003 | Mobile Money |
| **FR-INTG-041** | Update record to `REVERSED` and post credit entry on confirmed reversal | BG-003 | Mobile Money |
| **FR-INTG-042** | Place timed-out transactions in manual review queue | BG-003 | Mobile Money |
| **FR-INTG-043** | Store mobile money credentials using AES-256 encryption | BG-003 | Mobile Money |
| **FR-INTG-044** | Retrieve credentials from encrypted store at runtime only | BG-003 | Mobile Money |
| **FR-INTG-045** | Never log mobile money credentials in plaintext | BG-003 | Mobile Money |
| **FR-INTG-046** | Submit sales invoice to KRA eTIMS before customer delivery | BG-002 | KRA eTIMS |
| **FR-INTG-047** | Submit credit note to KRA eTIMS before customer delivery | BG-002 | KRA eTIMS |
| **FR-INTG-048** | Construct eTIMS payload per KRA field mapping | BG-002 | KRA eTIMS |
| **FR-INTG-049** | Include KRA PIN, HS codes, tax amounts in eTIMS payload | BG-002 | KRA eTIMS |
| **FR-INTG-050** | Transmit eTIMS payloads over TLS 1.2+ | BG-002 | KRA eTIMS |
| **FR-INTG-051** | Parse CUIN and QR code from eTIMS response | BG-002 | KRA eTIMS |
| **FR-INTG-052** | Store CUIN and QR code on invoice record | BG-002 | KRA eTIMS |
| **FR-INTG-053** | Embed CUIN and QR code in printed invoice | BG-002 | KRA eTIMS |
| **FR-INTG-054** | Mark invoice `ETIMS_SUBMITTED` on successful response | BG-002 | KRA eTIMS |
| **FR-INTG-055** | Retry failed eTIMS submission with exponential backoff (3 attempts) | BG-002 | KRA eTIMS |
| **FR-INTG-056** | Queue payload and mark invoice `ETIMS_QUEUED` after 3 failures | BG-002 | KRA eTIMS |
| **FR-INTG-057** | Do not block invoicing workflow when eTIMS submission is queued | BG-002 | KRA eTIMS |
| **FR-INTG-058** | Retain queued eTIMS payloads for 72 hours | BG-002 | KRA eTIMS |
| **FR-INTG-059** | Display eTIMS status indicator on invoice record | BG-002 | KRA eTIMS |
| **FR-INTG-060** | Auto-process offline queue on eTIMS endpoint reconnection | BG-002 | KRA eTIMS |
| **FR-INTG-061** | Retrieve eTIMS credentials from encrypted store only | BG-002 | KRA eTIMS |
| **FR-INTG-062** | Never log eTIMS credentials in plaintext | BG-002 | KRA eTIMS |
| **FR-INTG-063** | Activate NSSF adapter when HR & Payroll active and profile is `UG`/`KE` | BG-001, BG-002 | NSSF |
| **FR-INTG-064** | Apply jurisdiction-specific NSSF rules per localisation profile | BG-001, BG-002 | NSSF |
| **FR-INTG-065** | Generate monthly NSSF contribution file from payroll close | BG-001, BG-002 | NSSF |
| **FR-INTG-066** | Format contribution file per NSSF-specified schema | BG-001, BG-002 | NSSF |
| **FR-INTG-067** | Allow Payroll administrator to preview file before submission | BG-001, BG-002 | NSSF |
| **FR-INTG-068** | Submit contribution file via NSSF REST API or SFTP | BG-001, BG-002 | NSSF |
| **FR-INTG-069** | Record NSSF submission reference number and status | BG-001, BG-002 | NSSF |
| **FR-INTG-070** | Surface NSSF portal validation errors to Payroll administrator | BG-001, BG-002 | NSSF |
| **FR-INTG-071** | Allow correction and resubmission of rejected records | BG-001, BG-002 | NSSF |
| **FR-INTG-072** | Retain NSSF contribution files for 7 years | BG-001, BG-002 | NSSF |
| **FR-INTG-073** | Allow tenant administrator to register webhook endpoint with URL, secret, and events | BG-004 | Webhook |
| **FR-INTG-074** | Validate webhook URL is a syntactically valid HTTPS URL | BG-004 | Webhook |
| **FR-INTG-075** | Allow activation/deactivation of webhook without deletion | BG-004 | Webhook |
| **FR-INTG-076** | Allow update of webhook URL, secret, and event subscriptions | BG-004 | Webhook |
| **FR-INTG-077** | Store webhook secret key using AES-256 encryption | BG-004 | Webhook |
| **FR-INTG-078** | Support standard event types for webhook subscription | BG-004 | Webhook |
| **FR-INTG-079** | Allow new event types to be registered without modifying webhook core | BG-004 | Webhook |
| **FR-INTG-080** | Deliver webhooks as HTTP POST with `Content-Type: application/json` | BG-004 | Webhook |
| **FR-INTG-081** | Include `event_type`, `event_id`, `tenant_id`, `timestamp`, `data` in payload | BG-004 | Webhook |
| **FR-INTG-082** | Sign outbound webhook payload with HMAC-SHA256 in `X-Longhorn-Signature` | BG-004 | Webhook |
| **FR-INTG-083** | Document HMAC-SHA256 verification procedure in developer reference | BG-004 | Webhook |
| **FR-INTG-084** | Dispatch webhook within 10 seconds at P95 | BG-004 | Webhook |
| **FR-INTG-085** | Consider delivery successful on HTTP 2xx within 10 seconds | BG-004 | Webhook |
| **FR-INTG-086** | Retry failed webhook delivery with exponential backoff (3 attempts) | BG-004 | Webhook |
| **FR-INTG-087** | Move payload to DLQ after 3 failed delivery attempts | BG-004 | Webhook |
| **FR-INTG-088** | Retain DLQ entries for 7 days and surface to tenant administrator | BG-004 | Webhook |
| **FR-INTG-089** | Allow manual re-delivery of DLQ entries | BG-004 | Webhook |
| **FR-INTG-090** | Record delivery log entry for every webhook dispatch attempt | BG-004 | Webhook |
| **FR-INTG-091** | Retain webhook delivery logs for 30 days | BG-004 | Webhook |

## 8.3 Non-Functional Requirements Traceability

| NFR Identifier | Requirement Summary | Business Goal | Integration Domain |
|---|---|---|---|
| **NFR-INTG-001** | EFRIS submission latency ≤ 5 seconds at P95 | BG-001 | EFRIS |
| **NFR-INTG-002** | Mobile money callback processing ≤ 3 seconds at P95 | BG-003 | Mobile Money |
| **NFR-INTG-003** | Webhook dispatch within 10 seconds at P95, zero data loss | BG-004 | Webhook |
| **NFR-INTG-004** | Payloads queued for retry without blocking tenant workflow | BG-001, BG-002, BG-003 | All |
| **NFR-INTG-005** | EFRIS/eTIMS offline queue durability ≥ 72 hours | BG-001, BG-002 | EFRIS, KRA eTIMS |
| **NFR-INTG-006** | Webhook DLQ durability ≥ 7 days | BG-004 | Webhook |
| **NFR-INTG-007** | All API credentials AES-256 encrypted at rest; never logged or returned | BG-001, BG-002, BG-003 | All |
| **NFR-INTG-008** | All outbound communications use TLS 1.2+ | BG-001, BG-002, BG-003, BG-004 | All |
| **NFR-INTG-009** | All webhook payloads signed with HMAC-SHA256 | BG-004 | Webhook |
| **NFR-INTG-010** | Concurrent multi-tenant submissions within P95 latency threshold | BG-001, BG-002 | EFRIS, KRA eTIMS |
| **NFR-INTG-011** | Webhook engine supports ≥ 10,000 dispatches/minute | BG-004 | Webhook |
| **NFR-INTG-012** | Every transaction logged with correlation ID within 5 minutes | BG-001, BG-002, BG-003, BG-004 | All |
| **NFR-INTG-013** | NSSF files retained in immutable storage for ≥ 7 years | BG-001, BG-002 | NSSF |

## 8.4 Open Context Gaps

The following context gaps must be resolved before this document is baselined for implementation:

| Gap ID | Description | Affected Requirements |
|---|---|---|
| GAP-001 | EFRIS API endpoint URL and authentication scheme not confirmed | FR-INTG-001 through FR-INTG-020, NFR-INTG-001 |
| GAP-009 | KRA eTIMS API endpoint URL, authentication scheme, and payload schema version not confirmed | FR-INTG-046 through FR-INTG-062, NFR-INTG-001 |
| GAP-013 | NSSF Uganda and NSSF Kenya contribution file format, API endpoint, authentication, and SFTP server details not confirmed | FR-INTG-063 through FR-INTG-072, NFR-INTG-013 |
