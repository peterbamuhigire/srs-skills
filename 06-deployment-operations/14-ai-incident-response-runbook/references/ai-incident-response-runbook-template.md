# AI Incident Response Runbook Template

This template is operator-grade. Fill in the bracketed `{values}` per project. Print it. Pin it in the on-call channel topic.

## 1. Roles

| Role | Holder (on-call rotation) | Pager | Joins from |
|------|---------------------------|-------|------------|
| Incident Commander | `{IC rotation}` | `{pager}` | SEV1: immediately. SEV2: 15 min. |
| AI lead on-call | `{AI rotation}` | `{pager}` | SEV1/2: immediately. |
| SRE on-call | `{SRE rotation}` | `{pager}` | All SEV: immediately. |
| Comms lead | `{comms rotation}` | `{pager}` | SEV1: 5 min. SEV2: 15 min. |
| Scribe | assigned by IC | n/a | SEV1/2: immediately. |
| Security on-call | `{security rotation}` | `{pager}` | Mandatory for injection-class, leakage, exfil. |
| DPO / legal on-call | `{DPO rotation}` | `{pager}` | Mandatory for cross-tenant leakage, Art. 73 triggers. |
| CSM on-call | `{CSM rotation}` | `{pager}` | SEV1/2 affecting Enterprise tenants. |
| FinOps on-call | `{FinOps rotation}` | `{pager}` | Mandatory for cost runaway. |
| Executive sponsor | `{exec rotation}` | `{pager}` | SEV1; press inquiry; Art. 73 trigger. |

## 2. Timed phases

| Phase | SEV1 | SEV2 | SEV3 | SEV4 |
|-------|------|------|------|------|
| Triage | 5 min | 15 min | 1 h | NBD |
| First containment action | 30 min | 1 h | 4 h | sprint |
| Customer comms initial | 15 min | 30 min | 4 h | release notes only |
| Investigation start | 30 min | 1 h | 1 d | sprint |
| Mitigation target | 1-4 h | 4-24 h | 1-5 d | sprint |
| Postmortem published | 5 BD | 10 BD | optional | none |

## 3. Classification decision tree

See `ai-incident-classification-decision-tree.md`.

## 4. Per-failure-class procedures

### 4.1 Hallucination spike

| Field | Value |
|-------|-------|
| Detection signal | Hallucination SLO burn-rate alert (`{alert name}`); customer flag-button rate >= 3x baseline in 1 h; press / social mention |
| First five steps | (1) Open dashboard `{dashboard url}`. (2) Confirm factuality / citation SLI drop on production sample. (3) Classify severity per matrix. (4) Page AI lead + IC. (5) Open incident channel. |
| Containment (default) | Prompt rollback to last green tag (4.b.3); if rollback ineffective in 15 min, model fallback (4.b.2); if still ineffective, abstain mode (4.b.5) |
| Verification | Re-run dashboard query on a 5-min window; confirm SLI back within SLO floor |
| Evidence to preserve | trace bundle for affected requests; prompt + model + tool versions at time T; retrieval set for sampled traces; eval output for current green and current candidate; reproduce script |
| Investigation path | RCA taxonomy: model regression; prompt regression; retrieval drift; eval-drift confounder |
| Customer comms | `status-page-hallucination-spike` template + `tenant-notification-quality-issue` for affected tenants |
| Regulator trigger | High-risk feature: assess Art. 73 fundamental-rights limb at hour 2; GDPR Art. 33 unlikely unless personal data leaked |
| Resolution | 30 min sustained within-SLO operation with the durable fix applied |

### 4.2 Prompt drift / prompt regression

| Field | Value |
|-------|-------|
| Detection signal | Eval CI regression alert; canary cohort SLI drop; flag-button rate uptick on a known-recent prompt change |
| First five steps | (1) Identify candidate prompt PR. (2) Confirm regression on canary cohort. (3) Pause percentage-cohort progression per rollout runbook. (4) Page AI lead. (5) Open incident channel if customer-visible. |
| Containment | Prompt rollback to last green tag (4.b.3) |
| Verification | Eval rerun on golden set; production-sample SLI within SLO floor for 30 min |
| Evidence | candidate prompt diff; eval run id pre and post; canary metrics; sample traces with regression |
| Investigation path | RCA taxonomy: prompt-regression node; eval-drift confounder |
| Customer comms | usually internal; status-page entry only if SEV2+ |
| Regulator trigger | rarely; if customer-visible and high-risk, Art. 73 15-d assessment |
| Resolution | rollback verified + post-rollback eval green |

