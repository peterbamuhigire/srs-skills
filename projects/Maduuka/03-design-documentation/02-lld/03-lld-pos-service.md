---
title: "Maduuka Platform — Low-Level Design, Section 3: POS Service"
author: "Chwezi Core Systems"
date: "2026-04-05"
---

# POS Service

**Document ID:** MADUUKA-LLD-003
**Version:** 1.0
**Status:** Draft
**Owner:** Peter Bamuhigire, Chwezi Core Systems
**Date:** 2026-04-05

---

## 1. Overview

`POSService` is the central orchestrator for all point-of-sale operations. It depends on the following injected collaborators:

- `SaleRepository` — all reads and writes to `sales`, `sale_items`, `sale_payments`
- `SessionRepository` — reads and writes to `pos_sessions`
- `StockService` — stock decrement and FEFO selection
- `CustomerRepository` — credit balance reads and updates
- `PaymentAccountRepository` — payment account balance updates
- `AuditLogService` — audit trail writes
- `ReceiptService` — receipt generation and delivery
- `PaymentStrategyFactory` — resolves the correct `PaymentStrategyInterface` implementation

---

## 2. Method Signatures and Behaviour

### 2.1 openSession

```php
public function openSession(
    int $franchiseId,
    int $cashierId,
    int $branchId,
    float $openingFloat
): Session;
```

**Pre-conditions:**

- The cashier must not have an open session for the same branch (one active session per cashier per branch).
- `openingFloat` must be >= 0.

**Behaviour:**

1. Query `pos_sessions` for an existing `open` session with `cashier_id = $cashierId AND branch_id = $branchId AND franchise_id = $franchiseId`. If found, throw `BusinessRuleViolationException` with code `SESSION_ALREADY_OPEN`.
2. Insert a new `pos_sessions` row with `status = 'open'`, `opening_float = $openingFloat`, `opened_at = UTC_NOW()`.
3. Fire `SessionOpened` event; audit observer writes `action = 'session.opened'`.
4. Return the persisted `Session` entity.

---

### 2.2 processSale

```php
public function processSale(SaleRequest $request): SaleResult;
```

`SaleRequest` value object fields: `franchiseId`, `sessionId`, `cashierId`, `branchId`, `customerId` (nullable), `items: array<SaleItemData>`, `payments: array<PaymentData>`, `discountAmount`, `notes`, `clientUuid` (for idempotency).

**Pre-conditions:**

- The POS session identified by `sessionId` must have `status = 'open'` and belong to `franchiseId`.

**Behaviour:**

1. **Idempotency check:** query `sales` for `client_uuid = $request->clientUuid AND franchise_id = $franchiseId`. If found, return the existing `SaleResult` without reprocessing.
2. **Validate cart:** for each item in `$request->items`, verify the product exists and is active within `franchiseId`. Verify stock availability in the session's warehouse (if `track_batches = FALSE`, check `stock_levels.quantity >= requested_quantity`).
3. **FEFO selection:** for products with `track_batches = TRUE`, call `StockService::enforceFefo()` to resolve the batch.
4. **Credit limit enforcement (BR-002):** if any `PaymentData` has `method = 'credit'`, retrieve `customers.credit_limit` and `customers.outstanding_balance`. Compute `projectedBalance = outstanding_balance + credit_amount`. If `projectedBalance > credit_limit`, check whether `$request->managerOverrideById` is set and holds a user with `pos.credit.override` permission. If no valid override, throw `BusinessRuleViolationException` with code `CREDIT_LIMIT_EXCEEDED`.
5. **Compute totals:** sum `line_total` for all items; apply `discountAmount`; apply applicable tax rates from `product_categories.tax_rate_id`; compute `total`.
6. **Multi-payment validation (BR-010):** sum all `PaymentData.amount` values. If the sum does not equal `total`, throw `ValidationException` with code `PAYMENT_SUM_MISMATCH`.
7. **Persist sale:** insert `sales` row; insert `sale_items` rows; insert `sale_payments` rows (one row per payment component).
8. **Decrement stock (FR-POS-016):** call `StockService::recordMovement()` for each sale item with `movement_type = 'sale'` and `quantity = -1 * requested_quantity`.
9. **Update customer credit balance:** if any payment is credit, increment `customers.outstanding_balance` by the credit component amount.
10. **Update payment account balances:** for each cash or MoMo payment, increment the corresponding `payment_accounts.balance`.
11. **Process MoMo payments:** for each payment with `method IN ('mtn_momo', 'airtel_money')`, delegate to the appropriate `PaymentStrategyInterface` implementation. On `PENDING` status from the gateway, set `sale_payments.reference` to the gateway transaction ID and mark the payment status as `pending`.
12. **Receipt generation:** call `ReceiptService::generate()` asynchronously (queued job).
13. **Receipt gap check (BR-008):** verify the new `receipt_number` is contiguous with the last receipt in the session. If a gap is detected, insert a `receipt_gap_flags` record for manager review.
14. Fire `SaleCreated` event; audit observer writes `action = 'sale.created'` with `new_values = { saleId, total, paymentMethods }`.
15. Return `SaleResult { sale, receiptNumber, paymentStatuses }`.

---

### 2.3 processMoMoPayment

```php
public function processMoMoPayment(
    int $saleId,
    string $phoneNumber,
    float $amount,
    string $provider,
    int $franchiseId
): PaymentStatus;
```

