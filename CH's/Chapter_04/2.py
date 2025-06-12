marks = []

for i in range(6):
    Mi=input(f"Enter {i+1} Student marks: ")
    marks.append(Mi)
print("The Marks of Students are:", marks)
marks.sort()
print("The Sorted Marks of Students are:", marks)