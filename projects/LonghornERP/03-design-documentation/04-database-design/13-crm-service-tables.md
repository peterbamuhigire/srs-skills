# CRM Service Tables

## Overview

These tables extend LonghornERP with a first-class CRM data model for revenue CRM and service CRM.

Design principles:

- relationship workflow is stored in CRM tables
- ERP execution and finance truth stay in ERP-owned tables
- customer financial context in CRM is snapshot or reference data sourced from ERP
- approvals, SLA events, and quote handoffs are explicitly modeled for auditability

All tables include `id`, `tenant_id`, `created_at`, `updated_at`, and the standard audit columns unless stated otherwise.

---

## Revenue CRM Core Tables

### `crm_accounts`

| Column | Type | Notes |
|---|---|---|
| `account_code` | `varchar(40)` | Tenant-scoped human-readable account identifier. |
| `account_name` | `varchar(255)` | Display name of the account. |
| `legal_name` | `varchar(255)` | Optional legal-entity name used for duplicate control. |
| `account_status` | `varchar(30)` | `prospect`, `active`, `inactive`, `former`. |
| `segment_code` | `varchar(40)` | Current assigned segment. |
| `tier_code` | `varchar(40)` | Current commercial or service tier. |
| `territory_id` | `bigint` | Owning territory or region. |
| `owner_user_id` | `bigint` | Primary relationship owner. |
| `parent_account_id` | `bigint` | Nullable parent account reference. |
| `channel_partner_id` | `bigint` | Nullable current channel partner relationship. |
| `external_ref` | `varchar(100)` | Optional external or legacy source identifier. |
| `tax_identifier` | `varchar(100)` | Duplicate control and legal matching field. |

### `crm_account_hierarchies`

| Column | Type | Notes |
|---|---|---|
| `parent_account_id` | `bigint` | Parent account. |
| `child_account_id` | `bigint` | Child account. |
| `relationship_type` | `varchar(40)` | `group_parent`, `branch`, `affiliate`, `billing_only`. |
| `effective_from` | `date` | Relationship start date. |
| `effective_to` | `date` | Nullable relationship end date. |

### `crm_contacts`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Owning account. |
| `full_name` | `varchar(255)` | Contact name. |
| `email` | `varchar(255)` | Contact email. |
| `phone` | `varchar(80)` | Contact phone. |
| `role_title` | `varchar(120)` | Job or functional title. |
| `decision_role` | `varchar(60)` | `economic_buyer`, `technical_buyer`, `champion`, `service_contact`. |
| `is_primary` | `boolean` | Primary contact for the account. |
| `is_active` | `boolean` | Soft-active flag. |

### `crm_leads`

| Column | Type | Notes |
|---|---|---|
| `company_name` | `varchar(255)` | Prospect organization name. |
| `contact_name` | `varchar(255)` | Prospect contact name. |
| `email` | `varchar(255)` | Prospect email. |
| `phone` | `varchar(80)` | Prospect phone. |
| `source` | `varchar(80)` | Campaign or acquisition source. |
| `status` | `varchar(30)` | `new`, `qualified`, `nurture`, `converted`, `disqualified`. |
| `estimated_value` | `decimal(18,2)` | Estimated revenue potential. |
| `assigned_to` | `bigint` | Assigned user. |
| `qualification_score` | `decimal(5,2)` | Qualification or fit score. |

### `crm_opportunities`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Linked account. |
| `primary_contact_id` | `bigint` | Linked primary contact. |
| `lead_id` | `bigint` | Nullable originating lead. |
| `opportunity_name` | `varchar(255)` | Opportunity title. |
| `pipeline_code` | `varchar(40)` | Pipeline classification. |
| `stage_code` | `varchar(40)` | Current sales stage. |
| `status` | `varchar(30)` | `open`, `won`, `lost`, `pending_execution`, `on_hold`. |
| `estimated_value` | `decimal(18,2)` | Expected deal value. |
| `probability_pct` | `decimal(5,2)` | Stage-based or overridden probability. |
| `expected_close_date` | `date` | Expected close date. |
| `forecast_category` | `varchar(30)` | `pipeline`, `best_case`, `commit`, `closed`. |
| `owner_user_id` | `bigint` | Responsible seller. |
| `competitor_summary` | `text` | Optional competitive context. |

