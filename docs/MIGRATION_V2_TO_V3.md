# Migration Guide: v2.x → v3.0

This guide helps existing **SRS-Skills v2.x** users migrate to **SDLC-Docs-Engine v3.0**.

---

## TL;DR (Quick Migration)

**If you're using the Waterfall SRS pipeline:**

1. Update submodule: `git submodule update --remote skills`
2. Update skill paths: `01-initialize-srs` → `02-requirements-engineering/waterfall/01-initialize-srs`
3. (Optional) Run `00-meta-initialization` to formalize methodology
4. Continue using the same workflow with new paths

**Everything still works.** Paths changed, but functionality is identical.

---

## What Changed in v3.0?

### Project Renamed

- **v2.x:** SRS-Skills (SRS-only focus)
- **v3.0:** SDLC-Docs-Engine (comprehensive SDLC documentation)

### Directory Restructure

**v2.x Structure:**
```
srs-skills/
├── 01-initialize-srs/
├── 02-context-engineering/
├── 03-descriptive-modeling/
├── 04-interface-specification/
├── 05-feature-decomposition/
├── 06-logic-modeling/
├── 07-attribute-mapping/
├── 08-semantic-auditing/
└── skills/
```

**v3.0 Structure:**
```
sdlc-docs-engine/
├── 00-meta-initialization/          # NEW
├── 01-strategic-vision/             # NEW
├── 02-requirements-engineering/
│   ├── waterfall/                   # MOVED HERE (v2.x phases 01-08)
│   │   ├── 01-initialize-srs/
│   │   ├── 02-context-engineering/
│   │   ├── 03-descriptive-modeling/
│   │   ├── 04-interface-specification/
│   │   ├── 05-feature-decomposition/
│   │   ├── 06-logic-modeling/
│   │   ├── 07-attribute-mapping/
│   │   └── 08-semantic-auditing/
│   └── agile/                       # NEW
├── 03-design-documentation/         # NEW
├── 04-development-artifacts/        # NEW
├── 05-testing-documentation/        # NEW
├── 06-deployment-operations/        # NEW
├── 07-agile-artifacts/              # NEW
├── 08-end-user-documentation/       # NEW
├── 09-governance-compliance/        # NEW
└── skills/                          # EXISTING
```

### New Features

- ✅ **Methodology Selection** (Phase 00): Waterfall vs. Agile vs. Hybrid
- ✅ **Agile Support**: User stories, story mapping, backlog management
- ✅ **Multi-Phase Support**: 10 SDLC phases (00-09)
- ✅ **23 Document Types**: Beyond SRS (HLD, LLD, API specs, test plans, etc.)

---

## Migration Steps

### Step 1: Update Submodule

```bash
# Navigate to your project root
cd /path/to/your/project

# Update the submodule to latest v3.0
cd skills
git fetch origin
git checkout main
git pull origin main
cd ..

# Commit submodule update
git add skills
git commit -m "chore: Update skills submodule to v3.0 (SDLC-Docs-Engine)"
```

### Step 2: Update Skill Paths in Documentation/Scripts

If you have any scripts or documentation referencing skills, update paths:

**Before (v2.x):**
```bash
# Old paths
Run skill: 01-initialize-srs
Run skill: 02-context-engineering
Run skill: 03-descriptive-modeling
Run skill: 04-interface-specification
Run skill: 05-feature-decomposition
Run skill: 06-logic-modeling
Run skill: 07-attribute-mapping
Run skill: 08-semantic-auditing
```

**After (v3.0):**
```bash
# New paths (all under 02-requirements-engineering/waterfall/)
Run skill: 02-requirements-engineering/waterfall/01-initialize-srs
Run skill: 02-requirements-engineering/waterfall/02-context-engineering
Run skill: 02-requirements-engineering/waterfall/03-descriptive-modeling
Run skill: 02-requirements-engineering/waterfall/04-interface-specification
Run skill: 02-requirements-engineering/waterfall/05-feature-decomposition
Run skill: 02-requirements-engineering/waterfall/06-logic-modeling
Run skill: 02-requirements-engineering/waterfall/07-attribute-mapping
Run skill: 02-requirements-engineering/waterfall/08-semantic-auditing
```