### 4.3 Model regression (provider rotation / deprecation)

| Field | Value |
|-------|-------|
| Detection signal | Production SLI drop without our deploy; provider deprecation email; provider status page; benchmark divergence |
| First five steps | (1) Confirm no in-house deploy at T. (2) Check provider status page and deprecation notices. (3) Confirm SLI regression. (4) Page AI lead. (5) Open incident channel. |
| Containment | Model fallback to pinned-version checkpoint or to the secondary provider (4.b.2) |
| Verification | sample call goes to fallback; SLI back within SLO floor |
| Evidence | provider notice (if any); model id pre and post; eval re-run on both checkpoints; gateway routing snapshot |
| Investigation path | RCA taxonomy: provider rotation; provider deprecation; provider price change (parallel) |
| Customer comms | status-page entry; tenant notification if SEV1/2; trust-center model-card update post-incident |
| Regulator trigger | Art. 73 assessment if the regression breaches a high-risk SLO; provider as sub-processor noted in DPA |
| Resolution | fallback held; eval green on the new pinned checkpoint; model-card updated |

### 4.4 Jailbreak / prompt injection (direct)

| Field | Value |
|-------|-------|
| Detection signal | safety-violation SLI breach; red-team escalation; customer report of policy-violating output; security alert |
| First five steps | (1) Confirm policy-violating output is reproducible. (2) Page security on-call. (3) Determine if data exfiltrated. (4) Declare SEV1 if exfiltration or fundamental-rights infringement; SEV2 otherwise. (5) Open joint incident with security IR. |
| Containment | abstain mode if confined to a feature (4.b.5); kill switch if injection vector is the feature itself (4.b.1); read-only mode if tool-use is implicated (4.b.6) |
| Verification | Re-run the jailbreak prompts; confirm refusal / abstain |
| Evidence | full prompt + completion; tenant id; user id; trace; security investigation handoff per IR-Security |
| Investigation path | RCA taxonomy: input-filter gap; system-prompt regression; model behaviour change; tool-scope misconfig |
| Customer comms | SEV1: per-tenant notification within 15 min if data exfil; status page if platform-wide |
| Regulator trigger | GDPR Art. 33 if personal data exfiltrated (72 h); EU AI Act Art. 73 fundamental-rights limb (2 d) if high-risk feature |
| Resolution | input-filter fix + red-team smoke green + eval green |

### 4.5 Jailbreak / prompt injection (indirect — via retrieval or tool)

| Field | Value |
|-------|-------|
| Detection signal | unexpected agent action; output containing instructions clearly from a retrieved document; tool-call audit anomaly |
| First five steps | (1) Confirm injection source (retrieved doc, tool output, user upload). (2) Page security + AI lead. (3) Determine blast radius (which tenants ingested the poisoned content). (4) Declare SEV1 if irreversible action taken. (5) Open joint incident with security IR. |
| Containment | read-only mode (4.b.6) immediately; index pinning (4.b.4) to halt re-ingestion; abstain mode for affected workflows (4.b.5) |
| Verification | confirm no further unauthorised tool calls; confirm index frozen |
| Evidence | the poisoning document or tool response; ingestion trace; agent trace + tool-call log; affected-tenant list |
| Investigation path | RCA taxonomy: retrieval-poison; tool-scope expansion; agent-instruction parsing |
| Customer comms | tenant notification for affected tenants; status-page entry |
| Regulator trigger | GDPR Art. 33 if data exfiltrated; EU AI Act Art. 73 fundamental-rights or property limb depending on action |
| Resolution | poisoning vector remediated; index re-built from known-good source; red-team smoke green |

### 4.6 Tool-chain failure

