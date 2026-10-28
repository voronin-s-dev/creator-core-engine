#!/usr/bin/env python3
"""
Creator Core Engine — Content Anti-Slop and Policy Linter.
Enforces authentic human syntax, strips AI tells (em-dashes, clickbait markers,
formulaic contrasts), and checks platform character constraints.

Exit code 0: Passed.
Exit code 1: Violations found.
"""

import sys
import re
import argparse
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Explicit AI tells and synthetic patterns
DEFAULT_FORBIDDEN_PATTERNS = [
    (r"—", "Em-dash (—): classic AI rhythm marker. Use hyphen (-) with spaces or rephrase without dashes."),
    (r"👇", "Down-arrow (👇): clickbait AI marker."),
    (r"знакомо\s+(состояние|чувство)", "Rhetorical opener 'Знакомо состояние/чувство'."),
    (r"тред о том", "Formulaic announcement 'Тред о том, почему...'."),
    (r"квантов(ый|ая|ое|ые)", "Pseudo-scientific jargon: 'квантовый'."),
    (r"сервер\s+ibm", "Artificial tech metaphor 'сервер IBM'."),
    (r"план на миллион", "Hustle-culture cliché 'план на миллион'."),
    (r"сверхмощн(ый|ая|ое)", "Pompous AI adjective 'сверхмощный'."),
    (r"инструкция по эксплуатации (вашего )?(тела|психики)", "Cliche 'инструкция по эксплуатации тела'."),
    (r"чистая (математика|физика),?\s+а не", "Formulaic contrast 'чистая математика/физика, а не X'."),
    (r"включают режим самобичевания", "Bureaucratic formula 'включают режим самобичевания'."),
    (r"it's not just x, it's y", "Synthetic reveal pattern 'it's not just X, it's Y'."),
    (r"game-?changer", "Corporate buzzword 'game-changer'."),
    (r"dive deep", "AI cliché 'dive deep'."),
    (r"unlock (your )?potential", "Generic marketing cliché 'unlock potential'."),
]

COLD_START_PATTERNS = [
    (r"напишите (свою )?дату (рождения)?", "Lead-magnet CTA forbidden in manifesto/cold-start posts."),
    (r"посчитаю (вам|твой|ваш|профиль|батарейку)", "Direct calculation offer forbidden in introductory posts."),
    (r"черкните дату", "Data collection prompt forbidden in cold-start posts."),
    (r"link in bio", "Hard sales push forbidden in brand-building cold posts."),
    (r"ссылка в шапке", "Hard sales push forbidden in brand-building cold posts."),
]

def lint_text(
    text: str,
    is_first_post: bool = False,
    max_len: int = 500,
    custom_forbidden: list = None
) -> list[str]:
    """
    Audits content string against anti-slop rules and character limits.
    Returns a list of human-readable error descriptions.
    """
    errors = []
    
    # Split text into multi-post thread blocks if delimiter is present
    blocks = re.split(r"\n\s*---\s*\n|\n\s*(?:Пост\s*\d+|\d+\.)\s*\n", text)
    for i, block in enumerate(blocks, 1):
        clean_block = block.strip()
        if not clean_block:
            continue
        if len(clean_block) > max_len:
            errors.append(f"Block #{i} exceeds length limit ({len(clean_block)} > {max_len} chars).")

    # Audit against forbidden patterns
    patterns = DEFAULT_FORBIDDEN_PATTERNS + (custom_forbidden or [])
    for pattern, reason in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            errors.append(f"[Anti-Slop] Found: '{matches[0]}'. Reason: {reason}")

    # Audit cold-start positioning
    if is_first_post:
        for pattern, reason in COLD_START_PATTERNS:
            matches = re.findall(pattern, text, flags=re.IGNORECASE)
            if matches:
                errors.append(f"[Positioning] Found: '{matches[0]}'. Reason: {reason}")

    return errors

def main():
    parser = argparse.ArgumentParser(description="Creator Core Anti-Slop Linter")
    parser.add_argument("file", nargs="?", help="Path to text or markdown file")
    parser.add_argument("--text", help="Raw string to lint")
    parser.add_argument("--first-post", action="store_true", help="Enforce Cold Start rules (no transactional CTAs)")
    parser.add_argument("--max-len", type=int, default=500, help="Max length per block (default 500 for Threads)")
    
    args = parser.parse_args()
    
    content = ""
    if args.text:
        content = args.text
    elif args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"Error: File '{args.file}' not found.")
            sys.exit(2)
        content = p.read_text(encoding="utf-8")
    else:
        content = sys.stdin.read()
        
    if not content.strip():
        print("Error: Empty content.")
        sys.exit(2)
        
    errors = lint_text(content, is_first_post=args.first_post, max_len=args.max_len)
    
    if errors:
        print(f"FAILED: {len(errors)} violation(s) detected:")
        for err in errors:
            print(f"  * {err}")
        sys.exit(1)
    else:
        print("PASSED: Content is clean, human, and compliant.")
        sys.exit(0)

if __name__ == "__main__":
    main()
