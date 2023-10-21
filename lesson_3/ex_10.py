def test_input_phrase():
    phrase = input("Set a phrase: ")
    number = 15

    assert len(phrase) < number, f"Фраза должна быть короче {number} символов"

