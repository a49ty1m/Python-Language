# Use nested loops to print a right-angled triangle of stars with `N` rows.

def triangle_right_angled(x: int) -> None:
    for i in range(x):
        for j in range(i+1):
            print("*", end=" ")
        print() # this is important because it creates a new line after each row or we can use \n in the print statement


triangle_right_angled(int(input("Enter the Number of rows You Want : ")))