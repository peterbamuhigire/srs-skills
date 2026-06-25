# Feature: Omnichannel Fulfilment & Returns

## Description

Order fulfilment and reverse-logistics capabilities across store, warehouse, ship-from-store, pickup, delivery, marketplace, and return channels.

## Standard Capabilities

- Available-to-promise calculation by channel, fulfilment node, stock status, reservation, and cut-off time.
- Inventory reservation at checkout with timeout, release, substitution, cancellation, and oversell exception logic.
- Fulfilment routing by cost, promise date, inventory availability, labour capacity, store priority, and customer option.
- Buy-online-pick-up-in-store, reserve-online-pick-up-in-store, ship-from-store, home delivery, and locker/pickup partner options.
- Fulfilment status at order-line level: reserved, allocated, picking, packed, ready, dispatched, delivered, cancelled, failed.
- Exception flows for partial fulfilment, unavailable items, failed pickup, failed delivery, damaged goods, and customer service override.
- Return initiation, eligibility check, reason capture, inspection, refund/exchange, restock, quarantine, repair, vendor return, donation, disposal.
- Return fraud review for high-risk items, repeated behaviour, receipt mismatch, or policy exception.
- Reverse-logistics cost and disposition reporting.

## Finance and Control Hooks

- Refunds must link to original order, tender, return reason, inspection result, approver where required, and settlement status.
- Restock decisions must create inventory source events and preserve disposition evidence.
- Disposal, damage, vendor return, and quarantine must route to inventory valuation and write-down controls.
- Fulfilment cost and return cost should be available for contribution margin analysis where finance scope includes profitability.

## Linked NFRs

- RET-NFR-002 Checkout Performance
- RET-NFR-004 Inventory Accuracy
- RET-NFR-007 Retail Event Auditability
- RET-NFR-008 Dashboard Freshness
