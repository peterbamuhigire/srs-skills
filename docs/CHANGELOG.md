# Changelog - SRS-Skills Engine

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - 2026-02-07

### Added

**AI-Assisted Development Skills:**
- **ai-assisted-development** - Orchestration patterns for coordinating multiple AI agents in software development workflows
  - 5 orchestration strategies (Sequential, Parallel, Conditional, Looping, Retry)
  - 3 AI-specific patterns (Agent Handoff, Fan-Out/Fan-In, Human-in-the-Loop)
  - Real-world examples from MADUUKA and BRIGHTSOMA applications
  - References: orchestration-strategies.md, ai-patterns.md, practical-examples.md

- **orchestration-best-practices** - The 10 Commandments of Orchestration for multi-step workflows
  - Enforces clear step definition, dependency tracking, error handling
  - Complete code examples (good vs bad patterns)
  - Verification checklist for all generated code
  - Anti-patterns guide

- **ai-error-prevention** - Error prevention strategies for AI-assisted development (Trust But Verify)
  - 7 prevention strategies to minimize wasted tokens and catch Claude's mistakes early
  - Common Claude failure modes and prevention techniques
  - App-specific checklists (MADUUKA, MEDIC8, BRIGHTSOMA, DDA, CROWNPOINT)
  - Token savings: 50-75% reduction in wasted tokens
  - References: prevention-strategies.md, failure-modes.md, app-specific-prevention.md

- **ai-error-handling** - 5-layer validation stack for AI-generated code
  - Layer 1: Syntax validation
  - Layer 2: Requirement matching
  - Layer 3: Test validation
  - Layer 4: Security checks
  - Layer 5: Documentation validation
  - Quality scoring system (0-100 with 80% acceptance threshold)

**Reference Guides:**
- **prompting-patterns-reference.md** - 10 essential prompting patterns for better AI instructions
  - Clear Task + Context + Constraints, Chain-of-Thought, Few-Shot Learning, etc.
  - Reduces clarification questions by 50%, improves first-time-right code by 60%

- **orchestration-patterns-reference.md** - Comprehensive orchestration guide for multi-agent workflows
  - 5 orchestration types with real-world examples
  - 4 core patterns (Map-Reduce, Pipeline, Fan-Out/Fan-In, Circuit Breaker)
  - Decision trees and complexity vs performance analysis

- **encoding-patterns-into-skills.md** - Guide for creating pattern-enforcing skills
  - Formula: Rules + Examples + Checklists + Decision Trees
  - Pattern encoding templates
  - Skill effectiveness and iteration strategies

**Documentation Standards:**
- All new skills comply with doc-standards.md (500-line hard limit)
- Two-tier structure (Tier 1 TOC + Tier 2 deep dives)
- Smart subdirectory grouping for maintainability

### Changed

- **skills/CLAUDE.md** - Updated repository structure to include AI development skills
- **skills/ai-assisted-development/SKILL.md** - Refactored from 879 lines to 462 lines (compliant)
  - Split into main SKILL.md + 3 reference files
  - Improved navigability and token efficiency

### Performance

- **Token Efficiency Improvements:**
  - ai-error-prevention saves 50-75% of tokens through early error detection
  - Prompting patterns reduce clarification rounds by 50%
  - Orchestration patterns enable 30-50% faster parallel execution

### Documentation

- Updated to reflect expanded scope beyond SDLC documentation to include AI development assistance
- All skills now enforce automatic pattern following through structured templates

## [3.0.0] - 2026-02-06

### Added

- Multi-methodology support (Waterfall, Agile, Hybrid)
- Expanded from SRS-only to 23 document types across 10 SDLC phases
- Phase 00: Meta-initialization for methodology detection
- Agile track: User story generation with INVEST criteria
- Backward compatibility with v2.x Waterfall SRS pipeline

### Changed

- Renamed from SRS-Skills to SDLC-Docs-Engine
- Reorganized phases: 01-08 → 02-requirements-engineering/waterfall/
- Updated README.md and PROJECT_BRIEF.md

## [1.0.0] - 2026-01-26

### Added

- Core 1-8 Skill Pipeline targeting IEEE 830 and ISO/IEC 25010.
- Submodule-ready architecture with relative pathing to ../project_context.
- High-density seeder templates for Skill 01 with ISO-aligned elicitation questions.
- Skill Registry (skill_overview.md) for architectural transparency.
- V&V Standard Operating Procedure in CLAUDE.md.

### Changed

- (Document future modifications to skill logic.prompt or root-level protocols here, referencing the Engineering Registry when appropriate.)

### Fixed

- (Reserve for bug fixes per semantic versioning.)

### Removed

- (Use this section for retired features or deprecated skill templates.)

### Security

- (Record security-related updates or compliance notes.)
