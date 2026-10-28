"""
Tests for Creator Core Engine content linter.
"""

from lint_content import lint_text

def test_clean_text_passes():
    text = (
        "Заметил странный раскол в том, как люди пробуют наладить жизнь.\n\n"
        "С одной стороны, культ достигаторства: вставай в 5 утра, терпи, ломай себя.\n\n"
        "С другой стороны, эзотерика: подыши, и все решится само.\n\n"
        "Но ответ обычно лежит посередине: в трезвом понимании устройства своей нервной системы."
    )
    errors = lint_text(text, is_first_post=True, max_len=500)
    assert len(errors) == 0, f"Expected clean text to pass, got: {errors}"

def test_catches_em_dash():
    text = "Это простая истина — но мало кто её понимает."
    errors = lint_text(text)
    assert any("Em-dash" in err for err in errors)

def test_catches_slop_buzzwords():
    text = "Знакомо состояние, когда план на миллион превращается в прах? Тред о том 👇"
    errors = lint_text(text)
    assert any("Знакомо состояние" in err for err in errors)
    assert any("план на миллион" in err for err in errors)
    assert any("Тред о том" in err for err in errors)
    assert any("Down-arrow" in err for err in errors)

def test_catches_cold_start_transactional_cta():
    text = "Привет всем! Напишите дату рождения в комментариях, я посчитаю вам профиль."
    errors = lint_text(text, is_first_post=True)
    assert any("Lead-magnet CTA" in err for err in errors)
    assert any("Direct calculation offer" in err for err in errors)

def test_catches_overlong_blocks():
    long_text = "слово " * 120  # ~720 chars
    errors = lint_text(long_text, max_len=500)
    assert any("exceeds length limit" in err for err in errors)

def test_multi_block_thread_support():
    thread_text = (
        "Первый пост ветки без лишних слов.\n---\n"
        "Второй пост ветки с нормальным продолжением мысли."
    )
    errors = lint_text(thread_text, max_len=500)
    assert len(errors) == 0

if __name__ == "__main__":
    test_clean_text_passes()
    test_catches_em_dash()
    test_catches_slop_buzzwords()
    test_catches_cold_start_transactional_cta()
    test_catches_overlong_blocks()
    test_multi_block_thread_support()
    print("ALL TESTS PASSED SUCCESSFULLY!")
