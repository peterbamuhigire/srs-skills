---
name: 06-ccb-charter
description: Use when establishing a Change Control Board's scope, membership, quorum, decision rights, evidence requirements, records, and escalation. Use change-impact-analysis for a specific change and sign-off-ledger for decisions.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Skill: CCB Charter

<!-- dual-compat-start -->

## Use When

- Use when establishing a Change Control Board's scope, membership, quorum, decision rights, evidence requirements, records, and escalation. Use change-impact-analysis for a specific change and sign-off-ledger for decisions.

## Do Not Use When

- Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared.
- Do not use this skill to fabricate missing project facts, legal conclusions, test results, approvals, or certification claims.

## Required Inputs

| Artefact | Source or provider | Required? | Missing-input behaviour |
|---|---|---:|---|
| Controlled baselines; change policy; CCB roles and delegates; quorum and voting rules; impact thresholds; emergency path; decision-record requirements | Sponsor, change manager, product owner, technical lead, QA, security, and operations | Yes | Stop dependent work; name the missing item, owner, and decision impact. A review check remains `not assessed`. |
| Scope, audience, baseline/version, and accountable decision owner | Requester or project context | Yes | Ask for or record the gap; do not infer authority or scope. |

## Capability and permission boundaries

Default to read-only. Read and search access to the supplied artefacts are required. Editing is limited to an explicitly authorised requested draft or project files. Execute validation only when authorised; publishing, signature, certification, production mutation, destructive action, spending, and risk acceptance require explicit authority.

## Degraded Mode

When files, tools, network, rendering, fonts, execution, or evidence are unavailable, return the narrowest useful qualified draft or finding set. Name every unavailable check and its consequence; an unassessed check is never a pass. Preserve evidence already gathered and provide the exact next verification step.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A required source, owner, obligation, or acceptance condition is missing | Stop the affected claim and record the gap | Unsupported governance artefact |
| Evidence satisfies the declared acceptance condition | Record the decision and hand off to the named consumer | Ambiguous approval or release |

## Workflow

1. Confirm the requested artefact, audience, scope, decision owner, and applicable baseline or version. Work read-only by default; source mutation, publication, signature, certification, production change, or risk acceptance requires explicit authority.
2. Inspect every required input and record missing, stale, conflicting, or inaccessible evidence. Stop claims that depend on an unresolved required input.
3. Apply the Decision Rules, then execute the existing Core Instructions below in order; preserve project terminology and trace each material statement to its source.
4. Test the draft against the output acceptance conditions and domain quality standards. If a check cannot run, mark it `not assessed` and never convert it into a pass.
5. On failure, recover by preserving completed evidence, identifying the narrowest corrective action and owner, and rerunning only the affected checks before handoff.
6. Produce the named artefact and evidence record; publish, sign, certify, mutate production, or accept risk only under explicit authority.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Skill: CCB Charter | Accountable reviewer, control owner, auditor, or release authority | The charter names scope, members, quorum, authority thresholds, conflict rules, emergency ratification, records, and escalation. |
| Gap and decision record | Accountable owner and downstream reviewer | Every gap has status, impact, owner, next action, and no unsupported pass or approval. |

## Evidence Produced

| Evidence | Contents | Acceptance condition |
|---|---|---|
| Skill: CCB Charter evidence record | Source identifiers, scope/version, decisions, checks, exceptions, and approval state | A reviewer can reproduce each material conclusion from named sources. |
| Validation record | Check, result (`pass`, `fail`, or `not assessed`), evidence location, date, and actor | No required check is omitted or silently treated as passed. |

## Quality Standards

- Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify.
- Use deterministic acceptance conditions and preserve traceability from source to decision and output.
- Separate facts, inferences, assumptions, and approvals; never present one as another.
- Apply `28-anti-ai-slop` during authoring and `29-ai-slop-audit` at major checkpoints and release.

## Anti-Patterns

- **Producing Skill: CCB Charter from assumptions instead of named project sources.** Fix: Cite the source or mark the item unverified.
- **Treating a missing or inaccessible check as passed.** Fix: Mark it `not assessed`, state impact, and block dependent claims.
- **Using vague gates such as "adequate", "secure", or "user-friendly".** Fix: Replace each with an observable criterion, threshold, and evidence source.
- **Copying a generic template without product, control, role, version, or jurisdiction detail.** Fix: Ground every section in the supplied context and remove unused boilerplate.
- **Publishing, signing, certifying, changing production, or accepting risk without authority.** Fix: Prepare a draft and route the decision to the accountable owner.
- **Listing evidence without provenance or an acceptance result.** Fix: Record source, period, integrity check, mapping, and pass/fail/not-assessed status.

## Worked Example

Example: if a required source, owner, obligation, or acceptance condition is missing, stop the affected claim and record the gap. Record the evidence and result in the validation record; this avoids unsupported governance artefact.

## References

- [Repository operating rules](../../AGENTS.md) — apply the engine's routing, evidence, and release gates.

<!-- dual-compat-end -->

## Source

PMBOK 6th Edition — Book of Forms; ISO 14764:2006 (Software Engineering — Software Life Cycle Processes — Maintenance), Section 7.2 (Change Management).

## Purpose

Generate a Change Control Board Charter that governs all changes to baselined project artifacts after formal approval. No baselined artifact may be modified without CCB approval. The charter establishes board composition, meeting cadence, decision authority thresholds, and the change request process.

## When to Use This Skill

- At project initiation, when the first baseline is established
- When transitioning from requirements gathering to design (SRS baseline)
- When a project lacks a formal change governance process
- When preparing for an audit or contractual review requiring evidence of change control
- When onboarding a new sponsor or client representative who must participate in CCB

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Input** | vision.md, stakeholders.md |
| **Output** | CCB_Charter.md |
| **Standard** | PMBOK 6th Ed., ISO 14764:2006 |
| **Estimated Time** | 10-20 minutes |

