"""
file_service.py — File Handling Service
=========================================
This module handles all file I/O operations for student data persistence.

File Handling Concepts Demonstrated:
    - Reading and writing JSON files
    - Creating directories and files automatically
    - Handling FileNotFoundError, json.JSONDecodeError, PermissionError
    - Creating backup copies before overwriting data
    - Graceful recovery from corrupted files

Design Decision:
    JSON is used as the storage format because it is:
    1. Human-readable (easy to inspect and debug)
    2. Natively supported by Python's standard library
    3. Sufficient for the scale of this application
    4. Does not require external database software
"""

import json
import os
import shutil

from config import DATA_DIR, DATA_FILE, BACKUP_FILE
from models.student import Student
from utils.exceptions import FileCorruptedError


class FileService:
    """
    Handles persistent storage of student records in JSON format.

    Responsibilities:
        - Save a list of Student objects to data/students.json
        - Load Student objects from data/students.json
        - Create data directory if it doesn't exist
        - Create backup before each save
        - Handle file errors gracefully
    """

    def __init__(self):
        """
        Initialize FileService and ensure the data directory exists.

        If the data directory does not exist, it is created automatically.
        This prevents FileNotFoundError on first run.
        """
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """
        Create the data directory if it does not exist.

        Uses os.makedirs with exist_ok=True so it doesn't raise
        an error if the directory already exists.
        """
        try:
            os.makedirs(DATA_DIR, exist_ok=True)
        except PermissionError:
            print(f"  ❌ Permission denied: Cannot create directory '{DATA_DIR}'.")
        except OSError as e:
            print(f"  ❌ OS error while creating data directory: {e}")

    def _create_backup(self):
        """
        Create a backup of the current data file before overwriting.

        This provides a safety net in case the save process is
        interrupted or the new data is somehow corrupted.
        """
        try:
            if os.path.exists(DATA_FILE):
                shutil.copy2(DATA_FILE, BACKUP_FILE)
        except (PermissionError, OSError) as e:
            # Backup failure should not block the save operation
            print(f"  ⚠️  Warning: Could not create backup: {e}")

    def save_students(self, students):
        """
        Save a list of Student objects to the JSON data file.

        Process:
            1. Create a backup of the existing file
            2. Serialize each Student to a dictionary
            3. Write the list of dictionaries as JSON

        Args:
            students (list[Student]): List of Student objects to save.

        Returns:
            bool: True if saved successfully, False otherwise.
        """
        try:
            # Step 1: Create backup of existing data
            self._create_backup()

            # Step 2: Convert Student objects to dictionaries
            data = [student.to_dict() for student in students]

            # Step 3: Write JSON with indentation for readability
            with open(DATA_FILE, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            return True

        except PermissionError:
            print(f"  ❌ Permission denied: Cannot write to '{DATA_FILE}'.")
            return False
        except TypeError as e:
            print(f"  ❌ Serialization error: {e}")
            return False
        except OSError as e:
            print(f"  ❌ File system error while saving: {e}")
            return False

    def load_students(self):
        """
        Load student records from the JSON data file.

        Process:
            1. Check if the file exists (return empty list if not)
            2. Read and parse the JSON content
            3. Deserialize each dictionary into a Student object
            4. Handle corrupted files gracefully

        Returns:
            list[Student]: List of Student objects loaded from file.
                           Returns an empty list if the file is missing
                           or empty.

        Raises:
            FileCorruptedError: If the file exists but contains invalid JSON.
        """
        # If the file doesn't exist yet, return empty list (first run)
        if not os.path.exists(DATA_FILE):
            return []

        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                content = file.read().strip()

                # Handle empty file
                if not content:
                    return []

                data = json.loads(content)

            # Validate that the loaded data is a list
            if not isinstance(data, list):
                raise FileCorruptedError(
                    filepath=DATA_FILE,
                    message="Data file does not contain a JSON array."
                )

            # Deserialize each dictionary to a Student object
            students = []
            for i, record in enumerate(data):
                try:
                    student = Student.from_dict(record)
                    students.append(student)
                except Exception as e:
                    # Skip corrupted individual records but warn the user
                    print(
                        f"  ⚠️  Skipping corrupted record #{i + 1}: {e}"
                    )

            return students

        except json.JSONDecodeError as e:
            raise FileCorruptedError(
                filepath=DATA_FILE,
                message=(
                    f"Data file contains invalid JSON: {e}. "
                    f"Check '{DATA_FILE}' or restore from backup."
                )
            )
        except PermissionError:
            print(f"  ❌ Permission denied: Cannot read '{DATA_FILE}'.")
            return []
        except OSError as e:
            print(f"  ❌ File system error while loading: {e}")
            return []

    def file_exists(self):
        """
        Check if the data file exists.

        Returns:
            bool: True if the data file exists.
        """
        return os.path.exists(DATA_FILE)

    def get_file_info(self):
        """
        Get information about the data file.

        Returns:
            dict: File info including path, size, and existence status.
        """
        info = {
            "path": DATA_FILE,
            "exists": os.path.exists(DATA_FILE),
            "size": 0,
            "backup_exists": os.path.exists(BACKUP_FILE)
        }
        if info["exists"]:
            info["size"] = os.path.getsize(DATA_FILE)
        return info
