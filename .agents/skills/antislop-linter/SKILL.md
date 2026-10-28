---
name: antislop-linter
description: Quality assurance and anti-slop gatekeeper for AI-generated text. Audits drafts against robotic cadence, em-dashes, formulaic clickbait openers, and platform character limits using tools/lint_content.py. Use before presenting copy or scheduling posts.
---

# Anti-Slop Content Linter Skill

Guarantees that all social media copy sounds authentically human, grounded, and free of AI fingerprints.

## Prohibited Patterns & Checks

1. **Em-Dashes (`—`):**  
   Strictly forbidden in social copy. AI models overuse em-dashes as a stylistic crutch. Replace with hyphens with spaces (` - `) or rephrase.
2. **Formulaic Openers:**  
   Reject: *"Знакомо состояние...?", "Тред о том, почему... 👇", "Let's dive in"*.
3. **Pompous Buzzwords:**  
   Reject: *"квантовый", "сервер IBM", "план на миллион", "game-changer", "чистая математика, а не воля"*.
4. **Premature Transactional CTAs in Cold Posts:**  
   Reject: *"Напишите дату рождения", "Посчитаю вам", "Link in bio"* in manifesto or introductory posts.
5. **Length Limits:**  
   Strictly check 500-character ceiling for Threads single posts.

## Tool Execution

Run the deterministic linter:
```bash
python tools/lint_content.py <file-path> [--first-post] [--max-len 500]
```
If errors are reported (exit code 1), rewrite the text to eliminate violations before presenting to the user.
