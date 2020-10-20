# Exercise 1: Guess the Number by A00196141 

from random import randint

random_number =randint(1,100)
print("I'm thinking of a number between 1 and 100. Try to guess it.")

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
        print("Game Over")
        break