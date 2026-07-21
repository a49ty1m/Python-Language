"""Student model using a dataclass.

Attributes:
- roll (int): Unique roll number
- name (str)
- age (int)
- course (str)
- marks (dict): subject → numeric mark (0‑100)
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Student:
    roll: int
    name: str
    age: int
    course: str
    marks: Dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        # Ensure marks are floats
        for sub, val in self.marks.items():
            self.marks[sub] = float(val)

    def total(self) -> float:
        return sum(self.marks.values())

    def average(self) -> float:
        return self.total() / len(self.marks) if self.marks else 0.0

    def to_dict(self) -> dict:
        """Serialise to a plain dict for JSON storage."""
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks,
        }

    @staticmethod
    def from_dict(data: dict) -> "Student":
        return Student(
            roll=data["roll"],
            name=data["name"],
            age=data["age"],
            course=data["course"],
            marks=data.get("marks", {}),
        )
