
# Here are the rules of the game:

# The player should roll two dice.
# If the sum of both of them is 7 or 11 the player wins.
# If the sum is 2, 3 or 12 (craps) the casino wins. 
# If during the first roll the sum is 4, 5, 6, 8, 9 or 10, that number becomes the “goal” number. 
# To win, the player should roll the dice till they roll the goal number again. 
# If the player rolls a 7 before rolling the goal number, they lose. 


# Your task is to recreate this game using Python.
# Your program should roll two dice and output the sum of two random numbers. 
# By following the rules of the game, your program should decide whether the player wins or loses. 
# Please make sure :
#     The program is written only on Python 
#     You use “Random” library 
#     You use the while loop, conditions, print function and functions you create


import random

def roll(goal):
    sum = random.randint(1, 6) + random.randint(1, 6)
    print(f"dice total is: {sum}")
    if sum == 2 or sum == 3 or sum == 12 or (goal and sum == 7):
        print("Casino Wins")
        exit(0)
    elif sum == 7 or sum == 11 or (goal and sum == goal):
        print("You Win")
        exit(0)
    elif goal == 0:
        goal = sum
        print(f"the goal number is: {goal}")
    return goal
        
def main():
    goal = 0
    while(True):
        key = input("press ENTER to roll")
        if not key:
            goal = roll(goal)
        else:
            continue
    
main()