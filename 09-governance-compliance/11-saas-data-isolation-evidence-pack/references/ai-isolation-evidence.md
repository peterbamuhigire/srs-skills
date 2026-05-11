# AI-Specific Isolation Evidence (addendum to Data Isolation Evidence Pack)

For SaaS with AI features, the isolation evidence pack MUST add the AI-specific surfaces below. Tenant isolation in the database is necessary but not sufficient.

## Additional evidence surfaces

| Surface | Isolation mechanism | Evidence required |
|---------|---------------------|--------------------|
| Vector store | per-tenant namespace / table + tenant-claim enforcement | schema check + sample-query forbidden-cross-tenant test results |
| Conversation log store | per-tenant partition | partition listing + cross-partition query denial test |
| Model gateway | tenant-claim mandatory; cross-tenant retrieval 403 | gateway access log + integration test result |
| Prompt registry | tags scoped to features; no per-tenant prompt unless contracted | registry config audit |
| Eval and red-team sets | separated from production retrieval indexes | store list + access policy |
| Conversation-log -> training pipeline | explicitly disabled | pipeline config + audit dates |
| Per-tenant KMS key (Enterprise) | tenant-scoped key wraps embeddings + logs | KMS key inventory + rotation log |

## Required tests (run on the standard cadence)

1. **Cross-tenant retrieval probe** — authenticate as tenant A, attempt retrieval scoped to tenant B's namespace via gateway and via direct store access. Expect 403 / zero results. Result: PASS / FAIL.
2. **Embedding similarity probe** — embed a tenant-B distinctive phrase, query tenant A's index. Expect no hits. Result: PASS / FAIL.
3. **Conversation log read probe** — attempt log read with mismatched tenant claim. Expect 403. Result: PASS / FAIL.
4. **Billing event cross-tenant probe** — attempt to read tenant B's `ai.usage.*` events as tenant A. Expect 403. Result: PASS / FAIL.
5. **Prompt-injection cross-tenant leak probe** — craft a prompt injection in tenant A's retrieved content that requests tenant-B identifiers. Expect refusal / no leak. Result: PASS / FAIL.

## Evidence artefacts to produce

- Monthly automated test run with results stored in the evidence pack.
- Quarterly manual review by Security + AI Lead.
- Annual external red-team review of AI isolation.

## Cross-links

- Multi-Tenancy Spec: `03-design-documentation/10-saas-multi-tenancy-architecture-spec/`
- AI Architecture Spec: `03-design-documentation/11-ai-architecture-spec/`
- AI Data Spec: `02-requirements-engineering/15-ai-data-and-knowledge-base-spec/`
- AI Red-Team Plan: `05-testing-documentation/05-ai-red-team-test-plan/`
