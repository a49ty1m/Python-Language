# Create a grade calculator: 90–100 → A+, 80–89 → A, 70–79 → B, 60–69 → C, below 60 → Fail.

def marks_check(m: int) -> None:
    if m>=90 and m<=100:
        print("A+")
    elif m>=80 and m<=89:
        print("A")
    elif m>=70 and m<=79:
        print("B")
    elif m>=60 and m<=69:
        print("C")
    else:
        print("Fail")

m=int(input("Enter Your Marks : "))
marks_check(m)