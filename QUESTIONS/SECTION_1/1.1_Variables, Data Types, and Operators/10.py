# Explain the difference between `==` and `is`; give one example where they produce different results.

list_1 = [1,2,3,4,5]
list_2 = [1,2,3,4,5]
list_3 = list_1

print(f"id of list_1 : {id(list_1)}")
print(f"id of list_2 : {id(list_2)}")
print(f"id of list_3 : {id(list_3)}")

print(f"\ncomparison operator\n")
print(f"list_1 == list_2 : {list_1 == list_2}") # true because it checks the values of list_1 and list_2
print(f"list_1 is list_2 : {list_1 is list_2}") # false because it checks the memory address of list_1 and list_2
print(f"list_2 is list_3 : {list_2 is list_3}") # true because it checks the memory address of list_2 and list_3

print("\nidentity operator\n")
print(f"list_1 is not list_2 : {list_1 is not list_2}") # true because it checks the memory address of list_1 and list_2
print(f"list_1 is not list_3 : {list_1 is not list_3}")
print(f"list_2 is not list_3 : {list_2 is not list_3}")
