# Use augmented assignment operators (`+=`, `-=`, `*=`, `//=`, `**=`, `%=`) inside a loop.

def augmented_assignment_operators(a, b):

    a += b # a = a + b
    print(f"a = {a}")
    a -= b # a = a - b
    print(f"a = {a}")
    a *= b # a = a * b
    print(f"a = {a}")
    a //= b # a = a // b
    print(f"a = {a}")
    a **= b # a = a ** b
    print(f"a = {a}")
    a %= b # a = a % b
    print(f"a = {a}")


x = 10
y = 2

print(f"Initial value of a : {a}")
print(f"Initial value of b : {b}")

augmented_assignment_operators(x, y)
