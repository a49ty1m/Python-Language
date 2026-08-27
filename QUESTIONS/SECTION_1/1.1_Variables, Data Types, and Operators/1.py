# Create variables for a student's name, age, room number, and CGPA. Print both their values and data types.

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
room_num = int(input("Enter Your Room_Number : "))
cgpa = float(input("Enter Your CGPA : "))


print(f"Name is {name} and its datatype is {type(name)}")
print(f"Age is {age} and its datatype is {type(age)}")
print(f"Room_Number is {room_num} and its datatype is {type(room_num)}")
print(f"CGPA is {cgpa} and its datatype is {type(cgpa)}")