### `crm_opportunity_stage_history`

| Column | Type | Notes |
|---|---|---|
| `opportunity_id` | `bigint` | Parent opportunity. |
| `from_stage_code` | `varchar(40)` | Prior stage. |
| `to_stage_code` | `varchar(40)` | New stage. |
| `changed_by_user_id` | `bigint` | User making the stage change. |
| `change_reason` | `text` | Evidence or rationale. |
| `changed_at` | `datetime` | Stage change timestamp. |

### `crm_pipeline_stage_policies`

| Column | Type | Notes |
|---|---|---|
| `pipeline_code` | `varchar(40)` | Pipeline identifier. |
| `stage_code` | `varchar(40)` | Governed stage code. |
| `required_fields_json` | `json` | Required data before stage progression. |
| `approval_rules_json` | `json` | Commercial exception rules. |
| `probability_pct` | `decimal(5,2)` | Standard stage probability. |
| `is_active` | `boolean` | Active policy flag. |

### `crm_opportunity_reviews`

| Column | Type | Notes |
|---|---|---|
| `opportunity_id` | `bigint` | Parent opportunity. |
| `review_type` | `varchar(40)` | `pipeline_review`, `deal_desk`, `forecast_commit`. |
| `review_status` | `varchar(30)` | `open`, `completed`, `cancelled`. |
| `owner_user_id` | `bigint` | Review owner. |
| `due_at` | `datetime` | Review due time. |
| `notes` | `text` | Review notes. |

### `crm_opportunity_approvals`

| Column | Type | Notes |
|---|---|---|
| `opportunity_id` | `bigint` | Parent opportunity. |
| `approval_type` | `varchar(40)` | `discount`, `non_standard_terms`, `strategic_bid`, `partner_exception`. |
| `approval_status` | `varchar(30)` | `pending`, `approved`, `rejected`, `expired`. |
| `requested_by_user_id` | `bigint` | Requesting user. |
| `approved_by_user_id` | `bigint` | Nullable deciding user. |
| `requested_at` | `datetime` | Request timestamp. |
| `decided_at` | `datetime` | Nullable decision timestamp. |
| `justification` | `text` | Request justification. |
| `decision_comment` | `text` | Nullable decision notes. |

### `crm_activities`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Linked account. |
| `opportunity_id` | `bigint` | Nullable linked opportunity. |
| `case_id` | `bigint` | Nullable linked case. |
| `activity_type` | `varchar(40)` | `call`, `email`, `meeting`, `demo`, `task`. |
| `subject` | `varchar(255)` | Short activity description. |
| `notes` | `text` | Activity notes. |
| `due_at` | `datetime` | Nullable next action or task due time. |
| `completed_at` | `datetime` | Nullable completion timestamp. |
| `owner_user_id` | `bigint` | Assigned or logging user. |

### `crm_quote_handoffs`

| Column | Type | Notes |
|---|---|---|
| `opportunity_id` | `bigint` | Parent opportunity. |
| `handoff_status` | `varchar(30)` | `prepared`, `submitted`, `accepted`, `rejected`, `converted`. |
| `quote_number` | `varchar(80)` | CRM quote reference. |
| `pricing_basis` | `varchar(80)` | Commercial basis for ERP validation. |
| `currency_code` | `varchar(10)` | Transaction currency. |
| `valid_until` | `date` | Quote validity. |
| `handoff_payload_hash` | `varchar(128)` | Immutable payload fingerprint. |
| `erp_quote_id` | `bigint` | Nullable ERP quote reference. |
| `erp_order_id` | `bigint` | Nullable ERP order reference. |
| `erp_feedback_status` | `varchar(30)` | Latest ERP response. |
| `erp_feedback_message` | `text` | Nullable ERP validation or rejection details. |

### `crm_quote_handoff_lines`

| Column | Type | Notes |
|---|---|---|
| `handoff_id` | `bigint` | Parent handoff. |
| `line_no` | `int` | Sequential line number. |
| `item_ref` | `varchar(100)` | SKU or service reference. |
| `quantity` | `decimal(18,4)` | Requested quantity. |
| `unit_price` | `decimal(18,4)` | Intended unit price. |
| `discount_pct` | `decimal(5,2)` | Discount at handoff time. |
| `line_payload_json` | `json` | Extended line detail for ERP mapping. |

