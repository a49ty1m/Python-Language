import random

name = input("What is your name?")
def greet(name):
    print(f"Hello {name}, Welcome to the HANGMAN's Game")
greet(name)


wordlist = ["hacker", "devlop", "protry", "master", "python", "cyborg", "smiloo", "bugbug", "random"]

print("So the word is of 6 letters")
word = []
print(word)

secret_word = random.choice(wordlist)
print(secret_word)


guess = input("Guess The Word:").lower()

for _ in secret_word:
    if _ == guess:
        print("Correct Guess")
        word.append(_)
    else:
        print("Wrong guess") 
        word.append("_")   
    
print(word)