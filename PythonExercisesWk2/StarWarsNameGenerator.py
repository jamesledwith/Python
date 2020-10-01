# Program to generate a Star Wars name by A00196141
  
   
  
# Input firstname
firstname = input ("Enter your firstname: ")

# Input lastname
lastname = input ("Enter your lastname: ")

# Input mother_maiden_name
mother_maiden_name = input ("Enter your mother's maiden name: ")

# Input birthplace
birthplace = input ("Enter your birthplace: ")

# Generate stars_wars_name
starwars_firstname = firstname[:3] + lastname[:2]
starwars_lastname = mother_maiden_name[:2] + birthplace[:3]
starwars_name = (starwars_firstname + " " + starwars_lastname).title()

# Print stars_wars_name
print("Your Star Wars name is ", starwars_name)



# Inputs: firstname, lastname, mother's maiden name, birthplace
# Output: star wars name
# Processing: Input firstname, Input lastname, Input mother_maiden_name
# Input birthplace, Generate starwars_name, Print starwars_name