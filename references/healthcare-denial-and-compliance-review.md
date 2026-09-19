# Healthcare denial, compliance, and risk-adjustment review

Use this reference to document denial cases, compliance review, and model or
risk-adjustment evidence. It is a human-governed review contract and does not
authorise automated diagnosis, upcoding, payment, or risk acceptance.

## Source and currentness

This is an independent synthesis of B08-A03. Current payer policy, jurisdiction,
clinical/compliance authority, and any risk-adjustment model documentation are
required inputs. Until they are supplied and verified, the related claim is
`NOT_ASSESSED` and must remain quarantined. `needs-current-verification` is the
source disposition for those inputs.

## Denial case contract

| Field | Required value |
| --- | --- |
| `case_id` | Stable case and claim identifiers |
| `denial_reason` | Verbatim source reason plus mapped category, if approved |
| `evidence` | Claim, encounter, payer response, and provenance references |
| `owner` | Named claims/compliance role |
| `disposition` | Correct, appeal, accept, request information, or `NOT_ASSESSED` |
| `due_date` | Source-backed date or explicitly unknown |
| `review` | Clinical/compliance decision, reviewer, date, and scope |
| `model_version` | Version and source documentation for any risk-adjustment use |
| `controls` | Access, separation of duties, audit, and escalation evidence |

## Review rules

- No denial closes without disposition evidence and an accountable reviewer.
- An unverified legal, payer, clinical, or model claim is quarantined.
- Referral or payment anomalies route to the current compliance owner.
- Model inputs, version, source documentation, and limitations are retained.
- The system may surface evidence and route work; a human makes diagnosis,
  coding, upcoding, payment, and risk-acceptance decisions.

## Negative fixture

```yaml
case_id: DEN-001
denial_reason: source response supplied
evidence: payer response only; encounter evidence missing
owner: named owner required
disposition: absent
model_version: absent
expected_result: BLOCKED
```

The case cannot close. Record the missing evidence, resolver, and next review;
do not infer a denial outcome from a partial response.