### Step 3: (Optional) Formalize Methodology

While not required, it's recommended to run the new meta-initialization skill:

```bash
Run skill: 00-meta-initialization
```

This will:
- Create `../project_context/methodology.md` documenting your Waterfall choice
- Generate `../project_context/doc_roadmap.md` with your documentation plan
- Formalize your approach for future team members

When prompted:
- Select `[1] Waterfall` (since you're already using the Waterfall SRS pipeline)
- Confirm selection

### Step 4: Continue Normal Workflow

Your existing workflow remains identical, just with updated paths.

**Example workflow:**

```bash
# v2.x workflow
Run: 01-initialize-srs
Edit: ../project_context/*.md files
Run: 02-context-engineering
Run: 03-descriptive-modeling
# ... continue through 08

# v3.0 workflow (functionally identical)
Run: 02-requirements-engineering/waterfall/01-initialize-srs
Edit: ../project_context/*.md files
Run: 02-requirements-engineering/waterfall/02-context-engineering
Run: 02-requirements-engineering/waterfall/03-descriptive-modeling
# ... continue through 08
```

---

## Compatibility Matrix

| v2.x Skill Path | v3.0 Skill Path | Status | Notes |
|-----------------|-----------------|--------|-------|
| `01-initialize-srs` | `02-requirements-engineering/waterfall/01-initialize-srs` | ✅ Identical | Same logic, new location |
| `02-context-engineering` | `02-requirements-engineering/waterfall/02-context-engineering` | ✅ Identical | Same logic, new location |
| `03-descriptive-modeling` | `02-requirements-engineering/waterfall/03-descriptive-modeling` | ✅ Identical | Same logic, new location |
| `04-interface-specification` | `02-requirements-engineering/waterfall/04-interface-specification` | ✅ Identical | Same logic, new location |
| `05-feature-decomposition` | `02-requirements-engineering/waterfall/05-feature-decomposition` | ✅ Identical | Same logic, new location |
| `06-logic-modeling` | `02-requirements-engineering/waterfall/06-logic-modeling` | ✅ Identical | Same logic, new location |
| `07-attribute-mapping` | `02-requirements-engineering/waterfall/07-attribute-mapping` | ✅ Identical | Same logic, new location |
| `08-semantic-auditing` | `02-requirements-engineering/waterfall/08-semantic-auditing` | ✅ Identical | Same logic, new location |

**All v2.x skills work identically in v3.0.** Only paths changed.

---

## Breaking Changes

### ⚠️ Path Changes (Non-Breaking if Using Skill Names)

If you referenced skills by **directory path** in scripts:

**Before:**
```python
skill_path = "skills/01-initialize-srs/"
```

**After:**
```python
skill_path = "skills/02-requirements-engineering/waterfall/01-initialize-srs/"
```

If you referenced skills by **skill name** (recommended):

```python
skill_name = "initialize-srs"  # Still works
```

### ⚠️ Repository Name Change (Non-Breaking)

GitHub repository URL remains the same:
```bash
https://github.com/peterbamuhigire/srs-skills.git
```

The repository is now called **SDLC-Docs-Engine** internally, but the GitHub slug remains `srs-skills` for backward compatibility.

---

## New Capabilities You Can Use

After migrating to v3.0, you can optionally leverage new features:

### 1. Methodology Detection (Phase 00)

```bash
Run skill: 00-meta-initialization
```

Analyzes your project and recommends Waterfall/Agile/Hybrid based on:
- Regulatory keywords (FDA, HIPAA)
- Project type (startup, enterprise)
- Development pace (commit frequency)

### 2. Agile Requirements (Phase 02 - Agile Track)

If your project has agile components (e.g., frontend with rapid iteration):

```bash
Run skill: 02-requirements-engineering/agile/01-user-story-generation
```

Generates INVEST-compliant user stories from `features.md`.

### 3. Design Documentation (Phase 03)

Generate High-Level Design documents:

```bash
Run skill: 03-design-documentation/01-high-level-design
```

Input: Your SRS (`../output/SRS_Draft.md`)
Output: HLD with C4 diagrams (`../output/HLD.md`)

### 4. Testing Documentation (Phase 05)

Generate test plans from requirements:

```bash
Run skill: 05-testing-documentation/02-test-plans
```

Input: SRS requirements
Output: IEEE 829-compliant test plans

### 5. Governance Expansion (Phase 09)

New compliance documentation:

```bash
Run skill: 09-governance-compliance/03-compliance-docs
```

Generates GDPR, HIPAA, or SOC2 compliance documentation.

---

## Rollback (If Needed)

If you need to revert to v2.x:

```bash
cd skills
git checkout v2.9.0  # (or your last v2.x version)
cd ..
git add skills
git commit -m "chore: Rollback to v2.x temporarily"
```

**Note:** v2.x is no longer maintained. v3.0 is fully backward compatible, so rollback shouldn't be necessary.

---

## FAQ

### Q: Do I need to regenerate my existing SRS?

**A:** No. Existing SRS documents generated with v2.x remain valid. Only regenerate if you want to leverage new features (e.g., HLD from SRS).

### Q: Will my existing context files work?

**A:** Yes. All files in `../project_context/` (vision.md, features.md, etc.) work identically in v3.0.

### Q: What if I have custom modifications to v2.x skills?

**A:** Custom modifications in your project's copy of the skills will be preserved. When updating the submodule, you can:
1. Keep your customized local copy (don't update submodule)
2. Update submodule and reapply customizations
3. Contribute customizations back to main repo via PR

### Q: Can I use both Waterfall and Agile in the same project?

**A:** Yes! This is the **Hybrid approach**:
- Use `02-requirements-engineering/waterfall/` for regulated components
- Use `02-requirements-engineering/agile/` for rapidly evolving components
- Generate unified design docs with `03-design-documentation/01-high-level-design`

### Q: Do I have to use Phase 00 (meta-initialization)?

**A:** No, it's optional. Phase 00 is helpful for:
- New projects (select methodology upfront)
- Team onboarding (document methodology choice)
- Methodology changes (switch from Waterfall to Agile)

If you're already using Waterfall SRS successfully, you can skip Phase 00.

### Q: Are there any performance changes?

**A:** No. All skills execute identically to v2.x. The only difference is directory organization.

### Q: What about the `skills/` directory (domain skills)?

**A:** The `skills/` directory (multi-tenant, security, GIS, etc.) is unchanged and fully compatible with v3.0.

---

## Support

If you encounter issues during migration:

1. **Check the README:** https://github.com/peterbamuhigire/srs-skills/blob/main/README.md
2. **Review CHANGELOG:** `docs/CHANGELOG.md` for detailed changes
3. **Open an issue:** https://github.com/peterbamuhigire/srs-skills/issues
4. **Discussion forum:** https://github.com/peterbamuhigire/srs-skills/discussions

---

## Summary

### ✅ What Stayed the Same

- All Waterfall SRS skills (01-08) work identically
- Input files (`../project_context/*.md`) unchanged
- Output files (`../output/SRS_Draft.md`, etc.) unchanged
- IEEE 830/1233/1012 compliance unchanged
- Verification & Validation procedures unchanged

### ✨ What's New

- **Phase 00:** Methodology detection and selection
- **Agile Support:** User story generation, story mapping, backlog management
- **Expanded Scope:** 10 SDLC phases, 23 document types
- **Better Organization:** Clear separation of Waterfall vs. Agile tracks
- **Hybrid Support:** Mix methodologies in the same project

### 📝 What You Need to Do

1. Update submodule: `git submodule update --remote skills`
2. Update skill paths: Add `02-requirements-engineering/waterfall/` prefix
3. (Optional) Run `00-meta-initialization` to formalize methodology
4. Continue using the same workflow

**Migration time: <30 minutes for most projects**

---

**Welcome to SDLC-Docs-Engine v3.0!**

**Version:** 3.0.0
**Last Updated:** 2026-02-07
**Maintained by:** Peter Bamuhigire
