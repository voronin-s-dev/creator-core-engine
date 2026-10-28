---
name: creator-core
description: Master orchestrator for the Creator Core Engine framework. Coordinates identity extraction, domain compendium creation, combinatorial idea synthesis, format production (Reels, Carousels, Threads, Motion), and automated anti-slop linting. Use when onboarding a new creator, setting up a content engine, or orchestrating social content pipelines.
---

# Creator Core Engine — Master Orchestrator

This skill coordinates the full lifecycle of building and running a high-authority, anti-slop content engine for any creator or expert.

## Full Multi-Agent Pipeline

```
[Phase 1: Knowledge & Strategy]
  ├── identity-extractor   (Extracts biological limits, scars, anti-values)
  ├── compendium-builder   (Structures 4-tier domain knowledge vault)
  └── content-synthesizer  (Collides identity limits with domain models)
           │
           ▼
[Phase 2: Format Production Engine]
  ├── reels-scriptwriter   (30-45s vertical video scripts + teleprompter + 26 hooks)
  ├── carousel-architect   (1080x1350 10-slide high-save carousels)
  ├── threads-creator      (500-char dialogue threads & engagement loops)
  └── motion-producer      (Remotion animation + AI B-roll + Kowalski springs)
           │
           ▼
[Phase 3: Quality & Verification Gate]
  └── antislop-linter      (Automated Python audit: zero em-dashes, zero slop)
```

## Step-by-Step Execution

1. **Verify Strategy & Foundations:**
   * If `IDENTITY_CORE.md` is missing: route to `identity-extractor`.
   * If `DOMAIN_COMPENDIUM.md` is missing: route to `compendium-builder`.
   * Synthesize new angles via `content-synthesizer`.

2. **Select Output Format:**
   * For short-form video (Reels / Shorts): route to `reels-scriptwriter`.
   * For visual slide progression: route to `carousel-architect`.
   * For text discussions & viral series: route to `threads-creator`.
   * For video animation & motion graphics: route to `motion-producer`.

3. **Mandatory Mechanical Audit:**
   * Run all drafts through `tools/lint_content.py`.
   * Never deliver unlinted content to the user or publishing queues.
