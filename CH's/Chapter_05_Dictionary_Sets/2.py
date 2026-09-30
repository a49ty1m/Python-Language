s=set()
for i in range(10):
    n=int(input(f"Enter {i+1} number: "))# if we don't convert to int, it will be a string and will add all same numbers as strings
    s.add(n)
print("The Set of Numbers is:", s)