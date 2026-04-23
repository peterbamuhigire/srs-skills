# CRM Service Endpoints

## Overview

These endpoints define the CRM API layer for revenue CRM and service CRM. They support customer workflow, pipeline governance, service resolution workflow, quote-to-cash coordination, and customer-intelligence use cases.

CRM endpoints expose workflow state and relationship context. They do not replace ERP execution endpoints for orders, invoicing, receivables, or accounting postings.

---

## Account and Contact Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/accounts` | Create an account with ownership, segment, and hierarchy metadata. |
| `GET` | `/api/crm/accounts/{accountId}` | Return account profile, hierarchy, contacts, health score, and financial context snapshot. |
| `PATCH` | `/api/crm/accounts/{accountId}` | Update account relationship attributes such as owner, segment, territory, or partner linkage. |
| `POST` | `/api/crm/accounts/{accountId}/contacts` | Add a contact to an account. |
| `PATCH` | `/api/crm/contacts/{contactId}` | Update contact role, communication details, or primary-contact status. |
| `GET` | `/api/crm/accounts/{accountId}/financial-context` | Return read-only customer financial context sourced from ERP. |

---

## Lead and Opportunity Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/leads` | Create a lead. |
| `PATCH` | `/api/crm/leads/{leadId}/qualification` | Record qualification outcomes and next action. |
| `POST` | `/api/crm/leads/{leadId}/convert` | Convert a qualified lead into account, contact, and opportunity context. |
| `POST` | `/api/crm/opportunities` | Create an opportunity directly under an account. |
| `GET` | `/api/crm/opportunities/{opportunityId}` | Return opportunity detail, stage history, approvals, and activities. |
| `PATCH` | `/api/crm/opportunities/{opportunityId}/stage` | Advance or regress the opportunity stage subject to policy validation. |
| `POST` | `/api/crm/opportunities/{opportunityId}/reviews` | Create a formal pipeline or deal-desk review. |
| `POST` | `/api/crm/opportunities/{opportunityId}/approvals` | Submit a commercial exception approval request. |
| `POST` | `/api/crm/opportunity-approvals/{approvalId}/decision` | Approve or reject an opportunity approval request. |
| `GET` | `/api/crm/forecasts/commit` | Return commit, best-case, and pipeline forecast summaries for a month. |

---

## Activity and Account Planning Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/activities` | Log a sales or service activity tied to an account and optional opportunity or case. |
| `GET` | `/api/crm/accounts/{accountId}/activities` | Return chronological activity history for the account. |
| `POST` | `/api/crm/segmentation-models` | Create or version a segmentation model. |
| `POST` | `/api/crm/accounts/{accountId}/segment` | Classify an account into a segment and tier. |
| `POST` | `/api/crm/accounts/{accountId}/plans` | Create an account plan. |
| `POST` | `/api/crm/account-plans/{planId}/initiatives` | Add an initiative to an account plan. |
| `GET` | `/api/crm/account-priorities` | Return prioritized accounts using segment, health, whitespace, and renewal context. |

---

## Quote-to-Cash Handoff Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/opportunities/{opportunityId}/quote-handoffs/prepare` | Build the canonical quote-to-cash handoff payload. |
| `POST` | `/api/crm/opportunities/{opportunityId}/quote-handoffs` | Submit a governed quote handoff into ERP execution. |
| `GET` | `/api/crm/quote-handoffs/{handoffId}` | Return handoff state, ERP references, and error context. |
| `POST` | `/api/crm/quote-handoffs/{handoffId}/erp-feedback` | Record ERP acceptance, rejection, quote creation, or order conversion feedback. |

---

## Case Management and SLA Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/cases` | Open a service case with SLA policy selection. |
| `GET` | `/api/crm/cases/{caseId}` | Return case detail, SLA state, comments, and timeline. |
| `PATCH` | `/api/crm/cases/{caseId}/assignment` | Change case owner or queue assignment. |
| `POST` | `/api/crm/cases/{caseId}/comments` | Add a case comment. |
| `POST` | `/api/crm/cases/{caseId}/escalations` | Escalate a case under governed escalation workflow. |
| `POST` | `/api/crm/cases/{caseId}/resolve` | Resolve a case and stop SLA clocks. |
| `GET` | `/api/crm/cases/sla-watchlist` | Return open cases near or beyond SLA thresholds. |
| `POST` | `/api/crm/sla-policies` | Create or version an SLA policy. |

---

## Customer Health and Renewal Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/accounts/{accountId}/health-signals` | Capture a customer health signal. |
| `POST` | `/api/crm/accounts/{accountId}/health-score/recalculate` | Recalculate the composite health score for an account. |
| `GET` | `/api/crm/accounts/{accountId}/health-score` | Return the current health score and contributing signals. |
| `POST` | `/api/crm/accounts/{accountId}/renewals` | Register a renewal or contract milestone. |
| `GET` | `/api/crm/renewals/watchlist` | Return the renewal watchlist with risk and service context. |

---

## Channel and Partner Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/crm/channel-partners` | Register a channel or partner organization. |
| `POST` | `/api/crm/accounts/{accountId}/partner-links` | Link an account to a partner relationship. |
| `POST` | `/api/crm/channel-partners/{partnerId}/deals` | Register a partner deal against an opportunity. |
| `GET` | `/api/crm/channel-partners/{partnerId}/pipeline` | Return the partner-associated pipeline. |

---

## API Guardrails

1. CRM API responses that include financial context must identify the ERP source timestamp.
2. Quote-to-cash handoff endpoints must be idempotent and reject duplicate release of the same approved payload.
3. Opportunity approval endpoints must preserve immutable decision history.
4. Case timeline endpoints must preserve the order of operational events, comments, assignments, and escalations.
5. Customer and partner identity endpoints must enforce duplicate controls and hierarchy integrity.
