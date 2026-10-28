# CLAUDE.md — Claude Code Instructions

Refer to [AGENTS.md](AGENTS.md) for primary multi-agent directives and constraints.

## Fast Commands
* Run linter: `python tools/lint_content.py <file>`
* Run unit tests: `python tools/test_linter.py`

## Guidelines
1. Always enforce `tools/lint_content.py` before presenting social copy.
2. Never use em-dashes (`—`) in social copy.
3. Keep single posts under 500 characters.
4. Anchor every post angle in `DOMAIN_COMPENDIUM.md`.
