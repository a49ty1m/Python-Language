a1=int(input("Enter first number: "))
a2=int(input("Enter second number: "))
a3=int(input("Enter third number: "))
a4=int(input("Enter fourth number: "))
a5=int(input("Enter fifth number: "))
if (a1<=a2 and a1<=a3 and a1<=a4 and a1<=a5):
    print(f"The smallest number is {a1}")
elif (a2<=a1 and a2<=a3 and a2<=a4 and a2<=a5):
    print(f"The smallest number is {a2}")
elif (a3<=a1 and a3<=a2 and a3<=a4 and a3<=a5):
    print(f"The smallest number is {a3}")
elif (a4<=a1 and a4<=a2 and a4<=a3 and a4<=a5):
    print(f"The smallest number is {a4}")
else:
    print(f"The smallest number is {a5}")
# This code takes five integer inputs from the user and determines the smallest number among them.