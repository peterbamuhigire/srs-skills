---
title: "User Stories -- Inventory, Customer, and Supplier Management (F-002, F-003, F-004)"
project: "Maduuka"
module: "Inventory / Customer / Supplier"
version: "1.0"
date: "2026-04-05"
---

# User Stories: Inventory, Customer, and Supplier Management (F-002, F-003, F-004)

These stories express the inventory, customer, and supplier functional requirements from the perspective of two roles: Stock Manager (David) and Accountant (Grace).

---

## Inventory and Stock Management (F-002)

**US-INV-001:** As a stock manager, I want to receive stock against a purchase order so that the system records the incoming goods and updates stock levels automatically.

**Acceptance Criteria:**

- Given a purchase order exists and goods arrive, when the stock manager records the goods receipt and enters received quantities per line item, then the system increments stock at the receiving warehouse and updates the purchase order status to "partially received" or "fully received."
- Given the received quantity differs from the ordered quantity, then the system flags the variance.
- Given the goods receipt is confirmed, then an immutable stock movement record of type "purchase_receipt" is created.

**FR Reference:** FR-INV-006, FR-SUP-004

**Priority:** Must Have

---

**US-INV-002:** As a stock manager, I want to record a stock adjustment with a reason code so that unplanned changes in stock levels are documented and traceable.

**Acceptance Criteria:**

- Given the stock manager initiates a stock adjustment, when no reason code is entered, then the system prevents saving.
- Given the adjustment value (quantity x cost price) is below the configured approval threshold, then the adjustment is applied immediately.
- Given the adjustment value exceeds the threshold, then the adjustment is held in "pending_approval" status and a push notification is sent to the manager.

**FR Reference:** FR-INV-009

**Priority:** Must Have

---

**US-INV-003:** As a stock manager, I want to initiate a physical stock count for selected products so that I can verify that system quantities match the physical shelf.

**Acceptance Criteria:**

- Given the stock manager initiates a stock count for a set of products, when the count window is open, then stock movements for those products are frozen.
- Given physical quantities are entered per product per location, when the count is submitted, then the system calculates the variance (physical - system).
- Given the variance is submitted, then a pending adjustment is created for manager approval before the count result is applied.

**FR Reference:** FR-INV-014

**Priority:** Must Have

---

**US-INV-004:** As a stock manager, I want to approve a stock variance after counting so that only verified adjustments are committed to stock records.

**Acceptance Criteria:**

- Given a stock count variance is pending approval, when the manager reviews and approves it, then the system applies the adjustment and creates an immutable stock movement record.
- Given the manager rejects the variance, then the count result is discarded and the original system quantity is retained.

**FR Reference:** FR-INV-014

**Priority:** Must Have

---

**US-INV-005:** As a stock manager, I want to transfer stock between branches so that the system tracks the goods while they are in transit and credits the destination only on confirmed receipt.

**Acceptance Criteria:**

- Given the stock manager initiates a transfer from a source warehouse, when the transfer is created, then stock is decremented at the source and placed in "in_transit" status.
- Given the receiving branch confirms receipt, then stock is credited to the destination warehouse.
- Given the receiving confirmation has not been made, then the stock remains in "in_transit" and is not counted at either location.

**FR Reference:** FR-INV-008

**Priority:** Must Have

---

**US-INV-006:** As a stock manager, I want to receive an alert when a product is approaching its expiry date so that I can take action before the goods expire.

**Acceptance Criteria:**

- Given a product has batch tracking enabled and a batch expiry date is within the configured alert threshold (30, 60, or 90 days), then the batch appears in the near-expiry alert list on the dashboard.
- Given the stock manager opens the near-expiry list, then the system shows: product name, batch number, expiry date, and current stock quantity.

**FR Reference:** FR-INV-012

**Priority:** Must Have

---

## Customer Management (F-003)

**US-CUS-001:** As an accountant, I want to view the debtors ageing report so that I can prioritise collection of overdue customer balances.

**Acceptance Criteria:**

- Given the accountant requests the debtors ageing report, when the report loads, then it lists all customers with outstanding balances grouped by: 0-30 days, 31-60 days, 61-90 days, and over 90 days.
- Given the report is displayed, then it shows the total outstanding per customer and per bucket.

**FR Reference:** FR-CUS-006

**Priority:** Must Have

---

**US-CUS-002:** As an accountant, I want to generate a customer statement so that I can send the customer a summary of all transactions and their closing balance.

**Acceptance Criteria:**

- Given the accountant selects a customer and a date range, when the statement is generated, then it lists all transactions (sales, returns, payments) with a running balance and a closing balance.
- Given the statement is generated, then the accountant can download it as a PDF.

**FR Reference:** FR-CUS-007

**Priority:** Must Have

---

**US-CUS-003:** As a stock manager, I want the system to enforce credit limits at the POS so that customers cannot exceed their approved credit without a manager override.

**Acceptance Criteria:**

- Given a credit sale would cause the customer's balance to exceed their credit limit, when the cashier attempts to complete the sale, then the system blocks completion and requires a manager-level user to approve the override with a reason code.
- Given the manager approves the override, then the sale proceeds and the override is logged with the manager's name and reason.

**FR Reference:** FR-CUS-004, FR-POS-014

**Priority:** Must Have

---

## Supplier and Vendor Management (F-004)

**US-SUP-001:** As an accountant, I want to record a supplier payment so that the supplier's outstanding balance is reduced and the payment is linked to the correct invoice.

**Acceptance Criteria:**

- Given the accountant selects a supplier and a payment amount, when the payment is recorded with method and date, then the supplier's outstanding balance is decremented.
- Given the payment is partial, then the remaining balance is retained and visible.
- Given the payment is recorded, then a payment record appears in the supplier's transaction history.

**FR Reference:** FR-SUP-006

**Priority:** Must Have

---

**US-SUP-002:** As an accountant, I want the system to flag invoice discrepancies during three-way matching so that I do not pay a supplier for goods or amounts that do not match the purchase order.

**Acceptance Criteria:**

- Given a goods receipt is confirmed and the supplier invoice amount differs from the purchase order total or received quantity value, when the accountant attempts to approve the invoice, then the system flags the discrepancy.
- Given the discrepancy is flagged, then payment of the invoice is blocked until a manager resolves it.

**FR Reference:** FR-SUP-005

**Priority:** Must Have

---

**US-SUP-003:** As a stock manager, I want to create a purchase order for a supplier so that I have a formal documented request for goods that can be shared with the supplier as a PDF.

**Acceptance Criteria:**

- Given the stock manager creates a purchase order with products, quantities, and agreed prices, when the order is saved, then the system calculates the order total and generates a PDF formatted with the business logo and address.
- Given the PDF is generated, then the stock manager can download or share it.

**FR Reference:** FR-SUP-003

**Priority:** Must Have

---

**US-SUP-004:** As an accountant, I want to generate a supplier statement so that I have a reconciled view of all orders, receipts, and payments for a supplier within a date range.

**Acceptance Criteria:**

- Given the accountant selects a supplier and a date range, when the statement is generated, then it lists all purchase orders, goods receipts, invoices, and payments with a closing balance.

**FR Reference:** FR-SUP-007

**Priority:** Should Have
