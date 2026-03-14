---
name: business-case
description: Generate a business case document with problem analysis, cost-benefit analysis, ROI projection, risk assessment, and go/no-go criteria per IEEE 1058.
---

# 02-Business-Case Skill

## Overview

This is the third and final skill in Phase 01 (Strategic Vision). It consumes the Vision Statement and PRD produced by sibling skills to build a financial and strategic justification for the project. The Business Case provides decision-makers with quantitative data -- cost-benefit analysis, ROI projections, risk assessment, and measurable go/no-go criteria -- so they can make an informed investment decision before the project advances to Phase 02.

## When to Use

Run this skill after `01-prd-generation` has produced a PRD. It can also be executed standalone with only `vision.md` and `stakeholders.md` if the PRD is not yet available; in that mode the financial analysis will carry more "[COST-TBD]" flags, but the document structure remains valid.

## Quick Reference

| Attribute   | Value                                                                                 |
|-------------|---------------------------------------------------------------------------------------|
| **Inputs**  | `../project_context/vision.md`, `../project_context/stakeholders.md`, optionally `../output/PRD.md`, `../output/Vision_Statement.md` |
| **Output**  | `../output/Business_Case.md`                                                          |
| **Tone**    | Executive, quantitative, decision-focused                                             |

## Input Files

| File                | Location                           | Required     | Purpose                                      |
|---------------------|------------------------------------|--------------|----------------------------------------------|
| `vision.md`         | `../project_context/vision.md`     | **Required** | Primary source for problem domain and goals   |
| `stakeholders.md`   | `../project_context/stakeholders.md` | **Required** | Identifies decision-makers and beneficiaries |
| `PRD.md`            | `../output/PRD.md`                 | Recommended  | Enriches solution description and timeline    |
| `Vision_Statement.md` | `../output/Vision_Statement.md`  | Optional     | Provides strategic alignment language         |

## Output Files

| File                | Location                       | Description                                    |
|---------------------|--------------------------------|------------------------------------------------|
| `Business_Case.md`  | `../output/Business_Case.md`   | Complete business case with financial analysis |

## Core Instructions

1. **Read Context Files.** Read `vision.md` and `stakeholders.md`. Optionally read `PRD.md` and `Vision_Statement.md`. Log all file paths accessed. Halt execution if `vision.md` is missing.

2. **Generate Executive Summary.** Write one paragraph summarizing the business opportunity, the magnitude of investment required, and the expected return. Use active voice and executive tone.

3. **Generate Problem Statement.** Document the current state, pain points, and quantified impact of inaction. Extract data from `vision.md`. Where quantification data is unavailable, flag with `[IMPACT-TBD: Requires stakeholder input]`.

4. **Generate Proposed Solution.** Describe the high-level approach and list 3-5 key capabilities. Align each capability with a business goal from the vision. If `PRD.md` is available, summarize from it; otherwise derive from `vision.md`.

5. **Generate Cost-Benefit Analysis.** Produce three subsections -- Development Costs, Operational Costs, and Revenue/Savings Projections. Use LaTeX for Net Present Value:

   $$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$

   Flag every unknown cost with `[COST-TBD]` and state assumptions explicitly.

6. **Generate ROI Projection.** Calculate return on investment:

   $$ROI = \frac{Net\ Benefits - Total\ Costs}{Total\ Costs} \times 100\%$$

   Include payback period:

   $$Payback = \frac{Total\ Investment}{Annual\ Net\ Benefit}$$

   State all assumptions.

7. **Generate Risk Assessment.** Construct a 3x3 probability-impact matrix (Low / Medium / High). List the top 5 risks, each with: Description, Probability, Impact, Mitigation Strategy, and Risk Owner. Do not fabricate probabilities; use qualitative assessment when data is unavailable.

8. **Generate Timeline and Milestones.** Align with the PRD release strategy if available. Include decision gates and review points.

9. **Generate Go/No-Go Criteria.** Define 3-5 measurable decision gates with specific thresholds (e.g., "Proceed if MVP demonstrates 80% feature completion within 110% of budget").

