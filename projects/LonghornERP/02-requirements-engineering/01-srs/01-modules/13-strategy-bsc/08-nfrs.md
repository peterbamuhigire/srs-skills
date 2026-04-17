# Non-Functional Requirements for the Strategy and Balanced Scorecard Module

## 8.1 Overview

Non-functional requirements (NFRs) define the quality and constraint envelope within which all functional behaviour specified in Sections 2 through 7 must operate. Each NFR is assigned a unique identifier in the `NFR-BSC-NNN` series and is stated with a specific, measurable metric per IEEE 982.1.

## 8.2 Performance

**NFR-BSC-001:** The system shall render the executive scorecard dashboard — including all active perspective cards, RAG indicators, spark-line trends, and the scorecard summary banner — within ≤ 2 seconds at P95 for a tenant with up to 8 perspectives, 40 objectives, 120 KPIs, and 30 initiatives, measured under a load of 50 concurrent dashboard sessions on the same tenant.

**NFR-BSC-002:** The system shall recalculate and update all affected KPI scores, objective scores, perspective scores, and dashboard RAG indicators within ≤ 3 seconds of a manual actual entry submission (FR-BSC-024), measured from the server receiving the HTTP POST to the updated state being reflected in the dashboard API response.

**NFR-BSC-003:** The system shall complete the automated ERP data pull for all Auto-Pull KPIs on a single tenant within ≤ 60 seconds of the scheduled trigger time, for a tenant with up to 120 Auto-Pull KPIs pulling from the Accounting, HR/Payroll, Sales, and Projects modules concurrently.

**NFR-BSC-004:** The system shall generate the executive PDF report (FR-BSC-052) within ≤ 15 seconds at P95 for a tenant with up to 8 perspectives, 40 objectives, 120 KPIs, and 30 initiatives.

**NFR-BSC-005:** The system shall apply a dashboard filter (FR-BSC-040) and re-render the filtered scorecard within ≤ 1 second at P95, without a full page reload.

## 8.3 Reliability and Data Integrity

**NFR-BSC-006:** KPI actual records in the `kpi_actuals` table shall be immutable once the reporting period has been closed; the system shall enforce this at both the application layer (role check) and the database layer (row-level trigger), rejecting any UPDATE or DELETE with an application error.

**NFR-BSC-007:** Every write operation on the `strategic_objectives`, `kpis`, `kpi_actuals`, `initiatives`, `initiative_updates`, `okr_objectives`, `okr_key_results`, and `workplans` tables shall produce an audit log entry within the same database transaction, ensuring no write succeeds without a corresponding audit record.

**NFR-BSC-008:** The system shall retain all historical KPI actual values, initiative status updates, and OKR check-ins for the full tenure of the client subscription; no automated data purge shall be applied to these tables.

## 8.4 Availability

**NFR-BSC-009:** The Strategy and BSC module shall be available 99.5% of each calendar month, excluding scheduled maintenance windows announced ≥ 48 hours in advance; availability is measured as the ratio of successful health-check responses to total health-check requests against the BSC API over the month.

## 8.5 Security and Access Control

**NFR-BSC-010:** BSC configuration operations — including perspective creation, objective creation, KPI definition, threshold setting, framework mode switching, and NDP III mapping — shall be restricted to users holding the `strategy.admin` role; all such operations shall be enforced server-side and shall not rely on UI visibility controls alone.

**NFR-BSC-011:** The executive scorecard dashboard and all BSC read endpoints shall require a valid authenticated session token; unauthenticated requests shall return HTTP 401 within ≤ 200 ms.

**NFR-BSC-012:** All scorecard data served by the BSC API shall be transmitted over TLS 1.2 or higher; unencrypted HTTP requests to any BSC endpoint shall be rejected with HTTP 301 redirect to HTTPS.

**NFR-BSC-013:** Tenant data isolation shall be enforced at the database query layer for all BSC tables; every query against `strategic_objectives`, `kpis`, `kpi_actuals`, `initiatives`, `okr_objectives`, `okr_key_results`, `logframe_entries`, and `workplans` shall include a `tenant_id` predicate; the absence of a `tenant_id` predicate in any BSC query shall be treated as a critical security defect and shall block release.

## 8.6 Auditability

**NFR-BSC-014:** All audit log entries for the BSC module shall be retained for a minimum of 7 years; records older than 7 years may be archived to cold storage but must remain retrievable within 72 hours of a retrieval request.

**NFR-BSC-015:** The system shall expose a **BSC Audit Log** screen, accessible to users with the `strategy.admin` role, displaying all write events on BSC entities, filterable by entity type, user, action, and date range, and exportable to Excel.
