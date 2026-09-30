"""Vertualization"""
# we can make vertual machine using python
# like
#first we need to install the library
'''
for linux = 
- sudo apt install python3-venv  # Install the venv package
- python3 -m venv myenv   # Create a virtual environment named 'myenv'
- source myenv/bin/activate  # Activate the virtual environment

for windows =
pip install virtualenv  # Install the virtualenv package
virtualenv myenv  # Create a virtual environment named 'myenv'
myenv\Scripts\activate  # Activate the virtual environment
# After activating the virtual environment, you can install packages using pip, and they will be isolated from the global Python installation.
# To deactivate the virtual environment, simply run:
- deactivate
# Virtual environments are useful for managing dependencies for different projects, ensuring that each project has its own set of packages without conflicts.
'''

"""freeze"""
'''
# it is use to save the current packages and their versions in a file or to see too
# we can freeze the requirements of a project using the following command
# pip freeze > requirements.txt
# this will create a file named requirements.txt with all the packages and their versions
# to install the packages from the requirements.txt file we can use the following command
# pip install -r requirements.txt
'''

"""Lambda Function"""
'''
# it is an anonymous function
# we can use it to create small functions
# syntax = lambda arguments: expression
# example =
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6
'''

"""Join Function"""
'''
# it is used to join the elements of a list or tuple into a single string with a specified separator
# syntax = separator.join(iterable)
# example =
words = ["Hello", "world", "from", "Python"]
sentence = "-".join(words)
print(sentence)  # Output: Hello-world-from-Python
'''

"""formate strings"""
'''
# let say we have a string 
#like 
a = "hi i'm {} and i am {} years old".format("Aditya", 20)
print(a) # output: hi i'm Aditya and i am 20 years old
#this will replace the {} with the values passed in the format function in order because by default the numbering starts from 0
# we can also use indexing to specify the order of replacement
b = "hi i'm {1} and i am {0} years old".format(20, "Aditya")
print(b) # output: hi i'm Aditya and i am 20 years old
# we can also use named placeholders
c = "hi i'm {name} and i am {age} years old".format(name="Aditya", age=20)
print(c) # output: hi i'm Aditya and i am 20 years old
# we can also use f-strings (formatted string literals) in python 3.6 and above
name = "Aditya"
age = 20
d = f"hi i'm {name} and i am {age} years old"
print(d) # output: hi i'm Aditya and i am 20 years old
'''

"""Map, Filter and Reduce"""
'''
"Map Function"
# let say we have a list of numbers and we want to square each number in the list
numbers = [1, 2, 3, 4, 5]
Square = lambda x: x ** 2
squared_numbers = list(map(Square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#or 
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# if we don't use list() then it will return a map object
"Filter Function"
even = lambda n: n % 2 == 0
even_numbers = list(filter(even, numbers))
print(even_numbers)  # Output: [2, 4]
#or
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# if we don't use list() then it will return a filter object
"Reduce Function"
from functools import reduce
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15
#the reduce function applies the lambda function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.
# in this case it will add all the numbers in the list and return the sum = 1+2=3+3=6+4=10+5=15
'''