---

## Service CRM Tables

### `crm_sla_policies`

| Column | Type | Notes |
|---|---|---|
| `policy_name` | `varchar(120)` | SLA policy name. |
| `case_type` | `varchar(40)` | Case category the policy applies to. |
| `priority_code` | `varchar(40)` | Priority band. |
| `response_target_minutes` | `int` | First-response target. |
| `resolution_target_minutes` | `int` | Resolution target. |
| `escalation_rule_json` | `json` | Escalation timing and role policy. |
| `is_active` | `boolean` | Active policy flag. |

### `crm_cases`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Customer account. |
| `contact_id` | `bigint` | Nullable contact. |
| `case_number` | `varchar(50)` | Human-readable case reference. |
| `case_type` | `varchar(40)` | `incident`, `request`, `complaint`, `billing_query`, `service_order`. |
| `priority_code` | `varchar(40)` | `low`, `medium`, `high`, `critical`. |
| `status` | `varchar(30)` | `open`, `in_progress`, `pending_customer`, `escalated`, `resolved`, `closed`. |
| `subject` | `varchar(255)` | Case subject. |
| `description` | `text` | Case description. |
| `channel_code` | `varchar(40)` | `email`, `phone`, `portal`, `walk_in`, `partner`. |
| `owner_user_id` | `bigint` | Case owner. |
| `queue_id` | `bigint` | Nullable assignment queue. |
| `sla_policy_id` | `bigint` | Applied SLA policy. |
| `response_due_at` | `datetime` | Response deadline. |
| `resolution_due_at` | `datetime` | Resolution deadline. |
| `resolved_at` | `datetime` | Nullable resolution time. |

### `crm_case_comments`

| Column | Type | Notes |
|---|---|---|
| `case_id` | `bigint` | Parent case. |
| `comment_body` | `text` | Comment content. |
| `is_customer_visible` | `boolean` | Visibility flag. |
| `commented_by_user_id` | `bigint` | Author. |
| `commented_at` | `datetime` | Comment timestamp. |

### `crm_case_timeline_events`

| Column | Type | Notes |
|---|---|---|
| `case_id` | `bigint` | Parent case. |
| `event_type` | `varchar(40)` | `opened`, `assigned`, `commented`, `status_changed`, `escalated`, `resolved`. |
| `event_summary` | `varchar(255)` | Short event summary. |
| `event_detail` | `text` | Extended event detail. |
| `event_at` | `datetime` | Event timestamp. |
| `actor_user_id` | `bigint` | Nullable actor. |

### `crm_case_escalations`

| Column | Type | Notes |
|---|---|---|
| `case_id` | `bigint` | Parent case. |
| `escalation_level` | `int` | Escalation level number. |
| `escalation_reason` | `text` | Reason for escalation. |
| `from_user_id` | `bigint` | Nullable previous owner. |
| `to_user_id` | `bigint` | Escalated owner. |
| `escalated_at` | `datetime` | Escalation timestamp. |
| `resolved_at` | `datetime` | Nullable escalation clearance time. |

---

## Customer Intelligence Tables

### `crm_segmentation_models`

| Column | Type | Notes |
|---|---|---|
| `model_name` | `varchar(120)` | Segmentation model name. |
| `effective_from` | `date` | Effective start date. |
| `criteria_json` | `json` | Segmentation logic. |
| `owner_user_id` | `bigint` | Model owner. |
| `is_active` | `boolean` | Active version flag. |

### `crm_account_segment_history`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `segment_code` | `varchar(40)` | Segment code. |
| `tier_code` | `varchar(40)` | Tier code. |
| `effective_from` | `date` | Start date. |
| `effective_to` | `date` | Nullable end date. |
| `reason` | `text` | Reason for change. |

### `crm_account_plans`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `plan_year` | `int` | Planning year. |
| `growth_goal` | `decimal(18,2)` | Revenue or expansion goal. |
| `renewal_risk` | `varchar(30)` | Risk summary. |
| `white_space_summary` | `text` | Expansion whitespace. |
| `owner_user_id` | `bigint` | Plan owner. |
| `plan_status` | `varchar(30)` | `draft`, `active`, `closed`. |

