# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:49:37 2020

@author: James
"""
#open the file
with open ("Customer_Churn.csv") as file_in:
    # for every word in 
    for line in file_in:
        #split each line up and into variables seperated by a comma
        gender,tenure,phone_service,internet_service,contract,monthly_costs,total_charges,churn = line.split(",")
        
        tenure = float(tenure)
        
        #remove the blank spaces '\n'
        line = line.strip()
        #prints all the words in the documet
        print(line)
    