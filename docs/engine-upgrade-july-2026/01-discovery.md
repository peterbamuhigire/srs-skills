# Discovery

Engine root: `C:\wamp64\www\srs-skills`
Discovery date: 2026-07-07

## What Was Read

I read the root router/controller files where present (`README.md`, `AGENTS.md`, `CLAUDE.md`) and read every discovered `SKILL.md` file in full. I also read every Markdown file matching governance, doctrine, standard, quality, anti-slop, architecture, router, guide, index, policy, protocol, or changelog naming patterns into the audit manifest. The full content inventory is in `10-appendix-file-inventory.md`.

## Tree Metrics

| Metric | Value |
| --- | --- |
| Files | 3190 |
| Directories | 864 |
| Maximum directory depth | 10 |
| Total content size | 31.32 MB |
| SKILL.md files | 147 |
| Governance/doctrine/standard files read | 618 |

## Unusual Findings

- Empty directories found: 8.
- Duplicate-content hash groups found: 20 sampled groups.

## Architecture Map

This engine claims to generate standards-driven software lifecycle documentation: PRDs, SRS documents, design docs, test plans, deployment/runbook material, Agile artefacts, governance records, and regulated evidence packs. A world-class deliverable in this domain looks like a signed-off IEEE/ISO-aligned requirements and design pack from a top systems integrator or regulated-product consultancy: traceable, testable, stakeholder-grounded, legally reviewable, implementation-ready, and backed by repeatable validation evidence. Benchmark: IBM/Thoughtworks-level requirements engineering plus regulated V&V discipline comparable to IEEE 29148 / IEEE 1012 delivery in safety- or audit-sensitive programmes.

The engine is organized as a hierarchical skill engine with filesystem-discovered `SKILL.md` entrypoints, router/controller Markdown at the root, and supporting assets in references, templates, scripts, examples, docs, projects, fonts, or tools depending on the engine. The architecture is strongest where routers tell the agent to glob `SKILL.md` fresh and weakest where empty directories, local project workspaces, or missing frontmatter create false surfaces.

## Asset Catalogue

| Extension/type | Count |
| --- | --- |
| .md | 2445 |
| .docx | 297 |
| .yaml | 123 |
| .py | 118 |
| .prompt | 100 |
| .png | 40 |
| .json | 11 |
| .sh | 11 |
| .jpg | 10 |
| .ps1 | 10 |
| [no extension] | 10 |
| .html | 4 |
| .j2 | 3 |
| .zip | 3 |
| .css | 1 |
| .csv | 1 |
| .template | 1 |
| .toml | 1 |
| .yml | 1 |

Supporting asset counts from path classification: references=260, templates=33, examples=10, scripts/script-like=139.

## Skill Frontmatter Quotation

The table quotes the discovered `name` and `description` frontmatter values. `[MISSING]` means the field was not present in the file frontmatter.

