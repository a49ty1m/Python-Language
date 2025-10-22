N = int(input("Enter a number to display its multiplication table: "))
table = [str(N*i) for i in range(1, 11)] # we can use i in 2 different things on the same line which is called as list comprehension
print(", ".join(table))
