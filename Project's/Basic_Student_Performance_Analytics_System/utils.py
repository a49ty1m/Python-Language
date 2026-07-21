"""Utility helpers for validated user input.
"""
from typing import List

def read_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Value must be between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid integer.")

def read_float(prompt: str, min_val: float | None = None, max_val: float | None = None) -> float:
    while True:
        try:
            val = float(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Value must be between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

def read_marks(subjects: List[str]) -> dict:
    marks = {}
    for sub in subjects:
        val = read_float(f"Enter mark for {sub} (0-100): ", 0, 100)
        marks[sub] = val
    return marks
