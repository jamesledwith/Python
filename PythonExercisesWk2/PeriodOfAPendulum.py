# Program to calculate the period of a pendulum by A00196141

from math import pi, sqrt

   
#acceleration due to gravity
gravity = 9.81

# Input length of the pendulum
length = float(input("Input the length of the pendulum in metres: "))

# Generate period (in secs) to complete a cycle
time = 2 * pi * sqrt(length / gravity)

# Print the time to two decimals
print(f"The time is {time:.2f}")



# Input: length , gravity
# Output: time
# Processing: Input gravity, Input length, Generate time, Print time