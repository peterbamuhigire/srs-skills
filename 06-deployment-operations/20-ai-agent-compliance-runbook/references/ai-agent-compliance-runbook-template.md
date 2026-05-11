# AI Agent Compliance Runbook — Template

Adapt by replacing `{placeholder}` values. All times in `{operating timezone}`.

## 1. Drill schedule

| Drill | Cadence | Default slot | Owner | Back-up | Verification |
|-------|---------|--------------|-------|---------|--------------|
| Global kill-switch (staging) | quarterly | first Tuesday of Mar, Jun, Sep, Dec — 10:00 | SRE Lead | Security on-call | Drill report; propagation ≤ 5 s; audit-log entry |
| Per-tenant kill-switch (staging) | quarterly | first Tuesday of Mar, Jun, Sep, Dec — 11:00 | SRE Lead | AI Lead | Drill report |
| Per-feature kill-switch (staging) | quarterly | first Tuesday of Mar, Jun, Sep, Dec — 11:30 | AI Lead | SRE Lead | Drill report |
| Global kill-switch (production) | annual | second Tuesday of Jun — 14:00; tenants notified 30 d prior | SRE Lead | Security on-call | Drill report; tenant notification log |
| Replay-a-run | quarterly | third Wednesday of Mar, Jun, Sep, Dec — 10:00 | AI Lead | Engineering Manager | Drill report |
| Force-pause + force-resume | quarterly | third Wednesday of Mar, Jun, Sep, Dec — 11:00 | SRE Lead | AI Lead | Drill report |
| Agent-task quarantine | annual | second Wednesday of Sep — 14:00 | AI Lead | DPO | Drill report; tenant-admin notification log |
| Evidence-pack assembly dry run | quarterly | last Friday of Mar, Jun, Sep, Dec — 14:00 | Compliance Manager | AI Lead | Pack signed zip; manifest hash recorded |
| BAA / DPA execution dry run | annual | first Monday of Oct — 10:00 | DPO | Legal | Counter-signed addendum produced |
| Auditor portal access dry run | quarterly | last Friday of Mar, Jun, Sep, Dec — 15:00 | Compliance Manager | Security | Access granted to named test recipient; revoked on day +1 |

## 2. Evidence-collection schedule

Reference: `09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md`.

For every row in that table, the calendar holds a recurring item with owner and verification step. Escalation: missed cadence × 2 = SEV2; × 3 = SEV1.

## 3. Control-test schedule

| Test | Cadence | Default slot | Owner | Verification |
|------|---------|--------------|-------|--------------|
| Agent service-principal access review | quarterly | second Tuesday of Mar, Jun, Sep, Dec | Security | Signed access-review CSV |
| Tool allow-list reperformance | quarterly | second Tuesday of Mar, Jun, Sep, Dec | AI Lead | Reperformance log |
| Hash-chain integrity (automated daily; weekly review) | daily + weekly | nightly job; Fridays 10:00 review | Security | Integrity report |
| Approval-event sample review (25) | monthly | second Monday | AI Lead | Sample reviewed; anomalies escalated |
| Daily-review ticket sample (25) | monthly | second Monday | AI Lead | Sample reviewed |
| PR sample review (25) | quarterly | second Monday of Mar, Jun, Sep, Dec | CTO | Sample reviewed; gate evidence verified |
| Sub-processor list review | quarterly | first Monday of Mar, Jun, Sep, Dec | DPO | Review record |
| BAA / DPA currency review | quarterly | first Monday of Mar, Jun, Sep, Dec | DPO | Currency table updated |
| Disclosure currency review | quarterly | first Monday of Mar, Jun, Sep, Dec | AI Lead | Screenshots captured |
| Bias review (protected-class features) | quarterly | third Monday of Mar, Jun, Sep, Dec | DPO + AI Lead | Bias review report |

## 4. Audit-window operating procedure

### Daily

