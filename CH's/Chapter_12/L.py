'''walrus'''
#here we do 
'''
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List has {n} elements, which is more than 3.")
'''
# This code uses the walrus operator to assign the length of the list to `n`
#else we would do 
# [n = len([1, 2, 3, 4, 5])
# if n > 3:
#     print(f"List has {n} elements, which is more than 3.")]
# The walrus operator allows us to assign a value to a variable as part of an expression.

"""Type Variables"""
# Type variables allow us to define generic types in Python functions and classes.
# They are used to create functions or classes that can operate on different types while maintaining type safety
#like 
'''
n: int = 5 
#here we define a variable n of type int and assign it the value 5
s: str = "Hello"
#here we define a variable s of type str and assign it the value "Hello"
'''

"""Use In Function"""
def add(x: int, y: int) -> int:
    #Adds two integers and returns the result. which will return an int
    return x + y

"""Advanced Typing"""
'''
from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
'''

"""Match Case"""
'''
def http_status(status):
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
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status
'''

"""Adding OF Dictionary"""
'''
# Adding 2 dictionaries together using the `|` operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = dict1 | dict2
# The result will be {'a': 1, 'b': 3, 'c': 4}
# Note: If there are duplicate keys, the value from the second dictionary will overwrite the value from the first dictionary.
'''

"""With Statement"""
'''
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    # Process files
    pass
#This allows you to open multiple files in a single with statement, ensuring that all files are properly closed after their block is executed.
'''

"""exceptions"""
'''
#if we use 
a= int(input("Enter a number: "))
#we can get an error if the input is not a number
#to handle this we can use try and except
'''
'''
try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")
except Exception as e:
    
    # **`Exception`**: This is a built-in Python class that represents the base class for 
    # most error types in Python. When you write `except Exception`, you're telling Python 
    # to catch almost any error that might occur in the `try` block. Some examples of 
    # exceptions include:
    # - `ValueError` (when you pass the wrong type of value)
    # - `TypeError` (when you use the wrong data type)
    # - `ZeroDivisionError` (when you divide by zero)
    # - `FileNotFoundError` (when a file doesn't exist)
    print(f"An error occurred: {e}")
    #this will catch the error and print a message instead of crashing the program
    print("Please enter a valid number.")
print("Thank You")
# This code will prompt the user to enter a number, and if they enter something that can't be converted to an integer,
'''
'''
#we can also give specific exceptions like this
try:
    pass
except ValueError as e:
    pass
except ZeroDivisionError as f:
    pass
except:
    pass
'''

"""Raise Exception"""
'''
#we can also raise exceptions using the 'raise' keyword
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b == 0:
    raise ZeroDivisionError("You cannot divide by zero! \nPlease Enter a Non-Zero Number.")
#this was a custom exception that we raised if the user tries to divide by zero
else:
    print(f"The result of {a} divided by {b} is {a / b}")
# This code will raise a ZeroDivisionError if the user tries to divide by zero,
# and the program will terminate with an error message.
'''

"""Else in Try Except"""
'''
#The 'else' block in a try-except statement is executed if the try block does not raise an exception.
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("You cannot divide by zero! Please Enter a Non-Zero Number.")
else:
    # This block will only execute if no exceptions were raised in the try block
    print("This is the else block, Executing after try block Without any exceptions.")
    print(f"The result of {a} divided by {b} is {result}")
'''

"""Finally in Try Except"""
'''
#this is mainly used in functions 
#like
def main():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        result = a / b
    except ZeroDivisionError:
        print("You cannot divide by zero! Please Enter a Non-Zero Number.")
        return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    else:
        print(f"The result of {a} divided by {b} is {result}")
        return
    finally:
        print("This is the finally block, Executing after try block, regardless of whether an exception occurred or not.")
        #if we don't use finally then the code will not execute if an exception is raised
# This block will always execute, even if an exception was raised or not
# It is often used for cleanup actions, like closing files or releasing resources.
main()
'''
"""__name__ and __main__"""
'''
import module
# This will import the module and execute the code in it
#this will print nothing go and check the module.py file
'''

"""Global and Local Variables"""
'''
a= 69
def hi():
    global a  # This will refer to the global variable 'a'
    a=7
    print(a)
    #this will print 7 because it is a local variable
hi()
# Now 'a' is changed to 7 globally
# If we print 'a' here, it will show the updated value not the old one
print(a)
'''


"""Enumerate"""
'''
#for a list
l= [1,2324,45225,523432,12323]
index = 0
for item in l: 
    print(f"Index of item {item} is {index}")
    index += 1
#this is cool zindagi but 
#now we use enumerate
for index, item in enumerate(l):
    print(f"Index of item {item} is {index}")
#this is mentos life
#this will print the index of each item in the list along with the item itself
#enumerate is a built-in function that adds a counter to an iterable and returns it as an enumerate object.
#The enumerate object contains pairs of index and value, which can be unpacked
#into separate variables in a for loop.
'''

"""List Comprehensions"""
'''
L=[1,2,3,4,5,6,8,11]
Sq=[]
for item in L:
    Sq.append(item**2)

print(Sq)
#this is aam zindagi
#now we use list comprehensions
sq = [item**2 for item in L]
print(sq)
#this is mentos zindagi
#List comprehensions provide a concise way to create lists by applying an expression to each item in an iterable.
#The syntax is [expression for item in iterable], which is more readable and often more efficient than using a for loop.
'''