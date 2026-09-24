## Objective

Produce the Prompt and System-Message Spec: the registry, the change-control rules, and the jailbreak-resistant patterns that every production prompt must use.

## Execution Steps

1. Verify the AI Architecture Spec and AI Feature PRD Spec exist.
2. Invoke `logic.prompt`.
3. Review with the AI lead and security lead; sign off prompt-owner roles in the registry README.

## Standards

- OWASP Top 10 for LLM Applications 2026: LLM01:2026 Prompt Injection, LLM08:2026 Hidden Context Exposure (formerly LLM07:2025 System Prompt Leakage)
- Anthropic prompt-engineering guidance
- NIST AI RMF MANAGE
