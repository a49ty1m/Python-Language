n = int(input("Enter The Number You Want Table of : "))
for i in range (11):
    num = n * (10-i)
    print(f"{n} * {10-i} = {num}")
# this code prints the table of a number in reverse order
# for example if the user inputs 5, it will print:
# 5 * 10 = 50
# 5 * 9 = 45
# 5 * 8 = 40
# 5 * 7 = 35
# 5 * 6 = 30
# 5 * 5 = 25
# 5 * 4 = 20
# 5 * 3 = 15
# 5 * 2 = 10
# 5 * 1 = 5
# 5 * 0 = 0
