# Prototype Validation Reference Guide

**Purpose:** Use prototypes to validate requirements through structured stakeholder walkthroughs, capturing feedback and updating requirements systematically.

**Standards:** IEEE 29148-2018 Section 6.6, Laplante Ch.6, Wiegers Practice 14

---

## 1. Prototype Types

### 1.1 Throwaway Prototype

**Definition:** A quick, disposable prototype built solely to validate requirements. It is discarded after validation; no code is reused.

| Attribute    | Value                                             |
|--------------|---------------------------------------------------|
| Purpose      | Validate requirements before committing to design |
| Fidelity     | Low to medium                                     |
| Lifespan     | Discarded after validation cycle                  |
| Build Effort | Hours to days                                     |
| Tools        | Paper, wireframes, Figma, Balsamiq                |

**When to Use:**
- Requirements are unclear or stakeholders cannot visualize the system
- High-risk features need early validation
- The domain is unfamiliar to the development team

### 1.2 Evolutionary Prototype

**Definition:** A working prototype that evolves into the final product through iterative refinement. Each iteration validates requirements and adds functionality.

| Attribute    | Value                                             |
|--------------|---------------------------------------------------|
| Purpose      | Validate and incrementally build the system       |
| Fidelity     | Medium to high                                    |
| Lifespan     | Evolves into production system                    |
| Build Effort | Days to weeks per iteration                       |
| Tools        | Production technology stack                       |

**When to Use:**
- Requirements are expected to evolve through stakeholder interaction
- The product can be delivered incrementally
- Stakeholders need a working system to provide meaningful feedback

### 1.3 Fidelity Spectrum

| Level      | Description                             | Typical Form                   | Validation Scope           |
|------------|-----------------------------------------|--------------------------------|----------------------------|
| Low        | Static representation of layout         | Paper sketches, wireframes     | Navigation flow, content   |
| Medium     | Interactive but non-functional          | Clickable mockups, HTML shells | User interaction, workflow |
| High       | Functional with real data processing    | Working code with test data    | Business logic, performance|

---

## 2. Stakeholder Walkthrough Protocol

### 2.1 Preparation

**Facilitator responsibilities:**

1. **Define Scope:** Select which features and requirements the prototype covers. Document the mapping:

| Prototype Screen/Component | Requirements Validated       |
|----------------------------|------------------------------|
| Login screen               | FR-001, FR-002, NFR-010      |
| Dashboard                  | FR-010, FR-011, FR-012       |
| Order entry form           | FR-020 through FR-028        |

2. **Prepare Scenarios:** Write scenario scripts that guide stakeholders through the prototype in a structured way. Each scenario SHALL:
   - Start from a defined precondition
   - Walk through a specific user task
   - End at a measurable outcome
   - Map to one or more requirements

**Scenario Template:**

```
Scenario ID: SC-001
Title: Place a New Order
Precondition: User is logged in as a Sales Representative
Requirements: FR-020, FR-021, FR-022, FR-025

Steps:
1. Navigate to the Order Entry screen
2. Search for customer "Acme Corp"
3. Add Product SKU-100 (qty: 5) to the order
4. Apply discount code "BULK10"
5. Submit the order

Expected Outcome: Order confirmation displayed with total reflecting 10% discount.

Validation Questions:
- Does the workflow match your expectations?
- Are any steps missing?
- Is the information displayed sufficient for your task?
```

3. **Select Participants:** Include stakeholders who represent each user role. Minimum 3 participants; maximum 8 per session.

4. **Schedule Session:** Allow 60-90 minutes. Do not combine more than 5 scenarios per session.

### 2.2 Facilitation

**During the walkthrough:**

1. **Introduction (5 min):** Explain the purpose: validate requirements, not evaluate the design or aesthetics. Emphasize that the prototype is incomplete and feedback is expected.

2. **Scenario Execution (10-15 min per scenario):**
   - The facilitator reads the scenario steps
   - The participant interacts with the prototype (or the facilitator demonstrates)
   - After each scenario, ask the validation questions
   - Record ALL feedback, including comments, questions, and concerns

3. **Open Discussion (15 min):** After all scenarios, allow free-form exploration and discussion. Capture additional feedback.

4. **Wrap-Up (5 min):** Summarize findings, explain next steps, thank participants.

### 2.3 Rules for the Facilitator

- Do NOT defend the design or explain why something works a certain way
- Do NOT lead the participant toward a desired answer
- Record exact quotes when possible; paraphrase only if necessary
- If a participant identifies a gap, ask: "What would you expect to happen here?"
- If a participant is confused, record the confusion as a finding (ambiguity defect)

