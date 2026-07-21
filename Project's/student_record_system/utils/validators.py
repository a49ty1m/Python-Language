"""
validators.py — Input Validation Functions
============================================
This module provides reusable validation functions for all user inputs.
Each function either returns the validated (and possibly type-cast) value
or raises a custom exception with a user-friendly message.

Design Decision:
    Validators are pure functions (no side effects) so they can be easily
    tested and reused across the menu, service, and model layers.
"""

from utils.exceptions import InvalidInputError, InvalidMarksError
from config import MIN_MARKS, MAX_MARKS, NUM_SUBJECTS, SUBJECTS


def validate_student_id(value):
    """
    Validate and return a student ID.

    A valid student ID must be:
        - Convertible to an integer
        - A positive number (> 0)

    Args:
        value: The raw input value (usually a string from user input).

    Returns:
        int: The validated student ID.

    Raises:
        InvalidInputError: If the value is not a positive integer.
    """
    try:
        student_id = int(value)
    except (ValueError, TypeError):
        raise InvalidInputError(
            field="Student ID",
            value=value,
            message=f"Student ID must be a positive integer. Got: '{value}'"
        )

    if student_id <= 0:
        raise InvalidInputError(
            field="Student ID",
            value=value,
            message=f"Student ID must be positive. Got: {student_id}"
        )

    return student_id


def validate_name(name):
    """
    Validate and return a student name.

    A valid name must be:
        - A non-empty string
        - Contain only alphabetic characters and spaces

    Args:
        name (str): The raw name input.

    Returns:
        str: The validated and title-cased name.

    Raises:
        InvalidInputError: If the name is empty or contains non-alpha chars.
    """
    if not isinstance(name, str) or not name.strip():
        raise InvalidInputError(
            field="Name",
            value=name,
            message="Student name cannot be empty."
        )

    # Allow alphabetic characters and spaces only
    cleaned = name.strip()
    if not all(ch.isalpha() or ch.isspace() for ch in cleaned):
        raise InvalidInputError(
            field="Name",
            value=name,
            message="Student name must contain only letters and spaces."
        )

    # Return in title case for consistent display
    return cleaned.title()


def validate_single_mark(value, subject_name="Subject"):
    """
    Validate a single mark value.

    Args:
        value: The raw mark input.
        subject_name (str): Name of the subject (for error messages).

    Returns:
        int: The validated mark.

    Raises:
        InvalidMarksError: If the value is not an integer in [0, 100].
    """
    try:
        mark = int(value)
    except (ValueError, TypeError):
        raise InvalidMarksError(
            marks=value,
            message=f"Mark for {subject_name} must be an integer. Got: '{value}'"
        )

    if mark < MIN_MARKS or mark > MAX_MARKS:
        raise InvalidMarksError(
            marks=mark,
            message=(
                f"Mark for {subject_name} must be between "
                f"{MIN_MARKS} and {MAX_MARKS}. Got: {mark}"
            )
        )

    return mark


def validate_marks(marks_list):
    """
    Validate a complete list of marks for all subjects.

    Args:
        marks_list (list): List of mark values (strings or ints).

    Returns:
        list[int]: List of validated integer marks.

    Raises:
        InvalidMarksError: If the list length doesn't match NUM_SUBJECTS,
                           or if any individual mark is invalid.
    """
    if not isinstance(marks_list, (list, tuple)):
        raise InvalidMarksError(
            marks=marks_list,
            message="Marks must be provided as a list."
        )

    if len(marks_list) != NUM_SUBJECTS:
        raise InvalidMarksError(
            marks=marks_list,
            message=(
                f"Expected {NUM_SUBJECTS} marks (one per subject: "
                f"{', '.join(SUBJECTS)}). Got {len(marks_list)}."
            )
        )

    validated = []
    for i, mark in enumerate(marks_list):
        validated.append(validate_single_mark(mark, SUBJECTS[i]))

    return validated


def validate_menu_choice(value, min_val, max_val):
    """
    Validate a numeric menu choice within a range.

    Args:
        value: The raw input value.
        min_val (int): Minimum valid choice (inclusive).
        max_val (int): Maximum valid choice (inclusive).

    Returns:
        int: The validated menu choice.

    Raises:
        InvalidInputError: If the value is not an integer in [min_val, max_val].
    """
    try:
        choice = int(value)
    except (ValueError, TypeError):
        raise InvalidInputError(
            field="Menu Choice",
            value=value,
            message=f"Please enter a number between {min_val} and {max_val}."
        )

    if choice < min_val or choice > max_val:
        raise InvalidInputError(
            field="Menu Choice",
            value=choice,
            message=f"Choice must be between {min_val} and {max_val}. Got: {choice}"
        )

    return choice


def validate_positive_integer(value, field_name="Value"):
    """
    Validate that a value is a positive integer.

    Useful for count inputs (e.g., number of random students to generate).

    Args:
        value: The raw input value.
        field_name (str): Descriptive name for error messages.

    Returns:
        int: The validated positive integer.

    Raises:
        InvalidInputError: If the value is not a positive integer.
    """
    try:
        num = int(value)
    except (ValueError, TypeError):
        raise InvalidInputError(
            field=field_name,
            value=value,
            message=f"{field_name} must be a positive integer. Got: '{value}'"
        )

    if num <= 0:
        raise InvalidInputError(
            field=field_name,
            value=num,
            message=f"{field_name} must be positive. Got: {num}"
        )

    return num
