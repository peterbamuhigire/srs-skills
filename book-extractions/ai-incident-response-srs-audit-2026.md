# AI Incident Response & Postmortem SRS-Skills Audit — May 2026

This audit extends the AI-on-SaaS pass (`ai-on-saas-srs-audit-2026.md`) with the documentation stack required to operate AI features under incident conditions inside a multi-tenant SaaS boundary. It contrasts the engine against the artefacts that an on-call engineer, an enterprise AI buyer, an EU AI Act market-surveillance authority, a GDPR supervisory authority, and an internal Responsible-AI committee will demand the day an AI feature fails in production, and emits the new skill stack.

Convention: skill IDs follow the existing per-phase numbered pattern. New skills are prefixed with `ai-` after the numeric prefix where the skill is AI-specific. The phase-06 AI family continues from slot 13 (the next free slot after `12-ai-cost-runbook`); the phase-09 AI compliance family continues from slot 18 (after `17-ai-adr-catalogue`).

## Summary of new artefacts created this session

- **New skills (8):** seven in phase 06, one in phase 09 — see "New skills" table at the foot.
- **Enhanced skills (10):** AI-incident addenda added to existing SaaS incident skill, hallucination SLO skill, rollout runbook skill, cost runbook skill, AI Act compliance skill, RAI declaration skill, eval-harness skill, red-team skill, DoD skill, phase-06 README.
- **Cross-cutting templates (11):** severity matrix, response runbook, RCA taxonomy, postmortem, evidence-pack spec, status-page templates, customer notification templates, regulator-notification template, drill catalogue, comms-language patterns, classification decision tree.

---

## Why AI incidents are a separate documentation pass

The existing `09-saas-incident-response-and-postmortem` skill handles the SaaS dimension (tenant scope, blast radius, blameless postmortem). It does not name the AI-specific failure classes, and an on-call engineer reaching for a generic runbook on the day of an AI incident will be operating blind. AI features fail in ways the generic SaaS runbook cannot guide:

1. **Hallucination spike** — model output starts asserting unsupported claims at elevated rate; not a service outage; not a 5xx; classic monitoring is blind.
2. **Prompt drift / prompt regression** — a prompt change passes eval but regresses in production traffic distribution.
3. **Model regression** — provider silently rotates a model version, deprecates a checkpoint, or changes default temperature; quality drops with no deploy on our side.
4. **Jailbreak / prompt injection** — indirect injection via retrieved content or tool output escalates privilege, exfiltrates data, or coerces unauthorised action.
5. **Tool-chain failure** — an agent's tool API changes schema or rate-limits; the agent fails partially or loops.
6. **Cost runaway** — token spend per tenant 10x baseline within an hour due to a prompt regression, retry storm, or abusive input.
7. **Agent-action incident** — autonomous action with side effects misfires (wrong email sent, wrong record updated, wrong file deleted).
8. **Training-data shift / distribution shift** — production input distribution drifts from eval set; metrics stay green on the golden set, real users see regressions.
9. **Retrieval drift** — index rebuild changes ranking; embedding model upgrade silently breaks citation alignment.
10. **Eval drift** — the eval harness itself is wrong (golden-set rot, judge-LLM drift, test-set leakage); green eval no longer means safe.

Each of those has distinct detection signals, distinct mitigations (kill switch, prompt rollback, model fallback, index pinning, abstain mode, read-only mode), distinct evidence to preserve (trace bundle, prompt+model+tool version, retrieval set, eval output), distinct customer comms (we cannot say "outage" when output is wrong; we cannot stay silent because the user sees the wrong output), distinct regulator obligations (EU AI Act Art. 73 serious-incident reporting for high-risk systems, GDPR Art. 33 breach where personal data leaked).

The SaaS pass cannot cover this. The current engine does not cover it. This pass closes the gap.

---

## Phase 06 — Deployment & Operations

### Gaps the AI-incident reality reveals

