"""
helpers.py — Console Display Helpers
======================================
This module provides utility functions for formatting console output.
Keeping display logic here ensures a consistent look-and-feel across
all menus and reports, and prevents code duplication.

Design Decision:
    We use simple print-based formatting rather than a TUI library
    (like curses) because the project targets learning Core Python.
    The helpers still produce a polished, aligned console experience.
"""

import os

from config import APP_NAME, APP_VERSION, TABLE_WIDTH


def clear_screen():
    """
    Clear the terminal screen.

    Uses 'cls' on Windows and 'clear' on Unix/macOS.
    Falls back to printing blank lines if the OS command fails.
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        # Fallback: print enough blank lines to push content off screen
        print("\n" * 50)


def pause():
    """
    Pause execution until the user presses Enter.

    Used after displaying results so the user can read them before
    the menu redraws.
    """
    input("\n  Press Enter to continue...")


def print_header(title=None):
    """
    Print a styled application header.

    Args:
        title (str, optional): Sub-title to display below the app name.
    """
    print()
    print("╔" + "═" * (TABLE_WIDTH - 2) + "╗")
    print("║" + f" {APP_NAME} v{APP_VERSION} ".center(TABLE_WIDTH - 2) + "║")
    if title:
        print("║" + f" {title} ".center(TABLE_WIDTH - 2) + "║")
    print("╚" + "═" * (TABLE_WIDTH - 2) + "╝")
    print()


def print_separator(char="─", width=None):
    """
    Print a horizontal separator line.

    Args:
        char (str): The character to repeat.
        width (int, optional): Width of the line. Defaults to TABLE_WIDTH.
    """
    width = width or TABLE_WIDTH
    print("  " + char * (width - 4))


def print_menu_title(title):
    """
    Print a formatted menu section title.

    Args:
        title (str): The menu title text.
    """
    print()
    print_separator("═")
    print(f"  ◆ {title}")
    print_separator("═")
    print()


def print_menu_option(number, text):
    """
    Print a single menu option with consistent formatting.

    Args:
        number (int or str): The option number.
        text (str): Description of the option.
    """
    print(f"    [{number}] {text}")


def print_success(message):
    """
    Print a success message with a checkmark icon.

    Args:
        message (str): The success message.
    """
    print(f"\n  ✅ {message}")


def print_error(message):
    """
    Print an error message with a cross icon.

    Args:
        message (str): The error message.
    """
    print(f"\n  ❌ {message}")


def print_warning(message):
    """
    Print a warning message with a warning icon.

    Args:
        message (str): The warning message.
    """
    print(f"\n  ⚠️  {message}")


def print_info(message):
    """
    Print an informational message with an info icon.

    Args:
        message (str): The informational message.
    """
    print(f"\n  ℹ️  {message}")


def print_table_header(columns, widths):
    """
    Print a formatted table header row.

    Args:
        columns (list[str]): Column header names.
        widths (list[int]): Width for each column.
    """
    print_separator("─")
    row = "  "
    for col, width in zip(columns, widths):
        row += f"{col:<{width}}"
    print(row)
    print_separator("─")


def print_table_row(values, widths):
    """
    Print a formatted table data row.

    Args:
        values (list): Data values for each column.
        widths (list[int]): Width for each column.
    """
    row = "  "
    for val, width in zip(values, widths):
        row += f"{str(val):<{width}}"
    print(row)


def get_input(prompt):
    """
    Get user input with a styled prompt.

    Args:
        prompt (str): The prompt message.

    Returns:
        str: The user's input (stripped of leading/trailing whitespace).
    """
    return input(f"\n  ▶ {prompt}: ").strip()


def confirm_action(message):
    """
    Ask the user to confirm an action (yes/no).

    Args:
        message (str): Description of the action to confirm.

    Returns:
        bool: True if the user confirms, False otherwise.
    """
    response = input(f"\n  ⚠️  {message} (y/n): ").strip().lower()
    return response in ('y', 'yes')
