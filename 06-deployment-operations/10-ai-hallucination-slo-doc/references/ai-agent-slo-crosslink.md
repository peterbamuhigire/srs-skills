# Agent SLO Cross-Link

The AI Hallucination SLO Doc covers factuality, citation, abstention, safety violations. For agent features, the **AI Agent SLO Doc** (`06-deployment-operations/13-ai-agent-slo-doc`) adds agent-specific SLIs.

## Agent SLIs added

- Task success.
- Step efficiency.
- Intervention rate.
- **Irreversible-action-incident rate** (zero budget; SEV1 on breach; per-tenant feature kill-switch).
- Agent-task availability.
- Agent-cost-per-run.
- Tool-error rate.

## Agent-action-incident SLO

For agent features, add a row to the hallucination SLO doc that points to the agent-action-incident SLO:

```
| Feature | Agent-action incident |
|---------|------------------------|
| Inbox Triage | 0 per million runs (zero budget) |
| Daily Reconciliation | 0 per million runs (zero budget) |
```

## Customer commitments

For agent features, commitments add:

- Agent-task availability (numeric).
- 24 h notification of any irreversible-action incident.
- "Performed by agent" notification standard.
- Right to request human handling.

These additions are captured in `13-ai-agent-slo-doc` and do not change the hallucination SLO commitments.
