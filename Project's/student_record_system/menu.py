"""
menu.py — Menu-Driven User Interface
=======================================
This module implements the complete menu system for the application.

The menu is organized as a hierarchy:
    Main Menu
    ├── [1] Student Management
    │   ├── Add Student
    │   ├── View All Students
    │   ├── Search Student
    │   ├── Update Student
    │   ├── Delete Student
    │   └── Back
    ├── [2] NumPy Analysis
    │   ├── Statistical Analysis
    │   ├── Broadcasting (Grace Marks)
    │   ├── Matrix Operations
    │   ├── Boolean Indexing
    │   └── Back
    ├── [3] Reports
    │   ├── Student Report
    │   ├── Class Summary
    │   ├── Statistics Report
    │   └── Back
    ├── [4] Random Generator
    └── [5] Exit

Design Decision:
    Each sub-menu is a separate method that handles its own input loop.
    This keeps each method focused and readable. All user input is
    validated using utils.validators, and all exceptions are caught
    at the menu level to prevent crashes.
"""

import numpy as np

from config import SUBJECTS, NUM_SUBJECTS, PASS_MARKS
from services.student_service import StudentService
from services.numpy_analysis import NumpyAnalysis
from services.random_generator import RandomGenerator
from services.report_service import ReportService
from utils.validators import (
    validate_menu_choice,
    validate_student_id,
    validate_single_mark,
    validate_positive_integer
)
from utils.exceptions import StudentSystemError
from utils.helpers import (
    clear_screen,
    pause,
    print_header,
    print_menu_title,
    print_menu_option,
    print_success,
    print_error,
    print_warning,
    print_info,
    print_separator,
    print_table_header,
    print_table_row,
    get_input,
    confirm_action
)


class MenuHandler:
    """
    Manages the entire menu-driven interface.

    This class orchestrates user interaction by displaying menus,
    collecting input, dispatching to services, and showing results.

    Attributes:
        student_service (StudentService): Handles CRUD operations.
        report_service (ReportService): Generates reports.
        random_generator (RandomGenerator): Creates test data.
        running (bool): Controls the main menu loop.
    """

    def __init__(self):
        """
        Initialize MenuHandler and all required services.

        StudentService automatically loads existing data from file.
        """
        self.student_service = StudentService()
        self.report_service = ReportService()
        self.random_generator = RandomGenerator()
        self.running = True

    # ═════════════════════════════════════════════════════════════════════
    # MAIN MENU
    # ═════════════════════════════════════════════════════════════════════

    def run(self):
        """
        Start the main menu loop.

        This is the entry point called by main.py. It keeps running
        until the user selects Exit.
        """
        while self.running:
            try:
                self._show_main_menu()
            except KeyboardInterrupt:
                print("\n")
                print_warning("Interrupted! Use option [5] to exit properly.")
                pause()
            except Exception as e:
                print_error(f"Unexpected error: {e}")
                pause()

    def _show_main_menu(self):
        """Display and handle the main menu."""
        clear_screen()
        print_header()
        print_menu_title("MAIN MENU")

        print_menu_option(1, "Student Management")
        print_menu_option(2, "NumPy Analysis")
        print_menu_option(3, "Reports")
        print_menu_option(4, "Random Dataset Generator")
        print_menu_option(5, "Exit")

        count = self.student_service.get_student_count()
        print_info(f"Total Students in System: {count}")

        try:
            choice = validate_menu_choice(get_input("Enter your choice"), 1, 5)

            if choice == 1:
                self._student_management_menu()
            elif choice == 2:
                self._numpy_analysis_menu()
            elif choice == 3:
                self._reports_menu()
            elif choice == 4:
                self._random_generator_menu()
            elif choice == 5:
                self._exit_application()

        except StudentSystemError as e:
            print_error(str(e))
            pause()

    def _exit_application(self):
        """Handle graceful application exit."""
        if confirm_action("Are you sure you want to exit?"):
            clear_screen()
            print_header()
            print_success("Thank you for using the Student Record System!")
            print_info("All data has been saved. Goodbye!")
            print()
            self.running = False
        # If not confirmed, simply return to main menu

    # ═════════════════════════════════════════════════════════════════════
    # STUDENT MANAGEMENT SUB-MENU
    # ═════════════════════════════════════════════════════════════════════

    def _student_management_menu(self):
        """Display and handle the Student Management sub-menu."""
        while True:
            try:
                clear_screen()
                print_header("Student Management")
                print_menu_title("STUDENT MANAGEMENT")

                print_menu_option(1, "Add New Student")
                print_menu_option(2, "View All Students")
                print_menu_option(3, "Search Student")
                print_menu_option(4, "Update Student")
                print_menu_option(5, "Delete Student")
                print_menu_option(6, "Back to Main Menu")

                choice = validate_menu_choice(
                    get_input("Enter your choice"), 1, 6
                )

                if choice == 1:
                    self._add_student()
                elif choice == 2:
                    self._view_all_students()
                elif choice == 3:
                    self._search_student()
                elif choice == 4:
                    self._update_student()
                elif choice == 5:
                    self._delete_student()
                elif choice == 6:
                    break

            except StudentSystemError as e:
                print_error(str(e))
                pause()
            except KeyboardInterrupt:
                print()
                break

    def _add_student(self):
        """
        Handle adding a new student.

        Collects: student ID, name, and marks for each subject.
        Validates all inputs before creating the record.
        """
        clear_screen()
        print_header("Add New Student")

        # Suggest next available ID
        next_id = self.student_service.get_next_id()
        print_info(f"Suggested next ID: {next_id}")

        # Collect student ID
        student_id = get_input("Enter Student ID")

        # Collect student name
        name = get_input("Enter Student Name")

        # Collect marks for each subject
        print()
        print_info("Enter marks for each subject (0-100):")
        marks = []
        for subject in SUBJECTS:
            mark = get_input(f"  {subject}")
            marks.append(mark)

        # Add the student (service handles validation)
        student = self.student_service.add_student(student_id, name, marks)

        print_success(f"Student added successfully!")
        print(f"\n  {student}")
        pause()

    def _view_all_students(self):
        """Display all student records in a formatted table."""
        clear_screen()
        print_header("All Students")

        students = self.student_service.get_all_students()

        if not students:
            print_warning("No students found in the system.")
            print_info("Use 'Add Student' or 'Random Generator' to add records.")
        else:
            # Print table
            print(f"\n  {'ID':<6} {'Name':<22} {'Total':>7} {'Avg':>8} "
                  f"{'Grade':>7} {'Status':>8}")
            print_separator("─")

            for student in students:
                status = "PASS" if student.is_passed() else "FAIL"
                print(
                    f"  {student.student_id:<6} {student.name:<22} "
                    f"{student.get_total():>7} {student.get_average():>8.2f} "
                    f"{student.get_grade():>7} {status:>8}"
                )

            print_separator("─")
            print_info(f"Total Students: {len(students)}")

        pause()

    def _search_student(self):
        """
        Search for students by ID or name.

        Supports partial name matching (case-insensitive).
        """
        clear_screen()
        print_header("Search Student")

        keyword = get_input("Enter Student ID or Name to search")

        results = self.student_service.search_students(keyword)

        if not results:
            print_warning(f"No students found matching '{keyword}'.")
        else:
            print_success(f"Found {len(results)} student(s):")
            print()
            for student in results:
                print(f"  {student}")
            print()

            # Offer detailed view
            if len(results) == 1:
                if confirm_action("View detailed report?"):
                    report = self.report_service.generate_student_report(
                        results[0]
                    )
                    print(report)

        pause()

    def _update_student(self):
        """
        Update an existing student's name or marks.

        First finds the student, shows current data, then allows
        selective update of name and/or marks.
        """
        clear_screen()
        print_header("Update Student")

        student_id = get_input("Enter Student ID to update")

        # Find the student first
        student = self.student_service.get_student_by_id(student_id)
        print_info(f"Current record: {student}")

        # Update name?
        new_name = get_input(
            "Enter new name (or press Enter to keep current)"
        )
        name = new_name if new_name else None

        # Update marks?
        update_marks = confirm_action("Do you want to update marks?")
        marks = None
        if update_marks:
            print_info("Enter new marks for each subject (0-100):")
            marks = []
            for subject in SUBJECTS:
                mark = get_input(f"  {subject}")
                marks.append(mark)

        # Perform the update
        updated = self.student_service.update_student(
            student_id, name=name, marks=marks
        )

        print_success("Student updated successfully!")
        print(f"\n  {updated}")
        pause()

    def _delete_student(self):
        """
        Delete a student record after confirmation.

        Shows the student's data before asking for confirmation
        to prevent accidental deletions.
        """
        clear_screen()
        print_header("Delete Student")

        student_id = get_input("Enter Student ID to delete")

        # Show the student first
        student = self.student_service.get_student_by_id(student_id)
        print_warning(f"About to delete: {student}")

        # Confirm deletion
        if confirm_action("Are you sure you want to delete this student?"):
            deleted = self.student_service.delete_student(student_id)
            print_success(f"Student '{deleted.name}' (ID: {deleted.student_id}) deleted.")
        else:
            print_info("Deletion cancelled.")

        pause()

    # ═════════════════════════════════════════════════════════════════════
    # NUMPY ANALYSIS SUB-MENU
    # ═════════════════════════════════════════════════════════════════════

    def _numpy_analysis_menu(self):
        """Display and handle the NumPy Analysis sub-menu."""
        while True:
            try:
                clear_screen()
                print_header("NumPy Analysis")
                print_menu_title("NUMPY MARKS ANALYSIS")

                print_menu_option(1, "Statistical Analysis")
                print_menu_option(2, "Broadcasting (Grace Marks)")
                print_menu_option(3, "Matrix Operations")
                print_menu_option(4, "Boolean Indexing (Pass/Fail/Toppers)")
                print_menu_option(5, "Back to Main Menu")

                choice = validate_menu_choice(
                    get_input("Enter your choice"), 1, 5
                )

                if choice == 1:
                    self._statistical_analysis()
                elif choice == 2:
                    self._broadcasting_menu()
                elif choice == 3:
                    self._matrix_operations()
                elif choice == 4:
                    self._boolean_indexing_menu()
                elif choice == 5:
                    break

            except StudentSystemError as e:
                print_error(str(e))
                pause()
            except ValueError as e:
                print_error(str(e))
                pause()
            except KeyboardInterrupt:
                print()
                break

    def _statistical_analysis(self):
        """
        Display comprehensive statistical analysis.

        Uses NumpyAnalysis to calculate sum, mean, median, std, min, max
        for overall, per-student, and per-subject dimensions.
        """
        clear_screen()
        print_header("Statistical Analysis")

        students = self.student_service.get_all_students()
        if not students:
            print_warning("No students available. Add students first.")
            pause()
            return

        analyzer = NumpyAnalysis(students)
        stats = analyzer.get_full_statistics()

        # Overall Statistics
        print_menu_title("OVERALL STATISTICS")
        overall = stats["overall"]
        print(f"  Grand Total   : {overall['total']:.0f}")
        print(f"  Overall Mean  : {overall['mean']:.2f}")
        print(f"  Overall Median: {overall['median']:.2f}")
        print(f"  Std Deviation : {overall['std']:.2f}")
        print(f"  Minimum Mark  : {overall['min']:.0f}")
        print(f"  Maximum Mark  : {overall['max']:.0f}")

        # Per-Subject Statistics
        print_menu_title("PER-SUBJECT STATISTICS")
        print(f"  {'Subject':<20} {'Total':>8} {'Mean':>8} {'Median':>8} "
              f"{'Std':>8} {'Min':>6} {'Max':>6}")
        print_separator("─")

        per_subj = stats["per_subject"]
        for i, subject in enumerate(SUBJECTS):
            print(
                f"  {subject:<20} "
                f"{per_subj['totals'][i]:>8.0f} "
                f"{per_subj['means'][i]:>8.2f} "
                f"{per_subj['medians'][i]:>8.1f} "
                f"{per_subj['stds'][i]:>8.2f} "
                f"{per_subj['mins'][i]:>6.0f} "
                f"{per_subj['maxs'][i]:>6.0f}"
            )

        # Per-Student Statistics
        print_menu_title("PER-STUDENT STATISTICS")
        print(f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Mean':>8} "
              f"{'Median':>8} {'Std':>8} {'Min':>6} {'Max':>6}")
        print_separator("─")

        per_stu = stats["per_student"]
        for i, student in enumerate(students):
            print(
                f"  {student.student_id:<6} {student.name:<22} "
                f"{per_stu['totals'][i]:>7.0f} "
                f"{per_stu['means'][i]:>8.2f} "
                f"{per_stu['medians'][i]:>8.1f} "
                f"{per_stu['stds'][i]:>8.2f} "
                f"{per_stu['mins'][i]:>6.0f} "
                f"{per_stu['maxs'][i]:>6.0f}"
            )

        pause()

    def _broadcasting_menu(self):
        """
        Handle the broadcasting (grace marks) sub-menu.

        Offers two types of broadcasting:
            1. Uniform grace: same value added to all marks
            2. Subject-wise grace: different value per subject
        """
        clear_screen()
        print_header("Broadcasting — Grace Marks")

        students = self.student_service.get_all_students()
        if not students:
            print_warning("No students available. Add students first.")
            pause()
            return

        print_menu_title("BROADCASTING OPTIONS")
        print_menu_option(1, "Apply Uniform Grace Marks (same for all)")
        print_menu_option(2, "Apply Subject-wise Grace Marks")
        print_menu_option(3, "Back")

        try:
            choice = validate_menu_choice(
                get_input("Enter your choice"), 1, 3
            )
        except StudentSystemError as e:
            print_error(str(e))
            pause()
            return

        if choice == 3:
            return

        analyzer = NumpyAnalysis(students)

        print()
        print_info("Current Marks Matrix:")
        self._display_marks_matrix(analyzer, students)

        if choice == 1:
            # Uniform grace marks
            grace = get_input("Enter uniform grace marks to add")
            try:
                grace_val = int(grace)
            except ValueError:
                print_error("Grace marks must be an integer.")
                pause()
                return

            result = analyzer.apply_uniform_grace(grace_val)
            print()
            print_success(f"After applying {grace_val} grace marks to all:")
            self._display_result_matrix(result, students)

            # Offer to save
            if confirm_action("Save these updated marks?"):
                self._save_graced_marks(students, result)

        elif choice == 2:
            # Subject-wise grace marks
            print()
            print_info("Enter grace marks for each subject:")
            grace_list = []
            for subject in SUBJECTS:
                g = get_input(f"  {subject}")
                try:
                    grace_list.append(int(g))
                except ValueError:
                    print_error(
                        f"Invalid grace mark for {subject}: '{g}'"
                    )
                    pause()
                    return

            result = analyzer.apply_subject_grace(grace_list)
            print()
            print_success("After applying subject-wise grace marks:")
            print_info(
                f"Grace: {dict(zip(SUBJECTS, grace_list))}"
            )
            self._display_result_matrix(result, students)

            # Offer to save
            if confirm_action("Save these updated marks?"):
                self._save_graced_marks(students, result)

        pause()

    def _save_graced_marks(self, students, new_marks_matrix):
        """
        Save grace-adjusted marks back to students.

        Args:
            students (list[Student]): The students to update.
            new_marks_matrix (np.ndarray): Updated marks matrix.
        """
        for i, student in enumerate(students):
            new_marks = [int(m) for m in new_marks_matrix[i]]
            self.student_service.update_student(
                student.student_id, marks=new_marks
            )
        print_success("Updated marks saved successfully!")

    def _matrix_operations(self):
        """
        Display matrix operations on the marks data.

        Demonstrates:
            - Matrix shape and creation
            - Transpose
            - Row-wise and column-wise operations
            - Matrix multiplication
        """
        clear_screen()
        print_header("Matrix Operations")

        students = self.student_service.get_all_students()
        if not students:
            print_warning("No students available. Add students first.")
            pause()
            return

        analyzer = NumpyAnalysis(students)

        # Matrix info
        print_menu_title("MARKS MATRIX")
        print_info(f"Shape: {analyzer.matrix_shape()} "
                   f"(Students × Subjects)")
        print()
        self._display_marks_matrix(analyzer, students)

        # Transpose
        print_menu_title("TRANSPOSED MATRIX")
        transposed = analyzer.transpose()
        print_info(f"Shape: {transposed.shape} (Subjects × Students)")
        print()

        # Print transposed with subject labels as rows
        ids_header = "  " + f"{'Subject':<20}"
        for s in students:
            ids_header += f"{'ID-' + str(s.student_id):>8}"
        print(ids_header)
        print_separator("─")

        for i, subject in enumerate(SUBJECTS):
            row_str = f"  {subject:<20}"
            for val in transposed[i]:
                row_str += f"{val:>8.0f}"
            print(row_str)

        # Row-wise operations
        print_menu_title("ROW-WISE OPERATIONS (Per Student)")
        print(f"  {'ID':<6} {'Name':<22} {'Sum':>8} {'Mean':>8}")
        print_separator("─")

        row_sums = analyzer.row_sum()
        row_means = analyzer.row_mean()
        for i, student in enumerate(students):
            print(
                f"  {student.student_id:<6} {student.name:<22} "
                f"{row_sums[i]:>8.0f} {row_means[i]:>8.2f}"
            )

        # Column-wise operations
        print_menu_title("COLUMN-WISE OPERATIONS (Per Subject)")
        print(f"  {'Subject':<20} {'Sum':>8} {'Mean':>8}")
        print_separator("─")

        col_sums = analyzer.col_sum()
        col_means = analyzer.col_mean()
        for i, subject in enumerate(SUBJECTS):
            print(
                f"  {subject:<20} {col_sums[i]:>8.0f} {col_means[i]:>8.2f}"
            )

        # Matrix multiplication (only if small enough)
        if len(students) <= 10:
            print_menu_title("MATRIX × MATRIX^T (Student Correlation)")
            result = analyzer.matrix_multiply_transpose()
            print_info(f"Result Shape: {result.shape}")
            print()

            # Header
            header = "  " + " " * 6
            for s in students:
                header += f"{'ID-' + str(s.student_id):>10}"
            print(header)
            print_separator("─")

            for i, student in enumerate(students):
                row_str = f"  {'ID-' + str(student.student_id):<6}"
                for val in result[i]:
                    row_str += f"{val:>10.0f}"
                print(row_str)

        pause()

    def _boolean_indexing_menu(self):
        """
        Handle boolean indexing operations sub-menu.

        Uses NumPy boolean masks to filter students by:
            - Pass/Fail status
            - Top performers
            - Custom average threshold
        """
        while True:
            try:
                clear_screen()
                print_header("Boolean Indexing")
                print_menu_title("BOOLEAN INDEXING FILTERS")

                print_menu_option(1, "Show Passed Students")
                print_menu_option(2, "Show Failed Students")
                print_menu_option(3, "Show Toppers")
                print_menu_option(4, "Show Students Above Custom Threshold")
                print_menu_option(5, "Back")

                choice = validate_menu_choice(
                    get_input("Enter your choice"), 1, 5
                )

                students = self.student_service.get_all_students()
                if choice != 5 and not students:
                    print_warning("No students available. Add students first.")
                    pause()
                    continue

                if choice == 5:
                    break

                analyzer = NumpyAnalysis(students)

                if choice == 1:
                    self._show_passed_students(analyzer)
                elif choice == 2:
                    self._show_failed_students(analyzer)
                elif choice == 3:
                    self._show_toppers(analyzer)
                elif choice == 4:
                    self._show_above_threshold(analyzer)

            except StudentSystemError as e:
                print_error(str(e))
                pause()
            except ValueError as e:
                print_error(str(e))
                pause()
            except KeyboardInterrupt:
                print()
                break

    def _show_passed_students(self, analyzer):
        """Display students who passed all subjects."""
        clear_screen()
        print_header("Passed Students")

        passed = analyzer.get_passed_students()

        if not passed:
            print_warning("No students have passed all subjects.")
        else:
            print_success(f"{len(passed)} student(s) passed all subjects "
                         f"(≥ {PASS_MARKS} in each):")
            print()
            print(f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Avg':>8} "
                  f"{'Grade':>7}")
            print_separator("─")

            for student, marks_arr in passed:
                print(
                    f"  {student.student_id:<6} {student.name:<22} "
                    f"{student.get_total():>7} "
                    f"{student.get_average():>8.2f} "
                    f"{student.get_grade():>7}"
                )

        pause()

    def _show_failed_students(self, analyzer):
        """Display students who failed at least one subject."""
        clear_screen()
        print_header("Failed Students")

        failed = analyzer.get_failed_students()

        if not failed:
            print_success("All students have passed! 🎉")
        else:
            print_warning(
                f"{len(failed)} student(s) failed at least one subject:"
            )
            print()
            print(f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Avg':>8} "
                  f"{'Failed Subjects'}")
            print_separator("─")

            for student, marks_arr in failed:
                # Find which subjects were failed
                failed_subjs = [
                    SUBJECTS[i]
                    for i in range(NUM_SUBJECTS)
                    if marks_arr[i] < PASS_MARKS
                ]
                print(
                    f"  {student.student_id:<6} {student.name:<22} "
                    f"{student.get_total():>7} "
                    f"{student.get_average():>8.2f} "
                    f"  {', '.join(failed_subjs)}"
                )

        pause()

    def _show_toppers(self, analyzer):
        """Display top N students by total marks."""
        clear_screen()
        print_header("Toppers")

        n = get_input("How many toppers to display? (default: 3)")
        try:
            n = int(n) if n else 3
        except ValueError:
            n = 3

        toppers = analyzer.get_toppers(n)

        print_success(f"Top {len(toppers)} Student(s):")
        print()
        print(f"  {'Rank':<6} {'ID':<6} {'Name':<22} {'Total':>7} "
              f"{'Avg':>8} {'Grade':>7}")
        print_separator("─")

        for rank, (student, total, marks_arr) in enumerate(toppers, 1):
            medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
            print(
                f"  {medal} {rank:<4} {student.student_id:<6} "
                f"{student.name:<22} {total:>7.0f} "
                f"{student.get_average():>8.2f} "
                f"{student.get_grade():>7}"
            )

        pause()

    def _show_above_threshold(self, analyzer):
        """Display students whose average is above a custom threshold."""
        clear_screen()
        print_header("Custom Threshold Filter")

        threshold = get_input("Enter minimum average threshold")
        try:
            threshold = float(threshold)
        except ValueError:
            print_error("Threshold must be a number.")
            pause()
            return

        results = analyzer.get_above_threshold(threshold)

        if not results:
            print_warning(
                f"No students have an average ≥ {threshold:.1f}."
            )
        else:
            print_success(
                f"{len(results)} student(s) with average ≥ {threshold:.1f}:"
            )
            print()
            print(f"  {'ID':<6} {'Name':<22} {'Average':>8} {'Grade':>7}")
            print_separator("─")

            for student, avg, marks_arr in results:
                print(
                    f"  {student.student_id:<6} {student.name:<22} "
                    f"{avg:>8.2f} {student.get_grade():>7}"
                )

        pause()

    # ═════════════════════════════════════════════════════════════════════
    # REPORTS SUB-MENU
    # ═════════════════════════════════════════════════════════════════════

    def _reports_menu(self):
        """Display and handle the Reports sub-menu."""
        while True:
            try:
                clear_screen()
                print_header("Reports")
                print_menu_title("REPORT GENERATION")

                print_menu_option(1, "Student-wise Report")
                print_menu_option(2, "Class Summary")
                print_menu_option(3, "Statistics Report")
                print_menu_option(4, "Back to Main Menu")

                choice = validate_menu_choice(
                    get_input("Enter your choice"), 1, 4
                )

                if choice == 1:
                    self._student_report()
                elif choice == 2:
                    self._class_summary()
                elif choice == 3:
                    self._statistics_report()
                elif choice == 4:
                    break

            except StudentSystemError as e:
                print_error(str(e))
                pause()
            except KeyboardInterrupt:
                print()
                break

    def _student_report(self):
        """Generate and display a detailed report for one student."""
        clear_screen()
        print_header("Student Report")

        student_id = get_input("Enter Student ID for report")
        student = self.student_service.get_student_by_id(student_id)

        report = self.report_service.generate_student_report(student)
        print(report)
        pause()

    def _class_summary(self):
        """Generate and display the class summary report."""
        clear_screen()
        students = self.student_service.get_all_students()
        report = self.report_service.generate_class_summary(students)
        print(report)
        pause()

    def _statistics_report(self):
        """Generate and display the full statistics report."""
        clear_screen()
        students = self.student_service.get_all_students()
        report = self.report_service.generate_statistics_report(students)
        print(report)
        pause()

    # ═════════════════════════════════════════════════════════════════════
    # RANDOM GENERATOR
    # ═════════════════════════════════════════════════════════════════════

    def _random_generator_menu(self):
        """Handle random student generation."""
        clear_screen()
        print_header("Random Dataset Generator")

        count_str = get_input(
            "How many random students to generate? (default: 10)"
        )

        try:
            count = int(count_str) if count_str else 10
            count = validate_positive_integer(count, "Student Count")
        except (ValueError, StudentSystemError) as e:
            print_error(str(e))
            pause()
            return

        # Determine starting ID
        next_id = self.student_service.get_next_id()

        print_info(
            f"Generating {count} random students starting from ID {next_id}..."
        )

        try:
            new_students = self.random_generator.generate_students(
                count, start_id=next_id
            )

            # Add each student through the service
            added = 0
            for student in new_students:
                try:
                    self.student_service.add_student(
                        student.student_id,
                        student.name,
                        student.marks
                    )
                    added += 1
                except Exception as e:
                    print_warning(f"Skipped: {e}")

            print_success(f"Successfully added {added} random students!")

            # Show a preview
            print()
            print(f"  {'ID':<6} {'Name':<22} {'Total':>7} {'Avg':>8} "
                  f"{'Grade':>7}")
            print_separator("─")

            for student in new_students[:10]:  # Show first 10
                print(
                    f"  {student.student_id:<6} {student.name:<22} "
                    f"{student.get_total():>7} "
                    f"{student.get_average():>8.2f} "
                    f"{student.get_grade():>7}"
                )

            if count > 10:
                print_info(f"... and {count - 10} more.")

        except Exception as e:
            print_error(f"Error generating students: {e}")

        pause()

    # ═════════════════════════════════════════════════════════════════════
    # HELPER DISPLAY METHODS
    # ═════════════════════════════════════════════════════════════════════

    def _display_marks_matrix(self, analyzer, students):
        """
        Display the marks matrix with labels.

        Args:
            analyzer (NumpyAnalysis): The analysis object.
            students (list[Student]): Students for row labels.
        """
        matrix = analyzer.get_marks_matrix()

        # Header
        header = f"  {'ID':<6} {'Name':<18}"
        for subject in SUBJECTS:
            header += f"{subject[:6]:>8}"
        print(header)
        print_separator("─")

        # Data rows
        for i, student in enumerate(students):
            row_str = f"  {student.student_id:<6} {student.name[:16]:<18}"
            for val in matrix[i]:
                row_str += f"{val:>8.0f}"
            print(row_str)

        print_separator("─")

    def _display_result_matrix(self, matrix, students):
        """
        Display a result matrix (e.g., after broadcasting).

        Args:
            matrix (np.ndarray): The result matrix.
            students (list[Student]): Students for row labels.
        """
        header = f"  {'ID':<6} {'Name':<18}"
        for subject in SUBJECTS:
            header += f"{subject[:6]:>8}"
        print(header)
        print_separator("─")

        for i, student in enumerate(students):
            row_str = f"  {student.student_id:<6} {student.name[:16]:<18}"
            for val in matrix[i]:
                row_str += f"{val:>8.0f}"
            print(row_str)

        print_separator("─")
