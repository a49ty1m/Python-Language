# Troubleshooting Guide

## Common Issues and Solutions

### 1. ModuleNotFoundError: No module named 'numpy'

**Cause**: NumPy is not installed.

**Solution**:
```bash
pip install numpy
# or
pip install -r requirements.txt
```

### 2. ModuleNotFoundError: No module named 'models'

**Cause**: Running the script from the wrong directory.

**Solution**: Make sure you're inside the `student_record_system/` directory:
```bash
cd student_record_system
python main.py
```

### 3. "Permission denied" when saving data

**Cause**: The `data/` directory or `students.json` file has restrictive permissions.

**Solution**:
```bash
# Linux/macOS
chmod 755 data/
chmod 644 data/students.json

# Or create the directory manually
mkdir -p data
```

### 4. "Data file is corrupted" error on startup

**Cause**: The `data/students.json` file contains invalid JSON (e.g., manually edited incorrectly).

**Solutions**:

**Option A**: Restore from backup:
```bash
cp data/students_backup.json data/students.json
```

**Option B**: Reset the data file:
```bash
echo "[]" > data/students.json
```

**Option C**: Validate and fix the JSON:
```bash
python -c "import json; json.load(open('data/students.json'))"
```
This will show the exact error location.

### 5. Unicode/Emoji display issues

**Cause**: Terminal doesn't support Unicode characters.

**Solution**: Use a modern terminal emulator that supports UTF-8:
- **Linux**: GNOME Terminal, Konsole, Alacritty
- **macOS**: Terminal.app, iTerm2
- **Windows**: Windows Terminal, PowerShell 7

### 6. "Student ID must be positive" error

**Cause**: Entering 0, negative numbers, or non-numeric values as Student ID.

**Solution**: Enter a positive integer (e.g., 1, 2, 3, ...).

### 7. Screen doesn't clear properly

**Cause**: The `clear` command may not work in all terminal environments (e.g., some IDEs).

**Solution**: This is cosmetic only and doesn't affect functionality. The application continues to work correctly.

### 8. Application closes unexpectedly

**Cause**: An unhandled exception (should be rare due to comprehensive error handling).

**Solution**:
1. Check the terminal output for error details
2. Verify `data/students.json` is not corrupted
3. Run the smoke tests from `docs/Testing.md` to isolate the issue

### 9. Random generator creates duplicate names

**Cause**: When generating many students (>100), name combinations may repeat.

**Solution**: This is expected behavior. Names can repeat but Student IDs are always unique. The system handles this correctly.

### 10. NumPy analysis shows "No students available"

**Cause**: The database is empty.

**Solution**: Add students first using:
- **Option 1**: Student Management → Add New Student
- **Option 2**: Random Dataset Generator (Main Menu → [4])

## Getting Help

If you encounter an issue not listed here:

1. Check the error message carefully — the system provides specific messages
2. Verify your Python version: `python --version` (must be 3.8+)
3. Verify NumPy is installed: `python -c "import numpy; print(numpy.__version__)"`
4. Check the data file: `cat data/students.json`
5. Run the smoke tests: see `docs/Testing.md`
