# Take two numbers as input and display their addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.

num1= float(input("Enter Your First Number : "))
num2= float(input("Enter Your Second Number : "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
mod = num1 % num2
exp = num1 ** num2

print(f"Addition is : {add}")
print(f"Subtraction is : {sub}")
print(f"Multiplication is : {mul}")
print(f"Division is : {div}")
print(f"Floor Division is : {floor_div}")
print(f"Modulus is : {mod}")
print(f"Exponentiation is : {exp}") 