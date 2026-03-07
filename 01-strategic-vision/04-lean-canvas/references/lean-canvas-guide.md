# Lean Canvas Block-by-Block Filling Guide

## Purpose

This reference provides detailed guidance for populating each of the nine Lean Canvas blocks, including examples, common mistakes, and iteration protocols. The Lean Canvas is a one-page business model adapted from Alexander Osterwalder's Business Model Canvas by Ash Maurya for lean startup contexts.

## Reference Standards

- Ash Maurya, "Running Lean" -- Lean Canvas methodology
- IEEE 29148-2018 -- Stakeholder needs and requirements documentation
- BA Guide for Lean Enterprises -- Business analysis in lean contexts

## Lean Canvas vs Business Model Canvas

| Aspect | Lean Canvas | Business Model Canvas |
|--------|-------------|----------------------|
| **Focus** | Problem-solution fit for startups | Business model for established companies |
| **Replaces** | Key Partners with Problem | Retains Key Partners |
| **Replaces** | Key Activities with Solution | Retains Key Activities |
| **Replaces** | Key Resources with Key Metrics | Retains Key Resources |
| **Replaces** | Customer Relationships with Unfair Advantage | Retains Customer Relationships |
| **Best For** | MVP validation, early-stage products | Mature products, enterprise strategy |

**Rule:** Use Lean Canvas when the primary uncertainty is problem-solution fit. Use Business Model Canvas when the business model is the primary uncertainty.

## Block-by-Block Guide

### Block 1: Problem

**What to capture:** The top 3 problems your target customers face today.

**Filling procedure:**
1. Extract pain points from `vision.md`.
2. Rank by severity (frequency x impact).
3. For each problem, identify the existing alternative (how customers solve it now).

**Template:**

| # | Problem | Existing Alternative |
|---|---------|---------------------|
| 1 | [Most severe problem] | [Current workaround or competitor] |
| 2 | [Second problem] | [Current workaround or competitor] |
| 3 | [Third problem] | [Current workaround or competitor] |

**Common mistake -- Solution Bias:**
- Wrong: "Users need a mobile app to track expenses."
- Correct: "Users lose track of business expenses, resulting in an average of $2,400/year in missed tax deductions."

The Problem block shall describe pain, not prescribe a fix. Flag solution language with `[SOLUTION-BIAS]`.

### Block 2: Customer Segments

**What to capture:** Who has these problems. Distinguish early adopters from the broader market.

**Filling procedure:**
1. Identify the early adopter -- the customer who feels the problem most acutely and will try an imperfect solution.
2. Define the broader target market the product will expand to.
3. If `stakeholders.md` exists, cross-reference customer segments.

**Template:**

| Segment | Type | Size | Key Characteristic |
|---------|------|------|-------------------|
| [Segment A] | Early Adopter | [Estimate or SIZE-TBD] | [Why they feel the pain most] |
| [Segment B] | Target Market | [Estimate or SIZE-TBD] | [Broader demographic] |

**Common mistake:** Defining the segment too broadly ("everyone who uses a computer"). Narrow to a specific, reachable group.

### Block 3: Unique Value Proposition

**What to capture:** A single, clear sentence explaining why the product is different and worth paying attention to.

**Filling procedure:**
1. Combine the #1 problem with the #1 solution.
2. State the outcome, not the mechanism.
3. Add a high-level concept: "X for Y" (e.g., "Uber for dog walking").

**Template:**
- **UVP:** [Single sentence: outcome-focused, specific, no superlatives]
- **High-Level Concept:** [Known product] for [target segment]

**Common mistake:** Using subjective adjectives ("the fastest, most intuitive..."). The UVP shall be concrete and verifiable.

### Block 4: Solution

**What to capture:** The top 3 features that address the top 3 problems.

**Filling procedure:**
1. Map each problem from Block 1 to a feature from `features.md`.
2. State the feature as a capability, not an implementation detail.
3. Keep it to 3 features maximum; this is an MVP.

| Problem | Solution Feature | Source |
|---------|-----------------|--------|
| [Problem 1] | [Feature addressing it] | `features.md` |
| [Problem 2] | [Feature addressing it] | `features.md` |
| [Problem 3] | [Feature addressing it] | `features.md` |

