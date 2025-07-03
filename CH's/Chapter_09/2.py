import random
def game():
    print("Welcome to the game!")
    print("Your are Playing a Game")
    score = random.randint(1, 100)
    # This is a random score generator
    print(f"Your score is: {score}")
    #this is a random generated score
    with open("CH's/Chapter_09/score.txt",) as f:
        hi_score = f.read()
    #here we are reading the high score from the file
    if (hi_score == ""):
        hiscore = 0
    #if the file is empty then we will set the high score to 0
    else:
        hiscore = int(hi_score)
    #if the file is not empty then we will convert the high score to integer
    #because the high score is stored as a string in the file
    if (score > hiscore):
        print("congratulations! You have a new high score!")
        with open("CH's/Chapter_09/score.txt", "w") as f:
            f.write(str(score))
    #here we are checking if the score is greater than the high score
    #if it is then we will write the new high score to the file
        print(f"Your score: {score}, High score: {score}")
    #we will print the score and the high score
    else:
        print("You did not beat the high score.")
        print(f"Your score: {score}, High score: {hiscore}")
    #if the score is not greater than the high score then we will print the score and the high score


game() 