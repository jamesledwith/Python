# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:10:33 2020

@author: James
"""
print("This program generates a username from a user's fullname") 
 
fullName = input("Enter your name in the format firstname lastname: ") 
firstName, lastName = fullName.split(" ") 
print(firstName.lower() + lastName[0].lower()) 