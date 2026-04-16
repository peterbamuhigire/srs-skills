---
name: "go-live-readiness"
description: "Generate a go-live readiness assessment and launch control plan that verifies the system is operationally, organizationally, and commercially ready for release."
metadata:
  use_when: "Use when the product is approaching release, pilot, cutover, or production launch and a structured readiness decision is required."
  do_not_use_when: "Do not use when the project is still in early design without an intended deployment target, release scope, or operational owner."
  required_inputs: "Provide the release scope, deployment approach, operational documentation, unresolved risks, support model, and stakeholder decision context."
  workflow: "Follow the readiness-dimension review, gate scoring, cutover planning, and decision-record steps before generating the final assessment."
  quality_standards: "Keep the output decision-oriented, evidence-backed, and explicit about blockers, conditions, owners, and due dates."
  anti_patterns: "Do not reduce readiness to a test pass, ignore support transition, or approve launch without rollback and incident ownership."
  outputs: "Produce a go-live readiness report with gate criteria, blocker register, launch recommendation, and cutover control plan."
  references: "Use `references/` when deeper detail is needed."
---

# Go-Live Readiness Skill

## Overview

This skill closes the loop between design, delivery, and operations by determining whether the product is actually ready to launch. It synthesizes deployment, monitoring, runbook, infrastructure, and transition evidence into a decision record that supports go, conditional go, or no-go outcomes.

## When to Use

- Before a production launch, customer rollout, pilot, migration, or major cutover
- When release stakeholders need a structured readiness review rather than ad hoc signoff
- When support, training, communication, operational ownership, or rollback planning could affect launch success
- When the team needs an explicit blocker list and conditional-release criteria

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/Deployment_Guide.md`, `projects/<ProjectName>/<phase>/<document>/Runbook.md`, `projects/<ProjectName>/<phase>/<document>/Monitoring_Setup.md`, `projects/<ProjectName>/<phase>/<document>/Infrastructure_Docs.md` (recommended), release-specific evidence |
| **Output** | `projects/<ProjectName>/<phase>/<document>/Go_Live_Readiness.md` |
| **Tone** | Decision-oriented, risk-aware, operationally concrete |
| **Standards** | Production readiness, transition governance, and operational acceptance practices |

## Core Instructions

### Step 1: Define the Release Decision Context

State:
- release scope
- target environment and launch window
- launch type such as big-bang, phased, pilot, or canary
- accountable approvers and operating owners

### Step 2: Evaluate Readiness Dimensions

Assess at minimum:
- product scope completeness
- deployment and rollback readiness
- monitoring and alerting readiness
- support and incident response readiness
- security and compliance readiness
- data migration or cutover readiness
- training, communication, and organizational transition readiness
- vendor or dependency readiness

### Step 3: Score and Classify Findings

For each dimension, mark:
- ready
- conditionally ready
- blocked

Every conditional or blocked item must include an owner, evidence gap, due date, and mitigation path.

### Step 4: Build the Launch Control Plan

Document:
- cutover timeline
- decision checkpoints
- rollback triggers
- communications cadence
- hypercare support period
- first-day and first-week success metrics

### Step 5: Record the Go/No-Go Recommendation

Choose one outcome:
- go
- conditional go
- no-go

State the reasoning, unresolved risks, and exact conditions for changing the decision.

### Step 6: Generate Output

Write `projects/<ProjectName>/<phase>/<document>/Go_Live_Readiness.md` with readiness assessment, blocker register, cutover plan, and recommendation.

## Common Pitfalls

- Treating technical deployment readiness as the whole launch decision
- Launching without named incident, rollback, and business-communication owners
- Ignoring customer support, operations staffing, or training gaps
- Declaring readiness without measurable success and abort criteria

## Verification Checklist

- [ ] The launch scope, timing, and accountable owners are explicit.
- [ ] Every readiness dimension has evidence and a status.
- [ ] Every blocker or conditional item has an owner and due date.
- [ ] Rollback triggers and hypercare support are defined.
- [ ] The final recommendation is explicit and justified.
- [ ] The document can support an actual go/no-go meeting without extra reconstruction.
