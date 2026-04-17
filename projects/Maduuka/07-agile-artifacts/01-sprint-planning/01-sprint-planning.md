---
title: "Sprint Planning Guidelines — Maduuka Phase 1"
version: "1.0"
date: "2026-04-05"
status: "Approved"
owner: "Peter Bamuhigire"
---

# Sprint Planning Guidelines — Maduuka Phase 1

## Section 1: Sprint Structure

**Sprint duration:** 2 weeks.

**Team size:** 2–5 people. Velocity targets are adjusted proportionally based on active headcount at sprint planning.

**Ceremony schedule:**

1. *Sprint Planning* (Day 1, 2 hours): select stories from the backlog, confirm each story satisfies the Definition of Ready, assign tasks to team members, and confirm the sprint goal.
2. *Daily Standup* (each morning, 15 minutes): each team member answers three questions — what did I complete since yesterday, what will I complete today, and what is blocking me.
3. *Sprint Review* (Day 14, 1 hour): demo working software on the staging environment to Peter. Only features that satisfy the Definition of Done are demonstrated.
4. *Sprint Retrospective* (Day 14, 30 minutes): structured discussion — what worked well this sprint, what should we improve, and what one action will we take in the next sprint.

## Section 2: Phase 1 Sprint Plan (Reference)

The 15 web completion phases from `projects/Maduuka/04-development-artifacts/` map to sprints as follows. This plan assumes a team of 2–3 developers and 20–25 story points per developer per sprint.

| Sprint | Weeks | Phases Covered | Focus |
|---|---|---|---|
| Sprint 1 | Weeks 1–2 | Phase 1 + Phase 2 | Foundation audit and multi-tenant data layer |
| Sprint 2 | Weeks 3–4 | Phase 3 | Authentication and RBAC |
| Sprint 3 | Weeks 5–6 | Phase 4 | POS core |
| Sprint 4 | Weeks 7–8 | Phase 5 + Phase 6 | POS payments and receipts |
| Sprint 5 | Weeks 9–10 | Phase 7 | Inventory management |
| Sprint 6 | Weeks 11–12 | Phase 8 | Customers and suppliers |
| Sprint 7 | Weeks 13–14 | Phase 9 | Expenses and finance |
| Sprint 8 | Weeks 15–16 | Phase 10 + Phase 11 | Reports and HR/Payroll |
| Sprint 9 | Weeks 17–18 | Phase 12 | Dashboard and settings |
| Sprint 10 | Weeks 19–20 | Phase 13 | Integrations (MoMo, Airtel, Africa's Talking) |
| Sprint 11 | Weeks 21–22 | Phase 14 | Security hardening |
| Sprint 12 | Weeks 23–24 | Phase 15 | Performance optimisation and go-live |

*Note: Sprint 10 (Integrations) is blocked until GAP-001 (MTN MoMo Business API credentials) is resolved. See Section 4.*

## Section 3: Velocity Baseline and Estimation

**Complexity point scale (Fibonacci):** 1, 2, 3, 5, 8, 13.

| Points | Meaning |
|---|---|
| 1 | Trivial change: single field, config update, copy fix |
| 2 | Small feature: one screen, one API endpoint, clear acceptance criteria |
| 3 | Medium feature: 2–3 API endpoints, database migration, basic UI |
| 5 | Large feature: cross-cutting concern, multi-step workflow, RBAC integration |
| 8 | Very large: complex module integration, offline sync logic, payment gateway |
| 13 | Epic: must be split before entering a sprint |

**Target velocity:** 20–30 story points per developer per sprint.

**Story size constraint:** no single story may exceed 8 points. Any story estimated at 13 points must be split into smaller stories before it can be included in a sprint backlog.

**Velocity review:** velocity is recalibrated after Sprint 2 using the average of Sprints 1 and 2. Subsequent sprint capacity is set from the rolling 3-sprint average.

## Section 4: Blocker Escalation

**Daily standup protocol:** any blocker identified in standup is assigned an owner and a resolution target before the standup ends. A blocker without an owner is escalated to Peter immediately.

**Named gap owners and escalation targets:**

| Gap | Description | Owner | Escalation Trigger |
|---|---|---|---|
| GAP-001 | MTN MoMo Business API sandbox credentials | Peter | Sprint 10 blocked if not resolved by Week 18 |
| GAP-002 | Data Protection Act 2019 legal review | Peter | No PII collection in production until closed |
| GAP-004 | iOS thermal printer Bluetooth compatibility | Dev team | Phase 2 iOS build blocked |

**Resolution rule:** if a named blocker is not resolved within 2 business days of being raised in standup, the affected story is rescheduled to a later sprint. The sprint goal is revised and Peter is notified at the same time.
