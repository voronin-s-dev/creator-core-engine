# AGENTS.md — Control Plane & Multi-Agent Protocol

This file defines rules for AI coding agents and LLM orchestrators in this repository.

## 1. Operating Rules

1. The repository follows the Creator Core Engine methodology.
2. Agents must not generate content without an active `IDENTITY_CORE.md`.
3. Agents must not brainstorm topics without reference to `DOMAIN_COMPENDIUM.md`.
4. Agents must select verified hook formulas from `templates/HOOKS_VAULT_26.md`.
5. Agents must validate all generated copy using `tools/lint_content.py`.
6. If the linter reports errors, the agent must rewrite the text.
7. Agents must reject em-dashes and formulaic clickbait phrases.
8. Agents must keep single social posts under 500 characters.

## 2. Multi-Agent Team Roster

### Phase 1: Strategy & Knowledge
* **`creator-core`**: Routes requests and coordinates subagent execution.
* **`identity-extractor`**: Conducts the diagnostic interview to build `IDENTITY_CORE.md`.
* **`compendium-builder`**: Maps niche mental models into `DOMAIN_COMPENDIUM.md`.
* **`content-synthesizer`**: Collides identity limits with domain models to produce post angles.

### Phase 2: Production Formats
* **`reels-scriptwriter`**: Writes 30-45s vertical video shooting scripts with teleprompter text.
* **`carousel-architect`**: Builds 10-slide 1080x1350 visual carousels for Instagram and LinkedIn.
* **`threads-creator`**: Writes 500-character conversational threads and series for Threads and X.
* **`motion-producer`**: Designs Remotion vector animations with spring physics and video B-roll.

### Phase 3: Quality Gate
* **`antislop-linter`**: Audits and strips robotic AI markers from all drafts before presentation.

## 3. Strict Verification Gate

Every publication draft must pass automated checks:
```bash
python tools/lint_content.py <target-file> --max-len 500
```
An exit code of `0` is mandatory before showing drafts to the user.
