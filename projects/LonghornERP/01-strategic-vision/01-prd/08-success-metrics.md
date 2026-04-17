# Success Metrics

All metrics below are measurable thresholds. Each constitutes a pass/fail criterion that must be verified before the Phase 1 launch gate is approved.

## Usability: Unassisted Task Success Rate

The system shall achieve a ≥ 85% unassisted task success rate across the following 5 benchmark tasks, measured in moderated usability testing with participants who have not received prior training on the system.

| Task ID | Task Description | Pass Criterion |
|---|---|---|
| **UT-01** | Create and send a sales invoice to a customer | Completed without requesting help and without dead-end navigation |
| **UT-02** | Record a payment received against an outstanding invoice | Completed without requesting help and without dead-end navigation |
| **UT-03** | Check current stock level for a specified item | Completed without requesting help and without dead-end navigation |
| **UT-04** | Submit a leave request for an employee | Completed without requesting help and without dead-end navigation |
| **UT-05** | Run monthly payroll for a specified pay group | Completed without requesting help and without dead-end navigation |

*Measurement method: moderated usability test, minimum 10 participants per task, recruited from target user personas (Finance Manager, Operations Manager, HR Officer, Sales Executive, and CEO/Owner).*

*Failure definition: participant requests verbal guidance, or navigates to a dead end and requires backtracking more than once.*

## Performance: Page Response Time

The system shall load any page in ≤ 2 seconds at the 95th percentile (P95) under a concurrent load of 100 active users, measured at the application server boundary with no client-side caching.

| Metric | Threshold |
|---|---|
| Page load time (P95, 100 concurrent users) | ≤ 2 seconds |
| API response time for read operations (P95, 100 concurrent users) | ≤ 800 ms |
| API response time for write operations (P95, 100 concurrent users) | ≤ 1,500 ms |

*Measurement method: load testing tool (e.g., k6 or Apache JMeter) simulating 100 concurrent users performing mixed read/write operations over a 10-minute sustained run.*

## Availability: Platform Uptime

The system shall maintain ≥ 99.5% uptime measured on a rolling 30-day window, excluding pre-announced maintenance windows of ≤ 4 hours per calendar month.

| Metric | Threshold |
|---|---|
| Rolling 30-day uptime | ≥ 99.5% |
| Maximum unplanned downtime per 30 days | ≤ 3.6 hours |
| *Recovery Time Objective* (RTO) | ≤ 2 hours |
| *Recovery Point Objective* (RPO) | ≤ 1 hour |

*Measurement method: external uptime monitoring service polling the application health endpoint at 1-minute intervals.*

## Tenant Provisioning Time

The system shall provision a new tenant — from subscription payment confirmation to first authenticated login — in ≤ 10 minutes, with no manual intervention by Chwezi operations staff.

| Metric | Threshold |
|---|---|
| End-to-end tenant provisioning time | ≤ 10 minutes |
| Manual operations steps required | 0 |

*Measurement method: automated provisioning test run at each deployment; time recorded from payment webhook receipt to successful first login.*

## Revenue Milestones

| Phase | Market | MRR Target (UGX) | MRR Target (USD equiv.) | Timeline |
|---|---|---|---|---|
| Phase 1 | Uganda | UGX 56M | ~$15K | Launch year |
| Phase 2 | East Africa | UGX 188M | ~$50K | 24 months post-launch |
| Phase 3 | Francophone Africa | UGX 450M | ~$120K | 36 months post-launch |
| Phase 4 | Enterprise + Global | UGX 1.1B+ | ~$300K+ | 48–60 months post-launch |

*Revenue milestones are gate criteria for market expansion phases. Phase 2 development budget is not released until Phase 1 MRR target is achieved for two consecutive months.*

## Security and Compliance

| Metric | Threshold |
|---|---|
| Tenant data isolation failures in penetration test | 0 |
| Critical security vulnerabilities unpatched for > 7 days | 0 |
| URA EFRIS submission success rate | ≥ 99% of valid invoices submitted within 24 hours |
