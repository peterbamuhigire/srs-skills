# AI Agent Compliance Policy Pack — Template

This file is the canonical structure for the seven-policy bundle. Reproduce it section by section, replacing `{placeholder}` with project values.

---

## Pack cover page

**Pack title:** AI Agent Compliance Policy Pack
**Owner:** AI Lead
**Version:** v{n.m}
**Effective date:** {YYYY-MM-DD}
**Next review:** {YYYY-MM-DD}
**Controls supported:** SOC 2 TSC (CC1, CC5, CC7, CC8, A1, C1, PI1, P1–P8); ISO 27001:2022 (A.5.1, A.5.15, A.5.25, A.5.30, A.5.34, A.8.15, A.8.16, A.8.25, A.8.29, A.8.32); HIPAA §164.308, §164.312, §164.316; ISO/IEC 42001:2023 Clauses 5–10.

| # | Policy | Owner | Version | Effective | Next review |
|---|--------|-------|---------|-----------|--------------|
| 1 | Agent Action Governance | AI Lead | | | |
| 2 | Agent Audit-Log Retention | DPO | | | |
| 3 | Agent Approval and Supervision | CTO | | | |
| 4 | Agent Kill-Switch and Drill | CISO | | | |
| 5 | Agent Memory Erasure | DPO | | | |
| 6 | Agent Red-Team and Safety | CISO | | | |
| 7 | Agent Compliance Evidence and Attestation | AI Lead | | | |

---

## 1. Agent Action Governance Policy

### 1.1 Purpose

Establish the rules that govern what an autonomous or semi-autonomous agent feature may do, what classification an action carries, what autonomy level is permitted, and what gating applies to irreversible actions.

### 1.2 Scope

All agent features at autonomy L0 through L4. All environments (production, staging, replay). All workforce members designing, operating, approving, or auditing agent actions.

### 1.3 Definitions

- **Agent action** — a tool call emitted by the planner and executed by the dispatcher.
- **Reversibility class** — `idempotent` | `compensable` | `irreversible` per the action-catalogue rubric.
- **Autonomy level** — L0 suggest-only, L1 approve-each, L2 approve-batch, L3 autonomous, L4 cross-domain.

### 1.4 Policy statements

1. Every tool callable by the planner shall appear in the action catalogue and carry a reversibility class, a side-effect class, a per-tier availability, audit fields, a rate-limit class, and kill-switch behaviour.
2. Every irreversible-class tool call shall be gated by a named human approval at the moment of execution; the approval shall be a signed event with approver role, time, and plan identifier.
3. No tool with side-effect class other than `read` shall be available on the Free tier.
4. Catalogue changes shall require a pull request, an ADR, a red-team smoke run, an eval gate pass, AI Lead sign-off, and Security sign-off.
5. Free-form tool execution (shell-like, eval-like) is prohibited.

### 1.5 Roles and responsibilities

| Role | Responsibility |
|------|-----------------|
| AI Lead | Catalogue owner; reviews every change |
| CTO | Approves autonomy-level changes |
| CISO | Approves kill-switch behaviour changes |
| DPO | Approves PHI/PII-touching tool additions |

### 1.6 Exceptions and waivers

Exceptions require ADR plus a waiver. Maximum duration 90 days. Approver: CTO + CISO + DPO.

### 1.7 Review cadence

Annual. Off-cycle review triggered by: new SEV1 incident, regulator advisory, material change to the planner / catalogue / supervisor.

### 1.8 Related controls

SOC 2 CC5.1, CC6.1, CC6.3, CC8.1, PI1.1, PI1.4. ISO 27001 A.5.15, A.5.27, A.8.2, A.8.9, A.8.25. HIPAA §164.308(a)(4), §164.312(a)(1). ISO/IEC 42001 Clause 8.

### 1.9 Related documents

Action Catalogue Spec, Agent Architecture Spec, Responsible-AI Addendum, ADR Catalogue.

### 1.10 Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| AI Lead | | | |
| CTO | | | |
| CEO | | | |

---

## 2. Agent Audit-Log Retention Policy

### 2.1 Purpose

Bind the retention schedule for every agent event class.

### 2.4 Policy statements

1. Retention shall match or exceed the table below.

| Event class | Hot | Cold |
|--------------|-----|------|
| Tool call (read) | 90 d | 13 months |
| Tool call (write-internal) | 13 months | 3 years |
| Tool call (write-external, billing, irreversible) | 13 months | 7 years |
| Plan + approval events | 13 months | 7 years |
| Kill-switch events | 13 months | 7 years |
| Human-approval events | 13 months | 7 years |
| PHI-touching event (where HIPAA applies) | 13 months | 6 years minimum (§164.316(b)) |

