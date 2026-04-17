# 4. KRA eTIMS Integration Requirements

<!-- [DOMAIN-DEFAULT: Integration] -->
**Activation condition:** The Kenya Revenue Authority (KRA) electronic Tax Invoice Management System (eTIMS) adapter activates automatically when a tenant's localisation profile is set to `KE`. No manual configuration is required beyond credential provisioning.
<!-- [END DOMAIN-DEFAULT] -->

`[CONTEXT-GAP: GAP-009 — KRA eTIMS API endpoint URL, authentication scheme (API key / OAuth / client certificate), and payload schema version not confirmed. All requirements below assume REST/JSON with bearer token unless superseded by the KRA eTIMS integration guide.]`

## 4.1 Submission of Fiscal Documents

**FR-INTG-046:** The system shall submit every sales invoice to the KRA eTIMS API simultaneously with or prior to delivering the invoice to the customer, when the tenant localisation profile is `KE` and the Sales module generates a confirmed invoice.

**FR-INTG-047:** The system shall submit every credit note to the KRA eTIMS API before the credit note is made available to the customer, when a credit note is raised against a previously submitted eTIMS invoice.

**FR-INTG-048:** The system shall construct each eTIMS submission payload using the field mapping defined in the KRA eTIMS Integration Guide for the active API version, when preparing a submission for a given invoice or credit note.

**FR-INTG-049:** The system shall include the tenant's KRA Personal Identification Number (PIN), business name, invoice date, line items with Harmonised System (HS) codes where applicable, tax amounts, and invoice totals in every outbound eTIMS payload, when constructing the payload from a confirmed invoice record.

**FR-INTG-050:** The system shall transmit all eTIMS payloads over TLS 1.2 or higher, when communicating with the KRA eTIMS endpoint.

## 4.2 Fiscal Response Handling

**FR-INTG-051:** The system shall parse the eTIMS control unit invoice number (CUIN) and QR code returned in the KRA eTIMS API success response, when the KRA eTIMS API returns HTTP 200 with a valid fiscal receipt payload.

**FR-INTG-052:** The system shall store the CUIN and QR code against the originating invoice record in the database, when a successful eTIMS response is received.

**FR-INTG-053:** The system shall embed the CUIN and QR code in the printed and PDF versions of the invoice, when the invoice is rendered for customer delivery following a successful eTIMS submission.

**FR-INTG-054:** The system shall mark the invoice with status `ETIMS_SUBMITTED` upon receipt of a successful eTIMS fiscal response, when the submission cycle completes without error.

## 4.3 Retry and Failure Handling

**FR-INTG-055:** The system shall retry a failed eTIMS submission up to 3 times using exponential backoff intervals of 30 seconds, 60 seconds, and 120 seconds respectively, when the eTIMS API returns a network error, HTTP 5xx response, or connection timeout.

**FR-INTG-056:** The system shall place the invoice submission payload onto the offline queue and mark the invoice with status `ETIMS_QUEUED` when all 3 retry attempts fail, allowing the tenant workflow to continue without blocking invoice delivery.

**FR-INTG-057:** The system shall not block or delay the tenant's invoicing workflow while an eTIMS submission is in `ETIMS_QUEUED` status, when the offline queue is active.

**FR-INTG-058:** The system shall retain queued eTIMS payloads for a minimum of 72 hours, when the external eTIMS service is unavailable.

**FR-INTG-059:** The system shall display a visible status indicator on the invoice record showing `ETIMS_QUEUED` or `ETIMS_FAILED` to the authorised Finance user, when a submission has not completed successfully.

## 4.4 Offline Queue and Reconnection

**FR-INTG-060:** The system shall automatically detect restoration of connectivity to the eTIMS endpoint and begin processing all payloads in the offline queue in FIFO order, when the system performs its scheduled connectivity health check and the endpoint is reachable.

## 4.5 Credential Management

**FR-INTG-061:** The system shall retrieve all KRA eTIMS API credentials exclusively from the platform encrypted credential store using the tenant identifier as the lookup key, when initiating any eTIMS API call.

**FR-INTG-062:** The system shall never write KRA eTIMS API credentials, tokens, or private keys to application logs, error reports, or API response payloads, when processing any eTIMS transaction at any point in the request lifecycle.