| Field | Value |
|-------|-------|
| Detection signal | tool-error rate spike; agent loop alert; partial-execution audit anomaly |
| First five steps | (1) Identify failing tool. (2) Check tool vendor status. (3) Confirm whether any partial-execution left tenant state inconsistent. (4) Page AI lead + SRE. (5) Page security if scope changed. |
| Containment | read-only mode (4.b.6) for the affected tool; agent halt for affected workflows; abstain mode (4.b.5) |
| Verification | no further agent calls reach the failing tool |
| Evidence | tool-call log; vendor status snapshot; partial-execution audit trail; affected-tenant list |
| Investigation path | RCA taxonomy: tool API change; tool schema change; vendor outage; tool-scope expansion |
| Customer comms | tenant notification per affected workflow; status-page entry if multi-tenant |
| Regulator trigger | Art. 73 only if irreversible side effect; GDPR Art. 33 if leakage |
| Resolution | tool patched / vendor restored; partial-execution reconciliation complete |

### 4.7 Cost runaway

| Field | Value |
|-------|-------|
| Detection signal | cost-anomaly alert (2x baseline / 1 h or per cost-runbook thresholds) |
| First five steps | (1) Identify the tenant(s) and feature. (2) Determine if abuse, misconfig, or prompt regression. (3) Apply per-tenant throttle per cost runbook. (4) Page FinOps + AI lead. (5) Page security if abuse suspected. |
| Containment | per-tenant throttle (cost-runbook procedure); model fallback to cheaper-tier (4.b.2); abstain mode for that tenant if 5x baseline (4.b.5) |
| Verification | spend rate within 1.2x baseline for 30 min |
| Evidence | per-tenant cost trace; prompt and traffic distribution; rate of tool invocations; price-table snapshot |
| Investigation path | RCA taxonomy: prompt-regression (retry storm); abuse; misconfig; vendor price change |
| Customer comms | tenant admin notification immediately on throttle; status-page if platform-wide |
| Regulator trigger | typically none; if cascade into critical infra service, Art. 73 |
| Resolution | spend back at baseline + durable fix (prompt patch, abuse block, rate limit) |

### 4.8 Agent-action incident (autonomous side-effect misfire)

| Field | Value |
|-------|-------|
| Detection signal | customer report; tool-call audit anomaly; downstream system alert (CRM, billing, mail server) |
| First five steps | (1) Identify the action(s) taken. (2) Determine reversibility per action. (3) Identify affected records / recipients. (4) Page IC + AI lead + security + legal/DPO. (5) Engage CSM for affected tenants. Declare SEV1 if irreversible. |
| Containment | read-only mode immediately (4.b.6); kill switch on the feature (4.b.1); freeze any related background jobs |
| Verification | no further agent writes occur; manual confirmation from downstream system |
| Evidence | agent trace; tool-call log with arguments and responses; affected-record IDs; affected-recipient list; chain-of-custody for the trace |
| Investigation path | RCA taxonomy: tool-scope expansion; indirect injection; model behaviour change; missing human-in-loop gate |
| Customer comms | per-tenant notification within 30 min; executive comms for Enterprise; press-statement readiness for SEV1 |
| Regulator trigger | EU AI Act Art. 73: death/serious harm (10 d, immediate if wide-scale); fundamental rights (2 d); property/environment (15 d). GDPR Art. 33 (72 h) if personal data involved. Notify within fastest applicable window. |
| Resolution | side effects reversed where possible; durable fix; red-team smoke green; rollback rehearsal recorded |

### 4.9 Training-data / distribution shift

| Field | Value |
|-------|-------|
| Detection signal | production factuality SLI drops while eval-set factuality is stable; new traffic segment underperforms |
| First five steps | (1) Confirm divergence between production and eval distributions. (2) Identify the drifted segment. (3) Pause GA for the affected segment (rollback to previous prompt for that segment). (4) Page AI lead. (5) Open incident channel. |
| Containment | per-segment abstain mode (4.b.5); per-segment prompt rollback (4.b.3); fallback model for that segment |
| Verification | production SLI on the affected segment within SLO floor |
| Evidence | segment-level traces; eval-vs-production divergence report; data-distribution snapshot |
| Investigation path | RCA taxonomy: data shift; eval set rot; missing eval coverage for segment |
| Customer comms | usually internal; tenant comms if segment is identifiable |
| Regulator trigger | Art. 73 if high-risk and discriminatory outcome confirmed |
| Resolution | eval coverage extended to the segment; durable fix; eval green on extended set |

