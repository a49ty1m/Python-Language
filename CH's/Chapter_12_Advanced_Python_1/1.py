try :
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
    #this will catch the error and print a message instead of crashing the program
    print("Please make sure if the file exists.")
    #normally this will print the content of the file if it exists
    #but if the file does not exist, it will raise a FileNotFoundError
try :
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
    #this will catch the error and print a message instead of crashing the program
    print("Please make sure if the file exists.")
try :
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(f"An error occurred: {e}")
    #this will catch the error and print a message instead of crashing the program
    print("Please make sure if the file exists.")
print("Thank You")
    
