num_list = []

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)
print("The List of Numbers are:", num_list)
print("Sum of Numbers List is ", sum(num_list))