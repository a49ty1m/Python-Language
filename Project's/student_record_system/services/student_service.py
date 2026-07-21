"""
student_service.py — Student CRUD Service
============================================
This module provides all Create, Read, Update, Delete (CRUD) operations
for student records. It acts as the bridge between the menu (presentation)
layer and the data (file) layer.

Design Decision:
    The service maintains an in-memory list of Student objects for fast
    access and automatically persists changes to disk via FileService
    after every mutation (add, update, delete). This pattern is called
    "write-through caching" — the in-memory list is always in sync with
    the JSON file.
"""

from models.student import Student
from services.file_service import FileService
from utils.exceptions import (
    StudentNotFoundError,
    DuplicateStudentError,
    InvalidInputError
)
from utils.validators import validate_student_id, validate_name, validate_marks


class StudentService:
    """
    Manages the collection of Student records.

    This service is the single point of access for all student data
    operations. It ensures data integrity by:
        - Preventing duplicate student IDs
        - Validating inputs before modifications
        - Auto-saving after every change

    Attributes:
        students (list[Student]): In-memory list of all student records.
        file_service (FileService): Handles file persistence.
    """

    def __init__(self):
        """
        Initialize StudentService by loading existing records from file.

        If the data file doesn't exist or is empty, starts with an
        empty list.
        """
        self.file_service = FileService()
        self.students = []
        self._load_data()

    def _load_data(self):
        """
        Load student records from the JSON file into memory.

        Handles FileCorruptedError gracefully — if the file is corrupted,
        starts with whatever records could be recovered (or empty list).
        """
        try:
            self.students = self.file_service.load_students()
        except Exception as e:
            print(f"  ⚠️  Warning: Error loading data: {e}")
            print("  ℹ️  Starting with empty student list.")
            self.students = []

    def _save_data(self):
        """
        Persist the current in-memory student list to the JSON file.

        Called automatically after every mutation (add, update, delete).
        """
        self.file_service.save_students(self.students)

    def _find_student_index(self, student_id):
        """
        Find the index of a student by ID.

        Args:
            student_id (int): The student ID to search for.

        Returns:
            int: Index of the student in the list.

        Raises:
            StudentNotFoundError: If no student with the given ID exists.
        """
        for index, student in enumerate(self.students):
            if student.student_id == student_id:
                return index
        raise StudentNotFoundError(student_id)

    # ─────────────────────────────────────────────────────────────────────
    # CREATE — Add a new student
    # ─────────────────────────────────────────────────────────────────────

    def add_student(self, student_id, name, marks):
        """
        Add a new student record.

        Validates that the student ID is not already in use, then creates
        a new Student object and appends it to the list.

        Args:
            student_id: Unique ID for the new student.
            name (str): Student's full name.
            marks (list): List of marks for each subject.

        Returns:
            Student: The newly created Student object.

        Raises:
            DuplicateStudentError: If the student_id already exists.
            InvalidInputError: If any input fails validation.
        """
        # Validate the ID first
        validated_id = validate_student_id(student_id)

        # Check for duplicate
        for student in self.students:
            if student.student_id == validated_id:
                raise DuplicateStudentError(validated_id)

        # Create the Student (constructor validates name and marks)
        new_student = Student(validated_id, name, marks)

        # Add to in-memory list and persist
        self.students.append(new_student)
        self._save_data()

        return new_student

    # ─────────────────────────────────────────────────────────────────────
    # READ — View and search students
    # ─────────────────────────────────────────────────────────────────────

    def get_all_students(self):
        """
        Retrieve all student records.

        Returns:
            list[Student]: List of all Student objects (may be empty).
        """
        return self.students

    def get_student_by_id(self, student_id):
        """
        Retrieve a specific student by ID.

        Args:
            student_id: The student ID to look up.

        Returns:
            Student: The matching Student object.

        Raises:
            StudentNotFoundError: If no student with the ID exists.
        """
        validated_id = validate_student_id(student_id)
        index = self._find_student_index(validated_id)
        return self.students[index]

    def search_students(self, keyword):
        """
        Search students by ID or partial name match.

        The search is case-insensitive for name matching. If the keyword
        is numeric, it also tries to match by student ID.

        Args:
            keyword (str): Search term (ID number or name fragment).

        Returns:
            list[Student]: List of matching Student objects.
        """
        keyword = str(keyword).strip().lower()
        results = []

        for student in self.students:
            # Match by partial name (case-insensitive)
            if keyword in student.name.lower():
                results.append(student)
            # Match by ID (if keyword is numeric)
            elif keyword.isdigit() and student.student_id == int(keyword):
                if student not in results:
                    results.append(student)

        return results

    # ─────────────────────────────────────────────────────────────────────
    # UPDATE — Modify an existing student
    # ─────────────────────────────────────────────────────────────────────

    def update_student(self, student_id, name=None, marks=None):
        """
        Update an existing student's name and/or marks.

        Only the provided fields are updated; None fields are left unchanged.

        Args:
            student_id: ID of the student to update.
            name (str, optional): New name (or None to keep current).
            marks (list, optional): New marks (or None to keep current).

        Returns:
            Student: The updated Student object.

        Raises:
            StudentNotFoundError: If the student ID doesn't exist.
            InvalidInputError: If the new name is invalid.
            InvalidMarksError: If the new marks are invalid.
        """
        validated_id = validate_student_id(student_id)
        index = self._find_student_index(validated_id)
        student = self.students[index]

        # Update name if provided (setter validates automatically)
        if name is not None:
            student.name = name

        # Update marks if provided (setter validates automatically)
        if marks is not None:
            student.marks = marks

        # Persist changes
        self._save_data()

        return student

    # ─────────────────────────────────────────────────────────────────────
    # DELETE — Remove a student
    # ─────────────────────────────────────────────────────────────────────

    def delete_student(self, student_id):
        """
        Delete a student record by ID.

        Args:
            student_id: ID of the student to remove.

        Returns:
            Student: The deleted Student object (for confirmation display).

        Raises:
            StudentNotFoundError: If the student ID doesn't exist.
        """
        validated_id = validate_student_id(student_id)
        index = self._find_student_index(validated_id)
        deleted_student = self.students.pop(index)

        # Persist changes
        self._save_data()

        return deleted_student

    # ─────────────────────────────────────────────────────────────────────
    # Utility Methods
    # ─────────────────────────────────────────────────────────────────────

    def get_student_count(self):
        """
        Get the total number of students.

        Returns:
            int: Count of student records.
        """
        return len(self.students)

    def get_next_id(self):
        """
        Suggest the next available student ID.

        Returns:
            int: One greater than the current maximum ID,
                 or 1 if no students exist.
        """
        if not self.students:
            return 1
        return max(s.student_id for s in self.students) + 1

    def clear_all_students(self):
        """
        Remove all student records.

        This is a destructive operation and should be confirmed
        by the user before calling.

        Returns:
            int: Number of records that were deleted.
        """
        count = len(self.students)
        self.students = []
        self._save_data()
        return count
