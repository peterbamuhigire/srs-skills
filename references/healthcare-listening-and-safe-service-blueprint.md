# Healthcare listening and safe-service blueprint

Use this blueprint to turn patient, caregiver, staff, and professional
listening into testable service requirements. It supports accessible service
paths while preserving clinical and operational decision rights.

## Source and currentness

This is an independent synthesis of B32-A05. Current local access, privacy,
clinical safety, and service requirements are required inputs and remain
`needs-current-verification` until their owners and effective versions are
recorded. Marketing language is not evidence of a health fact.

## Blueprint contract

| Stage | Actor and decision right | Requirement and evidence |
| --- | --- | --- |
| Listen | patient/caregiver may describe need; staff records consent and scope | accessible input path, consent/status, source timestamp |
| Understand | professional/service owner interprets service need within scope | plain-language confirmation and escalation option |
| Act | authorised human decides service action | role/credential evidence and action record |
| Interrupt | patient, caregiver, staff, or professional may stop or defer | preserved state, reason, owner, and escalation record |
| Support | support owner handles access, language, communication, or technical barrier | accommodation, handoff, and unresolved barrier |
| Feedback | patient/caregiver/staff may report outcome or harm | feedback id, route, response owner, and review date |

## Acceptance and failure paths

- A representative user completes or documents an accessible path with the
  project-defined access needs recorded.
- An interrupted workflow preserves the current state, escalation route, and
  audit evidence so a human can resume or close it.
- Missing consent, inaccessible content, unresolved safety concern, or unknown
  owner routes to support/review and is not silently closed.
- Verified service facts and marketing claims are stored and reviewed as
  separate content classes.
- No clinical action is automated by this blueprint.

## Synthetic interruption fixture

```yaml
journey_id: LISTEN-001
actor: caregiver using an accessible service path
event: session is interrupted before a service decision
expected_result: state and escalation owner remain visible; no action is taken
evidence: interruption reason, timestamp, current state, owner, and follow-up route
review_status: NOT_ASSESSED until project access/privacy requirements are supplied
```

