def test_user_registration(registration_result):
    """Тест реєстрації користувача. Використовує лише фікстури."""
    assert registration_result is True, "Реєстрація не підтверджена (нема success-тосту/редіректу)"
