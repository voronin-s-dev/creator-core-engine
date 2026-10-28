---
name: creator-core
description: Master orchestrator for the Creator Core Engine framework. Coordinates identity extraction, domain compendium creation, combinatorial synthesis of content ideas, and automated anti-slop linting. Use when onboarding a new creator, setting up a content engine, or orchestrating social content pipelines.
---

# Creator Core Engine — Master Orchestrator

This skill coordinates the full lifecycle of building a high-authority, anti-slop content engine for any creator or expert.

## Workflow Pipeline

```
1. Extraction   ──>   2. Taxonomy   ──>   3. Synthesis   ──>   4. Audit & Linter
identity-extractor    compendium-builder  content-synthesizer  antislop-linter
```

## Step-by-Step Execution

1. **Verify or Extract Identity:**
   * Check if `IDENTITY_CORE.md` exists in the project workspace.
   * If missing, invoke or route to `identity-extractor` to conduct the 15-minute diagnostic interview with the user.

2. **Verify or Build Compendium:**
   * Check if `DOMAIN_COMPENDIUM.md` exists.
   * If missing, invoke or route to `compendium-builder` to curate the 4 knowledge layers for the author's niche.

3. **Synthesize Content:**
   * Use `content-synthesizer` to intersect `IDENTITY_CORE.md` with `DOMAIN_COMPENDIUM.md`.
   * Generate angles that attack common industry delusions using grounded mental models.

4. **Enforce Mechanical Anti-Slop Audit:**
   * Run all drafts through `tools/lint_content.py`.
   * Strip em-dashes (`—`), down-arrows, formulaic contrasts, and transactional CTAs.
   * Verify character limits (e.g. 500 chars for Threads).
