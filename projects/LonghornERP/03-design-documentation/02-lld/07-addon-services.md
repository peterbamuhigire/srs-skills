# Add-On Module Services — Low-Level Design

## Overview

Add-on modules extend Longhorn ERP beyond the core suite. Each is activated per tenant via `ModuleRegistry`. All add-on services follow the same constructor injection pattern as core services: `PDO`, `SessionService`, and `AuditService` are always injected; additional dependencies are listed per service.

---

## ManufacturingService

**Namespace:** `App\Modules\Manufacturing`

**Module guard:** `ModuleRegistry::isActive('MANUFACTURING', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `StockLedgerService`, `AccountingService`, `BOMService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createProductionOrder(int $finishedItemId, float $plannedQty, int $periodId): int` | Finished goods item primary key, planned production quantity, accounting period primary key | New `production_orders.id` | Validates that an active BOM exists via `BOMService::getActiveBOM()`. Explodes the BOM to determine raw material requirements. Inserts `production_orders` header (status `planned`) and `production_order_lines`. |
| `issueRawMaterials(int $orderId): void` | Production order primary key | `void` | For each `production_order_lines` row, calls `StockLedgerService::postMovement()` with movement type `PRODUCTION_OUT`. Reduces raw material stock. Sets `production_orders.status = 'in_progress'`. |
| `postWIP(int $orderId, float $labourCost, float $overheadCost): void` | Production order primary key, direct labour cost to date, overhead cost to date | `void` | Posts a debit to the WIP account and credits to wages payable and overhead absorbed via `AccountingService::postJournal()`. Updates `production_orders.wip_balance`. |
| `completeProduction(int $orderId, float $actualYieldQty): void` | Production order primary key, actual quantity of finished goods produced | `void` | Calls `postYield()` to transfer WIP balance to finished goods. Sets `production_orders.status = 'completed'`. |
| `postYield(int $orderId, float $yieldQty): void` | Production order primary key, yield quantity | `void` | Posts `PRODUCTION_IN` movement for the finished goods item via `StockLedgerService::postMovement()`. Posts a debit to finished goods inventory and a credit to WIP via `AccountingService::postJournal()`. Records any yield variance. |

**Tables read/written:** `production_orders`, `production_order_lines`

---

## BOMService

**Namespace:** `App\Modules\Manufacturing`

**Module guard:** `ModuleRegistry::isActive('MANUFACTURING', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createBOM(int $finishedItemId, array $components, string $effectiveDate): int` | Finished goods item primary key, array of `['component_item_id', 'qty_per_unit', 'unit_of_measure']` entries, ISO 8601 effective date | New `bom_headers.id` | Inserts `bom_headers` (status `active`) and `bom_lines`. If a prior active BOM exists for the same finished item, it is automatically versioned via `versionBOM()`. |
| `getActiveBOM(int $finishedItemId): array` | Finished goods item primary key | BOM header row with nested component lines | Reads `bom_headers WHERE finished_item_id = :id AND tenant_id = :tenant_id AND status = 'active'` and joins `bom_lines`. Throws `NoBOMException` if none found. |
| `versionBOM(int $bomId): void` | BOM header primary key | `void` | Sets `bom_headers.status = 'superseded'` and writes `superseded_at = NOW()` for the given row. |

**Tables read/written:** `bom_headers`, `bom_lines`

---

## SalesCRMService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`, `SalesOrderService`, `CustomerService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `upsertAccount(array $data): int` | Associative array of account attributes (`account_name`, `external_ref`, `segment_code`, `territory_id`, `parent_account_id`, `owner_user_id`, `channel_partner_id`) | New or existing `crm_accounts.id` | Inserts or updates one row in `crm_accounts`. Enforces duplicate checks on legal name, tax identifier, and external reference before merge or create. |
| `registerContact(int $accountId, array $data): int` | Account primary key and contact attributes (`full_name`, `email`, `phone`, `role_title`, `decision_role`, `is_primary`) | New `crm_contacts.id` | Inserts one row into `crm_contacts`. If `is_primary = true`, clears the prior primary contact for the same account. |
| `createLead(array $data): int` | Associative array of lead attributes (`company_name`, `contact_name`, `email`, `phone`, `source`, `estimated_value`, `assigned_to`, `segment_code`) | New `crm_leads.id` | Inserts one row into `crm_leads` with `status = 'new'`. Lead identity matching runs before insert to prevent duplicate prospect creation. |
| `qualifyLead(int $leadId, array $qualification): void` | Lead primary key and qualification payload (`fit_score`, `need_confirmed`, `budget_confirmed`, `timeline_confirmed`, `decision_process_notes`) | `void` | Updates the lead qualification fields and sets `crm_leads.status` to `qualified` or `nurture` according to configured scoring thresholds. |
| `convertToOpportunity(int $leadId, int $accountId, int $primaryContactId): int` | Lead primary key, account primary key, contact primary key | New `crm_opportunities.id` | Copies lead data into `crm_opportunities`, links the opportunity to the chosen account and primary contact, and sets `crm_leads.status = 'converted'`. Initial stage is `qualification`. |
| `advanceOpportunityStage(int $opportunityId, string $stageCode, array $evidence = []): void` | Opportunity primary key, target stage code, optional evidence bundle | `void` | Validates stage exit criteria, updates `crm_opportunities.stage_code`, recalculates probability, and writes one row into `crm_opportunity_stage_history`. |
| `submitOpportunityApproval(int $opportunityId, string $approvalType, string $justification): int` | Opportunity primary key, approval type code (`DISCOUNT`, `NON_STANDARD_TERMS`, `STRATEGIC_BID`, `PARTNER_EXCEPTION`), justification | New `crm_opportunity_approvals.id` | Opens a governed approval request and freezes restricted commercial fields until an approval decision is recorded. |
| `recordQuoteHandoff(int $opportunityId, array $quoteContext): int` | Opportunity primary key and quote handoff attributes (`quote_number`, `pricing_basis`, `valid_until`, `currency_code`, `handoff_payload_hash`) | New `crm_quote_handoffs.id` | Records the CRM-to-ERP quote handoff event, stores the payload fingerprint, and waits for downstream order or quote execution status from ERP services. |
| `logActivity(int $accountId, ?int $opportunityId, string $activityType, string $notes, ?string $dueAt = null): int` | Account primary key, optional opportunity primary key, activity type code (`CALL`, `EMAIL`, `MEETING`, `DEMO`, `TASK`), free-text notes, optional ISO 8601 due date/time | New `crm_activities.id` | Inserts one row into `crm_activities`, associates it to the account and optional opportunity, and updates the relevant last-activity timestamps. |
| `getCustomerFinancialContext(int $accountId): array` | Account primary key | `['credit_status' => string, 'receivables_ageing' => array, 'open_orders' => array, 'last_payment_date' => string|null]` | Returns a read-only financial context assembled from ERP customer, order, receivables, and credit-control data. CRM does not update financial truth. |
| `getForecast(string $month): array` | Target month in `YYYY-MM` format | Array of opportunity rows with `['name', 'stage', 'probability', 'weighted_value']` | Queries open opportunities and aggregates pipeline by stage, owner, and expected close month. $weighted\_value = estimated\_value \times probability$. |

**Tables read/written:** `crm_accounts`, `crm_account_hierarchies`, `crm_contacts`, `crm_leads`, `crm_opportunities`, `crm_opportunity_stage_history`, `crm_opportunity_approvals`, `crm_activities`, `crm_quote_handoffs`

### CRM Boundary Notes

- `SalesCRMService` owns selling and service workflow, account intelligence, pipeline evidence, and customer interaction history.
- `CustomerService`, `SalesOrderService`, and `AccountingService` remain the source of truth for customer masters in execution contexts, order execution, invoicing, receivables, credit exposure, and financial balances.
- CRM may originate quote intent and handoff payloads, but ERP owns executable orders, shipment, invoicing, taxation, and revenue recognition.

---

## AccountPlanningService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `SalesCRMService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `setSegmentationModel(array $data): int` | Segmentation model attributes (`name`, `effective_from`, `criteria_json`, `owner_user_id`) | New `crm_segmentation_models.id` | Inserts one row into `crm_segmentation_models`. Criteria are versioned so prior account classifications remain auditable. |
| `classifyAccount(int $accountId, string $segmentCode, string $tierCode, ?string $reason = null): void` | Account primary key, segment code, tier code, optional reason | `void` | Writes or updates the active segment assignment for the account and preserves history in `crm_account_segment_history`. |
| `createAccountPlan(int $accountId, array $data): int` | Account primary key and plan attributes (`plan_year`, `growth_goal`, `renewal_risk`, `white_space_summary`, `owner_user_id`) | New `crm_account_plans.id` | Inserts one row into `crm_account_plans`. |
| `setAccountPlanInitiative(int $planId, array $data): int` | Account plan primary key and initiative attributes (`initiative_name`, `target_value`, `due_date`, `status`) | New `crm_account_plan_initiatives.id` | Inserts one row into `crm_account_plan_initiatives` tied to the account plan. |
| `getPriorityAccounts(string $period): array` | Planning period in `YYYY` or `YYYY-MM` format | Prioritized account rows with segment, plan status, and risk indicators | Returns accounts ranked by segment, whitespace, active opportunities, renewal risk, and customer health signals. |

**Tables read/written:** `crm_segmentation_models`, `crm_account_segment_history`, `crm_account_plans`, `crm_account_plan_initiatives`

---

## OpportunityGovernanceService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `SalesCRMService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `setStagePolicy(string $pipelineCode, array $policy): int` | Pipeline code and stage-policy payload (`stage_code`, `required_fields`, `approval_rules_json`, `probability_pct`) | New `crm_pipeline_stage_policies.id` | Inserts or updates stage-governance policy rows for the given pipeline. |
| `submitOpportunityReview(int $opportunityId, string $reviewType, string $notes): int` | Opportunity primary key, review type (`PIPELINE_REVIEW`, `DEAL_DESK`, `FORECAST_COMMIT`), notes | New `crm_opportunity_reviews.id` | Creates a governed opportunity review record with due date and owner. |
| `recordApprovalDecision(int $approvalId, string $decision, ?string $comment = null): void` | Approval primary key, decision (`APPROVED`, `REJECTED`), optional comment | `void` | Updates the approval row, records the approver and timestamp, and unblocks or rejects the relevant commercial exception. |
| `getCommitForecast(string $month): array` | Target month in `YYYY-MM` format | Forecast summary grouped by seller, stage, and commit status | Reads governed opportunities, excludes unapproved exception deals from commit totals, and returns forecast aggregates. |

**Tables read/written:** `crm_pipeline_stage_policies`, `crm_opportunity_reviews`, `crm_opportunity_approvals`

---

## QuoteToCashHandoffService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `SalesOrderService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `prepareQuoteHandoff(int $opportunityId): array` | Opportunity primary key | Canonical quote handoff payload | Builds a normalized payload containing account, contact, commercial terms, item lines, and approval references for ERP execution. |
| `submitQuoteHandoff(int $opportunityId, array $payload): int` | Opportunity primary key and handoff payload | New `crm_quote_handoffs.id` | Persists the payload hash, posts the handoff event, and marks the opportunity as `pending_execution` if all mandatory approvals exist. |
| `recordERPExecutionFeedback(int $handoffId, array $feedback): void` | Handoff primary key and ERP feedback (`status`, `erp_quote_id`, `erp_order_id`, `error_message`) | `void` | Updates the handoff row with ERP acceptance, rejection, quote creation, or order conversion outcomes. |
| `getHandoffStatus(int $handoffId): array` | Handoff primary key | Handoff status, ERP references, and commercial exception notes | Returns CRM-to-ERP execution state for sales operations follow-up. |

**Tables read/written:** `crm_quote_handoffs`, `crm_quote_handoff_lines`

---

## CaseManagementService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `NotificationService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `openCase(int $accountId, array $data): int` | Account primary key and case attributes (`contact_id`, `case_type`, `priority_code`, `subject`, `description`, `channel_code`) | New `crm_cases.id` | Inserts one row into `crm_cases`, derives the applicable SLA policy, and starts the response and resolution clocks. |
| `assignCase(int $caseId, int $ownerUserId, ?int $queueId = null): void` | Case primary key, owner user primary key, optional queue primary key | `void` | Updates case ownership and writes a timeline event describing the assignment change. |
| `addCaseComment(int $caseId, string $comment, bool $isCustomerVisible): int` | Case primary key, comment body, customer-visible flag | New `crm_case_comments.id` | Inserts one row into `crm_case_comments` and mirrors it into `crm_case_timeline_events`. |
| `escalateCase(int $caseId, string $escalationReason, int $toUserId): int` | Case primary key, escalation reason, target user primary key | New `crm_case_escalations.id` | Records the escalation, updates the case severity if needed, and emits notifications according to the SLA policy. |
| `resolveCase(int $caseId, string $resolutionCode, string $resolutionSummary): void` | Case primary key, resolution code, resolution summary | `void` | Stops SLA clocks, sets `crm_cases.status = 'resolved'`, and records one final timeline event. |
| `getSLAWatchlist(): array` | None | Open case rows nearing or breaching SLA | Returns active cases ordered by SLA breach risk and escalation state. |

**Tables read/written:** `crm_cases`, `crm_case_comments`, `crm_case_timeline_events`, `crm_case_escalations`, `crm_sla_policies`

---

## CustomerHealthService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`, `SalesCRMService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `captureHealthSignal(int $accountId, array $data): int` | Account primary key and signal attributes (`signal_type`, `signal_score`, `observed_at`, `source_system`, `notes`) | New `crm_customer_health_signals.id` | Inserts one row into `crm_customer_health_signals` from usage, service, commercial, or financial context inputs. |
| `recalculateHealthScore(int $accountId): void` | Account primary key | `void` | Aggregates active health signals, recent cases, renewal posture, and financial context into the current account health score. |
| `registerRenewal(int $accountId, array $data): int` | Account primary key and renewal attributes (`contract_ref`, `renewal_date`, `renewal_value`, `renewal_owner_user_id`) | New `crm_renewals.id` | Inserts one row into `crm_renewals` and attaches the account to the renewal watchlist. |
| `getRenewalWatchlist(string $fromMonth, string $toMonth): array` | Inclusive month range in `YYYY-MM` format | Renewal rows with health, risk, and open-case indicators | Returns upcoming renewals with combined selling, service, and financial warning signals. |

**Tables read/written:** `crm_customer_health_signals`, `crm_account_health_scores`, `crm_renewals`

---

## ChannelPartnerService

**Namespace:** `App\Modules\SalesCRM`

**Module guard:** `ModuleRegistry::isActive('SALES_CRM', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `SalesCRMService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `registerChannelPartner(array $data): int` | Partner attributes (`partner_name`, `partner_type`, `coverage_region`, `tier_code`, `owner_user_id`) | New `crm_channel_partners.id` | Inserts one row into `crm_channel_partners`. |
| `linkAccountToPartner(int $accountId, int $partnerId, string $relationshipType): int` | Account primary key, partner primary key, relationship type (`RESELLER`, `DISTRIBUTOR`, `IMPLEMENTER`, `REFERRAL`) | New `crm_account_partner_links.id` | Inserts one row linking a customer account to a partner relationship. |
| `registerPartnerDeal(int $partnerId, int $opportunityId, array $data): int` | Partner primary key, opportunity primary key, deal registration attributes (`registration_date`, `protection_expiry`, `channel_discount_pct`) | New `crm_partner_deals.id` | Inserts one row into `crm_partner_deals` and blocks duplicate partner registration on the same opportunity while active. |
| `getPartnerPipeline(int $partnerId): array` | Partner primary key | Open partner opportunity rows with stage, forecast, and renewal context | Returns the governed pipeline associated with the partner. |

**Tables read/written:** `crm_channel_partners`, `crm_account_partner_links`, `crm_partner_deals`

---

## SalesAgentService

**Namespace:** `App\Modules\SalesAgents`

**Module guard:** `ModuleRegistry::isActive('SALES_AGENTS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `registerAgent(array $data): int` | Associative array of agent attributes (`name`, `phone`, `email`, `commission_type`, `commission_rate`) | New `sales_agents.id` | Inserts one row into `sales_agents`. Commission types are `FLAT` (fixed amount per sale) or `PERCENT` (percentage of invoice value). |
| `setTarget(int $agentId, string $period, float $targetAmount): void` | Agent primary key, target period in `YYYY-MM`, target sales amount | `void` | Upserts a row in `agent_targets`. |
| `attributeSale(int $agentId, int $invoiceId): void` | Agent primary key, invoice primary key | `void` | Inserts a row into `agent_sales` linking the agent to the invoice. Throws `DuplicateAttributionException` if the invoice is already attributed. |
| `runCommission(string $period): int` | Commission period in `YYYY-MM` | New `commission_runs.id` | For each agent with attributed sales in the period, calculates commission: $commission = \sum(invoice\_value \times rate)$ for PERCENT type, or $\sum(flat\_rate)$ for FLAT type. Inserts `commission_runs` header and `commission_run_lines`. Status is `pending`. |
| `approveCommission(int $runId): void` | Commission run primary key | `void` | Verifies the approving user holds `APPROVE_COMMISSION`. Sets `commission_runs.status = 'approved'`. |
| `bulkPayAgents(int $runId, string $paymentMethod): string` | Commission run primary key, payment method code (`BANK`, `MTN_MOMO`, `AIRTEL_MOMO`) | Path to the generated payment file | Posts commission expense debits and commission payable credits via `AccountingService::postJournal()`. Generates a disbursement file in the format appropriate for the chosen payment method. |

**Tables read/written:** `sales_agents`, `agent_targets`, `agent_sales`, `commission_runs`, `commission_run_lines`

---

## CooperativeService

**Namespace:** `App\Modules\Cooperative`

**Module guard:** `ModuleRegistry::isActive('COOPERATIVE', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `registerFarmer(array $data): int` | Associative array of farmer attributes (`name`, `national_id`, `phone`, `village`, `group_id`) | New `cooperative_farmers.id` | Inserts one row into `cooperative_farmers`. |
| `openIntakePeriod(string $crop, string $startDate, string $endDate, float $pricePerKg): int` | Crop name, ISO 8601 start date, ISO 8601 end date, buying price per kilogram | New `intake_periods.id` | Inserts one row into `intake_periods` with `status = 'open'`. |
| `recordIntake(int $intakePeriodId, int $farmerId, float $weightKg, string $source): int` | Intake period primary key, farmer primary key, weight in kilograms, source code (`WEIGHBRIDGE` for RS-232 scale, `MANUAL` for hand entry) | New `intake_records.id` | Inserts one row into `intake_records`. When `source = 'MANUAL'`, a supervisor `user_id` is required and stored for audit. Calculates `amount_payable = weightKg * intake_periods.price_per_kg`. |
| `calculatePayment(int $intakePeriodId): void` | Intake period primary key | `void` | Aggregates all `intake_records` for the period by farmer. Writes totals to `farmer_payment_summaries`. Posts the corresponding produce expense debit and produce payable credit via `AccountingService::postJournal()`. |
| `bulkPayFarmers(int $intakePeriodId, string $paymentMethod): string` | Intake period primary key, payment method code (`MTN_MOMO`, `AIRTEL_MOMO`, `BANK`) | Path to the generated payment file | Reads `farmer_payment_summaries` for the period. Generates a disbursement file. Sets `intake_periods.status = 'paid'`. |

**Tables read/written:** `cooperative_farmers`, `intake_periods`, `intake_records`, `farmer_payment_summaries`

---

## ProjectService

**Namespace:** `App\Modules\Projects`

**Module guard:** `ModuleRegistry::isActive('PROJECTS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`, `SalesInvoiceService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createProject(array $data): int` | Associative array of project attributes (`name`, `customer_id`, `billing_type`, `budget`, `start_date`, `end_date`) | New `projects.id` | `billing_type` is one of `TIME_AND_MATERIAL`, `FIXED_PRICE`, or `MILESTONE`. Inserts one row into `projects` with `status = 'active'`. |
| `addTask(int $projectId, array $data): int` | Project primary key, task attributes (`name`, `assigned_to`, `estimated_hours`, `due_date`) | New `project_tasks.id` | Inserts one row into `project_tasks`. |
| `logTimesheet(int $taskId, int $userId, string $date, float $hours, float $hourlyRate): int` | Task primary key, user primary key, ISO 8601 date, hours worked, billing rate | New `timesheets.id` | Inserts one row into `timesheets`. Accumulates cost against `projects.cost_to_date`. |
| `calculateTMBilling(int $projectId, string $periodStart, string $periodEnd): array` | Project primary key, ISO 8601 start date, ISO 8601 end date | Array of billable timesheet rows with totals | Reads `timesheets WHERE project_id = :id AND date BETWEEN :start AND :end`. $billable\_amount = \sum(hours \times hourly\_rate)$. |
| `triggerMilestoneBilling(int $milestoneId): int` | Project milestone primary key | New `invoices.id` | Validates that `project_milestones.status = 'completed'`. Calls `SalesInvoiceService::createInvoice()` with the milestone amount. |
| `getProjectPnL(int $projectId): array` | Project primary key | `['revenue' => float, 'cost' => float, 'gross_margin' => float, 'margin_pct' => float]` | Reads all invoices and timesheets for the project. $gross\_margin = revenue - cost$, $margin\_pct = (gross\_margin / revenue) \times 100$. |

**Tables read/written:** `projects`, `project_tasks`, `timesheets`, `project_milestones`

---

## StrategyService

**Namespace:** `App\Modules\Strategy`

**Module guard:** `ModuleRegistry::isActive('STRATEGY_BSC', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `setObjective(array $data): int` | Associative array of BSC objective attributes (`name`, `perspective`, `description`, `owner_id`) | New `bsc_objectives.id` | `perspective` is one of `FINANCIAL`, `CUSTOMER`, `INTERNAL_PROCESS`, `LEARNING_GROWTH`. Inserts one row into `bsc_objectives`. |
| `setKPI(int $objectiveId, array $data): int` | Objective primary key, KPI attributes (`name`, `unit`, `target_value`, `frequency`, `measurement_source`) | New `bsc_kpis.id` | Inserts one row into `bsc_kpis`. `frequency` is `MONTHLY`, `QUARTERLY`, or `ANNUAL`. |
| `recordActual(int $kpiId, string $period, float $actualValue): void` | KPI primary key, measurement period in `YYYY-MM`, actual measured value | `void` | Upserts a row in `bsc_actuals`. |
| `computeRAGScore(int $kpiId, string $period): string` | KPI primary key, measurement period | RAG status code: `RED`, `AMBER`, or `GREEN` | Reads `bsc_actuals.actual_value` and `bsc_kpis.target_value`. $score = (actual / target) \times 100$. GREEN if $score \geq 90\%$, AMBER if $score \geq 70\%$ and $< 90\%$, RED if $score < 70\%$. |
| `generateScorecardReport(string $period): array` | Measurement period in `YYYY-MM` | Array of objective rows each with nested KPI rows and RAG scores | Reads from `v_bsc_scorecard` filtered by `tenant_id` and `period`. |

**Views read:** `v_bsc_scorecard`

**Tables read/written:** `bsc_objectives`, `bsc_kpis`, `bsc_actuals`

---

## AssetService

**Namespace:** `App\Modules\Assets`

**Module guard:** `ModuleRegistry::isActive('ASSETS', $tenantId)`

**Dependencies:** `PDO`, `SessionService`, `AuditService`, `AccountingService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `registerAsset(array $data): int` | Associative array of asset attributes (`name`, `category_id`, `acquisition_date`, `acquisition_cost`, `useful_life_months`, `depreciation_method`, `residual_value`, `gl_account_id`) | New `assets.id` | `depreciation_method` is `STRAIGHT_LINE` or `REDUCING_BALANCE`. Inserts one row into `assets` with `status = 'active'`. Posts the acquisition debit to the asset GL account via `AccountingService::postJournal()`. |
| `runDepreciation(int $periodId): void` | Accounting period primary key | `void` | For each active asset, calculates the depreciation charge. Straight-line: $charge = (acquisition\_cost - residual\_value) / useful\_life\_months$. Reducing balance: $charge = book\_value \times (rate / 12)$. Posts debit to depreciation expense and credit to accumulated depreciation via `AccountingService::postJournal()`. Inserts `depreciation_records` rows. |
| `disposeAsset(int $assetId, float $saleProceeds, int $periodId): void` | Asset primary key, sale proceeds (0 if written off), accounting period primary key | `void` | Calculates net book value = acquisition cost − accumulated depreciation. Posts disposal entries: removes accumulated depreciation, removes asset cost, records proceeds, posts gain or loss to the appropriate GL account. Sets `assets.status = 'disposed'`. |
| `transferAsset(int $assetId, int $toBranchId): void` | Asset primary key, destination branch primary key | `void` | Updates `assets.branch_id`. Logs to `AuditService`. |
| `scheduleMaintenanceWork(int $assetId, string $scheduledDate, string $description): int` | Asset primary key, ISO 8601 scheduled date, work description | New `maintenance_schedules.id` | Inserts one row into `maintenance_schedules` with `status = 'scheduled'`. |

**Tables read/written:** `assets`, `depreciation_records`, `maintenance_schedules`
