# AI Agent HIPAA Security Rule Control Matrix Template

Worked example: agentic clinical-documentation SaaS used by a covered entity (ambulatory clinic group). Two features in scope:

- **F-1 inbox-triage** — agent reads incoming patient messages; drafts categorisation; clinician approves before any update. Classification: `limited` PHI touch.
- **F-2 chart-summary** — agent reads chart and produces a one-page summary for the clinician. Classification: `clinical` PHI touch. Admin-only; L0 only for clinician users; no external-write.

## PHI touch classification

| Feature | Classification | Tools that touch PHI | Allowed autonomy |
|---------|----------------|------------------------|--------------------|
| F-1 inbox-triage | limited | `patient.message.read`, `triage.category.suggest`, `clinician.notify` | L0; L1 only with per-call clinician approval; no L2+ |
| F-2 chart-summary | clinical | `chart.read`, `chart.section.read`, `summary.draft` | L0 only; no external-write; admin-only on clinician role |

## §164.308 Administrative safeguards

### §164.308(a)(1)(i) Security management process — Risk analysis (R)

| Field | Value |
|-------|-------|
| Agent treatment | Per-feature risk register row identifying PHI flows, reversibility, residual risk; reviewed at least annually and on material change |
| Evidence | `risk-register/agent-hipaa-features.csv`; review meeting minutes |
| Frequency | annual + on-change |
| Sampling | full population (each feature row reviewed) |
| Audit procedure | inspect register; inspect minutes; reperform: walk a feature and verify the risk row is current |

### §164.308(a)(1)(ii)(D) Information system activity review (R)

| Agent treatment | Daily irreversible-action audit-log review by on-call operator (HIPAA scope subset); weekly integrity report |
| Evidence | daily-review ticket log; weekly integrity report |
| Frequency | continuous |
| Sampling | 25 daily-review tickets |
| Audit procedure | inspect tickets; verify escalation when anomalies present |

### §164.308(a)(3)(i) Workforce security

| Agent treatment | Agent service principal is workforce-equivalent; provisioning and deprovisioning per the same procedure as human workforce |
| Evidence | service-principal lifecycle log; per-tenant scope review |
| Frequency | continuous + quarterly review |
| Audit procedure | inspect lifecycle log; reperform: deprovision a service principal in non-production and verify tool refusal |

### §164.308(a)(4)(ii)(B) Access authorisation (A)

| Agent treatment | Tool allow-list per agent service principal; explicit grant for every PHI-touching tool; tenant-admin re-grants on tenant deletion |
| Evidence | allow-list snapshots; grant log |
| Frequency | continuous |
| Audit procedure | inspect snapshots; sample grants |

### §164.308(a)(6) Security incident procedures (R)

| Agent treatment | Agent-specific incident playbooks for: cross-tenant retrieval leak, prompt-injection disclosure, audit-log integrity compromise, memory-tier leak |
| Evidence | runbook playbooks; incident log |
| Frequency | continuous |
| Audit procedure | inspect playbooks; sample incidents |

### §164.308(a)(7) Contingency plan (R)

| Agent treatment | Kill-switch drill quarterly; replay-a-run drill quarterly; force-pause + force-resume drill quarterly; criticality analysis identifies clinical PHI features as critical |
| Evidence | drill reports; criticality analysis |
| Frequency | quarterly |
| Audit procedure | inspect reports; observe drill if scheduled in window |

### §164.308(b)(1) Business associate contracts (R)

| Agent treatment | BAA addendum executed with every covered-entity tenant before agent goes live; model provider BAA executed or PHI is de-identified before model call; sub-processor change protocol notifies covered entity |
| Evidence | executed BAA addenda; provider BAA or de-id evidence; sub-processor change log |
| Frequency | per onboarding + on-change |
| Audit procedure | sample BAA addenda; trace sub-processor change |

## §164.310 Physical safeguards

Inherited from parent ISMS / SOC 2; cite inheritance.

## §164.312 Technical safeguards

