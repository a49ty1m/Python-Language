class calculator:
    def __init__(self,n):
        n=int(input("Enter a number for calculation: "))
        self.number = n 
    def sq(self):
        print("The square of " + str(self.number) + " is: " + str(self.number ** 2))
    def cube(self):
        print("The cube of " + str(self.number) + " is: " + str(self.number ** 3))
    def sq_root(self):
        print("The square root of " + str(self.number) + " is: " + str(self.number ** 0.5))
    def cube_root(self):
        print("The cube root of " + str(self.number) + " is: " + str(self.number ** (1/3))) 

a= calculator(5)
a.sq()
a.cube()
a.sq_root()
a.cube_root()
