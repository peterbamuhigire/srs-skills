# Structured Interview Protocol

## Purpose

This reference provides a complete protocol for conducting structured interviews as a requirements elicitation technique. It covers preparation, question design, execution, and documentation to ensure consistent, high-quality findings with full source attribution.

## Reference Standard

- IEEE 29148-2018 Section 6.3: Requirements elicitation
- Wiegers Practice 4: Interview facilitation

## When to Use Interviews

| Condition | Suitability |
|-----------|-------------|
| Stakeholder availability is high | Excellent |
| Domain complexity is high and needs expert exploration | Excellent |
| Requirements are greenfield or poorly understood | Excellent |
| Stakeholders are geographically distributed | Good (via video) |
| Large number of stakeholders with similar roles | Poor (use questionnaires) |

## Preparation Checklist

Before the interview:

- [ ] Identify the target stakeholder from the stakeholder register (SH-XXX)
- [ ] Review the stakeholder's Power/Interest quadrant and engagement strategy
- [ ] Review relevant sections of `vision.md` and `features.md` for context
- [ ] Prepare 8-12 questions using the three-tier approach (below)
- [ ] Schedule the interview with a defined duration (30-60 minutes)
- [ ] Confirm recording method (notes, audio, or transcript)
- [ ] Send the interview agenda to the stakeholder 48 hours in advance

## Three-Tier Question Approach

### Tier 1: Context Questions (2-3 questions)

Establish the stakeholder's role, responsibilities, and perspective. These build rapport and set the frame.

| # | Template | Purpose |
|---|----------|---------|
| 1 | "Describe your role and how it relates to [project domain]." | Establish authority and perspective |
| 2 | "What are your primary responsibilities that this system will affect?" | Identify scope of impact |
| 3 | "How do you currently accomplish [task/process]?" | Baseline current state |

### Tier 2: Open-Ended Questions (4-6 questions)

Explore needs, pain points, and workflows. These produce the richest elicitation findings.

| # | Template | Purpose |
|---|----------|---------|
| 4 | "What are the biggest challenges you face with [current process]?" | Identify pain points |
| 5 | "If you could change anything about how [task] works, what would it be?" | Capture desired improvements |
| 6 | "Walk me through a typical [workflow] from start to finish." | Document process steps |
| 7 | "What information do you need to make decisions about [domain area]?" | Identify data requirements |
| 8 | "What happens when [error/exception] occurs?" | Capture edge cases |
| 9 | "Who else should I talk to about [topic]?" | Discover hidden stakeholders |

### Tier 3: Closed Questions (2-3 questions)

Confirm specific requirements, constraints, and priorities. These validate and clarify.

| # | Template | Purpose |
|---|----------|---------|
| 10 | "Is [specific feature] critical for your work? (Yes/No)" | Confirm priority |
| 11 | "How frequently do you perform [task]? (Daily/Weekly/Monthly)" | Quantify usage |
| 12 | "What is the maximum acceptable response time for [operation]? (seconds)" | Define NFR thresholds |

## Interview Execution Protocol

### Opening (5 minutes)

1. Thank the stakeholder for their time
2. State the interview purpose and expected duration
3. Confirm permission to take notes or record
4. Explain how findings will be used (requirements documentation, not attribution by name unless consented)

### Body (20-45 minutes)

1. Follow the three-tier question sequence
2. Use active listening: paraphrase and confirm ("So what you're saying is...")
3. Probe deeper on vague statements ("Can you give me a specific example?")
4. Note exact phrasing for critical statements (mark as verbatim)
5. Track time and prioritize remaining questions if running long

### Closing (5 minutes)

1. Summarize the key findings back to the stakeholder
2. Ask: "Is there anything I did not ask about that you think is important?"
3. Confirm follow-up steps and timeline for review
4. Thank the stakeholder

## Recording Format

For each finding from the interview, record:

```
#### EL-XXX: [Finding Title]

- **Source**: SH-XXX -- [Role]
- **Technique**: Interview
- **Question**: [The question that prompted this finding]
- **Statement**: "[Verbatim or paraphrased response]"
- **Derived Requirement**: The system shall [requirement].
- **Type**: Functional | Non-Functional | Constraint | Assumption
- **Confidence**: Confirmed | Likely | Uncertain
- **Follow-up**: [Any action items or clarifications needed]
```

## Follow-Up Procedures

1. Send interview notes to the stakeholder within 48 hours for review
2. Request confirmation or corrections within 5 business days
3. Incorporate corrections into the elicitation log
4. Schedule follow-up interviews for unresolved items tagged as `Uncertain`
5. Cross-reference findings with other stakeholder interviews for consistency

## Anti-Patterns to Avoid

| Anti-Pattern | Description | Correction |
|--------------|-------------|------------|
| Leading questions | "Don't you think the system should..." | Use neutral phrasing: "How should the system handle..." |
| Solution framing | "Would a dropdown menu work here?" | Ask about the need: "What options do users select from?" |
| Monologue | Interviewer talks more than the stakeholder | Follow the 80/20 rule: stakeholder talks 80% |
| Skipping context | Jumping to detailed questions without rapport | Always start with Tier 1 context questions |
| No follow-up | Accepting vague answers without probing | Always ask for examples and specifics |
