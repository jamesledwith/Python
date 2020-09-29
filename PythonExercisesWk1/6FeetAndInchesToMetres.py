# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 21:40:44 2020

@author: James
"""

print("This program converts a distance in feet and inches to metres")

feet = float(input("Enter the number in feet: "));
inches = float(input("Enter the number in inches: "));

totalInches = feet * 12 + inches;
centimetres = totalInches * 2.54;
metres = centimetres / 100;

print("The distance in metres is ",  f"{metres:.4f}", " meters");