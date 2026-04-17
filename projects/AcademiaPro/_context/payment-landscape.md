# Payment Landscape — Academia Pro

## Strategic Positioning

Academia Pro is an ERP layer, not a competing payment processor. The payment strategy is:

- **Phase 1:** Internal fee management only — manual cash recording by the bursar, receipt generation, fee balance tracking. No third-party payment integration. Go live on Academia Pro's own merit first.
- **Phase 2:** Integrate WITH SchoolPay — connect to their payment rails after the core ERP is live and stable. Schools keep their SchoolPay infrastructure; Academia Pro adds the superior ERP layer on top.
- **Phase 3+:** Add direct MTN MoMo and Airtel Money APIs for schools that want ERP-native mobile money.
- **Phase 4+:** Card payments, diaspora corridors.
- **Phase 11:** Pan-Africa payment rails per country profile.

**Decision (2026-03-28):** SchoolPay integration will be approached after Phase 1 go-live. The product must prove its value as a standalone ERP before the integration conversation begins. This removes SchoolPay API dependency from the Phase 1 critical path.

Schools using SchoolPay for fee collection will not need to change their payment infrastructure when the integration is added in Phase 2 — Academia Pro will sync with SchoolPay to record and reconcile payments automatically at that point.

---

## SchoolPay Integration (Phase 1 — PRIMARY)

**Market position:** ~11,000 Uganda schools; ~6 million students on platform; Bank of Uganda licensed Payment Systems Operator. ERP launched January 2024 (immature — our opportunity to be the superior ERP layer they connect to).

**Base URL:** `https://schoolpay.co.ug/paymentapi/`

### Authentication

SchoolPay uses MD5 hash-based request signing — no OAuth, no API key header. Every request includes a `requestHash` computed as:

```
MD5(schoolCode + identifyingField + apiPassword)
```

The `identifyingField` varies by endpoint (transaction date, externalReference, or paymentReference). The `apiPassword` must be kept server-side in `.env` only — never in source code, never in the client.

**Critical:** MD5 is weak by modern standards but is SchoolPay's mandated scheme. Enforce TLS 1.3 on all outbound calls to compensate.

### Endpoints

| Purpose | Method | Endpoint |
|---|---|---|
| Sync transactions (single date) | GET | `/AndroidRS/SyncSchoolTransactions/{schoolCode}/{date}/{hash}` |
| Sync transactions (date range, max 31 days) | GET | `/AndroidRS/SchoolRangeTransactions/{schoolCode}/{from}/{to}/{hash}` |
| Register one-time payment | POST | `/AndroidRS/AdhocPayments/Register/{schoolCode}/{hash}` |
| Trigger mobile money debit | POST | `/AndroidRS/AdhocPayments/Request/{schoolCode}/{hash}` |
| Check payment status | GET | `/AndroidRS/AdhocPayments/Check/{schoolCode}/{hash}/{reference}` |

### Two Payment Models

**Model A — Student Payment Code (standard school fees):**
1. Each student has a permanent `studentPaymentCode` assigned by SchoolPay.
2. Parent pays via MTN MoMo, Airtel Money, bank branch, or agent, quoting the code.
3. SchoolPay processes and posts payment to the student's record.
4. Academia Pro receives confirmation via webhook or polls via SyncSchoolTransactions.

**Model B — Adhoc One-Time Payment (trips, uniform fees, etc.):**
1. Academia Pro calls `Register` with amount, student details, and a `callBackUrl`.
2. SchoolPay returns a `paymentReference`.
3. Optionally: call `Request` to push a mobile money debit prompt to a phone number.
4. Poll `Check` or wait for webhook callback confirming `"status": "PAID"`.
5. Response includes `receiptNumber` and `transactionId` for audit.

The `externalReference` field in Adhoc Register accepts Academia Pro's internal invoice ID — this is the idempotency anchor.

### Webhooks — CRITICAL CONSTRAINT

SchoolPay webhooks are **fire-and-forget — no retry mechanism**. If the Academia Pro endpoint is down or returns a non-200, the webhook is lost permanently.

**Verification:** Webhooks carry a `SHA256` signature field. All inbound payloads must be verified before any DB write.

Two webhook payload types:
- `"type": "SCHOOL_FEES"` — contains `studentPaymentCode`, `studentName`, `amount`, `sourcePaymentChannel`, `settlementBankCode`, `schoolpayReceiptNumber`
- `"type": "OTHER_FEES"` — adds `supplementaryFeeId`, `supplementaryFeeDescription`, `studentClass`

Academia Pro must respond HTTP 200 immediately (queue processing asynchronously). Because there are no retries, the nightly polling fallback is not optional — it is mandatory.

### Reconciliation Architecture (Academia Pro)

1. **Real-time:** Webhook → verify SHA256 signature → check `UNIQUE(external_reference)` → write to `fee_payments` with `channel=schoolpay` → return HTTP 200
2. **Polling fallback (nightly job):** Call `SyncSchoolTransactions` for the current date (and `SchoolRangeTransactions` for the previous 3 days) → compare against `fee_payments` → insert any missing records flagged as `source=poll_recovery`
3. **Manual bursar reconciliation:** Trigger a range pull from the bursar UI for any date range → display unmatched transactions for review

