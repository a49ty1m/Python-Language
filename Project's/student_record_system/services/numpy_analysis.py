"""
numpy_analysis.py — NumPy-Based Marks Analysis
=================================================
This module performs all statistical analysis, broadcasting, matrix
operations, and boolean indexing on student marks using NumPy.

NumPy Concepts Demonstrated:
    - **Array Creation**: Building 2D arrays from student marks
    - **Statistical Functions**: sum, mean, median, std, min, max
    - **Axis Operations**: Row-wise (per student) and column-wise (per subject)
    - **Broadcasting**: Adding scalar or per-subject grace marks to all rows
    - **Matrix Operations**: Transpose, dot product, row/col aggregations
    - **Boolean Indexing**: Filtering students by pass/fail, toppers, threshold

Design Decision:
    This class receives a list of Student objects and builds a NumPy array
    internally. It does NOT modify the original Student objects — analysis
    is read-only. Broadcasting operations return new arrays rather than
    mutating the source data, following NumPy best practices.
"""

import numpy as np

from config import SUBJECTS, NUM_SUBJECTS, PASS_MARKS, MAX_MARKS, MIN_MARKS


class NumpyAnalysis:
    """
    Performs statistical analysis on student marks using NumPy.

    The class builds a 2D NumPy array (marks matrix) from a list of
    Student objects, where:
        - Each ROW represents a student
        - Each COLUMN represents a subject

    Attributes:
        students (list[Student]): Reference to the student list.
        marks_matrix (np.ndarray): 2D array of shape (n_students, n_subjects).
        student_names (list[str]): Names corresponding to each row.
        student_ids (list[int]): IDs corresponding to each row.
    """

    def __init__(self, students):
        """
        Initialize NumpyAnalysis with a list of Student objects.

        Builds the marks matrix from the students' marks lists.

        Args:
            students (list[Student]): List of Student objects to analyze.

        Raises:
            ValueError: If the student list is empty.
        """
        if not students:
            raise ValueError("Cannot perform analysis: No students available.")

        self.students = students
        self.student_names = [s.name for s in students]
        self.student_ids = [s.student_id for s in students]

        # Build the 2D marks matrix
        # Each row is a student's marks, each column is a subject
        self.marks_matrix = np.array(
            [s.marks for s in students], dtype=np.float64
        )

    # ─────────────────────────────────────────────────────────────────────
    # Statistical Analysis — Using NumPy aggregate functions
    # ─────────────────────────────────────────────────────────────────────

    def total_marks(self, axis=None):
        """
        Calculate sum of marks.

        Args:
            axis: None = grand total, 0 = per-subject totals,
                  1 = per-student totals.

        Returns:
            np.ndarray or float: Sum result.
        """
        return np.sum(self.marks_matrix, axis=axis)

    def mean_marks(self, axis=None):
        """
        Calculate mean of marks.

        Args:
            axis: None = overall mean, 0 = per-subject mean,
                  1 = per-student mean.

        Returns:
            np.ndarray or float: Mean result rounded to 2 decimals.
        """
        return np.round(np.mean(self.marks_matrix, axis=axis), 2)

    def median_marks(self, axis=None):
        """
        Calculate median of marks.

        Args:
            axis: None = overall median, 0 = per-subject median,
                  1 = per-student median.

        Returns:
            np.ndarray or float: Median result.
        """
        return np.median(self.marks_matrix, axis=axis)

    def std_marks(self, axis=None):
        """
        Calculate standard deviation of marks.

        Args:
            axis: None = overall std, 0 = per-subject std,
                  1 = per-student std.

        Returns:
            np.ndarray or float: Standard deviation rounded to 2 decimals.
        """
        return np.round(np.std(self.marks_matrix, axis=axis), 2)

    def min_marks(self, axis=None):
        """
        Find minimum marks.

        Args:
            axis: None = overall min, 0 = per-subject min,
                  1 = per-student min.

        Returns:
            np.ndarray or float: Minimum value(s).
        """
        return np.min(self.marks_matrix, axis=axis)

    def max_marks(self, axis=None):
        """
        Find maximum marks.

        Args:
            axis: None = overall max, 0 = per-subject max,
                  1 = per-student max.

        Returns:
            np.ndarray or float: Maximum value(s).
        """
        return np.max(self.marks_matrix, axis=axis)

    def get_full_statistics(self):
        """
        Generate a comprehensive statistics summary.

        Returns:
            dict: Dictionary containing all statistical measures,
                  organized by scope (overall, per-student, per-subject).
        """
        return {
            "overall": {
                "total": float(self.total_marks()),
                "mean": float(self.mean_marks()),
                "median": float(self.median_marks()),
                "std": float(self.std_marks()),
                "min": float(self.min_marks()),
                "max": float(self.max_marks()),
            },
            "per_student": {
                "totals": self.total_marks(axis=1),
                "means": self.mean_marks(axis=1),
                "medians": self.median_marks(axis=1),
                "stds": self.std_marks(axis=1),
                "mins": self.min_marks(axis=1),
                "maxs": self.max_marks(axis=1),
            },
            "per_subject": {
                "totals": self.total_marks(axis=0),
                "means": self.mean_marks(axis=0),
                "medians": self.median_marks(axis=0),
                "stds": self.std_marks(axis=0),
                "mins": self.min_marks(axis=0),
                "maxs": self.max_marks(axis=0),
            }
        }

    # ─────────────────────────────────────────────────────────────────────
    # Broadcasting — Apply grace marks using NumPy broadcasting
    # ─────────────────────────────────────────────────────────────────────

    def apply_uniform_grace(self, grace_marks):
        """
        Apply the same grace marks to ALL subjects for ALL students.

        Broadcasting: scalar + 2D array → each element gets the scalar added.

        Args:
            grace_marks (int or float): Grace marks to add uniformly.

        Returns:
            np.ndarray: New marks matrix with grace applied (clipped to MAX_MARKS).
        """
        # Broadcasting: scalar is broadcast across the entire matrix
        result = self.marks_matrix + grace_marks

        # Clip to ensure no mark exceeds MAX_MARKS or goes below MIN_MARKS
        return np.clip(result, MIN_MARKS, MAX_MARKS)

    def apply_subject_grace(self, grace_array):
        """
        Apply different grace marks per subject to ALL students.

        Broadcasting: 1D array (1, n_subjects) + 2D array (n_students, n_subjects)
        → each column gets its respective grace added.

        Args:
            grace_array (list or np.ndarray): Grace marks per subject.
                Must have length equal to NUM_SUBJECTS.

        Returns:
            np.ndarray: New marks matrix with subject-wise grace applied.

        Raises:
            ValueError: If grace_array length doesn't match NUM_SUBJECTS.
        """
        grace = np.array(grace_array, dtype=np.float64)

        if grace.shape[0] != NUM_SUBJECTS:
            raise ValueError(
                f"Grace array must have {NUM_SUBJECTS} values "
                f"(one per subject). Got {grace.shape[0]}."
            )

        # Broadcasting: 1D array broadcasts across each row
        result = self.marks_matrix + grace

        # Clip to valid range
        return np.clip(result, MIN_MARKS, MAX_MARKS)

    # ─────────────────────────────────────────────────────────────────────
    # Matrix Operations — Demonstrate NumPy matrix capabilities
    # ─────────────────────────────────────────────────────────────────────

    def get_marks_matrix(self):
        """
        Return the raw marks matrix.

        Returns:
            np.ndarray: 2D array of shape (n_students, n_subjects).
        """
        return self.marks_matrix

    def transpose(self):
        """
        Transpose the marks matrix.

        Rows become columns and vice versa:
            Original: (n_students × n_subjects)
            Transposed: (n_subjects × n_students)

        Returns:
            np.ndarray: Transposed matrix.
        """
        return self.marks_matrix.T

    def row_sum(self):
        """
        Calculate the sum of each row (total marks per student).

        Returns:
            np.ndarray: 1D array of row sums.
        """
        return np.sum(self.marks_matrix, axis=1)

    def col_sum(self):
        """
        Calculate the sum of each column (total marks per subject).

        Returns:
            np.ndarray: 1D array of column sums.
        """
        return np.sum(self.marks_matrix, axis=0)

    def row_mean(self):
        """
        Calculate the mean of each row (average marks per student).

        Returns:
            np.ndarray: 1D array of row means.
        """
        return np.round(np.mean(self.marks_matrix, axis=1), 2)

    def col_mean(self):
        """
        Calculate the mean of each column (average marks per subject).

        Returns:
            np.ndarray: 1D array of column means.
        """
        return np.round(np.mean(self.marks_matrix, axis=0), 2)

    def matrix_shape(self):
        """
        Get the shape of the marks matrix.

        Returns:
            tuple: (n_students, n_subjects).
        """
        return self.marks_matrix.shape

    def matrix_multiply_transpose(self):
        """
        Multiply the marks matrix with its transpose.

        Result: (n_students × n_students) matrix showing student correlations.

        Returns:
            np.ndarray: Result of matrix × matrix.T.
        """
        return np.dot(self.marks_matrix, self.marks_matrix.T)

    # ─────────────────────────────────────────────────────────────────────
    # Boolean Indexing — Filter students based on conditions
    # ─────────────────────────────────────────────────────────────────────

    def get_passed_students(self):
        """
        Filter students who passed all subjects (>= PASS_MARKS in each).

        Boolean Indexing: Creates a boolean mask where each element is
        True if the student passed all subjects, then uses it to index
        the student list.

        Returns:
            list[tuple]: List of (Student, marks_array) for passed students.
        """
        # Create boolean mask: True if ALL marks >= PASS_MARKS for a row
        pass_mask = np.all(self.marks_matrix >= PASS_MARKS, axis=1)

        return [
            (self.students[i], self.marks_matrix[i])
            for i in range(len(self.students))
            if pass_mask[i]
        ]

    def get_failed_students(self):
        """
        Filter students who failed at least one subject.

        Boolean Indexing: Inverse of the pass mask.

        Returns:
            list[tuple]: List of (Student, marks_array) for failed students.
        """
        # Failed = NOT all marks >= PASS_MARKS
        fail_mask = ~np.all(self.marks_matrix >= PASS_MARKS, axis=1)

        return [
            (self.students[i], self.marks_matrix[i])
            for i in range(len(self.students))
            if fail_mask[i]
        ]

    def get_toppers(self, n=3):
        """
        Get the top N students by total marks.

        Uses np.argsort to find the indices of the highest totals.

        Args:
            n (int): Number of top students to return. Defaults to 3.

        Returns:
            list[tuple]: List of (Student, total, marks_array) sorted by total desc.
        """
        totals = np.sum(self.marks_matrix, axis=1)

        # argsort returns ascending order; we reverse for descending
        sorted_indices = np.argsort(totals)[::-1]

        # Take top N (or all if fewer students exist)
        top_n = min(n, len(self.students))
        result = []
        for idx in sorted_indices[:top_n]:
            result.append((
                self.students[idx],
                float(totals[idx]),
                self.marks_matrix[idx]
            ))
        return result

    def get_above_threshold(self, threshold):
        """
        Filter students whose average is above a custom threshold.

        Boolean Indexing: Creates a mask based on per-student averages.

        Args:
            threshold (float): Minimum average to qualify.

        Returns:
            list[tuple]: List of (Student, average, marks_array) for qualifying students.
        """
        averages = np.mean(self.marks_matrix, axis=1)
        mask = averages >= threshold

        return [
            (self.students[i], float(averages[i]), self.marks_matrix[i])
            for i in range(len(self.students))
            if mask[i]
        ]
