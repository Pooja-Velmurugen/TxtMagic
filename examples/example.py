
#from TxtMagic import color_text, rgb_colorify, rainbow_text, background_colorify, log_message ,emoji_text ,font_text 
from TxtMagic import *

# Example 1: Basic Text Coloring
print("=== Example 1: Basic Text Coloring ===")
print(color_text("Hello, World!", "red"))
print(color_text("Hello, World!", "green"))
print(color_text("Hello, World!", "blue"))
print()

# Example 2: Unique RGB Text Coloring
print("=== Example 2: Unique RGB Text Coloring ===")
print(rgb_colorify("Hello, World!", 255, 105, 180))  # Hot Pink
print(rgb_colorify("Hello, World!", 100, 200, 255))  # Sky Blue
print(rgb_colorify("Hello, World!", 255, 165, 0))    # Orange
print(rgb_colorify("Hello, World!", 147, 112, 219))  # Medium Purple
print(rgb_colorify("Hello, World!", 50, 205, 50))    # Lime Green
print(rgb_colorify("Hello, World!", 255, 127, 80))    # Coral
print(rgb_colorify("Hello, World!", 0, 128, 128))     # Teal
print(rgb_colorify("Hello, World!", 230, 230, 250))   # Lavender
print(rgb_colorify("Hello, World!", 255, 215, 0))     # Gold
print(rgb_colorify("Hello, World!", 250, 128, 114))   # Salmon
print(rgb_colorify("Hello, World!", 64, 224, 208))    # Turquoise
print(rgb_colorify("Hello, World!", 255, 0, 255))     # Magenta
print(rgb_colorify("Hello, World!", 128, 128, 0))     # Olive
print(rgb_colorify("Hello, World!", 75, 0, 130))      # Indigo
print(rgb_colorify("Hello, World!", 255, 218, 185))   # Peach
print(rgb_colorify("Hello, World!", 0, 255, 255))     # Cyan
print(rgb_colorify("Hello, World!", 128, 0, 0))       # Maroon
print(rgb_colorify("Hello, World!", 189, 252, 201))   # Mint
print(rgb_colorify("Hello, World!", 224, 17, 95))     # Ruby
print(rgb_colorify("Hello, World!", 106, 90, 205))    # Slate Blue
print()

# Example 3: Rainbow Gradient Text
print("=== Example 3: Rainbow Gradient Text ===")
print(rainbow_text("Hello, World!"))
print()

# Example 4: Log Messages with Colors
print("=== Example 4: Log Messages with Colors ===")
print(log_message("This is an info message.", "info"))
print(log_message("This is a success message.", "success"))
print(log_message("This is a warning message.", "warning"))
print(log_message("This is an error message.", "error"))
print()

# Example 5: Emoji Replacement
print("=== Example 5: Emoji Replacement ===")
print(emoji_text("I love Python"))  # Output: I ❤️🐍
print(emoji_text("Let's have some pizza!"))  # Output: Let's have some 🍕!
print(emoji_text("I feel happy and joyful!"))  # Output: I feel 😊 and 😊!
print()

# Example 6: Font Styling
print("=== Example 6: Font Styling ===")
print(font_text("Hello, World!", style="bold"))        # Output: 𝗛𝗲𝗹𝗹𝗼, 𝗪𝗼𝗿𝗹𝗱!
print(font_text("Hello, World!", style="cursive"))    # Output: 𝓗𝓮𝓵𝓵𝓸, 𝓦𝓸𝓻𝓵𝓭!
print(font_text("Hello, World!", style="superscript")) # Output: ᴴᵉˡˡᵒ, ᵂᵒʳˡᵈ!
print(font_text("Hello, World!", style="strikethrough")) # Output: H̶e̶l̶l̶o̶,̶ ̶W̶o̶r̶l̶d̶!
print(font_text("Hello, World!", style="underline"))# Output: H̲e̲l̲l̲o̲,̲ ̲W̲o̲r̲l̲d̲!
print(font_text("Hello, World!", style="double_struck"))# Output: ℍ𝕖𝕝𝕝𝕠, 𝕎𝕠𝕣𝕝𝕕!
print(font_text("Hello, World!", style="circled"))    # Output: Ⓗⓔⓛⓛⓞ, Ⓦⓞⓡⓛⓓ!
print(font_text("Hello, World!", style="circled_filled"))   # Output: 🅗🅔🅛🅛🅞, 🅦🅞🅡🅛🅓!
print(font_text("Hello, World!", style="inverted"))  # Output: Hǝllo, Moɹlp!
print(font_text("Hello, World!", style="squared"))  # Output: 🄷🄴🄻🄻🄾, 🅆🄾🅁🄻🄳!
print(font_text("Hello, World!", style="squared_filled"))  # Output: 🅷🅴🅻🅻🅾, 🆆🅾🆁🅻🅳!
print()


print("=== Example 7: Combinations Of All  ===")
cursive_text=font_text("Hello, World!", style="cursive")
print(rgb_colorify(cursive_text, 64, 224, 208)) 
print(rgb_colorify(font_text("Hello, World!", style="double_struck"), 250, 128, 114))
print(rgb_colorify(font_text("Hello, World!", style="circled_filled"), 255, 215, 0))
print(rainbow_text(font_text("Hello, World!", style="squared")))
print(rgb_colorify(emoji_text("Let's have some pizza!"), 64, 224, 208 ))
print(font_text(emoji_text("Let's have some pizza!"), style="cursive"))
print()
  
print("=== Example 8: Emoji With Text=== ")
print(add_emojis_With_text("I am very happy today!"))
print(add_emojis_With_text("Lets have some pizza!"))
print()

print("=== Example 9: analyze_sentiment=== ")
print(analyze_sentiment("This is a terrible day"))
print(analyze_sentiment("I feel happy when i sing a songs"))
print(analyze_sentiment("I hate Exams"))
print()


print("=== Example 10: Combining Features ===")

"""
Note : When using colorify, emojify, and fontify features simultaneously, it's important to 
       follow the correct order of operations.
       Apply emojis first to include them in the text, then apply font styles to transform the 
       text, and finally add colors last to ensure the entire text
"""

text = add_emojis_With_text("I love Python and pizza!")
styled_text = font_text(text, style="fraktur")
colored_text = rgb_colorify(styled_text, 189, 252, 201)   # Mint
print(colored_text)
print()


print("=== Example 10:Demo of text animations:=== ")
typing_animation("Hello, welcome to Python animations!")
scrolling_text("Python makes animations fun!")
glitch_effect("Glitchy Text!")
color_cycle("Color Cycling")
random_shuffle("Random Shuffle")
rainbow_text_anime("Rainbow Text")
text_shadow("Text Shadow")
blinking_text("Blinking Text")
text_gradient("Text Gradient")
text_mirror("Text Mirror")
text_fire("Text Fire")
text_neon("Text Neon")
text_wave("Text Wave")
shadow_wave("Shadow Wave")
text_3d("3D Text")
print()
