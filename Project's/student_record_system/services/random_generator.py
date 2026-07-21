"""
random_generator.py — Random Student Dataset Generator
========================================================
This module generates random student records for testing and demonstration.

NumPy Concepts Demonstrated:
    - numpy.random for generating random integer marks
    - Random name generation from predefined lists
    - Configurable dataset sizes

Design Decision:
    We use numpy.random instead of Python's random module to be consistent
    with the NumPy-based analysis layer. numpy.random is also faster
    for generating large batches of numbers.
"""

import numpy as np

from config import NUM_SUBJECTS, MIN_MARKS, MAX_MARKS, MAX_RANDOM_COUNT
from models.student import Student
from utils.exceptions import InvalidInputError


# ─────────────────────────────────────────────────────────────────────────────
# Predefined Name Lists for Random Generation
# ─────────────────────────────────────────────────────────────────────────────
FIRST_NAMES = [
    "Aarav", "Aditi", "Amit", "Ananya", "Arjun",
    "Deepa", "Diya", "Gaurav", "Isha", "Karan",
    "Kavya", "Meera", "Neha", "Nikhil", "Pooja",
    "Priya", "Rahul", "Riya", "Rohan", "Sakshi",
    "Sneha", "Suman", "Tanvi", "Varun", "Vikram",
    "Anjali", "Harsh", "Jaya", "Kunal", "Lakshmi",
    "Manish", "Nisha", "Pankaj", "Rashmi", "Sanjay",
    "Tara", "Uma", "Vinay", "Yamini", "Zara"
]

LAST_NAMES = [
    "Sharma", "Verma", "Patel", "Kumar", "Singh",
    "Gupta", "Mehta", "Joshi", "Reddy", "Nair",
    "Iyer", "Pillai", "Das", "Bose", "Chopra",
    "Malhotra", "Kapoor", "Saxena", "Tiwari", "Mishra",
    "Banerjee", "Mukherjee", "Rao", "Menon", "Shah",
    "Pandey", "Agarwal", "Chauhan", "Thakur", "Yadav"
]


class RandomGenerator:
    """
    Generates random student records for testing and demonstration.

    This class creates realistic-looking student data with random names
    and marks. It's useful for:
        - Populating the system quickly for demos
        - Testing analysis features with larger datasets
        - Generating sample data for reports

    Attributes:
        rng (numpy.random.Generator): NumPy random number generator
            for reproducible results when seeded.
    """

    def __init__(self, seed=None):
        """
        Initialize the random generator.

        Args:
            seed (int, optional): Random seed for reproducibility.
                If None, results will vary between runs.
        """
        self.rng = np.random.default_rng(seed)

    def _generate_name(self):
        """
        Generate a random full name by combining a first and last name.

        Uses numpy.random.choice to select from predefined lists.

        Returns:
            str: A random full name (e.g., "Priya Sharma").
        """
        first = self.rng.choice(FIRST_NAMES)
        last = self.rng.choice(LAST_NAMES)
        return f"{first} {last}"

    def _generate_marks(self):
        """
        Generate random marks for all subjects.

        Uses numpy.random.integers to generate NUM_SUBJECTS integer
        values in the range [MIN_MARKS, MAX_MARKS].

        Returns:
            list[int]: List of random integer marks.
        """
        return self.rng.integers(
            MIN_MARKS, MAX_MARKS + 1, size=NUM_SUBJECTS
        ).tolist()

    def generate_students(self, count, start_id=1):
        """
        Generate a specified number of random Student objects.

        Args:
            count (int): Number of students to generate.
            start_id (int): Starting student ID. IDs are assigned
                            sequentially from this value.

        Returns:
            list[Student]: List of generated Student objects.

        Raises:
            InvalidInputError: If count is not a positive integer
                               or exceeds MAX_RANDOM_COUNT.
        """
        # Validate count
        if not isinstance(count, int) or count <= 0:
            raise InvalidInputError(
                field="Count",
                value=count,
                message="Count must be a positive integer."
            )

        if count > MAX_RANDOM_COUNT:
            raise InvalidInputError(
                field="Count",
                value=count,
                message=(
                    f"Cannot generate more than {MAX_RANDOM_COUNT} "
                    f"students at once."
                )
            )

        students = []
        used_names = set()  # Track names to avoid duplicates

        for i in range(count):
            # Generate a unique name
            name = self._generate_name()
            attempts = 0
            while name in used_names and attempts < 100:
                name = self._generate_name()
                attempts += 1
            used_names.add(name)

            # Generate random marks
            marks = self._generate_marks()

            # Create Student object
            student = Student(
                student_id=start_id + i,
                name=name,
                marks=marks
            )
            students.append(student)

        return students

    def generate_marks_matrix(self, n_students, n_subjects=None):
        """
        Generate a random marks matrix without creating Student objects.

        Useful for demonstrating NumPy matrix operations independently.

        Args:
            n_students (int): Number of rows (students).
            n_subjects (int, optional): Number of columns (subjects).
                Defaults to NUM_SUBJECTS from config.

        Returns:
            np.ndarray: 2D array of random integer marks.
        """
        if n_subjects is None:
            n_subjects = NUM_SUBJECTS

        return self.rng.integers(
            MIN_MARKS, MAX_MARKS + 1,
            size=(n_students, n_subjects)
        )
