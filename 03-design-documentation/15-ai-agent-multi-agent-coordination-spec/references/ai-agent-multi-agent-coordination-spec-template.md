# Multi-Agent Coordination Spec Template

## 1. Topology Verdict

| Feature | Topology | Drivers | Rejected alternatives |
|---------|----------|---------|------------------------|
| Research-and-summarise agent | supervisor-worker | task decomposes into retrieve + summarise + verify | single-agent rejected: factuality below threshold without verifier |
| Numeric verification agent | debate (2 agents) | adversarial cross-check improves numeric correctness | single-agent rejected: hallucinated arithmetic |
| Onboarding flow agent | handoff chain | sequential phases | supervisor-worker rejected: phases are inherently sequential, supervision overhead unjustified |

## 2. Agent Inventory & Roles

### Research-and-summarise agent

| Role | Action-catalogue subset | Memory tiers | Planner template | Termination |
|------|-------------------------|--------------|------------------|-------------|
| Supervisor | none — coordinates only | scratchpad + episodic (read) | `planner-supervisor-v1` | when all workers report `done` or budget exhausted |
| Retriever | `search.execute`, `doc.fetch` (idempotent) | scratchpad | `planner-retriever-v1` | when retrieval count >= N OR confidence >= 0.8 |
| Drafter | `none` (text-only) | scratchpad | `planner-drafter-v1` | when draft passes self-rubric |
| Verifier | `search.execute` (factuality cross-check) | scratchpad | `planner-verifier-v1` | when every claim is supported OR three rounds exhausted |

## 3. Scratchpad Isolation

- Each role's scratchpad keyed `(tenant_id, agent_run_id, agent_role)`.
- Workers cannot read each other's scratchpad.
- Cross-role context is passed via explicit handoff messages on the message bus.
- Supervisor may read all worker scratchpads (read-only).

## 4. Supervision Policy

- Default: **review-after-act** with sample-review at 20% for non-irreversible workers.
- Override: **review-before-act** for any worker plan containing an irreversible tool, regardless of feature default.
- Escalation: any worker that returns abstain three times in a row is paused; supervisor escalates to HITL.

## 5. Message-Bus Contract

```yaml
type: object
required: [from_role, to_role, agent_run_id, payload, handoff_token]
properties:
  from_role:      { type: string }
  to_role:        { type: string }
  agent_run_id:   { type: string }
  payload:        { type: object }
  handoff_token:  { type: string }
  ts:             { type: string, format: date-time }
```

- `handoff_token` is issued by the supervisor; signed; valid for one consumption.
- Bus: Redis Streams partitioned by `tenant_id`.

## 6. Failure-Mode Handling

| Failure | Handling |
|---------|----------|
| Worker exceeds budget | supervisor aborts the worker; run continues with reduced scope OR terminates with `completed-failed` |
| Worker emits malformed handoff | supervisor rejects with one retry; second failure aborts the role |
| Debate fails to converge in 3 rounds | terminate; emit abstain payload `reason=ambiguous-goal` |
| Supervisor crashes | orchestrator re-elects supervisor from the durable state; resume SLA <= 30 s |
| Worker proposes irreversible tool without approval | dispatcher refuses; supervisor reviews; the worker is paused for the run |

## 7. ADR Seeds

| ADR | Topic |
|-----|-------|
| ADR-AGT-MA-001 | Multi-agent topology per feature |
| ADR-AGT-MA-002 | Supervision policy per feature |
| ADR-AGT-MA-003 | Message-bus technology |
| ADR-AGT-MA-004 | Debate round cap |

## 8. Traceability

| Feature | FR refs | Topology | ADR refs |
|---------|----------|----------|-----------|
| Research-and-summarise | AFR-RES-001 | supervisor-worker | ADR-AGT-MA-001..003 |
| Numeric verification | AFR-VER-001 | debate (2) | ADR-AGT-MA-001, 004 |
| Onboarding flow | AFR-OBD-001 | handoff chain | ADR-AGT-MA-001 |
