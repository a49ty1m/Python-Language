"""
In OOPS
Noun is use to represent a class
eg. `student`, `car`, `person`, etc.
Verb is used to represent a method
eg. `study()`, `drive()`, `speak()`, etc.
Adjective is used to represent an attribute/variable
eg. `name`, `age`, `color`, etc.
"""


'''
class student:
    name = "Aditya"     #this is a class attribute/variable
    roll_no="98"        #this is a class attribute/variable

adi=student()
print(adi.name , adi.roll_no)

sam=student()
sam.name="samiksha"   #this is an object/instance attribute/variable
#instance attributes/variables get priority over class attributes/variables
sam.roll_no="30"      #this is an object/instance attribute/variable

print(sam.name, sam.roll_no)

sunu=student()
sunu.salary=188888 
print(sunu.salary, sam.name)
'''
# The above code demonstrates the difference between class attributes and instance attributes in Python.
# Class attributes are shared across all instances of the class, while instance attributes are unique to each

# instance. In this example, `name` and `roll_no` are class attributes, while `sunu.salary` is an instance attribute.
# The output will show the class attributes for `adi` and the instance attributes for `sam` and `sunu`.


'''
class student:
    name = "Aditya"     # this is a class attribute/variable
    roll_no = "98"      # this is a class attribute/variable

    def get_info():
        print(f"Name: {name}, Roll No: {roll_no}")
    
adi = student()
print(adi.name, adi.roll_no)
adi.get_info() 
#this will raise an error because get_info is not defined as an instance method
#student.get_info() takes no arguments, but will be given one (the instance `adi`)
adi.get_info = student.get_info(adi)  # Assigning the class method to the instance
#so we have to use self in the method to access instance attributes
'''



'''
class student:
    name = "Aditya"     # this is a class attribute/variable
    roll_no = "98"      # this is a class attribute/variable

    def get_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

    def greet(self):
        #we have to use self to access instance attributes even if we don't use them
        print("Hello, I am a student!")
    
    #if we don't want to use self in the method we can use @staticmethod
    @staticmethod
    def morning_greet():        #this will not have access to instance attributes
        #this is a static method
        print("Hello, Good Morning!")

    def __init__(self): #this is a dunder method which is a special method because it starts and ends with double underscores
        #this is also the constructor method this will be called when an object is created without even calling it
        #this will execute on the beginning
        print("A new student object has been created!")
# Usage
adi=student()
# print(adi.name, adi.roll_no)
# adi.get_info()  # This will now work correctly as get_info is an instance method
adi.morning_greet()  # This will also work correctly
# adi.get_info = student.get_info(adi) #both are same 
'''

