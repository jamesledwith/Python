# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:08:08 2020

@author: James
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:49:37 2020

@author: James
"""
import math
from calculations_functions import calc_mean, calc_sdv

# create empty lists 
gender_list = []
tenure_list = []
phone_services_list = []
internet_service_list = []
contract_list = []
monthly_costs_list = []
total_charges_list = []
churns_list = []

try:
    #open the file
    with open ("Customer_Churn.csv") as file_in:
        header_values = file_in.readline()
        # for every word in 
        for line in file_in:
            #split each line up and into variables seperated by a comma
            gender,tenure,phone_service,internet_service,contract,monthly_costs,total_charges,churn = line.split(",")
            #remove the blank spaces '\n'
            line = line.strip()
            
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
        mean = calc_mean(tenure_list)
    
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
        
        #calculate variance for standard devition
        var = sum(pow(num - tenure_mean, 2) for num in tenure_list) / len(tenure_list)
        #standard deviation of tenure
        standard_deviation = math.sqrt(var)
        
        print(f"The mean tenure is {tenure_mean:0.2f} months")
        print(mean)
        print(f"The minimum tenure is {tenure_min} months")
        print(f"The maximum tenure is {tenure_max} months")
        print(f"The median of tenure is {median} months")
        print(f"The mode of tenure is {mode}")
        print(f"The standard deviation of tenure is {standard_deviation:0.2f}")
        print(f"{calc_sdv(tenure_list, mean):.01f}")
        
        while True:
            #Menu with choices
            choice = int(input("Calculate the following: \n 1:Max \n 2:Min \n 3:Mean \n 4:Median \n 5:Mode \n 6:Standard Deviation \n 7:Quit \n"))
            if choice == 7:
                break
            elif choice ==1:
                print(f"The maximum tenure is {tenure_max} months")
            elif choice ==2:
                print(f"The minimum tenure is {tenure_min} months")
            elif choice ==3:
                print(f"The mean tenure is {tenure_mean:0.2f} months")
                calc_mean(tenure_list)
            elif choice ==4:
                print(f"The median of tenure is {median} months")
            elif choice ==5:
                print(f"The mode of tenure is {mode}")
            elif choice ==6:
                print(f"The standard deviation of tenure is {standard_deviation:0.2f}")
            else:
                print("Please enter a correct value")
      
        # outputed the results to an external file
        with open("FileOutput.txt", "w") as output:
            output.write("The maximum tenure is: " + str(tenure_max) + "\n")
            output.write("The minimum tenure is: " + str(tenure_min) + "\n")
            output.write(f"The mean tenure is:  + {tenure_mean:0.2f} + \n")
            output.write("The median tenure is: " + str(median) + "\n")
            output.write("The mode tenure is: " + str(mode) + "\n")
            output.write("The standard deviation is: " + str(standard_deviation) + "\n")

except FileNotFoundError:
    print("Error Customer_Churn.csv does not exist")  
    print("Error FileOutput.txt does not exist")
    
