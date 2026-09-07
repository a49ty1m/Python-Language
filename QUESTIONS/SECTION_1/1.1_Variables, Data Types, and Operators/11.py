# Demonstrate bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) on small integers and explain each result.

inp1 = int(input("Enter the first number : "))
inp2 = int(input("Enter the second number : "))

print(f"Bitwise AND : {inp1 & inp2}")
print(f"Bitwise OR : {inp1 | inp2}")
print(f"Bitwise XOR : {inp1 ^ inp2}")
print(f"Bitwise NOT : {~inp1}")
print(f"Bitwise Left Shift : {inp1 << inp2}")
print(f"Bitwise Right Shift : {inp1 >> inp2}")