| Skill path | name | description |
| --- | --- | --- |
| 01-strategic-vision/01-prd-generation/SKILL.md | name: prd-generation | description: Generate a Product Requirements Document with market context, objectives, success metrics, and feature priority matrix per IEEE 29148 and IEEE 1233. |
| 01-strategic-vision/02-business-case/SKILL.md | name: business-case | description: Generate a business case document with problem analysis, cost-benefit analysis, ROI projection, risk assessment, and go/no-go criteria per IEEE 1058. |
| 01-strategic-vision/03-vision-statement/SKILL.md | name: vision-statement | description: Generate a formal project vision document with elevator pitch, product positioning, value propositions, and success criteria per IEEE 29148 Sec 6.2. |
| 01-strategic-vision/04-lean-canvas/SKILL.md | name: 04-lean-canvas | description: Generate a Lean Canvas, Impact Map, and Hypothesis Board for MVP, startup, exploratory, SaaS, AI, website, mobile, or uncertain projects as a lightweight alternative or precursor to full PRD. Use when assumptions, customer discovery, measurable goals, outcome traceability, and validation thresholds must drive requirements. |
| 01-strategic-vision/05-system-overview/SKILL.md | name: system-overview | description: Generate a system overview document understandable by every project stakeholder — required by Royce Step 1 |
| 01-strategic-vision/06-ai-economic-value-brief/SKILL.md | name: ai-economic-value-brief | description: Use when creating the strategic brief for an AI-powered system, AI feature, agentic workflow, analytics product, or automation initiative. Converts AI ambition into business outcomes, measurable requirements, data needs, risk controls, and a defensible delivery roadmap. |
| 01-strategic-vision/07-premium-product-positioning/SKILL.md | name: 07-premium-product-positioning | description: Generate or review premium product positioning, PRD/SRS inputs, and design requirements for systems intended for premium, affluent, executive, enterprise, luxury, high-ticket, or elite users. Use when software must justify premium pricing, win high-level buyers, or feel materially better than ordinary alternatives. |
| 01-strategic-vision/10-saas-mvp-scoping-doc/SKILL.md | name: saas-mvp-scoping-doc | description: Generate a SaaS MVP & Stair-Step Scoping Document: in/out for v1, single acquisition channel committed, escape-velocity success thresholds, feature-triage decision log. |
| 01-strategic-vision/11-saas-moat-and-defensibility-plan/SKILL.md | name: saas-moat-and-defensibility-plan | description: Generate a Moat & Defensibility Plan: which moat types apply (integrations / brand / owned channels / switching costs / data / network effect), which are false moats to avoid, milestones, and the roadmap to harden each. |
| 01-strategic-vision/12-saas-pricing-and-packaging-spec/SKILL.md | name: saas-pricing-and-packaging-spec | description: Generate a SaaS Pricing & Packaging Specification: tiers, value metric, feature gates, expansion mechanics, freemium decision, grandfathering, price-raise policy, public price-page contract, enterprise contact-us path. |
| 01-strategic-vision/13-ai-feature-strategy-doc/SKILL.md | name: ai-feature-strategy-doc | description: Generate the AI Feature Strategy Doc for a SaaS product: AI feature inventory by tier, differentiating-vs-table-stakes split, build-vs-buy decisions on models, moat analysis, sequencing, and the AI-feature go-to-market position. |
| 01-strategic-vision/14-ai-agent-strategy-doc/SKILL.md | name: ai-agent-strategy-doc | description: Generate the AI Agent Strategy Doc: when to use an agent vs a workflow or a single LLM call, agent capability ladder by pricing tier, autonomy-level taxonomy (suggest / approve-each / approve-batch / autonomous), proprietary action catalogue and tool-telemetry moat, and the agent-feature sequencing roadmap. |
| 02-requirements-engineering/13-saas-billing-and-metering-spec/SKILL.md | name: saas-billing-and-metering-spec | description: Generate a SaaS Billing & Metering Specification: the event catalogue, granularity, tenant-context propagation, transport bus, retention, aggregation, ERP/finance handoff, revenue-recognition rules per ASC 606 / IFRS 15, dunning, refund/credit handling — all as testable requirements. |
| 02-requirements-engineering/14-ai-feature-prd-spec/SKILL.md | name: ai-feature-prd-spec | description: Generate the AI-Feature PRD Spec: IEEE 830-form requirements for every AI-powered feature, with hallucination tolerance, latency budget, $/call ceiling, abstain criteria, citation policy, consent and training-data exclusion clauses, and acceptance tests anchored to the eval harness. |
| 02-requirements-engineering/15-ai-data-and-knowledge-base-spec/SKILL.md | name: ai-data-and-knowledge-base-spec | description: Generate the AI Data and Knowledge-Base Spec: the canonical record of what data feeds AI features, per-tenant vs shared scope, ingestion SLA, freshness, retention, lineage, training-data exclusion, and the cross-tenant leak controls for embeddings and conversation logs. |
| 02-requirements-engineering/16-ai-agent-feature-prd-spec/SKILL.md | name: ai-agent-feature-prd-spec | description: Generate the AI Agent Feature PRD Spec: IEEE 830-form requirements for every agentic feature, with task scope, autonomy level, action-catalogue summary, intervention triggers, success metrics, max-step / max-cost / wallclock budgets, abstain criteria, and irreversible-action gates anchored to the agent eval and red-team registries. |
| 02-requirements-engineering/17-ai-agent-action-catalogue-spec/SKILL.md | name: ai-agent-action-catalogue-spec | description: Generate the Action Catalogue Spec: the enumerated, schema-bound set of tools an agent may call. Every tool declares input/output schema, side-effect class, reversibility class, per-tier availability, audit fields, rate-limit class, and kill-switch behaviour. This is the contract between the planner, the dispatcher, and the operator. |
| 02-requirements-engineering/18-embedded-accounting-engine-srs/SKILL.md | name: embedded-accounting-engine-srs | description: Generate the SRS subsection for any system that handles money, inventory value, payroll, tax, grants, fees, payments, receivables, payables, fixed assets, or financial reporting. Specifies embedded accounting engine requirements: chart of accounts, mapping layer, LedgerPostingService, append-only journals, subledgers, accounting periods, reversals, reports, audit trail, IFRS/IFRS for SMEs/local tax context, and integrity invariants. |
| 02-requirements-engineering/agile/01-user-story-generation/SKILL.md | name: user-story-generation | description: Generate IEEE 29148-aligned user stories from project context with INVEST criteria compliance, acceptance criteria, and story point estimation for Agile projects |
| 02-requirements-engineering/agile/02-acceptance-criteria/SKILL.md | name: acceptance-criteria | description: Formalize Gherkin-format acceptance criteria (Given-When-Then) for each user story, ensuring deterministic pass/fail testability per IEEE 29148 Sec 6.4.5. |
| 02-requirements-engineering/agile/03-story-mapping/SKILL.md | name: story-mapping | description: Build Jeff Patton story maps with backbone user activities, walking skeleton, and release slices to visualize product scope per IEEE 29148. |
| 02-requirements-engineering/agile/04-backlog-prioritization/SKILL.md | name: backlog-prioritization | description: Prioritize the product backlog using MoSCoW classification and WSJF scoring, then allocate stories to sprints with a release plan per IEEE 29148 Sec 6.4.6. |
| 02-requirements-engineering/fundamentals/after/08-requirements-management/SKILL.md | name: requirements-management | description: Establish requirements baselines, change control processes, and version management for living requirements documents per IEEE 29148 Section 6.7. |
| 02-requirements-engineering/fundamentals/after/09-traceability-engineering/SKILL.md | name: traceability-engineering | description: Establish forward and backward traceability links between business goals, requirements, design elements, and test cases per IEEE 1012 and IEEE 29148. |
| 02-requirements-engineering/fundamentals/after/10-requirements-metrics/SKILL.md | name: requirements-metrics | description: Score requirements artifacts against quantitative quality metrics and enforce quality gate thresholds per IEEE 29148 and IEEE 982.1. |
| 02-requirements-engineering/fundamentals/after/11-requirements-reuse/SKILL.md | name: requirements-reuse | description: Identify reusable requirements patterns and build a requirements library for product line engineering per IEEE 29148 and Laplante Ch.9. OPTIONAL skill. |
| 02-requirements-engineering/fundamentals/after/12-solution-evaluation-and-transition/SKILL.md | name: solution-evaluation-and-transition | description: Plan organizational transition, go/no-go evidence, adoption readiness, and post-implementation solution evaluation after requirements and delivery artifacts exist. |
| 02-requirements-engineering/fundamentals/before/01-stakeholder-analysis/SKILL.md | name: stakeholder-analysis | description: Identify, classify, and prioritize stakeholders using power/interest grids. Generate a stakeholder register with communication preferences per IEEE 29148 and Wiegers Practices 1-3. |
| 02-requirements-engineering/fundamentals/before/02-elicitation-toolkit/SKILL.md | name: elicitation-toolkit | description: Multi-technique requirements gathering skill that guides the AI through choosing and executing the right elicitation techniques per IEEE 29148 Section 6.3 and Wiegers Practices 4-6. |
| 02-requirements-engineering/fundamentals/before/03-brd-generation/SKILL.md | name: brd-generation | description: Generate a Business Requirements Document bridging strategic vision to technical requirements. Includes a decision gate for determining BRD necessity. Per IEEE 29148 Section 6.4 and Business Requirements Gathering Ch.2-4. |
| 02-requirements-engineering/fundamentals/before/04-business-analysis-planning/SKILL.md | name: business-analysis-planning | description: Plan business analysis governance, stakeholder engagement, decision rights, work cadence, and artifact strategy before detailed requirements work begins. |
| 02-requirements-engineering/fundamentals/during/04-requirements-analysis/SKILL.md | name: requirements-analysis | description: Analyze, classify, detect conflicts, assess feasibility, and prioritize gathered requirements per IEEE 29148 Section 6.5 and Wiegers Practices 7-9. |
| 02-requirements-engineering/fundamentals/during/05-conceptual-data-modeling/SKILL.md | name: conceptual-data-modeling | description: Build entity-relationship models from business language, capturing data requirements at the conceptual level per IEEE 1016 and Book 2 data architecture principles. |
| 02-requirements-engineering/fundamentals/during/06-requirements-patterns/SKILL.md | name: requirements-patterns | description: Apply proven specification patterns (decision tables, state transitions, CRUD matrices) to structure complex requirement behavior per IEEE 830 and Wiegers Practices 10-12. |
| 02-requirements-engineering/fundamentals/during/07-requirements-validation/SKILL.md | name: requirements-validation | description: Validate requirements quality through structured reviews, inspections, and prototype testing before baselining per IEEE 1012-2016, Laplante Ch.6, and Wiegers Practices 13-14. |
| 02-requirements-engineering/fundamentals/during/08-business-process-modeling/SKILL.md | name: business-process-modeling | description: Model as-is and to-be business processes, actors, handoffs, exceptions, and control points to clarify requirements before detailed specification or design. |
| 02-requirements-engineering/fundamentals/during/09-business-rules-analysis/SKILL.md | name: business-rules-analysis | description: Capture, classify, normalize, and validate business rules so policy, calculations, decisions, and constraints are explicit before specification and design. |
| 02-requirements-engineering/fundamentals/during/10-prototyping-and-solution-discovery/SKILL.md | name: prototyping-and-solution-discovery | description: Generate and compare candidate solutions, prototypes, and discovery experiments to reduce uncertainty before locking requirements or design. |
| 02-requirements-engineering/fundamentals/during/11-experience-mapping-requirements/SKILL.md | name: 11-experience-mapping-requirements | description: Convert stakeholder journeys, customer journeys, employee journeys, ecosystem maps, and future-state experience maps into traceable SDLC requirements. Use when discovery must turn observed touchpoints, pain points, service evidence, emotions, and journey stages into PRD, SRS, backlog, UX, testing, rollout, and governance inputs. |
| 02-requirements-engineering/fundamentals/during/12-service-blueprint-requirements/SKILL.md | name: 12-service-blueprint-requirements | description: Convert service blueprints into requirements for frontstage UX, backstage operations, support, evidence, handoffs, failures, recovery, implementation, rollout, maintenance, and governance. Use for SaaS, websites, mobile apps, public-sector services, AI systems, and service-heavy products where delivery depends on people, process, policy, and technology working together. |
| 02-requirements-engineering/hybrid/hybrid-synchronization/SKILL.md | name: hybrid-synchronization | description: Use when a project is Hybrid (Water-Scrum-Fall). Generates _context/methodology.md, _registry/baseline-trace.yaml, and 07-agile-artifacts/definitions/dor-dod.md so Agile execution stays bound to the Waterfall baseline. |
| 02-requirements-engineering/retail-operating-model-srs/SKILL.md | name: retail-operating-model-srs | description: Generate retail SRS sections for omnichannel retail, merchandising, pricing, promotions, markdowns, loyalty, CRM, e-commerce, fulfilment, returns, store operations, shrink, vendor funding, private label, planograms, and KPI/WBR dashboards as testable software requirements with finance/control gates. |
| 02-requirements-engineering/waterfall/01-initialize-srs/SKILL.md | name: initialize-srs | description: Set up IEEE Std 830-1998 and US ISO/IEC 25051 compliant project context files so downstream SRS skills can operate with stakeholder data, quality criteria, and definitions. |
| 02-requirements-engineering/waterfall/02-context-engineering/SKILL.md | name: context-engineering | description: Synthesize Section 1.0 (Introduction) by reading vision.md and glossary.md, and write a standardized SRS Draft that captures purpose, scope, definitions, references, and overview with ISO/IEEE rigor. |
| 02-requirements-engineering/waterfall/03-descriptive-modeling/SKILL.md | name: descriptive-modeling | description: Build Section 2.0 by analyzing tech_stack.md, features.md, and quality_standards.md to describe product perspective, functions, users, constraints, and dependencies with ISO/IEEE rigor. |
| 02-requirements-engineering/waterfall/04-interface-specification/SKILL.md | name: interface-specification | description: Define Section 3.1 by mapping tech_stack.md and features.md into detailed user, hardware, software, and communications interfaces that cite ISO/IEEE requirements. |
| 02-requirements-engineering/waterfall/05-feature-decomposition/SKILL.md | name: feature-decomposition | description: Convert features.md into IEEE 830 Section 3.2 (Functional Requirements) using a Functional Decomposition Tree with stimulus/response pairs and verifiable \"shall\" clauses. |
| 02-requirements-engineering/waterfall/06-logic-modeling/SKILL.md | name: logic-modeling | description: Capture Section 3.2.2, 3.2.3, and 3.2.4 by transforming business rules, the technology stack, and quality standards into transition-aware logic and data constructs. |
| 02-requirements-engineering/waterfall/07-attribute-mapping/SKILL.md | name: attribute-mapping | description: Turn the prioritized ISO/IEC 25010 quality characteristics and technology stack into Sections 3.3–3.5.4 by documenting measurable performance, constraints, and software system attributes. |
| 02-requirements-engineering/waterfall/08-semantic-auditing/SKILL.md | name: semantic-auditing | description: Validate the full SRS and create a Requirements Traceability Matrix plus audit report following IEEE 1012 and IEEE 830. |
| 02-requirements-engineering/waterfall/09-use-case-modeling/SKILL.md | name: use-case-modeling | description: Generate UML use case models with fully-dressed use case descriptions, use case diagrams, and activity diagrams for complex business processes per UML 2.5 and IEEE 29148. |
| 03-design-documentation/01-high-level-design/SKILL.md | name: high-level-design | description: Generate a High-Level Design document with system architecture, component diagrams, deployment topology, data flow, and technology decisions per IEEE 1016-2009. |
| 03-design-documentation/02-low-level-design/SKILL.md | name: low-level-design | description: Generate a Low-Level Design document with module specifications, class diagrams, sequence diagrams, state machines, and algorithm detail per IEEE 1016-2009 Sec 6. |
| 03-design-documentation/03-api-specification/SKILL.md | name: api-specification | description: Generate API specification with endpoint definitions, request/response schemas, authentication, error codes, and an OpenAPI 3.0 YAML artifact per IEEE 29148. |
| 03-design-documentation/04-database-design/SKILL.md | name: database-design | description: Generate a database design document with ERD, normalization analysis, table definitions, indexes, constraints, migration strategy, and data dictionary per IEEE 1016 Sec 6.7. |
| 03-design-documentation/05-ux-specification/SKILL.md | name: 05-ux-specification | description: Generate a comprehensive UX specification document covering information architecture, wireframing standards, design system documentation, usability testing protocols, and design handoff specs per ISO 9241-210 and ISO 25010. |
| 03-design-documentation/06-infrastructure-design/SKILL.md | name: infrastructure-design | description: Generate an Infrastructure Design document for systems requiring high availability, scalability, or distributed architecture. OPTIONAL skill with a score-based decision gate per IEEE 1016-2009 and ISO 25010. |
| 03-design-documentation/07-iot-system-design/SKILL.md | name: iot-system-design | description: Generate IoT system design documentation covering device, edge, connectivity, cloud, security, lifecycle, and operational architecture for connected products. |
| 03-design-documentation/08-engineering-strategy-brief/SKILL.md | name: 08-engineering-strategy-brief | description: Produce an engineering strategy brief that connects business goals, product outcomes, architecture diagnosis, guiding policies, operating mechanisms, ADRs, SaaS assumptions, implementation sequencing, and governance. Use before major HLD, infrastructure, platform, AI, SaaS, public-sector, or modernization decisions. |
| 03-design-documentation/09-ux-content-and-form-specification/SKILL.md | name: 09-ux-content-and-form-specification | description: Produce UX content, microcopy, form, validation, error-state, empty-state, accessibility, and completion-metric specifications for web, mobile, SaaS, AI, public-sector, and premium product interfaces. Use when wording, form flow, labels, help text, confirmation, errors, and content quality must become testable requirements. |
| 03-design-documentation/10-saas-multi-tenancy-architecture-spec/SKILL.md | name: saas-multi-tenancy-architecture-spec | description: Generate a Multi-Tenancy Architecture Specification for a SaaS system covering control-plane / application-plane decomposition, per-microservice tenancy pattern (silo / pool / mixed / pod / VPC-per-tenant), tenant-context propagation, isolation strategy, noisy-neighbor controls, and ADR seeds per Golding (2024). |
| 03-design-documentation/11-ai-architecture-spec/SKILL.md | name: ai-architecture-spec | description: Generate the AI Architecture Specification: RAG vs fine-tune vs agent decisions, model gateway, vector store, eval harness, observability, security boundaries, and the SaaS-specific multi-tenant AI plane that the generic HLD does not capture. |
| 03-design-documentation/12-ai-model-card/SKILL.md | name: ai-model-card | description: Generate the AI Model Card per deployed AI feature: purpose, training data summary, evaluation metrics, limitations, bias notes, intended and out-of-scope use, version pin, and the EU AI Act Annex IV technical-documentation cross-walk. |
| 03-design-documentation/13-ai-prompt-and-system-message-spec/SKILL.md | name: ai-prompt-and-system-message-spec | description: Generate the AI Prompt and System-Message Spec: versioned prompt registry layout, change-control workflow, regression-eval attachment, jailbreak-resistant system-message patterns, retrieval-context formatting, and the deployment / rollback procedure for prompts. |
| 03-design-documentation/14-ai-agent-architecture-spec/SKILL.md | name: ai-agent-architecture-spec | description: Generate the AI Agent Architecture Spec: agent runtime loop, state machine, memory tiers (scratchpad, episodic, long-term), planner, tool dispatcher, supervisor (for multi-agent), durability and resumability, kill-switch wiring, and per-tenant isolation. Sits alongside the AI Architecture Spec and is mandatory for any product shipping an agent. |
| 03-design-documentation/15-ai-agent-multi-agent-coordination-spec/SKILL.md | name: ai-agent-multi-agent-coordination-spec | description: Generate the Multi-Agent Coordination Spec: topology choice (single-agent / supervisor-worker / debate / handoff chain), scratchpad isolation between agents, supervision policy, message-bus contract, and failure-mode handling specific to multi-agent systems. |
| 03-design-documentation/16-accounting-engine-design/SKILL.md | name: accounting-engine-design | description: Generate the SDS/HLD/LLD design for an embedded accounting engine: canonical data model, append-only journal tables, chart of accounts, mapping tables, accounting periods, LedgerPostingService interface, idempotency, reversal workflow, subledger tagging, materialized balance rebuilds, audit trail, and IFRS/IFRS for SMEs reporting projections. |
| 04-development-artifacts/01-technical-specification/SKILL.md | name: technical-specification | description: Generate a detailed technical specification bridging LLD to implementation with module contracts, data formats, and integration specifications per IEEE 1016 and IEEE 830. |
| 04-development-artifacts/02-coding-guidelines/SKILL.md | name: coding-guidelines | description: Generate language-specific coding standards with naming conventions, patterns, anti-patterns, and code quality metrics per IEEE 730. |
| 04-development-artifacts/03-dev-environment-setup/SKILL.md | name: dev-environment-setup | description: Generate development environment setup documentation with toolchain requirements, dependency installation, local configuration, and build instructions per IEEE 1074. |
| 04-development-artifacts/04-contribution-guide/SKILL.md | name: contribution-guide | description: Generate a contribution guide with branching strategy, PR process, commit conventions, review checklist, and code of conduct per IEEE 1074. |
| 04-development-artifacts/05-ai-agent-coding-guidelines-addendum/SKILL.md | name: ai-agent-coding-guidelines-addendum | description: Generate the AI Agent Coding Guidelines Addendum: tool-schema discipline, irreversibility annotations, blast-radius caps, deterministic state, idempotency keys for tool calls, error and timeout policy, and the test contract for agent-runtime code. |
| 05-testing-documentation/01-test-strategy/SKILL.md | name: test-strategy | description: Generate an overall test strategy defining test levels, types, tools, environments, and entry/exit criteria per BS ISO/IEC/IEEE 29119-3 Section 6. |
| 05-testing-documentation/02-test-plan/SKILL.md | name: test-plan | description: Generate a detailed test plan with test cases, requirement traceability, test data, schedule, and resource allocation per BS ISO/IEC/IEEE 29119-3 Sections 7-8. |
| 05-testing-documentation/03-test-report/SKILL.md | name: test-report | description: Generate a test execution report template with results summary, defect log, coverage metrics, and pass/fail analysis per BS ISO/IEC/IEEE 29119-3 Sections 9-10. |
| 05-testing-documentation/04-ai-eval-harness-spec/SKILL.md | name: ai-eval-harness-spec | description: Generate the AI Eval Harness Spec: golden datasets per feature, regression criteria, A/B prompt eval, judge-LLM patterns, CI gate definition, scheduled regression, and the operational ownership of eval as a production system. |
| 05-testing-documentation/05-ai-red-team-test-plan/SKILL.md | name: ai-red-team-test-plan | description: Generate the AI Red-Team Test Plan: adversarial scenarios across prompt injection, jailbreak, data exfiltration, cross-tenant leakage, PII surfacing, hallucination probe, agent tool misuse, and bias surfacing; severity matrix; CI smoke set and weekly full-run; sign-off rules. |
| 05-testing-documentation/06-ai-agent-eval-spec/SKILL.md | name: ai-agent-eval-spec | description: Generate the AI Agent Eval Spec: agent task-success metric, step efficiency, tool-choice quality, hallucinated-argument rate, irreversible-action rate, intervention rate, golden-task sets, replay-based eval against a deterministic synthetic environment, and CI gates. Extends the AI Eval Harness Spec; does not replace it. |
| 05-testing-documentation/07-ai-agent-red-team-test-plan/SKILL.md | name: ai-agent-red-team-test-plan | description: Generate the AI Agent Red-Team Test Plan: adversarial scenarios specific to agent systems — indirect prompt injection via tool output, action escalation, tenant data exfil via tool output, recursive self-modify, jailbreak via memory, agent-vs-supervisor confusion, budget-exhaustion DoS, and cross-tenant tool routing. Severity matrix, CI smoke set, weekly full run, sign-off rules. Extends the AI Red-Team Test Plan. |
| 05-testing-documentation/08-accounting-engine-test-plan/SKILL.md | name: accounting-engine-test-plan | description: Generate mandatory accounting-engine test plans for systems that handle money: debit-credit equality, trial balance, balance sheet equation, control-account-to-subledger reconciliation, inventory GL tie-out, period locks, idempotency keys, reversal-only correction, tenant isolation, report rebuilds, payroll/FX/fixed-asset/inventory posting tests, and no direct ledger writes. |
| 06-deployment-operations/01-deployment-guide/SKILL.md | name: deployment-guide | description: Generate a step-by-step deployment procedure with pre-checks, deployment steps, rollback procedures, and post-deployment verification per IEEE 1062. |
| 06-deployment-operations/02-runbook/SKILL.md | name: runbook | description: Generate an operational runbook with incident response procedures, monitoring alert responses, escalation paths, and common fix recipes following SRE best practices. |
| 06-deployment-operations/03-monitoring-setup/SKILL.md | name: monitoring-setup | description: Generate monitoring and alerting design documentation with metrics definitions, alert thresholds, dashboard specifications, and health check endpoints per ISO/IEC 25010. |
| 06-deployment-operations/04-infrastructure-docs/SKILL.md | name: infrastructure-docs | description: Generate infrastructure documentation with architecture diagrams, resource specifications, network topology, and IaC references per IEEE 1016. |
| 06-deployment-operations/05-go-live-readiness/SKILL.md | name: 05-go-live-readiness | description: Generate a go-live readiness assessment and launch control plan that verifies the system is operationally, organizationally, and commercially ready for release. |
| 06-deployment-operations/06-customer-adoption-and-support-plan/SKILL.md | name: 06-customer-adoption-and-support-plan | description: Generate customer adoption, training, rollout communication, service desk, escalation, recovery, maintenance, and post-launch support plans for SDLC deliverables. Use before pilots, go-live, SaaS rollout, public-sector launch, website launch, AI system adoption, or premium client handover. |
| 06-deployment-operations/07-saas-tenant-lifecycle-runbook/SKILL.md | name: saas-tenant-lifecycle-runbook | description: Generate an operational runbook covering the SaaS tenant lifecycle: provisioning, tier change, suspension, reactivation, offboarding, data export, hard delete, and retention obligations — each with detection, procedure, verification, audit-trail, and customer-comms requirements. |
| 06-deployment-operations/08-saas-slo-and-error-budget-doc/SKILL.md | name: saas-slo-and-error-budget-doc | description: Generate the SaaS SLO and Error-Budget Specification: SLIs per service, per-tier SLO targets (Bronze / Silver / Gold / Enterprise), error-budget math, burn-rate alerts, freeze rules, and the mapping from internal SLOs to customer-facing SLA commitments. |
| 06-deployment-operations/09-saas-incident-response-and-postmortem/SKILL.md | name: saas-incident-response-and-postmortem | description: Generate a SaaS-tuned Incident Response & Postmortem documentation pack: severity matrix that distinguishes tenant-scope vs platform-scope, blast-radius reporting, customer-comms templates per severity, status-page protocol, and the blameless postmortem template. |
| 06-deployment-operations/10-ai-hallucination-slo-doc/SKILL.md | name: ai-hallucination-slo-doc | description: Generate the AI Hallucination SLO Doc: SLIs for factuality, citation accuracy, and abstention; per-feature SLO targets; error budgets; multi-burn-rate alerts; freeze rules; and the mapping from internal AI SLOs to customer-facing AI-quality commitments. |
| 06-deployment-operations/11-ai-feature-rollout-runbook/SKILL.md | name: ai-feature-rollout-runbook | description: Generate the AI Feature Rollout Runbook: staged rollout (internal -> design partners -> opt-in beta -> percentage cohort -> GA), canary cohort definition, auto-rollback triggers tied to eval and SLO, comms plan, opt-in/out handling, and the post-launch monitoring window. |
| 06-deployment-operations/12-ai-cost-runbook/SKILL.md | name: ai-cost-runbook | description: Generate the AI Cost Runbook: per-tenant cost monitoring, per-feature ceilings, spend anomaly response, throttle and pause rules, model-fallback policy on cost overrun, FinOps cadence, and the per-tenant billing event reconciliation for AI usage. |
| 06-deployment-operations/13-ai-agent-slo-doc/SKILL.md | name: ai-agent-slo-doc | description: Generate the AI Agent SLO Doc: SLIs for task success, step efficiency, intervention rate, irreversible-action-incident rate, agent-task availability, and agent-cost-per-run; per-feature SLO targets by tier; error budgets; multi-burn-rate alerts; freeze and pause rules; mapping to customer-facing agent commitments. |
| 06-deployment-operations/13-ai-incident-severity-matrix/SKILL.md | name: ai-incident-severity-matrix | description: Generate the AI Incident Severity Matrix: three-dimensional severity (sev x tenant-scope x autonomy/blast-radius); per-AI-failure-class thresholds (hallucination spike, prompt drift, model regression, jailbreak/injection, tool-chain failure, cost runaway, agent-action incident, retrieval drift, eval drift); mapping to customer-SLA service credits and EU AI Act Article 73 serious-incident definitions. |
| 06-deployment-operations/14-ai-agent-runbook/SKILL.md | name: ai-agent-runbook | description: Generate the AI Agent Runbook: kill-switch (global, per-tenant, per-feature), force-pause, force-resume, replay-a-run, agent-task quarantine, audit-log review cadence, agent-incident handling playbooks, and the operator-on-call rotation for agent-specific incidents. |
| 06-deployment-operations/14-ai-incident-response-runbook/SKILL.md | name: ai-incident-response-runbook | description: Generate the AI Incident Response Runbook: timed first-five / first-thirty / first-two-hour playbook; per-failure-class procedures (hallucination spike, prompt drift, model regression, jailbreak/injection, tool-chain failure, cost runaway, agent-action incident, training-data shift, retrieval drift, eval drift); kill-switch, model-fallback, prompt-rollback, index-pinning, abstain-mode, and read-only-mode procedures. |
| 06-deployment-operations/15-ai-agent-rollout-runbook/SKILL.md | name: ai-agent-rollout-runbook | description: Generate the AI Agent Rollout Runbook: staged rollout (Internal → Dogfood → Shadow → Canary → Tier → GA), the shadow-mode pattern (agent proposes; human acts), promotion gates tied to agent eval + agent red-team + agent SLO, auto-rollback triggers, comms plan, opt-in/out per region, and the post-launch monitoring window. |
| 06-deployment-operations/15-ai-rca-taxonomy-doc/SKILL.md | name: ai-rca-taxonomy-doc | description: Generate the AI RCA (Root-Cause Analysis) Taxonomy Doc: full catalogue of AI failure root causes across six families — model (regression, deprecation, fine-tune drift, distribution shift, prompt regression), retrieval (index drift, embedding-model change, citation drift), tool/agent (tool API change, schema change, vendor outage, indirect injection, action-scope expansion), eval (test-set rot, judge drift, golden-set leakage), data (training-data shift), infra (gateway routing change), commercial (provider price change, rate-limit change). Each node carries an example incident and a default mitigation pointer. |
| 06-deployment-operations/16-ai-incident-postmortem-template/SKILL.md | name: ai-incident-postmortem-template | description: Generate the blameless AI Incident Postmortem template: timeline, RCA classification (against the AI RCA taxonomy), contributing factors, per-tenant impact, regulator-impact assessment, action items by class (improve eval, change gate, add red-team test, etc.), public publication policy. |
| 06-deployment-operations/17-ai-incident-evidence-pack-spec/SKILL.md | name: ai-incident-evidence-pack-spec | description: Generate the AI Incident Evidence Pack Spec: what evidence to preserve when an AI incident occurs — trace bundle, prompt + model + tool versions at the time of the incident, retrieval set, eval output at the time of the incident, customer-affected list, action audit log, reproduce script, model-price-table snapshot. Defines chain-of-custody, retention, redaction policy, and the regulator-handover format. |
| 06-deployment-operations/20-ai-agent-compliance-runbook/SKILL.md | name: ai-agent-compliance-runbook | description: Generate the AI Agent Compliance Runbook: the operational runbook for continuous compliance — drill schedule, evidence-collection schedule, control-test schedule, audit-window operations, on-the-day auditor playbook activation, gap-remediation cadence. Operates the artefacts produced by the SOC 2 / ISO / HIPAA control packs, policy pack, evidence pack spec, and attestation preparation spec. |
| 06-deployment-operations/21-accounting-operations-runbook/SKILL.md | name: accounting-operations-runbook | description: Generate operations runbooks for embedded accounting systems: go-live opening balances, period close, ledger integrity jobs, reconciliation failures, duplicate/missing postings, report rebuilds, materialized balance rebuilds, FX revaluation, depreciation, payroll remittance checks, locked-period exceptions, audit evidence packs, and first-close support. |
| 07-agile-artifacts/01-sprint-planning/SKILL.md | name: sprint-planning | description: Generate a sprint planning template with sprint goal, capacity calculation, selected backlog items, task breakdown, and risk tracking per the Scrum Guide and IEEE 29148. |
| 07-agile-artifacts/02-definition-of-done/SKILL.md | name: definition-of-done | description: Generate a Definition of Done checklist covering code quality, testing, documentation, review, and deployment readiness criteria per the Scrum Guide. |
| 07-agile-artifacts/03-definition-of-ready/SKILL.md | name: definition-of-ready | description: Generate a Definition of Ready checklist ensuring backlog items are sufficiently refined before sprint commitment per the Scrum Guide. |
| 07-agile-artifacts/04-retrospective-template/SKILL.md | name: retrospective-template | description: Generate a sprint retrospective template with multiple facilitation formats, action item tracking, and continuous improvement metrics per the Scrum Guide. |
| 07-agile-artifacts/05-saas-growth-experiment-doc/SKILL.md | name: saas-growth-experiment-doc | description: Generate a SaaS Growth Experiment Document: hypothesis, target metric, segment, MDE, sample size, duration, stop rule, instrumentation, decision rule, post-mortem template. |
| 08-end-user-documentation/01-user-manual/SKILL.md | name: user-manual | description: Generate a comprehensive user manual covering all features with step-by-step procedures, navigation guides, and role-based usage instructions per ISO 26514. |
| 08-end-user-documentation/02-installation-guide/SKILL.md | name: installation-guide | description: Generate step-by-step installation instructions covering prerequisites, system requirements, installation procedures, configuration, and verification per ISO 26514. |
| 08-end-user-documentation/03-faq/SKILL.md | name: faq | description: Generate a structured FAQ document organized by category with clear question-answer pairs, cross-references to documentation, and search-friendly formatting per ISO 26514. |
| 08-end-user-documentation/04-release-notes/SKILL.md | name: release-notes | description: Generate a release notes template with version tracking, new features, bug fixes, breaking changes, migration instructions, and known issues per IEEE 830. |
| 08-end-user-documentation/05-saas-customer-success-playbook/SKILL.md | name: saas-customer-success-playbook | description: Generate a SaaS Customer Success Playbook: customer-health-score spec, segmented intervention plays at each lifecycle stage (onboarding, adoption, renewal, at-risk, expansion, churned), QBR template, dunning recovery, escalation matrix. |
| 08-end-user-documentation/06-saas-onboarding-journey-spec/SKILL.md | name: saas-onboarding-journey-spec | description: Generate a SaaS Onboarding Journey Specification: define the aha-moment, activation milestones, channel-orchestrated nudges (in-app / email / push), KPI thresholds, drop-off interventions, segmented onboarding paths per ICP and tier. |
| 08-end-user-documentation/07-saas-lifecycle-email-strategy-doc/SKILL.md | name: saas-lifecycle-email-strategy-doc | description: Generate a SaaS Lifecycle Email Strategy Document: lifecycle map (acquisition → activation → adoption → retention → expansion → at-risk → win-back), campaign catalogue per stage, pre-send QA checklist, measurement plan, RFM segmentation. |
| 08-end-user-documentation/08-saas-sales-enablement-doc-pack/SKILL.md | name: saas-sales-enablement-doc-pack | description: Generate the SaaS Sales Enablement Doc Pack: ICP / target persona, sales-methodology selection (transactional / solution / consultative / provocative), 8-step discovery meeting script (SPI + TALKER), two-part demo script, competitive battlecards, closing playbook, MEDDIC qualification. |
| 08-end-user-documentation/09-ai-agent-user-disclosure-pack/SKILL.md | name: ai-agent-user-disclosure-pack | description: Generate the AI Agent User Disclosure Pack: end-user-facing copy explaining what the agent does and does not, where it has authority, how the user overrides, undo / revert language, the 'agent worked on your behalf' notification design, and the contestation path. Plain-language, layperson-reviewable, regionalised where required. |
| 09-governance-compliance/01-traceability-matrix/SKILL.md | name: Traceability Matrix | description: Generate a bidirectional requirements traceability matrix mapping every requirement to its source, design element, test case, and implementation status per IEEE 1012-2016. |
| 09-governance-compliance/02-audit-report/SKILL.md | name: Audit Report | description: Generate a verification and validation audit report assessing completeness, consistency, correctness, and traceability of all project documentation per IEEE 1012-2016. |
| 09-governance-compliance/03-compliance-documentation/SKILL.md | name: Compliance Documentation | description: Generate compliance documentation mapping project requirements and architecture to applicable regulatory frameworks including GDPR, HIPAA, and SOC2. |
| 09-governance-compliance/04-risk-assessment/SKILL.md | name: Risk Assessment | description: Generate a systematic risk assessment identifying technical, operational, compliance, and project risks with probability/impact scoring and mitigation strategies per ISO 31000 and IEEE 1012. |
| 09-governance-compliance/05-architecture-decision-records/SKILL.md | name: Architecture Decision Records | description: Capture significant architectural decisions as ADRs and maintain the project ADR catalog with status lifecycle, deciders, and supersession chains. |
| 09-governance-compliance/05-formal-review-gates/SKILL.md | name: formal-review-gates | description: Generate PSR, CSR, and FSAR formal customer review gate documents per Royce (1970) Step 5 |
| 09-governance-compliance/06-CCB-charter/SKILL.md | name: CCB Charter | description: Generate a Change Control Board (CCB) Charter governing all changes to baselined project artifacts per PMBOK 6th Ed. Book of Forms and ISO 14764. |
| 09-governance-compliance/06-change-impact-analysis/SKILL.md | name: Change Impact Analysis | description: Produce a Change Impact Analysis (CIA) entry for any proposed change to a baselined FR, NFR, or selected control, including downstream artifacts and a rollback plan. |
| 09-governance-compliance/07-baseline-delta/SKILL.md | name: Baseline Delta | description: Snapshot identifier hashes at phase-gate closure and compute the delta between two baselines as added, removed, and modified identifiers. |
| 09-governance-compliance/08-waiver-management/SKILL.md | name: Waiver Management | description: Capture a gate-specific waiver with approver, justification, and an expiry no more than 90 days from approval. |
| 09-governance-compliance/09-sign-off-ledger/SKILL.md | name: Sign-Off Ledger | description: Record every formal phase-gate sign-off with signer, role, date, and artifact set in a single append-only YAML ledger. |
| 09-governance-compliance/10-evidence-pack-builder/SKILL.md | name: Evidence Pack Builder | description: Assemble an auditor-ready ZIP bundle containing project context, registries, and the full governance tree plus a manifest CSV with SHA-256 hashes. |
| 09-governance-compliance/11-saas-data-isolation-evidence-pack/SKILL.md | name: saas-data-isolation-evidence-pack | description: Generate the auditor-grade Data Isolation Evidence Pack proving that tenant data and tenant access are isolated at each layer — network, compute, storage, IAM, code path, audit — with control mappings to SOC 2, ISO 27001, GDPR, and the tenant-isolation NFR catalogue. |
| 09-governance-compliance/12-saas-trust-center-document-pack/SKILL.md | name: saas-trust-center-document-pack | description: Generate a public Trust Center document pack: security overview, compliance attestations, sub-processor list, DPA template availability, status-page commitment, vulnerability-disclosure policy, and customer-data handling summary. |
| 09-governance-compliance/13-saas-dpa-and-privacy-doc-set/SKILL.md | name: saas-dpa-and-privacy-doc-set | description: Generate the SaaS DPA + Privacy doc set: Data Processing Addendum (controller-processor terms, SCCs, sub-processor list, audit rights), Records of Processing Activity (ROPA Art.30), retention & destruction schedule, breach-notification procedure, DSAR handling procedure. |
| 09-governance-compliance/14-ai-responsible-ai-declaration/SKILL.md | name: ai-responsible-ai-declaration | description: Generate the Responsible AI Declaration: the public-facing statement of what the product's AI does and does not do, the human-in-the-loop posture, contestability, data-use, model providers and sub-processors, and the regulatory tier assessment per feature. |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/SKILL.md | name: ai-act-and-regulatory-compliance-doc | description: Generate the AI Act and Regulatory Compliance Doc: EU AI Act risk-tier classification per feature, US state and sectoral AI rules (FCRA, HIPAA, EEOC, NYC AEDT, Colorado, California ADMT), Canadian / UK guidance, and African AI regulator overlays (Kenya ODPC, Nigeria NDPC, South Africa POPIA). Includes the Annex IV technical documentation index and the disclosure copy library. |
| 09-governance-compliance/16-ai-data-flow-and-dpia/SKILL.md | name: ai-data-flow-and-dpia | description: Generate the AI Data-Flow Diagram and AI-specific DPIA addendum: where customer data flows when AI features run, every model provider as a processor, sub-processor notice, consent capture, training-data exclusion evidence, cross-border transfer mechanism, and the AI-specific risk register that augments the base DPIA. |
| 09-governance-compliance/17-ai-adr-catalogue/SKILL.md | name: ai-adr-catalogue | description: Generate the AI ADR Catalogue: the required architecture decision records for an AI-feature SaaS -- model choice, RAG vs fine-tune, vector store, eval threshold, abstain policy, content filter, fallback, retraining trigger, and the prompt-registry change protocol. |
| 09-governance-compliance/18-ai-agent-responsible-ai-addendum/SKILL.md | name: ai-agent-responsible-ai-addendum | description: Generate the AI Agent Responsible-AI Addendum: action accountability (who is responsible for an agent action), audit-log retention by event class, contestability of agent actions, human-final-decision principle for irreversible actions, agent-specific bias and harm reviews, and the cross-link to the public Responsible AI Declaration. |
| 09-governance-compliance/19-ai-agent-adr-catalogue/SKILL.md | name: ai-agent-adr-catalogue | description: Generate the AI Agent ADR Catalogue: the required architecture decision records for an agent-feature SaaS — autonomy level per feature, irreversibility-gating policy, planner choice, memory store, tool-call audit-log retention, multi-agent topology, supervision policy, kill-switch SLA, and the agent change-control protocol. |
| 09-governance-compliance/20-ai-agent-soc2-control-pack/SKILL.md | name: ai-agent-soc2-control-pack | description: Generate the AI Agent SOC 2 Control Pack: TSC control matrix (Security, Availability, Confidentiality, Processing Integrity, Privacy) extended with agent-specific implementation requirements; per-control objective, agent-specific implementation, evidence required, evidence frequency, test procedure, sampling protocol, and the auditor-walkthrough script. |
| 09-governance-compliance/21-ai-agent-iso27001-control-pack/SKILL.md | name: ai-agent-iso27001-control-pack | description: Generate the AI Agent ISO/IEC 27001:2022 Control Pack: Annex A control matrix (A.5 Organisational, A.6 People, A.7 Physical, A.8 Technological) extended with agent-specific treatments; per-control treatment statement, applicability decision, evidence required, audit procedure, sampling, and the certification-body walkthrough script. Mapped to ISO/IEC 42001 where the AI overlay applies. |
| 09-governance-compliance/22-ai-agent-hipaa-control-pack/SKILL.md | name: ai-agent-hipaa-control-pack | description: Generate the AI Agent HIPAA Security Rule Control Pack: per-standard treatment for §164.308 Administrative, §164.310 Physical, §164.312 Technical safeguards; agent-specific implementation for access controls, audit controls, integrity controls, transmission security, contingency; admin-only constraint for clinical PHI agents; BAA implications; minimum-necessary application to agent service principals. |
| 09-governance-compliance/23-ai-agent-compliance-policy-pack/SKILL.md | name: ai-agent-compliance-policy-pack | description: Generate the AI Agent Compliance Policy Pack: seven bundled, signed, auditor-readable policies — agent action governance, agent audit-log retention, agent approval and supervision, agent kill-switch and drill, agent memory erasure, agent red-team and safety, agent compliance evidence and attestation. Each policy carries scope, definitions, statements, roles, exceptions, review cadence, and the signature block. |
| 09-governance-compliance/24-ai-agent-attestation-preparation-spec/SKILL.md | name: ai-agent-attestation-preparation-spec | description: Generate the AI Agent Attestation Preparation Spec: end-to-end preparation for SOC 2 Type II window, ISO/IEC 27001 surveillance audit, and HIPAA periodic review. Defines the 12-month timeline, the evidence pre-gathering schedule, the auditor-readiness checklist, the gap-remediation cadence, and the on-the-day auditor playbook for agent-specific control areas. |
| 09-governance-compliance/25-ai-agent-evidence-pack-spec/SKILL.md | name: ai-agent-evidence-pack-spec | description: Generate the AI Agent Evidence Pack Spec: what evidence the auditor expects per control class; evidence-pack file layout; sampling protocol; chain-of-custody; retention; redaction policy; presentation format; auditor portal access governance. Defines the contract the software-dev pass's collectors must satisfy. |
| 09-governance-compliance/26-ai-agent-baa-and-data-processing-language/SKILL.md | name: ai-agent-baa-and-data-processing-language | description: Generate the AI Agent BAA Addendum (HIPAA Business Associate Agreement) and DPA Addendum (GDPR + African DPA Data Processing Agreement) language for agentic engagements. Drop-in clauses to bolt onto the parent BAA / DPA; cover service-principal access, irreversibility, audit-log retention, kill-switch SLA, memory erasure, sub-processor change, training-data exclusion, breach notification, and cross-jurisdiction transfers. |
| 09-governance-compliance/27-ai-agent-regulator-overlap-mapping/SKILL.md | name: ai-agent-regulator-overlap-mapping | description: Generate the AI Agent Regulator Overlap Mapping: the multi-regime crosswalk that shows how a single piece of agent-compliance evidence satisfies multiple frameworks at once — SOC 2 × ISO 27001 × HIPAA × EU AI Act × NIST AI RMF × Kenya DPA × Nigeria NDP Act × South Africa POPIA × Uganda DPPA × Rwanda DP Law. Enables 'one piece of evidence, multiple regimes' reuse and surfaces where regimes diverge so distinct evidence is needed. |
| 09-governance-compliance/28-anti-ai-slop/SKILL.md | name: 28-anti-ai-slop | description: MANDATORY pre-ship guardrail. Run on EVERY generated SRS, technical spec, user story, acceptance criterion, design document, test document, ADR, or code artefact before it is delivered, so the output cannot be recognised as "AI slop". Carries the verified slop definition, the seven universal markers each paired with an avoidance rule, the banned-vocabulary list merged with this engine's prohibited-adjective rule, the SRS/spec avoidance block, and a ship-gate checklist. Load first; it overrides stylistic preferences but defers to IEEE/ISO grounding. |
| 09-governance-compliance/29-ai-slop-audit/SKILL.md | name: 29-ai-slop-audit | description: Analyse, evaluate, and audit any artefact for AI slop and score it. AUTO-RUNS whenever the user asks to analyse, review, evaluate, audit, critique, or "de-slop" any SRS, technical spec, requirement, user story, acceptance criterion, design doc, test doc, ADR, document, system, codebase, app, website, business plan, or proposal — or asks "does this look AI-generated?". Produces a graded slop report: per-marker findings with severity, evidence, and a concrete fix. Pairs with 28-anti-ai-slop (which prevents slop during production). |

