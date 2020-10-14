# Guess the Number is a simple guessing game.  
# The computer “thinks” of a number, and the player has ten attempts to guess it.  
# If the player guesses the number, s/he wins.  
# Otherwise, the computer tells the player if the guess was too high or too low, 
# and s/he can guess again.

from random import randint

random_number =randint(1,10)

while(True):
    for i in range(10):
        guess = int(input("Enter your guess: "))
        
        if guess > random_number:
            print("Too high, try again.")
        elif guess < random_number:
            print("Too low, try again.")
        elif guess == random_number:
            print("You guessed it! ")
            break
        
    play_again = input("Play again (y/n)? ")
    
    if play_again == "n":
        break