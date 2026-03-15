# Book Analysis: Choose Your WoW — Disciplined Agile (Ambler & Lines)
**Analyzed:** 2026-03-15
**Feeds:** W-18 (hybrid detection), B-05 (phase gate exit criteria), methodology selection enrichment

---

## Key Concept: Way of Working (WoW)

DA is explicitly anti-prescriptive. Teams choose from 21 process goals × hundreds of option lists based on context. Six lifecycle options, not one. The WoW evolves continuously via Guided Continuous Improvement (GCI) — a PDSA loop.

---

## Six DA Lifecycles

| Lifecycle | When to use | Key characteristic |
|-----------|-------------|-------------------|
| **Agile** | Teams new to agile; stable-ish requirements; small/medium co-located | Scrum++; Inception → Construction iterations → Transition |
| **Continuous Delivery: Agile** | Mature agile teams; high CI/CD automation | Releases to production every iteration or less |
| **Lean** | Rapidly changing requirements; sustaining/legacy teams; low psychological safety | Kanban, no fixed iterations; JIT work; tolerant of irregular stakeholder availability |
| **Continuous Delivery: Lean** | Highly disciplined teams; full CD automation | Kanban + several releases per day; feature toggles |
| **Exploratory** | New product/feature exploration; A/B testing; wicked problems | Lean Startup + parallel MVPs; NOT for regulatory contexts |
| **Program** | 30+ people; team-of-teams; single solution | Subteams choose own lifecycles; program-level coordination |

**Note:** Traditional/Waterfall is acknowledged as appropriate only for low-risk projects with stable, known requirements (e.g., hardware migrations). DA does not use it as a standard lifecycle.

---

## W-18: Water-Scrum-Fall Detection

DA defines WaterScrumFall (also "Wagile," "Scrumifall") as: Inception treated as mini-waterfall (detailed requirements documentation up-front), then agile Construction sprints, then Transition treated as another mini-waterfall (hardening sprints, big-bang testing).

### Five Detection Questions for Phase 00

| # | Question | WaterScrumFall signal |
|---|----------|----------------------|
| 1 | How long is your planned Inception/initiation phase? | >3 weeks for a small team |
| 2 | What level of requirements documentation is expected before development begins? | Detailed spec (BRUF flag) |
| 3 | Does your organization require a formal phase gate between requirements and development? | Yes |
| 4 | Does testing occur primarily at the end of development? | Yes |
| 5 | Are BAs or architects working in a separate sequential phase from developers? | Yes |

**Scoring:** 0–1 flags = healthy; 2–3 = WaterScrumFall risk; 4–5 = WaterScrumFall confirmed → recommend Lean lifecycle + Guided Lean Change transition.

### Seven SDCF Context Factors (from Figure 6.14/6.15)

For methodology selection in Phase 00, capture:
1. Team size → small=Agile; large sustaining=Lean
2. Regulatory context → strict=more governance rigor + documentation depth
3. Requirements stability → stable=Agile/Traditional; fluid=Lean; unknown=Exploratory
4. Team agile maturity → new=Agile; experienced=CD lifecycle
5. Stakeholder availability → low=Lean; high=Agile/CD
6. Geographic distribution → co-located=any; distributed=Lean (less ceremony overhead)
7. Technical debt level → high debt legacy = Lean lifecycle

---

## B-05: Phase Gate Exit Criteria — DA's Six Milestones

DA uses six risk-based milestones (not artifact-based quality gates). These replace the traditional "review a document to check a box" pattern.

| Milestone | Phase | Exit Criterion | srs-skills Mapping |
|-----------|-------|---------------|--------------------|
| **Stakeholder Vision** | End of Inception | Agreed scope, tech strategy, schedule estimate, budget, risks, team | Skills 01–03 outputs |
| **Proven Architecture** | Early Construction | Working code skeleton addresses technically risky requirements; NFRs demonstrably supported | Skill 04 (Interfaces) |
| **Continued Viability** | Mid-Construction (optional) | Stakeholder confirmation to proceed; any scope/team/budget changes documented | Ongoing |
| **Sufficient Functionality** | End of Construction | MMR complete (≥1 MMF delivers positive user outcome); deployment cost justified | Skill 05 (FRs) — all FRs have acceptance criteria |
| **Production Ready** | Transition | All transition activities complete; automated quality gates passed | Skills 06–08 — no open [V&V-FAIL] tags |
| **Delighted Stakeholders** | Post-delivery | Satisfaction metrics collected and acceptable | NFRs verified; stakeholder satisfaction defined |

**Anti-pattern:** Traditional quality gates that focus on reviewing documentation artifacts rather than demonstrating working outcomes are explicitly named as the WaterScrumFall symptom.

---

## Documentation Philosophy (CRUFT Formula)

DA recommends asking these five questions about every document:
- **C**orrect — is it accurate?
- **R**ead — will anyone actually read it?
- **U**nderstood — will readers understand it?
- **F**ollowed — will people act on it?
- **T**rusted — do stakeholders trust its accuracy?

Single-source wiki preferred. Executable specifications (BDD/ATDD) over static documentation. Concise templates (20% of fields = 80% of value). Continuous documentation throughout lifecycle — not batch at phase ends.

---

## DA's 21 Process Goals (for reference)

**Inception:** Form Team | Align with Enterprise Direction | Explore Scope | Identify Architecture Strategy | Plan the Release | Develop Test Strategy | Develop Common Vision | Secure Funding

**Construction:** Prove Architecture Early | Address Changing Stakeholder Needs | Produce a Potentially Consumable Solution | Improve Quality | Accelerate Value Delivery

**Transition:** Ensure Production Readiness | Deploy the Solution

**Ongoing:** Grow Team Members | Coordinate Activities | Evolve WoW | Address Risk | Leverage Existing Infrastructure | Govern Delivery Team

---

## Key Anti-Patterns

| Anti-Pattern | DA Name | Description |
|-------------|---------|-------------|
| WaterScrumFall | Wagile/Scrumifall | Waterfall Inception + Agile sprints + Waterfall Transition |
| Method prison | Method Prison (Jacobson) | Prescriptive framework that can't be deviated from |
| Fake agile | AINO (Agile in Name Only) | Agile ceremonies, waterfall thinking |
| Big Requirements Up Front | BRUF | Detailed spec before development begins |
| Big Design Up Front | BDUF | Excessive architecture before any code |
| Siloed governance | Specialized governance | Multiple sequential quality gates (security/arch/data/finance) = massive overhead |
| One-size-fits-all | Process dissonance | Same process mandated regardless of team context |

---

## Requirements Options (Explore Scope goal — ordered by preference)

- **Purpose:** Impact map | Value proposition canvas | Product vision box | Elevator pitch
- **Usage:** User story → Epics → User story map → Use case → Use case diagram
- **NFRs:** Acceptance criteria (first) → Explicit NFR list → Technical stories
- **Manage:** Work item list → Requirements backlog → Spreadsheet → Traditional requirements spec (last)

---

## Stakeholder Interaction (ordered by effectiveness)

1. Active stakeholder participation (daily availability)
2. On-site customer
3. Indirectly via Product Owner
4. Indirectly via Business Analyst
5. Occasional reviews (milestone reviews only)
6. Surveys/questionnaires (least effective)
