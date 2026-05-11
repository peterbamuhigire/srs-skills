# Experience Map To Requirement Conversion

Use this reference to convert research-backed experience maps into auditable SDLC requirements.

## Source Grounding

This guidance is derived from local HTML extractions:

- `mapping-experiences/toc.ncx`, `index_split_000.html` through `index_split_005.html`: alignment diagrams, frame the mapping effort, identify touchpoints, investigate, illustrate, customer journey maps, experience maps, mental models, ecosystem maps, future-state experiences.
- `service-design-thinking/toc.ncx`, `index_split_000.html`: user-centred, co-creative, sequencing, evidencing, holistic service design; exploration, creation, reflection, implementation.
- `lean-customer-development/toc.ncx`, `index_split_000.html` through `index_split_002.html`: where to start, who to talk to, what to learn, validated hypotheses, ongoing discovery.
- `impact-mapping/toc.ncx`, `index_split_000.html`: measurable goals, actors, impacts, alternatives, milestone planning, earn-or-learn loops.

No book passages are copied. The rules below are original operational conversions for this engine.

## Conversion Model

| Map Evidence | Requirement Type | Conversion Rule | Example Output Pattern |
|---|---|---|---|
| User action fails or stalls | Functional | Specify the system response that removes, shortens, or safeguards the action. | `FR-JNY-###: When [actor] reaches [stage], the system shall [response] so that [outcome metric].` |
| User confusion or wrong expectation | UX/content | Specify label, explanation, feedback, preview, confirmation, or recovery text. | `UX-JNY-###: The interface shall present [message/control] before [decision point].` |
| Touchpoint handoff breaks | Service/support | Specify ownership, notification, queue, escalation, or status visibility. | `SUP-JNY-###: The service desk shall receive [signal] within [time] when [handoff condition].` |
| Repeated workaround | Process/data | Specify captured data, automation, integration, policy change, or exception handling. | `DATA-JNY-###: The system shall record [field/event] at [stage] for [downstream use].` |
| Emotional low caused by uncertainty | Feedback/NFR | Specify progress, latency, status, assurance, or recoverability threshold. | `NFR-JNY-###: Status feedback shall appear within [N] seconds for [operation].` |
| Future-state opportunity | Hypothesis | Define experiment before committing to full implementation. | `HYP-JNY-###: We believe [change] will improve [metric] for [actor] by [threshold].` |

## Required Map Columns

Use these columns before deriving requirements:

| Column | Purpose | Gate |
|---|---|---|
| Stage | Names the journey segment. | Each stage has a start and end event. |
| Actor | Identifies who experiences or performs the stage. | Use stakeholder IDs where available. |
| Goal | States what the actor is trying to accomplish. | Must be actor-centred, not system-centred. |
| Action | Captures observed or reported behaviour. | Mark `Observed`, `Reported`, or `Inferred`. |
| Touchpoint | Names channel, screen, person, device, document, or system. | Must include non-digital touchpoints where relevant. |
| Evidence | Links to interview note, analytics, log, support ticket, field note, or artifact. | No evidence means no requirement, only a hypothesis. |
| Pain or Risk | Describes failure, delay, uncertainty, rework, anxiety, or policy exposure. | Translate into measurable impact. |
| Opportunity | Defines an intervention option. | Include non-feature alternatives. |
| Requirement Candidate | Drafts FR, NFR, UX, data, support, or governance requirement. | Must include trace fields. |

## Trace Matrix

| Journey ID | Stage | Actor | Evidence ID | Pain/Risk | Candidate Requirement | Type | Outcome Metric | Downstream Artifact |
|---|---|---|---|---|---|---|---|---|
| JNY-001 | Onboarding | Clerk | INT-004 | Cannot identify next required document | UX-JNY-001 | UX/content | Form completion rate >= target | UX spec, test plan |

## Future-State Requirement Rules

1. Preserve the current-state map as evidence.
2. Create future-state deltas only after naming the current problem.
3. For each delta, record the intervention type:
   - product feature
   - content or microcopy
   - service/support action
   - policy or operating procedure
   - integration or data capture
   - training or adoption action
4. If the delta is uncertain, create a validation hypothesis instead of a fixed requirement.
5. Feed validated deltas into SRS/backlog and unvalidated deltas into discovery or prototype plans.

## Quality Gate

Reject the conversion if:

- more than 20% of requirements have no evidence ID
- a journey stage has pain points but no requirement, hypothesis, or explicit deferral
- all opportunities become software features
- frontstage user changes are specified without checking employee, support, or operations impact
- metrics stop at satisfaction and omit task completion, error, time, support contact, adoption, or business outcome measures

