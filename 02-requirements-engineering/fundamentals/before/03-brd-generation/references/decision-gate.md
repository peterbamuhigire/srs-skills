# BRD Decision Gate: Criteria and Scoring Guide

## Purpose

This reference provides the decision criteria and scoring methodology for determining whether a formal Business Requirements Document (BRD) is warranted for a given project. The decision gate prevents unnecessary documentation overhead for projects that do not benefit from a BRD while ensuring that projects requiring formal business documentation produce one.

## Reference Standard

- IEEE 29148-2018 Section 6.4: Business requirements specification applicability
- Business Requirements Gathering Ch.2: When BRDs add value

## Decision Gate Overview

The decision gate evaluates eight criteria, each weighted by its importance to BRD necessity. The weighted score determines whether the BRD skill should proceed, pause for confirmation, or halt.

## Scoring Criteria

| # | Criterion | Weight | Rationale |
|---|-----------|--------|-----------|
| 1 | Multiple stakeholder groups with competing priorities | 3 | High weight: competing priorities are the primary driver for formal business documentation to establish shared understanding |
| 2 | Regulatory or compliance requirements mandate formal business documentation | 3 | High weight: regulatory mandates are non-negotiable and require auditable documentation |
| 3 | Contractual obligation to deliver a BRD | 3 | High weight: contractual requirements are binding and must be fulfilled |
| 4 | Project budget exceeds the organization's "small project" threshold | 2 | Medium weight: larger investments warrant more formal documentation to protect the investment |
| 5 | Project spans multiple departments or business units | 2 | Medium weight: cross-departmental projects need alignment documentation |
| 6 | Project replaces or integrates with existing business processes | 2 | Medium weight: process change projects need as-is/to-be documentation |
| 7 | Project timeline exceeds 6 months | 1 | Low weight: longer timelines benefit from documentation but do not require it |
| 8 | Stakeholder alignment is uncertain or contested | 1 | Low weight: alignment issues are better resolved through the BRD process but can also be addressed through other means |

## Scoring Formula

$$Score = \sum_{i=1}^{8} (Weight_i \times YesFlag_i)$$

Where $YesFlag_i = 1$ if the criterion is met, $0$ otherwise.

**Maximum possible score**: 17 (all criteria met)
**Minimum possible score**: 0 (no criteria met)

## Decision Thresholds

| Score Range | Decision | Action |
|-------------|----------|--------|
| 8-17 | **BRD Recommended** | Proceed with BRD generation. The project characteristics warrant formal business requirements documentation. |
| 4-7 | **BRD Optional** | Present the score and rationale to the user. The BRD may add value but is not essential. Await user confirmation before proceeding. |
| 0-3 | **BRD Not Recommended** | Advise the user to skip BRD generation and proceed directly to SRS (waterfall) or user story generation (agile). Halt unless the user explicitly overrides. |

## Evaluation Worksheet

Present this worksheet to the user during Step 0 of the BRD Generation skill:

```
## BRD Decision Gate Evaluation

Project: [Project Name]
Date: [Current Date]
Evaluator: [User or AI]

| # | Criterion | Yes/No | Weight | Score |
|---|-----------|--------|--------|-------|
| 1 | Multiple stakeholder groups with competing priorities | [ ] | 3 | |
| 2 | Regulatory/compliance mandates formal documentation | [ ] | 3 | |
| 3 | Contractual obligation to deliver a BRD | [ ] | 3 | |
| 4 | Budget exceeds "small project" threshold | [ ] | 2 | |
| 5 | Spans multiple departments/business units | [ ] | 2 | |
| 6 | Replaces/integrates with existing processes | [ ] | 2 | |
| 7 | Timeline exceeds 6 months | [ ] | 1 | |
| 8 | Stakeholder alignment is uncertain/contested | [ ] | 1 | |

**Total Score**: _____ / 17

**Decision**: [ ] Recommended (8+) | [ ] Optional (4-7) | [ ] Not Recommended (0-3)
```