### `crm_account_plan_initiatives`

| Column | Type | Notes |
|---|---|---|
| `plan_id` | `bigint` | Parent account plan. |
| `initiative_name` | `varchar(255)` | Initiative title. |
| `target_value` | `decimal(18,2)` | Initiative target value. |
| `due_date` | `date` | Planned completion date. |
| `status` | `varchar(30)` | Initiative status. |

### `crm_customer_health_signals`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `signal_type` | `varchar(60)` | `usage`, `service`, `payment`, `adoption`, `executive_change`, `renewal_risk`. |
| `signal_score` | `decimal(6,2)` | Signed contribution or scaled score. |
| `observed_at` | `datetime` | Observation time. |
| `source_system` | `varchar(80)` | Producing system. |
| `notes` | `text` | Supporting narrative. |

### `crm_account_health_scores`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `score_period` | `varchar(20)` | Scoring period marker. |
| `health_score` | `decimal(6,2)` | Composite health score. |
| `health_status` | `varchar(30)` | `green`, `amber`, `red`. |
| `calculated_at` | `datetime` | Score calculation time. |
| `summary_json` | `json` | Contributing factors. |

### `crm_renewals`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `contract_ref` | `varchar(100)` | Contract or subscription reference. |
| `renewal_date` | `date` | Renewal date. |
| `renewal_value` | `decimal(18,2)` | Renewal value. |
| `renewal_owner_user_id` | `bigint` | Renewal owner. |
| `renewal_status` | `varchar(30)` | `watch`, `at_risk`, `in_progress`, `closed_won`, `closed_lost`. |

### `crm_account_financial_snapshots`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Account reference. |
| `snapshot_at` | `datetime` | ERP snapshot time. |
| `credit_status` | `varchar(40)` | Credit-control status. |
| `receivables_balance` | `decimal(18,2)` | Total receivable exposure. |
| `overdue_balance` | `decimal(18,2)` | Overdue exposure. |
| `open_orders_count` | `int` | Count of open orders. |
| `last_payment_date` | `date` | Nullable most recent payment date. |
| `snapshot_json` | `json` | Additional ERP-derived context. |

---

## Channel and Partner Tables

### `crm_channel_partners`

| Column | Type | Notes |
|---|---|---|
| `partner_name` | `varchar(255)` | Partner name. |
| `partner_type` | `varchar(40)` | `reseller`, `distributor`, `implementer`, `referral`. |
| `coverage_region` | `varchar(120)` | Region or territory. |
| `tier_code` | `varchar(40)` | Partner tier. |
| `owner_user_id` | `bigint` | Internal partner manager. |
| `partner_status` | `varchar(30)` | `active`, `inactive`, `suspended`. |

### `crm_account_partner_links`

| Column | Type | Notes |
|---|---|---|
| `account_id` | `bigint` | Customer account. |
| `partner_id` | `bigint` | Channel partner. |
| `relationship_type` | `varchar(40)` | `reseller`, `delivery_partner`, `referral_partner`, `influencer`. |
| `effective_from` | `date` | Relationship start date. |
| `effective_to` | `date` | Nullable end date. |

### `crm_partner_deals`

| Column | Type | Notes |
|---|---|---|
| `partner_id` | `bigint` | Partner reference. |
| `opportunity_id` | `bigint` | Opportunity reference. |
| `registration_date` | `date` | Deal registration date. |
| `protection_expiry` | `date` | Protected period end date. |
| `channel_discount_pct` | `decimal(5,2)` | Partner commercial discount. |
| `deal_status` | `varchar(30)` | `registered`, `approved`, `rejected`, `expired`, `won`, `lost`. |

---

## Integrity Rules

1. `crm_accounts` must support duplicate detection on `legal_name`, `tax_identifier`, and `external_ref`.
2. `crm_account_hierarchies` must prevent cyclic parent-child relationships.
3. `crm_opportunity_approvals` must preserve immutable decision timestamps and users.
4. `crm_quote_handoffs.handoff_payload_hash` must support idempotent CRM-to-ERP handoff control.
5. `crm_cases` and `crm_case_timeline_events` together must provide full service audit reconstruction.
6. `crm_account_financial_snapshots` must be treated as read-only derivative context, not editable financial truth.
