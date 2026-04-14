# Phase 8: Deployment Pipeline, CI/CD & Infrastructure

> **For Claude:** Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Close the single biggest gap in the entire skills library — the inability to
deploy software to production, run it at scale, and deliver changes safely. Four new skills
and three enhancements convert excellent code capabilities into deployed, revenue-generating products.

**Architecture:** This is the highest-priority phase. Without cloud, Kubernetes, IaC, and
CI/CD skills, every other capability stays on localhost. This phase unlocks production.

**Skills library path:** `C:\Users\Peter\.claude\skills\`

> **EXECUTE THIS PHASE FIRST** regardless of the SDLC ordering in this plan.
> Infrastructure is the revenue blocker. Everything else can wait.

---

## Consultancy Capability This Phase Unlocks

A fully equipped consultant can:

- Deploy any web or mobile SaaS application to production AWS/GCP infrastructure
- Containerise applications with Docker and orchestrate them with Kubernetes
- Provision repeatable, version-controlled infrastructure using Terraform and Ansible
- Run GitHub Actions pipelines that test, build, and deploy on every commit
- Achieve zero-downtime deployments with rolling updates, blue-green, and canary strategies
- Manage secrets securely using HashiCorp Vault with PKI and automatic rotation
- Enforce ISO 27001 security controls and PCI-DSS requirements in infrastructure
- Run container runtime security with Falco and enforce policies with OPA/Gatekeeper
- Optimise cloud costs with FinOps practices: resource quotas, utilisation targets, budget alerts
- Harden Linux servers with sysctl tuning, cgroups, auditd, AppArmor, and fail2ban

---

## Current Strengths — Infrastructure Skills Already Built

- `cicd-devsecops` — SAST/DAST integration, secrets scanning, dependency auditing, SBOM
- `cicd-jenkins-debian` — Jenkins on Debian: pipelines, agents, Jenkinsfile, multibranch
- `cicd-pipeline-design` — Pipeline architecture: stages, gates, parallel jobs, artifact management
- `deployment-release-engineering` — Release strategies: blue-green, canary, feature flags, rollback
- `linux-security-hardening` — SSH hardening, UFW firewall, fail2ban, audit logging
- `network-security` — Firewall rules, TLS/SSL, network segmentation, VPN patterns

---

## Build Tasks

### Task 1: Create `cloud-architecture` skill

**File to create:** `C:\Users\Peter\.claude\skills\cloud-architecture\SKILL.md`

**Read first:**
- AWS Well-Architected Framework (free PDF — `aws.amazon.com/architecture/well-architected`)
- *Docker Deep Dive* — Nigel Poulton (read fully before writing)
- *The DevOps Handbook* — Kim, Humble, Debois, Willis (relevant chapters)

**Content outline for SKILL.md (target: 420–490 lines):**

1. **Cloud Provider Selection** — AWS vs GCP vs Azure: decision framework for East African SaaS
2. **Docker Fundamentals** — images, containers, Dockerfile best practices, multi-stage builds
3. **Docker Compose** — local development stack, service dependencies, health checks, volumes
4. **AWS Core Services:**
   - Compute: EC2 instance types, auto-scaling groups, Launch Templates
   - Storage: S3 bucket policies, lifecycle rules, pre-signed URLs, multipart upload
   - Database: RDS MySQL/PostgreSQL, parameter groups, Multi-AZ, read replicas
   - Serverless: Lambda triggers (S3, SQS, API Gateway), cold start mitigation
   - IAM: policies, roles, service accounts, least-privilege principle
5. **Networking** — VPC design: public/private subnets, NAT gateway, security groups, NACLs
6. **Load Balancers** — ALB vs NLB, target groups, health checks, SSL termination
7. **CDN** — CloudFront distribution, cache behaviours, origin shield, WAF integration
8. **SSL/TLS Automation** — Let's Encrypt with Certbot, auto-renewal, ACM for AWS
9. **Auto-Scaling** — CloudWatch metrics, scale-in/out policies, predictive scaling
10. **Zero-Downtime Deployments** — blue-green with ALB target group swap; rolling update
11. **Backup & Disaster Recovery** — RDS automated backups, S3 versioning, Recovery Time Objective
12. **Cost Optimisation** — Reserved Instances, Savings Plans, Spot for batch, tagging strategy
13. **Multi-Region Considerations** — latency, data residency (Uganda: Africa region), replication
14. **Security Baseline** — CloudTrail, Config Rules, GuardDuty, Security Hub quick setup

**Step 1:** Read the three source materials above.
**Step 2:** Create `SKILL.md` following the content outline. Include CLI commands and Terraform snippets.
**Step 3:** Every section must have a concrete command or configuration example.
**Step 4:** Run `wc -l SKILL.md` — confirm 400–500 lines.
**Step 5:** Commit: `feat(skills): add cloud-architecture skill`

---

### Task 2: Create `kubernetes-platform` skill

**File to create:** `C:\Users\Peter\.claude\skills\kubernetes-platform\SKILL.md`

**Read first:**
- *Kubernetes in Action* (2nd ed.) — Marko Luksa (Chapters 1–12 minimum)
- *Production Kubernetes* — Rosso, Lander, Brand, Harris (security and ops chapters)
- ArgoCD documentation — `argo-cd.readthedocs.io`

**Content outline for SKILL.md (target: 420–490 lines):**

1. **Cluster Architecture** — control plane components, worker nodes, etcd, CNI plugins
2. **Self-Managed Setup** — `kubeadm init` on Debian/Ubuntu VPS, `kubectl` config, node join
3. **Core Workloads** — Deployment, StatefulSet, DaemonSet, Job, CronJob: when to use each
4. **Services & Networking** — ClusterIP, NodePort, LoadBalancer, headless services
5. **Ingress** — Nginx Ingress Controller, TLS termination, path routing, rate limiting annotations
6. **ConfigMaps & Secrets** — external-secrets-operator, Sealed Secrets, Vault Agent Injector
7. **Helm** — chart structure, `values.yaml` override, release management, `helm diff` plugin
8. **Namespaces & RBAC** — namespace strategy, Role vs ClusterRole, RoleBinding, service accounts
9. **Resource Management** — requests vs limits, ResourceQuota, LimitRange, QoS classes
10. **Pod Security** — PodSecurityAdmission (restricted profile), SecurityContext, read-only FS
11. **Auto-Scaling** — HPA (CPU + custom metrics), VPA, KEDA for event-driven scaling
12. **Storage** — PersistentVolume, PVC, StorageClass, CSI drivers, dynamic provisioning
13. **Health Checks** — liveness probe, readiness probe, startup probe: correct configuration
14. **ArgoCD — GitOps** — app-of-apps pattern, sync policy (auto-sync + self-heal), App of Apps
15. **Deployment Strategies** — rolling update, blue-green (2 Deployments + Service swap), canary
16. **Node Operations** — `kubectl drain`, `cordon`, node affinity, taints and tolerations
17. **Observability** — metrics-server, Prometheus ServiceMonitor, kube-state-metrics
18. **Troubleshooting Playbook** — `kubectl describe`, `kubectl logs`, `kubectl exec`, CrashLoopBackOff

**Step 1:** Read Kubernetes in Action chapters 1–12 and Production Kubernetes security chapters.
**Step 2:** Create `SKILL.md`. Include `kubectl` commands and YAML manifests throughout.
**Step 3:** Every section must have a working YAML manifest or `kubectl` command.
**Step 4:** Run `wc -l SKILL.md` — confirm 400–500 lines.
**Step 5:** Commit: `feat(skills): add kubernetes-platform skill`

---

### Task 3: Create `infrastructure-as-code` skill

**File to create:** `C:\Users\Peter\.claude\skills\infrastructure-as-code\SKILL.md`

**Read first:**
- *Terraform: Up & Running* (3rd ed.) — Yevgeniy Brikman (Chapters 1–6)
- *Infrastructure as Code* (2nd ed.) — Kief Morris (patterns chapters)
- ArgoCD documentation — `argo-cd.readthedocs.io`

**Content outline for SKILL.md (target: 400–470 lines):**

1. **Why IaC** — snowflake servers, drift, reproducibility; Terraform vs Ansible: when to use each
2. **Terraform Fundamentals** — providers, resources, data sources, variables, outputs, locals
3. **State Management** — remote state (S3 + DynamoDB state lock), state inspection, import
4. **Modules** — writing reusable modules, input/output variables, module composition
5. **Workspaces** — environment separation (dev/staging/prod), workspace-aware variables
6. **Common Patterns:**
   - VPC with public/private subnets
   - ECS cluster + task definition + service
   - RDS instance with parameter group
   - S3 bucket with versioning and lifecycle
7. **Terraform Testing** — `terraform validate`, `terraform plan` review, Terratest framework
8. **Ansible Fundamentals** — inventory, playbooks, tasks, handlers, variables, templates (Jinja2)
9. **Ansible Roles** — role structure, `defaults/main.yml`, `tasks/main.yml`, Galaxy roles
10. **Idempotency** — writing idempotent tasks, `changed_when`, `failed_when`, check mode
11. **Ansible for Server Config** — Debian/Ubuntu: apt packages, systemd services, ufw rules, users
12. **GitOps with ArgoCD** — application manifest, sync policy, multi-cluster setup, rollback
13. **Flux as Alternative** — Flux v2: GitRepository, Kustomization, HelmRelease
14. **Drift Detection** — `terraform plan` as drift detector, ArgoCD out-of-sync alerts
15. **Secret Injection** — Vault provider for Terraform, Vault Agent for Ansible, ExternalSecrets
16. **IaC Repository Structure** — monorepo vs polyrepo, module registry, environment promotion

**Step 1:** Read Terraform: Up & Running Chapters 1–6.
**Step 2:** Create `SKILL.md`. Include complete HCL blocks and YAML playbook snippets.
**Step 3:** Every section must have working code (Terraform HCL, Ansible YAML, or ArgoCD manifest).
**Step 4:** Run `wc -l SKILL.md` — confirm 380–500 lines.
**Step 5:** Commit: `feat(skills): add infrastructure-as-code skill`

---

### Task 4: Create `cicd-pipelines` skill

**File to create:** `C:\Users\Peter\.claude\skills\cicd-pipelines\SKILL.md`

**Read first:**
- GitHub Actions documentation — `docs.github.com/en/actions`
- *Continuous Delivery* — Humble & Farley (Chapters 1–5 for theory)
- Fastlane documentation — `fastlane.tools/documentation`

**Content outline for SKILL.md (target: 400–470 lines):**

1. **Pipeline Design Principles** — fast feedback, fail fast, single artefact, deploy same binary
2. **GitHub Actions Fundamentals** — workflow syntax, triggers, jobs, steps, matrix strategy
3. **Secrets & Environment Variables** — GitHub Secrets, environment protection rules, OIDC
4. **Node.js / PHP Pipeline** — lint → type-check → test → build Docker → push ECR → deploy
5. **Next.js Pipeline** — type-check → E2E test → build → deploy to Vercel or K8s
6. **Docker Build & Push** — multi-platform build, layer caching, registry push patterns
7. **Kubernetes Deployment** — `kubectl apply` via GitHub Actions, ArgoCD image updater
8. **Environment Promotion** — dev → staging → production with manual approval gate
9. **Test Parallelisation** — matrix for Playwright shards, Jest parallel runners
10. **iOS CI/CD** — Fastlane `match` for code signing, `gym` for build, `deliver` for App Store
11. **Android CI/CD** — Gradle build, Google Play API upload via Fastlane `supply`
12. **Branch Strategy** — GitHub Flow for SaaS (main + feature branches), trunk-based for teams
13. **Semantic Versioning** — conventional commits, `semantic-release` automation, CHANGELOG
14. **Artefact Caching** — npm/composer/gradle cache keys, cache invalidation strategy
15. **Slack/Email Notifications** — failure alerts, deployment announcements, PR status
16. **Security Scanning in CI** — Trivy for Docker images, dependency audit, SAST gate

**Step 1:** Read GitHub Actions documentation (workflows, secrets, environments sections).
**Step 2:** Create `SKILL.md`. Include complete YAML workflow files.
**Step 3:** Include at least 3 complete, runnable GitHub Actions workflow YAML examples.
**Step 4:** Run `wc -l SKILL.md` — confirm 380–500 lines.
**Step 5:** Commit: `feat(skills): add cicd-pipelines skill`

---

### Task 5: Enhance `cicd-devsecops`

**File to modify:** `C:\Users\Peter\.claude\skills\cicd-devsecops\SKILL.md`

Add the following new section: `## Advanced Security Operations`