## Auto-Assessment from Context Files

When context files are available, the AI shall attempt to auto-assess criteria:

| Criterion | Auto-Assessment Source | Method |
|-----------|----------------------|--------|
| 1 | `stakeholder_register.md` | Count distinct stakeholder groups in "Manage Closely" quadrant; if > 2, mark Yes |
| 2 | `vision.md` constraints section | Search for regulatory/compliance keywords; if found, mark Yes |
| 3 | `vision.md` | Search for contractual or deliverable keywords; if found, mark Yes |
| 4 | `vision.md` constraints section | Search for budget references; infer if above threshold |
| 5 | `stakeholder_register.md` | Count distinct departments; if > 2, mark Yes |
| 6 | `vision.md` problem statement | Search for replacement/migration/integration keywords |
| 7 | `vision.md` constraints section | Search for timeline references; compare to 6-month threshold |
| 8 | `stakeholder_register.md` | Check for "Resistant" engagement levels or risk tags |

Tag all auto-assessed criteria with `[AUTO-ASSESSED]` and present to the user for confirmation before calculating the final score.

## Override Protocol

If the user overrides the decision gate recommendation:

- **Overriding "Not Recommended" to proceed**: Log the override with rationale. Generate the BRD but include a note in the Document Header: "Note: This BRD was generated at user request. The decision gate score of [X] did not meet the recommended threshold of 8."
- **Overriding "Recommended" to skip**: Log the override with rationale. Suggest the user proceed to the next skill in the pipeline (SRS initialization or user story generation).

## Examples

### Example 1: Enterprise ERP Replacement (Score: 15 -- Recommended)

| # | Criterion | Yes/No | Weight | Score |
|---|-----------|--------|--------|-------|
| 1 | Multiple stakeholder groups | Yes | 3 | 3 |
| 2 | Regulatory compliance (SOX) | Yes | 3 | 3 |
| 3 | Contractual (vendor agreement) | Yes | 3 | 3 |
| 4 | Budget > $500K | Yes | 2 | 2 |
| 5 | Spans Finance, Operations, HR | Yes | 2 | 2 |
| 6 | Replaces legacy ERP | Yes | 2 | 2 |
| 7 | 18-month timeline | No | 1 | 0 |
| 8 | Alignment contested | No | 1 | 0 |
| **Total** | | | | **15** |

**Decision**: BRD Recommended. Proceed with generation.

### Example 2: Internal Tool for One Team (Score: 2 -- Not Recommended)

| # | Criterion | Yes/No | Weight | Score |
|---|-----------|--------|--------|-------|
| 1 | Single team, aligned priorities | No | 3 | 0 |
| 2 | No regulatory requirements | No | 3 | 0 |
| 3 | No contractual obligation | No | 3 | 0 |
| 4 | Small budget | No | 2 | 0 |
| 5 | Single department | No | 2 | 0 |
| 6 | New tool, no replacement | No | 2 | 0 |
| 7 | 3-month timeline | No | 1 | 0 |
| 8 | Team is aligned | Yes | 1 | 1 |
| **Total** | | | | **2** |

**Decision**: BRD Not Recommended. Proceed directly to SRS or user stories.

### Example 3: Mid-Size SaaS Product (Score: 6 -- Optional)

| # | Criterion | Yes/No | Weight | Score |
|---|-----------|--------|--------|-------|
| 1 | Product, Engineering, Sales teams | Yes | 3 | 3 |
| 2 | No specific regulation | No | 3 | 0 |
| 3 | No contractual BRD requirement | No | 3 | 0 |
| 4 | Medium budget | No | 2 | 0 |
| 5 | Product and Engineering | Yes | 2 | 2 |
| 6 | No existing process replacement | No | 2 | 0 |
| 7 | 8-month timeline | Yes | 1 | 1 |
| 8 | General alignment | No | 1 | 0 |
| **Total** | | | | **6** |

**Decision**: BRD Optional. Present to user for confirmation.
