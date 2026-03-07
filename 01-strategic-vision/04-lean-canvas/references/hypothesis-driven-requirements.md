# Hypothesis-Driven Requirements Guide

## Purpose

This reference provides templates and procedures for formulating, testing, and validating product hypotheses. Hypothesis-driven requirements replace traditional upfront specification with a test-and-learn cycle, ensuring the team builds only what is validated by evidence.

## Reference Standards

- Ash Maurya, "Running Lean" -- Systematic hypothesis testing
- Eric Ries, "The Lean Startup" -- Build-Measure-Learn loop
- IEEE 29148-2018 -- Requirements validation and verification
- BA Guide for Lean Enterprises -- Assumption-driven analysis

## Hypothesis Format

### Standard Template

```
We believe [this capability]
will result in [this outcome]
for [this actor/segment].
We will know we are right when [measurable signal within timeframe].
```

### Extended Template (with Pivot Criteria)

```
We believe [this capability]
will result in [this outcome]
for [this actor/segment].
We will know we are right when [measurable signal within timeframe].
We will pivot if [failure signal] after [maximum investment].
```

### Examples

| Quality | Hypothesis |
|---------|-----------|
| Good | "We believe a one-click template library will result in 40% faster project setup for freelance designers. We will know we are right when 60% of new users create their first project using a template within 7 days of signup." |
| Good | "We believe competitive pricing ($9/month vs competitor's $29/month) will result in 200 conversions from competitor users within 90 days. We will pivot if fewer than 50 conversions occur after a 60-day landing page test." |
| Bad | "We believe users will like the new dashboard." (No measurable signal, no timeframe, no actor) |
| Bad | "We believe our product is better than competitors." (Subjective, not testable) |

## Assumption Types

### Desirability Assumptions

**Question:** Will users want this?

| Assumption Area | What to Validate | Risk Indicator |
|----------------|------------------|----------------|
| Problem exists | Users experience the stated pain point | Users cannot articulate the problem |
| Problem is severe | Users actively seek solutions | Users have adapted and no longer feel pain |
| Target segment is reachable | The team can access early adopters | No direct channel to the segment |
| Users will switch | Users will abandon current alternatives | Switching costs are high |

### Feasibility Assumptions

**Question:** Can the team build this?

| Assumption Area | What to Validate | Risk Indicator |
|----------------|------------------|----------------|
| Technical capability | The team has the skills and tools | Requires unfamiliar technology stack |
| Integration viability | Third-party services are available and reliable | API limitations or vendor lock-in |
| Performance targets | The system shall meet stated SLAs | Untested at scale |
| Timeline realism | The deliverable can ship within the stated timeframe | Dependencies on external teams |

### Viability Assumptions

**Question:** Will this sustain the business?

| Assumption Area | What to Validate | Risk Indicator |
|----------------|------------------|----------------|
| Willingness to pay | Users will pay the stated price | No pricing experiments conducted |
| Unit economics | Revenue per user exceeds cost per user | High customer acquisition cost |
| Market size | The addressable market supports the revenue goal | Niche segment with limited growth |
| Regulatory compliance | The product can operate legally | Unresolved regulatory requirements |

## Assumption Mapping

### Procedure

1. List every assumption embedded in the Lean Canvas (one per canvas block minimum).
2. Classify each assumption as Desirability, Feasibility, or Viability.
3. Rate each assumption's risk: High (unvalidated and critical), Medium (partially validated), Low (validated or non-critical).
4. Plot on the assumption map:

```
                HIGH RISK
                   |
    Desirability --|-- Feasibility
                   |
                   |
    -----------MEDIUM RISK-----------
                   |
                   |
      Viability ---|--- (Validated)
                   |
                LOW RISK
```

5. Address High-Risk assumptions first. Do not invest in building features whose underlying desirability assumptions are unvalidated.

## Experiment Design

### MVP Types

| MVP Type | Description | Best For | Cost | Time |
|----------|-------------|----------|------|------|
| **Concierge** | Manually deliver the service to a small group of users | Validating the problem and solution with real interactions | Low | 1-2 weeks |
| **Wizard of Oz** | Present an automated-looking interface backed by manual processes | Testing user experience before building backend | Medium | 2-4 weeks |
| **Landing Page** | Single page describing the product with a call-to-action (signup, pre-order) | Measuring demand and willingness to pay | Low | 1-3 days |
| **A/B Test** | Two variants tested against a control group | Optimizing a specific metric after initial validation | Medium | 1-2 weeks |
| **Prototype** | Interactive mockup without backend logic | Testing usability and workflow assumptions | Medium | 1-3 weeks |
| **Single Feature** | Ship one feature to a subset of users | Validating a specific capability in production | High | 2-6 weeks |

