# Payment Handling

## 4.1 Payment Methods

**FR-POS-030** — The system shall support the following payment methods on a single transaction: cash, MTN Mobile Money, Airtel Money, bank card (manual entry), and credit (to customer account); a single transaction shall support split payment across any combination of these methods until the full transaction amount is settled.

**FR-POS-031** — When cash payment is selected, the system shall accept the tendered amount, compute change as: $Change = TenderedAmount - TransactionTotal$, display the change due on screen, and record both tendered amount and change against the session cash reconciliation.

## 4.2 MTN and Airtel Mobile Money Push Payment

**FR-POS-032** — When MTN MoMo or Airtel Money is selected as a payment method, the system shall prompt the cashier to enter the customer's phone number; the system shall then invoke the applicable mobile money payment request API, sending the transaction amount and a merchant-generated reference.

**FR-POS-033** — After dispatching the mobile money payment request, the system shall display a pending status and poll the API for payment confirmation at 5-second intervals for a maximum of 120 seconds; if confirmed, the system shall proceed to receipt generation; if the timeout is reached without confirmation, the system shall mark the payment as "Pending" and require cashier action before completing the sale.

**FR-POS-034** — The system shall store the mobile money API transaction reference, network (MTN or Airtel), phone number used, and confirmation timestamp against each mobile money payment record.

## 4.3 Split Payments

**FR-POS-035** — When a cashier applies a split payment, the system shall display a payment summary showing the total transaction amount, the amount already paid by each applied method, and the outstanding balance; the cashier shall be able to add payment lines until the outstanding balance reaches zero.

**FR-POS-036** — The system shall prevent completion of a transaction until the sum of all applied payment amounts equals the transaction total; a balance > 0 shall block the confirm action, and a balance < 0 (overpayment) shall trigger the change-due display.

## 4.4 Card Payments (Manual Entry)

**FR-POS-037** — For version 1.0, card payments shall be recorded manually by the cashier entering the card network (Visa/Mastercard/Other), last-4 digits of the card number, and approval code from the physical card terminal; the system shall record these details against the transaction without processing the card electronically.

**FR-POS-038** — The system shall never store full card numbers; the card payment record shall contain only the last-4 digits and the approval code as stated in FR-POS-037.

## 4.5 Payment Reversal

**FR-POS-039** — When a sale return is processed per FR-POS-022 and the original payment was mobile money, the system shall record a mobile money reversal request reference; the actual refund disbursement shall be handled outside the system and confirmed manually by the cashier.

**FR-POS-040** — When a cash refund is issued on a return, the system shall deduct the refund amount from the session cash balance and record it in the session reconciliation as a negative cash movement.
