# Feature: Customer Loyalty

## Description
Customer loyalty program management — point accrual, tier management,
reward redemption, personalized offers, and privacy-compliant member
data handling.

## Standard Capabilities
- Loyalty account enrollment and profile management
- Points accrual rules (per dollar spent, bonus events, partner earn)
- Tier qualification tracking (e.g., Silver, Gold, Platinum) with tier benefits
- Points balance inquiry and transaction history
- Reward catalog and points redemption at checkout (POS and e-commerce)
- Expiry management and member notification of expiring points
- Targeted offer and coupon distribution (email, app, in-store)
- Referral program tracking
- Member data export (GDPR/CCPA portability request)
- Marketing consent management (opt-in/opt-out per channel)
- De-duplication and account merge for members with multiple identifiers

## Regulatory Hooks
- GDPR Art. 6: legitimate interest or explicit consent required for processing member data for marketing
- CCPA: members may opt out of the sale or sharing of their personal information with third-party marketing partners
- CAN-SPAM / CASL: all marketing emails must include a one-click unsubscribe and honor requests within 10 business days
- FTC: program terms (earn rates, expiry, partner participation) must be clearly disclosed at enrollment

## Linked NFRs
- RET-NFR-003 (Consumer Data Rights — loyalty member data subject to GDPR/CCPA erasure and portability)
- RET-NFR-002 (Checkout Performance — loyalty points lookup must not add latency to checkout flow)
- RET-NFR-005 (High Availability — redemption must be available during peak sales events)
