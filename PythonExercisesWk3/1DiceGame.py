#sixes bet game , will the player roll a six in four rolls?
from random import randint

count = 0;

while True:
    dice_roll = randint(1,6)
    count = count + 1
    
    print(f"Number of rolls: {count} \n  Die number: {dice_roll}")
    
    if dice_roll == 6:
        print(f"Congrats you got a six on the {count} roll")
        break 
    elif count == 4:
        print("Sorry you didnt get a six in four rolls")
        break

