# Feature: Retail KPI Dashboard & Weekly Business Review

## Description

Retail performance management capabilities for KPI definitions, dashboards, root-cause diagnosis, weekly business review cadence, and action tracking.

## Standard Capabilities

- Metric dictionary with owner, formula, grain, source system, refresh cadence, and reconciliation status.
- Dashboard views by executive, merchant, store operations, digital, fulfilment, finance, and loss-prevention roles.
- Drilldowns by store, channel, category, SKU, promotion, vendor, customer segment, fulfilment type, and time period.
- KPI families: sales, gross margin, sell-through, stock cover, out-of-stock, markdown rate, promotion performance, conversion, search zero-result rate, return rate, fulfilment SLA, shrink, labour productivity, vendor recovery, and action closure.
- Variance reason capture with controlled reason codes and narrative note where required.
- Weekly business review action register with issue, owner, due date, source metric, dependency, status, and closure evidence.
- Data freshness indicators and exception banners for stale or unreconciled metrics.
- Exportable management pack with source lineage and version timestamp.

## Finance and Control Hooks

- Financial KPIs must reconcile to finance-approved datasets or show unreconciled status.
- Gross margin, markdown, shrink, return, vendor funding, and cash/POS metrics must expose source lineage.
- WBR actions that require accounting, stock, refund, or vendor-claim action must route to the relevant finance/control queue.

## Linked NFRs

- RET-NFR-006 Product Data Quality
- RET-NFR-007 Retail Event Auditability
- RET-NFR-008 Dashboard Freshness
