# 
print("Program to check suitability for TV show")


q_score = int(input("Enter your Q score: "))

age = int(input("Enter your age: "))

marital_status = input("Enter your marital status: ")

if ( 18 <= age <= 35 and marital_status == "single" or (q_score > 50) ):
    print("You are suitable for the TV show")
else:
    print("You are not suitable for the TV show")
    

