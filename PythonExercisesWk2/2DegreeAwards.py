
print("This program displays the grade awarded based on average mark")

average_mark = int(input("Enter average mark: "))


if 70 <= average_mark <= 100 :
    print("First Class Honours")
elif 60 <= average_mark < 70:
    print("2nd Class Honours, Grade 1")
elif 50 <= average_mark < 60:
    print("2nd Class Honours, Grade 2")
elif 40 <= average_mark < 50:
    print("Pass")
elif 0 <= average_mark < 40:
    print("No Award")
else:
    print("Number outside range")

