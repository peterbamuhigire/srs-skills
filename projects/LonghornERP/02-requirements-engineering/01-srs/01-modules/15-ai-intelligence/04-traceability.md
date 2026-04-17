# Traceability Matrix — AI Intelligence Module

## 5.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6, and records the IEEE 830 verifiability criterion (the deterministic test oracle) for each requirement. All FRs without a mapping to a business goal are flagged `[TRACE-GAP]`.

## 5.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-AI-001 | Prevent cash flow crises through 90-day forward cash position visibility |
| BG-AI-002 | Detect internal fraud and unusual posting patterns through automated GL anomaly classification |
| BG-AI-003 | Eliminate stockouts and reduce over-stocking by generating data-driven reorder recommendations |
| BG-AI-004 | Reduce bad debt exposure by gating credit sales on a real-time customer payment risk score |
| BG-AI-005 | Make monthly financial accounts intelligible to non-accountant leadership |

## 5.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | PRD Reference | Test Oracle |
|---|---|---|---|---|---|
| FR-AI-001 | 3.1 | 90-day rolling cash flow forecast, 3 scenarios, nightly job | BG-AI-001 | AI Feature 1 (`10-ai-intelligence.md`) | Seed tenant with 90+ days AR/AP/payroll data; trigger job; verify 270 records in `ai_cashflow_forecast`; verify worst-case trough displayed on dashboard within 2,000 ms. |
| FR-AI-002 | 3.2 | Post-period GL anomaly scan, 4 classifiers, Anomaly Inbox | BG-AI-002 | AI Feature 2 (`10-ai-intelligence.md`) | Post journal with composite score ≥ 2 classifiers triggered; close period; verify flag written to `ai_anomaly_flags`; verify entry appears in Anomaly Inbox. |
| FR-AI-003 | 3.3 | Sunday demand forecast, weighted moving average, reorder panel | BG-AI-003 | AI Feature 3 (`10-ai-intelligence.md`) | Seed 90 days of sales history for 3 items; trigger Sunday job; verify `ai_demand_forecast` records; verify items with projected stock < 21 days appear in Reorder Recommendations panel. |
| FR-AI-004 | 3.4 | Credit order risk scorecard, Green/Amber/Red, Sales Manager gate | BG-AI-004 | AI Feature 4 (`10-ai-intelligence.md`) | Submit credit order for customer with composite score ≥ 25; verify order held; verify Sales Manager approval required; verify approval logged to audit trail; verify computation within 1,000 ms. |
| FR-AI-005 | 3.5 | Monthly narrative commentary via Claude API, push notification | BG-AI-005 | AI Feature 5 (`10-ai-intelligence.md`) | Close prior month; advance system date to 5th; trigger job with valid API key; verify commentary stored in `ai_narratives`; verify push notification sent to Finance Director and Managing Director roles; verify Finance Director can edit before Board Observer publication. |
