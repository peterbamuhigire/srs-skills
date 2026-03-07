# Low-Fidelity Prototyping for Requirements Discovery

## Purpose

This reference provides a workflow for using low-fidelity prototypes as a requirements elicitation technique. Prototyping makes abstract requirements concrete, enabling stakeholders to react to visual representations and surface requirements that are difficult to articulate verbally.

## Reference Standard

- IEEE 29148-2018 Section 6.3: Elicitation through modeling
- Wiegers Practice 5: Prototyping for requirements discovery

## When to Use Prototyping

| Condition | Suitability |
|-----------|-------------|
| User-facing features with complex workflows | Excellent |
| Stakeholders struggle to articulate requirements verbally | Excellent |
| Requirements maturity is Greenfield or Evolving | Excellent |
| Backend or API-only features with no user interface | Poor |
| Regulatory documentation requiring precise textual requirements | Poor |

## Prototype Fidelity Levels

| Level | Description | Tools | When to Use |
|-------|-------------|-------|-------------|
| **Paper** | Hand-drawn sketches on paper or whiteboard | Pen, paper, sticky notes | Early discovery, JAD workshops |
| **Wireframe** | Digital grayscale layouts without styling | Balsamiq, Figma (lo-fi), Draw.io | Feature scoping, layout validation |
| **Clickable Mockup** | Interactive wireframes with navigation | Figma, InVision, Marvel | Workflow validation, usability feedback |

For elicitation purposes, the skill shall default to **Paper** or **Wireframe** level. Clickable mockups are only warranted when workflow complexity demands interactive exploration.

## Prototyping Workflow

### Phase 1: Identify Prototype Candidates

From `features.md`, identify features that benefit from visual exploration:

| Selection Criteria | Example |
|--------------------|---------|
| Feature involves user data entry | Registration form, order entry |
| Feature involves a multi-step workflow | Checkout process, approval chain |
| Feature involves data visualization | Dashboard, report, map view |
| Feature involves navigation decisions | Menu structure, search/filter |
| Stakeholders have conflicting mental models | "I picture it differently than you do" |

For each candidate, record:
- Feature ID and name from `features.md`
- Reason for prototyping
- Target stakeholders for feedback

### Phase 2: Create Prototype Descriptions

For each prototype, describe the following elements:

```
#### PROTO-XXX: [Feature Name] Prototype

**Feature Reference**: [Feature ID from features.md]
**Fidelity Level**: Paper | Wireframe | Clickable Mockup
**Target Stakeholders**: [SH-XXX, SH-YYY]

**Screen/Element Descriptions**:

1. **[Screen/Element Name]**
   - Layout: [Description of element arrangement]
   - Data Fields: [List of input/output fields]
   - Actions: [Buttons, links, interactions available]
   - Navigation: [Where this screen leads to/from]

2. **[Next Screen/Element]**
   - ...

**Workflow Sequence**:
1. User starts at [Screen A]
2. User enters [data] and selects [action]
3. System displays [Screen B] with [result]
4. ...

**Feedback Questions**:
- "Does this layout match how you expect to interact with [feature]?"
- "Are all the information fields you need visible on this screen?"
- "What is missing from this view?"
- "What would you change about the workflow sequence?"
```

### Phase 3: Stakeholder Feedback Capture

Present the prototype to target stakeholders and record feedback:

```
#### EL-XXX: [Finding from Prototype Review]

- **Source**: SH-XXX -- [Role]
- **Technique**: Prototyping
- **Prototype**: PROTO-XXX -- [Feature Name]
- **Screen/Element**: [Specific screen discussed]
- **Stakeholder Reaction**: Approved | Modified | Rejected
- **Feedback**: "[Verbatim stakeholder feedback]"
- **Derived Requirement**: The system shall [requirement].
- **Type**: Functional | Non-Functional | Constraint
- **Confidence**: Confirmed | Likely | Uncertain
- **Iteration Needed**: Yes | No
```

### Phase 4: Iteration Protocol

If stakeholder feedback indicates significant changes:

1. Update the prototype description based on feedback
2. Mark the iteration number (Iteration 1, 2, 3...)
3. Re-present to the same stakeholders for confirmation
4. Maximum 3 iterations per prototype before escalating to a JAD workshop
5. Log all iterations in the elicitation log for traceability

## Feedback Question Templates

### Layout and Content Questions
- "Is all the information you need visible on this screen?"
- "What additional data would you expect to see here?"
- "What information on this screen is unnecessary for your workflow?"

### Workflow Questions
- "Does this sequence of steps match how you currently work?"
- "Are there steps missing from this workflow?"
- "At which step would you most likely need help or guidance?"

### Priority Questions
- "Which elements on this screen are most important to you?"
- "If we could only deliver three features from this prototype, which three?"
- "What is the first thing you look for on this screen?"

## Anti-Patterns to Avoid

| Anti-Pattern | Description | Correction |
|--------------|-------------|------------|
| Over-engineering | Building high-fidelity prototypes for elicitation | Use paper or wireframe level only |
| Prototype as spec | Treating the prototype as a final design document | Prototypes are disposable discovery tools |
| Leading the witness | "This is where the save button goes, right?" | Ask open-ended: "Where would you expect to save?" |
| Single iteration | Showing once and moving on without incorporating feedback | Plan for 2-3 feedback iterations |
| Missing stakeholders | Showing only to developers, not end users | Target stakeholders from "Keep Informed" quadrant |
