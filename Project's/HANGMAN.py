from os import truncate
import random

name = input("What is your name? : ")
def greet(name):
    print(f"Hello {name}, Welcome to the HANGMAN's Game")
greet(name)

wordlist = ["hacker", "devlop", "poetry", "master", "python", "cyborg", "smiloo", "bugbug", "random"]
secret_word = random.choice(wordlist)
print( secret_word)


word = []

for _ in range(len(secret_word)):
    word.append("_")
print(word)

game_over = False
while not game_over:
    guess = input("Guess The Letter:").lower()
    i=0 #score
    f=0 # fails
    for p in range(len(secret_word)): # p is possition (0,1,2,3,4,5)
        letter = secret_word[p]    # letter at the possition p
        i+=1
        if letter == guess:
            print("Possition is ", p+1)
            word[p] = letter
        else:  f+=1

    print(word)
    if "_" not in word:
        print ("You Won")
        print("Your Score Is : ",i)
        game_over= True
    if f == 6:
        print ("Too Many Tires, You Lost")
        game_over= True
