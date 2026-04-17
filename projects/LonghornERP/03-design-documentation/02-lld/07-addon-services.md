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

**Dependencies:** `PDO`, `SessionService`, `AuditService`

| Method | Parameters | Returns | Description |
|---|---|---|---|
| `createLead(array $data): int` | Associative array of lead attributes (`company_name`, `contact_name`, `email`, `phone`, `source`, `estimated_value`, `assigned_to`) | New `crm_leads.id` | Inserts one row into `crm_leads` with `status = 'new'`. |
| `convertToOpportunity(int $leadId): int` | Lead primary key | New `crm_opportunities.id` | Copies lead data into `crm_opportunities`. Sets `crm_leads.status = 'converted'`. Initial opportunity stage is `qualification`. |
| `logActivity(int $opportunityId, string $activityType, string $notes, ?string $nextActionDate = null): int` | Opportunity primary key, activity type code (`CALL`, `EMAIL`, `MEETING`, `DEMO`), free-text notes, optional ISO 8601 next action date | New `crm_activities.id` | Inserts one row into `crm_activities`. Updates `crm_opportunities.last_activity_at`. |
| `getForecast(string $month): array` | Target month in `YYYY-MM` format | Array of opportunity rows with `['name', 'stage', 'probability', 'weighted_value']` | Queries `crm_opportunities WHERE expected_close_month = :month AND tenant_id = :tenant_id AND status = 'open'`. $weighted\_value = estimated\_value \times probability$. |

**Tables read/written:** `crm_leads`, `crm_opportunities`, `crm_activities`

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
