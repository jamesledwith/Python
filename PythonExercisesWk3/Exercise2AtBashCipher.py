#Exercise 2: AtBash Cipher by A00196141

from string import ascii_lowercase
#create an empty string for the choice 
choice = ""

while choice != "q": 
    cypherletters = ""
    choice = input("Enter a message to encipher or q to quit: ")
    #for each character in the users input, converted to lowercase 
    for letter in choice.lower():
        
        # if it's a lowercase letter
        if letter.islower() :
            # get the users letters position
            letter_index = ascii_lowercase.index(letter)
            # get the reversed alphabet letter
            reversed_letter = ascii_lowercase[25 - letter_index]
            # add all cyperletters together to make the cypherword
            cypherletters = cypherletters + reversed_letter
        elif letter == " ":
            cypherletters += " "
    
    print("Encrypted message is:", cypherletters)