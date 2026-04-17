# Sales Forecasting and Territory Management

## 6.1 Sales Forecasting

**FR-CRM-027** — The system shall generate a monthly sales forecast by aggregating the weighted pipeline value of all opportunities with an expected close date in that month: $Forecast_{month} = \sum_{i \in month} EstimatedValue_i \times (CloseProb_i \div 100)$.

**FR-CRM-028** — The system shall provide a forecast accuracy report that compares, for each closed month, the forecast generated at the start of the month to the actual revenue from won opportunities; the report shall display the forecast accuracy ratio and the variance.

**FR-CRM-029** — The system shall provide a quarterly forecast view showing: total pipeline by stage, weighted forecast, committed deals (probability ≥ 80%), best-case scenario (all open deals win), and worst-case scenario (only committed deals close).

**FR-CRM-030** — The system shall allow a sales manager to apply a subjective override to any representative's monthly forecast; the override shall record the manager's identity, the original system-computed value, the overridden value, and the override justification.

## 6.2 Territory Management

**FR-CRM-031** — When an administrator creates a territory, the system shall record: territory name, geographic scope (country, region, county — as text or linked to a GIS polygon `[CONTEXT-GAP: GAP-010 — GIS territory polygon support]`), assigned sales representative(s), and assigned products or product categories.

**FR-CRM-032** — The system shall prevent a sales representative from creating an opportunity outside their assigned territory without a supervisor override; if the customer's country does not match the rep's territory, the system shall warn the rep and require their manager to approve the out-of-territory assignment.

**FR-CRM-033** — The system shall generate a territory performance report showing: each territory's total pipeline, closed won revenue, win rate, and average deal size for a selected period, enabling management to identify underperforming territories.
