# 🐍 Python Practice Questions
### Complete Reference for Automation · Networking · Security · Data Science

> **Rules:** Solve every question yourself. Test edge cases. Never paste solutions.
> For networking and security exercises — use only systems and captures you own or have explicit written authorization to test.

---

## Quick Navigation

| # | Section | Questions |
|---|---------|-----------|
| 1 | [Core Python Fundamentals](#1-core-python-fundamentals) | ~80 |
| 2 | [Object-Oriented Programming](#2-object-oriented-programming) | ~30 |
| 3 | [File Handling](#3-file-handling) | ~20 |
| 4 | [Modules, Packages & Environments](#4-modules-packages--environments) | ~15 |
| 5 | [Exception Handling](#5-exception-handling) | ~15 |
| 6 | [NumPy](#6-numpy) | ~40 |
| 7 | [Pandas](#7-pandas) | ~40 |
| 8 | [Networking Programming](#8-networking-programming) | ~30 |
| 9 | [requests](#9-requests) | ~25 |
| 10 | [BeautifulSoup (bs4)](#10-beautifulsoup-bs4) | ~20 |
| 11 | [Selenium](#11-selenium) | ~20 |
| 12 | [socket Library](#12-socket-library) | ~20 |
| 13 | [dnspython](#13-dnspython) | ~15 |
| 14 | [Scapy](#14-scapy) | ~20 |
| 15 | [PyShark](#15-pyshark) | ~15 |
| 16 | [cryptography](#16-cryptography) | ~20 |
| 17 | [Paramiko](#17-paramiko) | ~15 |
| 18 | [Regular Expressions (re)](#18-regular-expressions-re) | ~25 |
| 19 | [JSON, XML, CSV, YAML, urllib.parse](#19-json-xml-csv-yaml-urllibparse) | ~30 |
| 20 | [pwntools (Advanced)](#20-pwntools-advanced) | ~10 |
| 21 | [Automation Projects](#21-automation-projects) | ~20 |
| 22 | [Secure Coding Practices](#22-secure-coding-practices) | ~15 |
| 23 | [Code Quality & Professional Workflow](#23-code-quality--professional-workflow) | ~15 |
| 24 | [Capstone Projects](#24-capstone-projects) | ~10 |
| 25 | [Professional Curriculum Extensions](#25-professional-curriculum-extensions) | 80 |

---

## 1. Core Python Fundamentals

### 1.1 Variables, Data Types & Operators

**Output Prediction**
- [ ] Predict the output: `print(type(True + 1))`, `print(type(1 / 1))`, `print(type(1 // 1))`. Explain each result.
- [ ] Predict what `bool("")`, `bool("0")`, `bool([])`, `bool([0])`, `bool({})`, and `bool(None)` return. List all falsy values in Python.
- [ ] Predict: `print(0.1 + 0.2 == 0.3)`. Explain the floating-point issue and show a safe comparison method.
- [ ] Predict the result of `2 ** 3 ** 2` and `(2 ** 3) ** 2`. Explain right-associativity of `**`.
- [ ] Predict: `x = 256; y = 256; print(x is y)` vs `x = 1000; y = 1000; print(x is y)`. Explain Python's integer interning.
- [ ] Predict: `-7 // 2` and `-7 % 2`. Explain floor division behavior with negative numbers.

**Coding**
- [ ] Create variables for a student's name, age, CGPA, and enrollment status. Print each value with its type using an f-string.
- [ ] Take two integers as input. Print: sum, difference, product, true division, floor division, modulus, exponentiation, and their bitwise AND, OR, XOR.
- [ ] Write a program that converts temperature from Celsius to Fahrenheit, Kelvin, and Rankine. Format each output to 2 decimal places.
- [ ] Build a simple bill calculator: accept item price, quantity, discount (%), and tax (%). Apply discount first, then tax. Display itemized breakdown.
- [ ] Swap two variables three ways: with temp variable, tuple unpacking, and XOR trick. Verify all produce the same result.
- [ ] Write a script that checks whether a year is a leap year using a single boolean expression (no if/else).
- [ ] Given an IP address as a string (e.g. `"192.168.1.100"`), convert it to a 32-bit integer using bitwise shifts. Then convert back. Do not use the `ipaddress` module.
- [ ] Write a subnet calculator: accept an IP and prefix length (e.g. `192.168.1.50/24`). Print network address, broadcast, first host, last host, and total hosts using bitwise operators only.

**Debugging**
- [ ] Fix this code: `age = input("Age: ")` then `if age >= 18: print("Adult")`. Identify the bug type, fix it, and explain the root cause.
- [ ] Find and fix all bugs: `x = 10; y = "5"; z = x + y; print(f"Sum: {z}"); check = 0b1010 && 0b1100`.

---

### 1.2 Input, Output & String Formatting

**Output Prediction**
- [ ] Predict the exact output: `print("192", "168", "1", "1", sep=".")`, `print("Scan", end=" ")`, `print("done", end="\n\n")`, `print(*range(5), sep="-")`.
- [ ] Predict: `f"{'LEFT':<10}|"`, `f"{'RIGHT':>10}|"`, `f"{'CENTER':^10}|"`, `f"{'FILL':*^10}|"`, `f"{255:08b}"`, `f"{255:#010x}"`, `f"{0.0025:.2%}"`.
- [ ] Predict: `print(r"C:\new\test")` vs `print("C:\new\test")`. Explain raw strings and when you must use them.

**Coding**
- [ ] Build a "Host Info Collector" that takes hostname, IP, port count, and device type as input and prints a neatly aligned box-style summary.
- [ ] Write a port scanner result formatter: given a list of `(port, service, status)` tuples, print a table with padded columns, a header, and a footer showing counts of open/closed ports.
- [ ] Accept a full name as input. Normalize it: strip extra whitespace, apply title case, and print `First: X, Last: Y, Initials: XY`.
- [ ] Write a program that masks sensitive data: given a credit card number, show only the last 4 digits (`**** **** **** 1234`). Handle cards shorter than 4 digits.

---

### 1.3 Conditional Statements

**Output Prediction**
- [ ] Predict the output for `x = 15`: nested `if x > 10 → if x > 20 → "A" elif x > 15 → "B" else "C" else "D"`. Then predict for `x = 10` and `x = 21`.
- [ ] Predict the output of each ternary: `"pos" if -1 > 0 else "neg"`, `x or "default"` where `x = 0`, `x and expensive_call()` where `x = False`.

**Coding**
- [ ] Write a CVSS score classifier: 0.0 → None, 0.1–3.9 → Low, 4.0–6.9 → Medium, 7.0–8.9 → High, 9.0–10.0 → Critical. Reject scores outside 0–10.
- [ ] Write a port-to-service mapper using `match-case` (Python 3.10+). Handle at least 15 well-known ports and use `case _` as fallback.
- [ ] Build an HTTP status code describer using `match-case` with OR patterns: 2xx → Success, 3xx → Redirect, 4xx → Client Error, 5xx → Server Error.
- [ ] Write a login gate: accepts username, password, and 6-digit 2FA code. Provide distinct error messages for each failed condition without revealing which credential is wrong.
- [ ] Write a grade calculator: 90–100 A+, 80–89 A, 70–79 B, 60–69 C, below 60 F. Reject marks outside 0–100. Print grade and a motivational message.

**Debugging**
- [ ] Fix all bugs in a risk-scoring script that reads open port count and patch age from `input()`, computes a float score, and compares it to integer thresholds. There are at least 6 bugs including type errors and a syntax error.

---

### 1.4 Loops

**Output Prediction**
- [ ] Predict: `for i in range(10, 0, -3): print(i, end=" ")`. Then explain what `range(0)` produces and what the `else` clause of a `for` loop does.
- [ ] Predict the exact output of a `while` loop that prints the Collatz sequence starting at 27. How many steps does it take to reach 1?
- [ ] Predict this output: a `for` loop over `[1,2,None,4,None,6]` that skips `None` values using `continue` and sums the rest.
- [ ] Predict the behavior when modifying a list while iterating over it directly. Explain why it's dangerous and show the safe alternative.

**Coding**
- [ ] Print a multiplication table (1–12) as a formatted grid with aligned columns.
- [ ] Find all prime numbers between 1 and 1000 using a sieve or trial-division loop. Count them and print the largest.
- [ ] Generate all host IPs for any /24 subnet entered as `192.168.X.0`. Print them 8 per row and count them.
- [ ] Simulate a brute-force PIN attack: try all 4-digit PINs from 0000–9999 against hardcoded PIN `"4729"`. Print attempt number, progress every 1000, and time taken.
- [ ] Build an interactive CLI menu using `while True` with `match-case` dispatch: options for IP Info, Port Lookup, Password Checker, Caesar Cipher, and Exit. Never crash on bad input.
- [ ] Implement FizzBuzz from 1–100. Count and print how many of each category (Fizz, Buzz, FizzBuzz, plain numbers) appeared.
- [ ] Write a nested loop that prints a half-pyramid, full pyramid, and inverted pyramid of `*` characters for a given height.
- [ ] Write a "sliding window" loop: given a list of connection timestamps, flag any source that makes more than 5 connections within any 10-second window.

**Debugging**
- [ ] Fix this while loop that should scan ports 1–1024 but has an infinite loop, a wrong assignment operator (`=+` vs `+=`), a missing else branch, and an off-by-one error.
- [ ] Fix a loop that's supposed to detect brute-force IPs (more than 3 × 401s) but iterates `counts` incorrectly and uses `=` instead of `==` in a condition.

---

### 1.5 Strings

**Output Prediction**
- [ ] Predict: `s = "Hello, World!"` then `s[0]`, `s[-1]`, `s[7:]`, `s[:5]`, `s[::2]`, `s[::-1]`. Explain slicing syntax `[start:stop:step]`.
- [ ] Predict: `"  hello  ".strip()`, `"hello".center(11, "-")`, `"abc".zfill(6)`, `"abc" * 3`, `"a,b,,c".split(",")`, `",".join(["a","b","c"])`.
- [ ] Predict: `"abc" in "abcdef"`, `"xyz" not in "abcdef"`, `"Hello".lower() == "hello"`, `"Hello" == "hello"`.

**Coding**
- [ ] Count vowels, consonants, digits, spaces, and special characters in a user-entered string. Use a single loop.
- [ ] Check if a string is a pangram (contains every letter of the alphabet at least once). Test with: `"The quick brown fox jumps over the lazy dog"`.
- [ ] Reverse words in a sentence without reversing individual characters: `"Hello World"` → `"World Hello"`.
- [ ] Find the longest palindromic substring in a given string. Example: `"babad"` → `"bab"`.
- [ ] Write a Caesar cipher encoder/decoder: shift each letter by N positions, preserve case, leave non-alpha characters unchanged, wrap around Z→A.
- [ ] Implement a simple text compressor: `"aaabbbccdd"` → `"3a3b2c2d"`. Decompress it back.
- [ ] Extract all IPv4 addresses from a multi-line string using only string methods (no `re`). Split on spaces and dots, validate each octet.
- [ ] Write an anagram checker: two words are anagrams if they contain the same characters with the same frequency. `"listen"` and `"silent"` → True.
- [ ] Write a `sanitize_filename(name)` function: remove or replace characters not allowed in filenames (`/ \ : * ? " < > |`), limit length to 255 chars.
- [ ] Format a phone number string: strip non-digits, then format as `+1 (XXX) XXX-XXXX` for 11-digit numbers or `(XXX) XXX-XXXX` for 10-digit numbers.

**Debugging**
- [ ] Fix: a string formatting script that builds a SQL query by concatenation instead of parameterization. Identify the security issue and rewrite it safely.

---

### 1.6 Lists

**Output Prediction**
- [ ] Predict: `a = [1,2,3]; b = a; b.append(4); print(a)`. Then predict with `b = a.copy()`. Explain shallow vs deep copy.
- [ ] Predict: `lst = [1,2,3,4,5]; print(lst[1:4])`, `lst[::2]`, `lst[-3:]`, `lst[::-1]`. No running.
- [ ] Predict: `sorted([3,1,4,1,5], reverse=True)` vs `[3,1,4,1,5].sort(reverse=True)`. What does `sort()` return?

**Coding**
- [ ] Remove duplicates from a list while preserving the original order. Do not use `set()` directly — implement it manually, then compare with the `set` approach.
- [ ] Flatten a nested list of arbitrary depth: `[1, [2, [3, [4]], 5]]` → `[1, 2, 3, 4, 5]`. Use recursion.
- [ ] Given a list of scan results `[(ip, port, status)]`, sort first by IP (numerically), then by port number ascending.
- [ ] Write list comprehensions for: squares of evens 1–20, IPs ending in `.1` from a list, words longer than 4 chars from a sentence, and all `(x,y)` pairs where `x != y` from `range(4)`.
- [ ] Rotate a list left by `n` positions without using slicing twice: `[1,2,3,4,5]` rotated by 2 → `[3,4,5,1,2]`.
- [ ] Merge two sorted lists into one sorted list without using `sorted()` — implement the merge step manually.
- [ ] Given a list of integers, find the two numbers that sum to a target value. Return their indices. Do it in O(n) using a dict.
- [ ] Write `chunk(lst, n)` that splits a list into sub-lists of size n: `chunk([1..10], 3)` → `[[1,2,3],[4,5,6],[7,8,9],[10]]`.

**Debugging**
- [ ] Fix a list-processing function that accidentally modifies the input list (mutable default argument bug + in-place sort on original).

---

### 1.7 Tuples

**Output Prediction**
- [ ] Predict: `t = (1,2,3); t[0] = 99`. Then: `t = ([1,2], [3,4]); t[0].append(99); print(t)`. Explain immutability vs mutability of contents.
- [ ] Predict: `a, *b, c = (1,2,3,4,5); print(a, b, c)`. Then `x, y = y, x` where `x=10, y=20`.

**Coding**
- [ ] Create a tuple of network device info `(hostname, ip, mac, role)`. Unpack it into named variables. Print a formatted summary.
- [ ] Write a function that returns multiple values as a tuple: `(success, result, error_message)`. Call it and unpack correctly.
- [ ] Use a list of tuples as a lookup table for port-to-service mapping. Search by port using next() with a default.
- [ ] Demonstrate a named tuple (`collections.namedtuple`) for storing packet info: src_ip, dst_ip, src_port, dst_port, protocol. Access fields by name.
- [ ] Sort a list of `(ip, port, response_time)` tuples by response time ascending, then by port descending as a tiebreaker.
- [ ] Show that a tuple can be used as a dictionary key but a list cannot. Explain why and give a practical use case.

---

### 1.8 Sets

**Output Prediction**
- [ ] Predict: `s = {1,2,3,3,2,1}; print(s)`. Then `s.add(3); print(s)`. Then `s.discard(99); s.remove(99)` — which one raises an error?
- [ ] Predict: `{1,2,3} | {3,4,5}`, `{1,2,3} & {3,4,5}`, `{1,2,3} - {3,4,5}`, `{1,2,3} ^ {3,4,5}`. State the operation name for each.

**Coding**
- [ ] Given two lists of IP addresses from different scans, find: IPs in both scans, IPs only in scan 1, IPs only in scan 2, and IPs in either scan.
- [ ] Find the common skills between two job postings stored as lists. Use a set for O(1) lookups.
- [ ] Build a deduplicator: given a list of log entries, remove exact duplicates while keeping the first occurrence. Use a set as a seen-tracker.
- [ ] Check if a set of required ports `{80, 443, 22}` is a subset of a set of open ports. Print which required ports are missing.
- [ ] Remove all banned IPs from a list of scan targets efficiently using set difference. Measure time vs list iteration.
- [ ] Explain with code why `frozenset` can be used in a set or as a dict key, but `set` cannot.

---

### 1.9 Dictionaries

**Output Prediction**
- [ ] Predict: `d = {"a":1}; d["b"]; d.get("b"); d.get("b", 0)`. Which raises `KeyError`?
- [ ] Predict: `d = {}; d.setdefault("x", []); d["x"].append(1); d.setdefault("x", []); print(d)`.
- [ ] Predict: `{k:v for k,v in [("a",1),("b",2),("a",3)]}`. Which value does key `"a"` get?

**Coding**
- [ ] Count word frequency in a paragraph using a dictionary. Sort the result by frequency descending and print the top 10 words.
- [ ] Write `merge_dicts(*dicts)` that merges any number of dicts. Later keys overwrite earlier ones. Do not use `{**a, **b}` syntax — implement manually, then show the shorthand.
- [ ] Invert a dictionary `{k:v}` → `{v:k}`. Handle duplicate values by storing them in a list: `{v: [k1,k2,...]}`.
- [ ] Build a nested dictionary for a network scan result: `{ip: {port: {service, status, banner}}}`. Write functions to add, update, and print records.
- [ ] Write a `group_by(lst, key_func)` function: given a list of dicts, group them into a dict-of-lists by a key function. Example: group scan results by OS type.
- [ ] Implement a simple LRU cache using `collections.OrderedDict` with a configurable max size.
- [ ] Use dictionary comprehension to: square all values, filter keys starting with "port\_", and swap keys/values — each in one line.
- [ ] Sort the following dict by value descending using `sorted()` with a `key=` lambda: `{"ssh":22, "http":80, "rdp":3389, "ftp":21}`.

**Debugging**
- [ ] Fix a function that builds a frequency dict from a list but initializes with `dict.fromkeys(lst, [])` — causing all keys to share the same list object.

---

### 1.10 Functions (Advanced)

**Output Prediction**
- [ ] Predict: a closure where `funcs = [lambda x: x*i for i in range(3)]` then `[f(10) for f in funcs]`. Explain and show the fix.
- [ ] Predict: a decorator that wraps a function without `@functools.wraps`. Show `func.__name__` before and after, and explain why `wraps` matters.
- [ ] Predict: stacked decorators `@A @B def f()`. In what order are they applied? In what order do they execute?

**Coding**
- [ ] Implement `@timer` (measures execution time), `@retry(n, delay)` (retries on exception), `@require_role(role)` (checks caller's role), and `@memoize` (caches results). Apply them to sample functions.
- [ ] Write a `compose(*funcs)` function that returns a new function applying each function right-to-left. Then write `pipe(*funcs)` for left-to-right. Demonstrate with string transformations.
- [ ] Build a generator pipeline: `read_lines → filter_errors → parse_fields → enrich → output`. Each stage is a generator. Chain them without intermediate lists.
- [ ] Write `make_rate_limiter(max_calls, period_sec)` using a closure with `nonlocal` state. Returns a function that raises `RateLimitError` if called too often.
- [ ] Implement `partial_apply(func, **fixed_kwargs)` from scratch (like `functools.partial` but kwargs only). Demonstrate currying a scan function.
- [ ] Write a `safe_call(func, *args, default=None, **kwargs)` wrapper that calls `func`, catches any exception, logs it, and returns `default`.

---

## 2. Object-Oriented Programming

### 2.1 Classes & Objects

**Output Prediction**
- [ ] Predict: a class with a class attribute `count = 0` incremented in `__init__`. Create 3 instances. Print `instance.count` vs `ClassName.count`.
- [ ] Predict: `class A: x = []; a = A(); b = A(); a.x.append(1); print(b.x)`. Explain and fix.

**Coding**
- [ ] Create a `NetworkDevice` class with: `hostname`, `ip`, `open_ports` (list), `status`. Methods: `add_port(port)`, `remove_port(port)`, `is_risky()` (True if >5 ports), `__str__`, `__repr__`.
- [ ] Create a `BankAccount` class with: account number, holder name, balance. Methods: `deposit(amount)`, `withdraw(amount)` (raise `InsufficientFundsError` if needed), `transfer(other_account, amount)`, `statement()` (prints last 10 transactions), `__str__`.
- [ ] Create a `Student` class with name, roll number, marks dict (subject → mark). Class method `from_csv(line)` to create from a CSV string. Static method `is_pass(marks)`. Property `gpa`. `__eq__` compares by roll number.

---

### 2.2 Inheritance & Polymorphism

**Coding**
- [ ] Create hierarchy: `Vehicle → Car, Motorcycle, Truck`. Each has `fuel_type`, `speed_limit`. Override `describe()`. Demonstrate polymorphism by calling `describe()` on a mixed list via a loop.
- [ ] Create `Shape → Circle, Rectangle, Triangle`. Each implements `area()`, `perimeter()`, `__str__`. Create a list of shapes and print total area.
- [ ] Create `Packet → TCPPacket, UDPPacket, ICMPPacket`. Each has `parse(raw_bytes)` and `summarize()`. Override appropriately.
- [ ] Demonstrate multiple inheritance: `Flyable`, `Swimmable`, `Duck(Flyable, Swimmable)`. Show MRO with `Duck.__mro__`. Explain the diamond problem.
- [ ] Use `super()` correctly in multilevel inheritance: `A → B → C`. Each `__init__` takes different arguments. Show that all `__init__` methods run.

---

### 2.3 Encapsulation & Abstraction

**Coding**
- [ ] Refactor `BankAccount` to use name mangling (`__balance`). Provide a `balance` property (read-only). Show that `account.__balance` fails outside the class.
- [ ] Use the `abc` module to create an abstract base class `Scanner` with abstract methods `scan()`, `report()`, `close()`. Create `TCPScanner` and `UDPScanner` that implement them.
- [ ] Add `@property`, `@property.setter`, and `@property.deleter` to a `Config` class that validates values on assignment (e.g., port must be 1–65535, timeout must be > 0).

---

### 2.4 Magic Methods

**Output Prediction**
- [ ] Predict the output when `__add__`, `__len__`, `__contains__`, `__iter__`, and `__getitem__` are all defined on a custom `PortList` class.

**Coding**
- [ ] Build a `PortList` class that wraps a list of ports and implements: `__len__`, `__contains__`, `__add__` (merge), `__iter__`, `__getitem__`, `__str__`, `__repr__`, `__eq__`, `__lt__` (compare by count).
- [ ] Build a `Config` class using `__getattr__`, `__setattr__`, and `__delattr__` for attribute access. Store all config in an internal dict.
- [ ] Implement a `Vector` class with `__add__`, `__sub__`, `__mul__`, `__abs__`, `__neg__`, `__eq__`, and `__repr__`. Test with network throughput vectors.

---

### 2.5 Composition, Dataclasses & Design Patterns

**Coding**
- [ ] Use composition (not inheritance): `Scanner` has-a `Logger`, has-a `ReportGenerator`, has-a `RateLimiter`. Show how this is more flexible than inheritance.
- [ ] Use `@dataclass` to create: `ScanResult(ip, port, service, status, response_time)`. Add `__post_init__` validation. Add `order=True` for sorting. Compare with plain class version.
- [ ] Implement the **Singleton** pattern for a `Config` class. Verify only one instance is ever created.
- [ ] Implement the **Observer** pattern: a `Scanner` (subject) notifies `Logger`, `Alerter`, and `ReportWriter` (observers) when a port is found open.
- [ ] Implement the **Factory** pattern: `PacketFactory.create(packet_type)` returns TCP, UDP, or ICMP packet objects.
- [ ] Implement the **Strategy** pattern: a `Formatter` class accepts a formatting strategy (JSON, CSV, plain text) at runtime.

**Debugging**
- [ ] Fix a class that incorrectly uses `__init__` with a mutable default argument, accidentally shares state between instances, and has `__str__` returning `None`.

---

## 3. File Handling

### 3.1 Text & Binary Files

**Output Prediction**
- [ ] Predict: open a file in `r+` mode, write "Hello", seek(0), read all. What does the file contain? What does read() return?
- [ ] Predict: `open("x.txt","x")` twice. What happens on the second call?

**Coding**
- [ ] Write and read a scan log file. Use `with open(...)`. Write 10 log lines with timestamps. Read them back line by line, number each, and print lines containing "OPEN".
- [ ] Build a binary file inspector: open a file in `rb` mode, read the first 16 bytes, print as hex dump (two hex digits per byte, 8 per row), and identify the file type by magic bytes.
- [ ] Implement a `tail(filename, n=10)` function that returns the last `n` lines of a file efficiently without reading the entire file into memory first.

---

### 3.2 CSV, JSON, XML, YAML

**Coding**
- [ ] Read a CSV with `csv.DictReader`. Validate required columns exist. Calculate average and max values for numeric columns. Write a filtered CSV of rows where status == "OPEN".
- [ ] Load a JSON scan report, add new results, update a summary counter, and write it back. Handle `json.JSONDecodeError`. Pretty-print with 2-space indentation.
- [ ] Parse an nmap-style XML output: extract all hosts, ports, services, and states. Print a formatted table. Write a JSON summary.
- [ ] Load a YAML config with `yaml.safe_load`. Validate required keys. Write an updated YAML config with a new section added. Explain why `safe_load` is mandatory for untrusted input.
- [ ] Build a "universal converter": accepts any of CSV, JSON, XML, or YAML as input and outputs validated JSON. Handle missing/malformed fields gracefully.

---

### 3.3 pathlib & Context Managers

**Coding**
- [ ] Rewrite a script that uses `os.path.join`, `os.path.exists`, `os.listdir`, and `os.path.splitext` entirely using `pathlib.Path`.
- [ ] Use `Path.glob("**/*.log")` to recursively find all log files in a directory, sort by modification time, and print size and path.
- [ ] Build a custom context manager class `SafeWriter` that: creates a temp file, writes to it, on success renames to final name, on failure deletes temp and re-raises.
- [ ] Build a `@contextmanager` version of `SafeWriter` using `contextlib.contextmanager` and `yield`.

**Debugging**
- [ ] Fix: a script that opens a file without `with`, forgets to close it, reads from a file opened in `w` mode, and uses `yaml.load()` without a Loader argument.

---

## 4. Modules, Packages & Environments

**Output Prediction**
- [ ] Predict `__name__` inside a module when run directly vs when imported. Show how `if __name__ == "__main__"` prevents code from running on import.
- [ ] Predict what `from module import *` imports when `__all__` is defined vs when it is not.

**Coding**
- [ ] Create a package `sectool/` with sub-packages `network/`, `crypto/`, `reports/`. Write an `__init__.py` that re-exports key functions. Demonstrate absolute and relative imports.
- [ ] Use `importlib.import_module()` to build a plugin loader: scan a `plugins/` directory, import each `.py` file, call its `run()` function if it exists, and handle `ImportError` gracefully.
- [ ] Write a script using only standard library modules that: lists all `.py` files in CWD, prints Python version and platform, generates 10 random ports, and measures time to sum 10 million numbers.
- [ ] Create a `requirements.txt` with pinned versions for: `requests>=2.28`, `paramiko>=3.0`, `cryptography>=41.0`, `PyYAML>=6.0`, `pytest` (dev-only). Explain each version constraint style.
- [ ] Write a Python "Environment Auditor": list all installed packages, check against a required list with minimum versions, flag missing and outdated packages.

**Debugging**
- [ ] Diagnose and fix: a circular import between `a.py` and `b.py`, a `ModuleNotFoundError` caused by wrong `sys.path`, and an `ImportError` from a misspelled attribute name.

---

## 5. Exception Handling

**Output Prediction**
- [ ] Predict this flow: `try → raises ValueError → except ValueError → else → finally`. Which blocks run?
- [ ] Predict: `raise RuntimeError("outer") from ValueError("inner")`. What are `__cause__` and `__context__`?

**Coding**
- [ ] Write a `safe_connect(host, port, timeout)` that catches `socket.timeout`, `ConnectionRefusedError`, `OSError`, `socket.gaierror`, and a catch-all. Log each differently. Return a structured result dict.
- [ ] Design a custom exception hierarchy: `ToolkitError → NetworkError(ConnectionTimeoutError, ConnectionRefusedError), AuthError(InvalidCredentialsError, MFARequiredError), ScanError(InvalidTargetError)`. Each stores context (ip, port, timestamp).
- [ ] Use `assert` to validate scan config fields. Then explain why assertions should NOT replace input validation in production and rewrite using explicit `if/raise`.
- [ ] Configure `logging`: two handlers (StreamHandler at WARNING, FileHandler at DEBUG), a timestamp formatter, and log rotation (max 5MB, 3 backups). Write 5 log events at different levels.
- [ ] Build a `NetworkConnection` context manager (`__enter__`/`__exit__`) that: connects on enter, disconnects in finally, logs exceptions, and optionally suppresses them based on a parameter.

**Debugging**
- [ ] Fix: unreachable `except` clause after a bare `except`, `return False` inside `finally` (suppresses exceptions), a silent `except: pass` hiding a bug, and a `logging.basicConfig(level="debug")` wrong string level.

---

## 6. NumPy

### 6.1 Array Creation & Attributes

**Output Prediction**
- [ ] Predict: multiply a Python list by 2 vs a NumPy array by 2. What is the type and value of each result?
- [ ] Predict: `np.array([1,2,3]) + np.array([4,5,6])` vs `[1,2,3] + [4,5,6]`. Show the difference.
- [ ] Predict: `arr = np.array([[1,2,3],[4,5,6]]); print(arr.ndim, arr.shape, arr.size, arr.dtype, arr.itemsize, arr.nbytes)`.

**Coding**
- [ ] Create these arrays: 1D integers, 1D floats, a 3×3 identity matrix, a 4×4 zero matrix, a 2×3 matrix of ones, an arange from 0 to 50 step 5, and linspace of 10 values from 0 to 1.
- [ ] Create a 3D array of shape (2,3,4). Print its shape, ndim, size. Explain what each dimension represents in a real dataset context.
- [ ] Create a reproducible array of 20 random integers between 10 and 100 using `np.random.default_rng(seed=42)`. Find mean, median, std, min, max.
- [ ] Convert a Python list of IP last-octets to a NumPy array. Change dtype to `uint8`. Explain why `uint8` is appropriate for octets.

---

### 6.2 Operations & Broadcasting

**Output Prediction**
- [ ] Predict: `a = np.array([[1],[2],[3]]); b = np.array([10,20,30]); print(a + b)`. Draw the broadcasting diagram.
- [ ] Predict: `np.array([1,2,3]) + np.array([1,2])`. What error is raised? Why?

**Coding**
- [ ] Given a salary array, perform: add ₹5,000 bonus, apply 10% tax, give a 20% raise to salaries below ₹40,000, and identify salaries above ₹50,000. Do all steps with vectorized operations.
- [ ] Add a (3,1) column vector to a (1,4) row vector. Show the resulting shape and values. Explain broadcasting rules.
- [ ] For a 2D marks matrix (students × subjects), calculate: row sums (total per student), column means (average per subject), and the overall class average.
- [ ] Normalize a 1D array to [0,1] range. Handle the edge case where all values are equal (avoid division by zero).
- [ ] Round an array of floats to 2 decimal places. Compare `np.round()`, `np.floor()`, `np.ceil()`, and `np.trunc()` with negative numbers.

---

### 6.3 Indexing, Slicing & Filtering

**Output Prediction**
- [ ] Predict: `arr = np.arange(10); print(arr[2:8:2])`, `print(arr[-3:])`, `print(arr[::-1])`, `print(arr[[0,3,7]])`.
- [ ] Predict: `m = np.arange(9).reshape(3,3); print(m[1,:]); print(m[:,2]); print(m[0:2, 1:3])`.

**Coding**
- [ ] Using Boolean indexing on a salary array: print salaries above ₹40,000, give a ₹5,000 raise to those below ₹30,000, and zero out any salary above ₹100,000.
- [ ] Use fancy indexing: given an array of marks, extract marks at indices [0,2,4], replace marks at indices [1,3] with 0.
- [ ] Filter a 2D student-marks array: find all students with a score > 80 in subject column 2. Print their row indices and scores.
- [ ] Use `np.where()` to replace all negative values with 0 and all values > 100 with 100 in a single expression.
- [ ] Extract a rectangular sub-matrix from a 5×5 matrix: rows 1–3, columns 2–4.

---

### 6.4 Reshaping, Stacking & Linear Algebra

**Coding**
- [ ] Reshape a 1D array of 12 elements into (3,4), (4,3), (2,6), and (2,2,3). Use `-1` as a wildcard dimension.
- [ ] Stack two 3×4 arrays vertically (`vstack`) and horizontally (`hstack`). Then use `np.concatenate` with `axis=0` and `axis=1`. Confirm shapes.
- [ ] Compute: matrix multiplication (`@` or `np.dot`), element-wise multiplication, transpose, determinant, inverse, and eigenvalues for a 3×3 matrix.
- [ ] Save a NumPy array to `.npy` and `.npz` formats. Load them back. Verify shape and dtype match the original.
- [ ] Write a function that receives a numeric array and returns a stats dict: `{count, mean, median, std, min, max, q25, q75}`.

---

### 6.5 Applied NumPy

**Coding**
- [ ] Build a payroll script: start with 20 employee salaries (random). Apply: 20% raise for all, flag those above ₹50,000, give extra ₹3,000 to those below ₹40,000, deduct 10% tax from everyone. Print before/after comparison.
- [ ] Build a student result analyzer: 30 students × 5 subjects marks matrix. Calculate: total per student, average per subject, pass/fail (pass if all subjects ≥ 40 and total ≥ 250), rank students by total, top 5.
- [ ] Compare performance: sum of 1 million numbers using Python loop vs NumPy vectorization. Time both with `time.time()`. Print speedup ratio.
- [ ] Implement a simple moving average on a 1D array (e.g., network latency readings). Window size = 5. Use only NumPy operations, no loops.

---

## 7. Pandas

### 7.1 Series & DataFrame Basics

**Output Prediction**
- [ ] Predict: `s = pd.Series([10,20,30], index=["a","b","c"]); print(s["b"]); print(s[1])`. Which uses label? Which uses position? What is the difference?
- [ ] Predict: `df = pd.DataFrame({"A":[1,2], "B":[3,4]}); print(df["A"])` vs `print(df.A)`. When does the second form fail?

**Coding**
- [ ] Create a DataFrame from: a list of dicts, a dict of lists, a list of tuples with column names. Print `shape`, `dtypes`, `info()`, `describe()`, `head(3)`, `tail(3)`.
- [ ] Load a CSV with `pd.read_csv`. Inspect: shape, column names, dtypes, null counts per column. Print first and last 5 rows. Print a random sample of 10 rows.
- [ ] Explain and demonstrate the difference between `loc`, `iloc`, and boolean indexing. Show a case where they give different results.

---

### 7.2 Selection, Filtering & Sorting

**Coding**
- [ ] Select multiple columns. Filter rows where profit > 5000. Filter rows where age > 40 AND category == "Electronics". Use `query()` for the same.
- [ ] Sort a DataFrame by category ascending, then by sales descending as a secondary sort. Use `sort_values()` with `ascending=[True, False]`.
- [ ] Use `nlargest(5, "profit")` and `nsmallest(5, "discount")`. Show the result and explain when these are better than sort+head.
- [ ] Use `isin()` to filter rows where category is in `["Electronics", "Books"]`. Then use `~isin()` to exclude them.
- [ ] Add a computed column `profit_margin = profit / sales * 100`. Add a `risk_level` column: "HIGH" if open_ports > 5, "LOW" otherwise. Drop a column.

---

### 7.3 Aggregation & GroupBy

**Coding**
- [ ] Group a sales DataFrame by category. Calculate: total sales, total profit, average discount, max rating, count of orders per group. Display as a clean table.
- [ ] Use `agg()` with a dict to apply different aggregations to different columns in a single `groupby` call.
- [ ] Find the category with the highest total profit. Find the customer with the most orders. Find the month with the most sales (parse date column first).
- [ ] Use `transform()` to add a column showing each row's sales as a percentage of its category's total sales.
- [ ] Use `pivot_table()` to show average profit per category × region. Set `fill_value=0` for missing combinations.

---

### 7.4 Merging, Joining & Concatenating

**Coding**
- [ ] Create two DataFrames: orders and customers (shared key: `customer_id`). Perform inner, left, right, and outer joins. Explain which rows are kept in each.
- [ ] Use `pd.concat()` to stack two DataFrames vertically. Handle mismatched columns (some in A not in B). Use `ignore_index=True`.
- [ ] Merge three DataFrames sequentially (orders → customers → products). Print shape after each merge to track row count changes.
- [ ] Demonstrate `merge()` with `on=`, `left_on=`/`right_on=`, and `suffixes=` for overlapping column names.

---

### 7.5 Missing Values & Data Cleaning

**Coding**
- [ ] Check for missing values with `isnull().sum()`. Fill numeric NaN with column median. Fill categorical NaN with `"Unknown"`. Drop rows where more than 50% of columns are NaN.
- [ ] Detect and remove duplicate rows. Show count before and after. Explain `keep="first"`, `keep="last"`, and `keep=False`.
- [ ] Fix data types: parse a date column with `pd.to_datetime()`. Convert a string column that should be numeric (handle non-numeric strings with `errors="coerce"`).
- [ ] Rename columns to snake_case. Strip whitespace from all string columns. Standardize categorical values (e.g., `"OPEN"`, `"open"`, `"Open"` → `"open"`).

---

### 7.6 String Methods, Apply & Lambda

**Coding**
- [ ] Use pandas string methods (`.str.`): extract domain from email column, check if IP starts with "192.", count characters, split a full-name column into first/last.
- [ ] Use `apply()` with a custom function to classify each row's risk level based on multiple column values. Compare with a vectorized approach.
- [ ] Use `map()` to replace category codes with full names using a dictionary. Show the difference between `map()`, `apply()`, and `applymap()` / `map()` (DataFrame-level).
- [ ] Use `pd.cut()` to bin a continuous sales column into quartile ranges. Use `pd.qcut()` for equal-frequency bins. Show value counts for each.

---

### 7.7 Datetime & Time Series

**Coding**
- [ ] Parse a date column. Extract: year, month, day, day-of-week, quarter. Add a `days_since_epoch` column. Filter rows from the last 30 days.
- [ ] Resample daily data to weekly and monthly totals using `resample()`. Plot would be the next step — just produce the aggregated DataFrame here.
- [ ] Calculate the number of days between two date columns (e.g., order date and delivery date). Find orders taking more than 7 days.

---

### 7.8 Business Case Studies

**Coding**
- [ ] **Amazon Sales Analysis:** Load the dataset. Answer: (a) Which category has highest revenue? (b) Which product has the most orders? (c) What is average profit margin by category? (d) Which age group spends the most? (e) Are high-discount products more or less profitable?
- [ ] **Employee Churn Analysis:** Given a CSV with `employee_id, department, salary, years, left`. Find: churn rate by department, average salary of those who left vs stayed, and which salary band has the highest churn.
- [ ] **Security Log Analysis:** Given a log CSV with `timestamp, src_ip, dst_port, status`. Find: top 10 source IPs, peak hour of activity, IPs with >50 failed attempts (status!=200), and generate a JSON report.
- [ ] Write a reusable `generate_report(df, title)` function that prints: shape, null counts, numeric summary, top 5 rows, and category breakdown for all object columns.

---

## 8. Networking Programming

### 8.1 Foundations

**Conceptual / Code Reading**
- [ ] Explain: IP addresses, ports, sockets, TCP 3-way handshake, UDP connectionlessness, the OSI model's top 4 layers, and where Python socket operations sit.
- [ ] Trace a complete HTTPS request: DNS lookup → TCP connect → TLS handshake → HTTP request → response → connection close. Name which Python library handles each step.
- [ ] Explain: NAT, firewall rules, proxy servers, load balancers, CDNs. Give a Python-observable symptom of each when making HTTP requests.
- [ ] Compare `socket.AF_INET`, `socket.AF_INET6`, `socket.SOCK_STREAM`, `socket.SOCK_DGRAM`. Give a use case for each combination.

---

### 8.2 Socket Programming (TCP)

**Coding**
- [ ] Build a TCP echo server on `127.0.0.1:9000` and a matching client. Server echoes everything back. Both handle clean shutdown.
- [ ] Extend the TCP server to handle multiple clients using threads. Each client gets its own thread. Server prints which client sent what.
- [ ] Add to the TCP server: connection timeout, message size limit (reject > 4096 bytes), and a simple length-prefix framing protocol so messages aren't split.
- [ ] Build a local TCP chat server: clients connect, send a username, then broadcast messages to all other connected clients. Handle disconnections gracefully.
- [ ] Use `selectors` to build a non-blocking TCP server that handles multiple connections without threads.

---

### 8.3 Socket Programming (UDP)

**Coding**
- [ ] Build a UDP client and server on localhost. Client sends 5 messages, server echoes them back. Show that no connection state is maintained.
- [ ] Demonstrate UDP unreliability: send 100 messages rapidly, count how many arrive. Add a sequence number to each message so the receiver can detect gaps.

---

### 8.4 HTTP, REST APIs & DNS

**Coding**
- [ ] Use `socket` to make a raw HTTP/1.0 GET request to `127.0.0.1` (your own server). Parse status code and headers manually without using `requests`.
- [ ] Use `ssl.wrap_socket` (or `ssl.create_default_context`) to inspect the certificate of an HTTPS server you control. Print subject, issuer, and expiry date.
- [ ] Query DNS records using `socket.getaddrinfo()`. Compare A and AAAA results. Use `socket.gethostbyname()` and explain when it's insufficient.

---

### 8.5 Threading, Multiprocessing & asyncio

**Output Prediction**
- [ ] Predict the approximate output ordering of a script that starts 5 threads that each sleep a random 0–1s then print their index. Is the order guaranteed?

**Coding**
- [ ] Write a threaded port scanner: divide a port range (1–1024) across 10 threads. Use a `queue.Queue` for work distribution and a lock for printing results.
- [ ] Use `multiprocessing.Pool.map()` to scan 4 different IP address ranges in parallel (simulated). Compare with the sequential approach.
- [ ] Use `asyncio` + `asyncio.open_connection()` to check if a list of (host, port) pairs are open. Limit concurrency to 20 with `asyncio.Semaphore`.
- [ ] Explain: when to use threading vs multiprocessing vs asyncio. Which is best for: port scanning, CPU-intensive packet parsing, waiting for many API responses?

---

## 9. requests

**Output Prediction**
- [ ] Predict: `r = requests.get("https://httpbin.org/get")`. What type is `r`? What are `r.status_code`, `r.headers`, `r.text`, `r.json()`, `r.content`?

**Coding**
- [ ] Make GET, POST, PUT, PATCH, and DELETE requests to `https://httpbin.org`. Print status code, response time, and the request you sent reflected back.
- [ ] Use a `Session` object: set a base `User-Agent` header and an `Authorization: Bearer TOKEN` header. Make 3 requests and show the header is sent each time.
- [ ] Handle authentication: Bearer token (env variable), HTTP Basic auth, and an API key in a query parameter. Never hardcode credentials.
- [ ] Implement pagination: a mock API returns 100 items across 10 pages. Fetch all pages, combine results, and stop when `next` is null.
- [ ] Add exponential backoff: retry on 429 and 5xx status codes, respect `Retry-After` header, and give up after 5 attempts.
- [ ] Upload a file with `requests.post()` using `files=`. Download a large file in chunks using `stream=True` and show download progress.
- [ ] Handle all request errors: `requests.exceptions.Timeout`, `ConnectionError`, `HTTPError`, and `TooManyRedirects`. Return a structured error dict.
- [ ] Use `requests.get(..., verify=False)` — explain the security risk. Then show the correct way using a custom CA bundle.
- [ ] Send a JSON payload in a POST body. Compare `json=` parameter vs `data=json.dumps(...)` with a `Content-Type` header. Show the difference in what `httpbin` reflects.
- [ ] Build a reusable `APIClient` class: base URL, auth header, session, timeout, retry, and `get(path, params)`, `post(path, body)` methods.

---

## 10. BeautifulSoup (bs4)

**Coding**
- [ ] Parse a saved HTML file. Extract: page title, all `<h1>`–`<h3>` headings, all `<a>` href links (absolute only), all images with their `alt` text, and the meta description.
- [ ] Parse an HTML table into a list of dicts using `DictReader`-style extraction (header row = keys, data rows = values). Export as CSV.
- [ ] Find all forms on a page: extract each form's `action`, `method`, and all input fields (name, type, placeholder). This is foundational for security testing of your own apps.
- [ ] Use CSS selectors (`.select()`) to find: all elements with class `"error"`, all `<input type="password">`, all `<a>` inside `<nav>`.
- [ ] Build a polite scraper for a site you control: respect `robots.txt`, add 1-second delay between requests, handle 404 and 5xx gracefully, deduplicate URLs, and limit crawl depth to 3.
- [ ] Parse pagination: find the "Next" link on each page, follow it, and collect all article titles across pages (use saved HTML files for practice).
- [ ] Scrape a table of CVE data from a local HTML file: extract CVE ID, CVSS score, description, and affected product. Sort by score and save as JSON.

**Debugging**
- [ ] Fix a scraper that uses `soup.find("table").find_all("tr")[0]` on a page where the first `<tr>` is inside a `<thead>` and the actual header is nested differently.

---

## 11. Selenium

**Coding**
- [ ] Open a local HTML form, fill each field (text, dropdown, checkbox, radio, file), submit, and verify a success message appears. Use explicit waits — no `time.sleep()`.
- [ ] Take a full-page screenshot of a local web page. Resize the browser to mobile dimensions and take another screenshot. Compare.
- [ ] Wait for a dynamically loaded element: use `WebDriverWait` + `ExpectedConditions.visibility_of_element_located`. Explain why implicit waits are inferior.
- [ ] Automate login to a local test application: navigate to login page, fill credentials from environment variables, submit, verify you are redirected to the dashboard.
- [ ] Capture all browser console errors and network errors from a local page. Print them in a test report format.
- [ ] Extract a table that is rendered by JavaScript (not in initial HTML). Show that `requests` + BeautifulSoup alone cannot do this, but Selenium can.
- [ ] Write a Page Object Model (POM) class for a local login page. Separate locators from actions. Call it from a test function.

---

## 12. socket Library

**Coding**
- [ ] Create a TCP port checker: given a list of `(host, port)` pairs, check each with a 1-second timeout. Return `{host: {port: "open"/"closed"/"filtered"}}`.
- [ ] Implement a banner grabber for your own services: connect, wait 2 seconds, read response, decode, return. Handle timeout, refused, and OS errors.
- [ ] Build a multi-threaded port scanner: scan ports 1–1024 on localhost using 20 threads. Print open ports sorted numerically.
- [ ] Use `socket.create_server()` (Python 3.8+) to create a TCP server. Compare with the traditional `socket()`, `bind()`, `listen()`, `accept()` sequence.
- [ ] Implement proper message framing over TCP: prefix each message with a 4-byte big-endian length header. Write `send_message(sock, data)` and `recv_message(sock)`.
- [ ] Create a UDP broadcast sender on localhost. Create a listener that receives broadcasts. Explain where broadcasting is useful.
- [ ] Use `socket.setblocking(False)` and catch `BlockingIOError`. Explain non-blocking sockets and when you'd prefer `selectors` instead.
- [ ] Get and set socket options: `SO_REUSEADDR`, `SO_RCVBUF`, `TCP_NODELAY`. Explain what each does and when to use it.

---

## 13. dnspython

**Coding**
- [ ] Query A and AAAA records for a domain you own. Print all returned IPs. Handle `NXDOMAIN` and `NoAnswer` exceptions without crashing.
- [ ] Query MX records: sort by priority, print each mail server in order. Explain what MX priority means.
- [ ] Query NS records for a domain: list all authoritative nameservers. Do a follow-up A record lookup for each nameserver.
- [ ] Query TXT records: extract SPF, DKIM, and DMARC records if present. Parse the SPF record and list all authorized IP ranges.
- [ ] Do a PTR (reverse DNS) lookup for a given IP. Convert IP to PTR format manually (e.g., `1.2.3.4` → `4.3.2.1.in-addr.arpa`). Compare `dns.reversename.from_address()`.
- [ ] Query SOA record: extract primary nameserver, admin email, serial number, refresh, retry, expire, and minimum TTL.
- [ ] Write `dns_enum(domain)` that queries all record types (A, AAAA, MX, NS, TXT, SOA, CNAME) and returns a structured dict. Handle each type's exceptions independently.
- [ ] Use a custom DNS resolver (`dns.resolver.Resolver`) pointing to `8.8.8.8`. Set timeout and lifetime. Compare results with the system resolver.

---

## 14. Scapy

> ⚠️ All Scapy exercises must use offline PCAP files or an isolated lab. Never transmit crafted packets on networks you don't own.

**Output Prediction**
- [ ] Predict: `from scapy.all import IP, TCP; pkt = IP(dst="1.2.3.4")/TCP(dport=80); print(pkt.summary())`. What does `pkt[TCP].dport` return?

**Coding**
- [ ] Build an Ethernet/IP/TCP packet manually. Set src/dst IP, src/dst port, TCP flags (SYN). Print the packet's layers and each field's value using `.show()`.
- [ ] Load a PCAP file with `rdpcap()`. Print: total packet count, unique src IPs, unique dst IPs, protocol distribution (TCP/UDP/ICMP/Other).
- [ ] Extract all TCP SYN packets from a PCAP. Print src IP, dst IP, dst port for each. Count unique destination ports — this reveals what was being scanned.
- [ ] Reconstruct HTTP request lines from a PCAP: filter TCP packets with dst port 80, extract the `Raw` layer payload, decode as UTF-8, print lines starting with GET/POST/PUT.
- [ ] Count TCP flag combinations in a PCAP: SYN, SYN-ACK, ACK, FIN-ACK, RST. Build a frequency table.
- [ ] Extract all DNS queries from a PCAP: get query names and query types. List the top 10 queried domains.
- [ ] Use `sniff(count=10, prn=lambda p: p.summary(), filter="tcp", iface="lo")` on your loopback. What does each parameter do?
- [ ] Write a packet parser that reads a PCAP and outputs a CSV: `timestamp, src_ip, dst_ip, protocol, src_port, dst_port, length, flags`.

---

## 15. PyShark

> ⚠️ All PyShark exercises must use offline PCAP files or a loopback interface you control.

**Coding**
- [ ] Open a PCAP with `pyshark.FileCapture()`. Iterate over packets. Print layer names, src/dst IPs, and transport-layer port for each packet.
- [ ] Apply a display filter: load only `tcp.port == 80` packets from a PCAP. Compare with loading all and filtering in Python.
- [ ] Extract HTTP request methods, URIs, and response codes from a PCAP containing HTTP traffic. Print as a table.
- [ ] Count packets by protocol. Build a `{protocol: count}` dict. Print sorted by count descending.
- [ ] Extract DNS queries from a PCAP using PyShark. Compare the output format with the same task done in Scapy.
- [ ] Use `pyshark.LiveCapture(interface="lo")` to capture 20 packets from the loopback. Print a summary of each.
- [ ] Write a PCAP summary report: total packets, duration, top 5 talkers (by packet count), top 5 destination ports, and protocol breakdown. Export as JSON.

---

## 16. cryptography

**Output Prediction**
- [ ] Predict: `from cryptography.fernet import Fernet; key=Fernet.generate_key(); f=Fernet(key); token=f.encrypt(b"hello"); print(token)`. Will two runs produce the same token? Why?

**Coding**
- [ ] Generate a SHA-256 hash of a string. Then of a file (read in chunks). Verify a file against a known hash. Explain why you can't reverse a hash.
- [ ] Use Fernet (symmetric encryption): generate a key, encrypt a plaintext, decrypt it. Then tamper with 1 byte of the ciphertext and show that decryption fails with `InvalidToken`.
- [ ] Use AES-GCM: generate a key and nonce, encrypt plaintext with an authenticated additional data (AAD) string, decrypt, and verify the AAD. Show that changing the AAD breaks decryption.
- [ ] Generate RSA key pair (2048-bit). Encrypt a message with the public key. Decrypt with the private key. Explain why RSA is not used for bulk data.
- [ ] Generate an RSA key pair. Sign a message with the private key. Verify the signature with the public key. Tamper with the message and show verification fails.
- [ ] Derive a key from a password using PBKDF2HMAC with SHA-256, a random salt, and 600,000 iterations. Store the salt alongside the derived key. Show why the salt must be stored.
- [ ] Parse an X.509 certificate (PEM format): print subject, issuer, serial number, not_valid_before, not_valid_after, and public key type/size. Check if the cert is currently valid.
- [ ] Implement a "password vault" prototype: store encrypted entries (service, username, encrypted_password) in a JSON file. The encryption key is derived from a master password + stored salt.

---

## 17. Paramiko

> ⚠️ Only connect to SSH servers you own or have explicit written authorization to access.

**Coding**
- [ ] Connect to an SSH server you administer using key-based authentication (load private key from a protected path). Run `uname -a`, `whoami`, `uptime`. Print output and stderr separately.
- [ ] Run a series of commands and capture their exit codes. Fail fast if a command returns non-zero. Return a structured result dict for each command.
- [ ] Use `SSHClient.exec_command()` with a timeout. Handle `socket.timeout` and `paramiko.AuthenticationException` cleanly.
- [ ] Use SFTP: upload a local test file to a remote path, verify it with a size check, download it back, and compare checksums. Then delete the remote copy.
- [ ] Use `SCPClient` or SFTP to recursively transfer a directory to a remote server. Handle permissions errors.
- [ ] Load a `known_hosts` file and use `RejectPolicy`. Explain what happens when the host key is missing vs when it doesn't match. Why is `AutoAddPolicy` dangerous?
- [ ] Use `SSHClient.invoke_shell()` to open an interactive shell session. Send commands and read output in a loop. Handle the `select` or timeout pattern.

---

## 18. Regular Expressions (re)

### 18.1 Fundamentals

**Output Prediction**
- [ ] Predict: `re.match(r"\d+", "123abc")` vs `re.search(r"\d+", "abc123")` vs `re.fullmatch(r"\d+", "123abc")`. Which ones match? What do `.group()` and `.span()` return?
- [ ] Predict: `re.findall(r"\b\w{4}\b", "This is test code here")`. Explain `\b` and `\w`.
- [ ] Predict: `re.sub(r"\d{4}", "****", "Card: 4111 1111 1111 1111")`. Then `re.sub(r"(\d{4}\s){3}", lambda m: "**** "*3, ...)`.

**Coding**
- [ ] Write and test regex patterns for:
  - IPv4 address (strict: 0–255 per octet)
  - IPv6 address (full and compressed forms)
  - Email address (RFC-compliant simplified version)
  - URL (http/https, optional path and query)
  - MAC address (both `:` and `-` separators)
  - MD5 hash (32 hex chars)
  - SHA-256 hash (64 hex chars)
  - CIDR notation (IP/prefix)
  - Date formats: `YYYY-MM-DD` and `DD/MM/YYYY`
  - Credit card number (Visa, Mastercard pattern)

- [ ] Use named groups (`(?P<name>...)`) to parse an Apache log line into: `ip`, `timestamp`, `method`, `path`, `status`, `size`.
- [ ] Use `re.VERBOSE` (multi-line mode) to write a readable regex for parsing an email address. Add comments for each part.
- [ ] Explain and demonstrate: greedy vs lazy quantifiers (`*` vs `*?`, `+` vs `+?`). Show a case where greedy matching causes an unexpected result in HTML parsing.

---

### 18.2 Extraction & Validation

**Coding**
- [ ] Write an IOC extractor: given a block of threat intelligence text, extract all IPs, domains, URLs, file hashes (MD5/SHA256), and CVE IDs. Deduplicate and print each category.
- [ ] Write a log anonymizer: given a web server log, replace all IPs with `[REDACTED_IP]`, all email addresses with `[REDACTED_EMAIL]`, and all tokens matching `Bearer [A-Za-z0-9]{32,}` with `[REDACTED_TOKEN]`.
- [ ] Write a config file parser using regex: given an `.ini`-style file, extract all `key = value` pairs under each `[section]` header.
- [ ] Build an email header parser: given raw email headers as a string, extract `From`, `To`, `Subject`, `Date`, `Message-ID`, and all `Received` lines.

**Debugging**
- [ ] Fix a regex that's supposed to match IPv4 addresses but also matches `999.999.999.999`. Rewrite it to validate each octet is 0–255.

---

## 19. JSON, XML, CSV, YAML, urllib.parse

### JSON
- [ ] Load, modify, and write back a JSON config file. Handle `JSONDecodeError`. Use `json.dumps()` with `indent=2` and `sort_keys=True`.
- [ ] Write `flatten_json(nested_dict)` that converts `{"a": {"b": {"c": 1}}}` to `{"a.b.c": 1}`. Handle lists by using `a.0.b` notation.
- [ ] Validate a JSON object against a required schema: check required keys exist, values have correct types, and numeric values are within range. Return a list of validation errors.

### XML
- [ ] Parse an nmap XML output file: extract all hosts with status "up", their IPs, and open ports with services.
- [ ] Create an XML document from a Python dict. Use `xml.etree.ElementTree`. Write it with proper indentation.
- [ ] Explain XXE (XML External Entity) injection. Show a vulnerable XML parse call and the safe alternative.

### CSV
- [ ] Use `csv.DictReader` to read a scan results CSV. Detect missing required columns and report their names. Skip rows with empty required fields.
- [ ] Write a CSV normalizer: read a CSV where values may have extra quotes, mixed case, and leading/trailing spaces. Clean and write a normalized output.

### YAML
- [ ] Build a YAML config validator: given a schema dict (required keys + expected types), validate a loaded YAML config. Report all missing/wrong-type fields.
- [ ] Explain the difference between `yaml.safe_load()` and `yaml.load()`. Demonstrate why loading untrusted YAML with `yaml.load()` is dangerous (at a conceptual level).

### urllib.parse
- [ ] Parse a URL into components: scheme, netloc, path, params, query dict, fragment. Use `urlparse` and `parse_qs`.
- [ ] Build a URL safely from user input: encode query parameters with `urlencode`, join paths with `urljoin`. Reject URL schemes other than `http` and `https`.
- [ ] Encode and decode URL components: percent-encode a string with spaces and special chars, then decode. Show the difference between `quote()`, `quote_plus()`, and `urlencode()`.
- [ ] Write `normalize_url(url)` that: lowercases scheme and host, removes default ports (`:80`, `:443`), removes trailing slash from path, and sorts query parameters.

---

## 20. pwntools (Advanced)

> ⚠️ All exercises MUST be done against CTF targets, intentionally vulnerable binaries, or programs you wrote yourself. Never against real systems.

- [ ] Set up an isolated environment (VM or container) with pwntools installed. Verify with `python -c "from pwn import *; print(pwnlib.__version__)"`.
- [ ] Use `ELF("./binary")` to inspect a locally compiled binary: print entry point, architecture, and list of imported functions.
- [ ] Explain: ASLR, PIE, NX, stack canaries, RELRO. What does each mitigation prevent? Run `checksec` on a binary.
- [ ] Use `process("./binary")` to interact with a local program: send input with `p.sendline()`, receive output with `p.recvline()`, and verify expected behavior.
- [ ] Explain what a buffer overflow is conceptually. Write a vulnerable C program, compile it with protections disabled, and crash it with a too-long input from Python.
- [ ] Use `pwntools` to craft a payload that overwrites a return address in your own intentionally vulnerable program. Document the target, compile flags used, and expected behavior.
- [ ] Write a CTF lab report: target binary name, mitigations present, vulnerability identified, exploit approach, and what you learned about the defense that would have prevented it.

---

## 21. Automation Projects

Each project must include: argument parsing (`argparse`), logging, error handling, a dry-run mode, and a JSON/CSV report output.

- [ ] **Port Scanner:** Scan a user-specified host and port range. Multi-threaded. Report open/closed/filtered. Banner grab for open ports. CSV output.
- [ ] **Banner Grabber:** Connect to each open port, wait for banner, decode, and identify service version. Timeout and retry logic. JSON output.
- [ ] **Directory Brute Forcer:** Given a base URL (your own server) and a wordlist, test each path. Log 200/301/403 responses separately. Rate-limit with a delay flag.
- [ ] **Web Crawler:** Crawl your own site to a configurable depth. Respect `robots.txt`. Deduplicate URLs. Extract all links, forms, and emails. JSON report.
- [ ] **Log Analyzer:** Parse Apache/Nginx access logs. Report: top IPs, top URLs, status distribution, suspicious IPs (brute force heuristic), peak hour. JSON + CSV output.
- [ ] **IOC Extractor:** Read text files (threat intel reports). Extract and deduplicate IPs, domains, URLs, hashes (MD5/SHA256), CVE IDs. Export categorized JSON.
- [ ] **API Automation Tool:** Connect to a REST API (use a public test API like `jsonplaceholder`). Paginate through all resources. Filter, transform, and export data. Retry on failure.
- [ ] **Report Generator:** Accept a JSON scan result file. Generate an HTML report with: summary table, open ports list, risk assessment, and a findings section.
- [ ] **Vulnerability Config Checker:** Check an application's config file for insecure settings: debug mode on, default credentials, unencrypted connections, overly permissive file permissions.
- [ ] **Packet Parser:** Read a PCAP file. Produce a report: total packets, protocol breakdown, top talkers, suspicious patterns (port scans, repeated SYNs), and DNS queries. JSON output.
- [ ] **File Integrity Checker:** Record SHA-256 hashes of all files in a directory. On next run, compare and report: new files, modified files, deleted files. Alert on unexpected changes.
- [ ] **DNS Toolkit:** Given a list of domains, query all record types, check for misconfigurations (missing SPF/DMARC, open recursion), and export a structured JSON report.
- [ ] **SSH Automation Script:** Connect to a list of SSH servers (you own). Run health-check commands on each. Collect results. Generate a status report. Handle auth failures gracefully.
- [ ] **Inventory System:** CLI tool to manage a JSON-backed inventory of network devices: add, update, delete, search by IP or hostname, and export to CSV.

---

## 22. Secure Coding Practices

**Conceptual**
- [ ] Explain the OWASP Top 10 at a Python code level: for each one, show what insecure code looks like and the secure alternative.
- [ ] Explain why `eval()`, `exec()`, `pickle.loads()` on untrusted data, and `subprocess(shell=True)` with user input are dangerous. Show safe alternatives for each.

**Coding**
- [ ] Write a `validate_input(value, type, min, max, allowed_pattern)` function that validates type, range, format, and allowlist. Test with empty, oversized, wrong-type, and valid inputs.
- [ ] Store secrets (API keys, DB passwords) in environment variables only. Write code that reads them and fails clearly (not silently) if they're missing. Show a `.env` file with `.gitignore` entry.
- [ ] Sanitize a user-supplied filename: reject path traversal (`../`, `/`), null bytes, and disallowed extensions. Ensure the final path stays within an allowed directory using `Path.resolve()`.
- [ ] Use `subprocess.run()` with a list argument (not `shell=True`) and `check=True`. Show how `shell=True` + user input = command injection.
- [ ] Configure logging to redact sensitive fields: passwords, tokens, credit card numbers in log messages. Show a `logging.Filter` that scrubs secrets.
- [ ] Implement a `SafeConfig` loader: reads YAML config, validates all keys against an allowlist, rejects unknown keys, and raises on missing required keys.
- [ ] Audit a small script for: hardcoded credentials, `verify=False` in requests, `yaml.load()` without Loader, unhandled exceptions, and missing input validation. Fix every issue.

---

## 23. Code Quality & Professional Workflow

**Coding**
- [ ] Add type hints to a module with 5 functions. Run `mypy` and fix all reported errors. Explain what `Optional[str]`, `Union[int, str]`, and `List[Dict[str, Any]]` mean.
- [ ] Write `pytest` tests for a grade calculator: test each grade boundary, the exact boundary values (90, 80, 70, 60), invalid marks (<0, >100), and the error message for invalid input.
- [ ] Use `@pytest.mark.parametrize` to test an IP validator with: valid IPs, invalid octets, wrong format, empty string, and IPv6 addresses.
- [ ] Use `unittest.mock.patch` to mock a `requests.get` call in a test. Return a mock response with a specific status code and JSON body. Test your code without making real HTTP requests.
- [ ] Use `cProfile` and `pstats` to profile a slow function. Identify the top 3 bottlenecks by cumulative time. Optimize one using a better algorithm or data structure.
- [ ] Format a messy Python file with `black`. Run `flake8` and fix all PEP 8 violations. Run `pylint` and address the top 5 issues by severity.
- [ ] Set up a Git repository: `git init`, `.gitignore` (Python template), `git add`, `git commit`. Create a feature branch, make a change, merge it, resolve a simulated conflict.
- [ ] Write a README.md: purpose, installation (`pip install -r requirements.txt`), configuration (env vars), usage with examples, authorized-use statement, and known limitations.
- [ ] Create a `Makefile` or `pyproject.toml` `[tool.taskipy]` section with commands: `make test`, `make lint`, `make format`, `make clean`.

---

## 24. Capstone Projects

Each project must have: a README, argparse CLI, logging, error handling, tests, a virtual environment, a `requirements.txt`, and a sample report output.

- [ ] **Vulnerability Scanner:** Combines port scanning, banner grabbing, and service version detection against your own lab server. Match banners against a local CVE database (JSON file). Generate an HTML report.
- [ ] **Mini Nmap:** Pure Python. TCP SYN scan simulation (using raw socket or Scapy on localhost), OS fingerprinting attempt (TTL heuristic), service identification. JSON + text report.
- [ ] **Password Manager CLI:** AES-GCM encrypted vault stored locally. Master password → PBKDF2 key derivation. Add, get, list, delete entries. Clipboard copy. Auto-lock after inactivity.
- [ ] **Secure File Transfer Tool:** Paramiko SFTP with host-key verification. Encrypt files before transfer using Fernet. Verify integrity with SHA-256 after transfer. Log all operations.
- [ ] **Network Monitoring Dashboard:** Polls your own lab hosts every 60s. Checks port availability. Tracks uptime %. Detects new open ports. Stores history in SQLite. Prints terminal dashboard.
- [ ] **SIEM Log Parser:** Reads syslog, Apache, Windows event log (simulated JSON). Normalizes to a common schema. Applies detection rules (brute force, privilege escalation patterns). Generates alerts JSON.
- [ ] **API Testing Framework:** Given an OpenAPI spec (JSON), automatically test each endpoint with: valid input, missing fields, wrong types, oversized values, and auth failures. Report findings.
- [ ] **Threat Intelligence Parser:** Downloads (from your own server) or reads local threat intel feeds (STIX, plain text). Extracts IOCs. Deduplicates. Enriches with DNS lookups. Exports actionable JSON.
- [ ] **Web Automation Framework:** Selenium + requests hybrid. Logs into a local test app, navigates pages, fills forms, downloads a report, verifies data. Supports multiple test scenarios via YAML config.
- [ ] **Security Automation Toolkit:** A unified CLI (using sub-commands) that combines: port scanner, banner grabber, DNS enumerator, IOC extractor, and log analyzer — all in one installable Python package.

---

## Learning Outcome Checklist

- [ ] Build a professional Python tool from scratch with modular design, tests, documentation, and a reproducible environment.
- [ ] Explain every dependency, design decision, and security consideration in your tool.
- [ ] Demonstrate that the tool handles valid input, invalid input, expected failures, and cleanup safely.
- [ ] Package the tool so a new user can install and run it from documented instructions.
- [ ] Produce a sample report using only synthetic or authorized data.
- [ ] Review the tool against a secure coding checklist before every release.
- [ ] Obtain explicit written authorization before testing any non-local system.
- [ ] Present the tool's limitations and safe-use boundaries clearly.

---

*Keep this file as a living checklist. Check off questions as you complete them. Revisit unchecked ones before interviews.*

---

## 25. Professional Curriculum Extensions

**Difficulty:** 🟢 Easy · 🟡 Medium · 🔴 Hard · ⚫ Interview / design discussion

### 25.1 Algorithms & Complexity

- [ ] 🟢 State the time and space complexity of list indexing, list append, set membership, and dictionary lookup.
- [ ] 🟡 Explain why dictionary lookup is average-case O(1), rather than guaranteed O(1).
- [ ] 🟡 Replace a nested-loop duplicate check with a set-based solution; compare time and memory complexity.
- [ ] 🟡 Find two values in a sorted list that add to a target using the two-pointer technique.
- [ ] 🟡 Find the longest substring without repeated characters with a sliding window.
- [ ] 🟡 Implement iterative binary search and return the insertion position when a target is absent.
- [ ] 🔴 Compare brute-force, sort-and-search, and hash-map solutions to the two-sum problem.
- [ ] ⚫ Identify the time and space bottleneck in one automation project and justify an improvement with measurements.

### 25.2 Data Structures & Recursion

- [ ] 🟢 Implement a stack with a list and use it to validate balanced parentheses.
- [ ] 🟢 Implement a FIFO queue with `collections.deque`; explain why it is preferable to `list.pop(0)`.
- [ ] 🟡 Implement a singly linked list with append, search, insert, and delete operations.
- [ ] 🟡 Build an LRU cache with `OrderedDict` or an equivalent design; test its eviction behavior.
- [ ] 🟡 Implement binary-tree preorder, inorder, and postorder traversal.
- [ ] 🟡 Use `heapq` to keep the top `k` largest values from a stream.
- [ ] 🔴 Solve a grid maze using BFS and return the shortest valid path.
- [ ] ⚫ Explain when recursion is less reliable in Python than an explicit stack, using directory traversal as an example.

### 25.3 Functional Python & Iterators

- [ ] 🟢 Use `enumerate` and `zip` to produce a numbered report from two related lists.
- [ ] 🟢 Use `any` and `all` to validate a batch of input records.
- [ ] 🟡 Recreate one transformation with a comprehension, `map`, and `filter`; compare readability.
- [ ] 🟡 Use `functools.reduce` to combine values and explain when a loop is clearer.
- [ ] 🟡 Use `itertools.chain`, `islice`, `groupby`, and `product` on small sample data.
- [ ] 🟡 Write a closure that creates configurable threshold-checking functions.
- [ ] 🔴 Use `functools.lru_cache` to optimize a recursive calculation and verify cache behavior.
- [ ] ⚫ Explain the memory trade-off between a lazy iterator pipeline and a materialized list.

### 25.4 Type Hints & Interfaces

- [ ] 🟢 Add parameter and return type hints to a small calculator module.
- [ ] 🟢 Use `list[str]`, `dict[str, int]`, `tuple[str, int]`, `Optional`, and `Union` correctly.
- [ ] 🟡 Model validated configuration with `TypedDict`, including required and optional keys.
- [ ] 🟡 Use `Literal` to constrain a function to supported modes.
- [ ] 🟡 Write a generic `first_item` function with `TypeVar`.
- [ ] 🟡 Define a `Protocol` for a logging dependency and inject a compatible implementation.
- [ ] 🔴 Run a type checker on a project and correct meaningful errors without hiding them behind broad `Any` types.
- [ ] ⚫ Distinguish static type checking, runtime validation, nominal typing, and structural typing.

### 25.5 Standard Library Mastery

- [ ] 🟢 Use `pathlib` to find only `.log` files in a directory you own and `tempfile` to create disposable test data.
- [ ] 🟡 Copy, move, archive, and inspect test files with `shutil` without overwriting an unexpected target.
- [ ] 🟡 Parse timezone-aware timestamps with `datetime`, measure elapsed time with `time.perf_counter`, and display a month using `calendar`.
- [ ] 🟡 Read validated INI configuration with `configparser`; generate record IDs with `uuid` and secure tokens with `secrets`.
- [ ] 🟡 Run a harmless command using `subprocess.run` with an argument list, timeout, and `check=True`.
- [ ] 🟡 Use `hashlib`, `base64`, `hmac`, and `ipaddress` in small examples; explain their distinct purposes.
- [ ] 🔴 Create a SQLite-backed local inventory with parameterized queries, transactions, and schema initialization.
- [ ] ⚫ Explain how to choose among a flat file, SQLite, and a remote database for an automation tool.

### 25.6 Advanced NumPy & Pandas

- [ ] 🟢 Demonstrate the difference between a NumPy view and copy by changing a slice.
- [ ] 🟡 Use integer-array indexing, Boolean masks, `np.where`, and `np.clip` without Python loops.
- [ ] 🟡 Explain `strides`, contiguous memory, and why memory layout can affect performance.
- [ ] 🟡 Use `np.linalg` to solve a small linear system and verify the solution.
- [ ] 🟡 Create a Pandas pivot table, then reshape it with `melt` and `pivot`.
- [ ] 🟡 Normalize a list-valued Pandas column with `explode` and use categorical data to control ordering.
- [ ] 🔴 Use `groupby().transform()` and rolling metrics without losing the original DataFrame rows.
- [ ] ⚫ Benchmark vectorized NumPy/Pandas code against a loop-based solution and report time/memory trade-offs.

### 25.7 Advanced Networking

- [ ] 🟢 Resolve and connect to IPv6 localhost in a controlled test environment.
- [ ] 🟡 Use `selectors` to multiplex several non-blocking localhost socket connections.
- [ ] 🟡 Explain, at a high level, how `select`, `epoll`, and `kqueue` support event-driven networking.
- [ ] 🟡 Describe ICMP, ARP, DHCP, and packet fragmentation and their roles in a network.
- [ ] 🟡 Inspect an offline lab PCAP for ICMP and ARP traffic without generating live packets.
- [ ] 🟡 Explain raw sockets conceptually, including privilege requirements and authorization boundaries.
- [ ] 🔴 Implement a local `asyncio` echo service with cancellation, timeouts, and graceful shutdown.
- [ ] ⚫ Compare TCP, UDP, HTTP/1.1, HTTP/2, and WebSocket for a real-time application design.

### 25.8 Modern HTTP & Later Security Libraries

> ⚠️ Use security libraries only in isolated labs, CTFs, test services, or against files and systems you own or are explicitly authorized to assess.

- [ ] 🟢 Compare `urllib3`, `requests`, `httpx`, and `aiohttp` for synchronous and asynchronous API clients.
- [ ] 🟡 Build an `httpx` client for a permitted test API with timeouts, retries, and response validation.
- [ ] 🟡 Parse and validate a JWT locally without treating an unverified payload as trusted.
- [ ] 🟡 Explain OAuth 2.0 roles and use `requests-oauthlib` only with a test provider and non-production credentials.
- [ ] 🟡 Use `yara-python` with harmless test strings to write and validate a simple detection rule.
- [ ] 🟡 Inspect only a training binary or a file you own with `pefile`, LIEF, or Capstone; record basic metadata.
- [ ] 🔴 Use `angr` or Unicorn only on a CTF or self-created program, focusing on defensive understanding.
- [ ] ⚫ Write a lab safety plan defining scope, authorization, data handling, and cleanup for binary-analysis work.

### 25.9 Testing, Coverage & CI

- [ ] 🟢 Write `pytest` fixtures that create temporary test data and remove it after each test.
- [ ] 🟡 Use `unittest.mock.patch` to isolate an HTTP client from the network.
- [ ] 🟡 Parameterize tests for normal values, boundary values, and invalid input.
- [ ] 🟡 Measure coverage and identify meaningful untested branches rather than chasing a percentage blindly.
- [ ] 🟡 Run an integration test for a CLI tool using a temporary directory and subprocess.
- [ ] 🟡 Configure GitHub Actions to run formatting, linting, type checks, and tests on pushes and pull requests.
- [ ] 🔴 Add a regression test for a discovered bug and verify it would have failed before the fix.
- [ ] ⚫ Define a CI quality gate for a security-oriented project, including dependency review and secret scanning.

### 25.10 Challenges & Interview Practice

- [ ] 🟢 Build a command-line expense tracker using functions, JSON storage, validation, and a monthly summary.
- [ ] 🟡 Build a personal GitHub API client for a test or personal account, including pagination, retries, and tests.
- [ ] 🟡 Build a typed, configurable IOC extractor for local files and export a Markdown report.
- [ ] 🟡 Build an authorized log-anomaly detector using a sliding window and document likely false positives.
- [ ] 🟡 Build an offline PCAP report generator with filters, protocol summaries, and JSON output.
- [ ] 🔴 Refactor an O(n²) operation in one project and benchmark the improvement.
- [ ] 🔴 Review a small script for algorithmic complexity, unsafe input handling, poor testability, and missing documentation.
- [ ] ⚫ Present the architecture, authorization controls, failure modes, and limitations of one project in a mock interview.
