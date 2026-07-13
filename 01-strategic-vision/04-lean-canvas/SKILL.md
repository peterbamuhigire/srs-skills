---
name: 04-lean-canvas
description: Use when an MVP, startup, SaaS, AI, website or mobile initiative still has material customer, problem, channel or value assumptions to test through a Lean Canvas, Impact Map and Hypothesis Board; use PRD generation once evidence supports stable requirements.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Lean Canvas Skill
<!-- dual-compat-start -->
## Use When

- Customer, problem, value, channel or solution assumptions need explicit tests before full requirements investment.

## Do Not Use When

- Do not use as a substitute for an approved PRD, business case or detailed design after uncertainty has been resolved.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Discovery observations and stakeholder goals | Project context, interviews and research | Required | Mark unsupported canvas blocks as hypotheses and schedule evidence collection. |
| Decision horizon and validation budget | Sponsor or product owner | Required | Stop if no owner can accept, reject or fund a test. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the Lean Canvas, Impact Map and Hypothesis Board through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the Lean Canvas, Impact Map and Hypothesis Board to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Lean Canvas, Impact Map and Hypothesis Board | Product owner, discovery team and PRD author | Every material assumption has evidence status, test, owner, threshold and a consequence for requirements. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified Lean Canvas, Impact Map and Hypothesis Board draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Assumption is cheap and reversible | Run a bounded test | Learning precedes specification |
| Assumption is high-risk or irreversible | Escalate evidence and approval before commitment | A weak test authorises costly scope |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Filling a canvas from imagination. Fix: label evidence and confidence for every block.
- Treating features as outcomes. Fix: connect actor behaviour to a measurable goal in the Impact Map.
- Writing hypotheses with no rejection threshold. Fix: define a numeric or observable decision rule.
- Keeping disproved assumptions in the PRD. Fix: update the hypothesis board and downstream scope.
- Testing several variables at once. Fix: isolate the riskiest assumption and one learning question.

## References

- [Lean Canvas guide](references/lean-canvas-guide.md)
- [Hypothesis-driven requirements](references/hypothesis-driven-requirements.md)
- [Impact-map traceability](references/impact-map-traceability-matrix.md)
<!-- dual-compat-end -->





## Overview

This is an optional skill in Phase 01 (Strategic Vision). It provides a lightweight alternative to the full PRD for MVP, startup, or exploratory projects where requirements are highly uncertain. The skill produces three artifacts: a Lean Canvas (9 blocks), an Impact Map (4-level Mermaid mindmap), and a Hypothesis Board for assumption-driven development. A decision gate determines whether this skill is appropriate for the current project.

## When to Use

Run this skill instead of (or before) `01-prd-generation` when the project meets the decision gate threshold. It is designed for first-version products, small teams, tight timelines, and constrained budgets where a full PRD would introduce unnecessary overhead.

## Decision Gate

Score the project against these criteria. Each criterion adds the indicated points:

| Criterion | Points | Condition |
|-----------|--------|-----------|
| MVP or first version | +3 | The product has no existing production release |
| Highly uncertain/evolving requirements | +3 | Requirements are expected to change significantly |
| Startup or small team (<10 people) | +2 | The delivery team has fewer than 10 members |
| Time-to-market <3 months | +2 | Target launch is within 3 months |
| Budget <$100K | +2 | Total project budget is under $100,000 |

**Decision:**
- Score >= 5: Use Lean Canvas. Proceed with this skill.
- Score < 5: Consider full PRD instead. Redirect to `01-prd-generation`.

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/_context/vision.md`, `projects/<ProjectName>/_context/features.md`, `projects/<ProjectName>/_context/stakeholders.md` (optional) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Lean_Canvas.md` |
| **Tone** | Strategic, concise, hypothesis-driven; no marketing language |
| **Standards** | IEEE 29148-2018, Ash Maurya Lean Canvas, Gojko Adzic Impact Mapping |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| `vision.md` | `projects/<ProjectName>/_context/vision.md` | **Required** | Problem domain, target users, business goals, constraints |
| `features.md` | `projects/<ProjectName>/_context/features.md` | Recommended | Feature list for Solution and Deliverables blocks |
| `stakeholders.md` | `projects/<ProjectName>/_context/stakeholders.md` | Optional | Stakeholder roles for actor identification in Impact Map |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| `Lean_Canvas.md` | `projects/<ProjectName>/<phase>/<document>/Lean_Canvas.md` | Complete Lean Canvas, Impact Map, and Hypothesis Board |