Sub-sections to add:
- HashiCorp Vault: secret engines, PKI infrastructure, dynamic credentials, auto-rotation
- ISO 27001 controls mapping: Annex A controls relevant to SaaS, evidence collection checklist
- PCI-DSS v4.0: requirements for cardholder data, SAQ A (redirect model), scope reduction
- Falco: runtime threat detection rules, Kubernetes event stream, alert routing
- OPA/Gatekeeper: admission controller policies, constraint templates, violation reporting
- Trivy: container image scanning in CI, SBOM generation, CVE threshold policy

**Step 1:** Read Vault documentation (secret engines + PKI + Kubernetes auth method).
**Step 2:** Append the new section to `cicd-devsecops/SKILL.md`.
**Step 3:** Confirm total file length stays ≤ 500 lines. If it exceeds, split into a references file.
**Step 4:** Commit: `feat(skills): enhance cicd-devsecops with Vault, ISO 27001, Falco/OPA`

---

### Task 6: Enhance `cicd-jenkins-debian`

Add to existing skill: `## Linux Systems Hardening` section covering:
- sysctl hardening: `kernel.randomize_va_space`, `net.ipv4.conf.all.accept_redirects`, TCP hardening
- cgroups v2: resource limits for containers and services, memory.max, cpu.weight
- auditd: audit rules for privileged commands, file access monitoring, log forwarding
- AppArmor profiles for Nginx, MySQL, and Node.js processes
- fail2ban: custom jail rules, ban thresholds, Nginx + SSH jails
- Network stack tuning: BBR congestion control, SO_REUSEPORT, TCP keepalive settings

