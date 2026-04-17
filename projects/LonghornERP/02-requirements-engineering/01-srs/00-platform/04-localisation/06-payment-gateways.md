## 6. Payment Gateway and SMS Gateway Configuration

### 6.1 SMS Gateway Configuration

**FR-LOC-095:** The system shall route outbound SMS messages through the provider identified by the `sms_gateway_provider` field of the tenant's active localisation profile, when an SMS notification or OTP is triggered for that tenant and the field is non-null.

**FR-LOC-096:** The system shall resolve the SMS gateway shortcode and credential references from the `sms_gateway_config_json` field of the tenant's active localisation profile, using the credential key identifiers to retrieve secrets from the vault rather than storing plaintext credentials in the profile record, when initialising an SMS gateway session.

*Example profile values:*

| Profile | `sms_gateway_provider` | Typical Use |
|---|---|---|
| Uganda Phase 1 | `AFRICAS_TALKING` | Africa's Talking Uganda shortcode — East Africa. |
| Kenya Phase 2 | `AFRICAS_TALKING` | Africa's Talking Kenya shortcode. |
| Francophone Phase 3 | `ORANGE_MONEY_SMS` | Orange Money SMS gateway — Francophone West/Central Africa. |

**FR-LOC-097:** The system shall log every outbound SMS attempt — including the provider used, the destination number (masked to the last 4 digits), the status code returned, and the UTC timestamp — in the audit log, when an SMS is sent or a send attempt fails.

### 6.2 Mobile Money Gateway Configuration

**FR-LOC-098:** The system shall route mobile money payment requests through the providers listed in the `mobile_money_providers_json` field of the tenant's active localisation profile, when a mobile money payment or disbursement is triggered for that tenant.

**FR-LOC-099:** The system shall resolve gateway API endpoints and credential key identifiers from the `mobile_money_providers_json` field, using the credential keys to retrieve secrets from the vault, when initiating a mobile money API call.

The `mobile_money_providers_json` structure shall conform to:

```json
[
  {
    "provider": "MTN_MOMO_UG",
    "enabled": true,
    "credential_key": "mtn_momo_ug_prod",
    "endpoint_ref": "MTN_MOMO_UG_V2"
  },
  {
    "provider": "AIRTEL_MONEY_UG",
    "enabled": true,
    "credential_key": "airtel_money_ug_prod",
    "endpoint_ref": "AIRTEL_MONEY_UG_V1"
  }
]
```

*Example profile values:*

| Profile | Enabled Providers |
|---|---|
| Uganda Phase 1 | MTN MoMo Uganda, Airtel Money Uganda. |
| Kenya Phase 2 | M-Pesa Daraja B2C (Safaricom). |
| Tanzania Phase 2 | M-Pesa Tanzania, Airtel Money Tanzania. |
| Rwanda Phase 2 | MTN MoMo Rwanda. |
| Francophone Phase 3 | Orange Money, MTN MoMo (Cameroon, DRC, Rwanda). |

`[CONTEXT-GAP: GAP-011]` — MTN MoMo Business API specification for bulk payment (Uganda and Kenya) is required before the `MTN_MOMO_UG` and `MTN_MOMO_KE` provider integrations can be fully specified. Register on the MTN MoMo Developer Portal to obtain the bulk payment API spec.

### 6.3 Credential Storage

**FR-LOC-100:** The system shall store all payment gateway and SMS gateway credentials (API keys, client secrets, tokens) exclusively in the secrets vault, referenced by key identifier in the localisation profile configuration JSON fields, and shall not store plaintext credentials in the `localisation_profiles` table, `codebase`, or `application configuration files`, when gateway credentials are provisioned.

**FR-LOC-101:** The system shall encrypt gateway credential values at rest in the vault using AES-256 encryption, when credentials are written to the vault.

**FR-LOC-102:** The system shall rotate gateway credential references in the profile configuration JSON without requiring a profile version bump, by updating only the vault entry for the given credential key, when a credential rotation is performed by a super admin.

### 6.4 Graceful Degradation

**FR-LOC-103:** The system shall continue processing all core ERP functions — including invoice creation, journal posting, stock movements, and payroll calculation — without interruption when a configured payment gateway or SMS gateway is unavailable, unreachable, or returns an error, when a gateway failure event is detected.

**FR-LOC-104:** The system shall queue failed gateway requests in the `gateway_retry_queue` table with an exponential back-off schedule (initial delay 30 seconds, maximum delay 30 minutes, maximum retries 10), and shall notify the tenant admin via an in-app alert identifying the failed gateway and the pending queue depth, when a gateway request fails.

**FR-LOC-105:** The system shall mark affected transactions with a `gateway_pending` status visible in the relevant module's transaction list, and shall clear the status to `gateway_complete` when the queued request succeeds, when a gateway failure causes a transaction to be queued per **FR-LOC-104**.

`[CONTEXT-GAP: GAP-011]` — The graceful degradation queue behaviour for MTN MoMo bulk payment (HR payroll disbursement, cooperative payments) depends on the MTN MoMo bulk payment API error codes. Retry logic cannot be finalised until the API specification is obtained.
