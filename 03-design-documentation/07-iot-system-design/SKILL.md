---
name: "iot-system-design"
description: "Generate IoT system design documentation covering device, edge, connectivity, cloud, security, lifecycle, and operational architecture for connected products."
metadata:
  use_when: "Use when the system includes connected devices, embedded controllers, telemetry, remote commands, or physical-world integration that requires IoT-specific design decisions."
  do_not_use_when: "Do not use when the product is purely web or enterprise software with no meaningful device, sensor, or edge-computing scope."
  required_inputs: "Provide the product context, operating environment, device types, connectivity assumptions, data flows, security constraints, and lifecycle expectations."
  workflow: "Follow the device-context, architecture, connectivity, security, lifecycle, and operations steps before generating the final design."
  quality_standards: "Keep the design explicit about device constraints, trust boundaries, failure modes, update strategy, and end-to-end operational ownership."
  anti_patterns: "Do not treat IoT as only cloud APIs, ignore offline behavior, or omit fleet security and lifecycle management."
  outputs: "Produce an IoT system design document with architecture, device lifecycle, connectivity, security, observability, and deployment decisions."
  references: "Use `references/` when deeper detail is needed."
---

# IoT System Design Skill

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
