"""
config.py — Application Configuration
=======================================
This module stores all application-wide constants and configuration values.
Centralizing configuration ensures consistency across all modules and makes
it easy to change settings (like subjects or pass marks) in one place.

Design Decision:
    We use module-level constants (uppercase by PEP-8 convention) rather than
    a config file because this is a learning project and constants in code
    are easier to understand and debug.
"""

import os

# ─────────────────────────────────────────────────────────────────────────────
# Application Information
# ─────────────────────────────────────────────────────────────────────────────
APP_NAME = "Student Record Management & Marks Analysis System"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Student Performance Analytics Team"

# ─────────────────────────────────────────────────────────────────────────────
# Directory & File Paths
# ─────────────────────────────────────────────────────────────────────────────
# BASE_DIR is the root of the student_record_system package.
# All other paths are derived from it so the app works regardless of
# where it is installed.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "students.json")
BACKUP_FILE = os.path.join(DATA_DIR, "students_backup.json")

# ─────────────────────────────────────────────────────────────────────────────
# Academic Configuration
# ─────────────────────────────────────────────────────────────────────────────
# List of subjects every student is evaluated in.
# Changing this list automatically propagates to validation, analysis,
# and report modules.
SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Computer Science"]

# Number of subjects (derived to avoid magic numbers elsewhere).
NUM_SUBJECTS = len(SUBJECTS)

# ─────────────────────────────────────────────────────────────────────────────
# Marks Constraints
# ─────────────────────────────────────────────────────────────────────────────
MIN_MARKS = 0       # Minimum possible marks in any subject
MAX_MARKS = 100     # Maximum possible marks in any subject
PASS_MARKS = 35     # Minimum marks required to pass a single subject

# ─────────────────────────────────────────────────────────────────────────────
# Grade Thresholds
# ─────────────────────────────────────────────────────────────────────────────
# Stored as a list of (min_average, grade) tuples in descending order.
# The first match determines the grade.
GRADE_THRESHOLDS = [
    (90, "A+"),
    (80, "A"),
    (70, "B+"),
    (60, "B"),
    (50, "C"),
    (35, "D"),
    (0,  "F"),
]

# ─────────────────────────────────────────────────────────────────────────────
# Random Data Generation Defaults
# ─────────────────────────────────────────────────────────────────────────────
DEFAULT_RANDOM_COUNT = 10   # Default number of random students to generate
MAX_RANDOM_COUNT = 1000     # Maximum allowed in a single generation

# ─────────────────────────────────────────────────────────────────────────────
# Display Settings
# ─────────────────────────────────────────────────────────────────────────────
TABLE_WIDTH = 90            # Width of separator lines in console output
