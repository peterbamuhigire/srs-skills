# 6. Outbound Webhook Framework Requirements

## 6.1 Tenant Webhook Registration

**FR-INTG-073:** The system shall allow an authorised tenant administrator to register one or more outbound webhook endpoints by providing a target URL, a shared secret key, and a selection of subscribed event types, when the administrator accesses the Integrations settings panel.

**FR-INTG-074:** The system shall validate that a registered webhook URL is a syntactically valid HTTPS URL before saving the registration, when the administrator submits the webhook configuration form.

**FR-INTG-075:** The system shall allow an authorised tenant administrator to activate or deactivate any registered webhook endpoint without deleting it, when the administrator toggles the active/inactive control on the webhook record.

**FR-INTG-076:** The system shall allow an authorised tenant administrator to update the target URL, secret key, or subscribed event list of a registered webhook at any time, when the administrator saves changes to the webhook configuration.

**FR-INTG-077:** The system shall store the webhook shared secret key in the encrypted credential store using AES-256 encryption, when the secret is provisioned or updated by the tenant administrator.

## 6.2 Supported Event Types

**FR-INTG-078:** The system shall support the following standard event types for webhook subscription, when a tenant registers a webhook endpoint:

- `invoice.created` — a new sales invoice is confirmed
- `invoice.paid` — an invoice is fully settled
- `payment.received` — a payment is posted to the ledger
- `credit_note.issued` — a credit note is raised
- `stock.low` — a stock item falls below its reorder level
- `purchase_order.approved` — a purchase order passes the approval workflow
- `goods_received.posted` — a goods received note is posted to inventory
- `employee.onboarded` — a new employee record is activated in HR
- `payroll.run_completed` — a payroll run is finalised
- `tenant.subscription_renewed` — a SaaS subscription billing cycle completes successfully
- `tenant.subscription_overdue` — a SaaS subscription payment is overdue

**FR-INTG-079:** The system shall allow the platform engineering team to register additional event types in the webhook event registry without modifying the webhook delivery core, when new system events are introduced in future module releases.

## 6.3 Payload and Signature

**FR-INTG-080:** The system shall deliver every webhook notification as an HTTP POST request with a `Content-Type: application/json` header and a JSON payload to the registered endpoint, when a subscribed event occurs.

**FR-INTG-081:** The system shall include the following fields in every webhook payload: `event_type`, `event_id` (UUID v4), `tenant_id`, `timestamp` (ISO 8601 UTC), and `data` (event-specific object), when constructing the outbound payload.

**FR-INTG-082:** The system shall compute an HMAC-SHA256 signature of the serialised JSON payload using the tenant's registered secret key and include it in the `X-Longhorn-Signature` request header, when dispatching any outbound webhook.

**FR-INTG-083:** The system shall document the HMAC-SHA256 verification procedure in the developer-facing Integration API reference so that receiving systems can independently verify payload authenticity, when the webhook framework is documented.

## 6.4 Delivery, Retry, and Dead-Letter Queue

**FR-INTG-084:** The system shall dispatch the webhook notification within 10 seconds of the triggering event at P95 under normal operating load, when an event occurs that has one or more active webhook subscriptions.

**FR-INTG-085:** The system shall consider a webhook delivery successful when the receiving endpoint responds with HTTP 2xx within 10 seconds of the POST request being sent, when evaluating delivery outcome.

**FR-INTG-086:** The system shall retry a failed webhook delivery up to 3 times using exponential backoff intervals of 60 seconds, 300 seconds, and 900 seconds, when the endpoint returns a non-2xx response or does not respond within the 10-second window.

**FR-INTG-087:** The system shall move a webhook payload to the Dead-Letter Queue (DLQ) after 3 consecutive failed delivery attempts, when all retry attempts are exhausted.

**FR-INTG-088:** The system shall retain DLQ entries for a minimum of 7 days and make them visible to the tenant administrator in the Webhook Delivery Log, when a payload enters the DLQ.

**FR-INTG-089:** The system shall allow an authorised tenant administrator to manually re-trigger delivery of any entry in the DLQ, when the administrator selects the re-deliver action on a DLQ record.

## 6.5 Observability

**FR-INTG-090:** The system shall record a delivery log entry for every webhook dispatch attempt, including the event type, target URL, HTTP response code, response time in milliseconds, attempt number, and outcome (`SUCCESS` or `FAILED`), when a delivery is attempted.

**FR-INTG-091:** The system shall retain webhook delivery log entries for a minimum of 30 days and present them to the authorised tenant administrator through the Integrations settings panel, when the administrator views the Webhook Delivery Log.
