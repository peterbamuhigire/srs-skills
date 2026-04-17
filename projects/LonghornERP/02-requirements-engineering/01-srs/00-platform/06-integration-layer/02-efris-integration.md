# 2. EFRIS Integration Requirements

<!-- [DOMAIN-DEFAULT: Integration] -->
**Activation condition:** The EFRIS adapter activates automatically when a tenant's localisation profile is set to `UG`. No manual configuration is required beyond credential provisioning.
<!-- [END DOMAIN-DEFAULT] -->

`[CONTEXT-GAP: GAP-001 — EFRIS API endpoint URL and authentication scheme (API key / OAuth / certificate-based) not confirmed. All submission and authentication requirements below assume REST/JSON with bearer token unless superseded by the URA integration guide.]`

## 2.1 Submission of Fiscal Documents

**FR-INTG-001:** The system shall submit every sales invoice to the Uganda Revenue Authority (URA) Electronic Fiscal Receipting and Invoicing System (EFRIS) API simultaneously with or prior to delivering the invoice to the customer, when the tenant localisation profile is `UG` and the Sales module generates a confirmed invoice.

**FR-INTG-002:** The system shall submit every credit note to the EFRIS API before the credit note is made available to the customer, when a credit note is raised against a previously submitted EFRIS invoice.

**FR-INTG-003:** The system shall construct each EFRIS submission payload using the field mapping defined in the EFRIS Integration Guide for the active URA API version, when preparing a submission for a given invoice or credit note.

**FR-INTG-004:** The system shall include the tenant's EFRIS taxpayer identification number (TIN), supplier name, invoice date, line items, tax amounts, and totals in every outbound EFRIS submission payload, when constructing the payload from a confirmed invoice record.

**FR-INTG-005:** The system shall transmit all EFRIS payloads over Transport Layer Security (TLS) 1.2 or higher, when communicating with the URA EFRIS endpoint.

## 2.2 Fiscal Response Handling

**FR-INTG-006:** The system shall parse the fiscal document number and Quick Response (QR) code returned in the EFRIS API success response, when the URA EFRIS API returns HTTP 200 with a valid fiscal receipt payload.

**FR-INTG-007:** The system shall store the fiscal document number and QR code against the originating invoice record in the database, when a successful EFRIS response is received.

**FR-INTG-008:** The system shall embed the fiscal document number and QR code in the printed and PDF versions of the invoice, when the invoice is rendered for customer delivery following a successful EFRIS submission.

**FR-INTG-009:** The system shall mark the invoice with status `EFRIS_SUBMITTED` upon receipt of a successful EFRIS fiscal response, when the submission cycle completes without error.

## 2.3 Retry and Failure Handling

**FR-INTG-010:** The system shall retry a failed EFRIS submission up to 3 times using exponential backoff intervals of 30 seconds, 60 seconds, and 120 seconds respectively, when the EFRIS API returns a network error, HTTP 5xx response, or connection timeout.

**FR-INTG-011:** The system shall place the invoice submission payload onto the offline queue and mark the invoice with status `EFRIS_QUEUED` when all 3 retry attempts fail, allowing the tenant workflow to continue without blocking invoice delivery.

**FR-INTG-012:** The system shall not block or delay the tenant's invoicing workflow while an EFRIS submission is in `EFRIS_QUEUED` status, when the offline queue is active.

**FR-INTG-013:** The system shall retain queued EFRIS payloads for a minimum of 72 hours, when the external EFRIS service is unavailable.

**FR-INTG-014:** The system shall display a visible status indicator on the invoice record showing `EFRIS_QUEUED` or `EFRIS_FAILED` to the authorised Finance user, when a submission has not completed successfully.

## 2.4 Offline Queue and Reconnection

**FR-INTG-015:** The system shall automatically detect restoration of connectivity to the EFRIS endpoint and begin processing all payloads in the offline queue in FIFO (first-in, first-out) order, when the system performs its scheduled connectivity health check and the endpoint is reachable.

**FR-INTG-016:** The system shall update the invoice status to `EFRIS_SUBMITTED` and record the fiscal document number and QR code upon successful submission of a previously queued payload, when the reconnection processing cycle completes for that invoice.

## 2.5 Reconciliation

**FR-INTG-017:** The system shall generate a daily EFRIS reconciliation report listing all invoices submitted, their EFRIS fiscal document numbers, submission timestamps (UTC), and any outstanding `EFRIS_QUEUED` or `EFRIS_FAILED` records, when the Finance module triggers the end-of-day reconciliation process.

**FR-INTG-018:** The system shall allow an authorised Finance administrator to manually trigger resubmission of any invoice with status `EFRIS_FAILED`, when the administrator selects the resubmit action on that invoice record.

## 2.6 Credential Management

**FR-INTG-019:** The system shall retrieve all EFRIS API credentials exclusively from the platform encrypted credential store using the tenant identifier as the lookup key, when initiating any EFRIS API call.

**FR-INTG-020:** The system shall never write EFRIS API credentials, tokens, or private keys to application logs, error reports, or API response payloads, when processing any EFRIS transaction at any point in the request lifecycle.
