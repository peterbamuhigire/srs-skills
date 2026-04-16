# 06-Infrastructure-Design Skill

## Objective

This skill produces an Infrastructure Design document that addresses scalability, caching, messaging, load balancing, database scaling, reliability patterns, monitoring, and disaster recovery for systems with non-trivial availability and performance requirements. It is an **optional** skill controlled by a score-based decision gate.

## Decision Gate

Not every project requires a dedicated infrastructure design document. The skill evaluates six criteria against the project's SRS and context files:

| Criterion | Weight |
|-----------|--------|
| Expected concurrent users > 1,000 | 3 |
| 99.9%+ uptime requirement | 3 |
| Geographic distribution needed | 2 |
| Real-time processing requirements | 2 |
| Data volume > 100 GB | 2 |
| Regulatory data residency requirements | 2 |

**Score 7+**: Generate full document. **Score 4-6**: Optional, user confirms. **Score 0-3**: Skip, note in HLD.

## Execution Steps

1. Verify `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, and `projects/<ProjectName>/_context/tech_stack.md` exist. Optionally check for `projects/<ProjectName>/_context/quality_standards.md`.
2. Run the decision gate evaluation. Present the scoring worksheet to the user for confirmation.
3. If the gate passes, invoke the skill to generate all infrastructure sections and write `projects/<ProjectName>/<phase>/<document>/Infrastructure_Design.md`.
4. Review the Traceability Matrix to confirm every infrastructure component maps to an SRS requirement.
5. Proceed to downstream skills in Phase 05 (Testing) or Phase 06 (Deployment & Operations).

## Inputs

| File | Location | Required |
|------|----------|----------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes |
| SRS_Draft.md | `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md` | Yes |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes |
| quality_standards.md | `projects/<ProjectName>/_context/quality_standards.md` | No |

## Output

| File | Location |
|------|----------|
| Infrastructure_Design.md | `projects/<ProjectName>/<phase>/<document>/Infrastructure_Design.md` |

## Standards

- IEEE 1016-2009 Sec 5 (Architectural Design Viewpoints)
- ISO/IEC 25010 (Quality Model -- Reliability, Performance Efficiency)
- "System Design - The Big Archive" (ByteByteGo 2024)
