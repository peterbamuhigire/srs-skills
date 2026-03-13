# Retail: Architecture Patterns

## Payment Tokenization (Never Store Raw PANs)

- Raw PANs must be replaced with a payment token at the point of entry (client-side tokenization preferred)
- The token vault (PAN-to-token mapping) must reside in the CDE, separated from the main application database
- The application layer stores only tokens; it must never have access to the token vault decryption keys
- Recurring billing must use network tokens (Visa Token Service, Mastercard MDES) where available

```
Browser/POS Terminal → [TLS] → Payment Gateway (tokenizes PAN) → Token returned to Application
Application stores: token, last-4, card brand, expiry (month/year only)
Application never stores: full PAN, CVV/CVC, full track data
```

## Inventory Sync Patterns

- Inventory quantities must be the single source of truth in the inventory service; no duplicate counters
- Real-time sync between warehouse management, POS, and e-commerce storefronts using event streaming
- Inventory reservations (holds) must be applied atomically at checkout initiation; released on timeout or cancellation
- Stock level changes must be broadcast to all channels within 5 seconds to prevent oversell

## Cart and Checkout Flow

```
Add to Cart → Cart Validation (price, availability) → Address Entry →
Shipping Selection → Payment Entry (tokenized) → Order Preview →
Place Order → Inventory Deduction → Payment Authorization →
Order Confirmation → Fulfillment Queue
```

- Cart state must be persisted server-side for authenticated users; guest carts use signed session tokens
- Checkout must validate inventory availability immediately before payment authorization to prevent oversell
- GDPR/CCPA consent collection must occur at account creation and must not block checkout progress

## Returns and Refund Workflows

- Returns must be linked to the original order ID for audit trail integrity
- Refunds must reverse the original payment method wherever possible
- Restocking must trigger inventory quantity updates within the same atomic operation as the return record creation
- Refund authorization must follow the same maker-checker pattern as high-value payment transactions

## Multi-Channel Order Management

- A single order management system (OMS) must be the system of record for all orders regardless of channel (web, mobile, in-store, marketplace)
- Channel identifiers must be recorded on every order for attribution and fulfillment routing
- Split-ship and partial fulfillment must be supported with status tracking at the line-item level
