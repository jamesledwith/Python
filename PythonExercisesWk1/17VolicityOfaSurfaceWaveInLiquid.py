# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:09:31 2020

@author: James
"""
from math import sqrt, tanh, pi

print("This program calculates the velocity of a surface wave in liquid");

gravity = float(input("Enter the gravity: "))
wavelength = float(input("Enter the wavelength: "))
density = float(input("Enter the density: "))
surfaceTension = float(input("Enter the surface tension: "))
depth = float(input("Enter the depth: "))

velocity = sqrt( ((gravity * wavelength) / (2 * pi) + (2 * pi * surfaceTension) / (density * wavelength) ) * tanh(2 * pi * depth / wavelength) )

print(f"The velocity is: {velocity:.2f}")
