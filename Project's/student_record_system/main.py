"""
main.py — Application Entry Point
====================================
This is the entry point of the Student Record Management System.

It performs the following on startup:
    1. Sets up the Python path so that imports work correctly
    2. Initializes the MenuHandler (which loads data from file)
    3. Starts the interactive menu loop
    4. Handles top-level exceptions for graceful shutdown

Usage:
    $ cd student_record_system
    $ python main.py

Design Decision:
    The main module is intentionally thin — it only bootstraps the
    application. All logic lives in the menu, services, and model layers.
"""

import sys
import os

# ─────────────────────────────────────────────────────────────────────────────
# Path Setup
# ─────────────────────────────────────────────────────────────────────────────
# Add the student_record_system directory to Python's module search path.
# This allows imports like "from models.student import Student" to work
# regardless of the directory the user runs the script from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import MenuHandler
from utils.helpers import clear_screen, print_header, print_error, print_info


def main():
    """
    Main function — entry point of the application.

    Creates the MenuHandler and starts the interactive loop.
    Catches all unhandled exceptions to ensure a graceful exit.
    """
    try:
        # Initialize and start the menu system
        menu = MenuHandler()
        menu.run()

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n")
        print_info("Application interrupted. Exiting gracefully...")
        print_info("All data has been saved. Goodbye!")
        sys.exit(0)

    except Exception as e:
        # Catch any truly unexpected errors
        print_error(f"Fatal error: {e}")
        print_info("The application encountered an unexpected error.")
        print_info("Your data should be safe in data/students.json.")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# Script Guard
# ─────────────────────────────────────────────────────────────────────────────
# This ensures main() only runs when the file is executed directly
# (not when imported as a module).
if __name__ == "__main__":
    main()
