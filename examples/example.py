
from TxtMagic import color_text, rgb_colorify, rainbow_text, log_message ,emoji_text ,font_text 

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
print(font_text("Hello, World!", style="underline"))   # Output: H̲e̲l̲l̲o̲,̲ ̲W̲o̲r̲l̲d̲!
print()
