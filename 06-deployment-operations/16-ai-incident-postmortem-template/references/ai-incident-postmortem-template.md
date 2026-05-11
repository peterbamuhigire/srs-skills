# AI Incident Postmortem Template

Use this template for every AI incident at SEV2 or above. Tone: blameless. No individuals named as causes. Names of roles only.

```
# AI Postmortem: <incident title>

- Incident ID:
- Date / time started (UTC):
- Date / time resolved (UTC):
- Severity (final):
- Tenant scope: single / cohort / platform-wide / cross-tenant leakage
- Autonomy level at failure: advisory / assistive / autonomous-with-rollback / autonomous-irreversible
- AI failure class (per Severity Matrix section 2):
- RCA taxonomy tags:
  - Primary:
  - Contributing:
- Incident commander:
- AI lead:
- Author:
- Status: draft / under review / published / closed

## 1. Summary

One paragraph. State what happened, who was affected, what was done, and what the durable fix is.

## 2. Impact

- Tenants affected: <count> (named for Enterprise; anonymised for Free/Pro)
- Duration: HH:MM
- AI SLO burn:
  - Factuality: <minutes / % of monthly budget>
  - Citation accuracy: <minutes / % of monthly budget>
  - Abstention precision: <minutes / % of monthly budget>
  - Safety violations: <count> (zero-budget; any breach is SEV1)
- Financial impact (estimate):
  - Service credits owed: <amount>
  - Provider cost incurred during the incident: <amount>
  - Churn-risk ARR exposure: <amount>
- Support load: <ticket count>; peak concurrent <count>
- Reputational impact: press <urls>; social <urls>; trust-center update required <yes/no>

## 3. Timeline (UTC)

| Time | Event | Source | Action taken |
|------|-------|--------|--------------|
| T-X | Alert / report / trigger | <alert id / ticket id / scribe note> | <none> |
| T+0 | Incident declared | <IC> | severity assigned |
| ... | ... | ... | ... |
| T+N | Resolved | <IC> | status-page closed |

## 4. Root cause analysis

### 4.1 5-whys

1. Why? <answer>  [tag: <family.node>]
2. Why? <answer>  [tag: <family.node>]
3. Why? <answer>  [tag: <family.node>]
4. Why? <answer>  [tag: <family.node>]
5. Why? <answer>  [tag: <family.node>]

### 4.2 Tag verdict

- Primary: <family.node> — justification.
- Contributing: <family.node>, <family.node> — justification.

### 4.3 Evidence cross-refs

- Trace bundle: <evidence-pack ref>
- Prompt + model + tool versions at T: <ref>
- Retrieval set at T: <ref>
- Eval output at T: <ref>
- Reproduce script: <ref>
- Action-audit log: <ref>
- Model-price-table snapshot: <ref>

## 5. Per-tenant impact

| Tenant id | Tier | Severity-experienced | Requests affected | Outputs flagged | Autonomous actions taken | Reconciliation required | Comms sent (template) | Service credit owed |
|-----------|------|----------------------|-------------------|-----------------|--------------------------|--------------------------|------------------------|----------------------|

## 6. Regulator-impact assessment

Mandatory for every SEV1, regardless of whether reporting was triggered. Filled in jointly with DPO/legal.

| Regulator / regime | Limb evaluated | Verdict | Window | Status | Authority notified |
|--------------------|----------------|---------|--------|--------|---------------------|
| EU AI Act Art. 73 — death/serious harm | <yes/no> | <triggered/not> | immediate / 10 d | <sent / not required> | <authority> |
| EU AI Act Art. 73 — fundamental rights | <yes/no> | <triggered/not> | 2 d (wide-scale) / 15 d | <sent / not required> | <authority> |
| EU AI Act Art. 73 — critical infrastructure | <yes/no> | <triggered/not> | 2 d (wide-scale) / 15 d | <sent / not required> | <authority> |
| EU AI Act Art. 73 — property/environment | <yes/no> | <triggered/not> | 15 d | <sent / not required> | <authority> |
| GDPR Art. 33 — personal-data breach | <yes/no> | <triggered/not> | 72 h | <sent / not required> | <supervisory authority> |
| US NYC Local Law 144 — AEDT | <yes/no> | n/a unless employment | n/a | <annotated> | n/a |
| US Colorado SB24-205 | <yes/no> | <triggered/not> | per statute | <annotated> | <AG> |
| US California ADMT | <yes/no> | <triggered/not> | per statute | <annotated> | <AG / CPPA> |
| Kenya ODPC AI guidance | <yes/no> | <triggered/not> | per ODPC | <annotated> | <ODPC> |
| Nigeria NDPC advisory | <yes/no> | <triggered/not> | per NDPC | <annotated> | <NDPC> |
| South Africa POPIA s.22 | <yes/no> | <triggered/not> | as soon as reasonably possible | <annotated> | <Information Regulator> |

DPO sign-off: <name / role / date>.

## 7. What went well

- ...
- ...

## 8. What went poorly

- ...
- ...

## 9. Contributing factors

- Process: ...
- Technical: ...
- Organisational: ...
- External / commercial: ...

## 10. Action items by class

| ID | Class | Description | Owner | Severity | Due | Status |
|----|-------|-------------|-------|----------|-----|--------|
| AI-001 | improve eval | extend golden set to cover <segment> | <role> | high | <date> | open |
| AI-002 | change gate | strengthen the rollout-runbook citation-accuracy gate from 90% to 92% | <role> | medium | <date> | open |
| AI-003 | add red-team | add an indirect-injection probe for <agent> | <role> | high | <date> | open |
| AI-004 | change containment | extend abstain-mode copy library for <feature> | <role> | medium | <date> | open |
| AI-005 | change provider posture | pin model version <v>; add fallback to <p2> | <role> | high | <date> | open |
| AI-006 | update model card | disclose the failure mode and the change | <role> | medium | <date> | open |
| AI-007 | update runbook | patch per-failure-class procedure 4.X | <role> | low | <date> | open |
| AI-008 | update drill | add this scenario to the quarterly game-day catalogue | <role> | low | <date> | open |

## 11. Publication policy

| Audience | Decision | Redaction | Sent date | Owner |
|----------|----------|-----------|-----------|-------|
| Internal | publish to engineering | none | | AI lead |
| Affected tenants | distribute via `tenant-notification-postmortem` | tenant-specific only | | Comms |
| Public (trust center / blog) | <publish / hold> | per redaction policy | | Comms + Trust |

Public publication is required when Art. 73 reporting occurred or when the incident was widely visible (press, social).

## 12. Lessons

- ...
- ...

## 13. Closure

Incident closed when mitigated and monitoring confirmed 30 min healthy.
Postmortem closed when all high-severity action items are done.

## 14. Cross-refs

- Severity matrix: `06-deployment-operations/13-ai-incident-severity-matrix`.
- Response runbook: `06-deployment-operations/14-ai-incident-response-runbook`.
- RCA taxonomy: `06-deployment-operations/15-ai-rca-taxonomy-doc`.
- Evidence pack: `06-deployment-operations/17-ai-incident-evidence-pack-spec`.
- Regulator notification: `09-governance-compliance/18-ai-regulator-incident-notification-doc`.
- Parent SaaS postmortem: `06-deployment-operations/09-saas-incident-response-and-postmortem`.
```
