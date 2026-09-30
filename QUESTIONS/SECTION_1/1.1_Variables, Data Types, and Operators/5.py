# Check whether a student is eligible for placement when CGPA is at least 7 and there are no backlogs.

def check_eligible(cgpa,backlogs):
    if cgpa >= 7 and backlogs == 0:
        return True
    return False

cgpa = float(input("Enter CGPA: "))
backlogs = int(input("Enter backlogs: "))

if check_eligible(cgpa,backlogs):
    print("Eligible for placement")
else:
    print("Not eligible for placement")
    
    