*[BLOCKED: GAP-001 — MTN MoMo Business API sandbox credentials not yet provisioned. This method's external integration cannot be validated until credentials are available. Internal logic and status-mapping are designed; the `MoMoApiClient::requestPayment()` call is a stub returning `PENDING` until GAP-001 is resolved.]*

**Behaviour (designed, pending integration):**

1. Call `MoMoApiClient::requestPayment(phoneNumber, amount, referenceId)`.
2. Map gateway response to internal `PaymentStatus` enum: `PENDING`, `SUCCESS`, `FAILED`.
3. On `SUCCESS`: update `sale_payments.reference` with the gateway transaction reference; no further action.
4. On `FAILED`: fire `MoMoPaymentFailed` event; the cashier UI is notified via the polling endpoint `GET /v1/pos/payments/{paymentId}/status`.
5. On `PENDING`: the payment record persists with status `pending`; a background job polls the gateway every 10 seconds for up to 5 minutes.
6. All outcomes are written to the audit log with `action = 'payment.momo.{status}'`.

---

### 2.4 holdSale

```php
public function holdSale(int $cartId, int $franchiseId, int $cashierId): HoldReference;
```

**Behaviour:**

1. Validate that the cart belongs to the authenticated cashier's active session.
2. Persist the cart state to `held_sales` table (or serialise to JSON in `pos_sessions.held_carts` JSONB column — implementation decision deferred to developer).
3. Return `HoldReference { holdNumber: string, heldAt: DateTime }`.
4. Stock is not decremented at hold time; stock is decremented only on `processSale()` completion.

---

### 2.5 voidSale

```php
public function voidSale(
    int $saleId,
    string $reason,
    int $authorisedBy,
    int $franchiseId
): void;
```

**Pre-conditions:**

- The sale must exist, belong to `franchiseId`, and have `status = 'completed'`.
- The `authorisedBy` user must hold the `pos.sales.void` permission (Branch Manager or above).

**Behaviour:**

1. Verify `$authorisedBy` user holds `pos.sales.void` permission; throw `AuthorisationException` if not.
2. Update `sales.status = 'voided'` and set `voided_by = $authorisedBy`, `voided_at = UTC_NOW()`, `void_reason = $reason`.
3. For each `sale_items` row, call `StockService::recordMovement()` with `movement_type = 'customer_return'` and a positive quantity (reversal).
4. For each `sale_payments` row with `method = 'credit'`, decrement `customers.outstanding_balance` by the payment amount (credit reversal).
5. For each `sale_payments` row with `method IN ('cash', 'bank_transfer', 'other')`, decrement the corresponding `payment_accounts.balance`.
6. Fire `SaleVoided` event; audit observer writes `action = 'sale.voided'` with `old_values = { status: 'completed' }`, `new_values = { status: 'voided', reason, authorisedBy }`.

---

### 2.6 closeSession

```php
public function closeSession(
    int $sessionId,
    float $closingCash,
    int $franchiseId
): SessionReconciliation;
```

**Pre-conditions:**

- The session must have `status = 'open'`.
- All sales in the session must be either `completed` or `voided` (no in-progress sales).

**Behaviour (BR-007):**

1. Query all `sales` for the session. Verify none are in an in-progress state.
2. Sum cash sales: `cashSalesTotal = SUM(sale_payments.amount) WHERE method = 'cash' AND sale not voided`.
3. Sum cash refunds (voided sales that had cash components): `cashRefundsTotal`.
4. Compute expected closing cash: $ExpectedCash = openingFloat + cashSalesTotal - cashRefundsTotal$.
5. Compute variance: $Variance = closingCash - ExpectedCash$.
6. Update `pos_sessions`: set `status = 'closed'`, `closing_cash_counted = $closingCash`, `closed_at = UTC_NOW()`.
7. If `|Variance| > 0`, set a `variance_flagged = TRUE` flag on the session record. The dashboard displays flagged sessions for manager review.
8. Fire `SessionClosed` event; audit observer writes `action = 'session.closed'`.
9. Return `SessionReconciliation { sessionId, openingFloat, cashSales, cashRefunds, expectedCash, closingCash, variance, status: 'balanced'|'over'|'under' }`.

---

## 3. Offline Sync Service

### 3.1 SyncService

```php
class SyncService
{
    /**
     * Replays a batch of offline transactions in chronological order.
     * Each transaction is idempotency-checked before processing.
     *
     * @param array<OfflineTransaction> $pendingTransactions  Ordered by client_timestamp ASC
     */
    public function processBatch(
        array $pendingTransactions,
        int $franchiseId,
        int $userId
    ): SyncResult;
}
```

**Behaviour:**

1. Sort `$pendingTransactions` by `client_timestamp` ascending.
2. For each transaction:
   a. Check idempotency: query by `client_uuid`. If a matching record exists in `sales`, skip the transaction and append `{ clientUuid, status: 'already_synced' }` to the result.
   b. Validate the transaction payload against the same rules applied in `processSale()`.
   c. On validation success: call `processSale()` with the replayed data.
   d. On validation failure: append `{ clientUuid, status: 'failed', errors: [...] }` to the result. Do not abort the batch; continue processing remaining transactions.
3. Return `SyncResult { processed: int, skipped: int, failed: int, items: array<SyncItemResult> }`.

### 3.2 Conflict Resolution Rules

When the server has a more recent `updated_at` timestamp for the same entity than the client's `client_timestamp`, the server record is the authoritative version. The client's version is discarded. The conflict is logged:

```
conflict_log row:
  franchise_id    = <tenant>
  entity_type     = 'sale' | 'stock_level' | 'customer'
  entity_id       = <server record id>
  client_uuid     = <client transaction uuid>
  server_ts       = <server updated_at>
  client_ts       = <client_timestamp from payload>
  resolution      = 'server_wins'
  created_at      = NOW()
```

The Android client retrieves its conflict log via `GET /v1/sync/conflicts` on next successful sync and displays a notification to the cashier.
