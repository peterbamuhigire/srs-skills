# Agent Security And Oversight Requirements

Parent skill: [16-ai-agent-feature-prd-spec](../SKILL.md). Load when an agent FR
reads untrusted content, calls tools, holds memory, talks to other agents, or
takes actions that a human must be able to stop. This file states WHAT must be
true and how it is verified; HOW to build it belongs to the engineering engine
(`chwezi-dev-engine`: `ai-security`, `ai-agent-tooling-and-hitl`,
`ai-agent-governance-and-limits`).

## 1. Writing rules for these requirements

- Each statement is one verifiable obligation with a subject, a condition and
  an observable result. Use "shall".
- Never write a requirement that the model "shall not follow malicious
  instructions". Models cannot be required to be incorruptible; the system can
  be required to make corruption harmless. Write the requirement on the system
  boundary instead.
- Every requirement names its verification method (test, inspection, analysis,
  demonstration) and the evidence artefact.
- Thresholds come from the project's risk owner and eval data. Where none
  exists, write `TBD-owner` and block baseline sign-off; do not invent numbers.

## 2. Requirement patterns with acceptance criteria

IDs use `ASR-` (agent security requirement) and `AOR-` (agent oversight
requirement). Map each to the OWASP identifiers shown (LLM Top 10 2026 and Agentic Top 10 2026) so
reviewers can check coverage.

| ID pattern | Requirement template | Acceptance criterion | Maps to |
|---|---|---|---|
| ASR-SCOPE | The agent shall be able to invoke only the actions listed for FR `<id>` in the action catalogue. | Inspection of the deployed tool manifest equals the catalogue rows; a test call to any other action is refused and logged. | LLM03:2026, ASI02 |
| ASR-AUTHZ | Every agent action shall be authorised against the identity of the user on whose behalf it runs, independently of model output. | For each catalogue action, a test with a user lacking the permission results in denial, with the policy rule ID recorded. | ASI03 |
| ASR-UNTRUSTED | Content from `<sources>` (uploads, email bodies, web pages, tool results) shall not change the agent's task scope, tool set or recipients. | Red-team set `<id>` with embedded instructions yields zero out-of-scope actions across N runs. | LLM01:2026, ASI01 |
| ASR-EGRESS | Data classified `<class>` shall leave the system only to destinations fixed by configuration, never to model-supplied destinations. | Test: coerced model output naming an external URL or number results in no transmission. | LLM02:2026, ASI02 |
| ASR-OUTPUT | Model output shall be validated against the declared schema and business rules before it is stored, rendered or executed. | Malformed and malicious outputs in test set `<id>` are rejected with a typed error; none reach the sink. | LLM10:2026 |
| ASR-CODE | The agent shall not execute model-generated code outside an isolated environment without network and credential access. | Inspection of sandbox configuration; escape test result. | ASI05 |
| ASR-MEMORY | Persistent agent memory shall be scoped per `<tenant/user>`, carry provenance, and be erasable on request within `<period>`. | Cross-scope read test fails; erasure test shows no retrieval after deletion. | ASI06, LLM08:2026, LLM09:2026 |
| ASR-SUPPLY | Tools, connectors, MCP servers, prompts and models used by the agent shall be version-pinned and change-reviewed. | Inspection of registry; a changed tool description without review fails the release check. | LLM04:2026, ASI04 |
| ASR-A2A | Messages between agents shall be authenticated and schema-validated, and the receiving agent shall re-authorise any requested action. | Test: forged or unsigned message is rejected; valid message requesting an unauthorised action is denied. | ASI07 |
| ASR-BUDGET | Each run shall stop when it exceeds `<steps>`, `<cost>` or `<time>`, preserving state and reporting the reason. | Loop and fault-injection tests stop within the limit with a recorded reason. | LLM06:2026, ASI08 |
| ASR-SECRET | No credential, key or authorisation rule shall appear in any prompt or model-visible context. | Inspection and automated scan of prompt registry and traces. | LLM08:2026 |
| AOR-APPROVE | Actions in class `<irreversible/financial/external>` shall execute only after approval by `<role>` of the exact arguments shown. | Test: modified arguments after approval are rejected; approval expires after `<period>`. | ASI09, LLM03:2026 |
| AOR-SHOW | The approval view shall show the effect, source evidence, and model-written rationale labelled as model-written. | Demonstration with usability reviewer sign-off. | ASI09 |
| AOR-STOP | An authorised operator shall be able to pause or stop any agent, or all agents for a tenant, within `<time>`. | Timed drill evidence within the last `<period>`. | ASI10 |
| AOR-OWNER | Each production agent shall have a named accountable owner, a registry entry and a review date. | Inspection of the agent registry. | ASI10; NIST AI RMF Govern |
| AOR-TRACE | For every run, the system shall record requester, context sources, proposed actions, policy decisions, approvals and executed effects, retained for `<period>`. | Sample of runs reconstructs end to end from logs. | Observability; NIST AI RMF Measure/Manage |
| AOR-DEFER | When `<policy trigger or measured uncertainty condition>` holds, the agent shall hand the case to `<role>` instead of acting. | Test cases at and beyond the trigger route to the human queue. | LLM07:2026 |

