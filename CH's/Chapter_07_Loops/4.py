n = int(input("Please Enter A Number You Want to Check : "))

for i in range (2,n):
    if(n%i==0):
        print("The Number is Not a Prime Number")
        break
else:
    print("The Number is a Prime NUmber")
#This code checks if a given number is prime or not.
# A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