**Double-payment prevention (BR-FEE-005):** `fee_payments.external_reference` has a `UNIQUE` database constraint. Webhook handler uses `INSERT IGNORE` or `ON DUPLICATE KEY`. If a duplicate arrives, return HTTP 200 with `{"status": "duplicate", "original_receipt_id": "..."}` — never return 4xx (SchoolPay might retry on error, even though docs say it won't).

### Sandbox Environment

**No public sandbox.** Manual onboarding required — contact `[email protected]`. Explicitly request sandbox credentials during the onboarding negotiation before development begins.

### Supported Payment Channels (Confirmed)

- MTN MobileMoney Uganda
- Airtel Money Uganda
- Bank transfer (Centenary Bank, Tropical Bank, and others via settlement bank codes)
- Agent/cash payment points

Phone number format: both local (`077xxxxxxx`) and international (`256xxxxxxx`) accepted for mobile money debit requests.

### Integration Readiness Checklist (before Phase 1 dev begins)

- [ ] Obtain `schoolCode` and `apiPassword` from SchoolPay — store in `.env`
- [ ] Request sandbox environment from SchoolPay support
- [ ] Implement server-side MD5 hash generation utility
- [ ] Implement SHA256 webhook signature verification middleware
- [ ] Build polling fallback nightly job (`SyncSchoolTransactions`)
- [ ] Add `UNIQUE` constraint on `fee_payments.external_reference`
- [ ] Store `schoolpayReceiptNumber` and `transactionId` on every confirmed payment record
- [ ] Confirm webhook endpoint is always-on (high availability SLA covers it)

**Schools already using SchoolPay:** Academia Pro can target ~11,000 existing SchoolPay schools by promising a better ERP that already speaks SchoolPay's language — parents don't change payment habits, schools don't change payment infrastructure.

---

## MTN MoMo (Phase 3)

- **Product:** MTN Mobile Money Uganda (MoMo Pay / Merchant API)
- **Licence required:** BoU Payment Systems Operator licence OR integration via a licensed aggregator
- **API:** MTN MoMo Open API (Sandbox available at momodeveloper.mtn.com)
- **Flow:** Parent-initiated payment to Academia Pro merchant number → callback to Academia Pro → auto-reconcile to student account
- **Collection vs. disbursement:** Phase 3 = collection only; Phase 4+ = disbursement (refunds)

## Airtel Money (Phase 3)

- **Product:** Airtel Money Uganda — Merchant API
- **Licence:** Same BoU requirement as MTN
- **Flow:** Same pattern as MTN MoMo

## KUPAA Micro-Payment Model

Researched in master document Section 14. Key rules:
- No minimum payment floor — UGX 500 is a valid partial payment
- Payments are applied in chronological order (oldest arrear first, then current term)
- Community payment agents: third-party individuals authorised by the school to collect cash and record payments on behalf of the school (bursar role variant with restricted permissions — cash collection only, cannot modify fee structures)
- Pre-term payment discount: schools may configure a 1–5% discount for full payment before term opening date

## Card Payments (Phase 4)

- **Provider:** Flutterwave (supports Visa/Mastercard card-not-present, M-Pesa, MTN, Airtel across Africa)
- **Use case:** School owners paying their own subscription to Chwezi Core Systems; diaspora parents paying from abroad
- **PCI-DSS scope:** All card data handled on Flutterwave's servers; Academia Pro uses tokenised references only (no cardholder data storage)

## Diaspora / International (Phase 4+)

- **Provider:** Wise Business API or Flutterwave Global
- **Currency:** USD/GBP/EUR received; converted to UGX and credited to school account
- **Use case:** Ugandan parents abroad paying school fees for children in Uganda

## Pan-Africa Rails (Phase 11)

| Country | Mobile Money | Card | Other |
|---|---|---|---|
| Kenya | M-Pesa Daraja API (Safaricom) | Flutterwave / DPO Pay | Equity Bank API |
| Tanzania | Airtel Tanzania, Tigo Pesa | Flutterwave | CRDB Bank |
| Nigeria | Paystack / Flutterwave | Paystack | GTBank API |
| Ghana | MTN MoMo Ghana | Paystack | |

Each country is a data-driven profile: `country_id`, `currency_code`, `payment_gateways[]`, `tax_rate`, `curriculum_type`. No hardcoded country logic.

## USSD Short Code (Phase 11)

- **Provider:** Africa's Talking USSD API
- **Short code:** Apply for Uganda USSD short code via UCC (Uganda Communications Commission)
- **Use case:** Feature-phone parents checking fee balance and report card grades without a smartphone
- **Menu:** 1) Fee balance → 2) Last payment → 3) Report card term summary

---

## Action Items (from Section 20 Resource List)

- [ ] Contact SchoolPay for merchant API documentation and sandbox credentials
- [ ] Apply for MTN MoMo Developer account (momodeveloper.mtn.com)
- [ ] Apply for Airtel Money Uganda Merchant API access
- [ ] Engage BoU for Payment Systems Operator licence pre-application guidance (Phase 3 planning)
- [ ] Confirm Flutterwave Uganda merchant category and KYC requirements