## Core Instructions

Follow these eight steps in order. Do not skip or reorder.

### Step 1: Read Context Files

Read `vision.md` and `features.md` from `projects/<ProjectName>/_context/`. Optionally read `stakeholders.md`. Log the absolute path of each file read. Halt execution if `vision.md` is missing.

### Step 2: Execute Decision Gate

Score the project against the five decision gate criteria. Present the scoring table with justification for each score. Calculate the total.

- If total >= 5, proceed with this skill.
- If total < 5, recommend `01-prd-generation` instead and halt execution. Log the recommendation with the score breakdown.

### Step 3: Generate Lean Canvas

Produce the nine blocks of the Lean Canvas in the following order (problem-first, not solution-first):

#### Block 1: Problem

- List the top 3 problems the target users face. Extract from `vision.md` pain points.
- For each problem, identify existing alternatives (how users solve the problem today).
- Do not describe solutions in this block. Flag solution-bias language with `[SOLUTION-BIAS: Reframe as problem statement]`.

#### Block 2: Customer Segments

- Identify the early adopters (the first users who will try the product).
- Define the broader target market.
- For each segment, note: segment name, size estimate (if available or `[SIZE-TBD]`), and key characteristic.

#### Block 3: Unique Value Proposition

- Write a single, clear, compelling message that states why the product is different and worth attention.
- Include a high-level concept using the "X for Y" pattern (e.g., "Slack for healthcare teams").
- The UVP shall be specific and measurable, not subjective.

#### Block 4: Solution

- List the top 3 features that address the top 3 problems from Block 1.
- Each feature shall map directly to a problem. Present as a table:

| Problem | Solution Feature | Source |
|---------|-----------------|--------|
| [Problem 1] | [Feature 1] | `features.md` line [N] |

#### Block 5: Channels

- Identify the path to reaching customers: direct (web, mobile app), indirect (referral, partnership), or paid (advertising).
- List 2-4 channels with rationale for each.

#### Block 6: Revenue Streams

- Define the revenue model (subscription, transaction fee, freemium, licensing, etc.).
- State pricing assumptions. Flag unknown pricing with `[PRICE-TBD]`.
- Estimate customer lifetime value if data is available, or flag with `[LTV-TBD]`.

#### Block 7: Cost Structure

- List fixed costs (salaries, infrastructure, licenses) and variable costs (per-transaction, scaling).
- Estimate break-even point if data supports it, or flag with `[BREAKEVEN-TBD]`.

$$BreakEven = \frac{FixedCosts}{PricePerUnit - VariableCostPerUnit}$$

#### Block 8: Key Metrics

- Define metrics using the AARRR framework (Pirate Metrics):

| Stage | Metric | Measurement | Target |
|-------|--------|-------------|--------|
| **Acquisition** | [How users find the product] | [Measurement method] | [Target or TBD] |
| **Activation** | [First positive experience] | [Measurement method] | [Target or TBD] |
| **Retention** | [Users returning] | [Measurement method] | [Target or TBD] |
| **Revenue** | [Users paying] | [Measurement method] | [Target or TBD] |
| **Referral** | [Users referring others] | [Measurement method] | [Target or TBD] |

- Do not use vanity metrics (page views, downloads) without pairing them with actionable metrics. Flag vanity metrics with `[VANITY-METRIC: Pair with actionable metric]`.

#### Block 9: Unfair Advantage

- Identify what cannot be easily copied or bought: proprietary data, network effects, domain expertise, regulatory approval, community, existing customer base.
- If no clear unfair advantage exists, state "None identified" and flag with `[UA-TBD: Revisit after market validation]`.

### Step 4: Generate Impact Map

Produce a four-level Impact Map as a Mermaid mindmap:

```mermaid
mindmap
  root((Goal: [Measurable Business Objective]))
    Actor 1
      Impact 1a
        Deliverable 1a-i
        Deliverable 1a-ii
      Impact 1b
        Deliverable 1b-i
    Actor 2
      Impact 2a
        Deliverable 2a-i
```

