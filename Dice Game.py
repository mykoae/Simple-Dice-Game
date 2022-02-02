
# this code is about the dice game
# automatically loads the dice values
import random

min = 1
max = 6
print("enter the player names")
player1 = input()
player2 = input()
print("input yes if you wanted to roll the dice")


def dice():
    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are....")
        print(player1 + " " + str(random.randint(min, max)), str(random.randint(min, max)))
        print(player2 + " " + str(random.randint(min, max)), str(random.randint(min, max)))
        break;


roll_again = input()
dice()
print("do you want to roll the dice again then input Yes")
roll_again = input()
if roll_again == "yes" or roll_again == "y":
    dice()
else:
    exit(0)
dice()
