"""
exceptions.py — Custom Exception Classes
==========================================
This module defines a hierarchy of custom exceptions for the application.
Using custom exceptions instead of generic ones (like ValueError) provides:

    1. **Specificity** — Callers know exactly what went wrong.
    2. **Clean handling** — Menu code can catch StudentSystemError for all
       app-level errors while still distinguishing sub-types when needed.
    3. **User-friendly messages** — Each exception carries a descriptive
       message suitable for display to the end user.

Exception Hierarchy:
    StudentSystemError (base)
    ├── StudentNotFoundError
    ├── DuplicateStudentError
    ├── InvalidMarksError
    ├── InvalidInputError
    └── FileCorruptedError
"""


class StudentSystemError(Exception):
    """
    Base exception for all application-specific errors.

    All custom exceptions inherit from this class so that a single
    except clause can catch any application error when fine-grained
    handling is not needed.
    """

    def __init__(self, message="An error occurred in the Student System."):
        self.message = message
        super().__init__(self.message)


class StudentNotFoundError(StudentSystemError):
    """
    Raised when a student lookup (by ID or name) yields no results.

    Attributes:
        student_id: The ID that was searched for (if applicable).
    """

    def __init__(self, student_id=None, message=None):
        self.student_id = student_id
        if message is None:
            if student_id is not None:
                message = f"Student with ID {student_id} not found."
            else:
                message = "Student not found."
        super().__init__(message)


class DuplicateStudentError(StudentSystemError):
    """
    Raised when attempting to add a student whose ID already exists.

    Attributes:
        student_id: The duplicate ID.
    """

    def __init__(self, student_id, message=None):
        self.student_id = student_id
        if message is None:
            message = f"Student with ID {student_id} already exists."
        super().__init__(message)


class InvalidMarksError(StudentSystemError):
    """
    Raised when marks are outside the valid range or not numeric.

    Attributes:
        marks: The invalid marks value(s).
    """

    def __init__(self, marks=None, message=None):
        self.marks = marks
        if message is None:
            message = f"Invalid marks: {marks}. Marks must be between 0 and 100."
        super().__init__(message)


class InvalidInputError(StudentSystemError):
    """
    Raised when user input fails validation (e.g., non-numeric menu choice,
    empty name, negative ID).

    Attributes:
        field: The name of the field that failed validation.
        value: The invalid value provided.
    """

    def __init__(self, field=None, value=None, message=None):
        self.field = field
        self.value = value
        if message is None:
            message = f"Invalid input for '{field}': {value}"
        super().__init__(message)


class FileCorruptedError(StudentSystemError):
    """
    Raised when the data file exists but cannot be parsed (e.g., invalid JSON).

    Attributes:
        filepath: Path to the corrupted file.
    """

    def __init__(self, filepath=None, message=None):
        self.filepath = filepath
        if message is None:
            message = f"Data file is corrupted: {filepath}"
        super().__init__(message)
