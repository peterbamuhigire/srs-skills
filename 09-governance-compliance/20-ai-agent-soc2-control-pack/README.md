# AI Agent SOC 2 Control Pack

The SOC 2 control matrix for agentic SaaS. Companion to the parent SaaS SOC 2 pack — adds the agent-specific rows the auditor needs to see for each Trust Services Criterion.

## Output

- `AI_Agent_SOC2_Control_Pack.md` — the top-level pack.
- `soc2-controls/<criterion>.md` — one file per criterion (CC1.1, CC1.2, …, CC9.2, A1.1, …, P8.1).

## Relationship to software-dev pass

This skill defines **what evidence is collected, how often, and how the auditor tests it**. The parallel software-dev pass produces **the collectors and the auditor portal**. Cross-link via `ai-agent-evidence-pack-spec` and `ai-agent-evidence-frequency-table.md`.

## Related skills

- `09-governance-compliance/21-ai-agent-iso27001-control-pack`
- `09-governance-compliance/22-ai-agent-hipaa-control-pack`
- `09-governance-compliance/23-ai-agent-compliance-policy-pack`
- `09-governance-compliance/25-ai-agent-evidence-pack-spec`
- `09-governance-compliance/27-ai-agent-regulator-overlap-mapping`
- `06-deployment-operations/20-ai-agent-compliance-runbook`
