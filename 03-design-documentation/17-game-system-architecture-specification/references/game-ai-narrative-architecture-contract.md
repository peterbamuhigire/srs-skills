<!-- Source basis: AI for Game Developers (2005), Video Game Storytelling, Digital Storytelling, and MSC Software Magazine case-study workflow. Algorithm/API currency must be verified. -->

# Game AI and Narrative Architecture Contract

Keep the player-visible intent stable while allowing implementation changes.

| View | Required contract |
|---|---|
| Intent | What the character wants, believes, can do, and how this supports the narrative |
| Decision | FSM, steering, pathfinding, utility, planner or learned model and why the simplest fit was chosen |
| State | Typed state keys, ownership, transitions, interruption, save/load and recovery |
| World | Navigation costs, perception limits, reservations, obstacles and failure handling |
| Handoff | Animation/audio/level/narrative event names and timing/placeholder rules |
| Evidence | Trace, seed, build/config, performance envelope, fairness, accessibility and playtest result |

Instrument transitions, path failures, stuck recovery, decision reasons and
player-visible outcomes. Use normal, adversarial, worst-case and accessibility
scenarios. Historical algorithm descriptions are conceptual foundations, not a
license to assume a current engine API or production-ready learned model.