## Core Instructions

1. Read `projects/<ProjectName>/_context/vision.md` for project name, scope, and methodology. If the file is missing, halt and report.
2. Read `projects/<ProjectName>/_context/stakeholders.md` for CCB member names and roles. If the file is missing, generate the charter with `[TBD]` placeholders and flag each with `[CONTEXT-GAP]`.
3. Determine quorum size based on the stakeholder list (default: minimum 3 voting members).
4. Populate the budget threshold for Moderate/Major change types from the project context; if absent, flag `[CONTEXT-GAP: Budget threshold not defined]`.
5. Set meeting cadence based on the project methodology (Agile: weekly; Waterfall: bi-weekly; flag if ambiguous).
6. Generate `CCB_Charter.md` to `projects/<ProjectName>/09-governance-compliance/06-ccb-charter/CCB_Charter.md`.
7. After generating, present the document for human review per the Human Review Gate protocol in CLAUDE.md.

## CCB Charter Template

Generate the following document, substituting project-specific values:

---

```markdown
# Change Control Board Charter

**Document ID:** CCB-CHARTER-[ProjectName]-v[version]
**Project:** [ProjectName]
**Effective Date:** [YYYY-MM-DD]

## 1. Purpose

The Change Control Board (CCB) governs all changes to baselined project artifacts
after formal approval. No baselined artifact may be modified without CCB approval.

## 2. Scope

All changes to:
- Requirements baseline (SRS)
- Architecture baseline (SDD)
- Test baseline (STP)
- Production code baseline

## 3. CCB Composition

| Role | Name | Authority | Required for Quorum? |
|------|------|-----------|---------------------|
| CCB Chair (Project Manager) | | Approve/Reject | Yes |
| Technical Lead | | Recommend | Yes |
| QA Lead | | Recommend | Yes |
| Product Owner / Client Rep | | Approve scope changes | Yes |
| Domain Expert | | Advisory | No |

## 4. Meeting Cadence

- Regular: [Weekly / Bi-weekly] during active development
- Emergency: Within 24 hours for P1 change requests
- Quorum: Minimum [3] voting members required

## 5. Change Request Process

1. Requester submits Change Request form (CR-[ID])
2. CCB Chair triages within [2] business days
3. Technical Lead performs impact analysis
4. CCB reviews at next scheduled meeting (or emergency session)
5. Decision: Approve / Reject / Defer / Approve with conditions
6. If approved: baseline updated, version incremented, stakeholders notified
7. If rejected: requester notified with documented rationale

## 6. Approval Thresholds

| Change Type | Authority |
|-------------|-----------|
| Minor (no scope/schedule/budget impact) | Technical Lead alone |
| Moderate (schedule impact ≤ 5 days OR cost ≤ [budget threshold]) | CCB majority vote |
| Major (scope change OR schedule > 5 days OR cost > threshold) | CCB + Sponsor approval |
| Emergency (P1 system outage) | CCB Chair unilaterally, ratified at next meeting |

## 7. Documentation Requirements

- Every CCB decision recorded in the Change Log with: CR-ID, Decision, Date, Rationale, Approvers
- Approved changes trigger version increment of affected baseline document
- Rejected changes retain the CR with rationale for audit trail

## 8. Revision History

| Version | Date | Author | Change Summary |
|---------|------|--------|----------------|
| 1.0 | [YYYY-MM-DD] | | Initial charter |
```

---

## Verification Checklist

- [ ] Project name and Document ID populated
- [ ] All CCB roles identified with named individuals (or `[TBD]` with `[CONTEXT-GAP]` flag)
- [ ] Quorum count is explicit and ≥ 3 for projects with ≥ 4 stakeholders
- [ ] Budget threshold for Moderate/Major boundary is defined (not `[TBD]`)
- [ ] Meeting cadence matches the project methodology (Agile: weekly; Waterfall: bi-weekly)
- [ ] Change Request process has 7 numbered steps
- [ ] All four approval threshold rows are populated
- [ ] Documentation requirements reference the Change Log artifact

## Common Pitfalls

- Creating a CCB Charter after baselines have already been changed informally — go back and retroactively log those changes in the Change Log
- Omitting the budget threshold, which creates an ambiguous boundary between Moderate and Major changes
- Setting quorum to 1 or 2 — this undermines the governance control; enforce a minimum of 3
- Failing to include the Product Owner / Client Rep, who must approve scope changes per PMBOK 6th Ed.
- Confusing the CCB Charter (the governing document) with the Change Log (the operational record)

## Integration

- **Upstream:** Consumes project context from `_context/vision.md` and `_context/stakeholders.md`.
- **Downstream:** The CCB Charter governs all artifact changes across all phases. It must be referenced in the SRS, SDD, and STP as the change authority. The Change Log produced by CCB decisions feeds into `02-audit-report`.

## Standards Compliance

| Standard | Governs |
|----------|---------|
| PMBOK 6th Ed. (Book of Forms) | CCB composition, change request process, approval thresholds |
| ISO 14764:2006 §7.2 | Change management process for software maintenance baselines |
| IEEE 828-2012 | Software Configuration Management Plan (complements CCB governance) |

## Resources

- PMBOK 6th Edition: Project Management Body of Knowledge, Book of Forms
- ISO 14764:2006: Software Engineering — Software Life Cycle Processes — Maintenance
- IEEE 828-2012: Standard for Software Configuration Management Plans
- CLAUDE.md: Human Review Gate protocol (mandatory post-generation step)
