n = int(input("Enter The Number You Want Table of : "))
'''
#By For Loop
for i in range (11):
    num = n * i
    print(f"{n} * {i} = {num}")
# This code takes an integer input from the user and prints its multiplication table from 0 to 10.
'''
#By While Loop
i=0
while (i<=10):
    num = n * i
    print(f"{n} * {i} = {num}")
    i+=1

# This code takes an integer input from the user and prints its multiplication table from 0 to 10 using a while loop.
# For example, if the user inputs 5, it will print: