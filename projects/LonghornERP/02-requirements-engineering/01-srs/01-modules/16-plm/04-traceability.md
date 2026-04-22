# Traceability Matrix - Product Lifecycle Management Module

## 4.1 Overview

This matrix maps every functional requirement in this SRS to at least 1 business goal defined in Section 1.6 and records the deterministic test oracle for each requirement. All FRs without a mapping to a business goal are anomalies and shall be treated as `[TRACE-GAP]`.

## 4.2 Business Goal Reference

| ID | Business Goal |
|---|---|
| BG-PLM-001 | Ensure that downstream operations always consume the correct released product definition |
| BG-PLM-002 | Reduce engineering errors and wrong-build incidents through controlled revision and change governance |
| BG-PLM-003 | Accelerate NPI without sacrificing compliance, approval discipline, or auditability |
| BG-PLM-004 | Preserve traceable product history across revisions, documents, and effectivity windows |
| BG-PLM-005 | Enable a digital thread from engineering through procurement, manufacturing, and service operations |

## 4.3 Traceability Matrix

| FR ID | Section | Description Summary | Business Goal(s) | PRD Reference | Test Oracle |
|---|---|---|---|---|---|
| FR-PLM-001 | 2.1 | Engineering item master and controlled revision lifecycle | BG-PLM-001, BG-PLM-002, BG-PLM-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Create engineering item; release revision A; attempt direct edit; verify edit blocked and revision B draft required; query history and verify all revisions returned. |
| FR-PLM-002 | 2.2 | EBOM/MBOM, variant, and effectivity governance | BG-PLM-001, BG-PLM-004, BG-PLM-005 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Create BOM with 2 plants and date-based effectivity; request structure for Plant A and Plant B on same date; verify only valid effective lines are returned per context. |
| FR-PLM-003 | 2.3 | ECR and ECO workflow with dual-approval governance | BG-PLM-002, BG-PLM-003, BG-PLM-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Submit ECR; approve by engineering approver only; verify ECO release blocked; add operations or quality approval; verify ECO can proceed and audit events exist for each state change. |
| FR-PLM-004 | 2.4 | Technical document and compliance control | BG-PLM-002, BG-PLM-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Configure drawing and certificate as mandatory for release; release item without certificate; verify release blocked with explicit reason; upload certificate and verify release succeeds. |
| FR-PLM-005 | 2.5 | NPI stage-gate governance | BG-PLM-003, BG-PLM-004 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Create NPI record; attempt transition to released with incomplete checklist; verify blocked; complete checklist and release approvals; verify release allowed. |
| FR-PLM-006 | 2.6 | Controlled publication to downstream modules | BG-PLM-001, BG-PLM-005 | Industrial Lifecycle, Manufacturing Execution, and Transportation Depth (`11-industrial-lifecycle-and-logistics.md`) | Release revision with downstream publication enabled; force Manufacturing publication failure; verify engineering release remains released-but-not-published and retry state is recorded. |
