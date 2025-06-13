'''
basic 
un = input("Enter your username please: ")
if len(un) < 10:
    print("Username must be at least 10 characters long.")
else:
    print("Username is valid.")
    # This code checks if the username is at least 10 characters long and prints a message accordingly.
    '''

while True:
    un = input("Enter your username please: ")
    if len(un) < 10:
        print("Username must be at least 10 characters long.")
    else:
        print("Username is valid.")
        break
# This code checks if the username is at least 10 characters long and continues to prompt until a valid username is entered.