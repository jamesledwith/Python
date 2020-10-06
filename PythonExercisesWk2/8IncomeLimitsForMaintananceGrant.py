# 
print("This program displays the income limits for a full maintenance grant")

number_of_dependents = int(input("Number of dependents: "))


income = int(input("Input income: "))


if number_of_dependents < 4 and income < 39875:
    print("You are eligible for a full maintenance grant")
elif 4 <= number_of_dependents <= 7 and income < 43810:
    print("You are eligible for a full maintenance grant")
elif number_of_dependents >= 8 and income < 47575:
    print("You are eligible for a full maintenance grant")
else:
    print("You are not eligible for the maintenance grant")