---

## 3. Feedback Capture Template

### 3.1 Individual Feedback Record

| Field              | Content                                              |
|--------------------|------------------------------------------------------|
| Feedback ID        | Unique identifier (e.g., PV-001)                     |
| Session ID         | Which walkthrough session                            |
| Participant Role   | The stakeholder's role (e.g., Sales Manager)         |
| Scenario ID        | Which scenario triggered the feedback                |
| Requirement ID(s)  | Requirements affected by the feedback                |
| Feedback Type      | Confirmation, Gap, Change, Clarification, New        |
| Description        | Verbatim or paraphrased feedback                     |
| Impact             | Affects existing requirement / Requires new requirement / Cosmetic |
| Priority           | Critical / Major / Minor                             |

### 3.2 Feedback Type Definitions

| Type           | Definition                                                    | Action Required              |
|----------------|---------------------------------------------------------------|------------------------------|
| Confirmation   | Stakeholder confirms the requirement is correctly represented | No change; log as validation |
| Gap            | Stakeholder identifies missing behavior or information        | Create new requirement       |
| Change         | Stakeholder requests modification to an existing requirement  | Update requirement           |
| Clarification  | Stakeholder asks a question indicating ambiguity              | Refine requirement language  |
| New            | Stakeholder identifies an entirely new capability need        | Create new requirement; assess scope impact |

### 3.3 Aggregated Feedback Summary

After all sessions, aggregate feedback:

| Requirement ID | Confirmations | Gaps | Changes | Clarifications | New | Net Status      |
|----------------|---------------|------|---------|----------------|-----|-----------------|
| FR-020         | 5             | 0    | 1       | 0              | 0   | Validated (minor change) |
| FR-021         | 3             | 2    | 0       | 1              | 0   | Needs refinement|
| FR-025         | 1             | 3    | 2       | 2              | 0   | Major rework    |
| (new)          | -             | -    | -       | -              | 4   | New requirement |

---

## 4. Requirements Update Process

### 4.1 Triage

After feedback aggregation:

1. **Confirmed requirements:** Mark as "Prototype-Validated" in the analysis report
2. **Minor changes:** Update the requirement text and log the change with the feedback ID as justification
3. **Major rework:** Return the requirement to the requirements analysis skill for reclassification and re-analysis
4. **New requirements:** Add to the elicitation log with source "Prototype Walkthrough [Session ID]" and run through the full analysis pipeline

### 4.2 Change Control

Every requirement change resulting from prototype validation SHALL:
- Reference the feedback ID(s) that motivated the change
- Document the before and after requirement text
- Be re-validated against the Wiegers quality attributes
- Update traceability links

### 4.3 Iteration Decision

| Outcome                              | Decision                                          |
|---------------------------------------|---------------------------------------------------|
| All requirements confirmed            | Proceed to baselining                             |
| Minor changes only (< 10% of set)    | Apply changes and proceed                         |
| Major rework needed (10-30% of set)  | Update requirements, build new prototype iteration|
| Fundamental gaps (> 30% of set)      | Return to elicitation; current requirements insufficient |

---

## 5. Prototype Validation Metrics

| Metric                    | Formula                                                   | Target         |
|---------------------------|-----------------------------------------------------------|----------------|
| Confirmation Rate         | $\frac{ConfirmedRequirements}{TotalValidatedRequirements} \times 100$ | > 70%  |
| Gap Discovery Rate        | $\frac{GapsIdentified}{TotalValidatedRequirements} \times 100$ | < 20%    |
| New Requirement Rate      | $\frac{NewRequirements}{TotalValidatedRequirements} \times 100$ | < 10%    |
| Stakeholder Coverage      | $\frac{RolesRepresented}{TotalRoles} \times 100$          | 100%           |

---

## 6. Prototype Validation Checklist

- [ ] Prototype type selected (throwaway or evolutionary) with justification
- [ ] Prototype scope mapped to specific requirements
- [ ] Scenario scripts prepared with preconditions, steps, and expected outcomes
- [ ] Participants selected representing all relevant user roles
- [ ] Walkthrough sessions conducted following the facilitation protocol
- [ ] All feedback captured using the feedback template
- [ ] Feedback aggregated and triaged by type and priority
- [ ] Requirements updated with change control documentation
- [ ] Iteration decision made based on outcome thresholds
- [ ] Validation metrics calculated and reported

---

**Last Updated:** 2026-03-07