Construction rules:
- **Goal**: State one measurable business objective using SMART criteria (e.g., "Acquire 1,000 paying users within 6 months of launch").
- **Actors**: Identify who can help or hinder reaching the goal. Include users, stakeholders, and competitors.
- **Impacts**: Define how each actor's behavior should change to support the goal.
- **Deliverables**: List the smallest product capability that can create each impact. Prioritize by effort-to-impact ratio.

### Step 5: Generate Hypothesis Board

For each key assumption underlying the Lean Canvas, produce a hypothesis statement:

```markdown
| ID | Hypothesis | Type | Risk | Experiment | Validation Criteria |
|----|-----------|------|------|------------|-------------------|
| H-001 | We believe [capability] will result in [outcome]. | Desirability / Feasibility / Viability | High / Medium / Low | [Experiment type] | We will know we are right when [measurable signal]. |
```

Prioritization rules:
1. Order hypotheses by risk level (highest risk first).
2. Classify each hypothesis by type:
   - **Desirability**: Will users want this?
   - **Feasibility**: Can the team build this?
   - **Viability**: Will this sustain the business?
3. For each hypothesis, suggest an experiment type: concierge MVP, Wizard of Oz, landing page test, A/B test, user interview, or prototype test.
4. Define a pivot/persevere threshold for each hypothesis.
5. Use `references/discovery-interview-and-hypothesis-validation.md` to avoid predictive interview questions and to define evidence thresholds before experiments run.

### Step 6: Validate Internal Consistency

Perform these validation checks:

1. **Problem-Solution Fit**: Every Problem (Block 1) shall have a corresponding Solution (Block 4). Flag gaps with `[FIT-FAIL: Problem [N] has no solution]`.
2. **Metric-Goal Alignment**: Key Metrics (Block 8) shall connect to the Impact Map goal. Flag disconnected metrics.
3. **Hypothesis Coverage**: Every Lean Canvas block shall have at least one hypothesis on the Hypothesis Board.
4. **Revenue-Cost Coherence**: Revenue Streams (Block 6) shall plausibly exceed Cost Structure (Block 7) within a stated timeframe, or flag with `[VIABILITY-RISK: Revenue does not cover costs within [timeframe]]`.

### Step 7: Identify Iteration Triggers

Define conditions that trigger a canvas revision:

| Trigger | Action | Owner |
|---------|--------|-------|
| Hypothesis invalidated | Update affected canvas block; re-score decision gate | Product Owner |
| Customer segment pivot | Rebuild Blocks 2, 3, 5 | Product Owner |
| Revenue model change | Rebuild Blocks 6, 7, 8 | Business Analyst |
| New competitor enters market | Reassess Block 9 (Unfair Advantage) | Product Owner |

### Step 8: Write Output

Assemble the complete Lean Canvas document and write it to `projects/<ProjectName>/<phase>/<document>/Lean_Canvas.md`.

## Output Format

The generated `Lean_Canvas.md` shall contain:

```markdown
# Lean Canvas: [Project Name]

- **Date:** [YYYY-MM-DD]
- **Version:** [X.Y]
- **Standard:** IEEE 29148-2018, Ash Maurya Lean Canvas

## 1. Decision Gate
[Scoring table and decision]

## 2. Lean Canvas
### 2.1 Problem
### 2.2 Customer Segments
### 2.3 Unique Value Proposition
### 2.4 Solution
### 2.5 Channels
### 2.6 Revenue Streams
### 2.7 Cost Structure
### 2.8 Key Metrics
### 2.9 Unfair Advantage

## 3. Impact Map
[Mermaid mindmap]

## 4. Hypothesis Board
[Hypothesis table]

## 5. Validation Summary
[Results of consistency checks]

## 6. Iteration Triggers
[Trigger table]

## 7. Open Issues
[Consolidated list of TBD items]
```

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Solution bias in Problem block | Describe the pain, not the fix; flag violations with `[SOLUTION-BIAS]` |
| Vanity metrics in Key Metrics | Pair every vanity metric with an actionable metric |
| Skipping decision gate | Always score first; a project scoring <5 belongs in full PRD |
| Unfounded revenue projections | Flag all assumptions; use `[PRICE-TBD]` and `[LTV-TBD]` |
| Too many hypotheses | Focus on the 5-7 riskiest assumptions; defer lower-risk ones |
| Impact Map without measurable goal | Goal must include a number and a timeframe |

