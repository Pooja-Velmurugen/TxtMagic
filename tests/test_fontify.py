# test_fontify.py

import pytest
from TxtMagic.fontify import font_text  # Import the function to test

# Test cases for font_text
def test_font_text_bold():
    # Test with "bold" style
    result = font_text("Hello, World!", style="bold")
    expected = "𝗛𝗲𝗹𝗹𝗼, 𝗪𝗼𝗿𝗹𝗱!"
    assert result == expected

def test_font_text_italic():
    # Test with "italic" style
    result = font_text("Hello, World!", style="italic")
    expected = "𝘏𝘦𝘭𝘭𝘰, 𝘞𝘰𝘳𝘭𝘥!"
    assert result == expected

def test_font_text_cursive():
    # Test with "cursive" style
    result = font_text("Hello, World!", style="cursive")
    expected = "𝓗𝓮𝓵𝓵𝓸, 𝓦𝓸𝓻𝓵𝓭!"
    assert result == expected

def test_font_text_script():
    # Test with "script" style
    result = font_text("Hello, World!", style="script")
    expected = "ℋℯ𝓁𝓁ℴ, 𝒲ℴ𝓇𝓁𝒹!"
    assert result == expected

def test_font_text_fraktur():
    # Test with "fraktur" style
    result = font_text("Hello, World!", style="fraktur")
    expected = "ℌ𝔢𝔩𝔩𝔬, 𝔚𝔬𝔯𝔩𝔡!"
    assert result == expected

def test_font_text_monospace():
    # Test with "monospace" style
    result = font_text("Hello, World!", style="monospace")
    expected = "𝙷𝚎𝚕𝚕𝚘, 𝚆𝚘𝚛𝚕𝚍!"
    assert result == expected

def test_font_text_double_struck():
    # Test with "double_struck" style
    result = font_text("Hello, World!", style="double_struck")
    expected = "ℍ𝕖𝕝𝕝𝕠, 𝕎𝕠𝕣𝕝𝕕!"
    assert result == expected

def test_font_text_small_caps():
    # Test with "small_caps" style
    result = font_text("Hello, World!", style="small_caps")
    expected = "Hᴇʟʟᴏ, Wᴏʀʟᴅ!"
    assert result == expected

def test_font_text_circled():
    # Test with "circled" style
    result = font_text("Hello, World!", style="circled")
    expected = "Ⓗⓔⓛⓛⓞ, Ⓦⓞⓡⓛⓓ!"
    assert result == expected

def test_font_text_circled_filled():
    # Test with "circled_filled" style
    result = font_text("Hello, World!", style="circled_filled")
    expected = "🅗🅔🅛🅛🅞, 🅦🅞🅡🅛🅓!"
    assert result == expected

def test_font_text_inverted():
    # Test with "inverted" style
    result = font_text("Hello, World!", style="inverted")
    expected = "Hǝllo, Moɹlp!"
    assert result == expected

def test_font_text_squared():
    # Test with "squared" style
    result = font_text("Hello, World!", style="squared")
    expected = "🄷🄴🄻🄻🄾, 🅆🄾🅁🄻🄳!"
    assert result == expected

def test_font_text_squared_filled():
    # Test with "squared_filled" style
    result = font_text("Hello, World!", style="squared_filled")
    expected = "🅷🅴🅻🅻🅾, 🆆🅾🆁🅻🅳!"
    assert result == expected

def test_font_text_parenthesized():
    # Test with "parenthesized" style
    result = font_text("Hello, World!", style="parenthesized")
    expected = "⒣⒠⒧⒧⒪, ⒲⒪⒭⒧⒟!"
    assert result == expected

def test_font_text_fullwidth():
    # Test with "fullwidth" style
    result = font_text("Hello, World!", style="fullwidth")
    expected = "Ｈｅｌｌｏ, Ｗｏｒｌｄ!"
    assert result == expected

def test_font_text_superscript():
    # Test with "superscript" style
    result = font_text("Hello, World!", style="superscript")
    expected = "ᴴᵉˡˡᵒ, ᵂᵒʳˡᵈ!"
    assert result == expected

def test_font_text_subscript():
    # Test with "subscript" style
    result = font_text("Hello, World!", style="subscript")
    expected = "ₕₑₗₗₒ, 𝓌ₒᵣₗ𝒹!"
    assert result == expected

def test_font_text_strikethrough():
    # Test with "strikethrough" style
    result = font_text("Hello, World!", style="strikethrough")
    expected = "H̶e̶l̶l̶o̶, W̶o̶r̶l̶d̶!"
    assert result == expected

def test_font_text_underline():
    # Test with "underline" style
    result = font_text("Hello, World!", style="underline")
    expected = "H̲e̲l̲l̲o̲, W̲o̲r̲l̲d̲!"
    assert result == expected

def test_font_text_unknown_style():
    # Test with an unknown style (should default to original text)
    result = font_text("Hello, World!", style="unknown")
    expected = "Hello, World!"
    assert result == expected

def test_font_text_empty_input():
    # Test with empty input
    result = font_text("", style="bold")
    expected = ""
    assert result == expected