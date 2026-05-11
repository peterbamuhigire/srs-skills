# AI Agent HIPAA Security Rule Control Pack

The HIPAA Security Rule control matrix for agentic SaaS handling Protected Health Information (PHI). Enforces the admin-only constraint for clinical PHI agents.

## Output

- `AI_Agent_HIPAA_Control_Pack.md` — top-level pack.
- `hipaa-controls/<id>.md` — one file per applicable standard / implementation specification.
- `HIPAA_PHI_Touch_Classification.md` — per-feature classification.

## Admin-only constraint (critical)

A clinical PHI agent shall not act autonomously on external systems containing PHI. Every irreversible external-write tool touching PHI shall be gated by a named clinician approval event. Violation is a SEV1 incident.

## Related skills

- `09-governance-compliance/20-ai-agent-soc2-control-pack`
- `09-governance-compliance/21-ai-agent-iso27001-control-pack`
- `09-governance-compliance/23-ai-agent-compliance-policy-pack`
- `09-governance-compliance/26-ai-agent-baa-and-data-processing-language`
- `09-governance-compliance/16-ai-data-flow-and-dpia`
