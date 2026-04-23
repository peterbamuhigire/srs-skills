# Non-Functional Requirements

**NFR-CRM-005** - CRM account, contact, lead, and case data quality controls shall enforce duplicate prevention, mandatory-field validation, and referential integrity so that the monthly duplicate rate for accounts and contacts remains below the configured governance threshold and all blocked transactions are logged for review.

**NFR-CRM-006** - The mobile and field CRM experience shall allow a representative to review an account, log an activity, update an opportunity next step, and acknowledge or update a case from a mobile device in low-bandwidth conditions without requiring desktop-only workflows for routine field work.

**NFR-CRM-007** - CRM access control shall enforce role-based and record-based visibility for leads, opportunities, accounts, cases, partner-linked records, and personally identifiable contact data; sensitive fields and exported datasets shall be restricted to authorised roles and all access to protected CRM records shall be audit-logged.

**NFR-CRM-008** - Automated CRM routing and escalation actions, including lead assignment, case routing, stale-opportunity alerts, and SLA escalations, shall execute within 5 minutes of the triggering event under normal operating load.

**NFR-CRM-009** - SLA clocks, case escalations, reopen events, and quote-to-cash handoff histories shall be immutable and time-stamped so that auditors and managers can reconstruct who did what, when it happened, and which policy or SLA target applied at the time.

**NFR-CRM-010** - CRM pipeline, service, lifecycle, and partner dashboards shall use governed metric definitions and synchronised source data so that reported counts and values are reproducible and materially consistent with downstream Sales and ERP records for the same reporting period.
