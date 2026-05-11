# SaaS Revenue Recognition Spec Template (ASC 606 / IFRS 15)

## 1. Contract identification rules

A contract is recognised when:

- All parties have approved (signed order form or click-through).
- Each party's rights are identifiable.
- Payment terms are identifiable.
- The contract has commercial substance.
- Collection is probable.

State the contract types in scope: standard click-through (online signup), enterprise MSA + order form, partner reseller contract.

## 2. Performance obligations

| Obligation | Distinct? | Description |
|------------|-----------|-------------|
| Subscription access | Yes | Right to access SaaS for term |
| Professional services | Yes (if separable) | Implementation, training |
| Premium support | Yes | Higher SLA / named CSM |
| Usage overage | Variable | Beyond-tier consumption |
| Setup fee | Usually combined with subscription | One-time |

## 3. Transaction price

State how variable consideration is estimated (usage forecast), discounts allocated, refunds/credits accrued, and significant financing components (multi-year prepay).

## 4. Allocation to obligations

State the standalone-selling-price (SSP) method (observable price / adjusted market / cost+ / residual). Document the SSP per obligation in a versioned table.

## 5. Recognition pattern per obligation

| Obligation | Pattern | Mechanic |
|------------|---------|----------|
| Subscription | Ratable | Daily accrual = (contract_value / contract_days) |
| Setup fee | Point-in-time | Recognise on activation |
| Professional services | Milestone | Recognise on milestone acceptance |
| Usage overage | Point-in-time | Recognise as consumed |
| Premium support | Ratable | Daily over support term |

## 6. Contract modifications

State how upgrades / downgrades / mid-term changes are handled (prospective vs retrospective treatment). Each modification creates a new versioned contract record.

## 7. Deferred revenue & RPO

- **Deferred revenue** = billed but not yet recognised.
- **RPO (Remaining Performance Obligation)** = contracted but not yet billed + deferred revenue.
- Report monthly to Finance.

## 8. Controls

- Segregation of duties: invoice approval, revenue posting, journal review.
- Quarterly true-up: re-estimate variable consideration.
- Audit-trail: every change to a contract or to a recognition rule has a signed audit entry.

## 9. Disclosures

Required disclosures (for public-co track):

- Disaggregation of revenue by GTM segment / region / product line.
- Contract balances (deferred revenue / RPO).
- Performance-obligation timing.
- Significant judgements (variable consideration, SSP determination).

## 10. References

- ASC 606 — Revenue from Contracts with Customers (FASB).
- IFRS 15 — Revenue from Contracts with Customers (IASB).
- SaaS-specific application guidance: KPMG, Deloitte, EY SaaS revenue guides.