**Common mistake:** Listing 10+ features. The Lean Canvas shall focus on the minimum viable set. Defer non-essential features to the backlog.

### Block 5: Channels

**What to capture:** How the product reaches customers.

**Filling procedure:**
1. List 2-4 channels with rationale.
2. Prioritize by cost-effectiveness and reach to early adopters.

| Channel | Type | Rationale |
|---------|------|-----------|
| [Channel 1] | Direct / Indirect / Paid | [Why this channel reaches early adopters] |
| [Channel 2] | Direct / Indirect / Paid | [Why this channel is cost-effective] |

**Common mistake:** Listing channels without validating that early adopters use them. Test channels as hypotheses.

### Block 6: Revenue Streams

**What to capture:** How the product makes money.

**Filling procedure:**
1. Select a revenue model: subscription, transaction fee, freemium, licensing, advertising, or marketplace commission.
2. State pricing assumptions with source or `[PRICE-TBD]`.
3. Estimate customer lifetime value or flag `[LTV-TBD]`.

**Template:**
- **Model:** [Revenue model type]
- **Price Point:** [Amount per unit/month/transaction or PRICE-TBD]
- **LTV Estimate:** [Calculated value or LTV-TBD]

**Common mistake:** Assuming revenue without a pricing experiment. Every price point is a hypothesis until validated.

### Block 7: Cost Structure

**What to capture:** What it costs to operate the business.

**Filling procedure:**
1. List fixed costs (salaries, hosting, licenses).
2. List variable costs (per-transaction fees, scaling costs).
3. Calculate break-even if data supports it.

$$BreakEven = \frac{FixedCosts}{PricePerUnit - VariableCostPerUnit}$$

**Common mistake:** Underestimating hidden costs (support, compliance, infrastructure scaling). Include a contingency line item.

### Block 8: Key Metrics

**What to capture:** The 1-2 metrics per AARRR stage that indicate product health.

| Stage | Metric | Actionable? |
|-------|--------|-------------|
| Acquisition | [How users find you] | Yes -- directly influences marketing spend |
| Activation | [First value moment] | Yes -- indicates onboarding quality |
| Retention | [Users returning] | Yes -- indicates product-market fit |
| Revenue | [Users paying] | Yes -- indicates business viability |
| Referral | [Users referring] | Yes -- indicates organic growth |

**Common mistake -- Vanity Metrics:**
- Wrong: "Total page views" (not actionable)
- Correct: "Activation rate: % of signups who complete first task within 24 hours" (actionable)

Flag vanity metrics with `[VANITY-METRIC: Pair with actionable metric]`.

### Block 9: Unfair Advantage

**What to capture:** Defensibility -- what cannot be easily copied or bought.

**Valid unfair advantages:**
- Proprietary data or algorithms
- Network effects (product gets better with more users)
- Domain expertise or regulatory approvals
- Existing customer base or community
- Exclusive partnerships or distribution rights

**Common mistake:** Listing "first mover advantage" or "passion." These are not defensible. If no genuine unfair advantage exists, state "None identified" and flag with `[UA-TBD]`.

## Iteration Protocol

### Test Riskiest Assumption First

1. Identify the single riskiest assumption on the canvas (usually in Problem or UVP).
2. Design a minimum experiment to test it (see `hypothesis-driven-requirements.md`).
3. Run the experiment with the smallest investment of time and money.
4. Update the canvas based on results.

### Iteration Triggers

| Signal | Canvas Update |
|--------|--------------|
| Customers do not recognize the problem | Revise Block 1 (Problem) |
| Early adopters not reachable through planned channels | Revise Block 5 (Channels) |
| Willingness to pay is lower than assumed | Revise Block 6 (Revenue Streams) |
| Activation rate below threshold | Revise Block 4 (Solution) |
| No defensible advantage after 3 iterations | Escalate to strategic review |

### Canvas Versioning

Every iteration shall produce a new version of the canvas:
- **v0.1:** Initial hypothesis (pre-validation)
- **v0.x:** Post-experiment updates (one version per significant pivot)
- **v1.0:** Validated canvas (problem-solution fit confirmed)
