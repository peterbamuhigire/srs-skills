# Revenue, Service, and Account Management

## 8.1 Account and Hierarchy Management

**FR-CRM-043** - When a user creates or updates an account, the system shall capture: account name, account type (prospect, customer, partner, former customer), legal entity or trading name, industry, country, territory, assigned account owner, lifecycle status, customer since date, and linked ERP customer record where one exists.

**FR-CRM-044** - The system shall support parent-child account hierarchies so related legal entities, branches, and subsidiaries can be linked under a common group; the account record shall display the hierarchy path and a hierarchy summary showing aggregated open opportunities, open cases, overdue invoices, and latest NPS status across the account family.

**FR-CRM-045** - The system shall support account-team roles on each account, including at minimum account manager, sales representative, service owner, and finance relationship contact; account-team members shall be visible on the account record and available for task assignment, escalation routing, and approval visibility.

**FR-CRM-046** - The system shall support configurable customer segmentation and tiering on accounts, including segment, tier, strategic flag, whitespace indicator, and product-fit indicator fields; administrators shall be able to define scoring or rule-based defaults by industry, size, territory, or installed product base.

**FR-CRM-047** - The system shall provide a lightweight account plan for managed accounts, capturing current products or services, whitespace opportunities, relationship goals, active risks, named stakeholders, planned actions, target review date, and the owner responsible for maintaining the plan.

## 8.2 Pipeline Governance and Quote-to-Cash Handoff

**FR-CRM-048** - The system shall support configurable stage-exit criteria for each pipeline stage; an opportunity shall not move to a later stage unless all mandatory criteria for the target stage are satisfied.

**FR-CRM-049** - Every open opportunity shall require a next-step description, next-step owner, and next-step due date; the system shall block save when an opportunity is updated without a date-bound next step after qualification.

**FR-CRM-050** - When an opportunity has no completed activity for the configured dormancy threshold or its next-step due date passes without completion, the system shall mark the opportunity as stale, alert the opportunity owner, and escalate the exception to the manager dashboard.

**FR-CRM-051** - The opportunity record shall display the visibility status of related commercial approvals, including discount approvals, non-standard term approvals, credit-risk warnings, and other deal-risk approvals received from Sales or ERP workflows; approval status shall be read-only in CRM unless the user has approval authority in the source workflow.

**FR-CRM-052** - When a quotation or sales-order handoff is initiated from CRM, the system shall transmit a governed handoff context to the downstream Sales or ERP flow, including account, contact, opportunity owner, line items, estimated value, expected close or requested start date, billing and shipping context, promised service or delivery commitments, partner attribution where relevant, and any approved non-standard commercial terms.

**FR-CRM-053** - The system shall synchronise key downstream quote-to-cash statuses back into the originating CRM opportunity, including quotation issued, quotation accepted or rejected, order created, order on hold, delivery completed, invoice issued, and payment-status summary where such events are available from integrated modules.

**FR-CRM-054** - The system shall maintain an immutable handoff history between CRM and Sales or ERP records, showing the originating opportunity, transmitted commercial context, receiving quotation or order record, transmission timestamp, sending user, and subsequent downstream status changes.

## 8.3 Service and Case Management

**FR-CRM-055** - The system shall support case creation from manual entry, email intake, customer self-service form, or from a linked sales, delivery, invoice, or opportunity record; each case shall be linked to an account and may additionally be linked to a contact, product, quotation, sales order, delivery note, invoice, or opportunity.

**FR-CRM-056** - When a case is created, the system shall capture at minimum: case ID (`CASE-YYYY-NNNN`), category, subcategory, priority, severity, reported channel, summary, detailed description, customer impact, and requested response; the system shall apply a default SLA policy based on account tier, category, priority, or support agreement.

**FR-CRM-057** - The system shall route cases to queues or named owners using configurable rules based on category, product, territory, language, customer tier, partner attribution, or severity; the applied routing rule and routing timestamp shall be stored in the case history.

**FR-CRM-058** - For every case, the system shall track SLA target timestamps for first response and final resolution; the case record shall display current SLA status as on track, at risk, breached, or paused according to configured business rules.

**FR-CRM-059** - When a case reaches a configured SLA-risk threshold or breaches its SLA, the system shall escalate the case to the configured supervisor or queue, generate a notification, and record the escalation reason and timestamp in the case history.

**FR-CRM-060** - The system shall maintain a complete case worklog including internal notes, external updates, ownership transfers, status changes, attachments, and promised actions; the worklog shall be chronological, non-destructive, and audit-visible.

**FR-CRM-061** - A case shall not be closed unless the user records a resolution code, root-cause classification, resolution summary, closure timestamp, and whether a customer confirmation was obtained where customer confirmation is required by policy.

**FR-CRM-062** - The system shall support controlled case reopen handling; when a closed case is reopened, the system shall preserve the original case reference, record reopen reason, increment a reopen counter, and apply the configured reopened-case SLA policy without deleting prior closure evidence.

**FR-CRM-063** - The system shall provide service analytics showing case backlog, backlog aging, SLA attainment, first-response performance, resolution-time distribution, reopened-case rate, and resolution-code breakdown by team, account tier, product, and period.

**FR-CRM-064** - When severe or repeated service issues occur on an account, or when a case breaches configured renewal-risk thresholds, the system shall create an account-level lifecycle alert and notify the account owner so the issue can be considered in retention, renewal, or expansion planning.

## 8.4 Partner, Channel, and Customer Lifecycle Management

**FR-CRM-065** - The system shall support partner and channel account types, including distributor, reseller, referral partner, and implementation partner classifications, with fields for partner tier, territory coverage, assigned channel manager, and active-status flag.

**FR-CRM-066** - The system shall support partner-influenced and partner-led opportunity tracking, including deal-registration reference, partner role, end-customer account, conflict status, and partner-attributed pipeline and revenue reporting.

**FR-CRM-067** - Where a partner is linked to an opportunity or case, the system shall support configurable partner visibility rules so external or partner-facing users can be limited to the records, fields, and actions authorised for that partner relationship.

**FR-CRM-068** - The system shall maintain a customer lifecycle status for each account, with at minimum Prospect, New Customer, Active Customer, Renewal Due, At Risk, and Churned states; lifecycle-state changes shall be timestamped and preserved in account history.

**FR-CRM-069** - The system shall compute a configurable renewal or retention risk indicator for active accounts using signals such as unresolved high-severity cases, repeated SLA breaches, detractor NPS responses, declining order patterns, overdue receivables, or prolonged account inactivity.

**FR-CRM-070** - The system shall provide a renewal and expansion workbench for account owners showing upcoming renewal dates, expiring service agreements or contracts where such records exist, current whitespace indicators, open service risks, latest NPS result, and the next required retention or expansion action.

**FR-CRM-071** - For strategic or at-risk accounts, the system shall require periodic lifecycle reviews; the review shall record account health, top risks, top opportunities, committed actions, executive attention flag, and the next review date.
