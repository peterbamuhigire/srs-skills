# Lost Deal Analysis, Customer Satisfaction, and Mobile CRM

## 7.1 Lost Deal Analysis

**FR-CRM-034** — The system shall provide a lost deal analysis report for any selected period, showing: total deals lost, total value lost, breakdown by lost reason (count and value per reason), breakdown by competitor (where competitor attribution was recorded), win/loss ratio per sales representative, and average days in pipeline before loss.

**FR-CRM-035** — The system shall display a competitor win frequency table: for each competitor named in lost-deal records, the table shall show how many deals they won against Longhorn ERP clients and the combined value of those deals.

## 7.2 Customer Satisfaction (NPS)

**FR-CRM-036** — The system shall support NPS survey dispatch: when a sales order is delivered and the delivery note is confirmed, the system shall queue an NPS survey to be sent to the customer's registered email address after a configurable delay (default: 3 days).

**FR-CRM-037** — The NPS survey shall ask: "How likely are you to recommend [TenantName] to a friend or colleague?" on a 0–10 scale; the system shall categorise responses: 0–6 Detractors, 7–8 Passives, 9–10 Promoters.

**FR-CRM-038** — The system shall compute the rolling 90-day NPS score as: $NPS = \%Promoters - \%Detractors$; the NPS score shall be displayed on the CRM dashboard and updated whenever a new survey response is received.

**FR-CRM-039** — When a Detractor response is received (score 0–6), the system shall create an automatic follow-up task assigned to the account manager to contact the customer within 48 hours.

## 7.3 Mobile CRM for Field Representatives

**FR-CRM-040** — The mobile CRM application shall allow field representatives to: view their assigned leads and opportunities, log activities (call, meeting, WhatsApp), update opportunity stages, create quotations, and view the customer's account balance and recent invoices.

**FR-CRM-041** — The mobile CRM shall support offline operation: all lead, opportunity, and contact data shall be cached locally; activities logged offline shall be queued and synchronised when connectivity is restored.

**FR-CRM-042** — The mobile CRM shall provide a route optimisation view showing the field rep's scheduled visits for the day on a map, ordered by travel distance from their current GPS location.

## 7.4 Non-Functional Requirements

**NFR-CRM-001** — The Kanban pipeline board shall load all opportunities for the current user within 2 seconds for a pipeline of ≤ 500 open opportunities.

**NFR-CRM-002** — The sales forecast report shall compute within 3 seconds for a dataset of ≤ 1,000 opportunities in the selected period.

**NFR-CRM-003** — CRM data (leads, opportunities, activities, contacts) shall be tenant-isolated; no cross-tenant data leakage shall be possible at the API layer, validated during security penetration testing.

**NFR-CRM-004** — NPS survey emails shall be dispatched within 24 hours of the configured post-delivery delay; delivery failure shall be retried up to 3 times with 6-hour intervals.

## 7.5 Traceability Matrix

| Requirement ID | Requirement Summary | Business Goal |
|---|---|---|
| FR-CRM-001–007 | Lead capture, qualification, routing | BG-001, BG-002 |
| FR-CRM-008–014 | Opportunity management, Kanban, scoring | BG-001 |
| FR-CRM-015–021 | Activity logging, calendar, timeline | BG-002 |
| FR-CRM-022–026 | Contact management, deduplication | BG-002 |
| FR-CRM-027–033 | Forecasting, territory management | BG-001, BG-003 |
| FR-CRM-034–035 | Lost deal analysis | BG-003 |
| FR-CRM-036–039 | NPS surveys and follow-up | BG-004 |
| FR-CRM-040–042 | Mobile CRM for field reps | BG-002 |

**Context gaps:**
- `[CONTEXT-GAP: GAP-010]` — GIS territory polygon support is a future enhancement; initial implementation uses country/region text fields only.