## Output Format

The generated `Business_Case.md` shall follow this template:

```markdown
# Business Case: [Project Name]

## 1. Executive Summary
[One paragraph: opportunity, investment, expected return]

## 2. Problem Statement
### 2.1 Current State
### 2.2 Pain Points
### 2.3 Cost of Inaction
<!-- Use [IMPACT-TBD] where data is unavailable -->

## 3. Proposed Solution
### 3.1 High-Level Approach
### 3.2 Key Capabilities
| # | Capability | Business Goal Alignment |
|---|------------|------------------------|

## 4. Cost-Benefit Analysis
### 4.1 Development Costs
### 4.2 Operational Costs
### 4.3 Revenue / Savings Projections
$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t}$$
<!-- Flag unknowns with [COST-TBD] -->

## 5. ROI Projection
$$ROI = \frac{Net\ Benefits - Total\ Costs}{Total\ Costs} \times 100\%$$
$$Payback = \frac{Total\ Investment}{Annual\ Net\ Benefit}$$
### 5.1 Assumptions

## 6. Risk Assessment
### 6.1 Probability-Impact Matrix
|              | Low Impact | Medium Impact | High Impact |
|--------------|-----------|---------------|-------------|
| High Prob.   |           |               |             |
| Medium Prob. |           |               |             |
| Low Prob.    |           |               |             |

### 6.2 Top Risks
| # | Risk | Probability | Impact | Mitigation | Owner |
|---|------|-------------|--------|------------|-------|

## 7. Timeline and Milestones
| Milestone | Target Date | Decision Gate |
|-----------|-------------|---------------|

## 8. Go/No-Go Criteria
| # | Criterion | Threshold | Measurement Method |
|---|-----------|-----------|-------------------|

## 9. Approval
| Role | Name | Decision | Date |
|------|------|----------|------|
```

## Final Step: Write `manifest.md`

After generating all section files, create (or overwrite) `manifest.md` in this document's directory listing the section files in the correct assembly order:

```markdown
# Document Manifest — Business Case
# Generated by business-case. Edit to reorder or exclude sections before building.
01-executive-summary.md
02-problem-analysis.md
03-proposed-solution.md
04-cost-benefit.md
05-risks.md
```

This ensures `scripts/build-doc.sh` assembles sections in the intended order rather than alphabetical fallback.

## Common Pitfalls

- **Fabricating financial data.** Every figure must trace to a context file or carry a `[COST-TBD]` flag.
- **Missing risk mitigation.** Each identified risk must have a corresponding mitigation strategy and owner.
- **Vague go/no-go criteria.** Decision gates must include specific, measurable thresholds.
- **Ignoring cost of inaction.** Failing to quantify the consequences of not proceeding weakens the business justification.

## Verification Checklist

- [ ] `Business_Case.md` exists in `../output/`.
- [ ] All financial figures are flagged with a data source or `[COST-TBD]`.
- [ ] ROI and NPV formulas use LaTeX and are mathematically correct.
- [ ] Risk matrix covers at least 5 risks, each with a mitigation strategy.
- [ ] Go/no-go criteria are measurable with specific thresholds.
- [ ] Document traces to IEEE 1058-1998.

## Integration

| Direction   | Skill                         | Relationship                                    |
|-------------|-------------------------------|-------------------------------------------------|
| Upstream    | `01-prd-generation`           | Provides PRD with scope, features, and timeline |
| Upstream    | `03-vision-statement`         | Provides strategic alignment language            |
| Downstream  | Stakeholder review (external) | Business Case informs go/no-go decision          |

## Standards

- **IEEE 1058-1998** -- IEEE Standard for Software Project Management Plans
- **IEEE 29148-2018** -- Systems and software engineering -- Life cycle processes -- Requirements engineering

## Resources

- `logic.prompt` -- Executable prompt for this skill
- `README.md` -- Quick-start guide for this skill
