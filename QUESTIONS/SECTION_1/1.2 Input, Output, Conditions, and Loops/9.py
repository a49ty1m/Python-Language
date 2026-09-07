# Keep asking for the password `future123` until the correct password is entered (use `while`).
password = "future123"
def pass_checker(p: str) -> bool:
    while p != password:
        print("Incorrect password. \n Try Again.")
        p = input("Enter the password: ")
    print("Correct password")
    return True
pass_checker(input("Enter the password: "))

