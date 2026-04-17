# 11. External Integration Architecture

## 11.1 URA EFRIS Integration

The BIRDC ERP integrates with Uganda Revenue Authority's Electronic Fiscal Receipting and Invoicing Solution (EFRIS) via system-to-system REST API. Every commercial invoice and POS receipt must be submitted to EFRIS in real time.

[CONTEXT-GAP: GAP-001] — URA EFRIS API sandbox credentials are required for development and testing. The integration design below is based on the publicly documented EFRIS API specification.

### 11.1.1 Submission Flow

```
Invoice confirmed (POST /api/sales/invoices/{id}/confirm)
  → SalesService::confirmInvoice()
    → EFRISService::submitDocument(invoiceId)
      → Serialise invoice to EFRIS JSON payload (AES-256 encrypted, Base64)
      → POST to URA EFRIS API endpoint
      → Response: FDN + QR code
        → EFRISService::storeResponse(invoiceId, fdnNumber, qrCode)
        → Update tbl_sales_invoices: efris_status = 'SUBMITTED', fdn = '...', qr_code = '...'
```

### 11.1.2 Retry Queue

- If the EFRIS API call fails (network error, URA server error, or validation error), the invoice is placed in `tbl_efris_retry_queue` with `attempts = 1` and `next_retry_at = now() + 5 minutes`.
- A `ProcessEFRISRetryQueueJob` runs every 5 minutes via a cron job.
- After 3 failed attempts, the Finance Manager receives an email and SMS alert. The invoice is flagged `EFRIS_FAILED` and requires manual intervention.
- All EFRIS API responses (success and failure) are stored in `tbl_efris_log` for audit purposes.

### 11.1.3 FDN Storage

- FDN and QR code are stored in `tbl_sales_invoices.fdn_number` and `tbl_sales_invoices.efris_qr_code`.
- FDN is printed on all invoice PDF and thermal receipt outputs using mPDF.

### 11.1.4 Documents Submitted to EFRIS

- Sales invoices (standard and export)
- POS receipts (all 3 POS contexts)
- Credit notes
- Pro forma invoices (if fiscally required by URA)

## 11.2 MTN MoMo Business API Integration

[CONTEXT-GAP: GAP-002] — MTN MoMo sandbox credentials required.

| Use Case | Direction | API Operation |
|---|---|---|
| Agent remittance collection | BIRDC pushes payment prompt to agent | Collections API: `POST /v1_0/collection/requesttopay` |
| Farmer bulk payment | BIRDC disburses to farmer mobile money | Disbursements API: `POST /v1_0/disbursement/transfer` |
| Casual worker salary | BIRDC disburses to worker mobile money | Disbursements API: batch transfer |
| Customer payment (POS) | Customer-initiated MoMo payment to BIRDC | Collections API: `POST /v1_0/collection/requesttopay` |

All MTN MoMo API calls are made via `MobileMoneyService` (wraps both MTN and Airtel). Responses are stored in `tbl_mobile_money_transactions`. A payment is confirmed only when the MoMo API returns `SUCCESSFUL` status; pending transactions are polled via `GET /v1_0/collection/requesttopay/{referenceId}` by a background job.

## 11.3 Airtel Money API Integration

[CONTEXT-GAP: GAP-003] — Airtel Money sandbox credentials required.

Airtel Money provides dual-provider redundancy for all MTN MoMo use cases. The `MobileMoneyService` selects the provider based on the mobile number prefix:

- `+256 77x`, `+256 78x` → MTN MoMo
- `+256 75x`, `+256 70x` → Airtel Money

If the primary provider's API is unavailable, the transaction is queued for retry; no automatic failover to the other provider (to avoid double payments).

## 11.4 ZKTeco Biometric Device Integration

[CONTEXT-GAP: GAP-005] — ZKTeco device model and SDK version at BIRDC Nyaruzinga are unconfirmed.

The HR module integrates with ZKTeco biometric fingerprint attendance devices deployed on the Nyaruzinga premises.

- **Import mechanism:** The `ZKTecoImportService` connects to the ZKTeco device SDK (TCP/IP connection on the local network) and pulls attendance logs: employee ID, punch type (in/out), and timestamp.
- **Frequency:** Attendance is imported every 30 minutes automatically; can also be triggered manually.
- **Authoritative records:** Per BR-016, imported biometric records are treated as authoritative. Manual attendance overrides require Finance Manager approval and audit trail entry.
- **Data stored in:** `tbl_hr_attendance` with `source = 'BIOMETRIC'` or `source = 'MANUAL'`.

## 11.5 Africa's Talking SMS/WhatsApp

Africa's Talking provides outbound SMS and WhatsApp notifications for:

- **Agent notifications:** daily sales summary, remittance receipt confirmation, stock issuance notification, commission statement
- **Farmer notifications:** delivery receipt confirmation, payment confirmation with amount
- **Staff notifications:** payslip availability, budget vote alerts, EFRIS failure alerts

`NotificationService` wraps the Africa's Talking REST API. All notification content and templates are configurable in `tbl_notification_templates` (DC-002).

## 11.6 NSSF Uganda Contribution Schedule

The payroll module generates the monthly NSSF contribution schedule in the exact format required by NSSF Uganda for employer remittance.

[CONTEXT-GAP: GAP-009] — Exact NSSF Uganda file format required. The export produces a tabular file (CSV or Excel) listing: employer registration number, period, employee NIN, employee name, gross salary, employee contribution (5%), employer contribution (10%), and total.

## 11.7 Bank Bulk Payment File

The payroll module generates a bulk bank credit transfer file for employee salary payments.

[CONTEXT-GAP: GAP-006] — BIRDC's bank name and required bulk transfer file format are unconfirmed. The export format will be confirmed with BIRDC Finance Director and the relevant bank's corporate banking team.
