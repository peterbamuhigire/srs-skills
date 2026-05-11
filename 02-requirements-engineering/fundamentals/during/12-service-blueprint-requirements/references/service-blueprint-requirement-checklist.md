# Service Blueprint Requirement Checklist

## Source Grounding

Derived from local HTML extractions:

- `mapping-experiences/toc.ncx`, especially service blueprint chapters and elements listed in `index_split_004.html`.
- `service-design-thinking/toc.ncx`, especially user-centred, co-creative, sequencing, evidencing, holistic, exploration, creation, reflection, and implementation sections in `index_split_000.html`.
- `perfect-phrases-customer-service/toc.ncx` and HTML splits for apology, escalation, difficult interactions, and follow-up language patterns.
- `sales-scripts-that-sell/toc.ncx` and HTML splits for structured conversations, qualification, objections, and follow-up.

This file contains original derived SDLC guidance, not copied book text.

## Blueprint Lanes

| Lane | Requirement Questions | Output Requirement Types |
|---|---|---|
| Customer actions | What is the user trying to complete? Where can they stop, err, or need help? | FR, UX, accessibility, content |
| Frontstage interaction | What screen, person, message, device, form, or document meets the user? | UX, form, notification, support |
| Backstage action | What staff, automation, approval, queue, or review must happen out of sight? | Workflow, role, SLA, audit |
| Support systems | What system, integration, data store, AI service, or external API enables the action? | HLD, API, data, security, monitoring |
| Evidence | What proof does the user, operator, auditor, or manager need? | Document, receipt, log, report, trace |
| Failure and recovery | What can fail, how is it detected, who owns recovery, and what is said? | Error, incident, support script, rollback |
| Metric | How is service quality measured at this point? | Test, monitoring, rollout, evaluation |

## Requirement Extraction Checklist

For every blueprint step, ask:

1. Does the customer need a system response, status, document, or confirmation?
2. Does frontstage staff need a script, screen, permission, or checklist?
3. Does backstage staff need a queue, case state, approval rule, escalation path, or audit trail?
4. Does the system need to store an event, timestamp, actor, decision, exception, or evidence artifact?
5. Does a failure require inline recovery, support recovery, rollback, compensation, or human intervention?
6. Does the step create a training, adoption, maintenance, or governance obligation?
7. Does the service promise depend on a vendor, regulator, payment provider, network, AI model, or external data source?

## Failure Taxonomy

| Failure Type | Requirement Pattern |
|---|---|
| User cannot proceed | Provide inline recovery, alternative channel, or support escalation. |
| Staff cannot complete backstage action | Provide queue visibility, retry, reassignment, and escalation. |
| Integration fails | Provide timeout, retry, fallback, manual reconciliation, and incident trigger. |
| Evidence missing | Provide receipt, event log, audit record, or export requirement. |
| Policy exception | Provide approval workflow and decision record. |
| Misunderstanding | Provide content, confirmation, training, or script requirement. |

## Recovery Script Requirement Pattern

Use this original pattern for service desk or support scripts:

```text
SUP-BP-###: When [failure] occurs during [stage], support staff shall acknowledge the issue, confirm [user/context data], state the next action, provide [time expectation], and record [case evidence] before closing or escalating the case.
```

## Blueprint Trace Matrix

| Blueprint Step | Lane | Evidence | Failure Mode | Derived Requirement | Owner | Verification |
|---|---|---|---|---|---|---|
| BP-001 | Frontstage | Screen recording | User submits incomplete form | UX-BP-001 | UX Lead | Usability test |
| BP-002 | Backstage | SOP-004 | Approval queue stalls | WF-BP-002 | Operations | Workflow simulation |

## Acceptance Gate

The service blueprint is not ready if:

- any frontstage step lacks a backstage owner
- any critical backstage step lacks system support, monitoring, or manual fallback
- any high-risk failure lacks a recovery path and user/staff language
- any evidence artifact lacks storage, ownership, retention, and retrieval requirements
- launch documentation lacks training and support implications from the blueprint

