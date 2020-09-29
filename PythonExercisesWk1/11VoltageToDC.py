# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:59:21 2020

@author: James
"""
import math;

print("This program calculates the Voltage in a DC Circuit");

power = int(input("Enter the power: "));
resistance = int(input("Enter the resistance: "));
voltage = math.sqrt(power * resistance);

print(f"Voltage is {voltage}");
