# Architecture Documentation

## System Architecture

The Student Record Management System follows a **Layered Architecture** pattern with clear separation of concerns.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                     │
│                                                         │
│   main.py          menu.py          utils/helpers.py     │
│   (Entry Point)    (Menu Handler)   (Display Helpers)    │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                    SERVICE LAYER                         │
│                                                         │
│   student_service.py    numpy_analysis.py                │
│   (CRUD Operations)     (Statistical Analysis)           │
│                                                         │
│   report_service.py     random_generator.py              │
│   (Report Generation)   (Dataset Generation)             │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                     MODEL LAYER                          │
│                                                         │
│   models/student.py                                      │
│   (Student Class - OOP)                                  │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                   DATA ACCESS LAYER                      │
│                                                         │
│   services/file_service.py                               │
│   (JSON File I/O)                                        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                   INFRASTRUCTURE LAYER                   │
│                                                         │
│   config.py             utils/validators.py              │
│   (Configuration)       (Input Validation)               │
│                                                         │
│   utils/exceptions.py                                    │
│   (Custom Exceptions)                                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   data/students.json  │
              │   (Persistent Store)  │
              └───────────────────────┘
```

## Layer Responsibilities

### 1. Presentation Layer
- **Purpose**: Handle all user interaction
- **Components**: `main.py`, `menu.py`, `utils/helpers.py`
- **Rules**: Never contains business logic. Only displays data and collects input.

### 2. Service Layer
- **Purpose**: Implement business logic
- **Components**: `student_service.py`, `numpy_analysis.py`, `report_service.py`, `random_generator.py`
- **Rules**: No direct user I/O. Receives data, processes it, returns results.

### 3. Model Layer
- **Purpose**: Define data structures
- **Components**: `models/student.py`
- **Rules**: Self-validating. No file I/O or user interaction.

### 4. Data Access Layer
- **Purpose**: Handle persistence
- **Components**: `services/file_service.py`
- **Rules**: Only responsible for reading/writing files. No business logic.

### 5. Infrastructure Layer
- **Purpose**: Cross-cutting concerns
- **Components**: `config.py`, `utils/validators.py`, `utils/exceptions.py`
- **Rules**: No dependencies on upper layers. Used by all layers.

## Module Dependency Graph

```
main.py
  └── menu.py
        ├── student_service.py
        │     ├── file_service.py
        │     │     ├── models/student.py
        │     │     ├── config.py
        │     │     └── utils/exceptions.py
        │     ├── models/student.py
        │     ├── utils/exceptions.py
        │     └── utils/validators.py
        ├── numpy_analysis.py
        │     ├── config.py
        │     └── numpy (external)
        ├── report_service.py
        │     ├── numpy_analysis.py
        │     └── config.py
        ├── random_generator.py
        │     ├── models/student.py
        │     ├── config.py
        │     └── numpy (external)
        ├── utils/validators.py
        │     ├── config.py
        │     └── utils/exceptions.py
        └── utils/helpers.py
              └── config.py
```

## Design Patterns Used

| Pattern | Where | Purpose |
|---------|-------|---------|
| **Layered Architecture** | Overall system | Separation of concerns |
| **Service Pattern** | Services layer | Centralize business logic |
| **Repository Pattern** | FileService | Abstract data persistence |
| **Factory Method** | `Student.from_dict()` | Alternative construction |
| **Write-Through Cache** | StudentService | In-memory + file sync |

## Data Flow

### Adding a Student
```
User Input → MenuHandler → StudentService.add_student()
    → Validators (validate ID, name, marks)
    → Student.__init__() (create object)
    → StudentService._save_data()
    → FileService.save_students()
    → data/students.json (write)
```

### Performing Analysis
```
Menu Choice → MenuHandler → NumpyAnalysis.__init__()
    → Build marks matrix from Student objects
    → np.mean(), np.median(), etc.
    → Return results to MenuHandler
    → Display formatted output
```
