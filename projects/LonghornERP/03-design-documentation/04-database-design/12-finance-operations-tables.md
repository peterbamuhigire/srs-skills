# 12. Finance Operations Tables

## 12.1 Overview

These tables extend the accounting data model for finance operations and group finance. They are additive and do not replace journal, AP, AR, or core asset master tables. The intent is to give LonghornERP controlled finance-operational state while preserving future integration paths to external treasury and consolidation tools.

## 12.2 Bank Account Governance

### 12.2.1 `bank_accounts`

Stores approved bank-account master data by entity, currency, and payment purpose.

Key columns:

- `id`
- `tenant_id`
- `entity_id`
- `bank_name`
- `bank_branch_name`
- `bank_country_code`
- `account_name`
- `account_number_masked`
- `account_number_ciphertext`
- `iban_ciphertext`
- `swift_bic`
- `currency_code`
- `payment_purpose_code`
- `account_status`
- `is_default_for_purpose`
- `connector_profile_code`
- `last_approved_change_request_id`
- `created_by`
- `created_at`
- `updated_at`

### 12.2.2 `bank_account_change_requests`

Stores governed bank-account maintenance requests before sensitive changes become effective.

Key columns:

- `id`
- `tenant_id`
- `bank_account_id`
- `request_type`
- `requested_change_payload_json`
- `request_status`
- `submitted_by`
- `submitted_at`
- `approved_by`
- `approved_at`
- `rejection_reason`

## 12.3 Bank Statements and Reconciliation

### 12.3.1 `bank_statement_imports`

Stores import-level metadata for statements received through connectors, files, or manual upload.

Key columns:

- `id`
- `tenant_id`
- `bank_account_id`
- `source_type`
- `source_reference`
- `statement_start_date`
- `statement_end_date`
- `import_status`
- `line_count`
- `checksum_hash`
- `imported_by`
- `imported_at`

### 12.3.2 `bank_statement_lines`

Stores immutable parsed bank transactions linked to an import batch.

Key columns:

- `id`
- `tenant_id`
- `import_id`
- `bank_account_id`
- `statement_line_date`
- `value_date`
- `external_reference`
- `narrative`
- `amount`
- `currency_code`
- `debit_credit_indicator`
- `bank_running_balance`
- `raw_payload_json`

### 12.3.3 `bank_reconciliation_items`

Stores ERP-to-bank matching candidates, confirmations, and exceptions.

Key columns:

- `id`
- `tenant_id`
- `bank_account_id`
- `period_id`
- `statement_line_id`
- `erp_reference_type`
- `erp_reference_id`
- `match_status`
- `match_score`
- `match_method`
- `exception_code`
- `exception_notes`
- `confirmed_by`
- `confirmed_at`

## 12.4 Payment Batches and Release Control

### 12.4.1 `payment_batches`

Stores controlled payment batches before transmission or export.

Key columns:

- `id`
- `tenant_id`
- `entity_id`
- `bank_account_id`
- `payment_method_code`
- `payment_currency_code`
- `batch_status`
- `batch_total_amount`
- `batch_total_count`
- `release_channel_code`
- `prepared_by`
- `prepared_at`
- `released_by`
- `released_at`

### 12.4.2 `payment_batch_lines`

Stores payable obligations included in each payment batch.

Key columns:

- `id`
- `tenant_id`
- `payment_batch_id`
- `source_document_type`
- `source_document_id`
- `payee_type`
- `payee_id`
- `amount`
- `currency_code`
- `line_status`
- `failure_reason`

### 12.4.3 `payment_batch_approvals`

Stores approval workflow steps for payment batches.

Key columns:

- `id`
- `tenant_id`
- `payment_batch_id`
- `approval_step_no`
- `approval_role_code`
- `approver_user_id`
- `approval_status`
- `approval_limit_amount`
- `acted_at`
- `action_notes`

### 12.4.4 `payment_releases`

Stores release payload metadata, execution references, and feedback from banks or treasury channels.

Key columns:

- `id`
- `tenant_id`
- `payment_batch_id`
- `release_reference`
- `payload_hash`
- `transmission_status`
- `bank_ack_reference`
- `bank_execution_status`
- `feedback_payload_json`
- `released_by`
- `released_at`

## 12.5 Asset Accounting Operations

### 12.5.1 `asset_books`

Stores finance accounting books for fixed assets by entity and valuation basis.

Key columns:

- `id`
- `tenant_id`
- `entity_id`
- `book_code`
- `book_name`
- `valuation_basis_code`
- `currency_code`
- `depreciation_policy_json`
- `book_status`
- `created_at`

### 12.5.2 `asset_depreciation_runs`

Stores controlled depreciation or amortisation run headers.

Key columns:

- `id`
- `tenant_id`
- `asset_book_id`
- `period_id`
- `run_type`
- `run_status`
- `started_by`
- `started_at`
- `posted_by`
- `posted_at`
- `generated_journal_batch_id`

