# OKR Mode, NGO Logframe, NDP III Indicators, and Department Workplans

## 7.1 OKR Mode

**FR-BSC-054:** The system shall activate OKR mode for a tenant when a `strategy.admin` user sets the framework mode to OKR or Hybrid (see FR-BSC-009); in OKR mode, the system shall present the strategic hierarchy as Objective → Key Result, replacing the Perspective → Objective → KPI hierarchy on the dashboard.

**FR-BSC-055:** The system shall allow a `strategy.admin` user to create an OKR Objective by supplying: objective title (free text, max 200 characters), owner (active user account), time period (quarter or annual, with specific start and end dates), and optional parent objective (for cascaded OKRs); the system shall assign a unique identifier in the format `OKR-OBJ-{NNNN}`.

**FR-BSC-056:** The system shall allow a `strategy.admin` user or objective owner to add up to 5 Key Results per OKR Objective; each Key Result shall require: title (free text, max 160 characters), metric type (Numeric, Percentage, or Binary), start value, target value, and data source (Manual or Auto-Pull using the same ERP token syntax as FR-BSC-016); the system shall assign a unique identifier in the format `OKR-KR-{NNNN}`.

**FR-BSC-057:** The system shall calculate a Key Result progress score as:

$$KRScore = \left(\frac{Current - Start}{Target - Start}\right) \times 100$$

capped at 100%; for Binary Key Results (done/not-done), the score shall be 0% when not done and 100% when done; for inverse-polarity Key Results, the system shall use the inverse formula consistent with FR-BSC-020.

**FR-BSC-058:** The system shall calculate an OKR Objective confidence score as the unweighted mean of all linked Key Result scores:

$$OKRObjectiveScore = \frac{\sum_{i=1}^{n} KRScore_i}{n}$$

and shall display a progress indicator (0–100%) alongside a RAG status using the thresholds: Green ≥ 70%, Amber 40–69%, Red < 40%.

**FR-BSC-059:** The system shall allow the objective owner or any user with the `strategy.data_entry` role to post a weekly check-in for each OKR Objective, recording: confidence level (1–10 integer), status note (free text, max 500 characters), and any blockers (free text, max 500 characters); check-ins shall be stored as immutable records with `posted_by` and `posted_at` fields, and shall be displayed in chronological order in the OKR detail screen.

## 7.2 NGO Logframe Mapping

**FR-BSC-060:** The system shall allow a `strategy.admin` user to activate Logframe mode for the tenant, which adds a 4-level planning hierarchy: Activity → Output → Outcome → Impact; activating Logframe mode shall not disable BSC or OKR configuration; all 3 frameworks may coexist within a single tenant.

**FR-BSC-061:** The system shall allow a `strategy.admin` user to define a Logframe Matrix by creating entries at each of the 4 levels (Activity, Output, Outcome, Impact), each entry requiring: description (free text, max 500 characters), indicator (free text, max 200 characters), means of verification (free text, max 300 characters), assumptions (free text, max 300 characters), and responsible party (free text or linked user account).

**FR-BSC-062:** The system shall allow a `strategy.admin` user to link any Logframe Output or Outcome entry to a BSC strategic objective or OKR Objective, enabling a single strategic objective to be visible from both the scorecard view and the logframe view; the linkage shall be displayed as a cross-reference label on both records.

**FR-BSC-063:** The system shall allow a `strategy.data_entry` user to record actual indicator values against any Logframe entry for a specified reporting period, with the same manual entry and audit trail behaviour defined in FR-BSC-023 and FR-BSC-026.

## 7.3 NDP III Indicator Mapping

**FR-BSC-064:** The system shall maintain a read-only reference data set of Uganda NDP III indicators, seeded at platform installation, containing at minimum: NDP III indicator code, indicator description, NDP III goal, thematic area, and unit of measurement; `strategy.admin` users shall be able to browse and search this reference set but shall not be able to add, edit, or delete NDP III reference records.

**FR-BSC-065:** The system shall allow a `strategy.admin` user to map any tenant KPI or Logframe indicator to 1 or more NDP III reference indicators by selecting from the reference data set; once mapped, the KPI detail screen shall display the linked NDP III indicator codes and descriptions as reference labels, and a **NDP III Alignment Report** shall list all tenant KPIs that are mapped to NDP III indicators, showing the NDP III code, description, tenant KPI name, latest actual, target, and RAG status — exportable to PDF and Excel.

## 7.4 Department Workplan Linkage

**FR-BSC-066:** The system shall allow a `strategy.admin` user or department head (user with the `dept.head` role for their department) to create a department workplan for a defined period (quarter or annual) by supplying: department name (resolved from the HR module's department list), plan period, and a list of workplan activities each linked to at least 1 strategic objective; the system shall assign a unique identifier in the format `WP-{DEPT}-{NNNN}`.

**FR-BSC-067:** The system shall allow the department head or assigned activity owner to record the completion status (Not Started, In Progress, Completed, Deferred) and percentage completion (integer 0–100) for each workplan activity at any time; the system shall display a workplan progress summary on the department head's dashboard showing the count and percentage of activities per status for the current period.

**FR-BSC-068:** The system shall display a **Strategic Alignment** indicator on each workplan activity showing the RAG status of the linked strategic objective(s), providing department-level teams with direct visibility of how their operational activities contribute to strategic performance.
