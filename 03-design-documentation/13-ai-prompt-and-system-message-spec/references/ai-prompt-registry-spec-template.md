# AI Prompt Registry Spec Template

## 1. Registry Layout

```
prompts/
  README.md                 # registry contract, ownership rules
  ai-summary/
    system.v1.2.0.md
    user.v1.2.0.md
    eval-set.v1.2.0.yaml
    CHANGELOG.md
  ai-composer/
    system.v0.9.3.md
    user.v0.9.3.md
    retrieval-wrapper.v0.9.3.md
    eval-set.v0.9.3.yaml
    CHANGELOG.md
  ai-analyst/
    system.v1.0.1.md
    user.v1.0.1.md
    retrieval-wrapper.v1.0.1.md
    judge-rubric.v1.0.1.md
    eval-set.v1.0.1.yaml
    CHANGELOG.md
  ai-agent/
    planner.v0.5.0.md
    tool-result-wrapper.v0.5.0.md
    eval-set.v0.5.0.yaml
    CHANGELOG.md
```

Each file front-matter:

```yaml
---
feature: ai-composer
artefact: system
version: 0.9.3
owner: <role / name>
last_changed: YYYY-MM-DD
last_eval: { date: YYYY-MM-DD, set: EVAL-COMP-150, pass_rate: 0.91 }
last_red_team: { date: YYYY-MM-DD, set: RT-COMP-60, pass_rate: 0.92 }
related_adr: ADR-AI-003
---
```

## 2. Change-Control Workflow

1. Open PR with the prompt diff.
2. CI runs the attached regression eval against the prompt under change.
3. CI runs the red-team smoke set.
4. Reviewers: prompt owner + AI lead + (security lead if system message changed).
5. Bump the semantic version: patch for wording, minor for behaviour, major for output-schema change.
6. Merge bumps the registry tag.
7. Gateway picks up the new tag on next request after the staged deploy.

## 3. Deploy and Rollback

- Pinning: gateway resolves `prompts/<feature>@latest-stable` to a pinned tag per environment.
- Stages: dev (auto) -> staging (bake 24 h) -> prod (manual promote).
- Rollback: re-pin to the previous tag; alarms acknowledge within 5 min.
- Alerting: factuality / judge-score drop > 3 pp triggers SEV3 to AI lead.

## 4. Secrets and PII

- No secrets, API keys, or tenant credentials in prompt files. Reviewer rejects on detection.
- Tenant identifiers are passed as guarded claims by the service, not via prompt body.
- PII redaction: pre-processor scrubs known PII patterns; redaction count logged.

## 5. Audit Hooks

- Prompt-deploy events emitted to audit log with (tag, env, deployer, prior tag).
- Quarterly review of unused tags; archive after 12 months without use.
