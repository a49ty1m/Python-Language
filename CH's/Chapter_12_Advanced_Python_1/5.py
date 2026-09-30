n = int(input("Enter A Number:"))

table = [n * i for i in range(1, 11)]
with open('table.txt', 'w') as file:
    for index, value in enumerate(table):
        file.write(f"{n} x {index + 1} = {value}\n")
