#This program will convert power to dBM, or dBm to power, based off user's choice
from math import log10

print("Program for Power Ratio Conversions ")
print("1. Power to dPm")
print("2. dBm to Power")

choice = int(input("Enter your choice: "))

if choice == 1:
    milliwatts_power = float(input("Enter Power in milliwatts: "))
    power_ratio_dec = 10 * log10(milliwatts_power)
    print(f"Power ratio in milliwatts: {power_ratio_dec:0f}")
elif choice == 2:
    decibels = float(input("Enter Power Ratio in decibels: "))
    power = 10 (pow(decibels / 10))
else:
    print("Invalid choice")


 
