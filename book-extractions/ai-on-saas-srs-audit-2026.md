# AI-on-SaaS SDLC-Docs Skills Audit — May 2026

This audit extends the SaaS-on-SDLC pass (see `saas-srs-skills-audit-2026.md`) with the documentation stack required when a SaaS product ships AI features — RAG pipelines, agentic workflows, copilots, summarisation, classification, ranking, or any LLM-powered feature — inside a multi-tenant boundary. It contrasts the engine against the deliverables an enterprise AI-buying customer, an AI auditor (EU AI Act, US sectoral, emerging African AI guidelines), and an internal Responsible-AI committee will demand, and emits the new skill stack.

Convention: skill IDs follow the existing numbered pattern inside each phase. New skill numbering continues from the next free slot per phase. All new skills are prefixed with `ai-` after the numeric prefix so they are discoverable as the AI-feature family.

## Summary of new artefacts created this session

- **New skills (13):** see "New skills" table below — one per phase gap.
- **Enhanced skills (8):** AI-feature addendums added to existing PRD, HLD, coding-guidelines, test-strategy, monitoring, DoD, ADR-catalogue, and the recent SaaS-pricing / billing / isolation / trust-center / DPA skills.
- **Cross-cutting templates (11):** model-card, eval-harness, red-team plan, hallucination SLO, rollout runbook, cost runbook, responsible-AI declaration, DPIA addendum, prompt-registry, ADR seed pack, data-flow conventions.

---

## Why this is a separate pass from the SaaS pass

The previous SaaS pass intentionally deferred AI-feature documentation because LLM-powered features add risk surfaces that no generic SaaS doc captures:

1. **Non-determinism** — same prompt, different outputs. Test plans, DoD, SLOs, and acceptance criteria must accommodate distributional pass/fail.
2. **Hallucination as a first-class failure mode** — needs its own SLI/SLO, error budget, and rollback rule.
3. **Prompt injection / jailbreak** — a new threat class that does not appear in OWASP Top 10 application-security frameworks until OWASP LLM Top 10 (2023+).
4. **Cross-tenant data leakage via embeddings, conversation logs, fine-tunes, and shared model context** — requires its own isolation evidence beyond the database-level isolation pack.
5. **Model provider as a sub-processor with training-data implications** — DPA, sub-processor list, training-data opt-out, retention all change.
6. **EU AI Act + emerging US/African AI regulation** — explicit tiering (prohibited / high-risk / limited-risk / minimal-risk) and disclosure obligations that no SaaS-trust-center template encodes.
7. **Per-call cost variability** — token-priced calls make per-tenant cost runaway a real operational risk that needs its own runbook, distinct from generic FinOps.
8. **Eval as CI gate** — "tests pass" is no longer "tests are green on a deterministic input"; it is "the golden dataset regression stayed within tolerance and the judge-LLM grade did not drop." This is a categorically new development artefact.

The SaaS pass produced multi-tenancy, SLO, error-budget, billing/metering, trust-center, DPA. This pass layers AI-distinctive viewpoints on top.

---

## Phase 01 — Strategic Vision

### Gaps the AI-feature reality reveals

| # | Gap | Source |
|---|-----|--------|
| 1 | No AI feature strategy at the product level — what AI features ship in what tier, which are build vs buy, which are moat | Industry practice; Anthropic / OpenAI enterprise-buyer questionnaires |
| 2 | PRD has no AI-feature addendum — hallucination tolerance, latency budget, cost ceiling, abstain criteria, citation policy are absent | OWASP LLM Top 10; NIST AI RMF |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `13-ai-feature-strategy-doc` | `01-strategic-vision/13-ai-feature-strategy-doc/` | AI feature inventory by tier; build-vs-buy on models; AI moat analysis; differentiating-vs-table-stakes split |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `01-prd-generation` | `references/ai-feature-prd-addendum.md` — every AI-powered FR adds hallucination tolerance, latency budget, $/call ceiling, abstain criteria, citation policy, consent/opt-in, training-data exclusion |
| `12-saas-pricing-and-packaging-spec` | AI-feature-tier guidance appended in references |

---

## Phase 02 — Requirements Engineering

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No AI-feature PRD spec (formal requirements clauses, IEEE 830 form) | NIST AI RMF GOVERN-1 |
| 2 | No data-and-knowledge-base spec — what feeds the model, per-tenant vs shared, ingestion SLA, retention, freshness, lineage | OWASP LLM06; ISO/IEC 42001 |
| 3 | No AI-feature billing event additions to metering spec | Snowflake / OpenAI usage-based-pricing playbooks |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `14-ai-feature-prd-spec` | `02-requirements-engineering/14-ai-feature-prd-spec/` | IEEE-form AI-feature requirements: inputs, outputs, hallucination tolerance, latency, cost ceiling, abstain rules, citation policy, training/eval data sources, consent |
| `15-ai-data-and-knowledge-base-spec` | `02-requirements-engineering/15-ai-data-and-knowledge-base-spec/` | Knowledge sources, per-tenant vs shared, ingestion SLA, freshness, retention, lineage, training-data exclusion |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `13-saas-billing-and-metering-spec` | AI usage-metering event family added to references |

