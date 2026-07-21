"""NumPy analytics for a collection of Student objects.
"""
import numpy as np
from typing import List, Tuple
from student import Student

def _marks_matrix(students: List[Student]) -> Tuple[np.ndarray, List[str]]:
    """Return a (n_students × n_subjects) array and the ordered subject list.
    Missing marks are filled with ``np.nan``.
    """
    if not students:
        return np.empty((0, 0)), []
    subjects = sorted({sub for s in students for sub in s.marks})
    mat = np.full((len(students), len(subjects)), np.nan, dtype=float)
    for i, s in enumerate(students):
        for j, sub in enumerate(subjects):
            if sub in s.marks:
                mat[i, j] = s.marks[sub]
    return mat, subjects

# Basic statistics ----------------------------------------------------------
def total_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nansum(mat))

def mean_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nanmean(mat))

def median_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nanmedian(mat))

def std_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nanstd(mat))

def min_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nanmin(mat))

def max_marks(students: List[Student]) -> float:
    mat, _ = _marks_matrix(students)
    return float(np.nanmax(mat))

# Subject‑wise / student‑wise totals ----------------------------------------
def subject_totals(students: List[Student]):
    mat, subjects = _marks_matrix(students)
    return dict(zip(subjects, np.nansum(mat, axis=0)))

def student_totals(students: List[Student]):
    return {s.roll: s.total() for s in students}

# Broadcasting – apply grace marks ------------------------------------------
def apply_grace(students: List[Student], grace: float = 5) -> None:
    for s in students:
        for sub in s.marks:
            s.marks[sub] = min(s.marks[sub] + grace, 100.0)

# Matrix operations ----------------------------------------------------------
def marks_transpose(students: List[Student]):
    mat, subjects = _marks_matrix(students)
    return mat.T, subjects

def dot_product(students: List[Student]):
    mat, _ = _marks_matrix(students)
    clean = np.nan_to_num(mat)
    return clean @ clean.T

# Random generation ----------------------------------------------------------
def generate_random_students(count: int, subjects: List[str], seed: int | None = None) -> List[Student]:
    rng = np.random.default_rng(seed)
    out = []
    for i in range(1, count + 1):
        marks = {sub: int(rng.integers(35, 101)) for sub in subjects}
        out.append(Student(roll=i, name=f"Student_{i}", age=int(rng.integers(18, 25)), course="CS", marks=marks))
    return out

# Boolean indexing -----------------------------------------------------------
def passed_students(students: List[Student], threshold: float = 40) -> List[Student]:
    return [s for s in students if s.average() >= threshold]

def failed_students(students: List[Student], threshold: float = 40) -> List[Student]:
    return [s for s in students if s.average() < threshold]

def topper_students(students: List[Student], threshold: float = 85) -> List[Student]:
    return [s for s in students if s.average() >= threshold]
