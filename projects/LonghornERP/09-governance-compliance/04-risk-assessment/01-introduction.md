# Risk Assessment — Introduction and Methodology

## 1.1 Purpose

This Risk Assessment Register documents all identified risks to the Longhorn ERP project and platform. It serves as the primary governance artifact for tracking threats to schedule, compliance, data integrity, and commercial viability. Risks are derived from 2 sources:

- Open design gaps catalogued in `_context/gaps.md` (RISK-001 through RISK-018).
- Operational and strategic risks identified through architecture review (RISK-019 through RISK-024).

Each risk entry specifies a probability rating, impact rating, composite score, mitigation action, accountable owner, and target resolution date. This register is a living document; the accountable owner must update it when risk status changes.

## 1.2 Risk Categories

| Category | Definition |
|---|---|
| Technical | Risks arising from architecture decisions, implementation choices, or software defects. |
| Regulatory / Compliance | Risks arising from failure to meet statutory obligations under Ugandan or regional law. |
| Integration | Risks arising from dependence on third-party APIs, portals, or external systems. |
| Operational | Risks arising from day-to-day system operation, infrastructure, or staffing constraints. |
| Strategic | Risks arising from undecided business or product strategy decisions. |

## 1.3 Risk Scoring Methodology

Risk is scored using a 3×3 probability-impact matrix. Scores are expressed as integers from 1 (Minimal) to 9 (Critical).

### Probability Scale

| Rating | Label | Definition |
|---|---|---|
| H | High | The event is likely to occur within the planning horizon (> 60% probability). |
| M | Medium | The event may occur (30%–60% probability). |
| L | Low | The event is unlikely to occur (< 30% probability). |

### Impact Scale

| Rating | Label | Definition |
|---|---|---|
| H | High | The event threatens the project, product launch, or legal standing of the company. |
| M | Medium | The event causes significant delay (> 2 weeks), cost overrun, or degraded quality. |
| L | Low | The event causes minor inconvenience, resolvable within 1 sprint with no external consequence. |

### Risk Score Matrix

| | Impact: H | Impact: M | Impact: L |
|---|---|---|---|
| **Prob: H** | Critical (9) | High (6) | Medium (4) |
| **Prob: M** | High (6) | Medium (4) | Low (2) |
| **Prob: L** | Medium (4) | Low (2) | Minimal (1) |

### Score Labels

| Score | Label |
|---|---|
| 9 | Critical — immediate action required; blocks delivery |
| 6 | High — action required within current sprint |
| 4–5 | Medium — action required within current phase |
| 2–3 | Low — schedule for resolution before next phase |
| 1 | Minimal — monitor; no immediate action required |

## 1.4 Review Cadence

- **Quarterly review:** The full register must be reviewed every 3 months. Outdated mitigations or resolved risks must be updated.
- **Immediate update:** When a risk status changes (resolved, escalated, or new risk identified), the register must be updated within 2 business days.
- **Pre-phase gate:** All Critical and High risks must be reviewed and either mitigated or formally accepted before a new delivery phase begins.
- **Responsible party:** Peter Bamuhigire (Chwezi Core Systems) until a second developer is onboarded (see RISK-024).
