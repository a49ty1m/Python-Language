s=set()
s.add(10)
s.add(10.0)
s.add("10")
s.add("10.0")
print("The Set of Numbers is:", s)
# The Set of Numbers is: {10, '10', '10.0'} because 10 and 10.0 are considered the same number in Python, but "10" and "10.0" are different strings.
