# Swap two variables with and without using a temporary variable.

def swap_using_temp(x : int,y: int) -> tuple[int,int]:
    temp = y
    y = x
    x = temp
    return x,y

def swap_without_temp(x: int, y: int) -> tuple[int, int]:
    x = x + y
    y = x - y
    x = x - y
    return x, y

def swap_pythonic(x: int, y: int) -> tuple[int, int]:
    x, y = y, x
    return x, y


a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))

print(swap_using_temp(a,b))
print(swap_without_temp(a,b))
print(swap_pythonic(a,b))