| # | Gap | Source |
|---|-----|--------|
| 1 | No AI-specific severity matrix; existing matrix has severity × tenant scope but not autonomy / blast-radius (agent-action incident is operationally different from a hallucination spike) | NIST AI RMF MANAGE-2; EU AI Act Art. 73 serious-incident definition |
| 2 | No AI incident response runbook — no first-five-min / first-thirty-min / first-two-hour timed phases by AI failure class | Google SRE applied to AI; Anthropic / OpenAI production-LLM playbooks |
| 3 | No AI RCA taxonomy — engineers re-derive root-cause categories each incident; no shared vocabulary | NIST AI RMF MAP-2; ISO/IEC 42001 Annex A.6 |
| 4 | No AI postmortem template — blameless template exists for SaaS but does not name model / prompt / tool / retrieval / eval / data / cost failure modes | Google SRE; ISO/IEC 42001 Clause 10 (improvement) |
| 5 | No AI evidence-pack spec — when an AI incident lands, the trace, prompt, model version, tool call log, retrieval set, eval output, and reproduce-script must all be preserved with chain-of-custody for regulator handover | EU AI Act Art. 12 (logs); Art. 20 (corrective actions); GDPR Art. 30 records |
| 6 | No AI status-page or customer-notification templates per failure class — "outage" copy is wrong for hallucination; "investigating" is wrong when the system is producing confidently wrong answers | FCC / NIST incident-comms; FTC Section 5 (deceptive AI claims) |
| 7 | No AI incident drill / game-day spec — kill switch, model fallback, prompt rollback, index pinning, abstain mode, and read-only mode are never rehearsed; rollback rehearsal is mentioned in the rollout runbook but is not a catalogued game-day exercise | Google SRE DiRT; AWS GameDay; FedRAMP continuous monitoring |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `13-ai-incident-severity-matrix` | `06-deployment-operations/13-ai-incident-severity-matrix/` | Three-dimensional severity (sev × tenant-scope × autonomy/blast-radius); thresholds per AI failure class; mapping to SLA service credits and EU AI Act "serious incident" |
| `14-ai-incident-response-runbook` | `06-deployment-operations/14-ai-incident-response-runbook/` | Timed playbook (first-five / first-thirty / first-two-hour); per-failure-class procedures; kill-switch, model-fallback, prompt-rollback, index-pinning, abstain-mode, read-only-mode steps |
| `15-ai-rca-taxonomy-doc` | `06-deployment-operations/15-ai-rca-taxonomy-doc/` | Full root-cause catalogue: model, retrieval, tool/agent, eval, data, infra, commercial; example incidents per node |
| `16-ai-incident-postmortem-template` | `06-deployment-operations/16-ai-incident-postmortem-template/` | Blameless AI postmortem: timeline, RCA classification, contributing factors, per-tenant impact, regulator-impact assessment, action items by class, public publication policy |
| `17-ai-incident-evidence-pack-spec` | `06-deployment-operations/17-ai-incident-evidence-pack-spec/` | Trace bundle + prompt+model+tool versions + retrieval set + eval output + customer-affected list + action audit log + reproduce script + price-table snapshot; chain-of-custody; retention |
| `18-ai-incident-customer-comms-templates` | `06-deployment-operations/18-ai-incident-customer-comms-templates/` | Status-page templates per failure class; per-tenant notifications per severity; per-vertical adaptations |
| `19-ai-incident-drill-and-game-day-spec` | `06-deployment-operations/19-ai-incident-drill-and-game-day-spec/` | Game-day catalogue (token-cost runaway, foundation-model deprecation, prompt-injection-via-tool, retrieval-poison, hallucination spike, agent-action incident); quarterly cadence; pass/fail criteria |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `09-saas-incident-response-and-postmortem` | AI-specific addendum: severity-matrix third dimension (autonomy); pointer to AI response runbook, AI postmortem, AI evidence pack |
| `10-ai-hallucination-slo-doc` | Burn-rate alert → AI incident response runbook pointer |
| `11-ai-feature-rollout-runbook` | Auto-rollback trigger → AI incident pointer; rollback rehearsal cross-link to drill spec |
| `12-ai-cost-runbook` | Spend-anomaly → AI incident triage pointer |
| Phase 06 `README.md` | New AI-incident family registered |

---

## Phase 09 — Governance & Compliance

### Gaps the AI-incident reality reveals

