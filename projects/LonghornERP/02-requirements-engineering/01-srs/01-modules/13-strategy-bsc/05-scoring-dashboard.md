# RAG Scoring, Executive Scorecard Dashboard, and Drill-Down Navigation

## 5.1 Overview

The RAG scoring engine converts each KPI's actual-vs-target ratio into a traffic-light status that propagates upward through the hierarchy: KPI → Objective → Perspective → Overall Scorecard. The executive dashboard presents this hierarchy in a single-screen layout designed for board-level consumption, with drill-down capability to the underlying data.

## 5.2 RAG Scoring Formula and Thresholds

**FR-BSC-034:** The system shall calculate the score for each KPI using the formula:

$$Score = \left(\frac{Actual}{Target}\right) \times 100$$

For inverse-polarity KPIs (see FR-BSC-020), the system shall use:

$$Score = \left(\frac{Target}{Actual}\right) \times 100$$

The system shall cap the displayed score at 200% to prevent outlier values from distorting dashboard scales; the underlying calculated value shall remain uncapped in the database.

**FR-BSC-035:** The system shall assign a RAG status to each KPI based on the score and the thresholds configured per FR-BSC-018:

- **Green:** $Score \geq amber\_threshold$
- **Amber:** $red\_threshold \leq Score < amber\_threshold$
- **Red:** $Score < red\_threshold$

When no actual value has been recorded for the current period, the system shall display the KPI status as **No Data** (rendered in neutral grey) rather than Red, to avoid misrepresenting missing data as underperformance.

**FR-BSC-036:** The system shall calculate an aggregate RAG status for each strategic objective by applying the same threshold logic to the objective's aggregate score computed per FR-BSC-022; where thresholds are not configured at the objective level, the system shall inherit the modal (most-frequent) RAG threshold from the linked KPIs.

**FR-BSC-037:** The system shall calculate an aggregate RAG status for each BSC perspective by applying majority-rule logic: the perspective status shall be Red if ≥ 50% of its active objectives are Red; Amber if < 50% are Red and ≥ 30% are Amber; Green otherwise.

## 5.3 Executive Scorecard Dashboard

**FR-BSC-038:** The system shall display an executive scorecard dashboard accessible to users with the `executive`, `strategy.admin`, or `strategy.viewer` role; the dashboard shall render within ≤ 2 seconds at P95 under a load of 50 concurrent dashboard sessions on the same tenant.

**FR-BSC-039:** The dashboard shall present the following elements without requiring scrolling on a standard 1920×1080 display:

- Tenant mission and vision statements (collapsible).
- Active strategic themes as colour-coded filter chips.
- All active BSC perspectives displayed as cards, each showing the perspective name, aggregate RAG indicator, count of objectives per RAG status (green/amber/red/no-data), and a mini spark-line of the perspective's aggregate score trend over the last 6 periods.

**FR-BSC-040:** The system shall allow a user to filter the scorecard dashboard by strategic theme, perspective, reporting period, or objective owner; applying a filter shall update all dashboard cards within ≤ 1 second without a full page reload.

**FR-BSC-041:** The system shall display a **Scorecard Summary Banner** at the top of the dashboard showing: total active objectives, count by RAG status, count with No Data, and the reporting period currently displayed; the banner shall include a **Report Period** selector allowing the user to navigate to any prior period for which actuals exist.

## 5.4 Traffic-Light Display

**FR-BSC-042:** The system shall render RAG status throughout the dashboard and all sub-screens using consistent colour coding: Green as `#28a745`, Amber as `#ffc107`, Red as `#dc3545`, and No Data as `#6c757d`; these colours shall never be used for any other purpose within the Strategy and BSC module UI.

**FR-BSC-043:** The system shall render RAG status indicators in a form that does not rely on colour alone, in compliance with WCAG 2.1 AA accessibility guidelines; each RAG indicator shall include an accessible text label ("Green", "Amber", "Red", or "No Data") readable by screen readers.

## 5.5 Drill-Down Navigation

**FR-BSC-044:** The system shall implement 3-level drill-down navigation on the executive dashboard:

1. **Perspective → Objectives:** Selecting a perspective card shall expand or navigate to a list of all strategic objectives within that perspective, each showing its title, owner, aggregate score, RAG status, and count of linked KPIs.
2. **Objective → KPIs:** Selecting a strategic objective shall navigate to the objective detail screen, listing all linked KPIs with their current actual, target, score, RAG status, last updated date, and data source type.
3. **KPI → Actual History:** Selecting a KPI shall navigate to the KPI detail screen showing the full actual-value history table (period, actual, target, score, RAG status, source, entered-by) and a line chart of score trend over the most recent 12 periods.

Each drill-down level shall include a breadcrumb navigation component allowing one-click return to any parent level.
