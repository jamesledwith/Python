# program to valadate a username bu A00196141


# Prompt for username
username = input("Enter your username: ")

# Read username and check length,first char and is alphanumeric character
if  4 <= len(username) <= 8 and username[0].islower() and username.isalnum():
    # Output validation message 
    print("Valid username ")
elif len(username) < 4 :
    print("Invalid username: \n Too short - must have between 4 and 8 alphanumeric characters")
elif len(username) > 8 :
    print("Invalid username: \n Too long - must have between 4 and 8 alphanumeric characters")
elif username[0].isupper(): 
    print("Invalid username: \n Does not start with a lowercase letter")
elif not username.isalnum():
    print("Invalid username: \n Does not contain all alphanumeric characters")
else:
    print("Invalid username")





# Check length
# Check first char
# Check content
# Output validation message 
 
# Testing
# (Specify the inputs, expected outputs and actual outputs)
#  inputs: username
#  outputs: validation_message