## Verification Checklist

- [ ] `Lean_Canvas.md` exists in `projects/<ProjectName>/<phase>/<document>/`
- [ ] Decision gate scoring is documented with justification
- [ ] All nine Lean Canvas blocks are populated
- [ ] Problem block contains no solution-bias language
- [ ] Key Metrics use AARRR framework with no standalone vanity metrics
- [ ] Impact Map has a SMART goal at the root
- [ ] Hypothesis Board prioritizes by risk level (highest first)
- [ ] Every TBD flag uses the standard format: `[TYPE-TBD: context]`
- [ ] Validation summary confirms Problem-Solution Fit

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | `00-meta-initialization` | Requires `methodology.md` in `projects/<ProjectName>/_context/` |
| Alternative | `01-prd-generation` | Use PRD when decision gate score < 5 |
| Downstream | `02-business-case` | Lean Canvas informs financial justification |
| Downstream | `02-requirements-engineering` | Hypotheses and solutions feed requirements |

## Standards

- **IEEE 29148-2018** -- Systems and software engineering: stakeholder and vision documentation
- **Ash Maurya, "Running Lean"** -- Lean Canvas methodology and iteration protocol
- **Gojko Adzic, "Impact Mapping"** -- Goal-actor-impact-deliverable framework
- **BA Guide for Lean Enterprises** -- Business Analysis methodology for lean contexts

## Resources

- `references/lean-canvas-guide.md` -- Block-by-block filling guide with examples and common mistakes
- `references/impact-mapping-guide.md` -- Impact Map construction and Mermaid syntax
- `references/hypothesis-driven-requirements.md` -- Hypothesis templates and experiment design
- `references/discovery-interview-and-hypothesis-validation.md` -- customer interview patterns, assumption ledger, and validation thresholds derived from local HTML extractions
- `references/impact-map-traceability-matrix.md` -- goal-to-actor-to-impact-to-requirement trace matrix and milestone rules
- `README.md` -- Quick-start guide with decision gate explanation

## Lean Canvas ↔ Business Model Canvas mapping (added 2026-05-04 from Levy)

Canonical reference: `docs/ux-foundations.md` Section 2 (Business Model Canvas — 9 building blocks).

This is an **additive mapping** — it does not replace the existing Lean Canvas methodology in this skill. Lean Canvas (Maurya) and Osterwalder's BMC are complementary tools; both have their place.

### Block-by-block mapping

| Lean Canvas | Business Model Canvas | UX-strategy intersection |
|---|---|---|
| Problem | (covered indirectly by Customer Segments + Value Propositions) | Where personas' pain points live |
| Customer Segments | **Customer Segments** | **Bolded — UX strategy primary intersection** |
| Unique Value Proposition | **Value Propositions** | **Bolded — UX strategy primary intersection** |
| Solution | (BMC has no direct equivalent — implicit in Value Propositions + Key Activities) | Where UX-design tenet 4 (Killer UX Design) lives |
| Channels | Channels | Where omni-channel UX questions live |
| Revenue Streams | Revenue Streams | — |
| Cost Structure | Cost Structure | — |
| Key Metrics | (BMC has no direct equivalent) | Where Levy's Funnel Matrix metrics fit |
| Unfair Advantage | (covered in Key Resources + Key Partnerships) | Where Value Innovation differentiation lives |
| (no equivalent) | Customer Relationships | How acquisition + retention happen |
| (no equivalent) | Key Resources | Strategic assets — content, capital, patents |
| (no equivalent) | Key Activities | What unique things the business does |
| (no equivalent) | Key Partnerships | Suppliers and partners |

### When to use which

- **Lean Canvas:** early-stage startup, validating problem-solution fit
- **Business Model Canvas:** established product, articulating full operating model for strategic alignment
- **Both:** premium engagements where the team wants both fast-validation framing AND complete strategic articulation

### UX-strategy implication (per Levy)

UX strategy intersects most strongly with Customer Segments + Value Propositions on the BMC — exactly the same blocks where Lean Canvas places Customer Segments + Unique Value Proposition. Whichever canvas you use, those two blocks are where validated user research must produce evidence, not hypothesis.
