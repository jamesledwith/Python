# 
print("Program to check suitability for TV show")

age = int(input("Age"))

marital_status = input("Enter your marital status: ")

if ( 18 <= age <= 35 and marital_status == "Single"):
    print("You are suitable for the TV show")
else:
    print("You are not suitable for the TV show")
    

