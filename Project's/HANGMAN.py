import random

name = input("What is your name?")
def greet(name):
    print(f"Hello {name}, Welcome to the HANGMAN's Game")
greet(name)


wordlist = ["hacker", "devlop", "protry", "master", "python", "cyborg", "smiloo", "bugbug", "random"]

secret_word = random.choice(wordlist)
print(secret_word)
guess = input("Guess The Word:").lower()

for letter in secret_word:
    if letter == guess:
        print("Correct Guess")
    else:
        print("Wrong guess")    
    