#This is a simple number guessing game in Python.
#The user has to guess a number between 0 and 100.
from random import randint
print("Welcome to The Number Guessing Game")
sec_no= randint(0,100)
#This is the secret number that the user has to guess
#The number is randomly generated between 0 and 100
print("The Secret Number is Generated Between 0-100")
#The user has to guess the number
#The user has to input a number between 0 and 100
print(sec_no)
i=0#this is For The Score
a=-1#This is For The Initialization of Number
while (a != sec_no):
    #this is the main loop of the game
    #The user has to input a number between 0 and 100
    #The user has to guess the number
    #The user has to input a number between 0 and 100
    #this will continue until the user guesses the number
    a = int(input("Enter You Guess Number Between (0-100) : "))
    
    if(a>sec_no):
        print("You Guessed a Larger Number Please Guess a Smaller One! ")
    elif(a<sec_no):
        print("You Guessed a Smaller Number Please Guess a Larger One! ")
    else:
        print(f"Congratulation! \nYou Guessed The Right Number Which was {sec_no} \nYou Won The Game")
    i+=1
print(f"Your Took {i} Attempts to Guess The Right Number")



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''# This is another version of the number guessing game in Python.
import random
n = random.randint(1, 100) 
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")
'''