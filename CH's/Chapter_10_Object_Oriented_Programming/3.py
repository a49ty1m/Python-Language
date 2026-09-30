class demo:
    a=10
o=demo()
print(o.a)#this will print the class variable 'a' from the class 'demo'
o.a = 20  # Modifying class variable using instance
#this will change the value of the class variable 'a' for this instance only
print(o.a)  #this will print the instance variable 'a' from the instance 'o'