### 12.5.3 `asset_depreciation_run_lines`

Stores per-asset results for a depreciation run.

Key columns:

- `id`
- `tenant_id`
- `run_id`
- `asset_id`
- `expense_amount`
- `accumulated_depreciation_amount`
- `salvage_value_amount`
- `posting_status`
- `exception_code`

## 12.6 Group Finance Structures and Runs

### 12.6.1 `group_structures`

Stores reporting-group or consolidation-scope master records.

Key columns:

- `id`
- `tenant_id`
- `group_code`
- `group_name`
- `reporting_currency_code`
- `group_status`
- `created_at`

### 12.6.2 `ownership_hierarchy_versions`

Stores effective-dated versions of group ownership structures.

Key columns:

- `id`
- `tenant_id`
- `group_structure_id`
- `version_no`
- `effective_from`
- `effective_to`
- `status`
- `approved_by`
- `approved_at`

### 12.6.3 `ownership_hierarchy_nodes`

Stores parent-child ownership relationships inside a version.

Key columns:

- `id`
- `tenant_id`
- `hierarchy_version_id`
- `parent_entity_id`
- `child_entity_id`
- `ownership_percent`
- `control_type_code`
- `consolidation_method_code`

### 12.6.4 `fx_translation_runs`

Stores reporting-currency translation runs by group and period.

Key columns:

- `id`
- `tenant_id`
- `group_structure_id`
- `period_id`
- `rate_set_id`
- `run_status`
- `started_by`
- `started_at`
- `completed_at`
- `exception_count`

### 12.6.5 `fx_translation_run_lines`

Stores per-entity translation outputs and exceptions.

Key columns:

- `id`
- `tenant_id`
- `run_id`
- `entity_id`
- `source_currency_code`
- `target_currency_code`
- `translation_amount`
- `cta_amount`
- `line_status`
- `exception_code`

### 12.6.6 `elimination_runs`

Stores elimination-processing headers for a group close cycle.

Key columns:

- `id`
- `tenant_id`
- `group_structure_id`
- `period_id`
- `run_scope_code`
- `run_status`
- `started_by`
- `started_at`
- `completed_at`

### 12.6.7 `elimination_run_lines`

Stores elimination entries or exception records generated during a run.

Key columns:

- `id`
- `tenant_id`
- `run_id`
- `counterparty_entity_id`
- `account_id`
- `amount`
- `currency_code`
- `line_status`
- `exception_code`
- `generated_adjustment_id`

### 12.6.8 `topside_adjustments`

Stores controlled group-level adjustments outside source-ledger journals.

Key columns:

- `id`
- `tenant_id`
- `group_structure_id`
- `period_id`
- `adjustment_type_code`
- `adjustment_status`
- `description`
- `prepared_by`
- `prepared_at`
- `approved_by`
- `approved_at`

### 12.6.9 `topside_adjustment_lines`

Stores detailed debit-credit lines for each top-side adjustment.

Key columns:

- `id`
- `tenant_id`
- `topside_adjustment_id`
- `account_id`
- `entity_id`
- `debit_amount`
- `credit_amount`
- `currency_code`
- `line_description`

## 12.7 Reporting Certification

### 12.7.1 `reporting_certifications`

Stores certification-package headers for management, statutory, or lender report sets.

Key columns:

- `id`
- `tenant_id`
- `scope_type`
- `scope_id`
- `period_id`
- `report_set_code`
- `snapshot_reference`
- `certification_status`
- `submitted_by`
- `submitted_at`
- `published_at`

### 12.7.2 `reporting_certification_steps`

Stores workflow assignments and approval actions for each certification package.

Key columns:

- `id`
- `tenant_id`
- `reporting_certification_id`
- `step_no`
- `role_code`
- `assigned_user_id`
- `step_status`
- `acted_at`
- `action_notes`

## 12.8 Relationship Notes

- `bank_accounts.entity_id` references the legal entity master in ERP core.
- `payment_batches.bank_account_id` references `bank_accounts.id`.
- `bank_statement_imports.bank_account_id` and `bank_reconciliation_items.bank_account_id` anchor reconciliation by account.
- `asset_books.entity_id` links asset-accounting books to entities, while run tables link back to accounting periods and generated journal batches.
- `ownership_hierarchy_versions.group_structure_id` and `ownership_hierarchy_nodes.hierarchy_version_id` separate master group identity from effective-dated structures.
- `fx_translation_runs`, `elimination_runs`, and `topside_adjustments` align to reporting periods and group structures.
- `reporting_certifications` can certify either entity or group reporting scopes.

## 12.9 Design Intent

This schema gives LonghornERP durable internal structures for controlled finance operations while keeping bank adapters, treasury channels, and specialist consolidation tools outside the core ledger model. That preserves ERP ownership of finance truth and leaves future enterprise integration optional rather than mandatory.
