# A program of the game ChoHan by A00196141
from random import randint


# input the players guess
player_guess = input("Enter your guess (even or odd): ")

# roll the first dice 
dice_roll_1 = randint(1,6) 

# roll the second dice
dice_roll_2 = randint(1,6) 

#total of the two dice rolls
total = dice_roll_1 + dice_roll_2

#checks if a number is odd
odd = total % 2 == 1

#checks if a number is even
even = total % 2 == 0

# check if the guess was correct or wrong
if (even and player_guess == "even"):
    print(f"Dice rolls: {dice_roll_1} and {dice_roll_2} Total is {total}")
    print("You guessed right")
elif (odd and player_guess == "even"):
    print(f"Dice rolls: {dice_roll_1} and {dice_roll_2} Total is {total}")
    print("You guessed wrong")
elif (odd and player_guess == "odd"):
    print(f"Dice rolls: {dice_roll_1} and {dice_roll_2} Total is {total}")
    print("You guessed right")
elif (even and player_guess == "odd"):
    print(f"Dice rolls: {dice_roll_1} and {dice_roll_2} Total is {total}")
    print("You guessed wrong")
else:
    print("Invalid answer")