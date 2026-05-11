# AI Incident Severity Matrix Template

## 1. Dimensions

| Dimension | Values |
|-----------|--------|
| Severity | SEV1 / SEV2 / SEV3 / SEV4 |
| Tenant scope | single tenant / tenant cohort / platform-wide / cross-tenant leakage |
| Autonomy / blast-radius | advisory / assistive / autonomous-with-rollback / autonomous-irreversible |

Cross-tenant leakage is a distinct tenant-scope value because it carries GDPR Art. 33 and (if high-risk) EU AI Act Art. 73 obligations regardless of how few tenants are touched.

## 2. Per-failure-class thresholds

| Failure class | SEV1 | SEV2 | SEV3 | SEV4 |
|---------------|------|------|------|------|
| Hallucination spike | factuality drop >= 10 pp in 1 h on production sample; or >= 5 pp with safety-relevant content | factuality drop 5-10 pp in 1 h | factuality drop 2-5 pp in 24 h | < 2 pp; eval-only |
| Prompt drift / prompt regression | regression triggers cross-tenant leakage or unauthorised action; or breaches abstention recall SLO | citation accuracy drop > 5 pp in 24 h | minor prompt regression caught in canary | n/a |
| Model regression (provider rotation) | provider rotates checkpoint silently AND factuality or safety SLO breaches | provider rotation AND latency SLO breach | provider notifies upcoming deprecation with > 30 d notice | n/a |
| Jailbreak / prompt injection | confirmed exfiltration of customer data; or unauthorised action emitted; or fundamental-rights infringement | confirmed jailbreak yielding policy-violating output without data exfiltration | jailbreak attempt detected and blocked | research red-team finding |
| Tool-chain failure | autonomous-irreversible action misfires due to tool change; or tool exfiltrates data | agent loops or fails partial-execution leaving tenant state inconsistent | tool API change degrades feature but no state corruption | minor tool latency |
| Cost runaway | spend > 5x baseline platform-wide for 1 h; or > 10x for any tenant for 15 min | spend > 3x baseline platform-wide for 1 h | spend > 2x baseline for a tenant for 1 h | minor variance within ceiling |
| Agent-action incident | autonomous-irreversible action took an unauthorised side effect (wrong record, wrong recipient, wrong file) | autonomous-with-rollback action misfired but rolled back cleanly | assistive recommendation was wrong but human-in-loop caught it | advisory wrong output |
| Training-data shift / distribution shift | production factuality < SLO floor on > 25% of traffic | production factuality < SLO floor on 5-25% of traffic | < 5% of traffic | n/a |
| Retrieval drift | citation accuracy < SLO on production traffic; or retrieval surfaces cross-tenant content | citation accuracy drop > 5 pp in 24 h | retrieval ranking drifted but citation accuracy within SLO | minor ranking change |
| Eval drift | golden-set leakage discovered AND a release went live based on the contaminated eval | judge-LLM drift > 5 pp on calibration set | golden-set rot detected pre-release | minor calibration slip |

## 3. SLA service-credit mapping

| Severity | Free | Pro | Enterprise |
|----------|------|-----|------------|
| SEV1 (AI feature unavailable) | none | 10% monthly fee credit | 25% monthly fee credit |
| SEV1 (cross-tenant leakage) | account credits per DPA | per DPA + breach support | per DPA + breach support + executive briefing |
| SEV2 | none | 5% credit | 10% credit |
| SEV3 | none | none | none (status-page entry only) |
| SEV4 | none | none | none |

Numerical factuality is not a contracted SLA dimension (per the Hallucination SLO doc); availability and confidentiality are.

## 4. EU AI Act Article 73 mapping

| AI failure class | Art. 73 limb potentially triggered | Reporting window |
|------------------|------------------------------------|-------------------|
| Agent-action incident (irreversible) on a high-risk system | death/serious harm; property/environment; fundamental rights | immediate, not later than 10 d for death/serious harm; 2 d for wide-scale or fundamental rights; 15 d otherwise |
| Jailbreak/injection causing data exfiltration on a high-risk system | fundamental rights (privacy) | 2 d |
| Hallucination spike on a high-risk decision-support system | fundamental rights (non-discrimination, due process) where verified | 15 d |
| Model regression on a high-risk system breaching SLO | fundamental rights if discriminatory output | 15 d |
| Retrieval drift surfacing cross-tenant content on a high-risk system | fundamental rights (privacy) | 2 d |
| Cost runaway | typically not Art. 73 unless it cascades into critical-infrastructure disruption | n/a unless cascade |
| Eval drift | only if a downstream incident materialised; track separately | dependent |

For non-high-risk features (limited-risk, minimal-risk) Art. 73 does not apply, but GDPR Art. 33 (72 h personal-data breach) may; cross-link to the regulator-notification skill.

## 5. Elevation and de-escalation rules

- **Elevate** when: new evidence of cross-tenant leakage; confirmed autonomous-irreversible side effect; regulator inquiry opened; press inquiry on the incident.
- **De-escalate** when: confirmed bounded blast radius; abstain-mode or read-only-mode active and effective; mitigations applied and held for 30 min with no further degradation.
- Severity changes are logged with timestamp, incident-commander id, and one-line justification in the incident timeline.

## 6. Cross-refs

- `06-deployment-operations/09-saas-incident-response-and-postmortem` — SaaS severity baseline.
- `06-deployment-operations/14-ai-incident-response-runbook` — playbook keyed to this matrix.
- `06-deployment-operations/17-ai-incident-evidence-pack-spec` — evidence per severity.
- `06-deployment-operations/18-ai-incident-customer-comms-templates` — comms per severity.
- `09-governance-compliance/18-ai-regulator-incident-notification-doc` — Art. 73 and GDPR Art. 33 reporting.
