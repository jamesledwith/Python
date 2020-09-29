# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:10:39 2020

@author: James
"""
from random import randint 

print("This program simulates rolling 2 dice") 

random1 = randint(1,6) 
random2 = randint(1,6) 
total =  random1 + random2 

print("First number: ", random1) 
print("Second number: ", random2) 
print("Total: ", total) 