**Step 1:** Append `## Linux Systems Hardening` section.
**Step 2:** Every tuning parameter must show the exact `sysctl.conf` line or command.
**Step 3:** Confirm file ≤ 500 lines. Split if needed.
**Step 4:** Commit: `feat(skills): enhance cicd-jenkins-debian with Linux systems hardening`

---

### Task 7: Enhance `cicd-pipeline-design`

Add to existing skill: `## FinOps & Cost Governance` section covering:
- Resource tagging strategy: `Environment`, `Team`, `CostCenter`, `Project` tags
- AWS Cost Explorer: cost allocation reports, anomaly detection, budget alerts
- Kubernetes resource quotas: `ResourceQuota` per namespace, cost per namespace tracking
- Utilisation targets: CPU ≥ 70%, memory ≥ 60% — under-utilised instance identification
- Spot instance strategy for non-critical workloads (CI runners, batch jobs)
- FinOps maturity model: crawl → walk → run

**Step 1:** Append `## FinOps & Cost Governance` section.
**Step 2:** Include concrete `ResourceQuota` YAML and AWS CLI budget creation command.
**Step 3:** Confirm file ≤ 500 lines.
**Step 4:** Commit: `feat(skills): enhance cicd-pipeline-design with FinOps cost governance`

---

## Phase Completion Checklist

