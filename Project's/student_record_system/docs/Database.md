# Database Documentation

## Storage Format

The application uses **JSON** (JavaScript Object Notation) for data persistence.

### Why JSON?

| Advantage | Description |
|-----------|-------------|
| Human-readable | Can be opened and inspected in any text editor |
| No external DB | No MySQL, PostgreSQL, or SQLite setup required |
| Native support | Python's `json` module handles serialization |
| Portable | Single file, easy to backup, copy, or share |
| Structured | Preserves data types (strings, numbers, arrays) |

## Data File

**Location**: `data/students.json`

**Backup Location**: `data/students_backup.json`

## JSON Schema

The data file contains a JSON array of student objects:

```json
[
    {
        "student_id": 1,
        "name": "Priya Sharma",
        "marks": [85, 90, 78, 92, 88]
    },
    {
        "student_id": 2,
        "name": "Rahul Kumar",
        "marks": [72, 65, 80, 58, 74]
    }
]
```

### Field Descriptions

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `student_id` | Integer | Positive, unique | Unique identifier |
| `name` | String | Non-empty, alphabetic | Student's full name |
| `marks` | Array[Integer] | 5 elements, each 0-100 | Marks for each subject |

### Marks Array Index Mapping

| Index | Subject |
|-------|---------|
| 0 | Math |
| 1 | Physics |
| 2 | Chemistry |
| 3 | English |
| 4 | Computer Science |

## File Operations

### Save Process
1. Create backup of existing file → `students_backup.json`
2. Serialize Student objects to dictionaries
3. Write JSON array with 4-space indentation
4. UTF-8 encoding

### Load Process
1. Check if file exists (if not, return empty list)
2. Read file contents
3. Parse JSON (handle `JSONDecodeError`)
4. Validate data is a JSON array
5. Deserialize each object to a Student instance
6. Skip corrupted individual records (with warning)

### Error Recovery

| Scenario | Handling |
|----------|----------|
| File doesn't exist | Start with empty list (first run) |
| Empty file | Return empty list |
| Invalid JSON | Raise `FileCorruptedError` with recovery message |
| Corrupted record | Skip record, warn user, load rest |
| Permission denied | Display error, return empty list |
| OS error | Display error, return empty list |

## Backup Strategy

- A backup is created **before every save operation**
- Backup file: `data/students_backup.json`
- If save fails, the backup contains the last known good state
- Recovery: manually rename `students_backup.json` to `students.json`

## Data Integrity

| Check | Implementation |
|-------|----------------|
| Duplicate IDs | Checked in `StudentService.add_student()` |
| Valid marks range | Checked in `validators.validate_marks()` |
| Valid name format | Checked in `validators.validate_name()` |
| File consistency | Backup before write, recovery from corrupted records |
