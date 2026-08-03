n = int(input("Enter A Number:"))

table = [n * i for i in range(1, 11)]

for index, value in enumerate(table):
    print(f"{n} x {index + 1} = {value}")
