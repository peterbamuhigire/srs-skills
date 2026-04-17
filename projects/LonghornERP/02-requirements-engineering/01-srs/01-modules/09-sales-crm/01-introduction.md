# Introduction to the Sales and CRM Module SRS

## 1.1 Purpose

This Software Requirements Specification (SRS) defines all functional and non-functional requirements for the Sales and CRM module of Longhorn ERP. It covers the customer relationship management capabilities that extend the core Sales module (`FR-SALES-*`) with pipeline management, opportunity tracking, forecasting, and territory management. All requirements are prospective and use the prescriptive form "The system shall...".

## 1.2 Scope

The Sales and CRM module covers lead capture, opportunity management, activity logging, contact management, sales forecasting, territory assignment, lost deal analysis, customer satisfaction tracking, and a mobile CRM interface for field representatives. It integrates with the core Sales module to link CRM opportunities to quotations and sales orders.

The module does not cover post-sale customer support or helpdesk ticketing.

## 1.3 Business Goals

| ID | Goal |
|---|---|
| BG-001 | Revenue visibility: pipeline forecasting reduces missed targets by surfacing at-risk deals before month-end. |
| BG-002 | Field productivity: mobile CRM allows reps to log activities, access customer data, and submit quotations without returning to the office. |
| BG-003 | Win-rate improvement: systematic lost deal analysis identifies patterns that inform product and pricing decisions. |
| BG-004 | Customer retention: NPS tracking surfaces dissatisfied customers before they churn. |

## 1.4 Definitions and Acronyms

| Term | Definition |
|---|---|
| Lead | An unqualified prospect who has expressed initial interest or been identified as a potential customer. |
| Opportunity | A qualified lead with an identified need, estimated value, and an expected close date. |
| Pipeline | The aggregate of all open opportunities, typically visualised as a Kanban board with sales stages. |
| NPS | Net Promoter Score — a customer loyalty metric: percentage of promoters minus percentage of detractors. |
| Territory | A defined geographic or market segment assigned to one or more sales representatives. |
| Win Rate | The percentage of closed opportunities that result in a sale: $WinRate = (WonOpps \div (WonOpps + LostOpps)) \times 100$. |

## 1.5 Document Overview

| Section | Content |
|---|---|
| 2 | Leads Management |
| 3 | Opportunity Management |
| 4 | Activity Logging |
| 5 | Contact Management |
| 6 | Sales Forecasting |
| 7 | Territory Management |
| 8 | Lost Deal Analysis |
| 9 | Customer Satisfaction |
| 10 | Mobile CRM |
| 11 | Non-Functional Requirements |
| 12 | Traceability Matrix |
