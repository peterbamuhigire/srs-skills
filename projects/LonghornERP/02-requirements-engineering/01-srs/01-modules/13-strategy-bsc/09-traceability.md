# Traceability Matrix — Strategy and Balanced Scorecard

## 9.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6, and records the IEEE 830 verifiability criterion (the deterministic test oracle) for each requirement. All FRs without a mapping to a business goal are flagged `[TRACE-GAP]`.

## 9.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-BSC-001 | Integrated strategy definition and monitoring — replacing disconnected spreadsheets |
| BG-BSC-002 | Real-time KPI visibility through automated ERP data feeds |
| BG-BSC-003 | NGO, government, and donor framework support (logframe, NDP III) |
| BG-BSC-004 | Audit readiness — immutable history, audit trails, role-based access |
| BG-BSC-005 | Board-ready PDF report generation from live scorecard data |

## 9.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | Test Oracle |
|---|---|---|---|---|
| FR-BSC-001 | 2.2 | Create/update mission and vision statements | BG-BSC-001 | Save mission text; verify it appears at the top of the scorecard dashboard. |
| FR-BSC-002 | 2.2 | Create strategic theme with name, description, colour | BG-BSC-001 | Create theme; verify it appears as a filter chip on the dashboard in the configured colour. |
| FR-BSC-003 | 2.2 | Edit theme; block deletion of theme with active objectives | BG-BSC-001, BG-BSC-004 | Attempt delete on theme with 2 linked objectives; verify HTTP 422 with count of linked objectives. |
| FR-BSC-004 | 2.2 | Display themes as colour-coded filter chips on dashboard | BG-BSC-001 | Navigate to dashboard; verify theme chips visible and filter activates correctly. |
| FR-BSC-005 | 2.3 | Pre-populate 4 default BSC perspectives at module activation | BG-BSC-001 | Activate BSC module for new tenant; verify 4 perspectives exist with correct names and display order. |
| FR-BSC-006 | 2.3 | Rename, reorder, toggle, block deletion of perspective with objectives | BG-BSC-001, BG-BSC-004 | Rename "Financial" to "Finance"; verify dashboard reflects updated name. Attempt delete on perspective with objectives; verify rejection. |
| FR-BSC-007 | 2.3 | Create custom perspective; enforce max 8 active perspectives | BG-BSC-001 | Create 5th perspective; verify success. Attempt to create 9th; verify HTTP 422. |
| FR-BSC-008 | 2.3 | Hide perspectives on dashboard in OKR mode; restore on revert | BG-BSC-001 | Switch to OKR mode; verify perspectives absent from dashboard. Switch back to BSC; verify perspectives restored. |
| FR-BSC-009 | 2.4 | Set framework mode (BSC / OKR / Hybrid) | BG-BSC-001 | Switch to Hybrid mode; verify both BSC and OKR tabs present on dashboard. |
| FR-BSC-010 | 2.4 | Audit log on framework mode change | BG-BSC-004 | Change framework mode; verify audit log entry with user_id, from_mode, to_mode, timestamp. |
| FR-BSC-011 | 3.2 | Create strategic objective with mandatory fields; assign OBJ-NNNN ID | BG-BSC-001 | Submit valid objective form; verify OBJ-NNNN identifier assigned and objective appears under correct perspective. |
| FR-BSC-012 | 3.2 | Require change reason on title/period edit when actuals exist | BG-BSC-004 | Edit title of objective with actuals; verify change-reason field is mandatory and blocks save if empty. |
| FR-BSC-013 | 3.2 | Manage objective status; block deletion if linked KPIs or initiatives exist | BG-BSC-001, BG-BSC-004 | Attempt delete on objective with 3 KPIs; verify HTTP 422 listing linked item counts. |
| FR-BSC-014 | 3.2 | Display objectives grouped by perspective, sortable and filterable | BG-BSC-001 | Navigate to BSC configuration; verify objectives grouped by perspective and sort by owner works. |
| FR-BSC-015 | 3.3 | Create KPI with mandatory fields; assign KPI-NNNN ID | BG-BSC-001, BG-BSC-002 | Submit valid KPI form; verify KPI-NNNN identifier assigned and KPI appears under correct objective. |
| FR-BSC-016 | 3.3 | Define KPI formula with ERP token validation | BG-BSC-002 | Save formula with valid GL token; verify success. Save formula with undefined token; verify validation error identifying the token. |
| FR-BSC-017 | 3.3 | Set numeric target and baseline per period | BG-BSC-001 | Set target for Q1 and Q2 separately; verify each period stores independent target value. |
| FR-BSC-018 | 3.3 | Configure RAG thresholds; enforce red_threshold < amber_threshold | BG-BSC-001, BG-BSC-004 | Set amber = 80, red = 60; verify saved. Set amber = 50, red = 70; verify HTTP 422. |
| FR-BSC-019 | 3.3 | Display KPI detail panel with all specified fields | BG-BSC-001 | Select KPI from scorecard; verify all 11 specified fields are visible in the detail panel. |
| FR-BSC-020 | 3.3 | Inverse-polarity KPI scoring | BG-BSC-001 | Mark KPI as inverse; enter actual lower than target; verify score > 100%. Verify inverse indicator displayed. |
| FR-BSC-021 | 3.4 | Enforce exactly-1 objective linkage per KPI | BG-BSC-001 | Attempt save KPI without objective_id; verify database constraint error. |
| FR-BSC-022 | 3.4 | Calculate aggregate objective score as unweighted mean of linked KPI scores | BG-BSC-001 | Link 3 KPIs with scores 80%, 60%, 100%; verify objective score = 80%. Link 0 KPIs; verify "No data." |
| FR-BSC-023 | 4.2 | Manual actual entry with period, comment, source = manual | BG-BSC-002 | Enter actual for Monthly KPI for March; verify kpi_actuals record with source = manual, correct period, entered_by. |
| FR-BSC-024 | 4.2 | Recalculate score and RAG within ≤ 3 seconds of manual entry | BG-BSC-002 | Submit manual actual; verify dashboard reflects updated score and RAG within 3 seconds. |
| FR-BSC-025 | 4.2 | Block manual entry on Auto-Pull KPIs | BG-BSC-002 | Attempt manual entry on Auto-Pull KPI; verify informational message and entry form blocked. |
| FR-BSC-026 | 4.2 | Allow strategy.admin to edit/delete manual actual in same period; audit log | BG-BSC-004 | Edit actual as strategy.admin; verify original and revised values recorded in audit log. |
| FR-BSC-027 | 4.3 | Auto-pull GL KPI actuals; set source = auto_gl | BG-BSC-002 | Configure GL:Revenue KPI; trigger collection; verify kpi_actuals record with source = auto_gl and correct amount from GL. |
| FR-BSC-028 | 4.3 | Apply period filter when querying GL data | BG-BSC-002 | Configure monthly GL KPI for March; verify actual equals GL monthly total, not YTD. |
| FR-BSC-029 | 4.4 | Auto-pull HR KPI actuals; set source = auto_hr | BG-BSC-002 | Configure HR:Headcount KPI; trigger collection; verify actual matches HR module headcount. |
| FR-BSC-030 | 4.5 | Auto-pull Sales KPI actuals; set source = auto_sales | BG-BSC-002 | Configure SALES:WinRate KPI; trigger collection; verify actual matches Sales module win-rate aggregate. |
| FR-BSC-031 | 4.6 | Auto-pull Projects KPI actuals; set source = auto_proj | BG-BSC-002 | Configure PROJ:OnTimeCompletionRate KPI; trigger collection; verify actual matches Projects module data. |
| FR-BSC-032 | 4.7 | Generate data collection task; mark Overdue after 5 business days | BG-BSC-002 | At period start, verify My Tasks queue shows Manual KPI task. Simulate 6 business days without entry; verify status = Overdue. |
| FR-BSC-033 | 4.7 | Data Collection Status screen with filters | BG-BSC-002 | Navigate to Data Collection Status; verify all KPIs listed with correct next due date and status. Filter by Overdue; verify only overdue rows shown. |
| FR-BSC-034 | 5.2 | KPI score formula; cap at 200%; inverse KPI formula | BG-BSC-001, BG-BSC-002 | Enter actual = target; verify score = 100%. Enter actual = 2× target; verify displayed score = 200% and raw value stored uncapped. |
| FR-BSC-035 | 5.2 | Assign RAG status per thresholds; No Data for missing actuals | BG-BSC-001 | Verify score ≥ amber_threshold → Green, red_threshold ≤ score < amber → Amber, below red → Red. Delete actuals; verify No Data (grey). |
| FR-BSC-036 | 5.2 | Aggregate objective RAG based on objective score | BG-BSC-001 | Set 2 KPIs to Red, 1 to Green; verify objective RAG reflects Red status per threshold logic. |
| FR-BSC-037 | 5.2 | Perspective RAG by majority rule | BG-BSC-001 | Configure 4 objectives in a perspective: 2 Red, 1 Amber, 1 Green; verify perspective = Red (50% Red). |
| FR-BSC-038 | 5.3 | Dashboard renders within ≤ 2 seconds at P95 | BG-BSC-001 | Load dashboard under 50 concurrent sessions; verify P95 render time ≤ 2 seconds via load test. |
| FR-BSC-039 | 5.3 | Dashboard presents all required elements without scrolling on 1920×1080 | BG-BSC-001 | Render dashboard on 1920×1080 viewport; verify mission/vision, theme chips, perspective cards visible without vertical scroll. |
| FR-BSC-040 | 5.3 | Dashboard filter updates within ≤ 1 second without page reload | BG-BSC-001 | Apply theme filter; verify dashboard re-renders within 1 second and no full page reload occurs (no navigation event). |
| FR-BSC-041 | 5.3 | Scorecard Summary Banner with period selector | BG-BSC-001 | Verify banner shows total objectives, RAG counts, No Data count. Navigate to prior period; verify historical actuals reflected. |
| FR-BSC-042 | 5.4 | Consistent RAG colour codes throughout UI | BG-BSC-001 | Inspect all RAG indicators; verify Green = #28a745, Amber = #ffc107, Red = #dc3545, No Data = #6c757d. |
| FR-BSC-043 | 5.4 | WCAG 2.1 AA — accessible text label on RAG indicators | BG-BSC-004 | Run screen reader on dashboard; verify each RAG indicator announces "Green", "Amber", "Red", or "No Data". |
| FR-BSC-044 | 5.5 | 3-level drill-down with breadcrumb navigation | BG-BSC-001 | Click perspective → verify objectives list. Click objective → verify KPI list. Click KPI → verify actual history and chart. Verify breadcrumb present at each level. |
| FR-BSC-045 | 6.2 | Create strategic initiative; assign INIT-NNNN ID | BG-BSC-001 | Submit valid initiative form; verify INIT-NNNN assigned and initiative appears in register. |
| FR-BSC-046 | 6.2 | Initiative status transitions; require reactivation reason | BG-BSC-001, BG-BSC-004 | Set initiative to Completed; attempt set to In Progress; verify reactivation reason field mandatory. |
| FR-BSC-047 | 6.2 | Calculate and display budget variance | BG-BSC-001 | Set planned = 10,000,000, actual = 8,000,000; verify BudgetVariance = 2,000,000 displayed. |
| FR-BSC-048 | 6.3 | Display linked initiatives on objective detail screen | BG-BSC-001 | Link initiative to objective; navigate to objective detail; verify initiative row visible with correct fields. |
| FR-BSC-049 | 6.3 | Initiatives section on dashboard with RAG-style status indicators | BG-BSC-001 | Create initiative with end date in 7 days and In Progress status; verify Amber indicator. |
| FR-BSC-050 | 6.4 | Initiative status update stored as immutable record | BG-BSC-004 | Post status update; inspect initiative_updates table; verify posted_by, posted_at, and all fields immutable (no edit/delete controls). |
| FR-BSC-051 | 6.4 | Display chronological status update history | BG-BSC-001 | Post 3 updates; navigate to initiative detail; verify updates listed newest-first. |
| FR-BSC-052 | 6.5 | Generate executive PDF report with all specified sections | BG-BSC-005 | Generate report; verify cover page, mission/vision, scorecard summary, perspectives, initiatives table, footer present in PDF output. |
| FR-BSC-053 | 6.5 | PDF generation within ≤ 15 seconds at P95; 90-day archive | BG-BSC-005 | Generate report under P95 load; verify completion ≤ 15 seconds. Verify report accessible from archive for 90 days. |
| FR-BSC-054 | 7.1 | Activate OKR mode; replace perspective hierarchy on dashboard | BG-BSC-001 | Set framework to OKR; verify perspectives hidden and OKR hierarchy shown on dashboard. |
| FR-BSC-055 | 7.1 | Create OKR Objective; assign OKR-OBJ-NNNN ID | BG-BSC-001 | Submit OKR objective; verify OKR-OBJ-NNNN assigned and objective appears in OKR list. |
| FR-BSC-056 | 7.1 | Add up to 5 Key Results per OKR Objective | BG-BSC-001 | Add 5 Key Results; verify all saved. Attempt to add 6th; verify HTTP 422. |
| FR-BSC-057 | 7.1 | Key Result progress score formula; Binary and inverse variants | BG-BSC-001 | Set start = 0, target = 100, current = 40; verify score = 40%. Set Binary KR to done; verify 100%. |
| FR-BSC-058 | 7.1 | OKR Objective confidence score as mean of KR scores; RAG thresholds | BG-BSC-001 | Link 2 KRs with scores 80% and 60%; verify objective score = 70% = Green. Score 50% and 30%; verify mean = 40% = Amber. |
| FR-BSC-059 | 7.1 | Weekly OKR check-in stored as immutable record | BG-BSC-004 | Post check-in; verify record with posted_by and posted_at; verify no edit/delete controls in UI. |
| FR-BSC-060 | 7.2 | Activate Logframe mode; add 4-level hierarchy; coexist with BSC/OKR | BG-BSC-003 | Activate Logframe; verify Activity/Output/Outcome/Impact levels available. Verify BSC perspectives still accessible. |
| FR-BSC-061 | 7.2 | Define Logframe Matrix entries at all 4 levels | BG-BSC-003 | Create Outcome entry with all required fields; verify stored and visible in logframe view. |
| FR-BSC-062 | 7.2 | Link Logframe Output/Outcome to BSC or OKR objective | BG-BSC-001, BG-BSC-003 | Link Logframe Outcome to BSC objective; verify cross-reference label on both records. |
| FR-BSC-063 | 7.2 | Record actual indicator values against Logframe entries | BG-BSC-003 | Enter actual against Logframe Output; verify audit trail identical to FR-BSC-023 manual entry. |
| FR-BSC-064 | 7.3 | Read-only NDP III reference data set; browseable and searchable | BG-BSC-003 | Search NDP III indicators for "agriculture"; verify matching results. Attempt to add NDP III record; verify option absent. |
| FR-BSC-065 | 7.3 | Map tenant KPI to NDP III indicator; NDP III Alignment Report | BG-BSC-003 | Map KPI to NDP III indicator; verify NDP III code displayed on KPI detail. Generate NDP III Alignment Report; verify mapped KPI appears with correct code, actual, target, RAG. |
| FR-BSC-066 | 7.4 | Create department workplan; assign WP-DEPT-NNNN ID | BG-BSC-001, BG-BSC-003 | Submit workplan with 3 activities; verify WP-DEPT-NNNN assigned and activities linked to strategic objectives. |
| FR-BSC-067 | 7.4 | Record activity completion status and percentage; department progress summary | BG-BSC-001 | Mark 2 of 3 activities Completed; verify progress summary shows 2/3 (67%) Completed on dept head dashboard. |
| FR-BSC-068 | 7.4 | Display Strategic Alignment indicator on workplan activities | BG-BSC-001 | Link activity to objective with Red RAG status; verify Red indicator visible on workplan activity row. |
