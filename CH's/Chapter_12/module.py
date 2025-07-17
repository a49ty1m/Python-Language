"""__name__ and __main__"""
def my():
    print("Hello, World!")

if __name__ == "__main__":
    #This will only run if this file is run directly, not if it is imported
    my()
    print(__name__)
#this will print the name as main if this file is run directly, or the name of the module if imported after the hello world function is called
