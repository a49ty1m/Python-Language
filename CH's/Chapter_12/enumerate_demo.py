# Demonstrating how enumerate works internally

my_list = ['apple', 'banana', 'cherry']

print("What enumerate actually returns:")
for item in enumerate(my_list):
    print(f"enumerate returns: {item}")
    print(f"Type: {type(item)}")
    print(f"First element (index): {item[0]}")
    print(f"Second element (value): {item[1]}")
    print("---")

print("\nUsing tuple unpacking:")
for index, value in enumerate(my_list):
    print(f"index={index}, value={value}")

print("\nWhat happens if we swap the variable names:")
for value, index in enumerate(my_list):
    print(f"'value' variable contains: {value}")
    print(f"'index' variable contains: {index}")
    print("Notice how the variable names don't change what enumerate returns!")
