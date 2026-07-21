# Student Record Management & Marks Analysis System

## Overview

A comprehensive, menu-driven Python application for managing student records and performing statistical analysis on academic marks using NumPy.

## Features

| Module | Description |
|--------|-------------|
| **Student Management** | Add, view, search, update, and delete student records |
| **File Handling** | Automatic JSON persistence with backup and corruption recovery |
| **OOP** | Encapsulated Student class with validation, serialization, and grading |
| **Exception Handling** | Custom exception hierarchy with user-friendly messages |
| **NumPy Analysis** | Sum, mean, median, std, min, max — overall, per-student, per-subject |
| **Broadcasting** | Apply uniform or subject-wise grace marks using NumPy broadcasting |
| **Matrix Operations** | Transpose, row/column aggregations, matrix multiplication |
| **Random Generator** | Generate configurable datasets with random names and marks |
| **Boolean Indexing** | Filter passed/failed students, toppers, custom thresholds |
| **Reports** | Student-wise, class summary, and statistical reports |

## Quick Start

```bash
# 1. Navigate to the project directory
cd student_record_system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python main.py
```

## Project Structure

```
student_record_system/
│
├── main.py                         # Entry point
├── menu.py                         # Menu-driven interface
├── config.py                       # Application configuration
│
├── models/
│   └── student.py                  # Student class (OOP)
│
├── services/
│   ├── student_service.py          # CRUD operations
│   ├── file_service.py             # JSON file handling
│   ├── numpy_analysis.py           # NumPy statistical analysis
│   ├── report_service.py           # Report generation
│   └── random_generator.py         # Random dataset generator
│
├── utils/
│   ├── validators.py               # Input validation
│   ├── exceptions.py               # Custom exceptions
│   └── helpers.py                  # Console display helpers
│
├── data/
│   └── students.json               # Persistent data storage
│
├── docs/                           # Documentation
│   ├── README.md
│   ├── Architecture.md
│   ├── Workflow.md
│   ├── Database.md
│   ├── Testing.md
│   ├── Security.md
│   ├── Installation.md
│   ├── Troubleshooting.md
│   └── Project_Deep_Explanation.md
│
└── requirements.txt                # Dependencies
```

## Menu Structure

```
Main Menu
├── [1] Student Management
│   ├── [1] Add New Student
│   ├── [2] View All Students
│   ├── [3] Search Student
│   ├── [4] Update Student
│   ├── [5] Delete Student
│   └── [6] Back
├── [2] NumPy Analysis
│   ├── [1] Statistical Analysis
│   ├── [2] Broadcasting (Grace Marks)
│   ├── [3] Matrix Operations
│   ├── [4] Boolean Indexing
│   └── [5] Back
├── [3] Reports
│   ├── [1] Student-wise Report
│   ├── [2] Class Summary
│   ├── [3] Statistics Report
│   └── [4] Back
├── [4] Random Dataset Generator
└── [5] Exit
```

## Technologies Used

- **Python 3.8+** — Core language
- **NumPy** — Statistical analysis, broadcasting, matrix operations, boolean indexing
- **JSON** — Data persistence
- **OS module** — File system operations

## Learning Outcomes

This project demonstrates integration of:

- ✅ Core Python (variables, loops, conditionals, functions)
- ✅ Object-Oriented Programming (classes, encapsulation, inheritance)
- ✅ File Handling (JSON read/write, backup, error recovery)
- ✅ Exception Handling (custom exceptions, try/except)
- ✅ NumPy (arrays, broadcasting, matrix ops, boolean indexing)
- ✅ Modular Programming (separation of concerns)
- ✅ Clean Code (PEP-8, docstrings, comments)

## License

This project is for educational purposes.
