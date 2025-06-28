def check(x,y,z):
    if(x>y and x>z):
        print(f"{x} is The Largest Number")
    elif(y>x and y>z):
        print(f"{y} is The Largest Number")
    else:
        print(f"{z} is The Largest Number")
#this program checks which of the three numbers is the largest.
a=int(input("Enter First Number: ") )
b=int(input("Enter Second Number: ") )
c=int(input("Enter Third Number: ") )

check(a,b,c)