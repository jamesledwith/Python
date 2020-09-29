# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:33:44 2020

@author: James
"""
import math;

print("This program calculates the distance between two points");

x1 = int(input("Enter the x-coordinate of the first point: "));
y1 = int(input("Enter the y-coordinate of the first point: "));
x2 = int(input("Enter the x-coordinate of the second point: "));
y2 = int(input("Enter the y-coordinate of the second point: "));

distance = math.sqrt( ((x2 - x1) ** 2 ) + ((y2 - y1) ** 2) );

print(f"Resonant Frequency is {distance:.2f}");
