tuple_check=(1, 2, 3, 4, 5)
print("The tuple is:", tuple_check)
#tuple_check(6, 7, 8)  # This line will raise a TypeError since tuples do not support item assignment
# The above line will raise an error, so we need to comment it out
tuple_check = tuple_check + (6, 7, 8)  # Adding elements to the tuple
print("The tuple after adding elements is:", tuple_check)
#tuple_check.append(9)  # This will raise an AttributeError since tuples are immutable
# print("The tuple after appending an element is:", tuple_check)  # This line will not execute
# The above line will raise an error, so we need to comment it out