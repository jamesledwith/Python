# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 12:10:39 2020

@author: James
"""
import string 
from random import randint 
from random import choice 

print("This program generates password") 
 
firstWord = input("Enter the first word: ") 
secondWord = input("Enter the second word: ") 
randDigit = randint(0,9) 
randPunctuation = choice(string.punctuation) 

print(f"{firstWord}{randDigit}{secondWord}{randPunctuation}") 
