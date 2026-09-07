# Write a voting-eligibility checker for a user aged 18 or older.

def age_Check(a: int) -> None:
    if a >= 18:
        print("Your Are Mature Enough! ")
    else:
        print("Your Need To Grow Up Kid! ")

n=int(input("Enter Your Age Please : "))
age_Check(n)
