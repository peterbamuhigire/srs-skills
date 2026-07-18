---
name: 07-iot-system-design
description: Use when approved requirements involve devices, sensors, gateways, edge processing or operational technology and need end-to-end connectivity, identity, lifecycle, safety and fleet operations; use HLD for the wider system context.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# IoT System Design Skill
<!-- dual-compat-start -->
## Use When

- A connected product must be designed from device constraints through cloud and operations.

## Do Not Use When

- Do not use for ordinary web or mobile clients, or when device safety, connectivity and lifecycle evidence is unavailable.

## Required Inputs

| Artefact | Source or provider | Required? | Missing behaviour |
|---|---|---|---|
| Device capabilities, environment and safety constraints | Hardware, domain and requirements owners | Required | Stop on unknown safety-critical limits or regulatory obligations. |
| Connectivity, fleet scale and cloud integration | Network, platform and operations owners | Required | Model offline operation when live network evidence is unavailable. |

## Workflow

1. Read the named inputs and confirm their approval, version and unresolved decisions.
2. Apply the decision rules below before drafting; stop on a missing authority, unsafe assumption or unresolved scope driver.
3. Produce the IoT System Design through the existing domain procedure and load only the references needed for the chosen branch.
4. Trace each material statement in the IoT System Design to an input, decision or explicitly qualified assumption.
5. Verify the observable acceptance conditions, record unassessed checks, and hand the artefacts to their named consumers.
6. If validation fails, recover by correcting the source decision or artefact and rerun the affected check; do not weaken the acceptance condition.

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| IoT System Design | Firmware, edge, cloud, security, test and fleet operations teams | Identity, provisioning, telemetry, commands, offline behaviour, update, decommissioning, observability and failure recovery are specified end to end. |

## Evidence Produced

| Evidence | Consumer | Acceptance condition |
|---|---|---|
| Source and decision trace | Reviewer and downstream owner | Each material statement cites an approved input, named decision or qualified open issue. |
| Completed verification record | Release or phase gate owner | Every applicable check records pass/fail; unavailable checks remain `not assessed`. |

## Capability and permission boundaries

Read-only is the default for analysis, review, evaluation and planning. Read and search access to authorised project artefacts are required. Editing is limited to an explicitly requested project deliverable. Execution may run document, syntax or validation checks. Network access is used only for facts that require current verification. Do not publish, spend, change production, approve policy, or claim certification without explicit authority.

## Degraded mode

If any required capability is unavailable, return the narrowest useful qualified IoT System Design draft plus a gap register showing the missing item, affected sections, risk and owner. Never convert an unassessed check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Safety or latency needs local action | Place the rule at device/edge with safe fallback | Cloud outage does not create unsafe behaviour |
| Data is non-urgent and bandwidth constrained | Buffer, batch and reconcile | Connectivity cost and loss are controlled |

## Quality Standards

- Preserve repository terminology and trace every material choice to project context.
- Use deterministic acceptance conditions; replace vague quality claims with an observable check, threshold or named approval.
- Cover error, empty, edge, recovery and operational cases relevant to this skill.
- Verify standards, citations, APIs and package names before relying on them; qualify what cannot be checked.
- Stop release for a failed safety, security, legal, financial, accessibility or data-integrity gate.

## Anti-Patterns

- Treating a device as an always-online API client. Fix: design buffering and reconnection.
- Sharing fleet credentials. Fix: use per-device identity and rotation.
- Omitting failed-update recovery. Fix: specify signed updates, rollback and safe mode.
- Sending every sample to cloud. Fix: filter and aggregate against use cases.
- Ending lifecycle at deployment. Fix: specify monitoring, replacement and decommissioning.

## References

- [IoT architecture checklist](references/iot-architecture-checklist.md)
- [HLD neighbour](../01-high-level-design/SKILL.md)
<!-- dual-compat-end -->




## Overview

This skill extends Phase 03 for systems that include connected devices, sensors, gateways, edge processors, or operational technology integration. It turns verified requirements into an IoT-specific design that covers the full path from device behavior through edge or gateway coordination to cloud services, analytics, and lifecycle management.

## When to Use

- When the solution includes devices, sensors, actuators, wearables, kiosks, controllers, or gateways
- When connectivity is intermittent, bandwidth-constrained, or cost-sensitive
- When firmware, over-the-air updates, provisioning, or fleet management must be designed
- When the product crosses IT and OT boundaries and needs explicit safety, reliability, or physical-environment assumptions

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **Inputs** | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/<phase>/<document>/SRS_Draft.md`, `projects/<ProjectName>/_context/tech_stack.md`, `projects/<ProjectName>/_context/quality_standards.md` (recommended) |
| **Output** | `projects/<ProjectName>/<phase>/<document>/IoT_System_Design.md` |
| **Tone** | Systems-oriented, lifecycle-aware, deployment-realistic |
| **Standards** | IEEE 1016, IoT architecture and secure-device lifecycle practices |

## Core Instructions

### Step 1: Establish the IoT Context

Document:
- device classes and roles
- physical operating environment
- user and operator interactions
- telemetry and command flows
- safety, latency, and resilience expectations

### Step 2: Define End-to-End Architecture

Describe the architecture across:
- device layer
- gateway or edge layer
- connectivity layer
- cloud or platform layer
- application and analytics layer

State what processing occurs locally, at the edge, and in the cloud, and why.

### Step 3: Model Connectivity and Data Flow

Specify:
- communication protocols and why they fit
- expected message frequency and payload shape
- offline behavior and buffering strategy
- command acknowledgement and retry behavior
- ingestion, normalization, storage, and retention approach

### Step 4: Define Device Identity and Security

Document:
- provisioning and enrollment flow
- device identity and credential handling
- secure boot or hardware trust assumptions if applicable
- encryption in transit and at rest
- access control for device, operator, and service interactions
- key rotation, revocation, and incident response

### Step 5: Define Device Lifecycle Management

Cover:
- manufacturing or initial registration assumptions
- configuration management
- OTA firmware or software updates
- rollback and staged rollout strategy
- decommissioning and data sanitization

### Step 6: Address Reliability, Safety, and Operations

Define:
- failure modes and safe-state behavior
- monitoring and fleet health metrics
- diagnostics and remote troubleshooting
- serviceability constraints for field operations
- dependencies on third-party networks or hardware vendors

### Step 7: Generate Output

Write `projects/<ProjectName>/<phase>/<document>/IoT_System_Design.md` with architecture, connectivity, security, lifecycle, operational model, and traceability back to the source requirements.

## Common Pitfalls

- Assuming persistent connectivity when the device context does not support it
- Designing cloud-only control paths for safety-critical or latency-sensitive actions
- Ignoring secure provisioning and credential rotation
- Treating firmware updates as a release detail instead of a core architecture concern
- Omitting field diagnostics, fleet segmentation, and rollback mechanisms

## Verification Checklist

- [ ] The device, edge, and cloud responsibilities are clearly separated.
- [ ] Connectivity assumptions include offline and degraded modes.
- [ ] Security design covers provisioning, identity, encryption, and revocation.
- [ ] Lifecycle design covers onboarding, updates, rollback, and retirement.
- [ ] Operational sections include observability, fleet health, and supportability.
- [ ] Architectural decisions trace back to explicit product or requirements context.
