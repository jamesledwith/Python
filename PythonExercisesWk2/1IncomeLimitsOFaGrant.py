#print application description
print("This program displays the income limits for a full maintenance grant")

#input number of dependents
number_of_dependents = int(input("Number of dependents: "))

#set income for number of dependents
if number_of_dependents < 4:
    print("The income Limit is: 39875")
elif number_of_dependents <= 7:
    print("The income Limit is: 43810")
else:
     print("The income Limit is: 47575")