## 3. Worked example (original)

FR AFR-PAY-003, "Propose farmer payments", for a coffee cooperative:

- ASR-EGRESS-003: Payment instructions shall be sent only to the mobile-money
  number stored on the farmer record; the agent shall not supply or alter a
  payee number. Verification: test with an injected number in a delivery note;
  expected result, the payment draft uses the stored number and the attempt is
  logged.
- AOR-APPROVE-003: Payments shall be disbursed only after the treasurer
  approves the draft whose hash is shown on the approval screen; approval
  expires after 30 minutes (value set by the cooperative's risk owner).

## 4. Premium versus generic

| Generic | Apple-grade requirement |
|---|---|
| "The AI shall be secure against prompt injection." | ASR-UNTRUSTED with named sources, red-team set, run count and zero-tolerance result. |
| "Humans shall oversee the agent." | AOR-APPROVE, AOR-STOP and AOR-OWNER with roles, times and drill evidence. |
| Cites "OWASP LLM Top 10 agentic addendum". | Cites OWASP LLM 2026 and Agentic 2026 identifiers per requirement. |

## 5. Quality gate

- [ ] Every agent FR has ASR-SCOPE, ASR-AUTHZ and AOR-TRACE at minimum.
- [ ] Every FR touching untrusted content has ASR-UNTRUSTED and ASR-EGRESS.
- [ ] Every irreversible or financial action has AOR-APPROVE.
- [ ] Every requirement has a verification method and evidence artefact; no `TBD-owner` remains at baseline.
- [ ] Coverage table shows each OWASP LLM 2026 and ASI 2026 entry mapped or justified as not applicable.

## Evidence/currentness

Access date 2026-09-24. OWASP Top 10 for LLM Applications 2026, published 2026-08-03 (genai.owasp.org/resource/owasp-genai-llm-top-10-2026; LLM01:2026-LLM10:2026 names verified in the edition PDF). ASR-MEMORY carries LLM08:2026 because the 2026 Hidden Context Exposure entry covers leakage of memory and retrieved context, and LLM09:2026 for the vector store. The 2025 list (genai.owasp.org/llm-top-10) is superseded; OWASP Top 10 for Agentic Applications 2026, published 2025-12-09 (genai.owasp.org, publication verified; full text `NOT_ASSESSED`); NIST AI RMF 1.0 and AI 600-1 (nist.gov, verified). EU AI Act article applicability to a given product is `NOT_ASSESSED` here and must be confirmed by the regulatory skill.

Sources: Borges, D. and Campbell, D. (2026, early release) *AI Security Engineering*; Hodjat, B. and Blondeau, A. (2026, early release) *The Agentic Enterprise*; OWASP GenAI Security Project; NIST.
