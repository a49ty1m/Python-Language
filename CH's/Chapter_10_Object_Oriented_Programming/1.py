class programmer:
    company = "Microsoft"  # Class variable
    def __init__(self, name, salary, language, pin):
        self.name= name
        #in the self.name the name on the left is the instance variable and the name on the right is the parameter
        self.salary = salary
        #in the self.salary the salary on the left is the instance variable and the salary on the right is the parameter
        self.language = language
        #in the self.language the language on the left is the instance variable and the language on the right is the parameter
        self.pin = pin
        #in the self.pin the pin on the left is the instance variable and the pin on the right is the parameter

p = programmer("Smilo", 1200000, "Python", 342001)#the smilo will be passed to the name parameter, 1200000 will be passed to the salary parameter, Python will be passed to the language parameter and 342001 will be passed to the pin parameter
#then it will assign the values to the instance variables
print("The name is: " + p.name)  # Accessing instance variable
print("The salary is: " + str(p.salary))  # Accessing instance variable
print("The language is: " + p.language)  # Accessing instance variable
print("The pin Code is: " + str(p.pin))  # Accessing instance variable
print("The company is: " + p.company)  # Accessing class variable

r= programmer("Ron", 12000, "JavaScript", 27272384)
print("The name is: " + r.name)  # Accessing instance variable
print("The salary is: " + str(r.salary))  # Accessing instance variable             
print("The language is: " + r.language)  # Accessing instance variable
print("The pin Code is: " + str(r.pin))  # Accessing instance variable
print("The company is: " + r.company)  # Accessing class variable 