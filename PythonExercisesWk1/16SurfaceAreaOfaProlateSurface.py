# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:02:45 2020

@author: James
"""
import math;

print("This program calculates the surface area of a prolate_spheroid");

a = int(input("Enter the semi-axis a: "));
b = int(input("Enter the semi-axis b: "));

e = math.sqrt( (a * a) - (b * b) ) / a;
s = (2 * math.pi * b) * (b + ((a * math.asin(e)) / e));

print(f"The surface area is: {s:.2f}");
