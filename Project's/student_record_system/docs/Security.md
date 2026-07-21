# Security Documentation

## Input Validation Strategy

All user inputs are validated before processing. The system follows the principle of **"never trust user input"**.

### Validation Matrix

| Input Type | Validation Rules | Validator Function |
|------------|------------------|-------------------|
| Student ID | Positive integer | `validate_student_id()` |
| Name | Non-empty, alphabetic chars + spaces only | `validate_name()` |
| Marks | Integer, 0-100, correct count (5) | `validate_marks()` |
| Menu Choice | Integer within valid range | `validate_menu_choice()` |
| Count | Positive integer, ≤ 1000 | `validate_positive_integer()` |

### Validation Flow

```
Raw Input (string)
  │
  ├── Type conversion (str → int/float)
  │   └── Failure → InvalidInputError
  │
  ├── Range check (min ≤ value ≤ max)
  │   └── Failure → InvalidInputError or InvalidMarksError
  │
  ├── Format check (alphabetic, non-empty)
  │   └── Failure → InvalidInputError
  │
  └── Business rule check (no duplicates)
      └── Failure → DuplicateStudentError
```

## File Handling Safety

### Read Safety
- Check file existence before reading
- Catch `json.JSONDecodeError` for corrupted files
- Catch `PermissionError` for access issues
- Skip individual corrupted records without losing valid ones
- Never crash on file errors

### Write Safety
- Create backup before overwriting
- Use `ensure_ascii=False` for Unicode support
- Use `UTF-8` encoding explicitly
- Catch `PermissionError` and `OSError`
- Directory creation with `exist_ok=True`

### File Path Safety
- All paths derived from `config.py` constants
- Uses `os.path.join()` for cross-platform compatibility
- No user-supplied file paths accepted

## Exception Handling Strategy

### Custom Exception Hierarchy

```
StudentSystemError (base)
├── StudentNotFoundError    — lookup failures
├── DuplicateStudentError   — uniqueness violations
├── InvalidMarksError       — marks range violations
├── InvalidInputError       — general input failures
└── FileCorruptedError      — file parsing failures
```

### Exception Handling Layers

| Layer | Catches | Action |
|-------|---------|--------|
| Validator | `ValueError`, `TypeError` | Raise custom exception |
| Service | `StudentSystemError` | Propagate to menu |
| File Service | `FileNotFoundError`, `json.JSONDecodeError`, `PermissionError`, `OSError` | Return safe default or raise |
| Menu | `StudentSystemError`, `ValueError`, `Exception` | Display error, continue |
| Main | `KeyboardInterrupt`, `Exception` | Graceful shutdown |

### No Unhandled Exceptions Policy

The application is designed so that **no exception ever crashes the program**. Every possible exception is caught at some layer and handled with a user-friendly message.

## Data Protection

| Threat | Mitigation |
|--------|------------|
| Data loss from save failure | Backup created before every save |
| Data corruption | Validate on load, skip bad records |
| Accidental deletion | Confirmation required before delete |
| Buffer overflow | Python handles memory automatically |
| Injection attacks | N/A (no SQL, no eval, no exec) |

## Limitations

- Data is stored in plaintext JSON (not encrypted)
- No user authentication (single-user system)
- No network access (local-only)
- No concurrent access protection (single-process)

These are acceptable for an educational project. For production use, consider:
- Database with proper transactions
- User authentication and authorization
- Data encryption at rest
- Concurrent access controls
