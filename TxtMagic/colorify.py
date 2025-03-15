# ANSI Color Codes for Basic Colors
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    "reset": "\033[0m"
}
def color_text(text, color):
    """
    Apply a basic text color using ANSI escape codes.
    
    :param text: The input text.
    :param color: The color to apply (e.g., "red", "green", "blue").
    :return: The colored text.
    """
    return f"{COLORS.get(color, COLORS['reset'])}{text}{COLORS['reset']}"

def rgb_colorify(text, r, g, b):
    """
    Apply RGB color to text using ANSI escape codes.
    
    :param text: The input text.
    :param r: Red value (0-255).
    :param g: Green value (0-255).
    :param b: Blue value (0-255).
    :return: The colored text.
    """
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def background_colorify(text, r, g, b):
    """
    Apply background color using RGB ANSI codes.
    
    :param text: The input text.
    :param r: Red value (0-255).
    :param g: Green value (0-255).
    :param b: Blue value (0-255).
    :return: The text with a colored background.
    """
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"

def rainbow_text(text):
    """
    Apply a rainbow gradient effect to text.
    
    :param text: The input text.
    :return: The text with a rainbow gradient effect.
    """
    colors = [
        (255, 0, 0),      # Red
        (255, 165, 0),    # Orange
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (75, 0, 130),     # Indigo
        (238, 130, 238)   # Violet
    ]
    
    gradient_text = ""
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        gradient_text += f"\033[38;2;{r};{g};{b}m{char}"
    
    return gradient_text + "\033[0m"

def log_message(message, level="info"):
    """
    Log messages with different colors based on the level.
    
    :param message: The log message.
    :param level: The log level ("info", "success", "warning", "error").
    :return: The colored log message.
    """
    colors = {
        "info": "\033[94m",    # Blue
        "success": "\033[92m", # Green
        "warning": "\033[93m", # Yellow
        "error": "\033[91m"    # Red
    }
    color = colors.get(level, "\033[0m")
    return f"{color}[{level.upper()}] {message}\033[0m"


