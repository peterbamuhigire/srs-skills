# Section 2: Power/Interest Grid

The Power/Interest Grid plots all 29 stakeholders across two dimensions:

- **Power (vertical axis):** the stakeholder's authority to affect the project direction, approve or block funding, or mandate compliance. Scored 1–5; plotted as High (≥ 3) or Low (< 3).
- **Interest (horizontal axis):** the degree to which the stakeholder's day-to-day operations or mandate is affected by the BIRDC ERP system. Scored 1–5; plotted as High (≥ 3) or Low (< 3).

The grid produces 4 quadrants, each with a defined engagement strategy.

---

## 2.1 Quadrant Definitions

| Quadrant | Power | Interest | Strategy | Rationale |
|---|---|---|---|---|
| **Manage Closely** | High | High | Maximum engagement. Involve in requirements sign-off, phase-gate reviews, and issue resolution. | These stakeholders can both derail the project and provide the most valuable requirements input. |
| **Keep Satisfied** | High | Low | Regular structured updates. Address concerns proactively. Avoid over-involving in daily detail. | These stakeholders can block or redirect the project despite limited operational interest; keeping them informed prevents escalation. |
| **Keep Informed** | Low | High | Regular operational-level communication. Include in UAT and training. Capture detailed requirements. | Deep operational knowledge, critical for requirements quality. Limited formal authority but high impact on adoption. |
| **Monitor** | Low | Low | Periodic updates via standard reporting channels. No dedicated engagement beyond scheduled project communications. | Minimal risk of derailment; involvement is proportionate to need. |

---

## 2.2 Stakeholder Grid Placement

### Manage Closely — High Power, High Interest

These stakeholders receive the highest engagement intensity. Phase-gate sign-off cannot proceed without their formal acknowledgement.

| ID | Stakeholder | Power | Interest | Key Engagement Action |
|---|---|---|---|---|
| STK-001 | BIRDC Director | 5 | 5 | Monthly steering meeting; bi-weekly brief; final phase-gate sign-off authority |
| STK-002 | Finance Director | 5 | 5 | Weekly requirements review; approves all financial module specifications and deliverables |
| STK-003 | IT Administrator | 4 | 5 | Architecture review sessions; infrastructure co-planning; security specification sign-off |
| STK-026 | Auditor General (OAG Uganda) | 5 | 4 | Audit-readiness maintained continuously; Finance Director is primary interface; audit trail accessible on demand |

---

### Keep Satisfied — High Power, Low Interest

These stakeholders hold formal authority over BIRDC's funding and compliance environment. They do not require detailed day-to-day system involvement but must receive structured, timely assurance.

| ID | Stakeholder | Power | Interest | Key Engagement Action |
|---|---|---|---|---|
| STK-004 | Parliament Budget Committee | 5 | 3 | Progress reports at parliamentary milestone events; audit-ready documentation; value-for-money narrative |
| STK-022 | Uganda Revenue Authority (URA) | 5 | 3 | EFRIS compliance maintained at all times; IT Administrator manages API; Finance Director reviews |
| STK-027 | PPDA | 4 | 3 | Full procurement documentation compliance; annual PPDA compliance report from system |

---

### Keep Informed — Low Power, High Interest

These stakeholders have the deepest operational knowledge of the processes the system will support. Their requirements input is critical; their adoption directly determines whether the system delivers its value.

| ID | Stakeholder | Power | Interest | Key Engagement Action |
|---|---|---|---|---|
| STK-006 | Sales and Marketing Manager | 3 | 5 | Phase 1 requirements sessions; F-001 and F-002 sign-off |
| STK-007 | Procurement Manager | 3 | 5 | Phase 3 requirements sessions; PPDA workflow specification |
| STK-008 | Store Manager | 2 | 5 | Phase 1 UAT lead; dual-track inventory specification |
| STK-009 | Factory / Production Manager | 3 | 5 | Phase 4 requirements; mass balance specification |
| STK-010 | QC Manager | 3 | 5 | Phase 4 CoA and SPC specification |
| STK-012 | Payroll Officer | 2 | 5 | Phase 5 UAT lead for payroll |
| STK-015 | Field Sales Agents (1,071) | 2 | 5 | Pilot UAT group; training materials; Sales Agent App UX testing |
| STK-016 | Factory Floor Workers / Supervisors | 1 | 5 | Phase 4 UAT; Factory Floor App UX testing |
| STK-017 | Warehouse Staff | 1 | 5 | Phase 1 UAT; Warehouse App UX testing |
| STK-018 | Accounts Assistants | 2 | 5 | Phase 2 UAT; Finance Director supervises |
| STK-019 | Cashiers | 1 | 5 | DC-001 test; POS UX validation |
| STK-023 | MTN Uganda / Airtel Uganda | 3 | 3 | API integration testing in Phase 1 and Phase 3 |
| STK-024 | Export Market Buyers | 3 | 3 | CoA template requirements sourced from export contracts |
| STK-025 | NSSF Uganda | 3 | 3 | File format specification; Finance Director reviews submissions |
| STK-029 | BIRDC Cooperative Farmers' Unions | 2 | 4 | Aggregate cooperative payment reports; farmer payment accuracy briefings |

---

### Monitor — Low Power, Low Interest

These stakeholders are tracked via standard reporting channels. No dedicated engagement sessions are required beyond routine project updates.

| ID | Stakeholder | Power | Interest | Key Engagement Action |
|---|---|---|---|---|
| STK-011 | HR Manager | 2 | 4 | Phase 5 requirements input; ZKTeco integration specification |
| STK-013 | Research Coordinator | 1 | 4 | Phase 6 requirements input; quarterly check-in |
| STK-014 | Administration Officer | 2 | 4 | Phase 6 requirements input |
| STK-020 | Cooperative Farmers | 1 | 4 | Represented through Patrick (collections officer) and STK-029 |
| STK-021 | All Staff (HR Self-Service) | 1 | 4 | Phase 5 training; HR Manager oversees rollout |
| STK-028 | ZKTeco | 2 | 3 | IT Administrator obtains device API documentation; Phase 5 integration |

---

## 2.3 Visual Grid Summary

The grid below maps the quadrant positions in text form. Stakeholders are identified by ID only.

```
                         INTEREST
                   Low (1-2)      High (3-5)
                ┌──────────────┬──────────────────────────┐
           High │  KEEP        │  MANAGE CLOSELY          │
  P        (4-5)│  SATISFIED   │  STK-001, STK-002,       │
  O             │  STK-004,    │  STK-003, STK-026        │
  W             │  STK-022,    │                          │
  E             │  STK-027     │                          │
  R        ─────┼──────────────┼──────────────────────────┤
           Low  │  MONITOR     │  KEEP INFORMED           │
          (1-3) │  STK-011,    │  STK-006, STK-007,       │
                │  STK-013,    │  STK-008, STK-009,       │
                │  STK-014,    │  STK-010, STK-012,       │
                │  STK-020,    │  STK-015, STK-016,       │
                │  STK-021,    │  STK-017, STK-018,       │
                │  STK-028     │  STK-019, STK-023,       │
                │              │  STK-024, STK-025,       │
                │              │  STK-029                 │
                └──────────────┴──────────────────────────┘
```
