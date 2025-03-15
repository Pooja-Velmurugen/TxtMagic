# test_color_functions.py

import pytest
from TextMagic.colorify import (
    color_text,
    rgb_colorify,
    background_colorify,
    rainbow_text,
    log_message,
)


def test_color_text_basic():
    result = color_text("Hello, World!", "red")
    expected = "\033[31mHello, World!\033[0m"
    assert result == expected

def test_color_text_unknown_color():
    result = color_text("Hello, World!", "unknown")
    expected = "\033[0mHello, World!\033[0m"
    assert result == expected


def test_rgb_colorify_basic():
    result = rgb_colorify("Hello, World!", 255, 0, 0)  # Red
    expected = "\033[38;2;255;0;0mHello, World!\033[0m"
    assert result == expected

def test_rgb_colorify_edge_cases():
    result = rgb_colorify("Hello, World!", 0, 255, 0)  # Green
    expected = "\033[38;2;0;255;0mHello, World!\033[0m"
    assert result == expected

def test_background_colorify_basic():
    result = background_colorify("Hello, World!", 0, 0, 255)  # Blue background
    expected = "\033[48;2;0;0;255mHello, World!\033[0m"
    assert result == expected

def test_background_colorify_edge_cases():
    result = background_colorify("Hello, World!", 255, 255, 0)  # Yellow background
    expected = "\033[48;2;255;255;0mHello, World!\033[0m"
    assert result == expected

def test_rainbow_text_basic():
    result = rainbow_text("Hello")
    expected = (
        "\033[38;2;255;0;0mH"  # Red
        "\033[38;2;255;165;0me"  # Orange
        "\033[38;2;255;255;0ml"  # Yellow
        "\033[38;2;0;255;0ml"  # Green
        "\033[38;2;0;0;255mo"  # Blue
        "\033[0m"  # Reset
    )
    assert result == expected

def test_rainbow_text_long_string():
    result = rainbow_text("Hello, World!")
    assert result.startswith("\033[38;2;255;0;0mH")  # Starts with red
    assert result.endswith("\033[0m")  # Ends with reset


def test_log_message_info():
    result = log_message("This is an info message", "info")
    expected = "\033[94m[INFO] This is an info message\033[0m"
    assert result == expected

def test_log_message_success():
    result = log_message("This is a success message", "success")
    expected = "\033[92m[SUCCESS] This is a success message\033[0m"
    assert result == expected

def test_log_message_warning():
    result = log_message("This is a warning message", "warning")
    expected = "\033[93m[WARNING] This is a warning message\033[0m"
    assert result == expected

def test_log_message_error():
    result = log_message("This is an error message", "error")
    expected = "\033[91m[ERROR] This is an error message\033[0m"
    assert result == expected

def test_log_message_unknown_level():
    result = log_message("This is a message", "unknown")
    expected = "\033[0m[UNKNOWN] This is a message\033[0m"
    assert result == expected