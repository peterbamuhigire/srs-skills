# Agent Red-Team Cross-Link

The AI Red-Team Test Plan covers ten generic AI adversarial categories. For agent features, the **AI Agent Red-Team Test Plan** (`05-testing-documentation/07-ai-agent-red-team-test-plan`) adds ten agent-specific categories.

## Agent-specific categories (in addition to the generic ten)

1. Indirect prompt injection via tool output.
2. Action escalation.
3. Tenant data exfil via tool output.
4. Recursive self-modify.
5. Jailbreak via memory.
6. Agent-vs-supervisor confusion (multi-agent only).
7. Budget-exhaustion DoS.
8. Cross-tenant tool routing.
9. Plan-approval social engineering.
10. Tool-result poisoning.

## Cross-tenant leak category extension

The generic "Cross-tenant leakage" category extends in the agent setting to **cross-tenant tool routing**, which has higher severity (CRITICAL) than the generic case because the side-effect is an *action*, not just a read.

## CI smoke set

The generic smoke set covers prompt-injection, jailbreak, exfil. The agent smoke set adds the ten categories above; both run on agent-feature PRs.

## Sign-off rules

Agent features additionally require zero CRITICAL / HIGH in the agent-specific scenario set before any L1+ rollout, regardless of generic red-team status.
