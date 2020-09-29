# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:09:31 2020

@author: James
"""
import math;

print("This program calculates the velocity of a surface wave in liquid");

g = float(input("Enter the gravity: "));
w = float(input("Enter the wavelength: "));
d = float(input("Enter the density: "));
s = float(input("Enter the surface tension: "));
d = float(input("Enter the depth: "));

velocity = math.sqrt( ( ((g * w) / (2 * math.pi)) + ((2 * math.pi * s) / (d * w)) ) 
                     * (math.tanh( (2 * math.pi * d) / w)));

print(f"The velocity is: {velocity:.2f}");
