# Print the multiplication table for a number from 1 to 10.

def table(n: int) -> None:
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

n=int(input("Enter The Number : "))
table(n)
        