# 

print("This program calculates VAT")


price = float(input("Enter the price of your item: "))

category = input("Enter the category ")

if (category == "Standard"):
    tax = price * .23;
    total_price = tax + price;
    print(f"The tax due is {tax:.2f} and the total price is {total_price:.2f}")
elif (category == "Reduced"):
    tax = price * .135;
    total_price = tax + price;
    print(f"The tax due is {tax:.2f} and the total price is {total_price:.2f}")
elif (category == "Lower"):
    tax = price * .09;
    total_price = tax + price;
    print(f"The tax due is {tax:.2f} and the total price is {total_price:.2f}")
elif (category == "Livestock"):
    tax = price * .048;
    total_price = tax + price;
    print(f"The tax due is {tax:.2f} and the total price is {total_price:.2f}")
elif (category == "Exempt"):
    print(f"The tax due is 0% and the total price is {total_price:.2f}")
else:
    print("Invalid input")