### §164.312(a)(1) Access control

| Implementation spec | Agent treatment |
|---------------------|------------------|
| Unique user identification (R) | Agent service principal has unique ID; per-tenant scope encoded in identity claim |
| Emergency access procedure (R) | Operator kill-switch console + on-call rotation |
| Automatic logoff (A) | Operator console session expires after 15 minutes idle |
| Encryption and decryption (A) | Tool-call payloads encrypted at rest in audit log; at rest in memory tier |

Evidence: identity provider export; kill-switch console session policy; encryption configuration.
Frequency: continuous; quarterly review.
Audit procedure: inspect configuration; reperform out-of-scope tool call from a service principal and verify dispatcher refusal.

### §164.312(b) Audit controls (R)

| Agent treatment | Action audit log retention per Responsible-AI Addendum; hash-chain integrity; daily review of PHI-touching tool calls |
| Evidence | retention configuration; integrity report; daily-review ticket log |
| Frequency | continuous + daily review + daily integrity check |
| Sampling | 25 daily-review tickets; full population of integrity checks |
| Audit procedure | inspect configuration; reperform integrity check; sample audit-log rows for completeness of agent_run_id, plan_id, step_index, tenant_id, user_id |

### §164.312(c)(1) Integrity (A: mechanism to authenticate ePHI)

| Agent treatment | Hash-chain audit log with per-block signatures (from software-dev pass); reproduce-script preservation; signed approval events |
| Evidence | integrity report; sample signed approval event |
| Frequency | continuous + daily |
| Audit procedure | inspect integrity report; reperform: alter a captured artefact in test environment and verify integrity verifier flags it |

### §164.312(d) Person or entity authentication (R)

| Agent treatment | Approver identity verified at the approval moment via SSO or MFA; signed approval event recorded with approver role, time, plan id |
| Evidence | approval event log sample; SSO/MFA configuration |
| Frequency | continuous |
| Sampling | 25 approval events |
| Audit procedure | sample events; trace approver identity to a workforce member |

### §164.312(e)(1) Transmission security

| Implementation spec | Agent treatment |
|---------------------|------------------|
| Integrity controls (A) | TLS 1.2+ enforced; signed claim on tenant identity passed to provider |
| Encryption (A) | All in-transit PHI encrypted; key material managed per parent ISMS A.8.24 |

Evidence: TLS configuration; signed-claim sample; encryption standard document.
Frequency: continuous.
Audit procedure: inspect configuration; observe a tool call to a PHI-touching system and verify TLS handshake.

## §164.316 Policies, procedures, and documentation

| Standard | Agent treatment |
|----------|------------------|
| §164.316(a) Policies and procedures (R) | Compliance Policy Pack signed annually; agent-specific procedures in the runbook |
| §164.316(b)(1) Documentation (R) | Retention 6 years from creation or last effective date for every agent control document |

## Minimum-necessary application (§164.502(b))

- Tool allow-list per agent service principal restricted to the minimum set required for the task.
- Retrieval set returned to the agent minimised by query-scoped filter; per-tenant scope at retrieval-time; per-patient scope where required.
- Audit log records the PHI fields touched per tool call (field names redacted in customer-distribution view; not in regulator-handover view).
- Quarterly review samples 25 tool calls and verifies minimum-necessary compliance.

## Breach notification (§164.408)

- ≤ 60 days affected individuals; immediate HHS for breaches ≥ 500 individuals; media notification for ≥ 500 in a state.
- Agent breach scenarios:
  1. Cross-tenant retrieval leak: SEV1; covered entity notified within 24 h; OCR notification triggered.
  2. Prompt-injection-driven disclosure: SEV1; same path.
  3. Audit-log integrity compromise: SEV1; same path.
  4. Memory-tier leak: SEV1; same path.

## Sign-off

| Role | Name | Date |
|------|------|------|
| AI Lead | | |
| Security Officer | | |
| Privacy Officer | | |
| Covered-Entity Authorised Signatory | | |
