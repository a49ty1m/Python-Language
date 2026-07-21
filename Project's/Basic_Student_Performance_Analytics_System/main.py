"""Entry point – interactive menu for the analytics system.
"""
import sys
from typing import List
from database import load_students, save_students, add_student, update_student, delete_student
from student import Student
from analytics import (
    total_marks, mean_marks, median_marks, std_marks, min_marks, max_marks,
    subject_totals, student_totals, apply_grace, marks_transpose, dot_product,
    generate_random_students, passed_students, failed_students, topper_students,
)
from utils import read_int, read_float, read_marks

SUBJECTS = ["Python", "NumPy", "Database"]

def _print_student(s: Student) -> None:
    marks_str = ", ".join(f"{k}:{v:.1f}" for k, v in s.marks.items())
    print(f"Roll:{s.roll} Name:{s.name} Age:{s.age} Course:{s.course} Marks:[{marks_str}] Avg:{s.average():.2f}")

def add_student_menu() -> None:
    roll = read_int("Roll Number: ")
    name = input("Name: ")
    age = read_int("Age: ", 15, 100)
    course = input("Course: ")
    marks = read_marks(SUBJECTS)
    try:
        add_student(Student(roll, name, age, course, marks))
        print("Student added.")
    except ValueError as e:
        print(e)

def view_students_menu(students: List[Student]) -> None:
    if not students:
        print("No students in database.")
        return
    for s in students:
        _print_student(s)

def search_student_menu(students: List[Student]) -> None:
    term = input("Search by Roll or Name: ").strip().lower()
    matches = [s for s in students if term == str(s.roll).lower() or term in s.name.lower()]
    if not matches:
        print("No matching student.")
        return
    for s in matches:
        _print_student(s)

def update_student_menu() -> None:
    roll = read_int("Roll number to update: ")
    print("Leave a field blank to keep existing value.")
    name = input("New name (or press Enter): ")
    age_input = input("New age (or press Enter): ")
    course = input("New course (or press Enter): ")
    marks = {}
    if input("Update marks? (y/N): ").lower() == "y":
        marks = read_marks(SUBJECTS)
    updates = {}
    if name:
        updates["name"] = name
    if age_input:
        updates["age"] = int(age_input)
    if course:
        updates["course"] = course
    if marks:
        updates["marks"] = marks
    try:
        update_student(roll, **updates)
        print("Student updated.")
    except ValueError as e:
        print(e)

def delete_student_menu() -> None:
    roll = read_int("Roll number to delete: ")
    confirm = input(f"Are you sure you want to delete roll {roll}? (y/N): ")
    if confirm.lower() == "y":
        delete_student(roll)
        print("Deleted.")
    else:
        print("Cancelled.")

def analytics_menu(students: List[Student]) -> None:
    while True:
        print("\n--- Analytics Menu ---")
        print("1. Basic Statistics (sum, mean, median, std, min, max)")
        print("2. Subject‑wise totals")
        print("3. Student‑wise totals")
        print("4. Apply Grace Marks (+5)")
        print("5. Show Marks Matrix (transpose view)")
        print("6. Dot‑product matrix (student similarity)")
        print("7. Show Pass Students")
        print("8. Show Fail Students")
        print("9. Show Topper Students")
        print("0. Back to Main Menu")
        choice = input("Choice: ")
        if choice == "1":
            print(f"Total:{total_marks(students):.2f} Mean:{mean_marks(students):.2f} Median:{median_marks(students):.2f}")
            print(f"Std:{std_marks(students):.2f} Min:{min_marks(students):.2f} Max:{max_marks(students):.2f}")
        elif choice == "2":
            print(subject_totals(students))
        elif choice == "3":
            print(student_totals(students))
        elif choice == "4":
            apply_grace(students, 5)
            save_students(students)
            print("Grace marks applied and saved.")
        elif choice == "5":
            mat, subjects = marks_transpose(students)
            print("Subjects:", subjects)
            print(mat)
        elif choice == "6":
            print(dot_product(students))
        elif choice == "7":
            for s in passed_students(students):
                _print_student(s)
        elif choice == "8":
            for s in failed_students(students):
                _print_student(s)
        elif choice == "9":
            for s in topper_students(students):
                _print_student(s)
        elif choice == "0":
            break
        else:
            print("Invalid option.")

def generate_random_menu(students: List[Student]) -> List[Student]:
    count = read_int("How many random students to generate? ", 1)
    gen = generate_random_students(count, SUBJECTS)
    students.extend(gen)
    save_students(students)
    print(f"Generated and saved {count} random students.")
    return students

def main() -> None:
    students = load_students()
    while True:
        print("\n=== Student Performance Analytics System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Generate Random Students")
        print("7. Analytics")
        print("8. Exit")
        choice = input("Choice: ")
        if choice == "1":
            add_student_menu()
            students = load_students()
        elif choice == "2":
            view_students_menu(students)
        elif choice == "3":
            search_student_menu(students)
        elif choice == "4":
            update_student_menu()
            students = load_students()
        elif choice == "5":
            delete_student_menu()
            students = load_students()
        elif choice == "6":
            students = generate_random_menu(students)
        elif choice == "7":
            analytics_menu(students)
        elif choice == "8":
            save_students(students)
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
