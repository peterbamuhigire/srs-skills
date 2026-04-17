# KPI Actual Data Collection

## 4.1 Overview

Actual values for KPIs are collected through 2 mechanisms: manual entry by the designated data collection owner, and automated data pull from operational Longhorn ERP modules. Both mechanisms write to the same `kpi_actuals` table; the `source` field distinguishes between them. A data collection schedule governs when actuals are due and flags overdue items.

## 4.2 Manual Actual Entry

**FR-BSC-023:** The system shall allow the KPI data collection owner (or any user with the `strategy.data_entry` role) to record an actual value for a KPI by selecting the KPI, entering a decimal value (up to 4 decimal places), selecting the reporting period, and optionally entering a comment (free text, max 500 characters); the system shall set `source = 'manual'` and record `entered_by`, `entry_timestamp`, and `period` on the resulting `kpi_actuals` record.

**FR-BSC-024:** The system shall immediately recalculate the KPI score and RAG status upon successful submission of a manual actual entry, using the formula $Score = (Actual \div Target) \times 100$ (or the inverse formula for inverse-polarity KPIs), and shall reflect the updated score and RAG status on the dashboard within ≤ 3 seconds of submission.

**FR-BSC-025:** The system shall prevent a user from entering a manual actual for a KPI whose data source type is set to Auto-Pull, and shall display an informational message explaining that the value is sourced automatically.

**FR-BSC-026:** The system shall allow an authorised user (`strategy.admin` role) to edit or delete a previously entered manual actual within the same reporting period it was entered; the system shall record the original value, the revised value, the editing user, and the edit timestamp in the audit log.

## 4.3 Automated Data Pull — Accounting (GL) Integration

**FR-BSC-027:** The system shall automatically populate actual values for KPIs whose data source is configured as `GL:Revenue`, `GL:GrossProfit`, `GL:EBITDA`, `GL:OperatingCost`, or `GL:BudgetVariance` by querying the Accounting module's aggregated period totals for the relevant GL account group at the scheduled collection frequency; the system shall set `source = 'auto_gl'` on the resulting `kpi_actuals` record.

**FR-BSC-028:** The system shall apply the KPI's configured period filter (e.g., monthly, quarterly, year-to-date) when querying GL data, ensuring that a monthly KPI receives the GL total for only the target calendar month and not a cumulative year-to-date figure unless explicitly configured as year-to-date.

## 4.4 Automated Data Pull — HR/Payroll Integration

**FR-BSC-029:** The system shall automatically populate actual values for KPIs configured as `HR:Headcount`, `HR:TurnoverRate`, `HR:AbsenteeismRate`, or `HR:TrainingHours` by querying the HR/Payroll module's workforce analytics aggregates at the scheduled collection frequency; the system shall set `source = 'auto_hr'` on the resulting `kpi_actuals` record.

## 4.5 Automated Data Pull — Sales Integration

**FR-BSC-030:** The system shall automatically populate actual values for KPIs configured as `SALES:Revenue`, `SALES:WinRate`, `SALES:AverageDealSize`, or `SALES:CustomerAcquisitionCount` by querying the Sales and Sales CRM module aggregates at the scheduled collection frequency; the system shall set `source = 'auto_sales'` on the resulting `kpi_actuals` record.

## 4.6 Automated Data Pull — Projects Integration

**FR-BSC-031:** The system shall automatically populate actual values for KPIs configured as `PROJ:OnTimeCompletionRate`, `PROJ:BudgetUtilisation`, or `PROJ:MilestoneAchievement` by querying the Projects module aggregates at the scheduled collection frequency; the system shall set `source = 'auto_proj'` on the resulting `kpi_actuals` record.

[CONTEXT-GAP: Projects module] — Confirm that a Projects module exists in the Longhorn ERP roadmap before implementing FR-BSC-031.

## 4.7 Data Collection Schedule

**FR-BSC-032:** The system shall generate a data collection task for each Manual-source KPI at the start of each collection period (as defined by the KPI's measurement frequency), assigned to the KPI's data collection owner; the task shall appear in the data collection owner's **My Tasks** queue and shall be marked Overdue if the actual value has not been entered within 5 business days of the period end date.

**FR-BSC-033:** The system shall display a **Data Collection Status** screen listing all KPIs with their collection frequency, last actual entry date, next due date, and status (Collected, Pending, Overdue); the screen shall be filterable by perspective, strategic theme, data source type, and status, and shall be accessible to users with the `strategy.admin` or `strategy.data_entry` role.
