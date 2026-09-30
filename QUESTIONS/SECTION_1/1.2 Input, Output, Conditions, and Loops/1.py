# Write a program that checks whether an integer is even or odd.

def is_even_or_odd(num: int) -> None:
    if num % 2 == 0:
        print("Is Even")
    else :
        print("Is Odd")

n = int(input("Enter the Number Your Want to check : "))
is_even_or_odd(n)