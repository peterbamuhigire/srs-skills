# Human Agency and System Boundaries

This reference is a self-contained synthesis prepared from Rana Gujral,
*The AI Instinct*, and Sanjeev Mohan, *Designing the AI-Driven Data Foundations*.

## Architecture questions

- What decision remains human-owned, and what may the system recommend, draft, or execute?
- Which data, memory, feedback, and consequence signals enter the loop?
- How can a user inspect, correct, refuse, interrupt, or reverse the system's work?
- Which permissions, data boundaries, and escalation rules prevent capability from becoming authority?
- What evidence detects drift in the model, data, workflow, or user behaviour?

Treat memory as a governed state transition, not an invisible convenience. Keep
the model, data, tools, user, and operational system as separable components so
one failure can be contained and diagnosed.

## Required architecture evidence

Include an agency matrix, data and memory lineage, correction path, abstention
and escalation policy, audit events, drift signals, kill-switch or fallback, and
the human reviewer for consequential actions.
