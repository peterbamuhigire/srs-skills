# Retail: Regulations & Standards Reference

## PCI-DSS v4.0 (Payment Card Industry Data Security Standard)

| Requirement | Citation | Scope |
|---|---|---|
| Protect Cardholder Data | PCI-DSS v4.0 Req. 3 | Never store CVV/CVC; encrypt stored PANs; truncate display to last 4 digits |
| Secure Transmission | PCI-DSS v4.0 Req. 4 | TLS 1.2+ for all cardholder data in transit |
| Access Control | PCI-DSS v4.0 Req. 7–8 | Least privilege, MFA for CDE access, unique user IDs |
| Monitor and Log | PCI-DSS v4.0 Req. 10 | Audit logs of all CDE access; 12-month retention |
| Annual Assessment | PCI-DSS v4.0 Req. 12 | SAQ or QSA assessment based on transaction volume |

### PCI-DSS Merchant Levels

- **Level 1:** > 6 million card transactions/year — requires on-site QSA assessment
- **Level 2–4:** Lower volumes — may self-assess via SAQ with annual attestation

## GDPR (General Data Protection Regulation)

| Provision | Requirement |
|---|---|
| Lawful Basis | Processing consumer data requires a lawful basis (consent, contract, legitimate interest) |
| Right to Erasure | Consumers may request deletion of personal data (Art. 17); retail must honor within 30 days |
| Right to Portability | Consumers may request their order and account data in machine-readable format (Art. 20) |
| Consent | Cookie consent and marketing opt-in must be freely given, specific, informed, and unambiguous |
| Breach Notification | DPA must be notified within 72 hours of a breach affecting EU residents (Art. 33) |

- GDPR applies to any retailer processing personal data of EU/EEA residents, regardless of where the retailer is based

## CCPA (California Consumer Privacy Act)

| Right | Requirement |
|---|---|
| Right to Know | Consumers may request what personal information is collected and shared |
| Right to Delete | Retailers must delete consumer personal information on verified request |
| Right to Opt-Out | Consumers may opt out of the sale or sharing of their personal information |
| Non-Discrimination | Retailers may not discriminate against consumers who exercise CCPA rights |

- CCPA applies to for-profit businesses meeting any of: >$25M annual revenue, >100K consumer records, or >50% revenue from selling personal information
- CPRA (2023): strengthens CCPA with rights to correct data and limit use of sensitive personal information

## FTC Act — Unfair or Deceptive Practices

- Retailers must not make false or misleading claims about products, pricing, or promotions
- Dark patterns that obscure cancellation or manipulate consent are actionable under FTC Act Section 5
- Negative option marketing (auto-renewal) must clearly disclose terms before purchase (Negative Option Rule)

## ADA Title III — E-Commerce Accessibility

- U.S. courts have broadly held that websites are places of public accommodation under ADA Title III
- E-commerce sites must be accessible to users with disabilities; WCAG 2.1 AA is the de facto standard
- Failure to provide accessible checkout and product information is an actionable ADA violation
