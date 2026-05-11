# AI Agent Evidence Pack Spec

The contract the software-dev pass's evidence collectors must satisfy. Defines what evidence is collected, how it is sampled, where it lives, how it is presented, how the auditor accesses it.

## Output

- `AI_Agent_Evidence_Pack_Spec.md`
- `AI_Agent_Attestation_Evidence_Pack_Template.md`
- `AI_Agent_Evidence_Frequency_Table.md`

## Relationship to other packs

- **Compliance evidence (this pack)** is steady-state continuous.
- **Incident evidence (06-deployment-operations/17)** is per-event, superset.
- Both are owned by AI Lead. The collector machinery is owned by the software-dev pass.

## Related skills

- `09-governance-compliance/20-ai-agent-soc2-control-pack`
- `09-governance-compliance/21-ai-agent-iso27001-control-pack`
- `09-governance-compliance/22-ai-agent-hipaa-control-pack`
- `09-governance-compliance/23-ai-agent-compliance-policy-pack`
- `06-deployment-operations/17-ai-incident-evidence-pack-spec`
- `06-deployment-operations/20-ai-agent-compliance-runbook`
