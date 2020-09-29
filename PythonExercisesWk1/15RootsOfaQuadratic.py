# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:51:18 2020

@author: James
"""
import math;

print("This program calculates the roots of a quadratic equation");

a = int(input("Enter the coefficient of a: "));
b = int(input("Enter the coefficient of b: "));
c = int(input("Enter the coefficient of c: "));

determinant = math.sqrt( ((b * b) - (4 * a * c)) );

root1 = (-b + determinant) / (2 * a);
root2 = (-b - determinant) / (2 * a);

print(f"The solutions are {root1} and {root2}");

