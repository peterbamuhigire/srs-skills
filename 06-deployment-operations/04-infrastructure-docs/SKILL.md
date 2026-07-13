---
name: 04-infrastructure-docs
description: Use when producing or updating infrastructure documentation for topology, environments, dependencies, configuration ownership, recovery, and change controls. Use deployment-guide for the neighbouring concern; this skill owns the named document contract and its acceptance evidence.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---


# Infrastructure Docs Skill

<!-- dual-compat-start -->
## Use When

- Produce or update infrastructure documentation from approved project evidence.
- Resolve decisions about topology, environments, dependencies, configuration ownership, recovery, and change controls.
- Prepare a reviewable handoff for Platform engineers and auditors.

## Do Not Use When

- The task is primarily owned by deployment-guide; route there and use this skill only for its named output.
- Required project evidence or decision authority is unavailable and the requester expects a pass, release, certification, or production change.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when absent |
|---|---|---|---|
| Project _context/, approved requirements, and relevant architecture | Project owner and upstream phase skills | Required | Stop at a gap register; do not invent scope, thresholds, integrations, or owners. |
| Existing artefact, implementation, configuration, and evidence named below | Repository, delivery team, or service owner | Required when updating or assessing | Mark inaccessible items `not assessed`; do not treat them as passed. |
| Target audience, environment, risk tolerance, and authority | Requester and accountable owner | Required | Produce a read-only outline with explicit assumptions; do not mutate project or production state. |
## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Infrastructure Documentation | Platform engineers and auditors | The documented topology matches deployed evidence and names ownership, recovery assumptions, and sensitive configuration boundaries. |
| Decision and gap register | Reviewer and downstream phase owner | Every assumption, rejected option, unresolved dependency, waiver, and owner is explicit. |
| Validation evidence | Release or governance reviewer | Checks identify command or method, date, result, evidence location, and all unassessed items. |

## Evidence Produced

| Evidence | Minimum content | Acceptance |
|---|---|---|
| Traceability record | Source artefact, decision, output section, owner | No mandatory decision is source-free. |
| Quality-gate result | Check, expected result, observed result, evidence path | Failures and unavailable checks cannot appear as passes. |
| Review record | Reviewer, date, disposition, open actions | The consumer can reproduce the acceptance decision. |

## Capability and Permission Boundaries

- Minimum capabilities: read and search the authorised project sources. Execution is optional and limited to non-destructive validation.
- Assessment and planning default to read-only. Create or edit the named project document only when the request explicitly authorises it. Production mutation, publishing, destructive action, spending, external communication, or certification claims require separate explicit authority.
- Treat secrets, tenant data, incident evidence, and financial records as least-privilege inputs; expose only the minimum evidence needed for review.

## Degraded Mode

If files, execution, network, rendering, environment access, fonts, or current evidence are unavailable, return the narrowest useful draft plus a gap register. Label affected checks `not assessed`, retain the intended acceptance oracle, and state who must supply or verify the missing evidence. Never convert an unavailable check into a pass.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Evidence is complete and authority is explicit | Choose documentation depth from operational and audit risk and produce the full artefact. | A diagram that omits dependencies or recovery. |
| A required source or approval is missing | Stop the affected branch; record the gap, owner, and unblock condition. | Fabricated requirements or unauthorised action. |
| Evidence conflicts across sources | Preserve both claims, identify the controlling owner, and request a recorded decision. | Silent selection of a convenient but wrong source. |
| A check cannot run in the available environment | Keep its oracle and mark it `not assessed`; require later execution evidence. | False assurance from capability limits. |

## Workflow

1. Confirm the named deliverable, consumer, scope, environment, authority, and neighbouring-skill boundary.
2. Inventory required sources and validate provenance, freshness, internal consistency, and missing inputs. Stop the affected branch on a mandatory gap.
3. Extract traceable requirements, invariants, risks, and measurable acceptance criteria; record conflicts before choosing a design or procedure.
4. Apply the decision rules and the domain workflow below. For a failed branch, preserve evidence, choose the documented recovery path, or escalate to the named owner.
5. Draft the artefact, decision register, and evidence record together. Do not defer failure handling, rollback, security, tenancy, accessibility, or operational ownership.
6. Run available checks, review every result, repair failures, and hand off only when acceptance is observable. If recovery fails or authority is exceeded, stop and escalate without mutation.

