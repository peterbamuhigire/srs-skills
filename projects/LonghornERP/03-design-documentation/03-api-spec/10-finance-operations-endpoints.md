# 10. Finance Operations Endpoints

## 10.1 Overview

These endpoints expose finance-operations capabilities above the accounting core. They support controlled bank-account governance, payment release, reconciliation, asset-accounting runs, group-finance orchestration, and reporting certification.

## 10.2 Bank Account Governance

### 10.2.1 Create Bank Account

- `POST /api/v1/finance/bank-accounts`
- Purpose: create a controlled bank-account record for an entity, currency, and payment purpose.

### 10.2.2 Submit Bank Account Change

- `POST /api/v1/finance/bank-accounts/{bankAccountId}/change-requests`
- Purpose: request a governed change to sensitive account attributes.

### 10.2.3 Approve Bank Account Change

- `POST /api/v1/finance/bank-account-change-requests/{requestId}/approve`
- Purpose: approve or reject a bank-account maintenance request.

### 10.2.4 Suspend Bank Account

- `POST /api/v1/finance/bank-accounts/{bankAccountId}/suspend`
- Purpose: suspend operational use of a bank account without deleting historical references.

## 10.3 Payment Release Workflow

### 10.3.1 Create Payment Batch

- `POST /api/v1/finance/payment-batches`
- Purpose: create a payment batch from approved payable obligations and release criteria.

### 10.3.2 Validate Payment Batch

- `POST /api/v1/finance/payment-batches/{batchId}/validate`
- Purpose: run pre-release validations for policy, amount, currency, and bank-account readiness.

### 10.3.3 Submit Batch for Approval

- `POST /api/v1/finance/payment-batches/{batchId}/submit`
- Purpose: move a payment batch into approval workflow.

### 10.3.4 Approve or Reject Payment Batch

- `POST /api/v1/finance/payment-batches/{batchId}/approval-actions`
- Purpose: record an approval, rejection, or return-for-correction action.

### 10.3.5 Release Payment Batch

- `POST /api/v1/finance/payment-batches/{batchId}/release`
- Purpose: authorise final release to connector adapters or controlled export.

### 10.3.6 Record Bank Execution Feedback

- `POST /api/v1/finance/payment-batches/{batchId}/bank-feedback`
- Purpose: capture bank acknowledgement, settlement, return, or rejection outcomes.

## 10.4 Bank Statements and Reconciliation

### 10.4.1 Register Statement Import

- `POST /api/v1/finance/bank-statement-imports`
- Purpose: register a bank statement import batch and its source metadata.

### 10.4.2 Upload Parsed Statement Lines

- `POST /api/v1/finance/bank-statement-imports/{importId}/lines`
- Purpose: persist parsed statement lines for matching and exception handling.

### 10.4.3 Generate Reconciliation Suggestions

- `POST /api/v1/finance/bank-accounts/{bankAccountId}/reconciliation-suggestions`
- Purpose: generate ERP-to-bank candidate matches over a statement window.

### 10.4.4 Confirm Reconciliation Match

- `POST /api/v1/finance/reconciliation-items/{itemId}/confirm`
- Purpose: confirm a suggested or manually selected reconciliation match.

### 10.4.5 Flag Reconciliation Exception

- `POST /api/v1/finance/reconciliation-items/{itemId}/exceptions`
- Purpose: record an unresolved or investigatory reconciliation exception.

### 10.4.6 Close Reconciliation Period

- `POST /api/v1/finance/bank-accounts/{bankAccountId}/reconciliation-periods/{periodId}/close`
- Purpose: close reconciliation for a bank account and period after exception review.

## 10.5 Asset Accounting Operations

### 10.5.1 Create Asset Book

- `POST /api/v1/finance/asset-books`
- Purpose: create a finance accounting book for asset valuation and posting policy.

### 10.5.2 Start Depreciation Run

- `POST /api/v1/finance/asset-books/{assetBookId}/depreciation-runs`
- Purpose: start a controlled depreciation run for a period.

### 10.5.3 Preview Depreciation Run

- `POST /api/v1/finance/depreciation-runs/{runId}/preview`
- Purpose: calculate expected posting outputs before posting.

### 10.5.4 Post Depreciation Run

- `POST /api/v1/finance/depreciation-runs/{runId}/post`
- Purpose: create posting-ready depreciation journals in the accounting core.

### 10.5.5 Record Asset Accounting Adjustment

- `POST /api/v1/finance/asset-books/{assetBookId}/adjustments`
- Purpose: record a governed finance adjustment against an asset book.

### 10.5.6 Certify Asset Close

- `POST /api/v1/finance/asset-books/{assetBookId}/periods/{periodId}/certify-close`
- Purpose: certify asset-accounting completion for period close dependency tracking.

## 10.6 Group Finance Operations

### 10.6.1 Maintain Ownership Hierarchy

- `POST /api/v1/finance/group-structures/{groupId}/ownership-versions`
- Purpose: create or replace an effective-dated ownership hierarchy version.

### 10.6.2 Start FX Translation Run

- `POST /api/v1/finance/group-structures/{groupId}/fx-translation-runs`
- Purpose: start a reporting-currency translation run for a reporting period.

### 10.6.3 Review FX Translation Exceptions

- `POST /api/v1/finance/fx-translation-runs/{runId}/review`
- Purpose: record review decisions or exception outcomes for translation issues.

### 10.6.4 Start Elimination Run

- `POST /api/v1/finance/group-structures/{groupId}/elimination-runs`
- Purpose: execute intercompany or group-level elimination logic for a reporting period.

### 10.6.5 Record Top-Side Adjustment

- `POST /api/v1/finance/group-structures/{groupId}/periods/{periodId}/topside-adjustments`
- Purpose: create a controlled top-side adjustment outside source-ledger journals.

### 10.6.6 Close Group Finance Cycle

- `POST /api/v1/finance/group-structures/{groupId}/periods/{periodId}/close-cycle`
- Purpose: complete the group-finance cycle after dependencies and approvals are satisfied.

## 10.7 Reporting Certification

### 10.7.1 Create Certification Package

- `POST /api/v1/finance/report-certifications`
- Purpose: create a certification workflow for a report package.

### 10.7.2 Assign Certifier

- `POST /api/v1/finance/report-certifications/{packageId}/assignments`
- Purpose: assign review or sign-off responsibility.

### 10.7.3 Submit Certification Package

- `POST /api/v1/finance/report-certifications/{packageId}/submit`
- Purpose: submit a report package for formal certification.

### 10.7.4 Act on Certification Step

- `POST /api/v1/finance/report-certifications/{packageId}/actions`
- Purpose: approve, reject, or request rework on a certification step.

### 10.7.5 Publish Certified Report Set

- `POST /api/v1/finance/report-certifications/{packageId}/publish`
- Purpose: mark a report set as certified and publication-ready.

## 10.8 Integration Endpoints

### 10.8.1 Export Payment Release Payload

- `POST /api/v1/finance/payment-batches/{batchId}/export`
- Purpose: generate a controlled payment payload for an external bank or treasury channel.

### 10.8.2 Import External Consolidation Status

- `POST /api/v1/finance/group-structures/{groupId}/external-consolidation-status`
- Purpose: capture status returned by a future external consolidation platform while leaving LonghornERP as ERP source of truth.

## 10.9 API Notes

- All mutating endpoints require authenticated users, role-based access control, and audit-event capture.
- Approval and release endpoints must enforce segregation-of-duties rules server-side.
- Bank import and export endpoints must support idempotency keys to avoid duplicate processing.
