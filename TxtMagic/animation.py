import sys
import time
import random
import shutil
from rich.console import Console
from rich.text import Text

console = Console()

# 1. Typing Animation
def typing_animation(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# 2. Scrolling Text
def scrolling_text(text, duration=1):
    width = shutil.get_terminal_size().columns
    text = " " * width + text + " " * width
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(len(text) - width):
            sys.stdout.write("\r" + text[i:i+width])
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# 3. Wave Effect
def wave_effect(text, duration=5):
    end_time = time.time() + duration
    positions = [0, 1, 2, 3, 2, 1]
    while time.time() < end_time:
        for pos in positions:
            print(" " * pos + text)
            time.sleep(0.2)
            sys.stdout.write("\033[F")

# 4. Glitch Effect
def glitch_effect(text, duration=3):
    chars = list(text)
    end_time = time.time() + duration
    while time.time() < end_time:
        random.shuffle(chars)
        sys.stdout.write("\r" + ''.join(chars))
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r" + text)


# 5. Color Cycling Effect
def color_cycle(text, duration=5):
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in colors:
            console.print(Text(text, style=f"bold {color}"), end="\r")
            time.sleep(0.5)
    print()



# 6. Random Character Shuffle Effect
def random_shuffle(text, duration=3):
    end_time = time.time() + duration
    while time.time() < end_time:
        shuffled = list(text)
        random.shuffle(shuffled)
        sys.stdout.write("\r" + "".join(shuffled))
        sys.stdout.flush()
        time.sleep(0.2)
    print("\r" + text)


# 7. Rainbow Text Effect
def rainbow_text_anime(text, duration=5):
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in colors:
            styled_text = Text(text, style=f"bold {color}")
            console.print(styled_text, end="\r")
            time.sleep(0.5)
    print()



# 8. Text Shadow Effect
def text_shadow(text, duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        console.print(Text(text, style="bold white on black"), end="\r")
        time.sleep(0.5)
        console.print(Text(text, style="bold black on white"), end="\r")
        time.sleep(0.5)
    print()

# 9. Blinking Text Effect
def blinking_text(text, duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        console.print(Text(text, style="bold white"), end="\r")
        time.sleep(0.5)
        console.print(" " * len(text), end="\r")
        time.sleep(0.5)
    print()

# 10. Text Gradient Effect
def text_gradient(text, duration=5):
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in colors:
            gradient_text = Text(text, style=f"bold {color}")
            console.print(gradient_text, end="\r")
            time.sleep(0.5)
    print()



# 11. Text Mirror Effect
def text_mirror(text, duration=5):
    mirrored_text = text + " | " + text[::-1]
    end_time = time.time() + duration
    while time.time() < end_time:
        console.print(Text(mirrored_text, style="bold white"), end="\r")
        time.sleep(0.5)
    print()

# 12. Text Fire Effect
def text_fire(text, duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in ["red", "yellow", "orange"]:
            console.print(Text(text, style=f"bold {color}"), end="\r")
            time.sleep(0.2)
    print()

# 13. Text Neon Effect
def text_neon(text, duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in ["cyan", "magenta", "blue"]:
            console.print(Text(text, style=f"bold {color}"), end="\r")
            time.sleep(0.2)
    print()



# 14. Text Gravity Effect
def text_gravity(text, duration=5):
    height = shutil.get_terminal_size().lines
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(height):
            sys.stdout.write("\n" * i + text)
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# 15. Text Wave Effect
def text_wave(text, duration=5):
    """Creates a wave-like motion for the text."""
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(0, 10):
            sys.stdout.write("\r" + " " * i + text)
            sys.stdout.flush()
            time.sleep(0.1)
        for i in range(10, 0, -1):
            sys.stdout.write("\r" + " " * i + text)
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# 16. Shadow Wave Effect
def shadow_wave(text, duration=5):
    """Combines shadow and wave effects."""
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(0, 10):
            console.print(Text(" " * i + text, style="bold white"), end="\r")
            time.sleep(0.1)
        for i in range(10, 0, -1):
            console.print(Text(" " * i + text, style="bold white"), end="\r")
            time.sleep(0.1)
    print()

# 17. Text 3D Effect
def text_3d(text, duration=5):
    end_time = time.time() + duration
    while time.time() < end_time:
        for color in ["red", "green", "blue"]:
            console.print(Text(text, style=f"bold {color}"), end="\r")
            time.sleep(0.2)
    print()