## Quality Standards

- Ground every section in a named project source, decision, measured result, or accountable owner.
- Give each requirement or procedure a deterministic oracle that another reviewer can reproduce.
- Keep assumptions, exclusions, degraded checks, residual risks, and waivers visible at handoff.
- Preserve the domain invariants and more specific controls in the existing workflow below; this contract does not replace them.
- Run the repository anti-AI-slop gate: remove filler, verify named standards and dependencies, and retain purposeful domain detail.

## Anti-Patterns

- Copying a generic template without mapping it to project sources. Fix: attach each section to an approved requirement, configuration, risk, or owner.
- Choosing a threshold because it is common practice. Fix: derive it from a requirement, measured baseline, risk decision, or current verified source.
- Reporting an inaccessible or unexecuted check as passed. Fix: mark it `not assessed`, preserve the oracle, and name the verifier.
- Mixing the neighbouring deployment-guide concern into this artefact without a boundary. Fix: cross-reference its output and keep ownership explicit.
- Omitting failure, rollback, empty-state, security, tenancy, or escalation behaviour. Fix: specify the trigger, safe action, verification, and owner for each applicable case.
- Mutating a repository, environment, tenant, ledger, or external system while drafting guidance. Fix: remain read-only until the exact mutation and authority are explicit.
- Claiming compliance, certification, readiness, or release from prose alone. Fix: require source-attributed evidence and a named acceptance decision.

## Worked Example

Given an approved project source and a conflicting implementation detail, record both with provenance, stop the affected branch, and obtain the accountable owner's decision. Then update the relevant contract, define a reproducible acceptance check, and retain its observed result. The artefact is accepted only when the documented topology matches deployed evidence and names ownership, recovery assumptions, and sensitive configuration boundaries.

## References

- [logic.prompt](logic.prompt) - load only when its template, logic, or detail is needed.
- [README.md](README.md) - load only when its template, logic, or detail is needed.
<!-- dual-compat-end -->
## Overview

This is the fourth skill in Phase 06 (Deployment & Operations). It produces infrastructure documentation that defines architecture diagrams (Mermaid), compute resource specifications per environment, network topology, storage architecture, Infrastructure-as-Code references, and backup/disaster recovery procedures. The output conforms to IEEE 1016-2009 and provides a complete infrastructure reference for DevOps and platform engineering teams.

## When to Use

- After 02-runbook and 03-monitoring-setup complete (they provide operational and observability context).
- When `HLD.md` exists in `projects/<ProjectName>/<phase>/<document>/` with system architecture and component topology.
- When `tech_stack.md` is present in `projects/<ProjectName>/_context/` with technology choices and infrastructure tooling.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `projects/<ProjectName>/<phase>/<document>/HLD.md`, `projects/<ProjectName>/_context/tech_stack.md` |
| **Output**  | `projects/<ProjectName>/<phase>/<document>/Infrastructure_Docs.md` |
| **Tone**    | Technical, architecture-focused, DevOps-facing |
| **Standard** | IEEE 1016-2009 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `projects/<ProjectName>/<phase>/<document>/HLD.md` | Yes | System architecture, component topology, deployment targets |
| tech_stack.md | `projects/<ProjectName>/_context/tech_stack.md` | Yes | Technology choices, infrastructure tooling, cloud provider details |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Infrastructure_Docs.md | `projects/<ProjectName>/<phase>/<document>/Infrastructure_Docs.md` | Complete infrastructure documentation with diagrams, resources, network, storage, IaC, and DR |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `projects/<ProjectName>/<phase>/<document>/` and `tech_stack.md` from `projects/<ProjectName>/_context/`. Log the absolute path of each file read. Halt if any required file is missing.

### Step 2: Generate Infrastructure Architecture Diagram

