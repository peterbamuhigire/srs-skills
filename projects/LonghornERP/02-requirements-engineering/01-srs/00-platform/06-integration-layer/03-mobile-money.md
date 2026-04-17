# 3. Mobile Money Integration Requirements

## 3.1 Provider Coverage and Plugin Architecture

**FR-INTG-021:** The system shall implement mobile money provider support using a provider-plugin architecture, where each provider (MTN MoMo, Airtel Money, M-Pesa Daraja) is encapsulated in an independent Integration Adapter plugin conforming to the Mobile Money Adapter Interface, when the Mobile Money integration module is active.

**FR-INTG-022:** The system shall support activation of individual mobile money provider plugins per tenant without modifying the Integration Layer core, when a new provider plugin is registered in the platform adapter registry.

**FR-INTG-023:** The system shall activate the MTN Mobile Money (MoMo) plugin for tenants whose localisation profile includes `UG` (Uganda) or `RW` (Rwanda), when the Billing or Finance module initiates a mobile money transaction.

**FR-INTG-024:** The system shall activate the Airtel Money plugin for tenants whose localisation profile includes `UG` (Uganda), `KE` (Kenya), or `TZ` (Tanzania), when the Billing or Finance module initiates a mobile money transaction.

**FR-INTG-025:** The system shall activate the M-Pesa Daraja plugin for tenants whose localisation profile includes `KE` (Kenya) or `TZ` (Tanzania), when the Billing or Finance module initiates a mobile money transaction.

## 3.2 Use Cases

**FR-INTG-026:** The system shall initiate a mobile money collection request against a customer's registered mobile number to collect the Longhorn ERP subscription fee, when the automated SaaS billing cycle triggers payment for a tenant whose preferred payment method is mobile money.

**FR-INTG-027:** The system shall initiate a mobile money collection request for the amount on a confirmed customer invoice, when a customer selects mobile money as the payment method and provides a valid mobile number on the payment screen.

**FR-INTG-028:** The system shall initiate a mobile money disbursement to a registered supplier's mobile number for the net amount on an approved payment run, when the Finance module executes a supplier payment run that includes mobile money as the disbursement method.

## 3.3 Transaction Initiation

**FR-INTG-029:** The system shall transmit the transaction amount, currency code, customer mobile number, and a unique internal transaction reference to the provider API, when initiating any mobile money collection or disbursement request.

**FR-INTG-030:** The system shall assign a unique, non-reusable internal transaction reference (UUID v4) to every mobile money request before submission, when creating a new transaction record.

**FR-INTG-031:** The system shall record the provider-assigned transaction identifier returned by the API alongside the internal transaction reference in the payment ledger, when the provider API acknowledges initiation with a transaction ID.

## 3.4 Status Polling

**FR-INTG-032:** The system shall poll the provider's transaction status endpoint at intervals of 15 seconds, 30 seconds, and 60 seconds after initiation, when a mobile money transaction remains in `PENDING` status and no callback has been received within 15 seconds of initiation.

**FR-INTG-033:** The system shall mark a mobile money transaction as `TIMEOUT` and cease polling when no terminal status (success or failure) is received from the provider within 5 minutes of initiation, when the polling cycle reaches its maximum wait duration.

## 3.5 Callback Receipt

**FR-INTG-034:** The system shall expose a unique, tenant-isolated inbound callback endpoint for each active mobile money provider, when the provider is configured to deliver asynchronous status notifications.

**FR-INTG-035:** The system shall validate the authenticity of every inbound provider callback by verifying the provider-specific signature or token before processing the payload, when an HTTP POST is received at the callback endpoint.

**FR-INTG-036:** The system shall update the payment ledger and linked invoice or billing record to `PAID` status within 3 seconds of receiving and validating a successful provider callback, when the callback payload confirms a completed transaction.

**FR-INTG-037:** The system shall update the transaction record to `FAILED` and trigger a payment failure notification to the Finance module, when a provider callback indicates a declined, cancelled, or expired transaction.

## 3.6 Reconciliation

**FR-INTG-038:** The system shall generate a daily mobile money reconciliation report per provider listing all initiated, completed, failed, and reversed transactions with amounts, mobile numbers (masked), provider transaction IDs, and internal references, when the Finance module triggers the end-of-day reconciliation process.

**FR-INTG-039:** The system shall flag any discrepancy between the internal payment ledger and the provider's daily transaction statement as a reconciliation anomaly requiring Finance administrator review, when the automated reconciliation process detects a mismatch.

## 3.7 Reversals

**FR-INTG-040:** The system shall submit a reversal request to the provider API for the full transaction amount, when an authorised Finance administrator initiates a refund for a completed mobile money payment within the provider's permitted reversal window.

**FR-INTG-041:** The system shall update the transaction record and associated invoice to `REVERSED` status and post a credit entry in the accounting ledger, when the provider confirms successful reversal.

## 3.8 Timeout Handling

**FR-INTG-042:** The system shall place a timed-out mobile money transaction into a manual review queue visible to Finance administrators, when a transaction reaches `TIMEOUT` status, to allow the administrator to determine final outcome via the provider portal before reconciling.

## 3.9 Credential Management

**FR-INTG-043:** The system shall store all mobile money provider credentials (API keys, client secrets, subscription keys, OAuth tokens) per tenant using Advanced Encryption Standard (AES)-256 encryption at rest, when credentials are provisioned or updated.

**FR-INTG-044:** The system shall retrieve mobile money provider credentials exclusively from the encrypted credential store at runtime, when constructing any API request to a mobile money provider.

**FR-INTG-045:** The system shall never write mobile money credentials, bearer tokens, or OAuth secrets to application logs, error messages, audit trails, or API response payloads, when executing any mobile money operation.
