# program to valadate a username bu A00196141
# Inputs:
# username
 
# Outputs:
# validation_message 
 
# Processing Steps:
# Outline the logic of the program in plain english/pseudocode. Do not write Python code here
# Prompt for username
username = input("Enter your username: ")

# Read username
if  4 <= len(username) <= 8 and username[0].islower() and username.isalnum():
    print("Valid username ")
elif len(username) < 4 :
    print("Username Invalid:  Too short - must have between 4 and 8 alphanumeric characters")
elif len(username) > 8 :
    print("Username Invalid:  Too long - must have between 4 and 8 alphanumeric characters")
elif username[0].isupper(): 
    print("Does not start with a lowercase letter")
elif not username.isalnum():
    print("Does not contain all alphanumeric characters")
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