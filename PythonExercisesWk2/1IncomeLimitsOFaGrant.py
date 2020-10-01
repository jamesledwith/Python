#print application description
print("This program displays the income limits for a full maintenance grant")


number_of_dependents = int(input("Number of dependents: "))

if(number_of_dependents < 4):
    print("The income Limit is: 39875")
elif(number_of_dependents >=4 and number_of_dependents <=7):
    print("The income Limit is: 43810")
elif(number_of_dependents >= 8):
    print("The income Limit is: 47575")
else:
    print("Number outside range")