---

## Phase 03 — Design Documentation

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No AI architecture spec (RAG vs fine-tune vs agent; model gateway; vector store; eval harness; observability; security boundaries) | Sequoia, a16z LLM-architecture references; OWASP LLM Top 10 |
| 2 | No model card per deployed model / per AI feature | Mitchell et al. (2019) Model Cards; EU AI Act Annex IV |
| 3 | No prompt and system-message spec — versioned prompt registry, change control, regression-test attachment | Anthropic prompt-engineering guide; OWASP LLM01 (prompt injection) |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `11-ai-architecture-spec` | `03-design-documentation/11-ai-architecture-spec/` | RAG/agent/fine-tune decision, model gateway, vector store, eval harness, observability, security boundaries |
| `12-ai-model-card` | `03-design-documentation/12-ai-model-card/` | Per-deployed-feature model card: purpose, training data summary, eval metrics, limitations, bias notes, intended use, out-of-scope use, version |
| `13-ai-prompt-and-system-message-spec` | `03-design-documentation/13-ai-prompt-and-system-message-spec/` | Versioned prompt registry, change-control, regression-test attachment |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `01-high-level-design` | `references/ai-hld-mode.md` — when the HLD covers AI features, the addendum lists the additional viewpoints required (model gateway, eval harness, vector store, hallucination SLO) |

---

## Phase 04 — Development Artifacts

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | Coding guidelines do not cover prompt-injection-safe coding, structured-output enforcement, non-determinism handling, tenant-context propagation through LLM calls | OWASP LLM Top 10; LangChain / Anthropic guidance |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `02-coding-guidelines` | `references/ai-coding-guidelines-addendum.md` — prompt-injection-safe coding, deterministic-output enforcement, structured output, non-determinism handling, tenant-context propagation through LLM calls |

---

## Phase 05 — Testing Documentation

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No AI eval harness spec (golden datasets, regression criteria, A/B prompt eval, judge-LLM, CI gate) | OpenAI Evals; Anthropic eval guide; promptfoo |
| 2 | No AI red-team test plan (prompt injection, jailbreak, data exfil, cross-tenant leakage, PII surfacing, hallucination probe) | OWASP LLM Top 10; NIST AI RMF MEASURE |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `04-ai-eval-harness-spec` | `05-testing-documentation/04-ai-eval-harness-spec/` | Golden datasets per feature, regression criteria, A/B prompt eval, judge-LLM patterns, eval CI gate |
| `05-ai-red-team-test-plan` | `05-testing-documentation/05-ai-red-team-test-plan/` | Prompt injection / jailbreak / data exfil / cross-tenant leakage / PII surfacing / hallucination probe; severity matrix |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `01-test-strategy` | `references/ai-test-strategy-addendum.md` — eval harness is the new functional gate; red-team is the new security gate; non-determinism testing replaces some integration tests |

---

## Phase 06 — Deployment & Operations

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No hallucination SLI/SLO doc (citation accuracy, abstention rate, factuality score) | Google SRE applied to LLM; OpenAI eval reports |
| 2 | No AI-feature rollout runbook (staged rollout, canary cohorts, auto-rollback triggers, comms, opt-in/out handling) | Anthropic / Google production-LLM playbooks |
| 3 | No AI cost runbook (per-tenant cost monitoring, spend ceilings, anomaly response, model fallback on cost overrun) | OpenAI / Anthropic enterprise FinOps |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `10-ai-hallucination-slo-doc` | `06-deployment-operations/10-ai-hallucination-slo-doc/` | SLI/SLO for hallucination, citation accuracy, abstention; error budget; alerting; rollback rules |
| `11-ai-feature-rollout-runbook` | `06-deployment-operations/11-ai-feature-rollout-runbook/` | Staged rollout, canary cohorts, auto-rollback triggers, comms plan, opt-in/out handling |
| `12-ai-cost-runbook` | `06-deployment-operations/12-ai-cost-runbook/` | Per-tenant cost monitoring, spend ceilings, anomaly response, model-fallback policy |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `03-monitoring-setup` | `references/ai-monitoring-addendum.md` — AI-specific monitoring signals (token use, latency per model, fallback rate, abstention rate, citation rate, judge-LLM score drift) |

---

## Phase 07 — Agile Artifacts

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | DoD does not include eval-pass, red-team-pass, model-card-updated gates for AI-feature stories | Anthropic responsible-scaling-policy patterns |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `02-definition-of-done` | `references/ai-dod-addendum.md` — AI-feature DoD: eval suite passes; red-team scenarios pass; model card updated; prompt registry tag bumped; cost ceiling test passes |

---

## Phase 09 — Governance & Compliance

### Gaps

