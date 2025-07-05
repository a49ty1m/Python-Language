class Employee:
    salary = 100000   
    incriment = 10
    
    @property
    def salaryincrement(self):
        return (self.salary + (self.salary * self.increment / 100))
    #property converts a method into a read-only attribute, allowing access without parentheses.
    
    @salaryincrement.setter
    def salaryincrement(self, salary):
        self.increment = ((salary/self.salary) -1) * 100

adi=Employee()
print(adi.salary)
# print(adi.salary_after_increment)

adi.salaryincrement = 120000
print(adi.increment)