## Governance/Doctrine/Standard Files Read

| Path | Lines | SHA-256 prefix | First heading |
| --- | --- | --- | --- |
| AGENTS.md | 124 | fcc1c789eee0 | Repository Agents Guide |
| ARCHITECTURE.md | 14 | cfbc384d5732 | Architecture Overview |
| CLAUDE.md | 301 | 3e2549fa595c | AI Assistant Protocol: SRS-Skills |
| README.md | 982 | 8c982ff45223 | SDLC-Docs-Engine: Standards-Driven Documentation Across the Software Lifecycle |
| SETUP_GUIDE.md | 255 | 05e610f19f05 | SDLC-Docs-Engine: New Project Setup Guide |
| 01-strategic-vision/README.md | 34 | 4e708c1984e2 | Phase 01: Strategic Vision |
| 01-strategic-vision/01-prd-generation/README.md | 22 | 6e4bc6417757 | 01-PRD-Generation Skill |
| 01-strategic-vision/02-business-case/README.md | 17 | e2460e71f2ee | 02-Business-Case Skill |
| 01-strategic-vision/03-vision-statement/README.md | 17 | 2a258ea01b4f | 03-Vision-Statement Skill |
| 01-strategic-vision/04-lean-canvas/README.md | 49 | 305c2d46f870 | 04-Lean-Canvas Skill |
| 01-strategic-vision/04-lean-canvas/references/impact-mapping-guide.md | 190 | 586b08f710df | Impact Mapping Construction Guide |
| 01-strategic-vision/04-lean-canvas/references/lean-canvas-guide.md | 201 | ac4a585bb499 | Lean Canvas Block-by-Block Filling Guide |
| 01-strategic-vision/06-ai-economic-value-brief/README.md | 16 | 2496e818ec0c | Objective |
| 01-strategic-vision/10-saas-mvp-scoping-doc/README.md | 17 | 253f3a944d13 | 10-SaaS-MVP-Scoping-Doc Skill |
| 01-strategic-vision/11-saas-moat-and-defensibility-plan/README.md | 17 | 4f382c7b5a35 | 11-SaaS-Moat-and-Defensibility-Plan Skill |
| 01-strategic-vision/12-saas-pricing-and-packaging-spec/README.md | 18 | 2ff4c475ae86 | 12-SaaS-Pricing-and-Packaging-Spec Skill |
| 01-strategic-vision/13-ai-feature-strategy-doc/README.md | 15 | c56667fa17e9 | Objective |
| 01-strategic-vision/14-ai-agent-strategy-doc/README.md | 16 | ef9ca5dd030a | Objective |
| 02-requirements-engineering/README.md | 242 | 8f35b0e96c6c | Requirements Engineering |
| 02-requirements-engineering/13-saas-billing-and-metering-spec/README.md | 18 | 132a0374fc7c | 13-SaaS-Billing-and-Metering-Spec Skill |
| 02-requirements-engineering/14-ai-feature-prd-spec/README.md | 17 | 32d64be06547 | Objective |
| 02-requirements-engineering/15-ai-data-and-knowledge-base-spec/README.md | 17 | a6df99974716 | Objective |
| 02-requirements-engineering/16-ai-agent-feature-prd-spec/README.md | 16 | 1072602a4c11 | Objective |
| 02-requirements-engineering/17-ai-agent-action-catalogue-spec/README.md | 16 | 1b7bfafa873d | Objective |
| 02-requirements-engineering/agile/README.md | 128 | 7f0bcff792bf | Agile Requirements Pipeline |
| 02-requirements-engineering/agile/02-acceptance-criteria/README.md | 17 | ba0c05299cbc | 02-Acceptance-Criteria Skill |
| 02-requirements-engineering/agile/03-story-mapping/README.md | 17 | 5b02d4e0a8ba | 03-Story-Mapping Skill |
| 02-requirements-engineering/agile/04-backlog-prioritization/README.md | 17 | 378177493a5a | 04-Backlog-Prioritization Skill |
| 02-requirements-engineering/fundamentals/README.md | 214 | 481515fe4f01 | Requirements Engineering Fundamentals |
| 02-requirements-engineering/fundamentals/after/08-requirements-management/references/baselining-guide.md | 226 | 2347caac8958 | Requirements Baselining Guide |
| 02-requirements-engineering/fundamentals/after/10-requirements-metrics/references/quality-gate-thresholds.md | 186 | 2ff4b5babd09 | Quality Gate Thresholds Configuration |
| 02-requirements-engineering/fundamentals/before/02-elicitation-toolkit/references/interview-guide.md | 127 | 65185da2e3c8 | Structured Interview Protocol |
| 02-requirements-engineering/fundamentals/before/04-business-analysis-planning/references/governance-and-engagement.md | 26 | 7e82059762a9 | Governance And Engagement |
| 02-requirements-engineering/fundamentals/during/05-conceptual-data-modeling/references/data-quality-rules.md | 183 | ebec5091cd58 | Data Quality Rules Reference Guide |
| 02-requirements-engineering/fundamentals/during/05-conceptual-data-modeling/references/er-modeling-guide.md | 206 | a2d81c6ba743 | Entity-Relationship Modeling Guide |
| 02-requirements-engineering/hybrid/README.md | 26 | a1a4e80724fa | Hybrid Skills |
| 02-requirements-engineering/waterfall/README.md | 212 | ec093409afcd | Waterfall SRS Generation Pipeline |
| 02-requirements-engineering/waterfall/01-initialize-srs/examples/representative/README.md | 15 | b21fadc73988 | Worked example -- initialize-srs |
| 02-requirements-engineering/waterfall/01-initialize-srs/templates/quality_standards.md | 34 | ae15b67bb48e | Quality Standards Template |
| 02-requirements-engineering/waterfall/02-context-engineering/README.md | 17 | 5ee51ef7085b | 02-Context-Engineering Skill |
| 02-requirements-engineering/waterfall/03-descriptive-modeling/README.md | 17 | f4b200a9c1e5 | 03-Descriptive-Modeling Skill |
| 02-requirements-engineering/waterfall/04-interface-specification/README.md | 17 | 60a37f6b8444 | 04-Interface-Specification Skill |
| 02-requirements-engineering/waterfall/05-feature-decomposition/README.md | 17 | c95f4bfb451e | 05-Feature-Decomposition Skill |
| 02-requirements-engineering/waterfall/06-logic-modeling/README.md | 23 | 61c1d869c71e | 06-Logic-Modeling Skill |
| 02-requirements-engineering/waterfall/07-attribute-mapping/README.md | 23 | efec0fe6e16b | 07-Attribute-Mapping Skill |
| 02-requirements-engineering/waterfall/08-semantic-auditing/README.md | 23 | b9397d299832 | 08-Semantic-Auditing Skill |
| 02-requirements-engineering/waterfall/08-semantic-auditing/SKILL.md | 54 | bf9b0241bbec | Semantic Auditing Skill Guidance |
| 02-requirements-engineering/waterfall/09-use-case-modeling/README.md | 40 | fd66a55ef185 | 09-Use-Case-Modeling Skill |
| 02-requirements-engineering/waterfall/09-use-case-modeling/references/activity-diagram-guide.md | 199 | ecc92960904d | Activity Diagram Construction Guide |
| 03-design-documentation/README.md | 48 | 93b37ca9ae08 | Phase 03: Design Documentation |
| 03-design-documentation/01-high-level-design/README.md | 22 | 7053f1ba4fe5 | 01-High-Level-Design Skill |
| 03-design-documentation/01-high-level-design/references/practical-architecture-knowledge.md | 238 | 7d7ba2d27995 | Practical Architecture Knowledge |
| 03-design-documentation/02-low-level-design/README.md | 23 | 80fad5a59183 | 02-Low-Level-Design Skill |
| 03-design-documentation/03-api-specification/README.md | 23 | 3e535d9565dd | 03-API-Specification Skill |
| 03-design-documentation/03-api-specification/references/practical-api-architecture.md | 174 | e03010c1ac84 | Practical API Architecture |
| 03-design-documentation/04-database-design/README.md | 26 | ceaed6e76afd | 04 - Database Design |
| 03-design-documentation/05-ux-specification/README.md | 56 | 103e79c3f89f | 05 - UX Specification |
| 03-design-documentation/05-ux-specification/references/design-system-guide.md | 219 | 31a466f8e27e | Design System Guide Reference |
| 03-design-documentation/05-ux-specification/references/information-architecture.md | 112 | 2f7d0935ff3f | Information Architecture Reference |
| 03-design-documentation/05-ux-specification/references/wireframing-standards.md | 139 | 960934bab557 | Wireframing Standards Reference |
| 03-design-documentation/06-infrastructure-design/README.md | 50 | 87a53f6e9e76 | 06-Infrastructure-Design Skill |
| 03-design-documentation/07-iot-system-design/references/iot-architecture-checklist.md | 43 | 28c0eaf8a82d | IoT Architecture Checklist |
| 03-design-documentation/08-engineering-strategy-brief/references/saas-architecture-assumptions-and-scaling-checklist.md | 57 | eb46f6f9960d | SaaS Architecture Assumptions And Scaling Checklist |
| 03-design-documentation/09-ux-content-and-form-specification/references/ux-content-and-form-quality-gates.md | 80 | 0a5fe677bdaa | UX Content And Form Quality Gates |
| 03-design-documentation/10-saas-multi-tenancy-architecture-spec/README.md | 24 | a4ca96fa9502 | 10-SaaS-Multi-Tenancy-Architecture-Spec Skill |
| 03-design-documentation/10-saas-multi-tenancy-architecture-spec/SKILL.md | 219 | 31b998208c1e | SaaS Multi-Tenancy Architecture Specification Skill |
| 03-design-documentation/10-saas-multi-tenancy-architecture-spec/references/saas-control-plane-services.md | 87 | 8c320b2a7826 | Canonical Control-Plane Services for Multi-Tenant SaaS |
| 03-design-documentation/10-saas-multi-tenancy-architecture-spec/references/saas-tenancy-decision-template.md | 76 | 4dc288113841 | SaaS Tenancy Decision (ADR Template) |
| 03-design-documentation/11-ai-architecture-spec/README.md | 17 | f0c8054c3722 | Objective |
| 03-design-documentation/11-ai-architecture-spec/SKILL.md | 104 | fb56e6d0d0dc | AI Architecture Spec Skill |
| 03-design-documentation/11-ai-architecture-spec/references/ai-agent-runtime-crosslink.md | 31 | d06de2ce6688 | Agent Runtime Cross-Link |
| 03-design-documentation/11-ai-architecture-spec/references/ai-architecture-patterns.md | 65 | e260d2d20610 | AI Architecture Patterns Reference |
| 03-design-documentation/11-ai-architecture-spec/references/ai-architecture-spec-template.md | 120 | e17c196d16b6 | AI Architecture Spec Template |
| 03-design-documentation/12-ai-model-card/README.md | 17 | ec3f7bb3be14 | Objective |
| 03-design-documentation/13-ai-prompt-and-system-message-spec/README.md | 16 | 100f602481f5 | Objective |
| 03-design-documentation/14-ai-agent-architecture-spec/README.md | 17 | 3d642598e817 | Objective |
| 03-design-documentation/14-ai-agent-architecture-spec/SKILL.md | 110 | e55a50e82006 | AI Agent Architecture Spec Skill |
| 03-design-documentation/14-ai-agent-architecture-spec/references/ai-agent-architecture-spec-template.md | 169 | e0f406d994d7 | AI Agent Architecture Spec Template |
| 03-design-documentation/15-ai-agent-multi-agent-coordination-spec/README.md | 16 | 552ddbf13067 | Objective |
| 04-development-artifacts/README.md | 32 | 98e970735284 | Phase 04: Development Artifacts |
| 04-development-artifacts/01-technical-specification/README.md | 22 | c9c7ec730019 | 01-Technical-Specification Skill |
| 04-development-artifacts/02-coding-guidelines/README.md | 21 | 9bdb6a1d06f8 | 02-Coding-Guidelines Skill |
| 04-development-artifacts/02-coding-guidelines/SKILL.md | 144 | b084f520b043 | Coding Guidelines Skill |
| 04-development-artifacts/02-coding-guidelines/references/ai-coding-guidelines-addendum.md | 75 | da9927dfb014 | AI Coding Guidelines Addendum |
| 04-development-artifacts/02-coding-guidelines/references/saas-multi-tenant-coding-guidelines-addendum.md | 64 | 26444fbb895b | SaaS Multi-Tenant Coding Guidelines Addendum |
| 04-development-artifacts/03-dev-environment-setup/README.md | 21 | 011acd8cd9d1 | 03-Dev-Environment-Setup Skill |
| 04-development-artifacts/04-contribution-guide/README.md | 21 | 08cd44fd7300 | 04-Contribution-Guide Skill |
| 04-development-artifacts/04-contribution-guide/SKILL.md | 141 | a87da22940ab | Contribution Guide Skill |
| 04-development-artifacts/05-ai-agent-coding-guidelines-addendum/README.md | 16 | dee6fb3eb345 | Objective |
| 04-development-artifacts/05-ai-agent-coding-guidelines-addendum/SKILL.md | 77 | 7e7155bf2449 | AI Agent Coding Guidelines Addendum Skill |
| 04-development-artifacts/05-ai-agent-coding-guidelines-addendum/references/ai-agent-coding-guidelines-addendum-template.md | 134 | d15cfa995b88 | Coding Guidelines — Agent Addendum Template |
| 05-testing-documentation/README.md | 43 | b655c20a0db2 | Phase 05: Testing Documentation |
| 05-testing-documentation/01-test-strategy/README.md | 21 | 9a3662e4c830 | 01-Test-Strategy Skill |
| 05-testing-documentation/02-test-plan/README.md | 21 | 12a2ec42c33e | 02-Test-Plan Skill |
| 05-testing-documentation/02-test-plan/examples/representative/README.md | 14 | 2820b8e96ce1 | Worked example -- test-plan |
| 05-testing-documentation/03-test-report/README.md | 21 | 59516dd7819f | 03-Test-Report Skill |
| 05-testing-documentation/04-ai-eval-harness-spec/README.md | 17 | 10e56319947b | Objective |
| 05-testing-documentation/05-ai-red-team-test-plan/README.md | 16 | c6e9160d1a3d | Objective |
| 05-testing-documentation/06-ai-agent-eval-spec/README.md | 17 | 5f14ccd47c29 | Objective |
| 05-testing-documentation/07-ai-agent-red-team-test-plan/README.md | 17 | 66b2b1b722d2 | Objective |
| 06-deployment-operations/README.md | 42 | 71fbf11b6e19 | Phase 06: Deployment & Operations |
| 06-deployment-operations/01-deployment-guide/README.md | 21 | 8e35a0a285e8 | 01-Deployment-Guide Skill |
| 06-deployment-operations/01-deployment-guide/SKILL.md | 157 | 9fac12605a4d | Deployment Guide Skill |
| 06-deployment-operations/02-runbook/README.md | 21 | 3e75615ab8b4 | 02-Runbook Skill |
| 06-deployment-operations/03-monitoring-setup/README.md | 21 | 6310d9625816 | 03-Monitoring-Setup Skill |
| 06-deployment-operations/04-infrastructure-docs/README.md | 21 | 35c6080ef340 | 04-Infrastructure-Docs Skill |
| 06-deployment-operations/07-saas-tenant-lifecycle-runbook/README.md | 24 | 8fbdde5d5cd2 | 07-SaaS-Tenant-Lifecycle-Runbook Skill |
| 06-deployment-operations/08-saas-slo-and-error-budget-doc/README.md | 17 | dca5895eca4d | 08-SaaS-SLO-and-Error-Budget-Doc Skill |
| 06-deployment-operations/09-saas-incident-response-and-postmortem/README.md | 17 | 6e9c186723d2 | 09-SaaS-Incident-Response-and-Postmortem Skill |
| 06-deployment-operations/10-ai-hallucination-slo-doc/README.md | 15 | 3b8ff394ed0b | Objective |
| 06-deployment-operations/11-ai-feature-rollout-runbook/README.md | 15 | de6694444699 | Objective |
| 06-deployment-operations/12-ai-cost-runbook/README.md | 15 | a44ae01a47ed | Objective |
| 06-deployment-operations/13-ai-agent-slo-doc/README.md | 17 | 20e9b20ce18d | Objective |
| 06-deployment-operations/13-ai-incident-severity-matrix/README.md | 17 | 0b75828dc2ee | Objective |
| 06-deployment-operations/14-ai-agent-runbook/README.md | 17 | f10839958bee | Objective |
| 06-deployment-operations/14-ai-incident-response-runbook/README.md | 18 | 9e75ffd1fc66 | Objective |
| 06-deployment-operations/15-ai-agent-rollout-runbook/README.md | 17 | 2d0674a22f3a | Objective |
| 06-deployment-operations/15-ai-rca-taxonomy-doc/README.md | 17 | 86c2fa1bb80b | Objective |
| 06-deployment-operations/16-ai-incident-postmortem-template/README.md | 18 | 4b4e47646dc4 | Objective |
| 06-deployment-operations/17-ai-incident-evidence-pack-spec/README.md | 17 | 0ee921012a67 | Objective |
| 06-deployment-operations/20-ai-agent-compliance-runbook/README.md | 18 | c9dff976d989 | AI Agent Compliance Runbook |
| 07-agile-artifacts/README.md | 28 | 2185299f8035 | Phase 07: Agile Artifacts |
| 07-agile-artifacts/01-sprint-planning/README.md | 23 | 8c9444c310fd | 01-Sprint-Planning Skill |
| 07-agile-artifacts/02-definition-of-done/README.md | 22 | 45dd42b95148 | 02-Definition-of-Done Skill |
| 07-agile-artifacts/03-definition-of-ready/README.md | 22 | 141e299e6ff4 | 03-Definition-of-Ready Skill |
| 07-agile-artifacts/04-retrospective-template/README.md | 22 | a477d736a7f9 | 04-Retrospective-Template Skill |
| 07-agile-artifacts/05-saas-growth-experiment-doc/README.md | 17 | 90c2138007c4 | 05-SaaS-Growth-Experiment-Doc Skill |
| 08-end-user-documentation/README.md | 28 | 44d1a7ce2349 | Phase 08: End-User Documentation |
| 08-end-user-documentation/01-user-manual/README.md | 21 | 4e4c6aa07444 | 01-User-Manual Skill |
| 08-end-user-documentation/02-installation-guide/README.md | 21 | 5706fed2ca0b | 02-Installation-Guide Skill |
| 08-end-user-documentation/02-installation-guide/SKILL.md | 166 | ee07eccea88e | Installation Guide Skill |
| 08-end-user-documentation/03-faq/README.md | 21 | 22b6cdef44fa | 03-FAQ Skill |
| 08-end-user-documentation/04-release-notes/README.md | 21 | c58390dc8c4c | 04-Release-Notes Skill |
| 08-end-user-documentation/05-saas-customer-success-playbook/README.md | 17 | 483b42f18abd | 05-SaaS-Customer-Success-Playbook Skill |
| 08-end-user-documentation/06-saas-onboarding-journey-spec/README.md | 18 | 72093bb4935e | 06-SaaS-Onboarding-Journey-Spec Skill |
| 08-end-user-documentation/07-saas-lifecycle-email-strategy-doc/README.md | 17 | 6d33a22800d0 | 07-SaaS-Lifecycle-Email-Strategy-Doc Skill |
| 08-end-user-documentation/08-saas-sales-enablement-doc-pack/README.md | 17 | e3dcc1d3c07f | 08-SaaS-Sales-Enablement-Doc-Pack Skill |
| 08-end-user-documentation/08-saas-sales-enablement-doc-pack/references/saas-value-quantification-worksheet.md | 53 | 6a79624fe46d | SaaS Value Quantification Worksheet |
| 08-end-user-documentation/09-ai-agent-user-disclosure-pack/README.md | 17 | 2afd9a80f2db | Objective |
| 09-governance-compliance/README.md | 65 | 4dd199107494 | Phase 09: Governance & Compliance |
| 09-governance-compliance/01-traceability-matrix/README.md | 19 | b89690e216a5 | Traceability Matrix Skill |
| 09-governance-compliance/01-traceability-matrix/SKILL.md | 172 | eaa7926743c6 | Traceability Matrix Skill |
| 09-governance-compliance/02-audit-report/README.md | 19 | 7ef46dda6eeb | Audit Report Skill |
| 09-governance-compliance/02-audit-report/SKILL.md | 147 | bc5d5c9df5f6 | Audit Report Skill |
| 09-governance-compliance/03-compliance-documentation/README.md | 19 | 76f2460d8fe0 | Compliance Documentation Skill |
| 09-governance-compliance/03-compliance-documentation/SKILL.md | 176 | 214ab9c483d3 | Compliance Documentation Skill |
| 09-governance-compliance/04-risk-assessment/README.md | 19 | 995b1c4bdfa2 | Risk Assessment Skill |
| 09-governance-compliance/04-risk-assessment/SKILL.md | 157 | 4ddf83ba2f2d | Risk Assessment Skill |
| 09-governance-compliance/05-architecture-decision-records/SKILL.md | 75 | dd7f010a843c | Architecture Decision Records Skill |
| 09-governance-compliance/05-architecture-decision-records/examples/representative/README.md | 14 | 01069cc8bc95 | Worked example -- architecture-decision-records |
| 09-governance-compliance/05-architecture-decision-records/examples/representative/expected-output/ADR-001-use-postgres.md | 28 | 7a030f5b39a8 | ADR-001 Use PostgreSQL |
| 09-governance-compliance/05-architecture-decision-records/examples/representative/inputs/context-note.md | 9 | a684f25cb5e6 | Context note for ADR-001 |
| 09-governance-compliance/05-architecture-decision-records/references/saas-adr-catalogue.md | 99 | 5116ed473764 | SaaS ADR Catalogue |
| 09-governance-compliance/05-formal-review-gates/SKILL.md | 115 | 07f6ff198c8e | Skill: Formal Review Gates (PSR / CSR / FSAR) |
| 09-governance-compliance/05-formal-review-gates/references/uganda-public-sector-and-ngo-delivery-constraints.md | 82 | 5f7e282b0195 | Uganda Public-Sector and NGO Delivery Constraints |
| 09-governance-compliance/06-CCB-charter/SKILL.md | 168 | 3cf0ecf7cd4e | Skill: CCB Charter |
| 09-governance-compliance/06-change-impact-analysis/SKILL.md | 52 | 4286caf8a735 | Change Impact Analysis Skill |
| 09-governance-compliance/07-baseline-delta/SKILL.md | 47 | afc5734742b1 | Baseline Delta Skill |
| 09-governance-compliance/08-waiver-management/SKILL.md | 55 | 00d30563f30a | Waiver Management Skill |
| 09-governance-compliance/09-sign-off-ledger/SKILL.md | 52 | 6164bbf36fd1 | Sign-Off Ledger Skill |
| 09-governance-compliance/10-evidence-pack-builder/SKILL.md | 35 | bc5cb593a4d3 | Evidence Pack Builder Skill |
| 09-governance-compliance/11-saas-data-isolation-evidence-pack/README.md | 19 | 5cbc7a584ef2 | 11-SaaS-Data-Isolation-Evidence-Pack Skill |
| 09-governance-compliance/11-saas-data-isolation-evidence-pack/SKILL.md | 85 | f7b8dcb5b81a | SaaS Data Isolation Evidence Pack Skill |
| 09-governance-compliance/11-saas-data-isolation-evidence-pack/references/ai-isolation-evidence.md | 37 | 1ff653f97370 | AI-Specific Isolation Evidence (addendum to Data Isolation Evidence Pack) |
| 09-governance-compliance/11-saas-data-isolation-evidence-pack/references/saas-data-isolation-evidence-pack-template.md | 87 | 77961503a7fe | SaaS Data Isolation Evidence Pack — Template |
| 09-governance-compliance/12-saas-trust-center-document-pack/README.md | 18 | a8a618525abc | 12-SaaS-Trust-Center-Document-Pack Skill |
| 09-governance-compliance/12-saas-trust-center-document-pack/SKILL.md | 74 | 8a73c2b9f942 | SaaS Trust Center Document Pack Skill |
| 09-governance-compliance/12-saas-trust-center-document-pack/references/ai-trust-center-additions.md | 59 | ea2996a9df48 | AI Additions to the Trust Center Document Pack |
| 09-governance-compliance/12-saas-trust-center-document-pack/references/saas-trust-center-document-pack-template.md | 75 | 724b6e76171c | SaaS Trust Center — Public Document Pack Template |
| 09-governance-compliance/13-saas-dpa-and-privacy-doc-set/README.md | 19 | f92e182f3f1c | 13-SaaS-DPA-and-Privacy-Doc-Set Skill |
| 09-governance-compliance/13-saas-dpa-and-privacy-doc-set/SKILL.md | 83 | 84f0df8341b8 | SaaS DPA & Privacy Doc Set Skill |
| 09-governance-compliance/13-saas-dpa-and-privacy-doc-set/references/ai-dpa-additions.md | 86 | 973efabf0ca0 | AI-Specific DPA and Privacy Doc Additions |
| 09-governance-compliance/13-saas-dpa-and-privacy-doc-set/references/saas-dpa-and-privacy-doc-templates.md | 94 | 3cecd684653c | SaaS DPA & Privacy — Document Templates |
| 09-governance-compliance/14-ai-responsible-ai-declaration/README.md | 16 | d8ee1a5cc9c7 | Objective |
| 09-governance-compliance/14-ai-responsible-ai-declaration/SKILL.md | 83 | 277017803c18 | Responsible AI Declaration Skill |
| 09-governance-compliance/14-ai-responsible-ai-declaration/references/ai-agent-paragraphs-crosslink.md | 21 | 1c71127646ea | Agent Paragraphs Cross-Link |
| 09-governance-compliance/14-ai-responsible-ai-declaration/references/ai-responsible-ai-declaration-template.md | 72 | aa8014a5432d | Responsible AI Declaration |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/README.md | 16 | e51528b2988d | Objective |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/SKILL.md | 90 | 4207c4e42bdc | AI Act and Regulatory Compliance Doc Skill |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/references/ai-act-regulatory-compliance-doc-template.md | 83 | a76ba8b9ec92 | AI Act and Regulatory Compliance Doc Template |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/references/ai-agent-tier-crosslink.md | 34 | bc7fcebaceba | Agent Tier Under EU AI Act Cross-Link |
| 09-governance-compliance/15-ai-act-and-regulatory-compliance-doc/references/ai-disclosure-copy-library.md | 95 | 029c600b2dc5 | AI Disclosure Copy Library |
| 09-governance-compliance/16-ai-data-flow-and-dpia/README.md | 16 | 6eb0e35e71b3 | Objective |
| 09-governance-compliance/16-ai-data-flow-and-dpia/SKILL.md | 97 | f443e6ada460 | AI Data-Flow and DPIA Skill |
| 09-governance-compliance/16-ai-data-flow-and-dpia/references/ai-agent-tool-call-data-flow-crosslink.md | 37 | 99da69839568 | Agent Tool-Call Data Flow Cross-Link |
| 09-governance-compliance/16-ai-data-flow-and-dpia/references/ai-data-flow-diagram-conventions.md | 88 | edb247afb07b | AI Data-Flow Diagram Conventions |
| 09-governance-compliance/16-ai-data-flow-and-dpia/references/ai-dpia-addendum-template.md | 98 | aea25882bb0c | AI DPIA Addendum Template |
| 09-governance-compliance/17-ai-adr-catalogue/README.md | 16 | 170a1296730b | Objective |
| 09-governance-compliance/17-ai-adr-catalogue/SKILL.md | 52 | 19071998c89c | AI ADR Catalogue Skill |
| 09-governance-compliance/17-ai-adr-catalogue/references/ai-adr-templates.md | 124 | 1d77c41a66b3 | AI ADR Templates (seed ADRs) |
| 09-governance-compliance/17-ai-adr-catalogue/references/ai-agent-adr-slots-crosslink.md | 31 | 60e0364e6bf3 | Agent ADR Slots Cross-Link |
| 09-governance-compliance/18-ai-agent-responsible-ai-addendum/README.md | 16 | c690531c2270 | Objective |
| 09-governance-compliance/18-ai-agent-responsible-ai-addendum/SKILL.md | 100 | 04e38810e50b | AI Agent Responsible-AI Addendum Skill |
| 09-governance-compliance/18-ai-agent-responsible-ai-addendum/references/ai-agent-responsible-ai-addendum-template.md | 73 | b12a2ebd1240 | AI Agent Responsible-AI Addendum Template |
| 09-governance-compliance/18-ai-regulator-incident-notification-doc/references/ai-incident-regulator-notification-template.md | 146 | c34f6fae0356 | AI Incident Regulator Notification Template |
| 09-governance-compliance/19-ai-agent-adr-catalogue/README.md | 17 | 281108b515a8 | Objective |
| 09-governance-compliance/19-ai-agent-adr-catalogue/SKILL.md | 64 | 5ca788e6ce40 | AI Agent ADR Catalogue Skill |
| 09-governance-compliance/19-ai-agent-adr-catalogue/references/ai-agent-adr-templates.md | 132 | 6ef7776a19be | AI Agent ADR Templates (seed ADRs) |
| 09-governance-compliance/20-ai-agent-soc2-control-pack/README.md | 22 | 0067d932c56a | AI Agent SOC 2 Control Pack |
| 09-governance-compliance/20-ai-agent-soc2-control-pack/SKILL.md | 116 | 2ad7763809fe | AI Agent SOC 2 Control Pack Skill |
| 09-governance-compliance/20-ai-agent-soc2-control-pack/references/ai-agent-soc2-control-matrix-template.md | 262 | fce6220b9123 | AI Agent SOC 2 Control Matrix Template |
| 09-governance-compliance/21-ai-agent-iso27001-control-pack/README.md | 18 | 8e8fe3adb552 | AI Agent ISO/IEC 27001:2022 Control Pack |
| 09-governance-compliance/21-ai-agent-iso27001-control-pack/SKILL.md | 125 | 76d1c8969ff1 | AI Agent ISO/IEC 27001 Control Pack Skill |
| 09-governance-compliance/21-ai-agent-iso27001-control-pack/references/ai-agent-iso27001-control-matrix-template.md | 242 | 7a926a5dd9e8 | AI Agent ISO/IEC 27001:2022 Control Matrix Template |
| 09-governance-compliance/22-ai-agent-hipaa-control-pack/README.md | 22 | 0276c8ea365c | AI Agent HIPAA Security Rule Control Pack |
| 09-governance-compliance/22-ai-agent-hipaa-control-pack/SKILL.md | 116 | 2fe9a2cc0d84 | AI Agent HIPAA Security Rule Control Pack Skill |
| 09-governance-compliance/22-ai-agent-hipaa-control-pack/references/ai-agent-hipaa-control-matrix-template.md | 154 | f7ed6a9f6b3d | AI Agent HIPAA Security Rule Control Matrix Template |
| 09-governance-compliance/23-ai-agent-compliance-policy-pack/README.md | 22 | feb79fdf6f8d | AI Agent Compliance Policy Pack |
| 09-governance-compliance/23-ai-agent-compliance-policy-pack/SKILL.md | 133 | f7534feebeb7 | AI Agent Compliance Policy Pack Skill |
| 09-governance-compliance/23-ai-agent-compliance-policy-pack/references/ai-agent-compliance-policy-pack-template.md | 203 | e039570a0c95 | AI Agent Compliance Policy Pack — Template |
| 09-governance-compliance/24-ai-agent-attestation-preparation-spec/README.md | 19 | a42ee01ffd76 | AI Agent Attestation Preparation Spec |
| 09-governance-compliance/24-ai-agent-attestation-preparation-spec/SKILL.md | 108 | 2d94c73be226 | AI Agent Attestation Preparation Spec Skill |
| 09-governance-compliance/24-ai-agent-attestation-preparation-spec/references/ai-agent-auditor-on-the-day-playbook.md | 96 | 5463e0f04b2b | AI Agent Auditor On-The-Day Playbook |
| 09-governance-compliance/24-ai-agent-attestation-preparation-spec/references/ai-agent-compliance-readiness-checklist.md | 118 | b013855d189d | AI Agent Compliance Readiness Checklist (50–100 points) |
| 09-governance-compliance/25-ai-agent-evidence-pack-spec/README.md | 25 | 58d5beef9329 | AI Agent Evidence Pack Spec |
| 09-governance-compliance/25-ai-agent-evidence-pack-spec/SKILL.md | 166 | 5ea3794745a9 | AI Agent Evidence Pack Spec Skill |
| 09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-attestation-evidence-pack-template.md | 189 | e31a06b642cc | AI Agent Attestation Evidence Pack Template |
| 09-governance-compliance/25-ai-agent-evidence-pack-spec/references/ai-agent-evidence-frequency-table.md | 61 | 0ec6fbac5d7e | AI Agent Evidence Frequency Table |
| 09-governance-compliance/26-ai-agent-baa-and-data-processing-language/README.md | 17 | d1899311aa8a | AI Agent BAA and Data-Processing Language |
| 09-governance-compliance/26-ai-agent-baa-and-data-processing-language/SKILL.md | 124 | f7d6870ff549 | AI Agent BAA and Data-Processing Language Skill |
| 09-governance-compliance/26-ai-agent-baa-and-data-processing-language/references/ai-agent-baa-template.md | 126 | 2c5075a32d50 | AI Agent BAA Addendum — Template |
| 09-governance-compliance/26-ai-agent-baa-and-data-processing-language/references/ai-agent-dpa-template.md | 140 | 11d91a4abe35 | AI Agent DPA Addendum — Template |
| 09-governance-compliance/27-ai-agent-regulator-overlap-mapping/README.md | 18 | c684ec1adecf | AI Agent Regulator Overlap Mapping |
| 09-governance-compliance/27-ai-agent-regulator-overlap-mapping/SKILL.md | 114 | 7db6b0bdab13 | AI Agent Regulator Overlap Mapping Skill |
| 09-governance-compliance/27-ai-agent-regulator-overlap-mapping/references/ai-agent-regulator-overlap-matrix.md | 72 | 72444e61cfb6 | AI Agent Regulator Overlap Matrix |
| 09-governance-compliance/28-anti-ai-slop/SKILL.md | 129 | b3c4e319fd82 | Anti AI Slop |
| 09-governance-compliance/29-ai-slop-audit/SKILL.md | 151 | 8d84365f0d1c | AI Slop Audit |
| book-extractions/multi-tenant-saas-architectures.md | 1695 | 9d18bc690e66 | Document Outline {#index_split_001.html_calibre_pb_0 .calibre5} |
| book-extractions/saas-architectures-srs-extraction.md | 89 | 1b0b2b1ab281 | Building Multi-Tenant SaaS Architectures — SRS-Engine Extraction |
| docs/CHANGELOG.md | 364 | 8f23cb20e80c | Changelog - SRS-Skills Engine |
| docs/deterministic-governance.md | 85 | 49dab7c43529 | Deterministic Governance |
| docs/standards-clause-registry.md | 145 | 27a5b0ac8889 | Standards Clause Registry |
| domains/INDEX.md | 47 | 98d918348e06 | Domains Index |
| domains/agriculture/INDEX.md | 63 | 05b53d901072 | Domain: Agriculture |
| domains/agriculture/references/architecture-patterns.md | 226 | e755f350ca94 | Agriculture: Architecture Patterns |
| domains/automotive/INDEX.md | 47 | 22845920d82a | Domain: Automotive |
| domains/automotive/references/architecture-patterns.md | 65 | 016e0a493220 | Automotive — Architecture Patterns |
| domains/education/INDEX.md | 43 | 6c771ec32d12 | Domain: Education |
| domains/education/references/architecture-patterns.md | 64 | c39c0ad8145c | Education: Architecture Patterns |
| domains/finance/INDEX.md | 45 | 45cfeff778bc | Domain: Finance |
| domains/finance/references/architecture-patterns.md | 98 | f52e15d6f543 | Finance: Architecture Patterns |
| domains/government/INDEX.md | 43 | 5775d2ab94ad | Domain: Government |
| domains/government/references/architecture-patterns.md | 73 | 237ac769ded1 | Government: Architecture Patterns |
| domains/healthcare/INDEX.md | 45 | 43536d994502 | Domain: Healthcare |
| domains/healthcare/references/architecture-patterns.md | 63 | 7e98502fd20b | Healthcare: Architecture Patterns |
| domains/logistics/INDEX.md | 44 | 4906c5980c22 | Domain: Logistics |
| domains/logistics/features/warehouse-management.md | 37 | f880f9601867 | Feature: Warehouse Management |
| domains/logistics/references/architecture-patterns.md | 75 | f81c8ef4d412 | Logistics: Architecture Patterns |
| domains/productivity/INDEX.md | 62 | 5db08ca55e85 | Domain: Productivity (Knowledge Management & Desktop Productivity) |
| domains/productivity/features/search-indexing.md | 79 | 9de4fef0c211 | Feature: Search & Indexing |
| domains/productivity/references/architecture-patterns.md | 79 | fc0297db228a | Productivity — Architecture Patterns |
| domains/retail/INDEX.md | 70 | eba478357a97 | Domain: Retail |
| domains/retail/references/architecture-patterns.md | 48 | b0153da0beb9 | Retail: Architecture Patterns |
| domains/uganda/INDEX.md | 98 | 593b315a8769 | Domain: Uganda Government & Public Sector |
| projects/AcademiaPro/README.md | 185 | ba0bfb587d7e | AcademiaPro |
| projects/AcademiaPro/03-design-documentation/01-hld/02-security-architecture.md | 764 | d7b29f95505c | Security Architecture — Academia Pro |
| projects/AcademiaPro/03-design-documentation/02-lld/01-module-architecture.md | 663 | 6cecd902e8a8 | Low-Level Design — Academia Pro Phase 1 |
| projects/AcademiaPro/03-design-documentation/03-api-spec/00-index.md | 215 | 579d4a08be2c | OpenAPI 3.1 Specification — Academia Pro Phase 1 |
| projects/AcademiaPro/03-design-documentation/adr/README.md | 14 | 105415716da2 | Architecture Decision Records — pointer |
| projects/AcademiaPro/04-development/coding-standards.md | 28 | 4ddec3ce57f4 | Coding Standards — Academia Pro |
| projects/AcademiaPro/04-development/02-coding-guidelines/01-coding-guidelines.md | 478 | f5232739d826 | Coding Guidelines for Academia Pro |
| projects/AcademiaPro/04-development/02-coding-guidelines/manifest.md | 11 | 7fe8e394ab31 | Document Manifest |
| projects/AcademiaPro/06-deployment-operations/deployment-guide.md | 36 | 8219db48bbbc | Deployment Guide — Academia Pro |
| projects/AcademiaPro/06-deployment-operations/01-deployment-guide/01-deployment-guide.md | 589 | 2790e8ca1d6d | Deployment Guide — Academia Pro |
| projects/AcademiaPro/06-deployment-operations/01-deployment-guide/manifest.md | 11 | 95035ef8a5ed | Document Manifest |
| projects/AcademiaPro/08-end-user-documentation/02-installation-guide/01-installation-guide.md | 478 | 08c00b6f572d | AcademiaPro Installation Guide |
| projects/AcademiaPro/08-end-user-documentation/02-installation-guide/manifest.md | 11 | d791f83cb468 | Document Manifest |
| projects/AcademiaPro/09-governance-compliance/audit-report.md | 28 | 39c90a84d432 | Audit Report — Academia Pro v1.0 baseline |
| projects/AcademiaPro/09-governance-compliance/risk-assessment.md | 25 | bddb6d56c914 | Risk Assessment / Register — Academia Pro |
| projects/AcademiaPro/09-governance-compliance/01-traceability-matrix/01-traceability-matrix.md | 432 | 73b231012799 | Requirements Traceability Matrix — Academia Pro |
| projects/AcademiaPro/09-governance-compliance/01-traceability-matrix/manifest.md | 11 | de9012b51e5d | Document Manifest |
| projects/AcademiaPro/09-governance-compliance/02-audit-report/01-audit-report.md | 290 | 24b209016129 | Verification and Validation Audit Report — Academia Pro |
| projects/AcademiaPro/09-governance-compliance/02-audit-report/manifest.md | 11 | 3a26966a080f | Document Manifest |
| projects/AcademiaPro/09-governance-compliance/03-compliance/01-pdpo-compliance.md | 296 | 56219b819fb4 | Uganda Data Protection and Privacy Act 2019 — Compliance Document |
| projects/AcademiaPro/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 89 | 31009df9b33e | Control Evidence Matrix — Academia Pro |
| projects/AcademiaPro/09-governance-compliance/03-compliance/manifest.md | 12 | 18ae0226faed | Document Manifest |
| projects/AcademiaPro/09-governance-compliance/04-risk-assessment/01-risk-assessment.md | 354 | 1951a3be6044 | Risk Assessment — Academia Pro |
| projects/AcademiaPro/09-governance-compliance/04-risk-assessment/manifest.md | 11 | 7280bfeea903 | Document Manifest |
| projects/AcademiaPro/09-governance-compliance/05-adr/ADR-0001-laravel-over-node.md | 25 | 789c69b69aef | ADR-0001 Laravel 11 over Node/NestJS for backend |
| projects/AcademiaPro/09-governance-compliance/05-adr/ADR-0002-mysql-over-postgres.md | 25 | 97e2958b8271 | ADR-0002 MySQL 8 over PostgreSQL 15 |
| projects/AcademiaPro/09-governance-compliance/05-adr/ADR-0003-multi-tenant-via-tenant-id.md | 29 | 57aaaf013135 | ADR-0003 Multi-tenancy via tenant_id + Eloquent TenantScope |
| projects/AcademiaPro/09-governance-compliance/05-adr/ADR-0004-global-identity-architecture.md | 25 | bc2520ec0bc8 | ADR-0004 Global identity architecture for cross-school student portability |
| projects/AcademiaPro/09-governance-compliance/05-adr/ADR-0005-pii-scrubber-before-ai.md | 32 | 8153f98568b8 | ADR-0005 Mandatory PII scrubbing before every AI prompt |
| projects/AcademiaPro/09-governance-compliance/06-change-impact/CIA-001-add-dpia-for-ai-module.md | 22 | 695695752281 | CIA-001 — Add DPIA for the AI Module before Phase-2 go-live |
| projects/AcademiaPro/09-governance-compliance/06-change-impact/CIA-002-assign-runbook-contacts-sprint1.md | 22 | 044ac50bcbd0 | CIA-002 — Assign runbook on-call and team-lead contacts at Sprint 1 kick-off |
| projects/AcademiaPro/_context/quality-log.md | 11 | ff8840dd853f | Quality Log — Academia Pro |
| projects/AcademiaPro/_context/quality-standards.md | 35 | a7ee1329025c | Quality Standards — Academia Pro |
| projects/AcademiaPro/_context/quality_standards.md | 74 | 6ec97a6dcca3 | Quality Standards — Academia Pro |
| projects/Aqar-Property/README.md | 29 | 7544289ceb21 | Aqar-Property |
| projects/Aqar-Property/03-design-documentation/01-hld/03-runtime-architecture.md | 110 | 08b0f3f540d3 | Runtime Architecture |
| projects/Aqar-Property/03-design-documentation/01-hld/08-architecture-decisions.md | 134 | c1a2dc3040c5 | Architecture Decisions |
| projects/Aqar-Property/03-design-documentation/04-database-design/01-data-architecture-tenancy.md | 157 | 619681bd91ec | Data Architecture And Tenancy |
| projects/Aqar-Property/03-design-documentation/04-database-design/07-indexes-migrations-retention.md | 133 | 4ffd4c773caa | Indexes, Migrations, And Retention |
| projects/Aqar-Property/03-design-documentation/adr/README.md | 15 | d3b9445aa48a | Architecture Decision Records — Aqar |
| projects/Aqar-Property/04-development/coding-standards.md | 28 | 83da6718771d | Coding Standards — Aqar |
| projects/Aqar-Property/04-development-artifacts/01-technical-spec/04-delivery-standards.md | 64 | a6116cfc85ae | Delivery Standards |
| projects/Aqar-Property/04-development-artifacts/02-coding-guidelines/01-guidelines.md | 91 | 86df6be69e75 | Coding Guidelines |
| projects/Aqar-Property/04-development-artifacts/02-coding-guidelines/manifest.md | 3 | af3848af15cf | Document Manifest |
| projects/Aqar-Property/06-deployment-operations/deployment-guide.md | 28 | 3aa020ddae02 | Deployment Guide — Aqar |
| projects/Aqar-Property/06-deployment-operations/01-deployment-guide/01-deployment-guide.md | 147 | 2260b9f9c4d8 | Aqar Deployment Guide |
| projects/Aqar-Property/06-deployment-operations/01-deployment-guide/manifest.md | 2 | 442c58b7f7c2 |  |
| projects/Aqar-Property/08-end-user-documentation/02-installation-guide/01-installation-guide.md | 118 | e2c8547d2438 | Aqar Installation Guide |
| projects/Aqar-Property/08-end-user-documentation/02-installation-guide/manifest.md | 2 | ffb9e4cef946 |  |
| projects/Aqar-Property/09-governance-compliance/audit-report.md | 28 | bfae6277f57e | Audit Report — Aqar v1.1 baseline |
| projects/Aqar-Property/09-governance-compliance/risk-assessment.md | 25 | 1a4502897eb9 | Risk Assessment / Register — Aqar |
| projects/Aqar-Property/09-governance-compliance/01-traceability-matrix/01-traceability-matrix.md | 83 | e11fea4e490e | Aqar Traceability Matrix |
| projects/Aqar-Property/09-governance-compliance/01-traceability-matrix/manifest.md | 2 | 3c5426a8ff85 |  |
| projects/Aqar-Property/09-governance-compliance/02-audit-report/01-audit-report-template.md | 95 | c4224a63ff63 | Aqar Audit Report Template |
| projects/Aqar-Property/09-governance-compliance/02-audit-report/manifest.md | 2 | 9e38c156c60a |  |
| projects/Aqar-Property/09-governance-compliance/03-compliance/01-compliance.md | 115 | 6cf083afe7fe | Aqar Uganda Compliance Baseline |
| projects/Aqar-Property/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 66 | 20aab137f1f3 | Control Evidence Matrix — Aqar |
| projects/Aqar-Property/09-governance-compliance/03-compliance/manifest.md | 2 | d9e5d6df1d8e |  |
| projects/Aqar-Property/09-governance-compliance/04-risk-assessment/01-risk-assessment.md | 88 | 08c499ffef0f | Aqar Risk Assessment |
| projects/Aqar-Property/09-governance-compliance/04-risk-assessment/manifest.md | 2 | d91fcca652df |  |
| projects/Aqar-Property/_context/quality-log.md | 12 | 9d61a116f5c8 | Quality Log |
| projects/Aqar-Property/_context/quality-standards.md | 56 | dac66effc294 | Quality Standards |
| projects/Aqar-Property/_context/quality_standards.md | 76 | 6c39cc774a17 | Quality Standards |
| projects/BIRDC-ERP/02-requirements-engineering/01-srs-phase1-commerce/06-fr-inventory-warehouse.md | 344 | a6f9900229c0 | 3.3 Module F-003: Inventory and Warehouse Management |
| projects/BIRDC-ERP/02-requirements-engineering/04-srs-phase4-production/05-f012-quality-control.md | 531 | 7ac3cb507adb | 4. Specific Requirements — F-012: Quality Control & Laboratory |
| projects/BIRDC-ERP/03-design-documentation/01-hld/02-three-panel-architecture.md | 83 | d74fff6aa332 | 2. Three-Panel Application Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/03-deployment-architecture.md | 90 | bfa049b368b4 | 3. Deployment Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/04-application-architecture.md | 95 | a78f52a0e3a6 | 4. Application Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/05-database-architecture.md | 88 | 4e8f3c659d77 | 5. Database Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/09-security-architecture.md | 74 | fd858d538f17 | 9. Security Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/10-android-mobile-architecture.md | 92 | 18c663d93106 | 10. Android Mobile Architecture |
| projects/BIRDC-ERP/03-design-documentation/01-hld/11-external-integration-architecture.md | 97 | 1a67c9bf91a2 | 11. External Integration Architecture |
| projects/BIRDC-ERP/03-design-documentation/05-ux-spec/04-navigation-architecture.md | 161 | f3728394ff13 | 4. Navigation Architecture |
| projects/BIRDC-ERP/04-development/coding-standards.md | 31 | 70095d2820a0 | BIRDC ERP — Coding Standards |
| projects/BIRDC-ERP/04-development-artifacts/01-technical-spec/01-php-standards.md | 222 | cd3210bd0270 | 1. PHP 8.3+ Standards |
| projects/BIRDC-ERP/04-development-artifacts/01-technical-spec/02-mysql-standards.md | 163 | e17544131e08 | 2. MySQL 9.1 Database Standards |
| projects/BIRDC-ERP/04-development-artifacts/02-coding-guidelines/00-front-matter.md | 36 | d9fcdc15ab4a | Coding Guidelines — BIRDC ERP |
| projects/BIRDC-ERP/04-development-artifacts/02-coding-guidelines/01-php-guidelines.md | 179 | 58f1d02f939b | 1. PHP Coding Standards |
| projects/BIRDC-ERP/04-development-artifacts/02-coding-guidelines/02-kotlin-guidelines.md | 180 | df8e6cbf8ee9 | 2. Kotlin (Android) Coding Standards |
| projects/BIRDC-ERP/04-development-artifacts/02-coding-guidelines/03-git-workflow.md | 140 | 507af97ebbc3 | 3. Git Workflow |
| projects/BIRDC-ERP/04-development-artifacts/02-coding-guidelines/04-database-and-integrations.md | 223 | 84fbb89496d0 | 4. Database Access Rules |
| projects/BIRDC-ERP/05-testing-documentation/02-test-plan/10-test-case-index.md | 140 | 7cdcea47d532 | Test Case Index |
| projects/BIRDC-ERP/06-deployment-operations/deployment-guide.md | 37 | 96bad52cb82d | BIRDC ERP — Deployment Guide |
| projects/BIRDC-ERP/06-deployment-operations/01-deployment-guide/01-deployment-guide.md | 708 | e79a76393c31 | BIRDC ERP Deployment Guide |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/00-cover.md | 36 | a30ccd5480c0 | BIRDC ERP Installation and Configuration Guide |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/01-web-browser-access.md | 74 | e8defb07ee6d | Section 1: Web Browser Access |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/02-android-app-installation.md | 85 | de426ec9cb7d | Section 2: Android App Installation |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/03-first-time-configuration.md | 124 | 8822e091a2b6 | Section 3: First-Time Business Configuration |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/04-biometric-device.md | 53 | 12a0957cb47c | Section 4: ZKTeco Biometric Device Connection |
| projects/BIRDC-ERP/08-end-user-documentation/02-installation-guide/05-offline-mode.md | 83 | b3cc78285659 | Section 5: Offline Mode Guide |
| projects/BIRDC-ERP/08-end-user-documentation/03-faq/06-manufacturing-quality.md | 46 | ce2b5289b51a | Topic 6: Manufacturing and Quality |
| projects/BIRDC-ERP/09-governance-compliance/audit-report.md | 32 | b2a4d2c419ae | BIRDC ERP — Engine Gate Audit Report |
| projects/BIRDC-ERP/09-governance-compliance/risk-register.md | 21 | aaf3fdfd03d8 | BIRDC ERP — Risk Register |
| projects/BIRDC-ERP/09-governance-compliance/01-traceability-matrix/01-front-matter.md | 44 | fb0e682b223b | Requirements Traceability Matrix — BIRDC ERP |
| projects/BIRDC-ERP/09-governance-compliance/01-traceability-matrix/02-fr-to-bg-tc-matrix.md | 280 | df30e6687e84 | Section 1: Functional Requirements to Business Goals and Test Cases |
| projects/BIRDC-ERP/09-governance-compliance/01-traceability-matrix/03-br-to-fr-matrix.md | 27 | 5ad4ed35be91 | Section 2: Business Rules to Functional Requirements Matrix |
| projects/BIRDC-ERP/09-governance-compliance/01-traceability-matrix/04-dc-to-fr-matrix.md | 18 | ad1d57b4d6da | Section 3: Design Covenants to Functional Requirements Matrix |
| projects/BIRDC-ERP/09-governance-compliance/01-traceability-matrix/05-gap-analysis.md | 51 | 6c679ece80fd | Section 4: Traceability Gap Analysis |
| projects/BIRDC-ERP/09-governance-compliance/02-audit-report/01-front-matter.md | 48 | 51ee1318bdd8 | Pre-Development V&V Audit Report — BIRDC ERP |
| projects/BIRDC-ERP/09-governance-compliance/02-audit-report/02-findings.md | 111 | bd4bbf6202a2 | Section 2: Audit Findings by SRS Section |
| projects/BIRDC-ERP/09-governance-compliance/02-audit-report/03-gap-anomalies.md | 31 | 604268ea26f8 | Section 3: Open Anomalies — GAP-001 through GAP-014 |
| projects/BIRDC-ERP/09-governance-compliance/02-audit-report/04-verdict-and-recommendations.md | 48 | d47785bcdf76 | Section 4: Audit Verdict and Recommended Actions |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/01-front-matter.md | 37 | 13e32254909f | Regulatory Compliance Document — BIRDC ERP |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/02-dppa.md | 76 | 6a4a2cd6ba65 | Section 2: Uganda Data Protection and Privacy Act 2019 |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/03-ppda.md | 62 | 8727ccc14e40 | Section 3: PPDA Act Compliance |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/04-ura-efris-tax.md | 97 | bd822c8a74df | Section 4: Uganda Revenue Authority — EFRIS, PAYE, and WHT Compliance |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/05-nssf-icpau-iso.md | 126 | e437c345f07d | Section 5: NSSF, ICPAU, ISO 22000, and OAG Compliance |
| projects/BIRDC-ERP/09-governance-compliance/03-compliance/06-control-evidence-matrix.md | 44 | 58fff87e61d4 | BIRDC ERP — Control Evidence Matrix |
| projects/BIRDC-ERP/09-governance-compliance/04-risk-assessment/01-front-matter.md | 41 | 433800474c44 | Project Risk Assessment — BIRDC ERP |
| projects/BIRDC-ERP/09-governance-compliance/04-risk-assessment/02-risk-register.md | 288 | 065a388db494 | Section 2: Risk Register |
| projects/BIRDC-ERP/09-governance-compliance/04-risk-assessment/03-risk-summary.md | 50 | 0844bda33f43 | Section 3: Risk Summary and Heat Map |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/01-front-matter.md | 70 | b3ec67c19386 | DPPA 2019 Compliance Annex — BIRDC ERP System |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/02-pii-inventory.md | 91 | 94e3cb673076 | Section 2 — PII Inventory and Classification |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/03-lawful-basis.md | 65 | 118dc8959671 | Section 3 — Lawful Basis Mapping (Section 7, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/04-consent-requirements.md | 96 | 64de59f79707 | Section 4 — Consent Requirements (Sections 7, 8, 13, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/05-data-subject-rights.md | 106 | af286c038478 | Section 5 — Data Subject Rights (Sections 14–16, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/06-security-measures.md | 103 | a3a2cef7f585 | Section 6 — Security and Technical Measures (Section 20, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/07-retention-destruction.md | 78 | 8e8cb210e299 | Section 7 — Retention and Destruction Schedule (Section 18, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/08-breach-notification.md | 100 | ca5456b7cd68 | Section 8 — Data Breach Notification Procedure (Section 23, Regulation 33, DPPA 2019) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/09-dpo-pdpo-registration.md | 60 | 070e959e03e0 | Section 9 — DPO and PDPO Registration Requirements (Section 6, Regulations 15–16, 47) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/10-dpia-trigger.md | 52 | 0b077e8c3c9a | Section 10 — DPIA Trigger Assessment (Regulation 12, DPPA Regulations 2021) |
| projects/BIRDC-ERP/09-governance-compliance/05-dppa-annex/11-human-review-gate.md | 54 | 6bebe5225446 | Section 11 — Human Review Gate |
| projects/BIRDC-ERP/09-governance-compliance/06-dpia-farmer/01-dpia-farmer.md | 244 | a67cd0791201 | Data Protection Impact Assessment — Farmer Data Processing |
| projects/BIRDC-ERP/09-governance-compliance/07-open-items-register/01-register.md | 51 | 4988a4b710b4 | BIRDC ERP — Open Items and External-Dependency Register |
| projects/BIRDC-ERP/09-governance-compliance/08-gate-audits/01-ai-slop-audit-report.md | 75 | d00427628fdb | AI Slop Audit — BIRDC ERP documentation set — 2026-06-28 |
| projects/BIRDC-ERP/09-governance-compliance/08-gate-audits/02-finance-module-audit.md | 85 | bd63efd92ac2 | Finance Module Audit — BIRDC ERP — 2026-06-28 |
| projects/BIRDC-ERP/_context/quality-standards.md | 22 | 497476e07704 | BIRDC ERP — Applicable Quality & Regulatory Standards |
| projects/GarageFlow/04-development/coding-standards.md | 3 | 822d4227a810 | Coding Standards |
| projects/GarageFlow/06-deployment-operations/deployment-guide.md | 3 | f2960fff1c86 | Deployment Guide |
| projects/GarageFlow/09-governance-compliance/audit-report.md | 3 | aafa9f58d1d3 | Audit Report |
| projects/GarageFlow/09-governance-compliance/risk-register.md | 3 | a6e905292d12 | Risk Register |
| projects/GarageFlow/_context/quality-standards.md | 34 | 48590b38745b | Quality Standards — GarageFlow |
| projects/KampusPad/04-development/coding-standards.md | 40 | fe66e0726524 | Backend |
| projects/KampusPad/06-deployment-operations/deployment-guide.md | 38 | 70c35c8d9df4 | Deployment Guide |
| projects/KampusPad/09-governance-compliance/03-compliance.md | 60 | ed9dde8485db | Compliance Report |
| projects/KampusPad/09-governance-compliance/audit-report.md | 15 | 238302e6f5f0 | Audit Report |
| projects/KampusPad/09-governance-compliance/risk-register.md | 11 | 3405446e0faa |  |
| projects/KampusPad/_context/quality-standards.md | 39 | 12a1c1c8c3e8 | Quality Standards |
| projects/Kulima/README.md | 15 | 939720170403 | Kulima |
| projects/Kulima/03-design-documentation/adr/README.md | 24 | ca593e72dde7 | Architecture Decision Records — Kulima |
| projects/Kulima/04-development/coding-standards.md | 80 | 2d950e67bd0f | Coding Standards — Kulima Farm Operating System |
| projects/Kulima/04-development-artifacts/02-coding-guidelines/manifest.md | 10 | ca05d75eb4d4 | Document Manifest |
| projects/Kulima/06-deployment-operations/01-deployment-guide/deployment-guide.md | 88 | f1e11e0658cd | Deployment Guide — Kulima Farm Operating System |
| projects/Kulima/06-deployment-operations/01-deployment-guide/manifest.md | 10 | ca05d75eb4d4 | Document Manifest |
| projects/Kulima/08-end-user-documentation/02-installation-guide/manifest.md | 10 | ca05d75eb4d4 | Document Manifest |
| projects/Kulima/09-governance-compliance/audit-report.md | 41 | bc92ea559306 | Verification, Validation, and Anti-Slop Audit Report — Kulima |
| projects/Kulima/09-governance-compliance/risk-assessment.md | 23 | b120d2a1cf82 | Risk Assessment and Register — Kulima |
| projects/Kulima/09-governance-compliance/01-traceability-matrix/01-traceability-matrix.md | 43 | 759bd2046fa7 | Requirements Traceability Matrix — Kulima |
| projects/Kulima/09-governance-compliance/02-audit-report/01-audit-report.md | 41 | bc92ea559306 | Verification, Validation, and Anti-Slop Audit Report — Kulima |
| projects/Kulima/09-governance-compliance/03-compliance/01-dppa-compliance.md | 87 | dfe0b1dda301 | Data Protection Compliance Annex (DPPA 2019) and DPIA — Kulima |
| projects/Kulima/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 31 | b0c21ac564c7 | Control Evidence Matrix — Kulima |
| projects/Kulima/09-governance-compliance/04-risk-assessment/01-risk-assessment.md | 23 | b120d2a1cf82 | Risk Assessment and Register — Kulima |
| projects/Kulima/09-governance-compliance/04-risk-assessment/manifest.md | 10 | ca05d75eb4d4 | Document Manifest |
| projects/Kulima/09-governance-compliance/05-adr/0001-offline-first-sync.md | 20 | 87ca27e7901b | ADR-0001: Offline-first synchronisation with per-field last-write-wins |
| projects/Kulima/09-governance-compliance/05-adr/0002-tenant-isolation.md | 20 | 7d724948c06e | ADR-0002: Chwezi Core shared monolith with per-tenant isolation |
| projects/Kulima/09-governance-compliance/05-adr/0003-geojson-spatial-storage.md | 20 | e9d3bdf6c495 | ADR-0003: MySQL 8 JSON and spatial columns for GeoJSON boundaries |
| projects/Kulima/09-governance-compliance/05-adr/0004-mobile-money-record-only.md | 20 | 416dab3b7f29 | ADR-0004: Mobile money recorded but not API-validated in Phase 1 |
| projects/Kulima/09-governance-compliance/05-adr/0005-dual-mode-ledger.md | 21 | afb7a35fa662 | ADR-0005: Dual-mode accounting ledger with void-with-reversal immutability |
| projects/Kulima/09-governance-compliance/05-adr/0006-claude-ai-pii-scrubbing.md | 20 | cbb59ccd1bc1 | ADR-0006: Claude API as AI provider with mandatory PII scrubbing |
| projects/Kulima/_context/quality-log.md | 7 | 436fd7254a91 | Quality Log |
| projects/Kulima/_context/quality-standards.md | 37 | a7d6b4c82403 | Quality Standards — Kulima |
| projects/Kulima/_context/quality_standards.md | 57 | 8b49b90b0674 | Quality Standards |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/02-inventory/03-warehouse-management.md | 38 | 52234d3075b5 | Warehouse Management |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/05-hr-payroll/02a-position-and-workforce-governance.md | 18 | 223ea384abd7 | Position and Workforce Governance |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/05-hr-payroll/06a-payroll-governance-controls.md | 18 | d48aa06f617d | Payroll Governance and Controls |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/00-cover.md | 24 | c75595e99531 |  |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/01-introduction.md | 78 | 3bbefa1923cc | Introduction to the Sales Agents and Commissions Module |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/02-agent-register.md | 68 | 183ea99e459a | Agent Register |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/03-targets-attribution.md | 70 | 6bd6ce41dc26 | Sales Targets and Attribution |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/04-commission-rules.md | 76 | 9245e18044b2 | Commission Rule Engine |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/05-commission-run.md | 78 | a2b1dd614bc0 | Commission Run, Approval Workflow, and Mobile Money Payout |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/06-agent-portal.md | 70 | c7e354ccaeb3 | Agent Self-Service Portal |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/07-stock-remittance.md | 78 | a8d460a1d426 | Agent Stock Management, Remittance Verification, and Daily Summaries |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/08-nfrs.md | 73 | f891083c2c64 | Non-Functional Requirements |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/09-traceability.md | 96 | d51d5ca44963 | Traceability Matrix, Context Gaps, and Verification Notes |
| projects/LonghornERP/02-requirements-engineering/01-srs/01-modules/10-sales-agents/manifest.md | 11 | ca355c72fa0d |  |
| projects/LonghornERP/03-design-documentation/01-hld/06-security-architecture.md | 99 | d6296662f67c | Security Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/08-api-architecture.md | 115 | 922b07dfa311 | API Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/10-mobile-architecture.md | 83 | e229a698ab22 | Mobile Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/11-architecture-decision-records.md | 179 | 64858ae8d07c | Architecture Decision Records |
| projects/LonghornERP/03-design-documentation/01-hld/12-industrial-architecture.md | 119 | dbe2852b4537 | Industrial Module Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/13-finance-operations-and-group-architecture.md | 175 | cf40f51c3386 | 13. Finance Operations and Group Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/14-customer-revenue-and-service-architecture.md | 219 | 9b195d0e3f08 | Customer, Revenue, and Service Architecture |
| projects/LonghornERP/03-design-documentation/01-hld/15-workforce-planning-and-asset-operations-architecture.md | 122 | a3237ef9ddc0 | Workforce, Planning, and Asset Operations Architecture |
| projects/LonghornERP/03-design-documentation/04-database-design/10-indexing-strategy.md | 112 | 33d3ad3f643a | Indexing Strategy |
| projects/LonghornERP/03-design-documentation/adr/README.md | 16 | f6d87afc8f37 | Architecture Decision Records — Index |
| projects/LonghornERP/04-development/coding-standards.md | 29 | aa18f8fdd982 | Coding Standards — Longhorn ERP |
| projects/LonghornERP/04-development/02-coding-guidelines/00-cover.md | 35 | cb7aa0c75cb3 | Coding Guidelines |
| projects/LonghornERP/04-development/02-coding-guidelines/01-php-standards.md | 97 | 93ea96a9e29c | PHP 8.3 Coding Standards |
| projects/LonghornERP/04-development/02-coding-guidelines/02-security-rules.md | 146 | 4e989618d1ac | Mandatory Security Rules |
| projects/LonghornERP/04-development/02-coding-guidelines/03-database-patterns.md | 93 | 63119e46b79b | Database Access Patterns |
| projects/LonghornERP/04-development/02-coding-guidelines/04-service-layer-patterns.md | 86 | e134fc7f2a6d | Service Layer Patterns |
| projects/LonghornERP/04-development/02-coding-guidelines/05-api-endpoint-patterns.md | 98 | 188bd9e41235 | REST API Endpoint Conventions |
| projects/LonghornERP/04-development/02-coding-guidelines/06-frontend-patterns.md | 92 | 2b4f2029a379 | Frontend JavaScript Conventions |
| projects/LonghornERP/04-development/02-coding-guidelines/07-formatting-conventions.md | 68 | 10077c022895 | Data Formatting Conventions |
| projects/LonghornERP/04-development/02-coding-guidelines/08-testing-standards.md | 74 | 4b1ce6b9175a | Testing Standards |
| projects/LonghornERP/04-development/02-coding-guidelines/09-git-conventions.md | 68 | 460b4b759ded | Git Workflow Conventions |
| projects/LonghornERP/04-development/02-coding-guidelines/manifest.md | 11 | ab41ec0c7c5f |  |
| projects/LonghornERP/04-development/04-contribution-guide/contribution-guide.md | 30 | 41798f092313 | Contribution Guide — Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/00-cover.md | 17 | 11868cae32fd |  |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/01-server-requirements.md | 47 | d68db6952286 | Server Requirements for Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/02-installation.md | 110 | 4305efc9304c | Installation Procedure for Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/03-configuration.md | 133 | 0a2a08c63b7c | Configuration Reference for Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/04-first-run.md | 61 | ceb2330312d6 | First-Run Configuration for Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/05-backup-update.md | 162 | 8c2e52e400ee | Backup, Update, and Security Hardening for Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/deployment-guide.md | 38 | e1b13913406b | Deployment Guide — Longhorn ERP |
| projects/LonghornERP/06-deployment-operations/01-deployment-guide/manifest.md | 7 | 8c6daf19372d |  |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/00-cover.md | 17 | 26c8ddb3b348 |  |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/01-signup-plan-selection.md | 62 | 9458454f0ae3 | Step 1: Sign Up and Choose Your Plan |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/02-workspace-setup.md | 100 | 2f1e49542c1b | Step 2: Set Up Your Workspace |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/03-integration-setup.md | 73 | 0a82df0ef678 | Step 3: Set Up Integrations |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/04-data-import.md | 103 | 8876f526eb3e | Step 4: Import Your Existing Data |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/05-go-live-checklist.md | 79 | 37a4c5d2d70f | Step 5: Go-Live Checklist |
| projects/LonghornERP/08-end-user-documentation/02-installation-guide/manifest.md | 7 | 0ab7ab9d477c |  |
| projects/LonghornERP/09-governance-compliance/ai-slop-audit-report.md | 48 | 5a1baa92f4c8 | AI Slop Audit Report — Longhorn ERP |
| projects/LonghornERP/09-governance-compliance/audit-report.md | 34 | fbd017df072b | IEEE 1012 Audit Report — Longhorn ERP |
| projects/LonghornERP/09-governance-compliance/finance-module-audit-report.md | 47 | bc8f80531644 | Finance-Module Audit Report — Longhorn ERP |
| projects/LonghornERP/09-governance-compliance/risk-register.md | 18 | 687ae49ef136 | Risk Register — Longhorn ERP |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/00-cover.md | 17 | 1f3c413d428b |  |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/01-introduction.md | 81 | b75212754d84 | 1. Introduction |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/02-summary-statistics.md | 57 | 4ea74eb05e0b | 2. Summary Statistics |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/03-platform-traceability.md | 446 | 36e42de9b22d | 3. Platform Requirements Traceability |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/04-core-modules-traceability.md | 402 | d84a971d3742 | 4. Core Module Requirements Traceability |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/05-addon-modules-traceability.md | 705 | af7ef0fdb248 | 5. Add-On Module Requirements Traceability |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/06-gap-register.md | 93 | 071b30bf0368 | 6. Gap Register |
| projects/LonghornERP/09-governance-compliance/01-traceability-matrix/manifest.md | 8 | 8fd98cb396d1 |  |
| projects/LonghornERP/09-governance-compliance/03-compliance/00-cover.md | 35 | bbd34bc715ae | Security Model and Compliance Framework |
| projects/LonghornERP/09-governance-compliance/03-compliance/01-security-overview.md | 41 | 47eb80cb4ea1 | Security Design Philosophy |
| projects/LonghornERP/09-governance-compliance/03-compliance/02-authentication.md | 85 | fb8a67e86eaf | Authentication Model |
| projects/LonghornERP/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 33 | 15a7d6a35a86 | Control Evidence Matrix — Longhorn ERP |
| projects/LonghornERP/09-governance-compliance/03-compliance/03-authorization.md | 70 | 9a0dad054e57 | Authorization Model |
| projects/LonghornERP/09-governance-compliance/03-compliance/04-tenant-isolation.md | 58 | 2b22967a9fb8 | Tenant Data Isolation Controls |
| projects/LonghornERP/09-governance-compliance/03-compliance/05-audit-log.md | 64 | 6a1216fdea5f | Audit Log Security Requirements |
| projects/LonghornERP/09-governance-compliance/03-compliance/06-data-protection.md | 67 | 47afb5ffdfb3 | Data Protection and Privacy |
| projects/LonghornERP/09-governance-compliance/03-compliance/07-network-security.md | 94 | a1b43e702e9b | Transport and Network Security |
| projects/LonghornERP/09-governance-compliance/03-compliance/08-owasp-compliance.md | 144 | de960ff278d2 | OWASP Top 10 (2021) Compliance Requirements |
| projects/LonghornERP/09-governance-compliance/03-compliance/09-nita-u-compliance.md | 42 | bab69df867ff | NITA-U SaaS Compliance Obligations |
| projects/LonghornERP/09-governance-compliance/03-compliance/10-compliance-checklist.md | 38 | 8b359162087c | Pre-Launch Compliance Checklist |
| projects/LonghornERP/09-governance-compliance/03-compliance/manifest.md | 12 | c9b3f6043435 |  |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/00-cover.md | 17 | bd8145d20073 |  |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/01-introduction.md | 66 | 25f64e568bba | Risk Assessment — Introduction and Methodology |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/02-gap-risks.md | 27 | 964a51ece94f | Gap-Derived Risk Register (RISK-001 – RISK-018) |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/03-operational-risks.md | 15 | 6ba42742a9b0 | Operational and Architectural Risk Register (RISK-019 – RISK-024) |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/04-risk-summary.md | 49 | af576276ed98 | Risk Summary and Prioritisation |
| projects/LonghornERP/09-governance-compliance/04-risk-assessment/manifest.md | 6 | ace87f0259fe |  |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0001-php-di-service-architecture.md | 26 | 1208384bfc0a | ADR-0001: Service-oriented PHP 8.3 with PHP-DI over a full-stack framework |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0002-mysql-91-single-store.md | 21 | 186460861ae5 | ADR-0002: MySQL 9.1 InnoDB as the single relational store |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0003-multitenancy-tenant-id.md | 25 | 9353020995ed | ADR-0003: Shared-database multi-tenancy with row-level tenant_id isolation |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0004-ledger-first-accounting.md | 22 | daabab760ac3 | ADR-0004: Ledger-first accounting with module GL auto-posting |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0005-localisation-as-configuration.md | 22 | 4da4811f4520 | ADR-0005: Localisation-as-configuration via jurisdiction compliance adapters |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0006-jwt-mobile-api-registry.md | 22 | 74323795698a | ADR-0006: JWT-authenticated mobile API with a self-documenting endpoint registry |
| projects/LonghornERP/09-governance-compliance/05-adr/ADR-0007-hash-chained-audit-log.md | 25 | 488b3a78eb2d | ADR-0007: Tamper-evident hash-chained audit log (Roadmap control) |
| projects/LonghornERP/_context/quality-standards.md | 63 | 900032b56be8 | Quality Standards — Longhorn ERP |
| projects/Maduuka/README.md | 15 | 7d2f6d94e829 | Maduuka - SRS Documentation |
| projects/Maduuka/04-development/coding-standards.md | 32 | 7c2b8dbe6c4d | Maduuka Coding Standards |
| projects/Maduuka/04-development-artifacts/02-coding-guidelines/01-coding-guidelines.md | 198 | d4b675be1171 | Maduuka -- Coding Guidelines |
| projects/Maduuka/04-development-artifacts/02-coding-guidelines/manifest.md | 6 | 8e8fa55f66e1 | Document Manifest |
| projects/Maduuka/06-deployment-operations/deployment-guide.md | 38 | 24e1fcdf7735 | Maduuka Deployment Guide |
| projects/Maduuka/06-deployment-operations/01-deployment-guide/01-deployment-guide.md | 266 | 8eb8dbdfbbfc | Deployment Guide -- Maduuka Production System |
| projects/Maduuka/06-deployment-operations/01-deployment-guide/manifest.md | 6 | 6f5e8b89f61b | Document Manifest |
| projects/Maduuka/08-end-user-documentation/02-installation-guide/01-installation-guide.md | 198 | 17591221f517 | Maduuka Installation and Setup Guide |
| projects/Maduuka/08-end-user-documentation/02-installation-guide/manifest.md | 6 | 3c08c1153af8 | Document Manifest |
| projects/Maduuka/09-governance-compliance/audit-report.md | 37 | 0c25917e333a | Maduuka V&V Audit Report (IEEE 1012) |
| projects/Maduuka/09-governance-compliance/risk-register.md | 18 | a67f4444ad73 | Maduuka Risk Register |
| projects/Maduuka/09-governance-compliance/01-traceability-matrix/01-traceability-matrix.md | 261 | 1d041ff86cf1 | Traceability Matrix: Maduuka Phase 1 |
| projects/Maduuka/09-governance-compliance/01-traceability-matrix/02-traceability-matrix-continued.md | 222 | 713416306143 | 3.6 Module 4.6 — Financial Accounts and Cash Flow (FR-FIN-xxx) |
| projects/Maduuka/09-governance-compliance/01-traceability-matrix/manifest.md | 3 | 9c2566b1f460 |  |
| projects/Maduuka/09-governance-compliance/02-audit-report/01-audit-report.md | 306 | beee19571af7 | SRS Documentation Audit Report — Maduuka Phase 1 |
| projects/Maduuka/09-governance-compliance/02-audit-report/manifest.md | 6 | dd8a999460a4 | Document Manifest |
| projects/Maduuka/09-governance-compliance/03-compliance/01-compliance.md | 107 | bdb630bcb587 | Compliance and Data Protection — Maduuka |
| projects/Maduuka/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 28 | d99be2b7acc1 | Control Evidence Matrix |
| projects/Maduuka/09-governance-compliance/03-compliance/manifest.md | 6 | ed85f90c8472 | Document Manifest |
| projects/Maduuka/09-governance-compliance/04-risk-assessment/01-risk-assessment.md | 178 | 855e1557f7f2 | Risk Assessment — Maduuka Phase 1 |
| projects/Maduuka/09-governance-compliance/04-risk-assessment/manifest.md | 2 | c121581276af |  |
| projects/Maduuka/09-governance-compliance/05-adr/0001-vanilla-php-router.md | 26 | 090a5f6da013 | **ADR-0001**: Vanilla PHP 8.3 PSR-4 application over a full-stack framework |
| projects/Maduuka/09-governance-compliance/05-adr/0002-shared-db-multitenancy.md | 25 | 02ba36b4da29 | **ADR-0002**: Shared-database multi-tenancy with franchise_id row-level isolation |
| projects/Maduuka/09-governance-compliance/05-adr/0003-offline-first-room-sync.md | 25 | f73b49e56900 | **ADR-0003**: Offline-first Android client with Room and WorkManager sync |
| projects/Maduuka/09-governance-compliance/05-adr/0004-dual-auth-jwt-session.md | 26 | eb51d9edeaa8 | **ADR-0004**: Dual authentication — JWT for API clients, session for the web UI |
| projects/Maduuka/09-governance-compliance/05-adr/0005-ledger-first-accounting.md | 26 | 6233972ef909 | **ADR-0005**: Ledger-first double-entry accounting with module GL auto-posting |
| projects/Maduuka/09-governance-compliance/05-adr/0006-efris-queue-accreditation.md | 26 | 59b9f2ad02c6 | **ADR-0006**: EFRIS integration via an asynchronous queue with a sandbox-to-production accreditation path |
| projects/Maduuka/_context/quality-log.md | 6 | b79c6c594f90 | Quality Log -- Maduuka |
| projects/Maduuka/_context/quality-standards.md | 60 | 9711e2e64017 | Quality and Compliance Standards — Maduuka |
| projects/Maduuka/_context/quality_standards.md | 43 | e9f4973d230f | Quality Standards -- Maduuka |
| projects/Medic8/README.md | 143 | 55098e46e7d2 | Medic8 |
| projects/Medic8/03-design-documentation/01-hld/01-system-architecture.md | 578 | bf2c937a8c53 | System Architecture — Medic8 |
| projects/Medic8/03-design-documentation/01-hld/02-security-architecture.md | 398 | 8106970370c3 | Security Architecture — Medic8 |
| projects/Medic8/03-design-documentation/02-lld/01-module-architecture.md | 2966 | 839c1a035429 | Low-Level Design — Medic8 Phase 1 |
| projects/Medic8/03-design-documentation/03-api-spec/00-index.md | 2365 | 5d0688e5d10e | API Specification Index — Medic8 Phase 1 |
| projects/Medic8/04-development/coding-standards.md | 15 | 16c6e18fa2ff | Coding Standards: Medic8 |
| projects/Medic8/04-development-artifacts/02-coding-guidelines/01-coding-guidelines.md | 664 | 50df74b3bf56 | Coding Guidelines -- Medic8 Healthcare Management System |
| projects/Medic8/04-development-artifacts/02-coding-guidelines/manifest.md | 6 | 2dce95bca555 | Document Manifest |
| projects/Medic8/06-deployment-operations/deployment-guide.md | 16 | ff507279c4e1 | Deployment Guide: Medic8 |
| projects/Medic8/06-deployment-operations/01-deployment-guide/01-deployment-guide.md | 709 | 165f6956e91b | Deployment Guide for Medic8 Healthcare Management System |
| projects/Medic8/06-deployment-operations/01-deployment-guide/manifest.md | 6 | b3e9ba71776f | Document Manifest |
| projects/Medic8/08-end-user-documentation/02-installation-guide/01-installation-guide.md | 254 | 3fe7ba629a40 | Medic8 Installation and Onboarding Guide |
| projects/Medic8/08-end-user-documentation/02-installation-guide/manifest.md | 6 | ca2958d1e78b | Document Manifest |
| projects/Medic8/09-governance-compliance/audit-report.md | 18 | 66320613dd2f | IEEE 1012 Audit Report: Medic8 |
| projects/Medic8/09-governance-compliance/risk-register.md | 19 | bf5615a497d8 | Risk Register: Medic8 |
| projects/Medic8/09-governance-compliance/01-traceability-matrix/01-traceability-matrix.md | 297 | c28738479547 | Requirements Traceability Matrix -- Medic8 |
| projects/Medic8/09-governance-compliance/01-traceability-matrix/manifest.md | 6 | 55851e466e83 | Document Manifest |
| projects/Medic8/09-governance-compliance/02-audit-report/01-audit-report-template.md | 277 | 4b29b69dacba | Audit Report Template -- Medic8 |
| projects/Medic8/09-governance-compliance/02-audit-report/manifest.md | 6 | f7fd895a2e11 | Document Manifest |
| projects/Medic8/09-governance-compliance/03-compliance/01-compliance-documentation.md | 349 | 85f396368316 | Regulatory Compliance Documentation -- Medic8 |
| projects/Medic8/09-governance-compliance/03-compliance/02-control-evidence-matrix.md | 28 | d9159adc1859 | Control Evidence Matrix: Medic8 |
| projects/Medic8/09-governance-compliance/03-compliance/03-finance-accounting-standards.md | 54 | df94d0bb0b98 | Finance and Accounting Standards and Remediation Record |
| projects/Medic8/09-governance-compliance/03-compliance/manifest.md | 8 | 65794798e45a | Document Manifest |
| projects/Medic8/09-governance-compliance/04-risk-assessment/01-risk-assessment.md | 343 | 21e58c6ad8ef | Risk Assessment -- Medic8 |
| projects/Medic8/09-governance-compliance/04-risk-assessment/manifest.md | 6 | de0bc956d3bc | Document Manifest |
| projects/Medic8/09-governance-compliance/05-adr/ADR-0001-patient-identity-empi.md | 9 | 550bf6deb041 | ADR-0001: patient identity empi |
| projects/Medic8/09-governance-compliance/05-adr/ADR-0002-custom-php-di-framework.md | 40 | 974739e79b67 | ADR-0002: Custom PHP Application Framework (no full-stack framework) |
| projects/Medic8/09-governance-compliance/05-adr/ADR-0003-tenant-isolation-facility-id.md | 9 | 4ac672af99e2 | ADR-0003: Row-Level Tenant Isolation via `franchise_id` |
| projects/Medic8/09-governance-compliance/05-adr/ADR-0004-phi-encryption-aes256gcm.md | 9 | cfa82afe882e | ADR-0004: phi encryption aes256gcm |
| projects/Medic8/09-governance-compliance/05-adr/ADR-0005-ai-provider-adapter.md | 9 | f7c0fce0c3ed | ADR-0005: ai provider adapter |
| projects/Medic8/_context/quality-log.md | 7 | 89607c3c0c73 | Quality Log — Medic8 |
| projects/Medic8/_context/quality-standards.md | 74 | d1f5970e8756 | Quality and Performance Standards for Medic8 |
| projects/Medic8/_context/quality_standards.md | 69 | e5728e2fff5c | Quality and Performance Standards for Medic8 |
| projects/Ogma-Library/03-design-documentation/01-hld/01-architecture-overview.md | 90 | bd46ea44285c | 1. Architecture Overview |
| projects/Ogma-Library/03-design-documentation/01-hld/04-data-architecture.md | 100 | 40e291e52514 | 4. Data Architecture |
| projects/Ogma-Library/03-design-documentation/01-hld/07-ai-architecture.md | 60 | 91a58bce2c40 | 7. AI Architecture |
| projects/Ogma-Library/03-design-documentation/01-hld/08-lan-classroom-architecture.md | 93 | eb7de355f878 | 8. LAN / Classroom E-Library Architecture |
| projects/Ogma-Library/04-development/coding-standards.md | 153 | ebab1cb71f96 | Coding Standards for the Ogma Library Codebase |
| projects/Ogma-Library/06-deployment-operations/deployment-guide.md | 73 | faebdc750984 | Release, Build, Sign, and Distribute Guide |
| projects/Ogma-Library/08-end-user-documentation/installation-guide.md | 95 | 7e0447228160 | Ogma Library — Installation Guide |
| projects/Ogma-Library/09-governance-compliance/audit-report.md | 87 | 9bedc22f0003 | Internal Audit Report — Documentation Baseline v2.0 and As-Built System |
| projects/Ogma-Library/09-governance-compliance/risk-register.md | 67 | a22d606fd241 | Risk Register — Ogma Library |
| projects/Ogma-Library/09-governance-compliance/01-traceability-matrix/traceability-matrix.md | 101 | b53055ad4faf | Requirements Traceability Matrix — Governance Rollup |
| projects/Ogma-Library/09-governance-compliance/03-dpia/00-cover.md | 27 | 5d760c0eba98 | Data Protection Impact Assessment — Ogma Library |
| projects/Ogma-Library/09-governance-compliance/03-dpia/01-processing-overview.md | 44 | fd2f18fe30d2 | 1. Processing Overview |
| projects/Ogma-Library/09-governance-compliance/03-dpia/02-necessity-and-proportionality.md | 38 | cfb3afa542b5 | 2. Necessity and Proportionality |
| projects/Ogma-Library/09-governance-compliance/03-dpia/03-risk-assessment.md | 35 | b3a8971c8420 | 3. Risk Assessment |
| projects/Ogma-Library/09-governance-compliance/03-dpia/04-data-subject-rights.md | 27 | c3076e13e0b4 | 4. Data Subject Rights |
| projects/Ogma-Library/09-governance-compliance/03-dpia/05-conclusion-and-actions.md | 31 | 69692ffb8885 | 5. Conclusion and Required Actions |
| projects/Ogma-Library/09-governance-compliance/03-dpia/06-dpia-trigger-register.md | 16 | c86879a85618 | 6. DPIA Trigger Register |
| projects/Ogma-Library/09-governance-compliance/03-dpia/manifest.md | 8 | 2ab44e388e41 |  |
| projects/Ogma-Library/09-governance-compliance/05-adr/0001-runtime-dotnet-10-lts.md | 52 | 4ebaee2b2290 | ADR-0001: Target .NET 10 LTS as the Application Runtime |
| projects/Ogma-Library/09-governance-compliance/05-adr/0002-ui-shell-avalonia.md | 58 | f7bd54e51ba4 | ADR-0002: Adopt Avalonia as the Cross-Platform Desktop Shell |
| projects/Ogma-Library/09-governance-compliance/05-adr/0003-3d-shelf-webview-threejs.md | 58 | 41fe30c7c97f | ADR-0003: Render the 3D Shelf with WebView-Hosted Three.js Behind a Spike Gate |
| projects/Ogma-Library/09-governance-compliance/05-adr/0004-pdf-render-pdfium.md | 65 | 295a05aef9c4 | ADR-0004: Render and Extract PDF Content with PDFium Behind an Adapter |
| projects/Ogma-Library/09-governance-compliance/05-adr/0005-storage-sqlite-sidecar.md | 52 | e3f881930bd4 | ADR-0005: Use a SQLite Catalogue of Record with a Sidecar Asset Folder |
| projects/Ogma-Library/09-governance-compliance/05-adr/0006-search-hybrid-fts5-embeddings.md | 54 | 52922ee9574e | ADR-0006: Build Search as Hybrid Metadata, FTS5, and Semantic Embeddings |
| projects/Ogma-Library/09-governance-compliance/05-adr/0007-ai-provider-gateway-privacy-tiers.md | 54 | 5f9c0cb40205 | ADR-0007: Route AI Through a Provider-Neutral Gateway with Four Privacy Tiers |
| projects/Ogma-Library/09-governance-compliance/05-adr/0008-metadata-writeback-db-first.md | 52 | 3233c81eb77f | ADR-0008: Store Annotations and Metadata Database-First, Write Back to PDF Later |
| projects/Ogma-Library/09-governance-compliance/05-adr/0009-packaging-velopack-msix.md | 52 | 84f2f8e7eb83 | ADR-0009: Distribute with Velopack for Direct Channels and MSIX for Store and Enterprise |
| projects/Ogma-Library/09-governance-compliance/05-adr/0010-optin-library-host-mode.md | 62 | 5360423e2f02 | ADR-0010: Opt-In Library Host Mode Amends CI-2 for the Classroom Track |
| projects/Ogma-Library/09-governance-compliance/05-adr/0011-local-tesseract-ocr.md | 52 | 1ca5bb721239 | ADR-0011: Run OCR Locally with Tesseract, Never Through AI Providers |
| projects/Ogma-Library/09-governance-compliance/05-adr/0012-classroom-identity-roles-private-state.md | 55 | d127cbedb2fe | ADR-0012: Classroom Identity, Roles, and Per-Student Private State |
| projects/Ogma-Library/09-governance-compliance/05-adr/0013-school-managed-ai-host-gateway.md | 57 | 606c3cfd4a63 | ADR-0013: School-Managed AI Through the Host Gateway |
| projects/Ogma-Library/09-governance-compliance/05-adr/0014-efcore-9-on-net10-version-alignment.md | 45 | 39466c365c72 | ADR-0014: EF Core 9.x on the net10.0 Runtime — Version Alignment |
| projects/Ogma-Library/09-governance-compliance/05-adr/0015-documentation-baseline-v2-supersession.md | 51 | 60dc4e5d5044 | ADR-0015: Documentation Baseline v2.0 Supersedes the v1.0 Baseline |
| projects/Ogma-Library/09-governance-compliance/05-adr/README.md | 41 | f062bfd473b5 | Architecture Decision Records — Ogma Library |
| projects/Ogma-Library/09-governance-compliance/05-adr/manifest.md | 17 | fbf86647d4d4 |  |
| projects/_demo-hybrid-regulated/README.md | 78 | e424f83272fc | _demo-hybrid-regulated — Livelink Health (Uganda) |
| projects/_demo-hybrid-regulated/03-design-documentation/adr/README.md | 7 | 7b7903f75427 | Architecture Decision Records |
| projects/_demo-hybrid-regulated/04-development/coding-standards.md | 6 | a5d222c774b7 | Coding Standards |
| projects/_demo-hybrid-regulated/06-deployment-operations/deployment-guide.md | 6 | 48ac92c9d84b | Deployment Guide |
| projects/_demo-hybrid-regulated/09-governance-compliance/01-traceability-matrix.md | 19 | d3df66143d3a | Traceability Matrix |
| projects/_demo-hybrid-regulated/09-governance-compliance/03-compliance.md | 28 | 399530f9693b | Compliance Report |
| projects/_demo-hybrid-regulated/09-governance-compliance/audit-report.md | 15 | 2a2e24291f8f | Audit Report |
| projects/_demo-hybrid-regulated/09-governance-compliance/risk-assessment.md | 8 | 1f70508732c4 | Risk Assessment |
| projects/_demo-hybrid-regulated/09-governance-compliance/05-adr/ADR-0001-postgres-over-mysql.md | 28 | 9288d2cf5e44 | ADR-0001 Postgres over MySQL |
| projects/_demo-hybrid-regulated/09-governance-compliance/05-adr/ADR-0002-soft-delete-for-dppa-erasure.md | 29 | 80a7c9bccec4 | ADR-0002 Soft-delete with crypto-shredding for DPPA erasure |
| projects/_demo-hybrid-regulated/09-governance-compliance/06-change-impact/CIA-001-add-mfa-to-provider-login.md | 29 | f6bfea550f40 | CIA-001 Add MFA (TOTP) to provider login |
| projects/_demo-hybrid-regulated/_context/quality-standards.md | 7 | 429584a676e8 | Quality Standards |
| templates/README.md | 30 | 28c54ad08ca7 | Templates |
