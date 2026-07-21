"""
report_service.py — Report Generation Service
================================================
This module generates formatted reports for display in the console.

Report Types:
    1. **Student Report**: Detailed report for a single student
    2. **Class Summary**: Tabular overview of all students
    3. **Statistics Report**: Statistical analysis using NumPy

Design Decision:
    Reports are generated as formatted strings rather than printed directly.
    This separation allows the same report data to be displayed in the
    console, written to a file, or sent to any other output in the future.
"""

import numpy as np

from config import SUBJECTS, NUM_SUBJECTS, TABLE_WIDTH, PASS_MARKS
from services.numpy_analysis import NumpyAnalysis
from utils.helpers import print_separator


class ReportService:
    """
    Generates formatted reports for student data.

    This service creates human-readable reports for:
        - Individual student performance
        - Class-wide summaries
        - Statistical analysis
    """

    @staticmethod
    def generate_student_report(student):
        """
        Generate a detailed report for a single student.

        Includes:
            - Student information (ID, Name)
            - Subject-wise marks with pass/fail status
            - Total, Average, Grade, Overall Status

        Args:
            student (Student): The Student object to report on.

        Returns:
            str: Formatted report string.
        """
        lines = []
        lines.append("")
        lines.append("  ╔" + "═" * 50 + "╗")
        lines.append("  ║" + " STUDENT PERFORMANCE REPORT ".center(50) + "║")
        lines.append("  ╚" + "═" * 50 + "╝")
        lines.append("")
        lines.append(f"  Student ID   : {student.student_id}")
        lines.append(f"  Student Name : {student.name}")
        lines.append("")

        # Subject-wise marks
        lines.append("  " + "─" * 50)
        lines.append(f"  {'Subject':<25} {'Marks':>8} {'Status':>10}")
        lines.append("  " + "─" * 50)

        marks_dict = student.get_subject_marks_dict()
        for subject, mark in marks_dict.items():
            status = "PASS" if mark >= PASS_MARKS else "FAIL"
            marker = "✅" if mark >= PASS_MARKS else "❌"
            lines.append(
                f"  {subject:<25} {mark:>8} {marker} {status:>5}"
            )

        lines.append("  " + "─" * 50)

        # Summary
        lines.append("")
        lines.append(f"  Total Marks  : {student.get_total()} / {NUM_SUBJECTS * 100}")
        lines.append(f"  Average      : {student.get_average():.2f}")
        lines.append(f"  Grade        : {student.get_grade()}")

        overall = "✅ PASSED" if student.is_passed() else "❌ FAILED"
        lines.append(f"  Status       : {overall}")
        lines.append("")

        return "\n".join(lines)

    @staticmethod
    def generate_class_summary(students):
        """
        Generate a tabular class summary of all students.

        Displays each student in a row with:
            ID, Name, Total, Average, Grade, Status

        Args:
            students (list[Student]): List of Student objects.

        Returns:
            str: Formatted class summary table.
        """
        if not students:
            return "\n  ℹ️  No students to display.\n"

        lines = []
        lines.append("")
        lines.append("  ╔" + "═" * (TABLE_WIDTH - 4) + "╗")
        lines.append(
            "  ║" + " CLASS SUMMARY REPORT ".center(TABLE_WIDTH - 4) + "║"
        )
        lines.append("  ╚" + "═" * (TABLE_WIDTH - 4) + "╝")
        lines.append("")

        # Table header
        lines.append(
            f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Avg':>8} "
            f"{'Grade':>7} {'Status':>8}"
        )
        lines.append("  " + "─" * (TABLE_WIDTH - 4))

        # Table rows
        for student in students:
            status = "PASS" if student.is_passed() else "FAIL"
            lines.append(
                f"  {student.student_id:<6} {student.name:<22} "
                f"{student.get_total():>7} {student.get_average():>8.2f} "
                f"{student.get_grade():>7} {status:>8}"
            )

        lines.append("  " + "─" * (TABLE_WIDTH - 4))
        lines.append(f"\n  Total Students: {len(students)}")

        # Count pass/fail
        passed = sum(1 for s in students if s.is_passed())
        failed = len(students) - passed
        lines.append(f"  Passed: {passed} | Failed: {failed}")
        if students:
            lines.append(
                f"  Pass Rate: {(passed / len(students)) * 100:.1f}%"
            )
        lines.append("")

        return "\n".join(lines)

    @staticmethod
    def generate_statistics_report(students):
        """
        Generate a comprehensive statistics report using NumPy.

        Includes:
            - Overall statistics (mean, median, std, min, max)
            - Per-subject statistics
            - Per-student summaries

        Args:
            students (list[Student]): List of Student objects.

        Returns:
            str: Formatted statistics report.
        """
        if not students:
            return "\n  ℹ️  No students available for analysis.\n"

        try:
            analyzer = NumpyAnalysis(students)
        except ValueError as e:
            return f"\n  ❌ Analysis error: {e}\n"

        stats = analyzer.get_full_statistics()

        lines = []
        lines.append("")
        lines.append("  ╔" + "═" * (TABLE_WIDTH - 4) + "╗")
        lines.append(
            "  ║" +
            " STATISTICAL ANALYSIS REPORT ".center(TABLE_WIDTH - 4) + "║"
        )
        lines.append("  ╚" + "═" * (TABLE_WIDTH - 4) + "╝")

        # ── Overall Statistics ──
        lines.append("")
        lines.append("  ◆ OVERALL STATISTICS")
        lines.append("  " + "─" * 40)
        overall = stats["overall"]
        lines.append(f"  Grand Total   : {overall['total']:.0f}")
        lines.append(f"  Overall Mean  : {overall['mean']:.2f}")
        lines.append(f"  Overall Median: {overall['median']:.2f}")
        lines.append(f"  Std Deviation : {overall['std']:.2f}")
        lines.append(f"  Minimum Mark  : {overall['min']:.0f}")
        lines.append(f"  Maximum Mark  : {overall['max']:.0f}")

        # ── Per-Subject Statistics ──
        lines.append("")
        lines.append("  ◆ PER-SUBJECT STATISTICS")
        lines.append(
            f"  {'Subject':<20} {'Mean':>8} {'Median':>8} "
            f"{'Std':>8} {'Min':>6} {'Max':>6}"
        )
        lines.append("  " + "─" * 60)

        per_subj = stats["per_subject"]
        for i, subject in enumerate(SUBJECTS):
            lines.append(
                f"  {subject:<20} {per_subj['means'][i]:>8.2f} "
                f"{per_subj['medians'][i]:>8.1f} "
                f"{per_subj['stds'][i]:>8.2f} "
                f"{per_subj['mins'][i]:>6.0f} "
                f"{per_subj['maxs'][i]:>6.0f}"
            )

        # ── Per-Student Summary ──
        lines.append("")
        lines.append("  ◆ PER-STUDENT SUMMARY")
        lines.append(
            f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Mean':>8} "
            f"{'Min':>6} {'Max':>6}"
        )
        lines.append("  " + "─" * 60)

        per_stu = stats["per_student"]
        for i, student in enumerate(students):
            lines.append(
                f"  {student.student_id:<6} {student.name:<22} "
                f"{per_stu['totals'][i]:>7.0f} "
                f"{per_stu['means'][i]:>8.2f} "
                f"{per_stu['mins'][i]:>6.0f} "
                f"{per_stu['maxs'][i]:>6.0f}"
            )

        lines.append("")

        return "\n".join(lines)
