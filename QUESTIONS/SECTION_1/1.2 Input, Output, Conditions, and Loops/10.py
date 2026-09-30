# Build a number-guessing game that reports "Too High" or "Too Low" until the answer is correct.
import random
def random_generate(low:int,high:int) -> int:
    generate = random.randint(low,high)
    return generate\

def game_logic(my_guess:int,generate:int) -> int:
    guesses = 0
    while (my_guess := int(input("Enter your guess : "))) != generate:
        if my_guess < generate:
            print("Too Low")
        else:
            print("Too High")
        guesses += 1
    return my_guess, guesses
    
start_limit = int(input("Enter the Staring Limit : "))
end_limit = int(input("Enter the Ending Limit : ")) 

guess = game_logic(0,random_generate(start_limit,end_limit))
    
