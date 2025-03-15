import pytest 
from TextMagic.emojify import emoji_text 


def test_emoji_text_basic():
    result = emoji_text("I love Python")
    expected = "I ❤️ 🐍"
    assert result == expected


def test_emoji_text_multiple_keywords():
    result = emoji_text("I feel happy and joyful! Let's go to the party! 🎉")
    expected = "I feel 😊 and 😊! Let's go to the 🍺! 🎉"
    assert result == expected


def test_emoji_text_custom_mappings():
    custom_mappings = {"python": "🐍", "code": "💻"}
    result = emoji_text("I love coding in Python!", custom_mappings)
    expected = "I ❤️ coding in 🐍!"
    assert result == expected


def test_emoji_text_no_matches():
    result = emoji_text("This is a test with no emojis.")
    expected = "This is a test with no emojis."
    assert result == expected


def test_emoji_text_case_sensitivity():
    result = emoji_text("I LOVE PYTHON")
    expected = "I LOVE PYTHON" 
    assert result == expected


def test_emoji_text_empty_input():
    result = emoji_text("")
    expected = ""
    assert result == expected


def test_emoji_text_special_characters():
    result = emoji_text("I love Python! 🐍 #coding")
    expected = "I ❤️ 🐍! 🐍 #coding"
    assert result == expected