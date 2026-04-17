# Opportunity Management

## 3.1 Opportunity Record

**FR-CRM-008** — When a lead is converted to an opportunity, the system shall create an opportunity record with: opportunity ID (`OPP-YYYY-NNNN`), linked contact, linked company, assigned sales representative, pipeline stage (configurable: Prospecting → Qualification → Proposal → Negotiation → Closed Won/Lost), estimated value, expected close date, and close probability (%).

**FR-CRM-009** — The system shall provide a Kanban pipeline board displaying all open opportunities in columns matching the pipeline stages; dragging an opportunity card between columns shall update the stage and record the stage change with timestamp in the opportunity history.

**FR-CRM-010** — When an opportunity is moved to "Closed Won", the system shall link the opportunity to an existing or new quotation in the Sales module; the link shall be mandatory — the system shall not permit closure without a linked sales quotation or order.

**FR-CRM-011** — When an opportunity is moved to "Closed Lost", the system shall require the user to select a lost reason (configurable: Price, Competitor, No Budget, No Decision, Wrong Fit) and enter a brief narrative; this data feeds the lost deal analysis in Section 8.

## 3.2 Opportunity Scoring

**FR-CRM-012** — The system shall compute a weighted pipeline value for each opportunity: $WeightedValue = EstimatedValue \times (CloseProb \div 100)$; the pipeline dashboard shall display both total pipeline value and total weighted pipeline value per representative and per team.

**FR-CRM-013** — The system shall automatically reduce the close probability of an opportunity by a configurable amount (default: 10%) for each full calendar week past the expected close date that the opportunity remains open, until a minimum probability of 10% is reached.

## 3.3 Opportunity Collaboration

**FR-CRM-014** — The system shall allow multiple sales team members to be added to an opportunity as collaborators; each collaborator shall be able to log activities and view the opportunity record, but only the opportunity owner may change the stage or close the deal.