| # | Gap | Source |
|---|-----|--------|
| 1 | No responsible-AI declaration (public-facing what-AI-does / does-not / human-in-the-loop / contestability / data-use / sub-processors) | Anthropic Acceptable Use Policy; Google AI principles |
| 2 | No EU AI Act + US state AI + emerging African AI compliance doc | EU Reg 2024/1689; California SB-1001; Kenya ODPC AI guidance 2024; NDPC Nigeria advisory 2024; POPIA AI guidance ZA |
| 3 | No AI-specific DPIA addendum + data-flow with model provider as processor | EU AI Act Art. 27; GDPR Art. 35; Kenya DPA 2019 s.31 |
| 4 | No AI ADR catalogue family | engineering practice |

### New skills

| Skill | Path | Purpose |
|-------|------|---------|
| `14-ai-responsible-ai-declaration` | `09-governance-compliance/14-ai-responsible-ai-declaration/` | Public AI policy: what AI does/does not, human-in-the-loop, contestability, data use, model providers, sub-processors |
| `15-ai-act-and-regulatory-compliance-doc` | `09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/` | EU AI Act tiering, US state AI laws, sectoral rules (FCRA-AI, HIPAA-AI), African regulators (KE, NG, ZA), disclosure language |
| `16-ai-data-flow-and-dpia` | `09-governance-compliance/16-ai-data-flow-and-dpia/` | AI-specific DPIA addendum, data-flow diagram with model providers as processors, sub-processor notice, consent capture, training-data exclusion |
| `17-ai-adr-catalogue` | `09-governance-compliance/17-ai-adr-catalogue/` | Required ADRs for AI features (model choice, RAG vs fine-tune, vector store, eval threshold, abstain policy, content filter, fallback) |

### Enhancements

| Skill | What was added |
|-------|----------------|
| `05-architecture-decision-records` | `references/saas-adr-catalogue.md` extended with the AI ADR family |
| `11-saas-data-isolation-evidence-pack` | AI-isolation evidence section (embeddings, prompts, conversation logs) added in references |
| `12-saas-trust-center-document-pack` | AI sub-processor list + responsible-AI declaration link added in references |
| `13-saas-dpa-and-privacy-doc-set` | AI-specific DPA language + DPIA template added in references |

---

## Cross-cutting templates produced

| Template | Location | Purpose |
|----------|----------|---------|
| `ai-model-card-template.md` | `03-design-documentation/12-ai-model-card/references/` | Per-feature model card |
| `ai-eval-harness-spec-template.md` | `05-testing-documentation/04-ai-eval-harness-spec/references/` | Eval harness, golden dataset, judge-LLM patterns |
| `ai-red-team-test-plan-template.md` | `05-testing-documentation/05-ai-red-team-test-plan/references/` | Red-team scenarios + severity matrix |
| `ai-hallucination-slo-template.md` | `06-deployment-operations/10-ai-hallucination-slo-doc/references/` | Hallucination/citation/abstention SLI/SLO |
| `ai-rollout-runbook-template.md` | `06-deployment-operations/11-ai-feature-rollout-runbook/references/` | Canary rollout with auto-rollback |
| `ai-cost-runbook-template.md` | `06-deployment-operations/12-ai-cost-runbook/references/` | Per-tenant cost ceiling and anomaly response |
| `ai-responsible-ai-declaration-template.md` | `09-governance-compliance/14-ai-responsible-ai-declaration/references/` | Public-facing AI policy |
| `ai-dpia-addendum-template.md` | `09-governance-compliance/16-ai-data-flow-and-dpia/references/` | AI-specific DPIA + data-flow diagram conventions |
| `ai-prompt-registry-spec-template.md` | `03-design-documentation/13-ai-prompt-and-system-message-spec/references/` | Prompt registry & change-control |
| `ai-adr-templates.md` | `09-governance-compliance/17-ai-adr-catalogue/references/` | Seed ADRs every AI-feature SaaS needs |
| `ai-data-flow-diagram-conventions.md` | `09-governance-compliance/16-ai-data-flow-and-dpia/references/` | Symbols, lanes, model-provider boundary, training-data flag |

---

## Gaps still open after this pass

- **AI procurement / vendor assessment template** — when the SaaS buys a model from a third party, who fills out the security/legal/AI-act questionnaire. Recommended as a future session.
- **AI incident classification / post-mortem template** — distinct from generic incident postmortem (root cause may be prompt drift, model regression, training-data shift, jailbreak surface change). Recommended next session.
- **Fine-tune / training-job change-management spec** — when the team fine-tunes models the lineage, data manifest, and approval gate need their own artefact. Out of scope for this pass (no fine-tune assumed); flagged for future.
- **AI customer-disclosure copy** — the actual UI copy and tooltip text shown when AI is invoked. Belongs in Phase 08 user-doc. Flagged.
- **Bias / fairness evaluation deep-dive** — covered shallow in the model card; deserves its own evaluation spec, particularly for hiring / lending / housing / insurance verticals.

## Recommended next sessions

1. AI incident response & postmortem skill (Phase 06).
2. AI fine-tune / training-job change-management spec (Phase 04).
3. AI customer-disclosure UX copy pack (Phase 08).
4. Bias and fairness evaluation deep-dive (Phase 05).
5. AI procurement / vendor security questionnaire pack (Phase 09).
