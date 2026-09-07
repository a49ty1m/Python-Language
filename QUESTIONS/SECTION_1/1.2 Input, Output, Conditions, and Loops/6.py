# Find the sum of the first `N` natural numbers using a loop.

def sum_natural(n: int) -> None:
    s=0
    for i in range(1,n+1):
        s+=i
    print(f"The Sum of the first {n} natural numbers is {s}")

n=int(input("Enter a number : "))
sum_natural(n)
