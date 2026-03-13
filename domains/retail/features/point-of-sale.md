# Feature: Point of Sale

## Description
In-store and kiosk transaction processing — product lookup, cart management,
payment acceptance (card present, contactless, cash, gift card), receipt
issuance, and end-of-day reconciliation.

## Standard Capabilities
- Barcode and QR code scanning for product lookup
- Cart management with quantity adjustment and discount application
- Split-tender payment (multiple payment methods per transaction)
- Card-present payment acceptance (chip/tap/swipe via payment terminal)
- Cash payment with change calculation
- Gift card and store credit acceptance and balance inquiry
- Return and exchange processing at point of sale
- Employee identification and shift management
- End-of-day cash drawer reconciliation and Z-report generation
- Receipt printing and email receipt option
- Offline mode with transaction queue for intermittent connectivity

## Regulatory Hooks
- PCI-DSS: payment terminals must be PCI PTS-certified; terminal serial numbers must be logged
- PCI-DSS Req. 9.9: terminals must be inspected for tampering; a terminal inspection log must be maintained
- FTC: receipt must display the return policy
- Sales tax: tax rates must be applied per jurisdiction; nexus rules determine which transactions are taxable
- ADA: kiosk interfaces must be accessible (reachable controls, audio output option)

## Linked NFRs
- RET-NFR-001 (Cardholder Data Protection — card-present transactions in CDE scope)
- RET-NFR-004 (Inventory Accuracy — POS sales must decrement inventory in real time)
- RET-NFR-005 (High Availability — POS unavailability directly halts sales)