2. The audit log shall be append-only and shall maintain hash-chain integrity verified daily.
3. Retention shall meet or exceed regulatory minima per region (EU, UK, US sectoral, KE, NG, ZA, UG, RW).
4. Access shall follow the access policy declared in the evidence pack spec.
5. Erasure of audit-log entries is prohibited; redaction creates a derived artefact with back-link.

### 2.5 Roles

| Role | Responsibility |
|------|-----------------|
| DPO | Policy owner |
| AI Lead | Operational owner of the log |
| Security on-call | Integrity verifier ownership |

### 2.6–2.10 Standard structure as above.

Controls supported: SOC 2 CC7.2, PI1.4. ISO 27001 A.8.15, A.8.24. HIPAA §164.312(b), §164.312(c)(1), §164.316(b)(1). ISO/IEC 42001 Annex A.6.

---

## 3. Agent Approval and Supervision Policy

### 3.4 Policy statements

1. Review-before-act shall be required for: L1 features, every irreversible-class tool call, every PHI-touching action when the feature is classified `clinical`.
2. Review-after-act shall be permitted only for compensable-class actions at L2; sampling rate per feature declared in the supervision matrix.
3. Sample-review shall be permitted for read-only actions at L3; minimum 5% sample.
4. Every approval event shall be recorded as a signed event with approver role, time, plan identifier, and step index.
5. Supervision-policy changes require ADR.

Controls supported: SOC 2 CC5.1, PI1.4. ISO 27001 A.5.15, A.8.2. HIPAA §164.312(d). EU AI Act Art. 14.

---

## 4. Agent Kill-Switch and Drill Policy

### 4.4 Policy statements

1. Three kill-switch surfaces shall be maintained: global, per-tenant, per-feature.
2. Global kill-switch invocation shall follow the two-person rule.
3. Propagation SLA shall be ≤ 5 seconds.
4. Drills shall be conducted quarterly in staging; annual production drill conducted with prior tenant notification.
5. Every drill shall produce a drill report and an audit-log entry.

Controls supported: SOC 2 CC7.3, CC7.4, A1.3. ISO 27001 A.5.30, A.8.2. HIPAA §164.308(a)(7).

---

## 5. Agent Memory Erasure Policy

### 5.4 Policy statements

1. The memory tiers shall be: scratchpad (ephemeral per run), episodic (per session), long-term (opt-in per tenant).
2. Erasure triggers shall include: tenant deletion, user DSAR, contractual expiry, regulatory order, opt-out toggle.
3. Erasure shall be verifiable; a certificate of erasure shall be produced naming the tier, the scope, the operator, and the verification timestamp.
4. Retention exceptions shall be declared: legal hold; incident evidence pack within retention window.
5. Erasure SLA shall be ≤ 30 days from request unless an exception applies.

Controls supported: SOC 2 C1.2, P4. ISO 27001 A.5.34, A.8.10. HIPAA §164.502. GDPR Art. 17.

---

## 6. Agent Red-Team and Safety Policy

### 6.4 Policy statements

1. Agent red-team CI smoke shall run on every PR touching planner, tools, agent prompts, or action catalogue.
2. Weekly full red-team replay shall be conducted; external red-team quarterly.
3. Before any L1+ rollout, zero open CRITICAL and zero open HIGH findings shall be required.
4. New adversarial scenarios shall be added within 7 days of public advisory.
5. Scenario retirement requires ADR + sign-off.

Controls supported: SOC 2 CC4.1, CC7.2, CC8.1, PI1.2. ISO 27001 A.5.7, A.8.7, A.8.29. ISO/IEC 42001 Clause 8.3.

---

## 7. Agent Compliance Evidence and Attestation Policy

### 7.4 Policy statements

1. Per-control evidence shall be collected at the declared frequency; the collector is owned by the software-dev pass; the artefact is owned by AI Lead.
2. Evidence shall be retained per the evidence-pack spec.
3. Attestation cadence: SOC 2 Type II annual; ISO surveillance annual; HIPAA annual covered-entity review.
4. Auditor portal access shall be time-bound, logged, and limited to named auditors.
5. Gap-remediation cadence: SEV1 gap remediated within 7 days; SEV2 within 30 days; SEV3 within 90 days.

Controls supported: SOC 2 CC1.4, CC2.2, all evidence-bearing rows. ISO 27001 A.5.36 (planning), A.5.37 (operations). HIPAA §164.308(a)(8). ISO/IEC 42001 Clause 9.

---

## Sign-off ledger

Each policy carries its own sign-off block; the pack-level ledger records the bundle release.

| Bundle version | Effective | AI Lead | CTO | CEO | DPO | CISO |
|----------------|-----------|---------|-----|-----|-----|------|
| v{n.m} | {YYYY-MM-DD} | | | | | |
