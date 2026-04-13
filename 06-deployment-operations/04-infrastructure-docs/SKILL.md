---
name: "infrastructure-docs"
description: "Generate infrastructure documentation with architecture diagrams, resource specifications, network topology, and IaC references per IEEE 1016."
metadata:
  use_when: "Use when the task matches infrastructure docs skill and this skill's local workflow."
  do_not_use_when: "Do not use when a more specific upstream or downstream skill owns the task, or when the required project context has not been prepared."
  required_inputs: "Provide the target project or document, the relevant context files, scope constraints, and any domain or standards inputs referenced here."
  workflow: "Follow the ordered steps, review gates, and local generation logic in this file before consulting deeper support files as needed."
  quality_standards: "Keep outputs grounded in source context, traceable to stated standards, and specific enough to review or verify."
  anti_patterns: "Do not fabricate missing requirements, skip human review gates, or substitute vague prose for verifiable documentation."
  outputs: "Produce or update the document, scaffold, analysis, or phase artifact that this skill defines."
  references: "Use `README.md`, `logic.prompt` when deeper detail is needed."
---

# Infrastructure Docs Skill

## Overview

This is the fourth skill in Phase 06 (Deployment & Operations). It produces infrastructure documentation that defines architecture diagrams (Mermaid), compute resource specifications per environment, network topology, storage architecture, Infrastructure-as-Code references, and backup/disaster recovery procedures. The output conforms to IEEE 1016-2009 and provides a complete infrastructure reference for DevOps and platform engineering teams.

## When to Use

- After 02-runbook and 03-monitoring-setup complete (they provide operational and observability context).
- When `HLD.md` exists in `../output/` with system architecture and component topology.
- When `tech_stack.md` is present in `../project_context/` with technology choices and infrastructure tooling.

## Quick Reference

| Attribute   | Value |
|-------------|-------|
| **Inputs**  | `../output/HLD.md`, `../project_context/tech_stack.md` |
| **Output**  | `../output/Infrastructure_Docs.md` |
| **Tone**    | Technical, architecture-focused, DevOps-facing |
| **Standard** | IEEE 1016-2009 |

## Input Files

| File | Location | Required | Purpose |
|------|----------|----------|---------|
| HLD.md | `../output/HLD.md` | Yes | System architecture, component topology, deployment targets |
| tech_stack.md | `../project_context/tech_stack.md` | Yes | Technology choices, infrastructure tooling, cloud provider details |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| Infrastructure_Docs.md | `../output/Infrastructure_Docs.md` | Complete infrastructure documentation with diagrams, resources, network, storage, IaC, and DR |

## Core Instructions

Follow these seven steps in order. Halt and notify the user if a required input file is missing.

### Step 1: Read Context Files

Read `HLD.md` from `../output/` and `tech_stack.md` from `../project_context/`. Log the absolute path of each file read. Halt if any required file is missing.

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

Produce a cost estimate summary table per environment. Write the completed document to `../output/Infrastructure_Docs.md`. Log the total count of compute resources, network components, and storage systems documented.

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

- [ ] `Infrastructure_Docs.md` exists in `../output/` with all seven sections populated.
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