Produce a Mermaid diagram representing the infrastructure layout:
- Compute nodes (application servers, worker nodes, cron servers)
- Data stores (databases, caches, message queues)
- Network components (load balancers, API gateways, CDN)
- External integrations (third-party APIs, SaaS services)
- The diagram shall show connectivity and data flow between components

### Step 3: Define Compute Resources per Environment

For each environment (dev, staging, production), specify:
- Instance type or container resource limits (CPU cores, RAM)
- Storage allocation (root volume, data volume)
- Scaling policy (minimum, maximum, scaling trigger)
- Estimated monthly cost per resource where feasible

### Step 4: Define Network Topology

Document the network architecture:
- VPC/VNET layout with CIDR blocks
- Subnet design (public, private, data tier)
- Security groups and firewall rules (ingress/egress)
- Load balancer configuration (type, health check, routing rules)
- DNS configuration (domain, records, TTL)

### Step 5: Define Storage Architecture

Document storage systems and their configuration:
- Primary database (engine, version, instance size, storage type, replication)
- Cache layer (engine, cluster size, eviction policy)
- File/object storage (bucket names, access policies, lifecycle rules)
- CDN configuration (origin, cache behavior, invalidation strategy)

### Step 6: Define IaC References and Backup/DR

Document Infrastructure-as-Code artifacts:
- Terraform module locations and purpose
- Docker Compose or Kubernetes manifest locations
- CI/CD pipeline configuration file locations
Document backup and disaster recovery:
- Backup schedule, retention policy, and storage location
- Recovery Point Objective (RPO) and Recovery Time Objective (RTO)
- Disaster recovery procedure (failover steps, data restoration)
- DR testing schedule

### Step 7: Write Output with Cost Estimates

Produce a cost estimate summary table per environment. Write the completed document to `projects/<ProjectName>/<phase>/<document>/Infrastructure_Docs.md`. Log the total count of compute resources, network components, and storage systems documented.

## Output Format

The generated `Infrastructure_Docs.md` shall contain these sections in order: Document Header (project name, date, version, standards), 1. Infrastructure Architecture Diagram, 2. Compute Resources, 3. Network Topology, 4. Storage Architecture, 5. IaC References, 6. Backup & DR, 7. Cost Estimates.

## Common Pitfalls

| Pitfall | Remedy |
|---------|--------|
| Architecture diagrams without data flow direction | Every diagram shall show directional connectivity between components |
| Compute resources without scaling policies | Every production resource shall define minimum, maximum, and scaling trigger |
| Network topology without security groups | Every subnet shall have associated security group rules |
| Missing RPO/RTO definitions | Backup and DR shall define RPO and RTO targets explicitly |

## Verification Checklist

- [ ] `Infrastructure_Docs.md` exists in `projects/<ProjectName>/<phase>/<document>/` with all seven sections populated.
- [ ] Infrastructure architecture diagram renders valid Mermaid with directional data flows.
- [ ] Compute resources specify instance types, scaling policies for dev/staging/prod.
- [ ] Network topology defines VPC layout, subnets, security groups, and load balancers.
- [ ] Storage architecture covers database, cache, file storage, and CDN.
- [ ] IaC references list Terraform, Docker, or K8s manifest locations.
- [ ] Backup and DR define RPO, RTO, and DR testing schedule.

## Integration

| Direction | Skill | Relationship |
|-----------|-------|-------------|
| Upstream | 01-deployment-guide | Consumes deployment topology for infrastructure layout |
| Upstream | 02-runbook | Consumes operational context for DR procedures |
| Upstream | 03-monitoring-setup | Consumes monitoring architecture for infrastructure diagram |
| Downstream | Phase 08 (User Documentation) | Feeds infrastructure details into administrator guides |

## Standards

- **IEEE 1016-2009** -- Software Design Descriptions. Governs architecture viewpoints and design documentation structure.

## Resources

- `logic.prompt` -- Executable prompt containing the step-by-step infrastructure documentation generation logic.
- `README.md` -- Quick-start guide for this skill.