### Experiment Template

```markdown
#### Experiment: [EXP-NNN]

| Field | Value |
|-------|-------|
| **Hypothesis** | H-[NNN] |
| **MVP Type** | [Concierge / Wizard of Oz / Landing Page / A/B Test / Prototype / Single Feature] |
| **Target Segment** | [Early adopter segment from Lean Canvas Block 2] |
| **Sample Size** | [Number of participants or interactions needed for statistical significance] |
| **Duration** | [Timeframe for the experiment] |
| **Success Criteria** | [Quantified threshold: e.g., "60% of participants complete the task"] |
| **Failure Criteria** | [Quantified threshold: e.g., "Fewer than 20% express interest"] |
| **Data Collection** | [Method: analytics, surveys, interviews, observation] |
| **Owner** | [Person responsible for running and reporting] |
```

## Validation Criteria

### Quantitative Signals

| Signal Type | Example | Threshold Guidance |
|-------------|---------|-------------------|
| Conversion rate | % of visitors who sign up | >5% for landing pages; >20% for targeted campaigns |
| Activation rate | % of signups who complete first task | >40% within first session |
| Retention rate | % of users returning after 7 days | >20% for week-1 retention |
| Willingness to pay | % of users who complete payment | >2% of free users converting |
| Net Promoter Score | Would you recommend? (0-10) | >30 NPS for early-stage products |

### Qualitative Signals

| Signal Type | Collection Method | Positive Indicator |
|-------------|-------------------|-------------------|
| Problem recognition | User interview | User describes the problem unprompted |
| Solution resonance | Prototype test | User completes the task without guidance |
| Emotional response | Observation | User expresses relief or excitement |
| Referral intent | Post-test survey | User offers to refer a colleague |

## Pivot / Persevere Decision Framework

### Decision Matrix

After each experiment, evaluate the results:

| Result | Validation Signal Met? | Action |
|--------|----------------------|--------|
| Strong positive | Yes, exceeds threshold | **Persevere.** Proceed to next hypothesis or build the feature. |
| Weak positive | Yes, meets but does not exceed threshold | **Iterate.** Refine the hypothesis and run a follow-up experiment. |
| Inconclusive | Insufficient data | **Extend.** Increase sample size or duration. |
| Negative | No, below threshold | **Pivot.** Change the approach: new segment, new solution, or new problem. |

### Pivot Types

| Pivot Type | Description | When to Use |
|------------|-------------|-------------|
| **Customer Segment Pivot** | Same product, different target segment | Problem validated but current segment is not reachable or willing to pay |
| **Problem Pivot** | Same segment, different problem | Current problem is not severe enough to drive action |
| **Solution Pivot** | Same problem, different solution | Problem is validated but current solution does not resonate |
| **Channel Pivot** | Same product, different distribution channel | Product is validated but current channel is not cost-effective |
| **Revenue Model Pivot** | Same product, different monetization | Product has users but current pricing model does not sustain the business |

## Hypothesis Board Template

The skill shall produce a hypothesis board in this format:

| ID | Hypothesis | Type | Risk | Experiment | Validation Criteria | Status |
|----|-----------|------|------|------------|---------------------|--------|
| H-001 | We believe [capability] will result in [outcome] for [segment]. | Desirability | High | Landing Page | We will know we are right when [signal]. | Untested |
| H-002 | We believe [pricing] will sustain [revenue target]. | Viability | High | Concierge | We will know we are right when [signal]. | Untested |
| H-003 | We believe [technology] can deliver [performance target]. | Feasibility | Medium | Prototype | We will know we are right when [signal]. | Untested |

### Ordering Rules

1. High-risk hypotheses appear first.
2. Within the same risk level, Desirability hypotheses precede Viability, which precede Feasibility.
3. Maximum of 7 hypotheses on the board at any time. Defer lower-priority assumptions until top hypotheses are resolved.

## Integration with Lean Canvas

| Lean Canvas Block | Typical Hypothesis Type |
|-------------------|------------------------|
| Problem | Desirability: Do users experience this pain? |
| Customer Segments | Desirability: Can the team reach this segment? |
| Unique Value Proposition | Desirability: Does the UVP resonate? |
| Solution | Feasibility: Can the team build the top 3 features? |
| Channels | Viability: Is the channel cost-effective? |
| Revenue Streams | Viability: Will users pay this price? |
| Cost Structure | Viability: Can the team operate within budget? |
| Key Metrics | All types: Are the chosen metrics moving? |
| Unfair Advantage | Viability: Is the advantage defensible? |
