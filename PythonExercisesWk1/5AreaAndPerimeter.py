# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:17:50 2020

@author: James
"""

print("This program calculates the area and perimeter of a rectangle")

length = float(input("Enter the length in meters: "));
width = float(input("Enter the width in meters: "));
area = length * width;
perimeter = 2* (length + width);

print("The area is ", area, " square meters");
print("The perimeter is ", perimeter, " meters");
