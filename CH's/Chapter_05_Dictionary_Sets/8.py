d={}

for i in range(5):
    name= input(f"Enter {i+1} name of student: ")
    marks= int(input(f"Enter {i+1} marks of student: "))
    d.update({name:marks})
print("The Dictionary of Students with their marks is:", d)
print(d.items())
print(d.keys())
print("The Dictionary of student with their marks in soreted order is:", sorted(d.values()))

# if keys are same, it will update the value of that key 
# if values are same, it will not update the key, it will add the key with the same value