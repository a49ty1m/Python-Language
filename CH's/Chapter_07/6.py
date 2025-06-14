n= int(input("Enter the Number You Factorial of : "))
fact = 1
if n == 0:
    print("The Factorial of 0 is : 1")
    exit()
else:
    for i in range(1, n + 1):

        fact *= i
print(f"The Factorial of {n} is : {fact}")
# # This code calculates the factorial of a number n provided by the user.
# The factorial is calculated by multiplying all integers from 1 to n.