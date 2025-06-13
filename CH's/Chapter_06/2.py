d={}
n = int(input("Enter the number of subjects: "))
for i in range (n):
    subject = input(f"Enter {i+1} subject name: ")
    marks = int(input(f"Enter {i+1} marks of subject out of 100: "))
    d[subject] = marks
print("The Dictionary of Subjects with their marks is:", d)
print("the average marks is:", ((sum(d.values())/len(d))), "%")
if all(marks >= 33 for marks in d.values()):
    if (sum(d.values())/len(d)) >= 40:
        print("You are Pass Your average marks is:", (sum(d.values())/len(d)), "%")
    else:
        print("You are Fail Beause Your Average Marks is:", (sum(d.values())/len(d)), "%")
        print("Which is Less Than 40 marks in average of subjects")
else:
    print("You are Fail because you have less than 33 marks in one or more subjects")
'''
marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)
    '''