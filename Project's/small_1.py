print('''
i have taken 
1 for snake
0 for water
-1 for gun
now 
''')
choi={1: "snake", 0: "water", -1: "gun"}
import random

from requests import get
choices = [1, 0, -1]  # snake, water, gun
computer_choice = random.choice(choices)

# The above code randomly selects a choice from the list of choices (1, 0, -1) and prints the corresponding string value (snake, water, gun) based on the computer's choice.
c = int(input("Enter your choice (1 for snake, 0 for water, -1 for gun): "))
if c == computer_choice:
    print("Draw")
elif c == 1 and computer_choice == 0:
    print("You win! Snake beats Water")
elif c == 0 and computer_choice == 1:
    print("You lose! Snake beats Water") 
elif c == -1 and computer_choice == 1:
    print("You win! Gun Beats Snake")
elif c == 1 and computer_choice == -1:
    print("You lose! Gun beats Snake")
elif c == 0 and computer_choice == -1:
    print("You win! Water beats Gun")
elif c == -1 and computer_choice == 0:
    print("You lose! Water beats Gun")
else:
    print("Invalid choice")
print("Your choice:", choi.get((c), "Invalid choice"))

print("Computer choice:", choi[computer_choice])



'''
import random

1 for snake
-1 for water 
0 for gun

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (variables), you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): 
        print("You win!")

    elif(computer ==-1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer ==1 and you == 0):
        print("You Win!")

    elif(computer ==0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")
'''