### 4.10 Retrieval drift

| Field | Value |
|-------|-------|
| Detection signal | citation-accuracy SLI drop; retrieval ranking divergence on canonical queries; embedding-model upgrade flag |
| First five steps | (1) Confirm citation accuracy drop on production sample. (2) Identify the index event (rebuild, embedding-model swap, source change). (3) Page AI lead. (4) Declare severity per matrix. (5) Open incident channel. |
| Containment | index pinning to last-known-good snapshot (4.b.4); freeze re-indexing; if necessary, abstain on RAG outputs (4.b.5) |
| Verification | citation accuracy on production sample back within SLO floor |
| Evidence | index id pre and post; embedding-model id pre and post; retrieval set for sampled queries; citation-accuracy run |
| Investigation path | RCA taxonomy: index drift; embedding-model change; source-schema change; citation drift |
| Customer comms | status-page entry if SEV2+; tenant notification if cross-tenant content surfaces |
| Regulator trigger | EU AI Act Art. 73 fundamental-rights (2 d) if cross-tenant content leaked; GDPR Art. 33 (72 h) if personal data leaked |
| Resolution | index re-built / re-pinned; citation accuracy held within SLO 24 h |

### 4.11 Eval drift

| Field | Value |
|-------|-------|
| Detection signal | eval green but production red; judge-LLM calibration drift; discovery of golden-set leakage or rot |
| First five steps | (1) Confirm eval-vs-production divergence. (2) Identify whether eval-drift is the cause or a contributing factor. (3) Freeze any releases gated only by the suspect eval. (4) Page AI lead. (5) Open incident channel. |
| Containment | release freeze; revert any release deployed in the past N days that depended on the suspect eval gate |
| Verification | eval re-run on a known-clean golden set; production SLI alignment |
| Evidence | eval run history; judge-LLM version pre and post; golden-set diff; calibration-set scores |
| Investigation path | RCA taxonomy: golden-set rot; judge drift; test-set leakage; missing-eval-coverage |
| Customer comms | usually internal; tenant comms if a release based on the bad eval shipped customer-visible regression |
| Regulator trigger | rare; if a downstream incident triggered, follow that incident's clock |
| Resolution | eval rebuilt; calibration re-baselined; release gates re-armed |

## 4.b Containment-mode procedures

Each is runnable by an on-call engineer with no AI specialisation.

### 4.b.1 Kill switch

| Field | Value |
|-------|-------|
| What it does | disables the AI feature for all tenants; UI shows abstain or "feature unavailable" |
| System | `{feature-flag system}` |
| Flag name | `{flag.ai_feature.enabled}` |
| Command (disable) | `{cli command or UI path}` |
| Command (rollback) | `{cli command or UI path}` |
| Verification | call the feature endpoint; expect "feature unavailable" payload |
| Blast radius | entire feature, all tenants |
| Authority to invoke | SEV1: IC. SEV2+: AI lead. |
| Logging | flag-system audit log; incident timeline entry |

### 4.b.2 Model fallback

| Field | Value |
|-------|-------|
| What it does | routes generation calls from the primary model to the fallback model (per the model-fallback ladder in the cost runbook) |
| System | `{LLM gateway}` |
| Config key | `{gateway.model.primary -> fallback}` |
| Command | `{cli command}` |
| Rollback | revert config key |
| Verification | sample call; response metadata names the fallback model |
| Blast radius | one feature route or all generation calls |
| Authority | AI lead or SRE on-call |
| Logging | gateway audit log; eval rerun expected within 1 h |

### 4.b.3 Prompt rollback

| Field | Value |
|-------|-------|
| What it does | pins the prompt-registry tag to the last known-green tag for the affected feature |
| System | `{prompt registry}` |
| Command (list tags) | `{cli command}` |
| Command (pin tag) | `{cli command}` |
| Rollback | re-pin to current tag |
| Verification | call the feature; trace shows pinned tag id |
| Blast radius | one feature; can be scoped per cohort / per tenant if registry supports |
| Authority | AI lead |
| Logging | prompt-registry audit log; incident timeline; ADR if persistent |

