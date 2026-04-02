---
title: Product Commercialisation Skills — Design Document
date: 2026-04-03
status: Approved — implementing
sources: INSPIRED (Cagan), Mastering SPM (Dash), The Product Book (Anon/Villaumbrosia), The Business of Software (Cusumano), IT Project Proposals (Coombs), A Quick Guide to SaaS, Winning at IT (Technology Grant News)
---

# Product Commercialisation Skills — Design Document

## Purpose

Eight new skills extracted from seven product management, business, and proposal-writing books.
Goal: equip the skills repository to produce software that wins in competitive markets — both custom
software for specific clients and mass-market SaaS applications.

## Cluster 1 — Product Intelligence (build first)

These four skills form the thinking foundation. A practitioner uses them before writing a line of code.

| Skill | Folder | Primary Source |
|-------|--------|---------------|
| Product Discovery | `skills/product-discovery/` | INSPIRED (Cagan) |
| Product Strategy & Vision | `skills/product-strategy-vision/` | INSPIRED + Mastering SPM |
| Competitive Analysis for PMs | `skills/competitive-analysis-pm/` | Mastering SPM (Porter's Five Forces) |
| SaaS Business Metrics | `skills/saas-business-metrics/` | SaaS Guide + Mastering SPM |

## Cluster 2 — Commercial Execution (build second)

These four skills apply the thinking to win clients, revenue, and funding.

| Skill | Folder | Primary Source |
|-------|--------|---------------|
| Software Pricing Strategy | `skills/software-pricing-strategy/` | Mastering SPM |
| Software Business Models | `skills/software-business-models/` | Business of Software (Cusumano) |
| IT Proposal Writing | `skills/it-proposal-writing/` | IT Project Proposals (Coombs) |
| Technology Grant Writing | `skills/technology-grant-writing/` | Winning at IT |

## Architecture

- Each skill: one `SKILL.md` (≤ 500 lines) + `references/` subdirectory for deep content.
- Frontmatter: `name` + `description` fields, following existing skill format.
- Cross-references: each skill lists upstream and downstream skills.
- Standards: CLAUDE.md Three-Emphasis Rule, ATX headings, `-` bullets, no vague adjectives.

## Dependency Map

```
product-discovery
    → product-strategy-vision
    → competitive-analysis-pm → software-pricing-strategy
    → saas-business-metrics   → software-pricing-strategy
                                → software-business-models
                                → it-proposal-writing
                                → technology-grant-writing
```
