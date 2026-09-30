# Take three numbers and print the largest, including the case where values are equal.
import enum
def number_checker(a: int,b: int,c: int) -> None:
    if a==b and b==c:
        print("All are equal")

    elif a==b :
        if a>c:
            print("a and b are equal and they are greater than c")
        else:
            print("c is greater than a and b")

    elif b==c and c>a:
        if b>a:
            print("b and c are equal and they are greater than a")
        else:
            print("a is greater than b and c")

    elif a==c:
        if a>b:
            print("a and c are equal and they are greater than b")
        else:
            print("b is greater than a and c")

    elif a>b and a>c:
        print(f"number{a} is the largest")

    elif b>a and b>c:
        print(f"number {b} is the largest")
        
    else:
        print(f"number {c} is the largest")

a = int(input("Enter Number 1 : "))

b = int(input("Enter Number 2 : "))

c = int(input("Enter Number 3 : "))

number_checker(a,b,c)
