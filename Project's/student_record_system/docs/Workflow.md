# Workflow Documentation

## Application Startup Flow

```
1. User runs: python main.py
2. main.py sets up sys.path
3. MenuHandler() is created
   └── StudentService() is created
       └── FileService() is created
           └── Ensures data/ directory exists
       └── load_students() is called
           └── Reads data/students.json
           └── Deserializes to Student objects
4. menu.run() starts the main loop
5. Main menu is displayed
```

## User Workflow: Adding a Student

```
Main Menu → [1] Student Management → [1] Add New Student
│
├── System suggests next available ID
├── User enters Student ID
├── User enters Student Name
├── User enters marks for each of 5 subjects
│
├── Validation:
│   ├── ID: Must be positive integer, not duplicate
│   ├── Name: Must be alphabetic, non-empty
│   └── Marks: Each must be 0-100 integer
│
├── On Success:
│   ├── Student object created
│   ├── Added to in-memory list
│   ├── Auto-saved to students.json
│   └── Success message displayed
│
└── On Failure:
    ├── Specific error message shown
    └── User returns to menu (no data changed)
```

## User Workflow: Statistical Analysis

```
Main Menu → [2] NumPy Analysis → [1] Statistical Analysis
│
├── System loads all students
├── NumpyAnalysis object created
│   └── Builds 2D NumPy marks matrix
│
├── Calculates:
│   ├── Overall: total, mean, median, std, min, max
│   ├── Per-Subject: mean, median, std, min, max for each
│   └── Per-Student: total, mean, min, max for each
│
└── Displays formatted statistics tables
```

## User Workflow: Broadcasting Grace Marks

```
Main Menu → [2] NumPy Analysis → [2] Broadcasting
│
├── [1] Uniform Grace:
│   ├── User enters single grace value
│   ├── NumPy broadcasts: matrix + scalar
│   ├── Result clipped to [0, 100]
│   ├── Before/after comparison shown
│   └── User confirms to save changes
│
└── [2] Subject-wise Grace:
    ├── User enters grace per subject
    ├── NumPy broadcasts: matrix + 1D array
    ├── Result clipped to [0, 100]
    ├── Before/after comparison shown
    └── User confirms to save changes
```

## User Workflow: Boolean Indexing

```
Main Menu → [2] NumPy Analysis → [4] Boolean Indexing
│
├── [1] Passed Students:
│   └── mask = np.all(marks >= 35, axis=1)
│
├── [2] Failed Students:
│   └── mask = ~np.all(marks >= 35, axis=1)
│
├── [3] Toppers:
│   ├── User enters N (default: 3)
│   └── indices = np.argsort(totals)[::-1][:N]
│
└── [4] Above Threshold:
    ├── User enters threshold
    └── mask = averages >= threshold
```

## User Workflow: Random Dataset Generation

```
Main Menu → [4] Random Generator
│
├── User enters count (default: 10)
├── System calculates starting ID
├── For each student:
│   ├── Random name from FIRST_NAMES × LAST_NAMES
│   └── Random marks via numpy.random.integers(0, 101)
├── All students added via StudentService
├── Auto-saved to students.json
└── Preview of first 10 shown
```

## User Workflow: Report Generation

```
Main Menu → [3] Reports
│
├── [1] Student Report:
│   ├── User enters Student ID
│   └── Detailed single-student report generated
│
├── [2] Class Summary:
│   └── Tabular overview of all students
│
└── [3] Statistics Report:
    └── Full NumPy statistical analysis
```

## Error Handling Flow

```
User Input
  │
  ├── Validator catches → InvalidInputError/InvalidMarksError
  │   └── Menu displays: "❌ [specific error message]"
  │
  ├── Service catches → StudentNotFoundError/DuplicateStudentError
  │   └── Menu displays: "❌ [specific error message]"
  │
  ├── File Service catches → FileCorruptedError/PermissionError
  │   └── Menu displays: "❌ [specific error message]"
  │
  └── Unexpected Exception
      └── Top-level catch in menu: "❌ Unexpected error: [details]"

No error ever crashes the application.
```
