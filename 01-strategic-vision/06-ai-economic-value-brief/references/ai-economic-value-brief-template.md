# AI Economic Value Brief Template

## 1. Business Outcome

- Target metric (measurable):
- Current baseline (with measurement window):
- Desired improvement (% or absolute, with timeframe):
- Economic value per period (revenue uplift / cost saved / risk reduced, in currency):
- Stakeholders signing off the outcome:

## 2. Users and Workflow

- Users affected (roles, volumes):
- Current workflow (steps, latency, error rate, cost):
- AI-assisted workflow (steps after AI insertion):
- Decision or action the AI changes:
- Human-in-the-loop points retained:

## 3. AI Pattern

- Recommended pattern: { simple LLM call | RAG | deterministic-with-LLM-extraction | classical ML | agent | fine-tune }
- Why this pattern (3-5 reasons tied to risk / cost / latency / accuracy):
- Rejected alternatives and why:
- Model class (general-purpose / specialised / on-prem / hosted):

## 4. Data and Integration

- Data sources (system, owner, format, freshness):
- Data quality risks:
- Privacy classification (PII / SPI / business-confidential / public):
- Tenant-isolation rule (shared embeddings allowed? cross-tenant retrieval forbidden?):
- Required integrations (system, mode, SLA):

## 5. Evaluation and Acceptance

| Gate | Metric | Threshold | Source |
|------|--------|-----------|--------|
| Golden case pass rate | % | >= 95 | eval harness |
| Adversarial case pass rate | % | >= 90 | red-team harness |
| Citation accuracy (RAG) | % | >= 90 | judge-LLM + spot audit |
| Abstention precision | % | >= 80 | eval harness |
| Cost per call ceiling | USD | <= 0.05 | model gateway meter |
| Latency P95 | ms | <= 2000 | APM |
| Rollback trigger | n/a | breach > 24 h | SLO doc |

## 6. Operations

- Human approval points (which steps require sign-off):
- Monitoring signals (token use, latency, fallback rate, abstention rate, citation rate, judge-LLM drift):
- Operating owner (named role):
- Maintenance cadence (eval re-run frequency, prompt-registry review):
- Incident escalation path:

## 7. Roadmap

| Stage | Scope | Exit criteria | Target date |
|-------|-------|---------------|-------------|
| Prototype | offline notebook on golden set | golden >= 95% | |
| Pilot | one tenant cohort, opt-in | red-team pass, SLO met for 14 d | |
| Production | full rollout | full DoD, eval CI gate green | |
| Scale | additional locales / verticals | per-locale eval pass | |

## 8. Risk Register Excerpt

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|------------|-------|
| Hallucination on regulated content | M | H | citation gate + abstain rule + human approval | |
| Cost runaway on per-tenant abuse | M | M | per-tenant ceiling + throttle | |
| Prompt injection from third-party content | H | H | content sanitisation + sandboxed tools | |
| Cross-tenant leak via embeddings | L | H | per-tenant index segregation + isolation evidence | |
| Model provider outage | M | M | fallback model + cached responses | |

## 9. References

- AI Feature Strategy Doc (`01-strategic-vision/13-ai-feature-strategy-doc`)
- AI Feature PRD Spec (`02-requirements-engineering/14-ai-feature-prd-spec`)
- AI Architecture Spec (`03-design-documentation/11-ai-architecture-spec`)
- AI Eval Harness Spec (`05-testing-documentation/04-ai-eval-harness-spec`)
- AI Hallucination SLO Doc (`06-deployment-operations/10-ai-hallucination-slo-doc`)
