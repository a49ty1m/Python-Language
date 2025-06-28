def table(n):
    '''This function prints the multiplication table of a given number n.'''
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")   

a=int(input("Enter a number to print its multiplication table: "))
table(a)
# The function table(n) takes an integer n as input and prints the multiplication table for that number from 0 to 10. 
# The input is taken from the user, and the