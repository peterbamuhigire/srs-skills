# Domain: Retail

## Profile

| Property | Value |
|---|---|
| **Regulatory Bodies** | FTC, PCI SSC, Data protection authorities (EU, state-level) |
| **Key Standards** | PCI-DSS v4.0, GDPR, CCPA, Consumer Protection laws |
| **Risk Level** | Medium — payment card data, consumer PII |
| **Audit Requirement** | PCI-DSS requires annual assessment |
| **Data Classification** | Cardholder Data (CHD), Consumer PII, Order History |

## Default Feature Modules

- Product Catalog & Inventory
- Point of Sale
- E-commerce & Orders
- Customer Loyalty

## Auto-Injected Requirements

See `references/nfr-defaults.md` for the full list of `[DOMAIN-DEFAULT]` requirements
injected into new retail projects at scaffold time.

Key injected areas:
- **NFR:** PCI-DSS card data protection, checkout performance, GDPR/CCPA erasure rights, inventory accuracy
- **FR:** Cookie consent management, consumer data export/deletion, payment tokenization
- **Interfaces:** Payment gateway APIs, inventory management system sync, loyalty platform integration

## References

- [regulations.md](references/regulations.md) — PCI-DSS, GDPR, CCPA, FTC Act, ADA Title III
- [architecture-patterns.md](references/architecture-patterns.md) — payment tokenization, inventory sync, cart/checkout, returns, multi-channel
- [security-baseline.md](references/security-baseline.md) — PCI scope minimization, tokenization, 3D Secure, fraud scoring, consent management
- [nfr-defaults.md](references/nfr-defaults.md) — default non-functional requirements for injection

## Feature Reference

- [product-catalog.md](features/product-catalog.md)
- [point-of-sale.md](features/point-of-sale.md)
- [ecommerce-orders.md](features/ecommerce-orders.md)
- [customer-loyalty.md](features/customer-loyalty.md)
