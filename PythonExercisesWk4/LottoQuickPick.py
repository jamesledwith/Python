# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:58:26 2020

@author: James
"""
# This program keeps randomly selecting numbers until we get 6 different ones

from random import randint

#empty list for the quick pick
qp_list = []

#while theres less than 6 numbers in the lis
while len(qp_list) < 6 :
    #randomly generate a number between 1 and 47
    random_num = randint(1,47)
    
    #if the numbers not in the quick pick list
    if random_num not in qp_list:
    #add the number to the quick pick list
        qp_list.append(random_num)

#sort list
qp_list.sort()

#print teh sorted numbers in list
print(qp_list)