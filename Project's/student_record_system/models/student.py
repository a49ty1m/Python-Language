"""
student.py — Student Model Class
===================================
This module defines the Student class, the core data model of the application.

OOP Concepts Demonstrated:
    - **Encapsulation**: Private attributes with property getters/setters
      that validate data before assignment.
    - **Constructor** (__init__): Initializes a student with validated inputs.
    - **Instance Methods**: get_total(), get_average(), is_passed(), get_grade().
    - **Class Method**: from_dict() — an alternative constructor for creating
      Student objects from dictionary data (loaded from JSON).
    - **Dunder Methods**: __str__, __repr__, __eq__ for clean string
      representation and comparison.

Design Decision:
    Marks are stored as a plain Python list inside the Student object.
    NumPy arrays are created on-the-fly in the analysis layer, which keeps
    the model lightweight and JSON-serializable without custom encoders.
"""

from config import SUBJECTS, NUM_SUBJECTS, PASS_MARKS, GRADE_THRESHOLDS
from utils.validators import validate_student_id, validate_name, validate_marks


class Student:
    """
    Represents a single student record.

    Attributes:
        student_id (int): Unique identifier for the student.
        name (str): Full name of the student.
        marks (list[int]): List of marks, one per subject.

    Example:
        >>> s = Student(1, "Alice Smith", [85, 90, 78, 92, 88])
        >>> print(s)
        ID: 1 | Name: Alice Smith | Total: 433 | Avg: 86.60 | Grade: A
    """

    def __init__(self, student_id, name, marks):
        """
        Initialize a Student instance.

        All parameters are validated before assignment. Invalid values
        raise custom exceptions (see utils.validators).

        Args:
            student_id (int): Positive integer ID.
            name (str): Alphabetic name (spaces allowed).
            marks (list): List of NUM_SUBJECTS integer marks in [0, 100].
        """
        # Use property setters to trigger validation
        self.student_id = student_id
        self.name = name
        self.marks = marks

    # ─────────────────────────────────────────────────────────────────────
    # Properties — Encapsulation with validation in setters
    # ─────────────────────────────────────────────────────────────────────

    @property
    def student_id(self):
        """int: The unique student ID."""
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        """Set student ID after validation."""
        self._student_id = validate_student_id(value)

    @property
    def name(self):
        """str: The student's full name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set student name after validation and title-casing."""
        self._name = validate_name(value)

    @property
    def marks(self):
        """list[int]: Marks for each subject."""
        return self._marks

    @marks.setter
    def marks(self, value):
        """Set marks after validating each value."""
        self._marks = validate_marks(value)

    # ─────────────────────────────────────────────────────────────────────
    # Instance Methods — Business logic tied to a single student
    # ─────────────────────────────────────────────────────────────────────

    def get_total(self):
        """
        Calculate the sum of all marks.

        Returns:
            int: Total marks across all subjects.
        """
        return sum(self._marks)

    def get_average(self):
        """
        Calculate the average marks.

        Returns:
            float: Mean of marks, rounded to 2 decimal places.
        """
        return round(sum(self._marks) / NUM_SUBJECTS, 2)

    def is_passed(self):
        """
        Determine if the student has passed.

        A student passes only if they score >= PASS_MARKS in every subject.

        Returns:
            bool: True if passed, False otherwise.
        """
        return all(mark >= PASS_MARKS for mark in self._marks)

    def get_grade(self):
        """
        Determine the grade based on average marks.

        Grades are assigned by comparing the average against GRADE_THRESHOLDS
        defined in config.py. The first matching threshold wins.

        Returns:
            str: Grade string (e.g., "A+", "B", "F").
        """
        avg = self.get_average()
        for threshold, grade in GRADE_THRESHOLDS:
            if avg >= threshold:
                return grade
        return "F"  # Fallback (should not reach here)

    def get_subject_marks_dict(self):
        """
        Return marks as a dictionary mapping subject names to scores.

        Returns:
            dict: {subject_name: mark} for each subject.
        """
        return dict(zip(SUBJECTS, self._marks))

    # ─────────────────────────────────────────────────────────────────────
    # Serialization — Convert to/from dictionary for JSON storage
    # ─────────────────────────────────────────────────────────────────────

    def to_dict(self):
        """
        Serialize the Student to a dictionary.

        This format is used for JSON persistence via FileService.

        Returns:
            dict: Dictionary with keys 'student_id', 'name', 'marks'.
        """
        return {
            "student_id": self._student_id,
            "name": self._name,
            "marks": self._marks
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Student instance from a dictionary.

        This is an alternative constructor used when loading records
        from JSON files.

        Args:
            data (dict): Dictionary with keys 'student_id', 'name', 'marks'.

        Returns:
            Student: A new Student instance.

        Raises:
            InvalidInputError: If required keys are missing.
            InvalidMarksError: If marks are invalid.
        """
        try:
            return cls(
                student_id=data["student_id"],
                name=data["name"],
                marks=data["marks"]
            )
        except KeyError as e:
            from utils.exceptions import InvalidInputError
            raise InvalidInputError(
                field="Student Data",
                value=str(data),
                message=f"Missing required field in student data: {e}"
            )

    # ─────────────────────────────────────────────────────────────────────
    # Dunder Methods — String representation and equality
    # ─────────────────────────────────────────────────────────────────────

    def __str__(self):
        """
        Human-readable string representation.

        Returns:
            str: Formatted summary of the student record.
        """
        status = "PASS" if self.is_passed() else "FAIL"
        return (
            f"ID: {self._student_id} | "
            f"Name: {self._name} | "
            f"Total: {self.get_total()} | "
            f"Avg: {self.get_average():.2f} | "
            f"Grade: {self.get_grade()} | "
            f"Status: {status}"
        )

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: Unambiguous representation with class name and key attrs.
        """
        return (
            f"Student(student_id={self._student_id}, "
            f"name='{self._name}', "
            f"marks={self._marks})"
        )

    def __eq__(self, other):
        """
        Two students are equal if they have the same student_id.

        Args:
            other (Student): Another Student instance.

        Returns:
            bool: True if IDs match.
        """
        if not isinstance(other, Student):
            return NotImplemented
        return self._student_id == other._student_id
