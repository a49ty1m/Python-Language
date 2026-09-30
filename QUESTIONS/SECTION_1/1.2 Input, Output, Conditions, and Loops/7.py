# Calculate a factorial using a loop. Handle zero and reject negative input.

def fac(n : int ) -> None:
    if n < 0:
        print("Please Enter a Positive Number")
    elif n == 0:
        print("The Factorial of 0 is 1")
    else:
        f=1
        for i in range(1,n+1):
            f*=i
        print(f"The Factorial of {n} is {f}")

n=int(input("Enter a Number : "))
fac(n)