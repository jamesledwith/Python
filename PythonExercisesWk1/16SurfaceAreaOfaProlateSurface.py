# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:02:45 2020

@author: James
"""
from math import sqrt, asin, pi

print("This program calculates the surface area of a prolate_spheroid")

a = int(input("Enter the semi-axis a: "))
b = int(input("Enter the semi-axis b: "))

e = sqrt( (a * a) - (b * b) ) / a
s = (2 * pi * b) * (b + ((a * asin(e)) / e))

print(f"The surface area is: {s:.2f}")
