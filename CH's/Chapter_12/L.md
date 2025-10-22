# Python Advanced Features — Chapter 12

A collection of modern Python features and best practices with examples and explanations.

---

## 1. Walrus Operator (`:=`)

**Introduced in Python 3.8**, the walrus operator allows assignment within expressions.

**Example:**
```python
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List has {n} elements, which is more than 3.")

# Traditional approach
# n = len([1, 2, 3, 4, 5])
# if n > 3:
#     print(f"List has {n} elements, which is more than 3.")
```

---

## 2. Type Hints

Type hints help document expected types and enable better IDE support and static type checking.

**Basic type hints:**
```python
n: int = 5
s: str = "Hello"
```

**Function annotations:**
```python
def add(x: int, y: int) -> int:
    """Adds two integers and returns the result."""
    return x + y
```

**Advanced typing:**
```python
from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Alice", 30)
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
identifier: Union[int, str] = "ID123"  # Can be int or str
```

---

## 3. Match-Case (Structural Pattern Matching)

**Introduced in Python 3.10**, `match-case` provides powerful pattern matching capabilities.

```python
def http_status(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

# Usage
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found
print(http_status(403))  # Output: Unknown status
```

---

## 4. Dictionary Merging

**Python 3.9+** introduced the `|` operator for merging dictionaries.

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = dict1 | dict2

# Result: {'a': 1, 'b': 3, 'c': 4}
# Note: If keys overlap, values from the second dictionary take precedence
```

---

## 5. With Statement (Context Managers)

Context managers ensure proper resource cleanup (like closing files).

**Opening multiple files:**
```python
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    # Process files
    pass
# Both files are automatically closed after the block
```

---

## 6. Exception Handling

### Basic Exception Handling

```python
try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please enter a valid number.")
print("Thank You")
```

**Common exception types:**
- `ValueError` — Wrong type of value
- `TypeError` — Wrong data type
- `ZeroDivisionError` — Division by zero
- `FileNotFoundError` — File doesn't exist

### Specific Exception Handling

```python
try:
    # Code that might raise exceptions
    pass
except ValueError as e:
    # Handle ValueError
    pass
except ZeroDivisionError as f:
    # Handle ZeroDivisionError
    pass
except:
    # Catch all other exceptions
    pass
```

### Raising Exceptions

```python
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ZeroDivisionError("You cannot divide by zero!\nPlease enter a non-zero number.")
else:
    print(f"The result of {a} divided by {b} is {a / b}")
```

### Using `else` with Try-Except

The `else` block executes only if **no exceptions** were raised.

```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("No exceptions occurred.")
    print(f"The result of {a} divided by {b} is {result}")
```

### Using `finally` for Cleanup

The `finally` block **always executes**, regardless of exceptions.

```python
def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    else:
        print(f"The result of {a} divided by {b} is {result}")
        return
    finally:
        print("This always executes — used for cleanup (closing files, etc.)")

main()
```

---

## 7. `__name__` and `__main__`

Use this pattern to run code only when the script is executed directly (not when imported).

```python
import module  # This will import and execute module code

# In module.py:
if __name__ == "__main__":
    # This only runs when module.py is executed directly
    print("Running as main script")
```

---

## 8. Global and Local Variables

```python
a = 69  # Global variable

def hi():
    global a  # Declare that we're using the global variable
    a = 7
    print(a)  # Prints 7

hi()
print(a)  # Prints 7 (global variable was modified)
```

**Without `global` keyword:**
- The variable inside the function would be local
- The global variable would remain unchanged

---

## 9. Enumerate

`enumerate()` adds a counter to an iterable, returning `(index, value)` pairs.

**Traditional approach:**
```python
l = [1, 2324, 45225, 523432, 12323]
index = 0
for item in l:
    print(f"Index of item {item} is {index}")
    index += 1
```

**Using `enumerate` (better approach):**
```python
for index, item in enumerate(l):
    print(f"Index of item {item} is {index}")
```

---

## 10. List Comprehensions

List comprehensions provide a concise way to create lists.

**Traditional approach:**
```python
L = [1, 2, 3, 4, 5, 6, 8, 11]
Sq = []
for item in L:
    Sq.append(item**2)
print(Sq)
```

**Using list comprehension (better approach):**
```python
sq = [item**2 for item in L]
print(sq)
```

**Syntax:** `[expression for item in iterable]`

**Benefits:**
- More readable
- Often more efficient
- Concise and Pythonic

---

## Summary

This chapter covers modern Python features that make code more:
- **Readable** — Clear syntax and patterns
- **Efficient** — Built-in optimizations
- **Maintainable** — Type hints and proper error handling
- **Pythonic** — Following Python best practices
