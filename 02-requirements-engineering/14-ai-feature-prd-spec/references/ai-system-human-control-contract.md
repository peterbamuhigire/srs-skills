<!-- Source basis: Designing for AI early release chapters 1-4; XP 2026 AI-in-Agile and AI-augmented engineering proceedings. Current legal claims require independent verification. -->

# AI System and Human-Control Contract

Attach to each AI functional requirement. Separate the model from the product
system that controls it.

| Layer | Requirement content | Acceptance evidence |
|---|---|---|
| Problem | User/system need and non-AI alternative | Outcome hypothesis and discovery evidence |
| Human | Actors, affected non-users, reviewer, contest owner, consent/notice | Actor map and approval/escalation test |
| System | Prompt, retrieval, tools, policy, queue, fallback and action boundary | System map and failure-path tests |
| Model | Version, capability, limitations and evaluation set | Model register and comparison report |
| Inputs | User-provided versus inferred data, provenance, quality and sensitivity | Input schema and data-quality/privacy checks |
| Outputs | Advice/content/ranking/action, uncertainty, citations and side effects | Structured output tests and audit event |

Require preview for irreversible actions, correction or contest, undo or safe
fallback, human escalation, and a record of actor/version/override/outcome.
Specify drift signals, feedback channels, rollback, and the minimum evidence for
each rollout stage. Do not label an unavailable legal or platform check compliant.
