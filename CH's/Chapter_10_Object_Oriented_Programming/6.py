from random import randint  #this will import the randint function from the random module
#now we don't need to use random.randint, we can directly use randint
class train:
    def __init__(slf,train_no):
        slf.train_no = train_no
        #we can use any name for the first parameter, here we are using slf instead of self
        #slf.train_no is the instance variable and train_no is the parameter
        #this will assign the value of train_no to the instance variable train_no

    def book(adi, fro, to):
        #here we used adi instead of self, it is just a name, we can use any name
        #adi is the instance of the class train
        print(f"Your train {adi.train_no} is booked from {fro} to {to}.")

    def getstatus(self, fro, to):
        print(f"Status of train {self.train_no} from {fro} to {to} is: On Time.")

    def getfair(self, fro, to):
        print(f"Fair of train {self.train_no} from {fro} to {to} is: {randint(2222,9484)}Rs.")

n = int(input("Enter train number: "))
#this will take the train number as input from the user and assign it to the variable n
#then it will pass the value of n to the train class constructor
fro = input("Enter departure city: ")
#this will take the departure city as input from the user and assign it to the variable fro
#then it will pass the value of fro to the book method
to = input("Enter destination city: ")
#this will take the destination city as input from the user and assign it to the variable to
#then it will pass the value of to to the book method
a=train(n)
a.book(fro, to)
a.getstatus(fro, to)
a.getfair(fro, to)
