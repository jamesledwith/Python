# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:13:08 2020

@author: James
"""
print ("This program demonstrates the features of strings");

wordEntered = input ("Enter a sentence: " );
print("Number of characters: ", str(len(wordEntered)));

print("First character : ", wordEntered[0]);
print("Last character : ", wordEntered[-1]);
print("Uppercased : ", wordEntered.upper());
print("Lowercased : ", wordEntered.lower());
print("Titled : ", wordEntered.title());
print("Swapcased : ", wordEntered.swapcase());
print("Number of Spaces : ", wordEntered.count(" "));

