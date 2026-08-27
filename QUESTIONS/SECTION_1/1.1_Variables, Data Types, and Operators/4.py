# Write a program that converts a user-entered age from a string to an integer safely (handle `ValueError`).

age = input("Enter your age : ")
try: 
    age = int(age)
    print(f"age = {age}\ndtype of age = {type(age)}")
except ValueError:
    print("Invalid age")