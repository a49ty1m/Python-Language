# Installation Guide

## Prerequisites

| Requirement | Minimum Version | Check Command |
|-------------|----------------|---------------|
| Python | 3.8+ | `python --version` or `python3 --version` |
| pip | Any | `pip --version` or `pip3 --version` |

## Step-by-Step Installation

### Step 1: Verify Python Installation

```bash
python3 --version
```

Expected output: `Python 3.8.x` or higher.

If Python is not installed:
- **Linux (Ubuntu/Debian)**: `sudo apt install python3 python3-pip`
- **macOS**: `brew install python3`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

### Step 2: Navigate to the Project

```bash
cd path/to/student_record_system
```

### Step 3: (Optional) Create a Virtual Environment

Recommended to avoid conflicts with system packages:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- **NumPy** (≥ 1.21.0) — the only external dependency

### Step 5: Run the Application

```bash
python main.py
```

You should see the main menu with options for Student Management, NumPy Analysis, Reports, and Random Generator.

## Verifying Installation

Run this quick test to verify everything is working:

```bash
python -c "
import numpy as np
from models.student import Student
s = Student(1, 'Test User', [80, 90, 70, 60, 50])
print('Student:', s)
print('NumPy version:', np.__version__)
print('Installation verified! ✅')
"
```

## Directory Structure After Installation

```
student_record_system/
├── main.py              ← Run this to start
├── menu.py
├── config.py
├── models/
│   ├── __init__.py
│   └── student.py
├── services/
│   ├── __init__.py
│   ├── student_service.py
│   ├── file_service.py
│   ├── numpy_analysis.py
│   ├── report_service.py
│   └── random_generator.py
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   ├── exceptions.py
│   └── helpers.py
├── data/
│   └── students.json    ← Data stored here
├── docs/
│   └── *.md             ← Documentation
└── requirements.txt
```

## Uninstallation

1. Deactivate the virtual environment (if used): `deactivate`
2. Delete the project directory
3. No system-level changes are made by this application
