# Traceability Matrix

## 10.1 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Revenue visibility: pipeline forecasting reduces missed targets by surfacing at-risk deals before month-end. |
| BG-002 | Field productivity: mobile CRM allows reps to log activities, access customer data, and submit quotations without returning to the office. |
| BG-003 | Win-rate improvement: systematic lost deal analysis identifies patterns that inform product and pricing decisions. |
| BG-004 | Customer retention: NPS tracking surfaces dissatisfied customers before they churn. |
| BG-005 | Account growth discipline: account hierarchies, segmentation, whitespace analysis, and lightweight account plans help teams grow strategic customers intentionally. |
| BG-006 | Service resolution and renewal protection: case routing, SLA control, escalation, and service-to-renewal feedback reduce avoidable churn and protect expansions. |
| BG-007 | Commercial governance: pipeline stage controls, approval visibility, partner/channel controls, and quote-to-cash handoff context reduce execution errors between CRM and ERP. |

## 10.2 Functional Requirement Traceability

| Requirement ID | Requirement Summary | Business Goal(s) |
|---|---|---|
| FR-CRM-001 | Lead capture fields and source tracking | BG-001, BG-002 |
| FR-CRM-002 | Bulk lead import with validation and duplicate checks | BG-001, BG-002 |
| FR-CRM-003 | Unique lead IDs and audit fields | BG-001 |
| FR-CRM-004 | Lead qualification and conversion to opportunity | BG-001 |
| FR-CRM-005 | Lead disqualification reasons and retention | BG-001, BG-003 |
| FR-CRM-006 | Territory-based lead assignment | BG-001, BG-002 |
| FR-CRM-007 | Uncontacted-lead follow-up alerts | BG-001, BG-002 |
| FR-CRM-008 | Opportunity record creation and core fields | BG-001 |
| FR-CRM-009 | Kanban pipeline board and stage history | BG-001 |
| FR-CRM-010 | Closed-won linkage to quotation or order | BG-001, BG-007 |
| FR-CRM-011 | Closed-lost reason capture and narrative | BG-003 |
| FR-CRM-012 | Weighted pipeline value calculation | BG-001 |
| FR-CRM-013 | Probability decay for overdue opportunities | BG-001 |
| FR-CRM-014 | Opportunity collaboration roles | BG-001, BG-002 |
| FR-CRM-015 | Supported CRM activity types | BG-002 |
| FR-CRM-016 | Call activity capture | BG-002 |
| FR-CRM-017 | Email activity capture | BG-002 |
| FR-CRM-018 | Meeting activity capture and actions | BG-002 |
| FR-CRM-019 | Activity calendar view | BG-002 |
| FR-CRM-020 | Overdue-activity dashboard and digest | BG-002 |
| FR-CRM-021 | Read-only chronological activity timeline | BG-002, BG-007 |
| FR-CRM-022 | Contact record fields and customer linkage | BG-002, BG-005 |
| FR-CRM-023 | Duplicate-email prevention for contacts | BG-002 |
| FR-CRM-024 | Multi-company and multi-opportunity contact associations | BG-002, BG-005 |
| FR-CRM-025 | Fuzzy duplicate check for contacts | BG-002 |
| FR-CRM-026 | Contact communication preferences | BG-002, BG-004 |
| FR-CRM-027 | Monthly sales forecast generation | BG-001 |
| FR-CRM-028 | Forecast accuracy reporting | BG-001 |
| FR-CRM-029 | Quarterly forecast scenarios | BG-001 |
| FR-CRM-030 | Manager forecast overrides with justification | BG-001, BG-007 |
| FR-CRM-031 | Territory master data | BG-001, BG-002 |
| FR-CRM-032 | Out-of-territory opportunity override control | BG-001, BG-007 |
| FR-CRM-033 | Territory performance reporting | BG-001, BG-003 |
| FR-CRM-034 | Lost-deal analysis reporting | BG-003 |
| FR-CRM-035 | Competitor win-frequency reporting | BG-003 |
| FR-CRM-036 | NPS survey dispatch after delivery | BG-004 |
| FR-CRM-037 | NPS scoring and categorisation | BG-004 |
| FR-CRM-038 | Rolling 90-day NPS calculation | BG-004 |
| FR-CRM-039 | Detractor follow-up task creation | BG-004, BG-006 |
| FR-CRM-040 | Mobile CRM functions for field representatives | BG-002 |
| FR-CRM-041 | Offline mobile CRM operation | BG-002 |
| FR-CRM-042 | Mobile route optimisation view | BG-002 |
| FR-CRM-043 | Account master data and ERP customer linkage | BG-005, BG-007 |
| FR-CRM-044 | Parent-child account hierarchies and rollups | BG-005, BG-006 |
| FR-CRM-045 | Account-team role management | BG-005, BG-006 |
| FR-CRM-046 | Segmentation, tiering, whitespace, and product-fit indicators | BG-005 |
| FR-CRM-047 | Lightweight account plans | BG-005 |
| FR-CRM-048 | Configurable pipeline stage-exit criteria | BG-001, BG-007 |
| FR-CRM-049 | Mandatory date-bound next steps on opportunities | BG-001, BG-007 |
| FR-CRM-050 | Stale-pipeline detection and escalation | BG-001, BG-007 |
| FR-CRM-051 | Deal, discount, and risk-approval visibility | BG-001, BG-007 |
| FR-CRM-052 | Governed quote-to-cash handoff context from CRM to Sales or ERP | BG-001, BG-007 |
| FR-CRM-053 | Downstream quote-to-cash status synchronisation back to CRM | BG-001, BG-007 |
| FR-CRM-054 | Immutable CRM-to-ERP handoff history | BG-007 |
| FR-CRM-055 | Case creation from manual, email, self-service, or transactional context | BG-006, BG-007 |
| FR-CRM-056 | Case classification, impact, and default SLA application | BG-006 |
| FR-CRM-057 | Configurable case routing rules | BG-006, BG-007 |
| FR-CRM-058 | SLA targets and case timer visibility | BG-006 |
| FR-CRM-059 | SLA-risk and breach escalation | BG-006 |
| FR-CRM-060 | Chronological non-destructive case worklog | BG-006, BG-007 |
| FR-CRM-061 | Controlled case closure with resolution evidence | BG-006, BG-007 |
| FR-CRM-062 | Controlled case reopen handling | BG-006, BG-007 |
| FR-CRM-063 | Service analytics for backlog, SLA, reopen rate, and resolution | BG-006 |
| FR-CRM-064 | Service-to-renewal and expansion feedback alerts | BG-004, BG-006 |
| FR-CRM-065 | Partner and channel account classification | BG-005, BG-007 |
| FR-CRM-066 | Partner-led and partner-influenced opportunity tracking | BG-001, BG-007 |
| FR-CRM-067 | Configurable partner visibility scopes | BG-007 |
| FR-CRM-068 | Customer lifecycle status and history | BG-004, BG-005, BG-006 |
| FR-CRM-069 | Renewal and retention risk scoring | BG-004, BG-006 |
| FR-CRM-070 | Renewal and expansion workbench | BG-004, BG-005, BG-006 |
| FR-CRM-071 | Periodic lifecycle reviews for strategic or at-risk accounts | BG-005, BG-006 |

## 10.3 Non-Functional Requirement Traceability

| Requirement ID | Requirement Summary | Supported Goal(s) |
|---|---|---|
| NFR-CRM-001 | Pipeline board performance | BG-001, BG-002 |
| NFR-CRM-002 | Forecast-report performance | BG-001 |
| NFR-CRM-003 | Tenant isolation and security | BG-007 |
| NFR-CRM-004 | NPS dispatch timeliness and retry handling | BG-004 |
| NFR-CRM-005 | CRM data-quality controls | BG-005, BG-007 |
| NFR-CRM-006 | Mobile and field usability | BG-002 |
| NFR-CRM-007 | Access control and privacy enforcement | BG-006, BG-007 |
| NFR-CRM-008 | Routing and escalation timeliness | BG-001, BG-006, BG-007 |
| NFR-CRM-009 | SLA and handoff auditability | BG-006, BG-007 |
| NFR-CRM-010 | Reporting trust and metric reproducibility | BG-001, BG-006, BG-007 |

## 10.4 Context Gaps

| ID | Context Gap | Impact |
|---|---|---|
| GAP-010 | GIS territory polygon support is a future enhancement; initial implementation uses country or region text fields only. | Territory assignment remains rules-based without native geospatial polygon management in the initial release. |
