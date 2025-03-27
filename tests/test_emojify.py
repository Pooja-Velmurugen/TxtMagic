import pytest 
from TxtMagic.emojify import emoji_text ,analyze_sentiment , add_emojis_With_text


def test_emoji_text_basic():
    result = emoji_text("I love Python")
    expected = "ℹ️  ❤️ 🐍"
    assert result == expected


def test_emoji_text_multiple_keywords():
    result = emoji_text("I feel happy and joyful! Let's go to the party! 🎉")
    expected = "ℹ️  🅵🅴🅴🛴 😊 🅰️ 🅽🅳 😊! 🛴🅴🆃'💲 🅶🅾️ 🆃🅾️ 🆃🅷🅴 🎊! 🎉"
    assert result == expected


def test_emoji_text_custom_mappings():
    custom_mappings = {"python": "🐍", "code": "💻"}
    result = emoji_text("I love coding in Python!", custom_mappings)
    expected = "ℹ️  ❤️ ©️ 🅾️🅳ℹ️ 🅽🅶 ℹ️ 🅽 🐍!"
    assert result == expected



def test_emoji_text_case_sensitivity():
    result = emoji_text("I LOVE PYTHON")
    expected = "ℹ️  ❤️ 🐍" 
    assert result == expected


def test_emoji_text_empty_input():
    result = emoji_text("")
    expected = ""
    assert result == expected


def test_emoji_text_special_characters():
    result = emoji_text("I love Python! 🐍 #coding")
    expected = "ℹ️  ❤️ 🐍! 🐍 #©️ 🅾️🅳ℹ️ 🅽🅶"
    assert result == expected
    

def test_emoji_With_text():
    result = add_emojis_With_text("I am very happy today!")
    expected = "I am very happy 😊 today!"
    assert result == expected   
    
    

def test_emoji_analyze_sentiment():
    result = analyze_sentiment("This is a terrible day")
    expected = "This is a terrible day 😢 😡 💔"
    assert result == expected  
     
    
  