| Item | Owner | Verification |
|------|-------|--------------|
| Hash-chain integrity report reviewed | Security on-call | Ticket created if any gap |
| Anomaly tickets triaged | SRE on-call | Triage notes |
| Approval-event log spot-check | AI Lead | Spot-check log |

### Weekly

| Item | Owner |
|------|-------|
| Evidence sweep — every artefact for the week captured | Compliance Manager |
| Manifest hash recorded | Compliance Manager |
| Red-team full set results reviewed | Security |

### Monthly

| Item | Owner |
|------|-------|
| SLO report assembled | AI Lead |
| Approval events sample (25) | AI Lead |
| Daily-review tickets sample (25) | AI Lead |

### Quarterly

| Item | Owner |
|------|-------|
| Drills (see Section 1) | per drill owner |
| Access reviews (see Section 3) | Security |
| Sub-processor review | DPO |
| BAA/DPA currency | DPO |
| Bias review | DPO + AI Lead |
| Auditor portal dry run | Compliance Manager |

### Mid-window (T-3)

| Item | Owner |
|------|-------|
| Gap check — every control's evidence completeness | Compliance Manager |
| Remediation actions for any control with < 95% completeness | AI Lead + control owner |

### T-1 (one month before fieldwork)

| Item | Owner |
|------|-------|
| Closure preparation | Compliance Manager |
| Auditor portal access prepared | Compliance Manager |
| On-the-day playbook printed and distributed | Compliance Manager |
| Demoer roster confirmed | AI Lead |
| Pre-window dry run with internal audit | Compliance Manager |

### T+1 (fieldwork begins)

Activate the auditor on-the-day playbook.

## 5. On-the-day playbook activation

1. Compliance Manager confirms auditor identity and activates portal access for named recipient.
2. Demoer roster confirmed; back-up demoers on standby.
3. Walkthrough order set with auditor.
4. Walkthroughs follow `09-governance-compliance/24-ai-agent-attestation-preparation-spec/references/ai-agent-auditor-on-the-day-playbook.md`.
5. Action items recorded as they arise.
6. End of day: portal access reduced to read-only; debrief held.

## 6. Gap-remediation cadence

| Severity | SLA | Owner | Closure verification |
|----------|-----|-------|----------------------|
| SEV1 — mandatory control without evidence; control failed during window | 7 days | AI Lead + CTO | Evidence captured; ledger updated; signature collected |
| SEV2 — evidence incomplete or sampling unattainable | 30 days | AI Lead | Evidence captured; pack updated |
| SEV3 — documentation polish; cross-link missing | 90 days | Compliance Manager | Cross-link added; review confirmed |

## 7. Roles

| Role | Compliance responsibilities |
|------|------------------------------|
| AI Lead | Evidence custodian; governance and approval walkthroughs; agent SLI and red-team accountable |
| CTO | Change management sample; system architecture walkthrough; sign-off on agent ADRs |
| CISO | Kill-switch drill owner; access reviews; security walkthroughs; sign-off on red-team |
| DPO | Privacy controls; DSAR; BAA/DPA; sub-processor reviews; bias review co-owner; HIPAA admin-only sign-off |
| Compliance Manager | Audit-window orchestration; auditor portal; sign-off ledger; pack assembly |
| SRE Lead | Drill execution; observability evidence; orchestrator availability evidence |

## 8. Calendar index

| Item | Cadence | Owner |
|------|---------|-------|
| (see all rows above; pulled into one sortable index) | | |

## 9. Cross-Refs

- Control packs: `09-governance-compliance/20`, `21`, `22`.
- Policy pack: `09-governance-compliance/23`.
- Attestation preparation: `09-governance-compliance/24`.
- Evidence pack: `09-governance-compliance/25`.
- Agent operations runbook: `06-deployment-operations/14`.
- AI incident response runbook: `06-deployment-operations/14-ai-incident-response-runbook`.

## 10. Sign-off

| Role | Name | Date |
|------|------|------|
| AI Lead | | |
| Compliance Manager | | |
| CISO | | |
| DPO | | |
