# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:49:37 2020

@author: James
"""

# create empty lists 
gender_list = []
tenure_list = []
phone_services_list = []
internet_service_list = []
contract_list = []
monthly_costs_list = []
total_charges_list = []
churns_list = []

#open the file
with open ("Customer_Churn.csv") as file_in:
    header_values = file_in.readline()
    # for every word in 
    for line in file_in:
        #split each line up and into variables seperated by a comma
        gender,tenure,phone_service,internet_service,contract,monthly_costs,total_charges,churn = line.split(",")
        
        tenure = int(tenure)
        
        # add the values in the dataset to their respective lists
        gender_list.append(gender)
        tenure_list.append(tenure)
        phone_services_list.append(phone_service)
        internet_service_list.append(internet_service)
        contract_list.append(contract)
        monthly_costs_list.append(monthly_costs)
        total_charges_list.append(total_charges)
        churns_list.append(churn)
        
    
    #maximum tenure 
    tenure_max = max(tenure_list)
    #minimum tenure 
    tenure_min = min(tenure_list)
    #get averages for the numeric values (average is total/number of values)
    tenure_avg = sum(tenure_list) / len(tenure_list)
    #mode of tenure
    
    #median of tenure
    tenure_list.sort()
    mid_index = int(len(tenure_list)/2)
    
    if len(tenure_list) % 2 == 1:
        median = tenure_list[mid_index]
    else:
        median = tenure_list(tenure_list[mid_index -1 ] + tenure_list[mid_index + 1])/2
        
        
    
    print(f"The average tenure is {tenure_avg}")
    print(f"The minimum tenure is {tenure_min}")
    print(f"The maximum tenure is {tenure_max}")
    print(f"The median of tenure is {median}")
    
    #remove the blank spaces '\n'
    line = line.strip()
    #prints all the words in the documet
    print()
    