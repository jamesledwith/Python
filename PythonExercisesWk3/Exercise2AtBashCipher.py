#

from string import ascii_lowercase
#create an empty string for the choice and cypherletters
choice = " "
cypherletters = " "

while choice != "q": 
    choice = input("Enter a message to encipher or q to quit: ")
    
    #for each character in the users input, converted to lowercase 
    for letter in choice.lower():
        
        # if it's a letter
        if letter.islower():
            #reverse the letter
            letter_index = ascii_lowercase.index(letter)
            reversed_letter_index = 25 - letter_index
            #cypherletters = 
            print(reversed_letter_index)
            
            
            
            
            
            
            
            
            
            
      
        #    print(reversed_letter_index)
        # # if the character is not alphanumeric
        # if not letter.isalpha():
        #     continue # skip the character
        # else:
        #     #get index of input
        #     index = ascii_lowercase.index(letter)
            
        #     #find the index at the other side of the alphabet
        #     reverse_index = 25 - index
            
        #     #new index
           
        #     print(str(reverse_index))
    
        
    
        
    