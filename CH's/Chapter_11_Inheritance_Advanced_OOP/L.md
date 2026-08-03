````python
'''
class employee:
    #this is the parent class or a base class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
'''
'''
class programmer():
    company = "ITC infotech"
    def show(self):
        print(f"The name of the programmer is {self.name} and the salary is {self.salary}")
    
    def show_language(self):
        print(f"The language of the programmer is {self.language}")
#thia is a lengthy program and i have to use the show method of both the classes and if i do some changes in the show method of one class then i have to do the same changes in the other class also
# so i will use the concept of multiple inheritance to solve this problem
'''    
'''
class programmer(employee):
    #this is called single inheritance
    #this is the child class or a derived class
    #it will inherit the properties of the employee class
    #this will also have its own properties
    company = "ITC infotech"    
    
    def show_language(self):
        print(f"The language of the programmer is {self.language}") 

#this is called hierarchical inheritance
'''
##above code was an example of single inheritance

'''
class employee:
    #this is first base/parent class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class coder():
    #this is second base/parent class
    company = "ITC infotech"
    def show_language(self):
        print(f"The language of the coder is {self.language}")

class programmer(employee, coder):
    #this is called multiple inheritance
    #this is the child class or a derived class
    def shows(self):
        print(f"the level of the programmer is {self.level} , which is very high")

b=programmer()
b.name = "John"
b.salary = 50000
b.language = "Python"
b.level = "Expert"
b.show()
b.show_language()
b.shows()
'''
#this is called multiple inheritance

''' 
class employee:
    #this is first base/parent class
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
class coder():
    #this is second base/parent class
    company = "ITC infotech"
    def show_language(self):
        print(f"The language of the coder is {self.language}")

class programmer(employee, coder):
    #this is called multiple inheritance
    #this is the child class or a derived class
    def shows(self):
        print(f"the level of the programmer is {self.level} , which is very high")

class manager(programmer):
    #this is called multilevel inheritance
    #this is the child class or a derived class
    def show_manager(self):
        print(f"The manager's name is {self.name} and the salary is {self.salary}")

b=manager()
b.name = "John"
b.salary = 50000
b.language = "Python"
b.level = "Expert"
b.show()
b.show_language()
b.shows()
b.show_manager()
'''
#this is called multilevel inheritance

'''
class employee:
    #this is first base/parent class
    def __init__(self):
        print("This is the constructor of the employee class")

class coder():
    #this is second base/parent class
    def __init__(self):
        print("This is the constructor of the coder class")

class programmer(employee, coder):
    #this is called multiple inheritance
    #this is the child class or a derived class
    def __init__(self):
        print("This is the constructor of the programmer class")
        super().__init__()  # This will call the constructor of the first parent class (employee)
        coder.__init__(self)  # This will call the constructor of the second parent class (coder

b=programmer()
'''

'''
class employee:
    a=10
    def show(self):
        print("the value of a is", self.a)

x=employee()
x.a=20

x.show() # This will print "the value of a is 20" because we changed the value of a for the instance x

class programmer():
    b=30
    @classmethod # This is a class method
    def show_b(cls): #the cls is used to refer to the class itself but it is not mandatory to be cls, it can be anything
        print("the value of b is", cls.b)
    
y=programmer()
y.b=40
y.show_b()  # This will print "the value of b is 30" because class methods access class variables, not instance variables
'''

'''
class adi:
    @property
    def name(self):
        return self.cname

    @name.setter
    def name(self,value):
        self.fname = value.split()[0] # This will take the first part of the name by first splitting the string then taking the first part
        self.lname = value.split()[1] # This will take the second part of the name by first splitting the string then taking the second part
        self.cname = value

x = adi()
x.name = "Aditya Mishra"
print(x.cname)  # This will print "Aditya Mishra"
print(x.fname)  # This will print "Aditya"
print(x.lname)  # This will print "Mishra"
'''


'''

class number:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a
    
    
    Explanation of the __add__ method in the number class:
    When you write:
    ```python
    x = number(10)
    y = number(5)
    result = x + y  # This calls x.__add__(y)


    In the `__add__` method:
    - `self` refers to `x` (the first number object with `a = 10`)
    - `other` refers to `y` (the second number object with `a = 5`)
    - So `self.a + other.a` becomes `10 + 5 = 15`

    # When you do x + y, it calls x.__add__(y)
    result = x + y  # Returns 10 + 5 = 15
    print(result)   # Output: 15


    ## Key Point:

    # `other.a` **does have a value** - it's the `a` attribute of the second `number` object you're performing the operation with. Both objects need to exist for the  operation to work!
    
    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

    def __truediv__(self, other):
        return self.a / other.a


x = number(10)
y = number(5)
result_add = x + y  # Calls x.__add__(y)
result_sub = x - y  # Calls x.__sub__(y)
result_mul = x * y  # Calls x.__mul__(y)
result_div = x / y  # Calls x.__truediv__(y)
print(result_add)
print(result_sub)
print(result_mul)
print(result_div)
'''
````