# Rollout Support And Customer Service Scripts

## Source Grounding

Derived from local HTML extractions:

- `marketing-excellence/toc.ncx`: marketing measurement, customer insight, launching new brands, sustaining the promise, communications, loyal relationships, internal marketing, marketing capabilities.
- `handbook-persuasion-social-marketing/toc.ncx` and HTML splits: ethical behaviour change, diffusion, risk communication, social marketing campaigns, impact measurement.
- `sales-scripts-that-sell/toc.ncx` and HTML splits: qualification, structured sales conversations, objections, closing, and follow-up.
- `perfect-phrases-customer-service/toc.ncx` and HTML splits: empathy, apology, escalation, difficult interactions, follow-up, and recovery language.
- `service-design-thinking/toc.ncx`: evidencing and implementation of services.

The script patterns below are original and adapted for SDLC rollout.

## Adoption Segments

| Segment | Plan Needs | Evidence |
|---|---|---|
| Economic buyer | value proof, risk controls, reporting | ROI report, adoption dashboard |
| Daily user | workflow training, quick help, confidence | task completion, error rate |
| Administrator | configuration, permissions, support handoff | admin checklist |
| Support agent | scripts, escalation, known issues | support playbook |
| Operations owner | monitoring, incident, maintenance | runbook, SLO dashboard |
| Public/customer audience | trust, access, service expectations | launch communication |

## Launch Communication Matrix

| Audience | Message Goal | Channel | Timing | Owner | Success Signal |
|---|---|---|---|---|---|
| Users | Know what changes and what to do first | Email/in-app/training | T-7, T-1, launch | Product | First-task completion |
| Support | Handle predictable questions | Briefing/script | T-5, T-1 | Support Lead | Ticket resolution |
| Executives | See value and risk status | Brief/report | T-3, launch+7 | Sponsor | Decision confidence |

## Support Script Pattern

Use this structure for service desk scripts:

1. Acknowledge the user goal or problem.
2. Confirm identity, context, and affected workflow.
3. Classify severity and ownership.
4. State immediate action.
5. Set a time expectation.
6. Provide workaround or next best action where possible.
7. Record evidence and case ID.
8. Follow up and confirm closure.

```text
When a user reports [issue], support shall say: "I can help with [goal]. I need to confirm [context]. I will [action] by [time]. Your reference is [case]. If [condition], use [workaround/escalation]."
```

## Customer Recovery Requirement Pattern

```text
SUP-ROL-###: When [service failure] affects [audience], the support process shall acknowledge impact, explain the recovery path, provide a named owner, update the user every [interval], and record root cause, corrective action, and follow-up confirmation.
```

## Training Gate

Each role needs:

- task list
- training format
- practice environment or demo data
- pass/fail or confidence check
- help path
- owner for refresh updates after release changes

## Adoption Metrics

| Metric | Use |
|---|---|
| Activation rate | Users complete first meaningful workflow. |
| Feature adoption | Target roles use intended capability. |
| Support contact rate | Measures confusion or defects after rollout. |
| First-contact resolution | Measures support readiness. |
| Time to proficiency | Measures training quality. |
| Recovery satisfaction | Measures handling of failures. |
| Renewal/continuation signal | Measures sustained value for SaaS or premium services. |

## Gate

Do not approve rollout if:

- support cannot answer the top 10 likely questions
- no owner exists for hypercare triage
- training has no role-specific task checks
- launch communications omit risk, support path, or first action
- premium or public commitments exceed actual support capacity

