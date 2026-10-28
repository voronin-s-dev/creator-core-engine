# AGENTS.md — Control Plane & Multi-Agent Protocol

This file defines rules for AI coding agents and LLM orchestrators in this repository.

## 1. Operating Rules

1. The repository follows the Creator Core Engine methodology.
2. Agents must not generate content without an active `IDENTITY_CORE.md`.
3. Agents must not brainstorm topics without reference to `DOMAIN_COMPENDIUM.md`.
4. Agents must validate all generated copy using `tools/lint_content.py`.
5. If the linter reports errors, the agent must rewrite the text.
6. Agents must reject em-dashes and formulaic clickbait phrases.
7. Agents must keep single social posts under 500 characters.

## 2. Subagent Responsibilities

* **`creator-core`**: Routes requests and coordinates subagent execution.
* **`identity-extractor`**: Conducts the diagnostic interview to build `IDENTITY_CORE.md`.
* **`compendium-builder`**: Maps niche mental models into `DOMAIN_COMPENDIUM.md`.
* **`content-synthesizer`**: Collides identity limits with domain models to produce post angles.
* **`antislop-linter`**: Audits and strips robotic AI markers from all drafts.

## 3. Strict Verification Gate

Every publication draft must pass automated checks:
```bash
python tools/lint_content.py <target-file> --max-len 500
```
An exit code of `0` is mandatory before showing drafts to the user.
