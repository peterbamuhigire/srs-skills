# 11. Finance Operations Services

## 11.1 Overview

This section defines low-level finance operations services that extend the accounting core for payment control, bank reconciliation, asset-accounting runs, and group-finance orchestration. These services are additive. They consume accounting and operational master data from existing modules and publish governed finance outcomes back into accounting, reporting, and integration layers.

## 11.2 `BankAccountGovernanceService`

### 11.2.1 Responsibilities

- manage bank account master records by entity, currency, and usage
- maintain account status, signatory policy, and release thresholds
- store connector routing metadata without embedding bank-specific protocol logic in the ledger domain
- enforce approval workflow for creation, change, suspension, and closure of bank accounts

### 11.2.2 Core Operations

- `createBankAccount(entityId, payload)`
- `submitBankAccountChange(accountId, changeSet)`
- `approveBankAccountChange(requestId, approverId)`
- `suspendBankAccount(accountId, reason)`
- `listEligibleAccounts(entityId, purpose, currency)`

### 11.2.3 Rules

- active payment release requires an approved bank account in usable status
- account-number and routing-field changes require controlled approval, not direct overwrite
- default disbursement accounts are unique by entity, payment rail, and currency combination

## 11.3 `PaymentReleaseWorkflowService`

### 11.3.1 Responsibilities

- assemble payment batches from approved obligations
- validate batch composition, due dates, currencies, and bank-account policy
- orchestrate maker-checker approval steps
- generate release payloads for connector adapters or controlled exports
- capture release evidence, transmission status, and rejection outcomes

### 11.3.2 Core Operations

- `createPaymentBatch(entityId, sourceFilters)`
- `validatePaymentBatch(batchId)`
- `submitBatchForApproval(batchId, submitterId)`
- `recordApprovalAction(batchId, approverId, action, comment)`
- `releasePaymentBatch(batchId, releaserId)`
- `recordBankExecutionFeedback(batchId, statusPayload)`

### 11.3.3 Rules

- a user cannot both prepare and finally approve the same payment batch
- release requires all threshold approvals to be complete
- partially failed batches create actionable exception items without rewriting approved source obligations
- release payloads are immutable once transmitted; corrections occur through controlled reversal or replacement flows

## 11.4 `BankReconciliationService`

### 11.4.1 Responsibilities

- register statement import batches and parsed statement lines
- generate candidate matches between bank activity and ERP cash transactions
- maintain reconciliation items, exceptions, and manual-review decisions
- produce reconciliation completion status by bank account and period

### 11.4.2 Core Operations

- `registerStatementImport(accountId, importMetadata)`
- `ingestStatementLines(importId, lines)`
- `generateMatchSuggestions(accountId, statementWindow)`
- `confirmMatch(reconciliationItemId, actorId)`
- `flagException(reconciliationItemId, reasonCode)`
- `closeReconciliationPeriod(accountId, periodId)`

### 11.4.3 Rules

- raw imported statement lines remain immutable after load
- manual match overrides require reason capture
- reconciliation period closure is blocked while material exceptions remain unresolved according to policy

## 11.5 `AssetAccountingRunService`

### 11.5.1 Responsibilities

- maintain accounting books for fixed assets by entity and basis
- orchestrate depreciation, amortisation, revaluation, and disposal accounting runs
- validate tie-out between asset subledger balances and accounting postings
- publish posting-ready accounting entries to the accounting core

### 11.5.2 Core Operations

- `createAssetBook(entityId, valuationBasis, ruleset)`
- `startDepreciationRun(bookId, periodId)`
- `previewDepreciationRun(runId)`
- `postDepreciationRun(runId, actorId)`
- `recordAssetAccountingAdjustment(bookId, adjustmentPayload)`
- `certifyAssetClose(bookId, periodId, actorId)`

### 11.5.3 Rules

- one open depreciation run per asset book and period
- reruns after posting require controlled reversal or delta-adjustment treatment
- asset close certification requires all run exceptions to be resolved or explicitly waived

## 11.6 `GroupFinanceOrchestrationService`

### 11.6.1 Responsibilities

- manage ownership hierarchies and reporting groups
- orchestrate FX translation runs from local books into reporting currency
- execute elimination runs across intercompany and group relationships
- record top-side adjustments with approval traceability
- assemble consolidation status for group reporting cycles

### 11.6.2 Core Operations

- `maintainOwnershipHierarchy(groupId, structurePayload)`
- `startFxTranslationRun(groupId, periodId, rateSetId)`
- `reviewFxTranslationExceptions(runId)`
- `startEliminationRun(groupId, periodId)`
- `recordTopsideAdjustment(groupId, periodId, adjustmentPayload)`
- `closeGroupFinanceCycle(groupId, periodId)`

### 11.6.3 Rules

- ownership changes are versioned by effective date
- elimination and top-side adjustments are separated from source-ledger journals for audit clarity
- group close cannot complete until entity close dependencies, translation, eliminations, and certification gates are satisfied

## 11.7 `ReportingCertificationService`

### 11.7.1 Responsibilities

- create certification packages for management, statutory, and lender-facing reports
- capture reviewer sign-off, commentary, and evidence links
- store final certification status by entity, group, period, and report set
- expose publication readiness to reporting and portal layers

### 11.7.2 Core Operations

- `createCertificationPackage(scopeType, scopeId, periodId, reportSet)`
- `assignCertifier(packageId, userId, roleCode)`
- `submitCertification(packageId, actorId)`
- `approveCertificationStep(packageId, actorId, action, notes)`
- `publishCertifiedReportSet(packageId)`

### 11.7.3 Rules

- reports cannot be marked certified while upstream close gates remain open
- certification packages preserve the report snapshot reference used for approval
- certification withdrawal creates a new version rather than mutating prior evidence

## 11.8 Cross-Service Orchestration

### 11.8.1 Payment-to-Reconciliation Chain

1. `PaymentReleaseWorkflowService` creates and releases approved disbursement batches.
2. Bank adapter responses update execution outcomes.
3. `BankReconciliationService` consumes statement imports and suggests or confirms cash matches.
4. Accounting receives the final cash-clearing status for close and audit reporting.

### 11.8.2 Asset-to-Close Chain

1. `AssetAccountingRunService` executes period depreciation and adjustment logic.
2. Posting-ready entries are submitted to accounting.
3. Period close gates use asset close certification status as an upstream dependency.

### 11.8.3 Entity-to-Group Close Chain

1. Entity-level books are closed in accounting.
2. `GroupFinanceOrchestrationService` runs FX translation, eliminations, and top-side adjustments.
3. `ReportingCertificationService` controls final pack sign-off and publication readiness.

## 11.9 Integration Notes

- Connector-specific banking logic must remain in adapter classes outside these services.
- External treasury or consolidation suites may call these services or consume their outputs, but core finance state remains stored in LonghornERP.
- All service actions that affect approvals, release, or certification require durable audit-event emission.
