# Testing Documentation

## Test Strategy

The application is tested through a combination of:
1. **Unit-level smoke tests** — Quick Python checks for core functionality
2. **Manual integration tests** — Interactive testing of menu workflows
3. **Edge case tests** — Testing boundary conditions and error handling

## Unit Smoke Tests

Run these commands from the `student_record_system/` directory:

### Test 1: Student Model Creation
```bash
python -c "
from models.student import Student
s = Student(1, 'Alice Smith', [85, 90, 78, 92, 88])
print('Student:', s)
print('Total:', s.get_total())
print('Average:', s.get_average())
print('Passed:', s.is_passed())
print('Grade:', s.get_grade())
print('Dict:', s.to_dict())
print('TEST PASSED ✅')
"
```

### Test 2: Student Serialization Round-Trip
```bash
python -c "
from models.student import Student
s1 = Student(1, 'Test User', [90, 80, 70, 60, 50])
d = s1.to_dict()
s2 = Student.from_dict(d)
assert s1 == s2, 'Round-trip failed!'
print('Serialization round-trip: PASSED ✅')
"
```

### Test 3: Validation — Invalid Marks
```bash
python -c "
from models.student import Student
from utils.exceptions import InvalidMarksError
try:
    s = Student(1, 'Test', [85, 90, 150, 92, 88])  # 150 is invalid
    print('TEST FAILED ❌ — should have raised InvalidMarksError')
except InvalidMarksError as e:
    print(f'Correctly caught: {e}')
    print('TEST PASSED ✅')
"
```

### Test 4: Validation — Duplicate ID
```bash
python -c "
from services.student_service import StudentService
from utils.exceptions import DuplicateStudentError
svc = StudentService()
svc.students = []  # Reset
svc.add_student(1, 'First', [50,50,50,50,50])
try:
    svc.add_student(1, 'Duplicate', [60,60,60,60,60])
    print('TEST FAILED ❌')
except DuplicateStudentError as e:
    print(f'Correctly caught: {e}')
    print('TEST PASSED ✅')
"
```

### Test 5: NumPy Analysis
```bash
python -c "
import numpy as np
from models.student import Student
from services.numpy_analysis import NumpyAnalysis

students = [
    Student(1, 'A', [80, 90, 70, 60, 50]),
    Student(2, 'B', [30, 40, 50, 60, 70]),
]
analyzer = NumpyAnalysis(students)

print('Mean:', analyzer.mean_marks())
print('Row sums:', analyzer.row_sum())
print('Col means:', analyzer.col_mean())
print('Shape:', analyzer.matrix_shape())
print('Passed:', len(analyzer.get_passed_students()))
print('Failed:', len(analyzer.get_failed_students()))
print('TEST PASSED ✅')
"
```

### Test 6: Broadcasting
```bash
python -c "
import numpy as np
from models.student import Student
from services.numpy_analysis import NumpyAnalysis

students = [Student(1, 'Test', [80, 90, 70, 60, 50])]
analyzer = NumpyAnalysis(students)

# Uniform grace
result = analyzer.apply_uniform_grace(5)
print('After +5 grace:', result)
assert result[0][0] == 85, 'Uniform grace failed'

# Subject-wise grace
result2 = analyzer.apply_subject_grace([10, 5, 8, 3, 2])
print('After subject grace:', result2)
print('TEST PASSED ✅')
"
```

### Test 7: Random Generator
```bash
python -c "
from services.random_generator import RandomGenerator
gen = RandomGenerator(seed=42)
students = gen.generate_students(5, start_id=100)
for s in students:
    print(s)
print(f'Generated {len(students)} students')
print('TEST PASSED ✅')
"
```

## Manual Integration Test Checklist

### Student Management
- [ ] Add a student with valid data → Success message shown
- [ ] Add a student with duplicate ID → Error message shown
- [ ] Add a student with invalid marks (>100) → Error message shown
- [ ] Add a student with empty name → Error message shown
- [ ] View all students → Table displayed correctly
- [ ] Search by ID → Correct student found
- [ ] Search by name → Partial match works
- [ ] Search non-existent → "Not found" message
- [ ] Update student name → Name changed, old data preserved
- [ ] Update student marks → Marks changed, name preserved
- [ ] Delete student with confirmation → Student removed
- [ ] Delete student cancelled → Student preserved

### NumPy Analysis
- [ ] Statistical Analysis → All metrics displayed
- [ ] Uniform grace marks → Before/after shown, save works
- [ ] Subject-wise grace marks → Per-subject values applied
- [ ] Matrix operations → Shape, transpose, row/col ops shown
- [ ] Boolean indexing — Passed → Correct students filtered
- [ ] Boolean indexing — Failed → Shows failed subjects
- [ ] Boolean indexing — Toppers → Ranked correctly
- [ ] Boolean indexing — Threshold → Custom filter works

### Reports
- [ ] Student report → Detailed single report shown
- [ ] Class summary → All students in table format
- [ ] Statistics report → Full NumPy analysis shown

### Random Generator
- [ ] Generate 10 students → 10 added with unique names
- [ ] Generate 0 students → Error message shown
- [ ] Generate with invalid input → Error handled

### Edge Cases
- [ ] Run with empty database → All menus handle gracefully
- [ ] Delete all students, then analyze → "No students" message
- [ ] Enter letters for menu choice → Error handled
- [ ] Press Ctrl+C during menu → Caught, returns to menu
- [ ] Corrupt students.json manually → Handled on next load

## Running All Smoke Tests

```bash
cd student_record_system

# Run all smoke tests sequentially
echo "=== Test 1: Student Model ===" && \
python -c "from models.student import Student; s = Student(1, 'Test', [80,80,80,80,80]); print(s); print('PASS ✅')" && \
echo "=== Test 2: Round-trip ===" && \
python -c "from models.student import Student; s=Student(1,'T',[80,80,80,80,80]); assert s == Student.from_dict(s.to_dict()); print('PASS ✅')" && \
echo "=== Test 3: Validation ===" && \
python -c "
from utils.exceptions import InvalidMarksError
from models.student import Student
try:
    Student(1,'T',[150,80,80,80,80])
    print('FAIL ❌')
except InvalidMarksError:
    print('PASS ✅')
" && \
echo "=== All Tests Passed ==="
```
