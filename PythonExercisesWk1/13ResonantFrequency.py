# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 13:12:01 2020

@author: James
"""
import math

print("This program calculates the Resonant frequency of an LC Circuit")

inductance = float(input("Enter the inductance: "))
capacitance = float(input("Enter the capacitance: "))

resonantFrequency = (1 / (2 * math.pi * (math.sqrt(inductance * capacitance))))

print(f"Resonant Frequency is {resonantFrequency:.3f}")