| # | Gap | Source |
|---|-----|--------|
| 1 | No EU AI Act Art. 73 serious-incident-reporting doc — providers of high-risk systems must report to market-surveillance authorities within 15 days of awareness (immediate for wide-scale or death/serious-injury cases); template, evidence handover, and notification window matrix not in the engine | EU Reg 2024/1689 Art. 73 |
| 2 | No intersection doc between EU AI Act Art. 73 (15 d) and GDPR Art. 33 (72 h) — same incident can trigger both clocks with different scopes, different authorities, different evidence | EU Reg 2016/679 Art. 33; EU Reg 2024/1689 Art. 73 |
| 3 | No coverage of UK (pending), US state-level (Colorado, California ADMT, NYC AEDT), or African regulators (Kenya ODPC, Nigeria NDPC, South Africa POPIA) AI-incident touchpoints | UK ICO; CO SB24-205; CA ADMT regs; NYC LL 144; Kenya DPA 2019; NDP Act 2023; POPIA 2013 |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `18-ai-regulator-incident-notification-doc` | `09-governance-compliance/18-ai-regulator-incident-notification-doc/` | EU AI Act Art. 73 reporting; notification window matrix (EU 15 d / immediate for wide-scale; GDPR 72 h; UK pending; US state-level; African regulators); notification template; evidence handover; multi-regulator coordination |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `15-ai-act-and-regulatory-compliance-doc` | Art. 73 serious-incident reporting pointer |
| `14-ai-responsible-ai-declaration` | Incident-transparency commitments (postmortem publication, regulator-notification posture) |
| `04-ai-eval-harness-spec` (Phase 05) | Eval-drift → AI incident pointer |
| `05-ai-red-team-test-plan` (Phase 05) | Severe red-team finding → AI incident pointer (treat as incident) |
| `02-definition-of-done` | AI DoD addendum: AI runbook coverage + game-day inclusion before GA |

---

## Cross-engine handoff to the software-development engine

This pass coordinates with a parallel software-dev engine session that owns the engineering and tooling side of AI incidents. The boundary is explicit:

| Owned by docs engine (this pass) | Owned by software-dev engine (parallel) |
|----------------------------------|------------------------------------------|
| AI severity matrix | Severity-routing automation, pager rules |
| AI incident response runbook (operator-grade) | Kill-switch code, feature-flag plumbing, prompt-tag rollback, model fallback router |
| AI RCA taxonomy doc | RCA-tag emission from tracing system; structured-postmortem schema |
| AI postmortem template | Postmortem-tooling integration |
| AI evidence-pack spec | Evidence-bundle exporter; reproduce-script generator; price-table snapshotter |
| AI customer-comms templates | Status-page automation; per-tenant notification dispatcher |
| AI regulator-notification template | Regulator-portal integration (where available); evidence-handover packaging |
| AI drill / game-day spec | Game-day harness (controllable fault injection); chaos-AI tooling |

Cross-links from this pass into the software-dev pass are explicit in each skill's `references/`.

---

## Critical gaps still open after this pass

1. **Multi-cloud + multi-provider failover doc** — what to do when both the primary and the fallback foundation-model provider degrade simultaneously. The AI cost runbook names a fallback ladder but the recovery posture under joint degradation is not specified.
2. **AI-incident-and-cybersecurity-incident intersection** — when an AI incident is also a security incident (prompt injection that exfiltrates data is both), coordination with the security IR process needs a dedicated doc.
3. **AI-incident-and-customer-claims doc** — when an AI feature causes downstream customer harm (wrong action sent to wrong recipient, wrong recommendation acted on), the liability and contractual posture is undocumented.
4. **AI-incident retrospective metrics doc** — there is no rolled-up KPI / leading-indicator doc tying AI incident counts and classes back into the rolling Responsible-AI committee review.

---

## Aggregate table — all new skills emitted this pass

| Phase | Slot | Name | Output |
|-------|------|------|--------|
| 06 | 13 | `ai-incident-severity-matrix` | `AI_Incident_Severity_Matrix.md` |
| 06 | 14 | `ai-incident-response-runbook` | `AI_Incident_Response_Runbook.md` |
| 06 | 15 | `ai-rca-taxonomy-doc` | `AI_RCA_Taxonomy_Doc.md` |
| 06 | 16 | `ai-incident-postmortem-template` | `AI_Postmortem.md` per incident |
| 06 | 17 | `ai-incident-evidence-pack-spec` | `AI_Incident_Evidence_Pack_Spec.md` |
| 06 | 18 | `ai-incident-customer-comms-templates` | `AI_Incident_Customer_Comms.md` |
| 06 | 19 | `ai-incident-drill-and-game-day-spec` | `AI_Incident_Drill_And_Game_Day_Spec.md` |
| 09 | 18 | `ai-regulator-incident-notification-doc` | `AI_Regulator_Incident_Notification_Doc.md` |