- [ ] `cloud-architecture` created — 400–500 lines, Docker + AWS CLI examples
- [ ] `kubernetes-platform` created — 400–500 lines, YAML manifests throughout
- [ ] `infrastructure-as-code` created — 380–500 lines, HCL + Ansible YAML examples
- [ ] `cicd-pipelines` created — 380–500 lines, 3 complete workflow YAML examples
- [ ] `cicd-devsecops` enhanced with Vault, ISO 27001, PCI-DSS, Falco/OPA section
- [ ] `cicd-jenkins-debian` enhanced with Linux systems hardening section
- [ ] `cicd-pipeline-design` enhanced with FinOps cost governance section
- [ ] No skill file exceeds 500 lines
- [ ] All 4 new skills cross-reference each other appropriately
- [ ] Git commit made: `feat(skills): complete phase-8 — deployment pipeline & infrastructure`

---

## Reading Material

### Books to Buy

| Priority | Title | Author | Publisher | Price | Why Buy |
|----------|-------|--------|-----------|-------|---------|
| 1 | *Docker Deep Dive* | Nigel Poulton | Self-published | ~$35 | **Start here.** The best concise Docker book — images, containers, Compose, Swarm, security. 220 pages. Read before writing `cloud-architecture`. |
| 2 | *Kubernetes in Action* (2nd ed.) | Marko Luksa | Manning | ~$55 | The most thorough K8s book. Every object type, pattern, and operation explained with examples. Read before writing `kubernetes-platform`. |
| 3 | *Terraform: Up & Running* (3rd ed.) | Yevgeniy Brikman | O'Reilly | ~$55 | The definitive Terraform book — modules, state, testing, patterns. Read before writing `infrastructure-as-code`. |
| 4 | *Continuous Delivery* | Jez Humble & David Farley | Addison-Wesley | ~$50 | The CI/CD theory bible — pipeline design, deployment strategies, configuration management. Read before writing `cicd-pipelines`. |
| 5 | *Infrastructure as Code* (2nd ed.) | Kief Morris | O'Reilly | ~$55 | IaC patterns beyond Terraform basics — team workflows, testing, governance. Companion to Brikman. |
| 6 | *Production Kubernetes* | Rosso, Lander, Brand, Harris | O'Reilly | ~$55 | Ops-grade K8s — security hardening, multi-tenancy, cost management. Read after Luksa. |
| 7 | *The DevOps Handbook* (2nd ed.) | Kim, Humble, Debois, Willis | IT Revolution | ~$40 | Culture and practices behind CI/CD — the why behind every pipeline decision. |

### Free Resources

- AWS Well-Architected Framework — `aws.amazon.com/architecture/well-architected` — official AWS patterns (free PDF)
- GitHub Actions documentation — `docs.github.com/en/actions` — the authoritative Actions reference
- ArgoCD documentation — `argo-cd.readthedocs.io` — GitOps patterns, app-of-apps
- Helm documentation — `helm.sh/docs` — chart authoring, release management
- HashiCorp Vault documentation — `developer.hashicorp.com/vault` — secret engines, PKI, K8s auth
- Falco documentation — `falco.org/docs` — runtime security rules and alert routing
- OPA/Gatekeeper documentation — `open-policy-agent.github.io/gatekeeper` — admission control policies
- Fastlane documentation — `fastlane.tools/documentation` — iOS/Android CI/CD automation
- Trivy documentation — `trivy.dev` — container image and IaC scanning

---

*Next phase: [Phase 9 — Production Operations, Observability & SRE](phase-09.md)*
