"""JSON‑based persistence for Student objects with CRUD helpers.
"""
import json
from pathlib import Path
from typing import List
from student import Student

DB_FILE = Path("students.json")

def _load_raw() -> List[dict]:
    if not DB_FILE.exists():
        return []
    try:
        with DB_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Error] Loading DB failed: {e}")
        return []

def load_students() -> List[Student]:
    return [Student.from_dict(rec) for rec in _load_raw()]

def save_students(students: List[Student]) -> None:
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = [s.to_dict() for s in students]
    try:
        with DB_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[Error] Saving DB failed: {e}")

def add_student(student: Student) -> None:
    students = load_students()
    if any(s.roll == student.roll for s in students):
        raise ValueError(f"Roll number {student.roll} already exists.")
    students.append(student)
    save_students(students)

def update_student(roll: int, **updates) -> None:
    students = load_students()
    for s in students:
        if s.roll == roll:
            for key, val in updates.items():
                if hasattr(s, key):
                    setattr(s, key, val)
            save_students(students)
            return
    raise ValueError(f"Student with roll {roll} not found.")

def delete_student(roll: int) -> None:
    students = [s for s in load_students() if s.roll != roll]
    save_students(students)
