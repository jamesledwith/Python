# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:49:37 2020

@author: James
"""
import math

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
        
    
    tenure_max = max(tenure_list)
    tenure_min = min(tenure_list)
    tenure_mean = sum(tenure_list) / len(tenure_list)

    #median of tenure
    tenure_list.sort()
    mid_index = int(len(tenure_list)/2)   
    if len(tenure_list) % 2 == 1:
        median = tenure_list[mid_index]
    else:
        median = tenure_list(tenure_list[mid_index -1 ] + tenure_list[mid_index + 1])/2

    #mode of tenure    
    cnt = []
    for num in tenure_list:
        cnt.append(tenure_list.count(num))
    unique_count = []  
    for num in cnt:
        if num not in unique_count:
            unique_count.append(num)  
    if len(unique_count) > 1:
        m = []
        for num in list(range(len(cnt))):
            if cnt[num] == max(unique_count):
                m.append(tenure_list[num])
        mode = []
        for num in m:
            if num not in mode:
                mode.append(num)
    #https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list

    #calculate variance
    var = sum(pow(num - tenure_mean, 2) for num in tenure_list) / len(tenure_list)
    #standard deviation of tenure
    standard_deviation = math.sqrt(var)
    #https://stackoverflow.com/questions/24023927/computing-standard-deviation-without-packages-in-python
    
    print(f"The average tenure is {tenure_mean:0.2f} months")
    print(f"The minimum tenure is {tenure_min} months")
    print(f"The maximum tenure is {tenure_max} months")
    print(f"The median of tenure is {median} months")
    print(f"The mode of tenure is {mode}")
    print(f"The standard deviation of tenure is {standard_deviation:0.2f}")
    #print(sorted(tenure_list))
    #remove the blank spaces '\n'
    line = line.strip()
    #prints all the words in the documet
    print()
    