### 4.b.4 Index pinning

| Field | Value |
|-------|-------|
| What it does | freezes the retrieval index at the last known-good snapshot; halts re-ingestion jobs |
| System | `{vector store / search index}` |
| Snapshot id (last known good) | `{snapshot id}` |
| Command (pin) | `{cli command}` |
| Command (halt ingestion) | `{job-system command}` |
| Rollback | unpin + resume ingestion |
| Verification | sample retrieval query; results match expected ranking for canonical query set |
| Blast radius | one index / one feature |
| Authority | AI lead |
| Logging | search-system audit log; incident timeline |

### 4.b.5 Abstain mode

| Field | Value |
|-------|-------|
| What it does | switches the feature to return a deterministic abstain payload + UI copy explaining the situation |
| System | `{feature-flag system}` |
| Flag name | `{flag.ai_feature.abstain_mode}` |
| Command (enable) | `{cli command}` |
| Rollback | disable flag |
| User-facing copy (ships with abstain) | `{configurable copy}` per `ai-incident-status-page-templates.md` |
| Verification | call the feature; response is the abstain payload; UI shows the copy |
| Blast radius | one feature; can be scoped per cohort / per tenant |
| Authority | AI lead |
| Logging | flag-system audit log; incident timeline |

### 4.b.6 Read-only mode

| Field | Value |
|-------|-------|
| What it does | disables every tool that writes (sends mail, mutates records, modifies files); AI can read and recommend but not act |
| System | `{agent tool registry}` |
| Commands (per write-tool) | `{cli command per tool}` |
| Rollback (per tool) | `{cli command per tool}` |
| Verification | invoke an agent that would normally write; trace shows no write tool was called; user-facing copy explains |
| Blast radius | all agentic workflows |
| Authority | AI lead; SEV1 mandatory if agent-action incident |
| Logging | tool-registry audit log; incident timeline |

## 5. Handoff rules

- Security on-call leads from the moment a confirmed injection or exfiltration is in scope.
- DPO/legal leads from the moment cross-tenant leakage is confirmed.
- FinOps leads from the moment cost runaway is the primary failure class.
- Shift rotation: SEV1 incidents lasting > 4 h trigger relief rotation; the relieved IC writes a handoff note in the incident channel.

## 6. Joint-incident protocol with SaaS incident process

- SaaS IR leads on availability and data corruption.
- AI IR leads on quality and autonomy.
- Security IR leads on confidentiality, injection, exfiltration.
- One overall IC; specialised leads underneath. The IC decides which clock starts first (Art. 73 / Art. 33 / state-level / African) and is responsible for notifying legal/DPO.

## 7. Cross-refs

- Severity matrix: `06-deployment-operations/13-ai-incident-severity-matrix`.
- RCA taxonomy: `06-deployment-operations/15-ai-rca-taxonomy-doc`.
- Postmortem template: `06-deployment-operations/16-ai-incident-postmortem-template`.
- Evidence pack spec: `06-deployment-operations/17-ai-incident-evidence-pack-spec`.
- Customer comms: `06-deployment-operations/18-ai-incident-customer-comms-templates`.
- Drill / game-day: `06-deployment-operations/19-ai-incident-drill-and-game-day-spec`.
- Regulator notification: `09-governance-compliance/18-ai-regulator-incident-notification-doc`.
- Parent SaaS IR: `06-deployment-operations/09-saas-incident-response-and-postmortem`.
- Cost runbook: `06-deployment-operations/12-ai-cost-runbook`.
- Rollout runbook: `06-deployment-operations/11-ai-feature-rollout-runbook`.
- Hallucination SLO: `06-deployment-operations/10-ai-hallucination-slo-doc`.
- Software-dev engine handoff: kill-switch code, model-fallback router, prompt-registry tooling, index-pin tooling, abstain-payload library, tool-registry disable code are owned by the parallel software-dev pass.
