# Discovery Interview And Hypothesis Validation

## Source Grounding

Derived from local HTML extractions:

- `lean-customer-development/toc.ncx`, `index_split_000.html` through `index_split_002.html`: where to start, who to talk to, what to learn, interview questions, validated hypotheses, MVP choice, ongoing discovery.
- `mapping-experiences/toc.ncx`, `index_split_002.html`: review existing sources, internal interviews, external research, brief guide to interviewing, analysing data.
- `handbook-persuasion-social-marketing/toc.ncx`: behaviour-change and ethical persuasion concepts used only as adoption-risk checks.

This is original SDLC guidance.

## Assumption Ledger

| ID | Assumption | Type | Evidence Needed | Test | Threshold | Decision |
|---|---|---|---|---|---|---|
| ASM-001 | [segment] has [problem] during [situation] | desirability | recent examples from target segment | interview | >= 7/10 qualified participants report recent workaround | persevere |

Types:

- customer segment
- problem and pain intensity
- current workaround
- trigger to change
- buying/adoption blocker
- value/pricing
- channel
- feasibility
- risk/compliance

## Interview Pattern

Ask for recent behaviour:

1. "Tell me about the last time this happened."
2. "What did you do next?"
3. "What tools, people, forms, or workarounds were involved?"
4. "What made it difficult, risky, slow, expensive, or frustrating?"
5. "What would make you change from the current approach?"
6. "Who else is involved before a decision or action happens?"

Do not ask:

- "Would you use this?"
- "Do you like this idea?"
- "How much would you pay?" before the value and buying context are understood.

## Validation Thresholds

| Evidence Level | Meaning | Action |
|---|---|---|
| Anecdote | 1-2 examples, weak fit | Keep as hypothesis. |
| Pattern | Multiple target users show same behaviour or blocker | Create requirement candidate. |
| Strong signal | Behaviour, money, time, policy, or operational evidence confirms pain | Prioritize requirement or MVP experiment. |
| Contradiction | Target users behave differently from assumption | Pivot, segment, or stop. |

## Hypothesis Card

```text
We believe [segment] has [problem] in [situation], currently solves it by [workaround], and will [behaviour] if we provide [intervention]. Evidence needed: [signal]. Persevere threshold: [metric]. Pivot/stop threshold: [metric or contradiction].
```

## Handoff Gate

Only pass a hypothesis into PRD/SRS as a requirement when:

- the target segment is specific
- the problem is observed or strongly evidenced
- the current workaround is known
- the desired behaviour change is measurable
- the requirement has a source evidence ID

